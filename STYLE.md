# Style Guide

This document defines the styling guidelines for all articles in this repository. When processing content, the final step must always verify compliance with this guide.

## Markdown Formatting Rules

### No bold formatting
Do not use `**bold**` for emphasis. Write text without bold.

### No italic formatting
Do not use `*italic*` for emphasis. Write text without italics.

### No horizontal rules
Do not use `---` separators in articles.

### Spaces around dashes
When writing text, use ` - ` with spaces around the dash, not `-` without spaces.

### Code block separation
Two code blocks cannot follow each other directly. Always add explanatory text between code blocks.

## Writing Style

### Voice
The generated text should read as if written by Alexey - natural, direct, and practical.

### Content handling
You are a curator, not a writer. Organize findings without rewriting.

### Translations
Translate from Russian/mixed language to English, but preserve all information:
- Every idea must be preserved
- Every reason must be preserved
- Every sequence of steps must be preserved
- Only make stylistic corrections and grammar fixes
- Do not summarize voice message content

### Fact-checking
Do not assume facts not explicitly stated:
- If a transcript doesn't specify the platform (Slack vs Discord), do not guess
- When uncertain about details, check linked sources
- Better to be vague than wrong

## Article Structure

### Frontmatter
```markdown
---
title: "Article Title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
status: draft|published
---
```

### Source citations
Use inline citations `[^N]` where content is used. List all sources at the bottom with clickable links:

```markdown
## Sources

[^1]: [20260117_105133_AlexeyDTC_transcript.txt](../inbox/raw/20260117_105133_AlexeyDTC_transcript.txt)
```

## Pre-publishing Checklist

Before considering any article complete, verify:

- Style guide compliance - No bold, italic, horizontal rules, or other formatting issues
- All voice message content preserved - Nothing summarized or omitted
- All images referenced actually exist - Run `ls assets/images/{article_name}/`
- All source citations correct
- Any move requests from messages acted upon
