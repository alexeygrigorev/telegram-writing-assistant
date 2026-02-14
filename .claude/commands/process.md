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

# GENERAL PRINCIPLES

1. Assess everything before deciding - Read ALL incoming messages first. Read `articles/_index.md` to understand what exists before making any categorization decisions.

2. Content must serve the article's purpose - Only include elements (links, details, examples) that help readers understand the main point. Not every URL or detail belongs in the output.

3. If content doesn't fit any existing article, create a NEW article. Do not leave content unused or force it where it doesn't belong.

4. Review before finalizing - Use the pre-publishing checklist at the end of Step 3 before considering any article complete. This catches formatting errors, missed move requests, and other issues.

# CRITICAL STYLING REMINDERS

Before creating or editing ANY article content, review STYLE.md in the root repository.

The final step of processing MUST be to verify:
1. Read STYLE.md
2. Check the article for compliance with all formatting rules
3. Run grep to verify no bold formatting: `grep '\*\*' articles/{article-name}.md`
4. Verify all images exist: `ls assets/images/{article-name}/`

Remember: You are a curator, not a writer - organize findings, don't rewrite.

# FEEDBACK HANDLING

Some messages are feedback about the processing system itself, not content for articles.

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
2. Identify the target file: Which file should be updated?
   - process.md - for workflow, categorization, and processing rules
   - An article file - for content corrections
   - _index.md - for index-related changes
