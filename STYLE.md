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
- Avoid complex words like "further," "moreover," "additionally"
- No passive voice - use active voice
- No filler phrases like "let me tell you," "let me explain" - they don't add value

### Avoiding AI-sounding writing

Based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), avoid the following patterns that make text look machine-generated.

AI vocabulary words to avoid: delve, tapestry (figurative), landscape (figurative), crucial, pivotal, testament, underscore (as verb), vibrant, intricate/intricacies, meticulous/meticulously, garner, bolstered, enduring, foster/fostering, showcase/showcasing, enhance/enhancing, emphasize/emphasizing, highlight/highlighting, interplay, align with, valuable (as in "valuable insights"), profound, renowned, groundbreaking, nestled, encompassing, facilitate, comprehensive (as filler), leverage (as verb), multifaceted, realm, commendable, noteworthy, captivating, elevate, intriguing, boasts (meaning "has"), key (overused as adjective).

Transition words to avoid at the start of sentences: Additionally, Moreover, Furthermore, Notably, Importantly, Consequently, Nonetheless, Conversely, Hence.

Patterns to avoid:
- Puffing up significance: "marks a pivotal moment," "setting the stage for," "evolving landscape," "indelible mark," "deeply rooted," "a testament to," "underscores its importance," "reflects broader trends"
- Superficial -ing analyses at end of sentences: "...highlighting its importance," "...emphasizing the need for," "...reflecting the growing trend," "...contributing to the broader," "...fostering a sense of"
- Promotional tone: "boasts a," "in the heart of," "diverse array," "rich cultural heritage," "natural beauty," "commitment to excellence"
- Vague attributions: "experts argue," "industry reports suggest," "observers have cited," "some critics argue"
- "Despite challenges" formula: "Despite its success, X faces challenges including..." followed by vague optimism
- Negative parallelisms: "not just X, but also Y," "it's not about X, it's about Y"
- Rule of three overuse: "adjective, adjective, and adjective" or "phrase, phrase, and phrase" used to sound comprehensive
- Elegant variation: unnecessarily using different words for the same thing to avoid repetition (e.g., switching between "the tool," "the platform," "the solution" for the same product). Just repeat the word.
- Avoiding "is/are": replacing simple "is" with "serves as," "stands as," "represents," "marks." Just use "is."
- Overuse of em dashes for dramatic effect in every other sentence
- Collaborative chatbot phrases: "I hope this helps," "certainly," "let me know if you'd like," "here is a detailed breakdown"

### Inclusive Language
- Use gender-neutral terms: "person," "someone," "they" instead of "guy," "man," "he"
- Example: "marketing person" not "marketing guy"

### Organization
- Avoid brain dump style - add structure to content
- Use headings and lists to organize information
- Use level 2 (##) and level 3 (###) headings only - no level 4 (####) or deeper
- Numbered lists for steps or progressions
- Bullet points for related items

### Transcription Errors
Watch for and fix transcription errors. Transcription often produces words that don't make sense in context:
- Check if the word fits the surrounding content
- When a word seems wrong, check the original transcript
- Similar sounding words are often substituted incorrectly
- Fix anything that doesn't make logical sense

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
