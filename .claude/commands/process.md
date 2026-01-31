---
description: Process Telegram inbox materials and update articles
---

You are processing materials from the Telegram writing assistant inbox. Your goal is to organize thoughts into articles.

# IMPORTANT - START WITH GIT PULL

Before processing anything, ALWAYS run:
```bash
git pull
```

If there are merge conflicts, resolve them by keeping the most recent and correct version before proceeding with any processing.

# INPUT

Check `inbox/raw/` for new materials (text, transcripts, photos).

# PROCESSING ORDER

Process in TWO phases:

## Phase 1: Text Content

1. Read all files in `inbox/raw/`

2. Read existing articles from `articles/` folder (excluding `_index.md`)

3. Read `articles/_index.md` to understand what articles exist

4. For each text/transcript material:

   Understanding context

   If a message is short or unclear:
   - Look at nearby messages by timestamp (within 1-2 minutes)
   - Check frontmatter date field for related messages
   - Read related voice notes, text, and photos together

   Handling URLs

   If a message contains a URL, fetch its content using Jina Reader:
   ```bash
   curl "https://r.jina.ai/{original_url}"
   ```
   Then incorporate that content into the appropriate article.

   If a URL is marked as "resource" or is an orphaned link (a link sent without context that doesn't relate to nearby messages), add it to the "Interesting Resources" article (interesting-resources.md).

   Final processing

   - Translate to English if needed
   - Preserve key information: some summarization is fine, but keep core ideas and details
   - Apply the grouping rules below to choose the article
   - Incorporate content meaningfully in the right section

## Phase 2: Images (only after Phase 1 is complete)

1. Images are located in `inbox/raw/` alongside their markdown description files (frontmatter contains `image_file: filename.jpg`)

2. For each photo in `inbox/raw/`:
   - Read its markdown description file (contains Type, Content, Text, Context) - this is the ONLY source for image content, DO NOT use any vision/analyze_image tools
   - Look at messages sent before/after by timestamp for context
   - If articles exist: Find the most relevant section and add the image
   - If no articles exist yet: Defer the image

3. When placing an image in an article:
   - Rename the image to a descriptive name based on its content (e.g., `project-summary-slide.jpg`, `terminal-install-groq.jpg`, `claude-process-command.jpg`)
   - Move the image from `inbox/raw/` to `assets/images/{article_name}/` (create folder if needed)
   - Update image reference in article to point to new location with new filename
   - Update the markdown description file in `inbox/used/` with new frontmatter fields:
     - `original_image: TIMESTAMP_USERNAME.jpg`
     - `final_location: ../assets/images/{article_name}/descriptive-name.jpg`
   - Move the markdown description file to `inbox/used/`

4. Finding the RIGHT location for an image within an article:
   - Use timestamp as primary signal: Look at the image's date from frontmatter and find text content that was created around the same time
   - Use context: Read the image description (Type, Content, Text, Context) to understand what the image shows
   - Find related section: Search the article for content that matches the image's subject matter
   - Place strategically: Insert the figure NEAR the relevant text, not at the end. The text around should relate to what's in the image
   - Example: If image shows a terminal screenshot of installing a dependency, place it near the section about setup/dependencies, not at the end

5. If image cannot be placed:
   - Move the image to `assets/images/_unused/` (create folder if needed)
   - Move the markdown description file to `inbox/used/`

6. Image placement format in articles:
```html
<figure>
  <img src="../assets/images/{article_name}/descriptive-name.jpg" alt="Image description">
  <figcaption>Short caption - what's on the image</figcaption>
  <!-- how and why this illustration is relevant to the text around -->
</figure>
```

7. Track which images were placed and which were deferred

# COURSE NAMING CONVENTIONS

IMPORTANT: These are DIFFERENT courses and must be kept separate:

- AI Buildcamp (one word, lowercase c) - formerly "AI Bootcamp", now "AI Engineering Buildcamp"
- ML Zoomcamp (one word, lowercase c) - Machine Learning Zoomcamp
- Data Engineering Zoomcamp (one word, lowercase c) - Data Engineering Zoomcamp
- AI Dev Tools Zoomcamp (one word, lowercase c) - Development tools and workflows

When processing course-related content:
- Identify WHICH course the content refers to
- Content for different courses goes to DIFFERENT articles
- Do not mix course content even if related (e.g., ML Zoomcamp success stories should NOT be in AI Buildcamp article)
- Each course gets its own dedicated article
- Different aspects of the same course should also be separate articles (e.g., course structure, success stories, logistics)

# TRANSCRIPTION QUALITY NOTE

Most text content comes from transcribed voice messages. When processing:
- Expect typos, missing words, and recognition errors
- Use context to infer intended meaning
- Fix obvious errors but preserve original meaning
- When in doubt, keep the original wording

# GROUPING RULES

CORE PRINCIPLE: Each article must have ONE clear topic. Do not mix unrelated content even if messages were sent around the same time.

## When to group messages together

Messages should be grouped together ONLY when BOTH conditions are met:
- Sent around the same time (within 1-2 minutes)
- Thematically related (same topic, same article context)

If messages sent together are about different topics, create SEPARATE articles.

## Where content goes

Read all existing articles first. For each piece of content, ask:

- Does this content extend an existing article's topic?
- Would a reader of that article expect to find this information?

If yes, add it there. If no article matches, create a new one.

Each article should have a single, clear focus. Don't force unrelated content into an existing article just because it exists.

## New or existing article

Create a NEW article when:
- No existing article covers the topic
- Content is about a fundamentally different subject
- Adding it would dilute the focus of existing articles

Add to EXISTING article when:
- The content extends or supplements what's already there
- A reader of that article would expect to find this content

The key question: "If someone came to read about [existing article topic], would they expect to find this new content?"

# OUTPUT FORMAT

Articles are in: `articles/` folder

Styling guidelines:
- Language: English only (translate from Russian/mixed if needed)
- No bold formatting
- No horizontal rule separators
- Use short, clear sentences - break up long sentences
- You are a curator, not a writer - organize findings, don't rewrite
- Preserve original meaning and ALL details from voice notes

Article frontmatter:
```markdown
---
title: "Article Title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
status: draft
---
```

Inline source citations - when incorporating content from a source:
1. Add inline citation `[^N]` where the content is used
2. List all sources at the bottom with clickable links

Example:
```markdown
The idea for this system came after realizing that writing articles takes time[^1].

Initial workflow concept included an input pool of tasks[^2].

## Sources

[^1]: [20260117_105133_AlexeyDTC_transcript.txt](../inbox/raw/20260117_105133_AlexeyDTC_transcript.txt)
[^2]: [20260117_105343_AlexeyDTC_transcript.txt](../inbox/raw/20260117_105343_AlexeyDTC_transcript.txt)
```

Each article section MUST have sources listed at the bottom with inline citations in the text.

# SUMMARY REPORT

After processing, CREATE a summary file at `inbox/summaries/summary_` + timestamp + `.md` where timestamp is obtained by running:
```bash
python -c "from datetime import datetime; print(datetime.now().strftime('%Y%m%d_%H%M%S'))"
```

Use this EXACT format for the summary content:

```markdown
# Processing Summary

Date: YYYY-MM-DD HH:MM:SS

## Statistics
- Files processed: N
- Articles created: N
- Articles updated: N
- Images processed: N
- Images placed: N
- Images deferred (no suitable article found): N

## Articles Created
- article-title-1.md
- article-title-2.md

## Articles Updated
- existing-article-1.md
- existing-article-2.md

## Images Placed
- image1.jpg -> article-title-1.md
- image2.jpg -> article-title-2.md

## Images Deferred
- image3.jpg (reason: no related article yet)
- image4.jpg (reason: unclear context)
```

# CLEANUP

After processing:
1. Move all processed files from `inbox/raw/` to `inbox/used/`
2. Only transcripts remain (no .ogg files)

# GIT

Claude does:
```bash
git add -A
git commit -m "Process inbox: [brief description of what was processed]"
```

Python script handles `git push` and sends GitHub link to chat.
