---
title: "Bash Helpers for Claude Code"
created: 2026-01-23
updated: 2026-01-23
tags: [bash, claude-code, aliases, shortcuts]
status: draft
---

# Bash Helpers for Claude Code

Simple bash aliases and functions to make working with Claude Code more convenient.

## Aliases

These shortcuts make it faster to invoke Claude Code from the terminal:

```bash
alias c="claude"
alias cc="claude -c"
alias csp="claude --dangerously-skip-permissions"
alias ccsp="claude -c --dangerously-skip-permissions"
```

## Initialization Function

A helper function to initialize a new project with a Claude configuration file:

```bash
claude_init() {
  local src="$HOME/.claude/CLAUDE_COPY.md"
  local dest="$PWD/CLAUDe.md"

  if [[ -e "$dest" ]]; then
    echo "CLAUDe.md already exists in this directory. Nothing done."
    return 0
  fi

  cp "$src" "$dest" || return 1
  echo "Init successful: CLAUDe.md created."
}
```

This function copies a master Claude configuration file to the current directory, avoiding duplication and ensuring consistent configuration across projects[^1].

<figure>
  <img src="../assets/images/claude-bash-helpers/bash-helpers-nano.jpg" alt="Nano editor showing bash helpers for Claude">
  <figcaption>The bash configuration file with aliases and the claude_init function</figcaption>
  <!-- These helpers are added to .bashrc for quick access -->
</figure>

## Note: Claude Deleting Tests

One issue to watch out for - Claude sometimes deletes tests during refactoring and then says "oops, where did they go?" This requires constant supervision[^2].

## Sources

- [20260123_135217_AlexeyDTC_msg532_photo.md](../inbox/raw/20260123_135217_AlexeyDTC_msg532_photo.md)
- [20260122_182057_AlexeyDTC_msg413_photo.md](../inbox/raw/20260122_182057_AlexeyDTC_msg413_photo.md)

[^1]: [20260123_135217_AlexeyDTC_msg532_photo.md](../inbox/raw/20260123_135217_AlexeyDTC_msg532_photo.md)
[^2]: [20260122_182057_AlexeyDTC_msg413_photo.md](../inbox/raw/20260122_182057_AlexeyDTC_msg413_photo.md)
