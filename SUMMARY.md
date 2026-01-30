# Telegram → GitHub Article Assistant — Summary

## Idea

Telegram is used as a low-friction capture interface for ideas and findings:
- text messages
- voice messages
- images

A Telegram bot:
- stores all incoming data locally
- transcribes voice messages using Groq Whisper
- saves everything into a local git repository
- on demand, launches an offline agent (Claude Code) that:
  - analyzes accumulated raw materials
  - updates existing articles
  - or creates new articles when needed
  - commits the results to GitHub
  - returns a link to the commit back to Telegram

The goal is to **capture ideas first and structure them later**, without breaking the flow of thinking.

---

## Core Components

- Telegram Bot API — message ingestion
- Groq Whisper — speech-to-text (free tier with rate limits)
- Git + GitHub — storage, history, and review via diffs
- Claude Code — one-shot code/knowledge agent
- Markdown — canonical storage format

---

## Repository Structure (Obsidian-style Markdown Vault)

```
repo/
  articles/
    _index.md              # article index with short descriptions
    article-a.md
    article-b.md

  inbox/
    raw/                   # unprocessed inputs
    used/                  # processed inputs

  assets/
    images/

  scripts/
    process_inbox.py       # Claude Code runner

  logs/
    claude_runs/

  SUMMARY.md
```

Design principles:
- one article = one Markdown file
- files are readable without any special tooling
- compatible with Obsidian, VS Code, and GitHub
- easy for an agent to reason about incrementally

---

## Workflow

1. Input via Telegram:
   - text → saved as `.md`
   - voice → saved as audio + transcription `.txt`
   - images → saved as files

2. All inputs are stored in `inbox/raw`

3. A `/process` command triggers:
   - execution of `process_inbox.py`
   - invocation of Claude Code in non-interactive mode

4. Claude Code:
   - reads `_index.md` and existing articles
   - classifies each new input
   - appends material to relevant articles
   - or creates a new article when no match exists
   - avoids rewriting existing text

5. Results:
   - `git add / commit / push`
   - bot replies with a GitHub commit link

---

## Claude Code Execution Model

Claude Code is executed in one-shot mode:

```bash
claude -p "Process inbox and update articles"   --output-format json   > logs/claude_runs/run_$(date +%F_%H%M%S).json
```

Properties:
- no interactive session remains
- process exits automatically
- full execution log is preserved

---

## Editorial Philosophy

- the agent does not write final articles
- the agent does not rewrite authorial voice
- the agent only organizes and appends findings
- all changes are transparent via git diff
- the human remains the final editor

---

## Project Status

Current state:
> Personal assistant for long-term knowledge accumulation and article development
