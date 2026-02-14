#!/usr/bin/env python3
"""Check for broken internal links in articles.

Usage: python scripts/check-links.py
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


def check_inbox_links(articles):
    errors = []
    raw_links = []
    missing_used = []

    for article in articles:
        text = article.read_text(encoding="utf-8")
        for match in INBOX_RE.finditer(text):
            folder, filename = match.group(1), match.group(2)
            if folder == "raw":
                raw_links.append((article.relative_to(REPO_ROOT), filename))
            elif folder == "used":
                target = REPO_ROOT / "inbox" / "used" / filename
                if not target.exists():
                    missing_used.append(
                        (article.relative_to(REPO_ROOT), filename)
                    )

    print("## Inbox References\n")

    if raw_links:
        print(
            f"ERROR: {len(raw_links)} links point to inbox/raw/ "
            f"(should be inbox/used/):"
        )
        for article, filename in raw_links[:20]:
            print(f"  {filename} (in {article})")
        errors.extend(raw_links)
        print()

    if missing_used:
        print("Missing inbox/used files:")
        seen = set()
        for article, filename in missing_used:
            if filename not in seen:
                seen.add(filename)
                print(f"  {filename}")
        print(f"\nTotal missing inbox files: {len(seen)}")
        errors.extend(missing_used)
    elif not raw_links:
        print("All inbox references point to existing files.")

    return errors


def check_image_links(articles):
    errors = []
    missing = []

    for article in articles:
        text = article.read_text(encoding="utf-8")
        for match in IMG_RE.finditer(text):
            img_rel = match.group(1)
            resolved = (article.parent / img_rel).resolve()
            if not resolved.exists():
                missing.append(
                    (article.relative_to(REPO_ROOT), img_rel)
                )

    print("## Image References\n")

    if missing:
        print("Missing image files:")
        for article, img_path in missing:
            print(f"  {img_path} (in {article})")
        print(f"\nTotal missing images: {len(missing)}")
        errors.extend(missing)
    else:
        print("All image references point to existing files.")

    return errors


def main():
    articles = find_article_files()
    print(f"Checking internal links in {len(articles)} articles...\n")

    inbox_errors = check_inbox_links(articles)
    print()
    image_errors = check_image_links(articles)
    print()

    total_errors = len(inbox_errors) + len(image_errors)

    print("## Summary\n")
    print(f"Articles checked: {len(articles)}")
    print(f"Errors: {total_errors}")
    print()

    if total_errors > 0:
        print(f"FAILED: {total_errors} broken links found.")
        sys.exit(1)
    else:
        print("PASSED: All internal links are valid.")


if __name__ == "__main__":
    main()
