#!/usr/bin/env python3
"""Check for broken internal links in articles.

Usage:
    python scripts/check-links.py          # report only
    python scripts/check-links.py --fix    # fix what can be fixed automatically
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = REPO_ROOT / "articles"

INBOX_RE = re.compile(r"\.\./inbox/(raw|used)/([^)]+)")
IMG_RE = re.compile(r'src="(\.\./assets/[^"]+)"')


def find_article_files():
    return list(ARTICLES_DIR.rglob("*.md"))


def build_file_index():
    """Build a map of filename -> list of paths for all files in the repo."""
    index = {}
    for path in REPO_ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            name = path.name
            index.setdefault(name, []).append(path)
    return index


def find_file(filename, file_index):
    """Search for a file by name anywhere in the repo."""
    return file_index.get(filename, [])


def relative_inbox_path(found_path):
    """Convert an absolute path to a ../inbox/... relative path for articles."""
    try:
        rel = found_path.relative_to(REPO_ROOT)
        return f"../{rel.as_posix()}"
    except ValueError:
        return None


def check_links(articles, file_index):
    """Check all internal links and collect broken ones with suggestions."""
    broken = []

    for article in articles:
        text = article.read_text(encoding="utf-8")
        article_rel = article.relative_to(REPO_ROOT)

        # Check inbox links
        for match in INBOX_RE.finditer(text):
            folder, filename = match.group(1), match.group(2)
            full_match = match.group(0)
            target = REPO_ROOT / "inbox" / folder / filename
            if not target.exists():
                candidates = find_file(filename, file_index)
                broken.append({
                    "article": article_rel,
                    "article_path": article,
                    "type": "inbox",
                    "link": full_match,
                    "filename": filename,
                    "candidates": candidates,
                })

        # Check image links
        for match in IMG_RE.finditer(text):
            img_rel = match.group(1)
            resolved = (article.parent / img_rel).resolve()
            if not resolved.exists():
                img_name = Path(img_rel).name
                candidates = find_file(img_name, file_index)
                broken.append({
                    "article": article_rel,
                    "article_path": article,
                    "type": "image",
                    "link": img_rel,
                    "filename": img_name,
                    "candidates": candidates,
                })

    return broken


def report(broken):
    """Print a report of broken links with suggestions."""
    if not broken:
        print("PASSED: All internal links are valid.")
        return

    fixable = [b for b in broken if len(b["candidates"]) == 1]
    unfixable = [b for b in broken if len(b["candidates"]) != 1]

    # Group by unique filename for cleaner output
    seen = {}
    for b in broken:
        key = (b["filename"], b["link"])
        if key not in seen:
            seen[key] = b

    if fixable:
        print(f"## Fixable ({len(fixable)} links - file found elsewhere)\n")
        seen_fixable = {}
        for b in fixable:
            if b["filename"] not in seen_fixable:
                seen_fixable[b["filename"]] = b
        for b in seen_fixable.values():
            found = b["candidates"][0].relative_to(REPO_ROOT).as_posix()
            print(f"  {b['link']}")
            print(f"    -> found at: {found}")
        print()

    if unfixable:
        no_candidates = [b for b in unfixable if len(b["candidates"]) == 0]
        multi = [b for b in unfixable if len(b["candidates"]) > 1]

        if no_candidates:
            print(f"## Not found ({len(no_candidates)} links - file missing)\n")
            seen_missing = {}
            for b in no_candidates:
                if b["filename"] not in seen_missing:
                    seen_missing[b["filename"]] = b
            for b in seen_missing.values():
                articles_using = [
                    x["article"] for x in no_candidates
                    if x["filename"] == b["filename"]
                ]
                print(f"  {b['filename']}")
                for a in sorted(set(str(a) for a in articles_using)):
                    print(f"    in: {a}")
            print()

        if multi:
            print(f"## Ambiguous ({len(multi)} links - multiple matches)\n")
            seen_multi = {}
            for b in multi:
                if b["filename"] not in seen_multi:
                    seen_multi[b["filename"]] = b
            for b in seen_multi.values():
                print(f"  {b['filename']}")
                for c in b["candidates"]:
                    print(f"    -> {c.relative_to(REPO_ROOT).as_posix()}")
            print()

    print(f"## Summary\n")
    print(f"Total broken links: {len(broken)}")
    print(f"Fixable (1 match found): {len(fixable)}")
    print(f"Not found: {len([b for b in broken if len(b['candidates']) == 0])}")
    print(f"Ambiguous (multiple matches): {len([b for b in broken if len(b['candidates']) > 1])}")


def fix(broken):
    """Auto-fix broken links where exactly one candidate exists."""
    fixable = [b for b in broken if len(b["candidates"]) == 1]
    if not fixable:
        print("Nothing to fix automatically.")
        return 0

    # Group fixes by article file
    by_article = {}
    for b in fixable:
        by_article.setdefault(b["article_path"], []).append(b)

    fixed = 0
    for article_path, items in by_article.items():
        text = article_path.read_text(encoding="utf-8")
        for b in items:
            found = b["candidates"][0]
            new_ref = relative_inbox_path(found)
            if new_ref:
                old_ref = b["link"]
                text = text.replace(old_ref, new_ref)
                fixed += 1
        article_path.write_text(text, encoding="utf-8")

    print(f"Fixed {fixed} links across {len(by_article)} articles.")
    return fixed


def main():
    do_fix = "--fix" in sys.argv

    articles = find_article_files()
    print(f"Checking {len(articles)} articles...\n")

    file_index = build_file_index()
    broken = check_links(articles, file_index)

    report(broken)

    if do_fix and broken:
        print()
        fix(broken)

    if broken:
        fixable = len([b for b in broken if len(b["candidates"]) == 1])
        unfixable = len(broken) - fixable
        if not do_fix and fixable > 0:
            print(f"\nRun with --fix to auto-fix {fixable} links.")
        sys.exit(1 if unfixable > 0 else 0)


if __name__ == "__main__":
    main()
