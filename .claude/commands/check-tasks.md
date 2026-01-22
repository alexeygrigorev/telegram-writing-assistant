---
description: Check all inbox materials for tasks and create execution plan
---

You are scanning ALL materials from the Telegram inbox to identify any actionable tasks or things to do.

# INPUT

Check `inbox/raw/` for ALL files:
- Transcript files (ending in `_transcript.txt`)
- Text messages (ending in `.md`)
- Photo descriptions (ending in `_photo.md`)

# TASK EXTRACTION

For each file:

1. Read the file content (skip frontmatter between `---` markers)

2. Scan through the text and identify:
   - Direct tasks and action items
   - Implicit requests
   - Ideas for improvements
   - Bug reports
   - Feature suggestions
   - Content to create (posts, articles, social media)
   - Process changes needed

3. For photo descriptions: look for:
   - Issues identified in screenshots
   - Visual feedback on article structure
   - Examples of problems to fix

4. For text messages: look for:
   - Links to review (LinkedIn, etc.)
   - Questions that imply action needed
   - Ideas and suggestions

# OUTPUT

Print the plan to console in this format:

```markdown
# Task Plan

Date: YYYY-MM-DD HH:MM:SS

## Tasks Found

### [Source: filename]
- [Task description 1]
- [Task description 2]

### [Source: filename]
- [Task description]

## Execution Plan

Prioritized list of actionable tasks:

1. [Most important/critical task]
2. [Next task]
...

## Notes

[Any observations about dependencies, complexity, or suggestions]
```

Be smart about extracting tasks - not everything is a task. Look for genuine action items. Distinguish between:
- Tasks requiring code/process changes
- Content creation tasks (articles, posts)
- Ideas for future consideration

# NOTES

- This command does NOT create any files
- This command does NOT commit anything to git
- This command does NOT move files (only /process does that)
- The plan is displayed to user only
- Group related tasks together (e.g., all article organization fixes together)
- Prioritize: Critical fixes > Content creation > Future ideas
