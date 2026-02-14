#!/usr/bin/env python3
"""Find and remove orphaned inbox files and images not referenced by any article."""

import argparse
import os
import re
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"
INBOX_USED_DIR = ROOT / "inbox" / "used"
IMAGES_DIR = ROOT / "assets" / "images"

# Patterns to extract references from markdown files
INBOX_RE = re.compile(r"inbox/(?:used|raw)/([^)\"\s]+)")
IMAGE_RE = re.compile(r"assets/images/([^)\"\s]+)")


def collect_article_paths():
    """Return all article .md files (skip _index.md)."""
    paths = []
    for dirpath, _dirnames, filenames in os.walk(ARTICLES_DIR):
        for fname in filenames:
            if fname.endswith(".md") and fname != "_index.md":
                paths.append(Path(dirpath) / fname)
    return paths


def extract_references(article_paths):
    """Scan articles and return sets of referenced inbox basenames and image relative paths."""
    inbox_refs = set()
    image_refs = set()

    for path in article_paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        for m in INBOX_RE.finditer(text):
            # Normalize to basename (all files live in inbox/used/)
            inbox_refs.add(Path(m.group(1)).name)
        for m in IMAGE_RE.finditer(text):
            # Keep as subdir/filename relative to assets/images/
            image_refs.add(m.group(1))

    return inbox_refs, image_refs


def inventory_inbox():
    """List all files in inbox/used/ excluding feedback/ subdirectory and .gitkeep."""
    files = []
    if not INBOX_USED_DIR.exists():
        return files
    for f in INBOX_USED_DIR.iterdir():
        if f.is_dir():
            continue  # skip feedback/ and any other subdirs
        if f.name == ".gitkeep":
            continue
        files.append(f)
    return files


def inventory_images():
    """List all files in assets/images/*/ excluding _unused/ directory and .gitkeep."""
    files = []
    if not IMAGES_DIR.exists():
        return files
    for dirpath, dirnames, filenames in os.walk(IMAGES_DIR):
        # Skip _unused directory
        dirnames[:] = [d for d in dirnames if d != "_unused"]
        rel = Path(dirpath).relative_to(IMAGES_DIR)
        for fname in filenames:
            if fname == ".gitkeep":
                continue
            files.append(Path(dirpath) / fname)
    return files


def image_rel_key(image_path):
    """Return subdir/filename relative to assets/images/."""
    return str(image_path.relative_to(IMAGES_DIR)).replace("\\", "/")


def file_age_days(path):
    """Return the age of a file in days based on mtime."""
    return (time.time() - path.stat().st_mtime) / 86400


def file_size_human(path):
    """Return human-readable file size."""
    size = path.stat().st_size
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def find_orphans_full(older_than_days=None):
    """Full scan: find all orphaned inbox and image files."""
    article_paths = collect_article_paths()
    inbox_refs, image_refs = extract_references(article_paths)

    # Orphaned inbox files
    inbox_files = inventory_inbox()
    orphaned_inbox = []
    for f in inbox_files:
        if f.name not in inbox_refs:
            if older_than_days is not None and file_age_days(f) < older_than_days:
                continue
            orphaned_inbox.append(f)

    # Orphaned image files
    image_files = inventory_images()
    orphaned_images = []
    for f in image_files:
        key = image_rel_key(f)
        if key not in image_refs:
            if older_than_days is not None and file_age_days(f) < older_than_days:
                continue
            orphaned_images.append(f)

    return orphaned_inbox, orphaned_images, inbox_refs, image_refs


def find_orphans_git(since="HEAD~10", older_than_days=None):
    """Git mode: find files that became orphaned due to recent article deletions/modifications."""
    # Find deleted or modified article files in recent history
    try:
        result = subprocess.run(
            ["git", "log", "--diff-filter=D", "--name-only", "--pretty=format:", since + "..HEAD", "--", "articles/"],
            capture_output=True, text=True, cwd=ROOT,
        )
        deleted_files = [l.strip() for l in result.stdout.splitlines() if l.strip()]
    except Exception as e:
        print(f"Warning: git log failed: {e}")
        deleted_files = []

    if not deleted_files:
        print(f"No deleted articles found since {since}.")
        print("Falling back to full scan.\n")

    # Always do a full reference scan to confirm orphan status
    orphaned_inbox, orphaned_images, inbox_refs, image_refs = find_orphans_full(older_than_days)

    if deleted_files:
        # Extract references from deleted articles via git show
        candidate_inbox = set()
        candidate_images = set()
        for fpath in deleted_files:
            try:
                result = subprocess.run(
                    ["git", "show", f"{since}:{fpath}"],
                    capture_output=True, text=True, cwd=ROOT,
                )
                if result.returncode == 0:
                    text = result.stdout
                    for m in INBOX_RE.finditer(text):
                        candidate_inbox.add(Path(m.group(1)).name)
                    for m in IMAGE_RE.finditer(text):
                        candidate_images.add(m.group(1))
            except Exception:
                pass

        # Filter orphans to only those that were referenced by deleted articles
        orphaned_inbox = [f for f in orphaned_inbox if f.name in candidate_inbox]
        orphaned_images = [f for f in orphaned_images if image_rel_key(f) in candidate_images]

    return orphaned_inbox, orphaned_images, inbox_refs, image_refs


