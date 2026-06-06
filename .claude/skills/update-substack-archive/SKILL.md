---
name: update-substack-archive
description: Pull latest Alexey On Data Substack posts and update the local archive files. Use when the user asks to pull latest Substack articles, update the Substack archive, refresh substack.csv, or update articles/substack-archive-index.md.
---

# Update Substack Archive

Update the local lookup index for published posts on `alexeyondata.substack.com`.

## Files

- `articles/substack-archive-index.md`: human-readable archive table with dates, URLs, and searchable descriptions
- `substack.csv`: compact URL/title/description list used by tooling or ad hoc lookup
- `articles/_index.md`: root article index entry for `Substack Archive Index`

## Workflow

1. Run `scripts/update-substack-archive.py missing` to list feed items not yet in the archive.
2. Compare feed URLs against `articles/substack-archive-index.md`.
3. Add only missing posts, newest first.
4. Bump `updated:` in `articles/substack-archive-index.md` to today's date.
5. Update the `Substack Archive Index` row in `articles/_index.md` with the same date.
6. Add the missing posts near the top of `substack.csv`, after the header.
7. Run `scripts/update-substack-archive.py validate`.
8. Check `git diff -- articles/substack-archive-index.md articles/_index.md substack.csv` is scoped to archive updates.

## Description Style

For `articles/substack-archive-index.md`, prefer searchable descriptions over RSS subtitles. Include named tools, libraries, projects, products, and workflows mentioned by the post when known.

For `substack.csv`, use the RSS description unless it is malformed. Keep it compact and CSV-safe.

## Commands

```bash
python scripts/update-substack-archive.py missing
```

```bash
python scripts/update-substack-archive.py validate
```

```bash
python scripts/update-substack-archive.py feed
```
