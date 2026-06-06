---
name: cleanup-articles
description: Clean up published or removed article drafts and orphaned assets in this repository. Use when the user asks to delete published articles, remove an article with its source notes and images, clean unused notes/images, or run orphan cleanup.
---

# Cleanup Articles

Use this for repository hygiene after articles are published or removed.

## Scripts

- `scripts/remove-articles.py`: targeted removal for specific article drafts. It deletes the article files, their rows in `articles/_index.md`, and only the source notes/images that are not referenced by remaining articles.
- `scripts/cleanup.py`: global orphan cleanup. It scans all remaining articles and deletes inbox files/images that are not referenced anywhere.
- `scripts/check-links.py`: validation for broken internal article links.

## Remove Published Articles

1. Confirm the article drafts are already published, usually via `articles/substack-archive-index.md`.
2. Run a dry run:

```bash
python scripts/remove-articles.py articles/path-one.md articles/path-two.md
```

3. Review:
   - article files to delete
   - `_index.md` rows to remove
   - unique source notes to delete
   - unique images to delete
   - shared notes/images kept
   - missing notes/images ignored
4. Ask the user for confirmation before deleting.
5. Apply:

```bash
python scripts/remove-articles.py articles/path-one.md articles/path-two.md --delete
```

6. Replace links from remaining articles to deleted local drafts with the published Substack URLs.

## Clean All Orphans

Run a dry run first:

```bash
python scripts/cleanup.py --mode full
```

Apply only after the user confirms:

```bash
python scripts/cleanup.py --mode full --delete
```

For a more conservative cleanup:

```bash
python scripts/cleanup.py --mode full --older-than 30 --delete
```

## Validate

Run:

```bash
python scripts/cleanup.py --mode full
python scripts/check-links.py
```

`cleanup.py` should report zero orphaned inbox and image files after a full cleanup. `check-links.py` may still report pre-existing missing source links; distinguish those from links introduced by the cleanup.

## Rules

- Do not delete `inbox/summaries/*`; those are processing reports, not article source notes.
- Do not delete source notes or images that are referenced by any remaining article.
- Do not delete assets in `assets/images/_unused/` through this workflow; `cleanup.py` intentionally skips that directory.
- Never use broad shell globs for deletion. Use the scripts so shared references are checked first.