def print_report(orphaned_inbox, orphaned_images, inbox_refs, image_refs):
    """Print categorized report of orphaned files."""
    total_size = 0

    print("=" * 70)
    print("ORPHAN CLEANUP REPORT")
    print("=" * 70)
    print()

    # Stats
    inbox_total = len(inventory_inbox())
    images_total = len(inventory_images())
    print(f"Articles scanned:        {len(collect_article_paths())}")
    print(f"Inbox refs found:        {len(inbox_refs)}")
    print(f"Image refs found:        {len(image_refs)}")
    print(f"Inbox files on disk:     {inbox_total}")
    print(f"Image files on disk:     {images_total}")
    print()

    # Orphaned inbox files
    print(f"Orphaned inbox files:    {len(orphaned_inbox)}")
    if orphaned_inbox:
        inbox_size = sum(f.stat().st_size for f in orphaned_inbox)
        total_size += inbox_size
        print(f"  Total size:            {_human_size(inbox_size)}")
        print()
        for f in sorted(orphaned_inbox, key=lambda p: p.name):
            age = file_age_days(f)
            print(f"  {f.name}  ({file_size_human(f)}, {age:.0f}d old)")
    print()

    # Orphaned images
    print(f"Orphaned image files:    {len(orphaned_images)}")
    if orphaned_images:
        img_size = sum(f.stat().st_size for f in orphaned_images)
        total_size += img_size
        print(f"  Total size:            {_human_size(img_size)}")
        print()
        # Group by subdirectory
        by_dir = {}
        for f in sorted(orphaned_images, key=lambda p: str(p)):
            subdir = f.parent.name
            by_dir.setdefault(subdir, []).append(f)
        for subdir, files in sorted(by_dir.items()):
            print(f"  [{subdir}/]")
            for f in files:
                age = file_age_days(f)
                print(f"    {f.name}  ({file_size_human(f)}, {age:.0f}d old)")
    print()

    print(f"Total reclaimable space: {_human_size(total_size)}")
    print()


def _human_size(size_bytes):
    """Convert bytes to human-readable size."""
    for unit in ("B", "KB", "MB", "GB"):
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def delete_files(orphaned_inbox, orphaned_images):
    """Delete orphaned files and clean up empty directories."""
    deleted = 0
    errors = 0

    for f in orphaned_inbox + orphaned_images:
        try:
            f.unlink()
            deleted += 1
        except Exception as e:
            print(f"  Error deleting {f}: {e}")
            errors += 1

    # Clean up empty subdirectories in assets/images/ (bottom-up)
    cleaned_dirs = 0
    if IMAGES_DIR.exists():
        for dirpath, dirnames, filenames in os.walk(IMAGES_DIR, topdown=False):
            p = Path(dirpath)
            if p == IMAGES_DIR:
                continue
            if p.name == "_unused":
                continue
            # Check if directory is empty (or only has .gitkeep)
            remaining = [f for f in p.iterdir() if f.name != ".gitkeep"]
            if not remaining:
                # Remove .gitkeep too if it's the only thing left
                for f in p.iterdir():
                    f.unlink()
                p.rmdir()
                cleaned_dirs += 1

    print(f"Deleted {deleted} files ({errors} errors)")
    if cleaned_dirs:
        print(f"Removed {cleaned_dirs} empty directories")


def main():
    parser = argparse.ArgumentParser(
        description="Find and remove orphaned inbox files and images not referenced by any article.",
    )
    parser.add_argument(
        "--mode", choices=["full", "git"], default="full",
        help="Scan mode: 'full' scans all articles (default), 'git' focuses on recently orphaned files",
    )
    parser.add_argument(
        "--since", default="HEAD~10",
        help="Git ref for git mode (default: HEAD~10)",
    )
    parser.add_argument(
        "--older-than", type=int, default=None, metavar="DAYS",
        help="Only target files with mtime older than N days",
    )
    parser.add_argument(
        "--delete", action="store_true",
        help="Actually delete orphaned files (default is dry-run report)",
    )
    args = parser.parse_args()

    if args.mode == "git":
        orphaned_inbox, orphaned_images, inbox_refs, image_refs = find_orphans_git(
            since=args.since, older_than_days=args.older_than,
        )
    else:
        orphaned_inbox, orphaned_images, inbox_refs, image_refs = find_orphans_full(
            older_than_days=args.older_than,
        )

    print_report(orphaned_inbox, orphaned_images, inbox_refs, image_refs)

    if not orphaned_inbox and not orphaned_images:
        print("Nothing to clean up.")
        return

    if args.delete:
        print("Deleting orphaned files...")
        delete_files(orphaned_inbox, orphaned_images)
    else:
        total = len(orphaned_inbox) + len(orphaned_images)
        print(f"Dry run: {total} files would be deleted.")
        print("Run with --delete to actually remove them.")


if __name__ == "__main__":
    main()
