---
description: Check voice transcripts for tasks and create execution plan
---

You are analyzing voice transcripts from the Telegram inbox to extract tasks and create an execution plan.

# INPUT

Check `inbox/raw/` for transcript files (files ending in `_transcript.txt`).

# TASK EXTRACTION

For each transcript file:

1. Read the file content (skip frontmatter between `---` markers)

2. Look for task indicators in Russian and English:
   - давай / let's / let us
   - сделай / do / make / create
   - добавим / add / implement
   - нужно / надо / need to / should
   - хотелось бы / would like

3. Extract the task context (the sentence or phrase containing the indicator)

# OUTPUT

Create a plan document at `inbox/summaries/task_plan_` + timestamp + `.md` with this format:

```markdown
# Task Plan

Date: YYYY-MM-DD HH:MM:SS

## Tasks Found

### [Source: filename]
1. [Task description]
2. [Task description]

### [Source: filename]
1. [Task description]

## Execution Plan

Prioritized list of actionable tasks:

1. [Most important/critical task]
2. [Next task]
...

## Notes

[Any observations about dependencies, complexity, or suggestions]
```

# CLEANUP

After creating the plan:
1. Move processed transcript files from `inbox/raw/` to `inbox/used/`

# GIT

Claude does:
```bash
git add -A
git commit -m "Extract tasks: [brief description]"
```
