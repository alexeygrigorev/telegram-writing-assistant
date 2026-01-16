---
description: Process Telegram inbox materials and update articles
---

You are processing materials from the Telegram writing assistant inbox. Your goal is to organize thoughts into articles.

# INPUT

Check `inbox/raw/` for new materials (text, transcripts, photos).

# PROCESSING

1. Read all files in `inbox/raw/`

2. Read existing articles from `articles/` folder (excluding `_index.md`)

3. Read `articles/_index.md` to understand what articles exist

4. For each material:
   - Translate to English if needed
   - **Context awareness for images**: When processing a photo, look at messages sent before and after (by timestamp and filename) to understand what the image relates to. Images are often part of a sequence of related thoughts.
   - **Decide: existing article OR new article**
   - Check each existing article's title and content to see if material relates to it
   - If no existing article matches, create a new article in `articles/`
   - Append content to the appropriate article

5. Update `articles/_index.md` with any new articles

# OUTPUT FORMAT

**Articles are in: `articles/` folder**

**Styling guidelines:**
- Language: English only (translate from Russian/mixed if needed)
- No bold formatting (`**text**`)
- No `---` section separators
- Use short, clear sentences - break up long sentences
- You are a **curator**, not a writer - organize findings, don't rewrite
- Preserve original meaning, just structure it

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

**Source tracking** - each article section MUST list sources:
```markdown
## Sources
- [transcript filename](../inbox/raw/filename)
- [image filename](../assets/images/filename)
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