3. Perform root cause analysis: WHY did the mistake happen? What led to incorrect categorization?
4. Generalize the learning: Don't create specific rules. Understand the underlying principle and update the process accordingly.
5. Update the target file: Make the change to prevent recurrence.
6. DO NOT add feedback to articles (unless it's feedback about articles): Feedback about the system does not belong in content articles.

## Where Feedback Goes

After processing feedback, move those files to `inbox/used/feedback/` folder.

## Common Pattern to Avoid

The bot sometimes feels it MUST categorize ALL information into articles. This leads to feedback being transcribed and added to articles inappropriately. Remember: NOT everything needs to be in an article. Feedback about the system belongs in feedback/, not in articles.

# CONTENT MOVE REQUESTS

Some messages contain instructions to MOVE content from one article to another. This is different from feedback - it's an action item about reorganizing existing content.

## Identifying Move Requests

Look for phrases like (translated from Russian):
- "you placed this in [article X], let's move it to [article Y]" - "ты поместил это в ..., давай перенесем"
- "this should be in a separate article" - "это должно быть в отдельной статье"
- "I already told you this, move it" - "я уже говорил, давай перенесем"

## Processing Move Requests

When you encounter a content move request:

1. It is an ACTION ITEM, not context - treat it with the same priority as a direct instruction
2. Read the EXISTING article mentioned to find the content to move
3. Move the entire relevant section (not just parts of it)
4. Update source citations in both articles accordingly
5. The message requesting the move should still be used as a source for content from that session

DO NOT treat move requests as mere "context" for categorization. They are explicit instructions to reorganize existing content.

## Example

If user says: "You put my vision in the research article, let's move this to a separate article"

You MUST:
1. Open the research article
2. Find the "my vision" section
3. Move it to the new article
4. Update sources in both articles
5. Do this immediately, not as a follow-up correction

# PROCESSING WORKFLOW

## Step 1: Read Everything

1. Read all files in `inbox/raw/`
2. Read `articles/_index.md` to understand what articles exist
3. Read `articles/research/_index.md` to understand what research articles exist
4. For each piece of content, ask: Does this extend an existing article's topic? Would a reader of that article expect to find this information?

## Step 2: Categorize

CORE PRINCIPLE: Each article must have ONE clear topic. Do not mix unrelated content even if messages were sent around the same time.

### When to group messages together

Messages should be grouped together ONLY when BOTH conditions are met:
- Sent around the same time (within 1-2 minutes)
- Thematically related (same topic, same article context)

If messages sent together are about different topics, create SEPARATE articles.

### New or existing article

Create a NEW article when:
- No existing article covers the topic
- Content is about a fundamentally different subject
- Adding it would dilute the focus of existing articles
- Content represents a complete, standalone project or story (e.g., a full debugging story with a specific project)
- The content is substantial enough to stand on its own

Add to EXISTING article when:
- The content extends or supplements what's already there
- A reader of that article would expect to find this content
- CRITICAL: Keep all content about ONE topic together in ONE article. Do not split related content across multiple files. For example, if content about Automator Bot includes troubleshooting with Claude Code, that content belongs in automator-bot.md, NOT in claude-code-experiments.md.

## Step 3: Process Text Content

For each text/transcript material:

### Understanding context

If a message is short or unclear:
- Look at nearby messages by timestamp (within 1-2 minutes)
- Check frontmatter date field for related messages
- Read related voice notes, text, and photos together

### Fact-checking

DO NOT assume facts not explicitly stated:
- If transcript doesn't specify the platform (Slack vs Discord), don't guess
- If uncertain about details, check linked sources or ask
- Better to be vague than wrong

### Handling URLs

If a message contains a URL, DO NOT fetch and summarize it yourself. Use specialized subagents to avoid polluting the main agent's context.

**For research articles** - Use the article-summarizer agent:
- Launch article-summarizer subagent for each URL
- Agent fetches content via Jina Reader and writes deep summary with key insights, actionable patterns, technical details
- Multiple article-summarizer agents can run in parallel for different URLs targeting the same research article
- Example: `Summarize https://github.com/user/repo for articles/research/topic.md`

**For interesting resources** - Use the resource-describer agent:
- Launch resource-describer subagent for each orphaned URL or URL marked as "resource"
- Agent fetches content via Jina Reader and writes 2-4 sentence description in newsletter format
- Multiple resource-describer agents can run in parallel
- Example: `Add https://github.com/user/repo to interesting-resources.md`

**Launch subagents in parallel** when processing multiple URLs to speed up the workflow.

**Check subagent results**: Subagents sometimes write results directly to article files and _index.md instead of just returning text. After subagents complete, run `git status` or `git diff` to see what they changed. Review their edits for style compliance, correct source citations, and proper formatting before moving on. Do not blindly trust subagent file edits - they may miss source references to inbox files, use bold formatting, or make other style violations.

### Project Links

When the user mentions a project they implemented and shares a link to it (GitHub, etc.):
- ALWAYS include the link in the article
- Place it prominently - near the title or in the first paragraph
- Add the link message to Sources

### Final processing

- Translate to English if needed
- CRITICAL: Preserve ALL information from voice messages. Do not summarize. Every idea, reason, and sequence of steps must be preserved.
- Only stylistic corrections are allowed (translation, grammar fixes). Information must remain 100% intact.
- As a final step, compare what you wrote with the original transcript to ensure nothing was forgotten.
- Incorporate content meaningfully in the right section

### Pre-publishing checklist (CRITICAL)

Before considering an article complete, verify:

- [ ] Style guide compliance - No bold, italic, horizontal rules, or other formatting issues (see MARKDOWN STYLE GUIDE in CLAUDE.md)
- [ ] All voice message content preserved - Nothing summarized or omitted
- [ ] All images referenced actually exist - Run `ls assets/images/{article_name}/`
- [ ] All source citations correct
- [ ] Any move requests from messages acted upon

This checklist is NOT optional. Skipping it leads to corrections and rework.

## Step 4: Process Images

Images are located in `inbox/raw/` alongside their markdown description files (frontmatter contains `image_file: filename.jpg`)

### Attribution rules (CRITICAL)

- ALWAYS read voice transcripts FIRST before photo descriptions
- The user's caption (what they write when sending the photo) is AUTHORITATIVE for:
  - What the image contains
  - Who/what created it
  - What it represents in the workflow
- Filenames are NOT reliable for attribution
- Messages sent within 1-2 minutes are CONTEXTUALLY RELATED - read them together

### Default: PLACE images, don't defer

DEFAULT: Images should be PLACED in articles. When the user sends an image, they want it included.

Only defer an image if:
- The user explicitly says in the caption to not include it
- There is genuinely no matching article AND the content doesn't warrant creating a new one
- The image is a duplicate of content already in the article
- The image is feedback about the system (move to `feedback/` folder instead)

If text content from a message is added to an article, related images should ALSO be placed.

### Processing each photo

1. Read its markdown description file (contains Type, Content, Text, Context)
2. Look at messages sent before/after by timestamp for context
3. Check what topics were being discussed in nearby messages
4. Find the most relevant section in the appropriate article
5. If no suitable article exists, defer the image

### Placing an image in an article

1. Rename the image to a descriptive name (e.g., `project-summary-slide.jpg`)
2. Move the image from `inbox/raw/` to `assets/images/{article_name}/`
3. Update image reference in article to point to new location
4. Update the markdown description file with frontmatter fields:
   - `original_image: TIMESTAMP_USERNAME.jpg`
   - `final_location: ../assets/images/{article_name}/descriptive-name.jpg`
5. Move the markdown description file to `inbox/used/`

### Finding the right location within an article

- Use timestamp as primary signal: find text content created around the same time
- Read the image description (Type, Content, Text, Context) VERY carefully
- Search the article for content that matches the image's subject matter
- Place the figure NEAR the relevant text, not at the end
- Verify the image actually matches what you're placing it near - if unsure, defer

### Image placement format

```html
<figure>
  <img src="../assets/images/{article_name}/descriptive-name.jpg" alt="Image description">
  <figcaption>Short caption - what's on the image</figcaption>
  <!-- how and why this illustration is relevant to the text around -->
</figure>
```

### If image cannot be placed

- If the image is feedback about the system, move it to `inbox/used/feedback/`
- Otherwise, move the image to `assets/images/_unused/`
- Move the markdown description file to `inbox/used/`

### Verification step (CRITICAL)

After placing images, verify that all referenced files exist:
```bash
ls assets/images/{article_name}/
```

For each image reference in the article, confirm the file exists. This is just as important as checking that no information was omitted from voice messages.

## Step 5: Process Videos

Videos are NOT downloaded. Only metadata and Telegram link are saved in `inbox/raw/` (files ending with `_video.md`).

### Processing each video

1. Read the video metadata file (contains duration, resolution, file size, Telegram link)
2. Look at messages sent before/after by timestamp for context
3. Check the caption field - this is the user's description of what's in the video
4. Find the most relevant section in the appropriate article
5. If no suitable article exists, defer the video

### Placing a video in an article

Videos use the same `<figure>` format as images, but with text instead of an image:

```html
<figure>
  <p>Video: Screen recording of feature demo (2m 30s, 1080p) - <a href="https://t.me/c/3688590333/1234">View on Telegram</a></p>
  <figcaption>Short caption - what's shown in the video</figcaption>
  <!-- how and why this video is relevant to the text around -->
</figure>
```

Use the caption from the video metadata for the `<figcaption>` content.

### If video cannot be placed

Move the video metadata file to `inbox/used/` (unlike images, videos are not moved to `_unused/` since they don't take up space).

## Step 6: Verification (MANDATORY)

After processing all content, you MUST run the verify-content subagent to ensure:
1. No transcript content was summarized or omitted
2. All images mentioned in sources were actually placed
3. All video metadata was properly included

The verify-content subagent:
1. Checks git diff to find changed articles
2. Cross-references each source (transcripts, photos, videos)
3. Identifies missing or summarized content
4. Identifies images whose descriptions were used but images weren't placed
5. Fixes issues directly by restoring full content and placing missing images

Run the verification subagent:
- Use the `/agents` command to run the verify-content subagent
- OR if you have access to subagents directly, invoke verify-content
- Review the verification report
- Only proceed to Step 7 after verification passes

This step catches the most common errors:
- Summarizing instead of preserving voice message content
- Using photo description content but forgetting to place the photo
- Including video info in sources but not adding the video reference

# RESEARCH TAG

The "research" tag is used for articles about topics the user wants to investigate and learn more about. These are NOT completed work or implementations - they are collections of resources and exploration notes.

Research articles live in `articles/research/` with their own index at `articles/research/_index.md`.

When creating research articles:
- Use "research" tag in frontmatter: `tags: [research, ...]`
- Place in `articles/research/` folder with filename `{topic}.md` (e.g., `articles/research/agentic-memory.md`)
- Status should be "draft"
- Update `articles/research/_index.md` when creating new research articles
- Remove "research" tag when the investigation is complete and findings are implemented

Research articles contain:
- Links to resources (GitHub repos, blog posts, papers)
- Summaries of what the user wants to understand
- Notes and findings as they explore the topic
- Sources for all referenced materials

Example: "Spec-Driven Development" or "Agentic Memory" - topics to investigate, not completed implementations.

# WHAT I DID THIS WEEK

Content goes to the weekly article ONLY when the user explicitly says something like "what I've been working on this week" or "what I've been doing this week." Do NOT automatically add content to this article just because it was sent during the current week. The user must explicitly frame the message as a weekly update.

## Finding the current week number

To determine which week number to use, run:
```bash
python -c "from datetime import datetime; print(datetime.now().strftime('%Y-W%W'))"
```

For example: 2026-W06

## Adding to the weekly article

The article `what-i-did-this-week.md` serves as a working draft:
1. Add content under the current week heading
2. Include the date when the message was sent
3. This article accumulates unpublished content
4. When content is published elsewhere, remove it from this article

This approach provides:
- A single place for weekly updates
- Easy reference for current week's work
- A system to track what has been published vs not yet published

# COURSE NAMING CONVENTIONS

IMPORTANT: These are DIFFERENT courses and must be kept separate:

- AI Buildcamp (one word, lowercase c) - formerly "AI Bootcamp", now "AI Engineering Buildcamp"
- ML Zoomcamp (one word, lowercase c) - Machine Learning Zoomcamp
- Data Engineering Zoomcamp (one word, lowercase c) - Data Engineering Zoomcamp
- AI Dev Tools Zoomcamp (one word, lowercase c) - Development tools and workflows

When processing course-related content:
- Identify WHICH course the content refers to
- Content for different courses goes to DIFFERENT articles
- Do not mix course content even if related
- Each course gets its own dedicated article
- Different aspects of the same course should also be separate articles

# TRANSCRIPTION QUALITY NOTE

Most text content comes from transcribed voice messages. When processing:
- Expect typos, missing words, and recognition errors
- Use context to infer intended meaning
- Fix obvious errors but preserve original meaning
- When in doubt, keep the original wording

# OUTPUT FORMAT

Articles are in: `articles/` folder

Styling guidelines:
- Language: English only (translate from Russian/mixed if needed)
- No bold formatting
- No horizontal rule separators
- Use short, clear sentences
- You are a curator, not a writer - organize findings, don't rewrite
- CRITICAL: Preserve original meaning and ALL details from voice notes. Do not summarize. Every sequence of steps, every reason for doing something, every detail must be preserved. Only translate and fix stylistic issues.

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

Inline source citations:
1. Add inline citation `[^N]` where the content is used
2. List all sources at the bottom with clickable links

Example:
```markdown
The idea for this system came after realizing that writing articles takes time[^1].

## Sources

[^1]: [20260117_105133_AlexeyDTC_transcript.txt](../inbox/raw/20260117_105133_AlexeyDTC_transcript.txt)
```

## Step 7: Summary Report

After processing, CREATE a summary file at `inbox/summaries/summary_` + timestamp + `.md` where timestamp is obtained by running:
```bash
python -c "from datetime import datetime; print(datetime.now().strftime('%Y%m%d_%H%M%S'))"
```

Format:
```markdown
# Processing Summary

Date: YYYY-MM-DD HH:MM:SS

## Statistics
- Files processed: N
- Articles created: N
- Articles updated: N
- Images processed: N
- Images placed: N
- Images deferred: N
- Videos processed: N
- Videos placed: N
- Videos deferred: N

## Articles Created
- article-title-1.md

## Articles Updated
- existing-article-1.md

## Images Placed
- original.jpg -> descriptive-name.jpg -> article-title-1.md

## Images Deferred
- original.jpg (SPECIFIC reason: duplicate / no matching article / user said exclude / unclear context - NOT "content added to article")

## Videos Placed
- TIMESTAMP_USERNAME_msg1234_video.md -> article-title-1.md

## Videos Deferred
- TIMESTAMP_USERNAME_msg1234_video.md (SPECIFIC reason)
```

## Step 8: Cleanup

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

# WINDOWS PATH RULES

CRITICAL: Never use Windows backslash paths (`C:\Users\...`) in Bash tool commands. Git Bash interprets backslashes as escape characters, creating mangled file names instead of moving files.

Always use forward-slash Unix-style paths in Bash: `/c/Users/alexe/git/telegram-writing-assistant/inbox/raw/file.txt`

For Edit/Read/Write tools: use Windows backslash paths as required by CLAUDE.md.
