# Style Guide

This document defines the styling guidelines for all articles in this repository. When processing content, the final step must always verify compliance with this guide.

## Markdown Formatting Rules

- No `**bold**` or `*italic*` for emphasis
- No `---` horizontal rules
- Use ` - ` with spaces around dashes, not `-`
- Prefer ` - ` over em dashes in normal prose
- Two code blocks cannot follow each other directly - add text between them
- Don't overuse em dashes for dramatic effect

## Writing Style

### Voice
The generated text should read as if written by Alexey - natural, direct, and practical.
- Just use "is" - don't replace it with "serves as," "stands as," "represents"
- Repeat words instead of swapping synonyms ("the tool," "the platform," "the solution" for the same thing)

### Content handling
You are a curator, not a writer. Organize findings without rewriting. However, do edit brain dump style into proper article text - voice transcripts should read like written text, not stream-of-consciousness.

### Translations
Translate from Russian/mixed language to English, but preserve all information:
- Every idea must be preserved
- Every reason must be preserved
- Every sequence of steps must be preserved
- Only make stylistic corrections and grammar fixes
- Do not summarize voice message content

### Sentence Structure
- Use short sentences
- No passive voice - use active voice
- No filler phrases like "let me tell you," "let me explain"
- Don't start sentences with: Additionally, Moreover, Furthermore, Notably, Importantly, Consequently
- Don't puff up significance: "marks a pivotal moment," "a testament to," "reflects broader trends"
- Don't end sentences with vague -ing clauses: "...highlighting its importance," "...reflecting the growing trend"
- No promotional language: "boasts a," "diverse array," "commitment to excellence"
- No vague attributions: "experts argue," "industry reports suggest"
- No "not just X, but also Y" or rule-of-three patterns to sound comprehensive
- If there are several points, use a list instead of packing them into one long sentence
- If an idea needs explanation, don't bury it inside a bullet - give it its own short paragraph or subsection

Words to avoid: delve, crucial, pivotal, testament, underscore (verb), vibrant, intricate, garner, bolster, foster, showcase, enhance, emphasize, highlight, leverage (verb), multifaceted, realm, captivating, elevate, boasts (meaning "has"), key (overused adjective).

### Travel vocabulary

Never use "drive", "drove", or "driving" in the literal car sense - Alexey does not own a car, so transcripts that come out as "we drove to X" are always wrong. Use "we went to X", "we travelled to X", or another mode-neutral verb. Compound adjectives like "data-driven", "spec-driven", "skill-driven" are fine - this rule is about driving a car.

### Inclusive Language
- Use gender-neutral terms: "person," "someone," "they" instead of "guy," "man," "he"
- Example: "marketing person" not "marketing guy"

### Organization
- Use headings and lists to organize information
- Use level 2 (##) and level 3 (###) headings only - no level 4 (####) or deeper
- Numbered lists for steps or progressions
- Bullet points for related items

### Transcription Errors
- Watch for words that don't make sense in context - similar sounding words are often substituted incorrectly
- When a word seems wrong, check the original transcript
- Fix anything that doesn't make logical sense

### Fact-checking
- Do not assume facts not explicitly stated
- If a transcript doesn't specify the platform (Slack vs Discord), do not guess
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
