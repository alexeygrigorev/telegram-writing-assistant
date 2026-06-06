#!/usr/bin/env python3
"""Remove article drafts with their unique source notes and images.

Default mode is a dry run. Pass --delete to apply.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"
ARTICLE_INDEX = ARTICLES_DIR / "_index.md"
INBOX_USED_DIR = ROOT / "inbox" / "used"
IMAGES_DIR = ROOT / "assets" / "images"

SOURCE_EXTENSIONS = {".md", ".txt"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".mp4"}
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
IMG_SRC_RE = re.compile(r"<img\s+[^>]*src=[\"']([^\"']+)[\"']", re.I)


@dataclass(frozen=True)
class RemovalPlan:
    articles: list[Path]
    index_rows: list[str]
    source_notes: list[Path]
    shared_source_notes: list[tuple[str, list[Path]]]
    missing_source_notes: list[str]
    images: list[Path]
    shared_images: list[tuple[Path, list[Path]]]
    missing_images: list[Path]


def repo_path(path: Path) -> Path:
    path = Path(path)
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def all_article_files(excluding: set[Path]) -> list[Path]:
    return [
        p.resolve()
        for p in ARTICLES_DIR.rglob("*.md")
        if p.resolve() not in excluding and p.name != "_index.md"
    ]


def clean_link(raw: str) -> str | None:
    raw = raw.split("#", 1)[0].strip()
    if not raw or raw.startswith(("http://", "https://", "mailto:")):
        return None
    return raw


def article_links(article: Path) -> list[str]:
    text = article.read_text(encoding="utf-8", errors="replace")
    links = []
    for match in LINK_RE.finditer(text):
        raw = clean_link(match.group(1))
        if raw:
            links.append(raw)
    for match in IMG_SRC_RE.finditer(text):
        raw = clean_link(match.group(1))
        if raw:
            links.append(raw)
    return links


def inventory_inbox_by_name() -> dict[str, Path]:
    if not INBOX_USED_DIR.exists():
        return {}
    return {p.name: p.resolve() for p in INBOX_USED_DIR.rglob("*") if p.is_file()}


def remaining_article_texts(excluding: set[Path]) -> dict[Path, str]:
    return {
        p: p.read_text(encoding="utf-8", errors="replace")
        for p in all_article_files(excluding)
    }


def users_by_name(name: str, texts: dict[Path, str]) -> list[Path]:
    return [path for path, text in texts.items() if name in text]


def users_by_path(path: Path, texts: dict[Path, str]) -> list[Path]:
    keys = {path.name}
    try:
        keys.add(path.relative_to(ROOT).as_posix())
    except ValueError:
        pass
    return [article for article, text in texts.items() if any(key in text for key in keys)]


def find_index_rows(articles: list[Path]) -> list[str]:
    if not ARTICLE_INDEX.exists():
        return []
    rels = {article.relative_to(ARTICLES_DIR).as_posix() for article in articles}
    rows = []
    for line in ARTICLE_INDEX.read_text(encoding="utf-8").splitlines():
        if any(f"]({rel})" in line for rel in rels):
            rows.append(line)
    return rows


def build_plan(article_paths: list[Path]) -> RemovalPlan:
    articles = [repo_path(path) for path in article_paths]
    missing_articles = [path for path in articles if not path.exists()]
    if missing_articles:
        missing = "\n".join(display_path(path) for path in missing_articles)
        raise SystemExit(f"Article file(s) not found:\n{missing}")

    excluding = set(articles)
    texts = remaining_article_texts(excluding)
    inbox_by_name = inventory_inbox_by_name()

    source_names: set[str] = set()
    image_paths: set[Path] = set()
    missing_images: set[Path] = set()

    for article in articles:
        for raw in article_links(article):
            resolved = (article.parent / raw).resolve()
            suffix = Path(raw).suffix.lower()

            if "inbox/" in raw or "inbox/" in resolved.as_posix():
                if suffix in SOURCE_EXTENSIONS:
                    source_names.add(Path(raw).name)
            elif "assets/images/" in raw or "assets/images/" in resolved.as_posix():
                if suffix in IMAGE_EXTENSIONS:
                    if resolved.exists():
                        image_paths.add(resolved)
                    else:
                        missing_images.add(resolved)

    source_notes: list[Path] = []
    shared_source_notes: list[tuple[str, list[Path]]] = []
    missing_source_notes: list[str] = []
    for name in sorted(source_names):
        users = users_by_name(name, texts)
        path = inbox_by_name.get(name)
        if users:
            shared_source_notes.append((name, users))
        elif path:
            source_notes.append(path)
        else:
            missing_source_notes.append(name)

    images: list[Path] = []
    shared_images: list[tuple[Path, list[Path]]] = []
    for path in sorted(image_paths):
        users = users_by_path(path, texts)
        if users:
            shared_images.append((path, users))
        else:
            images.append(path)

    return RemovalPlan(
        articles=articles,
        index_rows=find_index_rows(articles),
        source_notes=source_notes,
        shared_source_notes=shared_source_notes,
        missing_source_notes=missing_source_notes,
        images=images,
        shared_images=shared_images,
        missing_images=sorted(missing_images),
    )


def print_plan(plan: RemovalPlan) -> None:
    print("Articles to delete:")
    for path in plan.articles:
        print(f"  {display_path(path)}")

    print(f"\n_index.md rows to remove: {len(plan.index_rows)}")
    for row in plan.index_rows:
        print(f"  {row}")

    print(f"\nUnique source notes to delete: {len(plan.source_notes)}")
    for path in plan.source_notes:
        print(f"  {display_path(path)}")

    print(f"\nUnique images to delete: {len(plan.images)}")
    for path in plan.images:
        print(f"  {display_path(path)}")

    print(f"\nShared source notes kept: {len(plan.shared_source_notes)}")
    for name, users in plan.shared_source_notes:
        user_list = ", ".join(display_path(user) for user in users)
        print(f"  {name}: {user_list}")

    print(f"\nShared images kept: {len(plan.shared_images)}")
    for path, users in plan.shared_images:
        user_list = ", ".join(display_path(user) for user in users)
        print(f"  {display_path(path)}: {user_list}")

    print(f"\nMissing source notes ignored: {len(plan.missing_source_notes)}")
    for name in plan.missing_source_notes:
        print(f"  {name}")

    print(f"\nMissing images ignored: {len(plan.missing_images)}")
    for path in plan.missing_images:
        print(f"  {display_path(path)}")


def remove_index_rows(plan: RemovalPlan) -> None:
    if not plan.index_rows or not ARTICLE_INDEX.exists():
        return
    remove = set(plan.index_rows)
    lines = ARTICLE_INDEX.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if line not in remove]
    ARTICLE_INDEX.write_text("\n".join(kept) + "\n", encoding="utf-8")


def cleanup_empty_image_dirs() -> int:
    removed = 0
    if not IMAGES_DIR.exists():
        return removed
    for path in sorted((p for p in IMAGES_DIR.rglob("*") if p.is_dir()), reverse=True):
        if path.name == "_unused":
            continue
        remaining = [child for child in path.iterdir() if child.name != ".gitkeep"]
        if not remaining:
            for child in path.iterdir():
                child.unlink()
            path.rmdir()
            removed += 1
    return removed


def apply_plan(plan: RemovalPlan) -> None:
    for path in plan.source_notes + plan.images + plan.articles:
        if path.exists():
            path.unlink()
    remove_index_rows(plan)
    removed_dirs = cleanup_empty_image_dirs()
    total = len(plan.source_notes) + len(plan.images) + len(plan.articles)
    print(f"Deleted {total} files.")
    if removed_dirs:
        print(f"Removed {removed_dirs} empty image directories.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("articles", nargs="+", help="Article markdown files to remove")
    parser.add_argument("--delete", action="store_true", help="Apply deletion; default is dry run")
    args = parser.parse_args()

    plan = build_plan([Path(path) for path in args.articles])
    print_plan(plan)

    if not args.delete:
        total = len(plan.articles) + len(plan.source_notes) + len(plan.images)
        print(f"\nDry run: {total} files would be deleted.")
        print("Run again with --delete to apply.")
        return 0

    print("\nDeleting files...")
    apply_plan(plan)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
