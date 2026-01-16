---
title: "Processing Pipeline"
created: 2026-01-16
updated: 2026-01-16
tags: [automation, claude-code, processing, github]
status: draft
---

# Processing Pipeline

The automation workflow for organizing materials from Telegram into articles using the /process command.

## How It Works

I want to write this agent using voice messages. I give instructions via voice, then on the computer, on the laptop, I ask Claude to read these instructions and enter all these instructions into a slash command. Based on this slash command, the command will be called every time I do slash-process in Telegram.

The idea of the slash-process command is that I do a brain dump of everything I have. Usually, one way or another, it relates to one article. I run process, it looks at everything that is not committed in git, looks at what is there, and processes it.

## Processing Steps

<figure>
  <img src="../assets/images/processing-pipeline/processing-requirements-list.jpg" alt="Processing requirements list">
  <figcaption>Terminal output showing the processing requirements derived from voice notes</figcaption>
  <!-- This illustrates the actual requirements being implemented in the code -->
</figure>

1. Check inbox/raw/ for uncommitted materials
2. Read all files in the raw folder
3. For each text/transcript material:
   - Translate to English if needed
   - Decide: existing article OR new article
   - Check each existing article's title and content
   - If no match, create a new article
   - Incorporate content into the right section

4. For each photo in inbox/raw/:
   - Read its markdown description file (this is the ONLY source for image content)
   - Look at messages before/after by timestamp for context
   - Find the most relevant section and add the image
   - Move image from inbox/raw/ to assets/images/{article_name}/
   - Move markdown description file to inbox/used/

5. After processing:
   - Move all processed files from inbox/raw/ to inbox/used/
   - Only transcripts remain (no .ogg files)

## Git Workflow

Claude does git add and git commit with a normal description. The push is done from the Python script. The script takes the hash and sends a GitHub link to the chat. It should be clickable so I can click and view the commit link on GitHub.

<figure>
  <img src="../assets/images/processing-pipeline/changelog-development-progress.jpg" alt="Development progress changelog">
  <figcaption>Terminal showing a summary of changes during development</figcaption>
  <!-- This shows development progress on the processing pipeline -->
</figure>

## Error Handling

When some exception occurs during bot processing, write the exception to the chat. That way we can debug immediately.

## Image Processing Guidelines

Images are processed using ONLY the markdown description file, NOT vision/analyze_image tools. The markdown file contains Type, Content, Text, and Context. To understand where an image best fits, look at the context by checking messages before and after by timestamp - what text information is around.

## Styling Guidelines

Articles should follow these formatting rules:
- Language: English only
- No bold formatting (no **text**)
- No --- section separators
- Use short, clear sentences - break up long sentences
- We are a curator, not a writer - organize findings, don't rewrite
- Preserve original meaning and all details from voice notes

Each article section must list sources at the end.

## Sources
- [20260116_211210_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211210_AlexeyDTC_transcript.txt)
- [20260116_211314_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211314_AlexeyDTC_transcript.txt)
- [20260116_211932_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211932_AlexeyDTC_transcript.txt)
- [20260116_212036_AlexeyDTC_transcript.txt](../inbox/raw/20260116_212036_AlexeyDTC_transcript.txt)
- [20260116_212800_AlexeyDTC_transcript.txt](../inbox/raw/20260116_212800_AlexeyDTC_transcript.txt)
- [20260116_213156_AlexeyDTC_transcript.txt](../inbox/raw/20260116_213156_AlexeyDTC_transcript.txt)
- [20260116_213629_AlexeyDTC_transcript.txt](../inbox/raw/20260116_213629_AlexeyDTC_transcript.txt)
- [20260116_220451_AlexeyDTC_transcript.txt](../inbox/raw/20260116_220451_AlexeyDTC_transcript.txt)
- [20260116_211757_AlexeyDTC_photo.md](../inbox/used/20260116_211757_AlexeyDTC_photo.md)
- [20260116_213322_AlexeyDTC_photo.md](../inbox/used/20260116_213322_AlexeyDTC_photo.md)
