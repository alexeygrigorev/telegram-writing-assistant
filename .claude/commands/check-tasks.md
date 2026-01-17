---
description: Check voice transcripts for tasks and create execution plan
---

You are scanning voice transcripts from the Telegram inbox to identify any actionable tasks or things to do.

# INPUT

Check `inbox/raw/` for transcript files (files ending in `_transcript.txt`).

# TASK EXTRACTION

For each transcript file:

1. Read the file content (skip frontmatter between `---` markers)

2. Scan through the text and identify any tasks, action items, or things that need to be done

3. Look for implicit requests, ideas for improvements, bug reports, feature suggestions

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

Be smart about extracting tasks - not everything is a task. Look for genuine action items.

# NOTES

- This command does NOT create any files
- This command does NOT commit anything to git
- This command does NOT move files (only /process does that)
- The plan is displayed to user only
