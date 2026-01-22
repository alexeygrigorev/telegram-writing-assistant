---
description: Process Telegram inbox materials and update articles
---

You are processing materials from the Telegram writing assistant inbox. Your goal is to organize thoughts into articles.

# INPUT

Check `inbox/raw/` for new materials (text, transcripts, photos).

# PROCESSING ORDER

Process in TWO phases:

## Phase 1: Text Content (voice transcripts, text messages)

1. Read all files in `inbox/raw/`

2. Read existing articles from `articles/` folder (excluding `_index.md`)

3. Read `articles/_index.md` to understand what articles exist

4. For each text/transcript material:
   - **THEMATIC COHERENCE IS CRITICAL**: Each article must have ONE clear topic. Do not mix unrelated content even if messages were sent around the same time.
   - **Content-first grouping**: Do NOT group messages just by timestamp. Group ONLY if:
     1. They were sent around the same time (within 1-2 minutes), AND
     2. They are THEMATICALLY RELATED (same topic, same article context)
   - **Examples of WRONG grouping**:
     - Putting workshop content in a course article
     - Putting course curriculum updates in a workshop article
     - Putting agent examples in a general Telegram assistant article
   - **Examples of CORRECT grouping**:
     - All course-related content (curriculum, frameworks, naming) goes in AI Bootcamp Course article
     - All workshop-related content (any workshop) goes in Agents Workshop article
     - Telegram assistant development goes in Telegram Writing Assistant article
   - If messages sent together are about different topics, create SEPARATE articles
   - **Context-aware grouping**: If the message is short or unclear, look at nearby messages by timestamp (within ~1-2 minutes) to understand the full context
   - Check frontmatter `date` field to find messages sent around the same time
   - Read related voice notes, text, and photos together to get complete picture
   - **URL handling**: If a message contains only a URL, fetch its content using Jina Reader:
     - Use curl: `curl "https://r.jina.ai/{original_url}"`
     - Example: `curl "https://r.jina.ai/https://datatalks.club"`
     - This returns clean markdown content from the page
     - Then incorporate that content into the article
   - Translate to English if needed
   - **Preserve key information** - some summarization is fine as long as we don't lose important details. Keep the core ideas, context, and nuances.
   - **Decide: existing article OR new article**
   - Check each existing article's title and content to see if material relates to it
   - If no existing article matches, create a new article in `articles/`
   - Incorporate the content into the appropriate article - add it meaningfully in the right section

## Phase 2: Images (only after Phase 1 is complete)

1. Images are located in `inbox/raw/` alongside their markdown description files (frontmatter contains `image_file: filename.jpg`)

2. For each photo in `inbox/raw/`:
   - Read its markdown description file (contains Type, Content, Text, Context) - this is the ONLY source for image content, DO NOT use any vision/analyze_image tools
   - Look at messages sent before/after by timestamp for context
   - **If articles exist**: Find the most relevant section and add the image
   - **If no articles exist yet**: Defer the image

3. When placing an image in an article:
   - **Rename the image** to a descriptive name based on its content (e.g., `project-summary-slide.jpg`, `terminal-install-groq.jpg`, `claude-process-command.jpg`)
   - Move the image from `inbox/raw/` to `assets/images/{article_name}/` (create folder if needed)
   - Update image reference in article to point to new location with new filename
   - **Update the markdown description file** in `inbox/used/` with new frontmatter fields:
     - `original_image: TIMESTAMP_USERNAME.jpg`
     - `final_location: ../assets/images/{article_name}/descriptive-name.jpg`
   - Move the markdown description file to `inbox/used/`

4. Finding the RIGHT location for an image within an article:
   - **Use timestamp as primary signal**: Look at the image's date from frontmatter and find text content that was created around the same time
   - **Use context**: Read the image description (Type, Content, Text, Context) to understand what the image shows
   - **Find related section**: Search the article for content that matches the image's subject matter
   - **Place strategically**: Insert the figure NEAR the relevant text, not at the end. The text around should relate to what's in the image
   - **Example**: If image shows a terminal screenshot of installing a dependency, place it near the section about setup/dependencies, not at the end

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

# OUTPUT FORMAT

**Articles are in: `articles/` folder**

**Styling guidelines:**
- Language: English only (translate from Russian/mixed if needed)
- No bold formatting (`**text**`)
- No `---` section separators
- Use short, clear sentences - break up long sentences
- You are a **curator**, not a writer - organize findings, don't rewrite
- Preserve original meaning and ALL details from voice notes

**Article frontmatter:**
```markdown
---
title: "Article Title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
status: draft
---
```

**Inline source citations** - when incorporating content from a source:
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

**Each article section MUST have sources listed at the bottom** with inline citations in the text.

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
