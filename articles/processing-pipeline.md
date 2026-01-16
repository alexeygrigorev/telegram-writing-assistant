---
title: "Processing Pipeline"
created: 2026-01-16
updated: 2026-01-16
tags: [processing, pipeline, automation, git]
status: draft
---

# Processing Pipeline

The processing command organizes accumulated materials into articles.

## Input

Check inbox/raw/ for new materials including text, transcripts, and photos.

## Processing Steps

1. Read all files in inbox/raw/
2. Read existing articles from articles/ folder
3. Read articles/_index.md to understand what articles exist
4. For each material:
   - Translate to English if needed
   - Consider context for images by looking at messages before and after
   - Decide whether to add to existing article or create new one
   - Check each existing article's title and content for relevance
   - If no match, create a new article
   - Append content to the appropriate article
5. Update articles/_index.md with any new articles

## Article Styling

- Language: English only
- No bold formatting
- No --- section separators
- Use short, clear sentences
- Act as a curator, not a writer
- Preserve original meaning

## Frontmatter Format

```markdown
---
title: "Article Title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
status: draft
---
```

## Source Tracking

Each article section must list sources:

```markdown
## Sources
- [transcript filename](../inbox/raw/filename)
- [image filename](../assets/images/filename)
```

## Cleanup

After processing:
1. Move all processed files from inbox/raw/ to inbox/used/
2. Delete .ogg files, keep only transcripts

## Git Workflow

Claude handles git add and commit with a descriptive message. Python script handles git push and sends the GitHub commit link back to chat. The link is clickable for easy access.

## Image Processing

When an image is received, create a markdown file that references it. Use Grok's image-to-text capabilities or OpenAI if needed. Send the image description back to the chat.

## Error Handling

When an exception occurs during bot processing, output the error details to the chat for immediate debugging.

## Sources
- [20260116_211210_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211210_AlexeyDTC_transcript.txt)
- [20260116_211314_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211314_AlexeyDTC_transcript.txt)
- [20260116_211501_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211501_AlexeyDTC_transcript.txt)
- [20260116_211757_AlexeyDTC_photo.md](../inbox/raw/20260116_211757_AlexeyDTC_photo.md)
- [20260116_211932_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211932_AlexeyDTC_transcript.txt)
- [20260116_212036_AlexeyDTC_transcript.txt](../inbox/raw/20260116_212036_AlexeyDTC_transcript.txt)
- [20260116_212800_AlexeyDTC_transcript.txt](../inbox/raw/20260116_212800_AlexeyDTC_transcript.txt)
- [20260116_213156_AlexeyDTC_transcript.txt](../inbox/raw/20260116_213156_AlexeyDTC_transcript.txt)
- [20260116_213629_AlexeyDTC_transcript.txt](../inbox/raw/20260116_213629_AlexeyDTC_transcript.txt)
- [20260116_213322_AlexeyDTC_photo.md](../inbox/raw/20260116_213322_AlexeyDTC_photo.md)
