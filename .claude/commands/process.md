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

# HANDLING FEEDBACK AND META-CONTENT

CRITICAL: Some messages in the inbox are feedback about the processing system itself, not content for articles.

## Identifying Feedback

Feedback messages typically contain:
- Instructions on how to process materials
- Corrections about previous processing mistakes
- Suggestions for improving the workflow
- Meta-commentary about the bot/agent behavior
- Tasks related to repository maintenance (updating index, sorting, etc.)

## Processing Feedback

When you encounter feedback:

1. Extract actionable insights: What specific change is being requested?
2. Identify the target file: Which file should be updated based on this feedback?
   - process.md - for workflow, categorization, and processing rules
   - An article file - for content corrections
   - _index.md - for index-related changes
   - Other files as appropriate
3. Perform root cause analysis: WHY did the mistake happen? What led to incorrect categorization?
4. Generalize the learning: Don't create specific rules like "don't put community in Telegram". Instead, understand the underlying principle and update the process accordingly.
5. Update the target file: Make the change to prevent recurrence.
6. DO NOT add feedback to articles: Feedback about the system does not belong in content articles.

## Common Patterns to Avoid

The bot sometimes feels it MUST categorize ALL information into articles. This leads to:
- Feedback being transcribed and added to articles inappropriately
- Meta-discussion about the system ending up in content
- Process instructions being treated as article content

Remember: NOT everything needs to be in an article. Feedback about the system belongs in feedback/, not in articles.

## Where Feedback Goes

After processing feedback, move those files to `inbox/used/feedback/` folder (not `inbox/used/`).

Examples of content that goes to `feedback/`:
- Messages instructing how to process content
- Corrections about mis-categorized content
- Suggestions for workflow improvements
- Repository maintenance tasks (updating _index.md, sorting, etc.)

# PROCESSING ORDER

## General Principles

1. Assess everything before deciding - Read ALL incoming messages first. Read ALL existing articles (or at least _index.md) before making any categorization decisions.

2. Content must serve the article's purpose - Only include elements (links, details, examples) that help readers understand the main point. Not every URL or detail belongs in the output.

3. Review before finalizing - Check for structural issues (duplicate headings, broken formatting, inconsistent style) before considering processing complete.

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

   CRITICAL: Always use Jina Reader (curl with r.jina.ai) for URL content. Do NOT use web_reader, mcp__web_reader, or other web fetch tools.

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
   - Read its markdown description file (contains Type, Content, Text, Context)
   - CRITICAL: The user's CAPTION is the authoritative source for what the image contains
   - The "Text" and "Context" fields describe what's in the image - use these along with Grok vision output
   - Look at messages sent before/after by timestamp for context (within 1-2 minutes)
   - Check what topics were being discussed in nearby messages to understand the image's purpose
   - Process images CAREFULLY and VERY THOROUGHLY - find the right place to put them
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
   - CRITICAL: Read the image description (Type, Content, Text, Context) VERY carefully - this is what the user says is in the image
   - The "Text" field in the photo description is the user's own description - treat this as authoritative for what the image contains
   - Find related section: Search the article for content that matches the image's subject matter
   - Cross-reference with nearby messages by timestamp to understand context
   - Place strategically: Insert the figure NEAR the relevant text, not at the end. The text around should relate to what's in the image
   - Example: If image shows a terminal screenshot of installing a dependency, place it near the section about setup/dependencies, not at the end
   - Verify the image actually matches what you're placing it near - if unsure, leave a note or defer

5. **IMAGE CATEGORIZATION BEST PRACTICES**:
   - Not all images belong in every article even if they were sent around the same time
   - An image showing "7 of 10" results is different from "certificate background" - they are NOT the same image
   - Read the user's description of what's in the image (Text/Context fields) - this is critical for proper categorization
   - Use vision/analyze tools ONLY as a last resort - the user's own description is authoritative
   - When in doubt about where to place an image, defer rather than place incorrectly

6. **CRITICAL: Processing Order for Image Attribution**:
   - ALWAYS read voice transcripts FIRST before photo descriptions
   - The user's caption (what they write when sending the photo) is AUTHORITATIVE for:
     - What the image contains
     - Who/what created it
     - What it represents in the workflow
   - Messages sent within 1-2 minutes are CONTEXTUALLY RELATED - read them together to understand the full workflow
   - When uncertain about attribution, trace back to original voice messages and captions

6. If image cannot be placed:
   - Move the image to `assets/images/_unused/` (create folder if needed)
   - Move the markdown description file to `inbox/used/`

7. Image placement format in articles:
```html
<figure>
  <img src="../assets/images/{article_name}/descriptive-name.jpg" alt="Image description">
  <figcaption>Short caption - what's on the image</figcaption>
  <!-- how and why this illustration is relevant to the text around -->
</figure>
```

8. Track which images were placed and which were deferred

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

IMPORTANT: If content doesn't fit into any existing article, create a NEW article. Do not leave content unused or force it where it doesn't belong.

Create a NEW article when:
- No existing article covers the topic
- Content is about a fundamentally different subject
- Adding it would dilute the focus of existing articles
- Content represents a complete, standalone project or story

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
1. Move content files from `inbox/raw/` to `inbox/used/`
2. Move feedback files from `inbox/raw/` to `inbox/used/feedback/`

# GIT

Claude does:
```bash
git add -A
git commit -m "Process inbox: [brief description of what was processed]"
```

Python script handles `git push` and sends GitHub link to chat.
