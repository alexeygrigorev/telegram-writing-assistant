---
title: "Processing Pipeline"
created: 2026-01-16
updated: 2026-01-16
tags: [automation, pipeline, claude, git]
status: draft
---

# Processing Pipeline

Automation workflow for organizing materials into articles.

## Command Structure

The /process command is defined as a slash command that Claude reads and executes. Instructions are given via voice notes, then Claude reads them and creates the command file.

## Processing Steps

1. Check inbox/raw/ for uncommitted materials
2. Read all new files
3. Read existing articles from articles/ folder
4. For each material:
   - Translate to English if needed
   - Check image context by examining messages before and after by timestamp
   - Decide if material belongs to existing article or requires new one
   - Append content to appropriate article
5. Update articles/_index.md with new articles
6. Move processed files from inbox/raw/ to inbox/used/
7. Only transcripts remain, no .ogg files

## Image Processing

Images are saved with a markdown file that references them. The bot uses image-to-text to describe contents. Grok's image capabilities are tried first, falling back to OpenAI if needed. Description is sent back to the chat for immediate feedback.

For context awareness, look at messages sent before and after by timestamp to understand what the image relates to.

## Styling Guidelines

Articles are in English only. No bold formatting. No --- section separators. Use short, clear sentences. Break up long sentences. Be a curator, not a writer. Organize findings without rewriting.

## Source Tracking

Each article section lists sources with relative paths to transcripts and images.

## Git Workflow

Claude does git add and git commit with a descriptive message. A Python script handles git push and sends the GitHub commit link back to chat. The link is clickable for easy access to view changes.

## Instructions Reference

The processing instructions reference a summary file which describes what to do. The process command should be updated based on feedback from that summary file.

## Sources

- [20260116_211210_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211210_AlexeyDTC_transcript.txt)
- [20260116_211314_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211314_AlexeyDTC_transcript.txt)
- [20260116_211932_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211932_AlexeyDTC_transcript.txt)
- [20260116_212036_AlexeyDTC_transcript.txt](../inbox/raw/20260116_212036_AlexeyDTC_transcript.txt)
- [20260116_212800_AlexeyDTC_transcript.txt](../inbox/raw/20260116_212800_AlexeyDTC_transcript.txt)
- [20260116_213629_AlexeyDTC_transcript.txt](../inbox/raw/20260116_213629_AlexeyDTC_transcript.txt)
- [20260116_211757_AlexeyDTC_photo.md](../inbox/raw/20260116_211757_AlexeyDTC_photo.md)
- [20260116_213322_AlexeyDTC_photo.md](../inbox/raw/20260116_213322_AlexeyDTC_photo.md)
