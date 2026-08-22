---
name: update-substack-archive
description: Pull latest Alexey On Data Substack posts and update the local archive files. Use when the user asks to pull latest Substack articles, update the Substack archive, refresh substack.csv, or update articles/_substack-archive-index.md.
---

# Update Substack Archive

Update the local lookup index and full-text reference archive for published posts on [aishippingblog.com](https://aishippingblog.com) (the AI Shipping Blog newsletter, formerly `alexeyondata.substack.com`).

## Files

- `articles/_substack-archive-index.md`: human-readable archive table with dates, URLs, and searchable descriptions
- `substack.csv`: compact URL/title/description list used by tooling or ad hoc lookup
- `articles/_index.md`: root article index entry for `Substack Archive Index`
- `reference/substack/{date}-{slug}.md`: full text of every published post, re-fetched from the live page so real `##`/`###` headings are preserved (not just the RSS description). Use this whenever you need to quote, summarize, or check the exact wording of something already published, or to check whether a draft in `articles/` duplicates a post that already went out.

## Workflow

1. Run `scripts/update-substack-archive.py missing` to list feed items not yet in the archive.
2. Compare feed URLs against `articles/_substack-archive-index.md`.
3. Add only missing posts, newest first.
4. Bump `updated:` in `articles/_substack-archive-index.md` to today's date.
5. Update the `Substack Archive Index` row in `articles/_index.md` with the same date.
6. Add the missing posts near the top of `substack.csv`, after the header.
7. Run `scripts/update-substack-archive.py validate`.
8. Run `scripts/update-substack-archive.py reference-sync` to fetch full text for any newly-added rows into `reference/substack/`.
9. Check `git diff -- articles/_substack-archive-index.md articles/_index.md substack.csv reference/substack` is scoped to archive updates.

## Description Style

For `articles/_substack-archive-index.md`, prefer searchable descriptions over RSS subtitles. Include named tools, libraries, projects, products, and workflows mentioned by the post when known.

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

```bash
python scripts/update-substack-archive.py reference-sync
```

`reference-sync` only fetches rows missing a `reference/substack/*.md` file. Pass `--force` to re-fetch and overwrite everything (e.g. after a conversion-quality fix).
