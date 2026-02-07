---
title: "Bash Helpers for Claude Code"
created: 2026-01-23
updated: 2026-02-07
tags: [bash, claude-code, aliases, shortcuts]
status: draft
---

# Bash Helpers for Claude Code

Simple bash aliases and functions to make working with Claude Code more convenient.

Code: https://github.com/alexeygrigorev/.claude/[^3]

## The Problem

I have many libraries and projects that I work on across different devices - my main computer and my tablet. I used to share code snippets and commands via Telegram, but that was inconvenient. When switching devices, I had to dig through messages to find the right command.

A better solution emerged: create a GitHub repository for all my Claude Code configuration and sync it across devices. Everything I need is now in one place, accessible from any device, and automatically synchronized.

## Repository Structure

The `.claude` repository contains:
- `commands/` - Custom slash commands for Claude Code
- `skills/` - Custom skills for Claude Code
- `.bashrc` - Claude-related aliases and functions
- `CLAUDE.md` - Project-specific instructions for Claude

To set up symlinks from the repo to your home directory:

cd ~/git/.claude
ln -sf "$(pwd)/skills" ~/.claude/skills
ln -sf "$(pwd)/commands" ~/.claude/commands

Or use the install script:

./install.sh

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

## Slash Commands

The repository includes several custom slash commands that automate common workflows. These commands can be used across all projects and devices - changes to the commands are automatically synchronized.

### Release Command

Automates the Python library release process. Previously, I did this manually with some automation:
1. Run tests
2. Bump version number
3. Run build
4. Push to TestPyPI
5. Verify everything works
6. Push to PyPI
7. Create GitHub release with notes
8. Clean up build artifacts

The `/release` command uses GitHub CLI to automate all of this[^4].

Key features:
- Checks for Makefile with publish targets first
- Falls back to manual process if no Makefile
- Creates GitHub release with auto-generated notes from git log
- Uploads binaries to the release
- Cleans up build artifacts afterwards

The command also generates release notes by looking at commits since the last tag, which I previously left empty or filled manually. This saves time and provides better documentation[^5].

### init-library Command

Initializes a new Python library with a consistent structure. This was created after analyzing all my existing libraries (minsearch, toyaikit, jackson, gitsource) to find common patterns[^6].

The command creates:
- Proper project structure with package directory, tests, CI workflows
- pyproject.toml with correct build configuration (hatchling)
- Makefile with standard targets (test, setup, shell, publish-build, publish-test, publish, publish-clean)
- __version__.py file for version management
- .github/workflows/test.yml for CI
- Standard .gitignore and .python-version files

The structure is designed to work with the `/release` command - libraries initialized this way follow the expected format for automated releases[^7].

### create-github-repo Command

When working in a directory and deciding something is ready to publish to GitHub, this command handles the creation process[^8].

Previously required:
1. Going to GitHub website manually
2. Creating the repository
3. Running git commands (which I often had to Google or ask ChatGPT for)
4. Pushing to remote

The `/create-github-repo` command asks for the repository name and handles everything via GitHub CLI. It supports:
- Using current folder name
- Suggested name based on codebase analysis
- Custom name
- Public or private visibility
- Immediate push or setup only

## Why Global Commands?

Instead of maintaining these commands in each individual repository, keeping them globally in `.claude` means:
- Changes propagate automatically to all devices
- Single source of truth for all projects
- Commands work identically everywhere
- Easy to update and improve workflow[^9]

## Sources

- [20260123_135217_AlexeyDTC_msg532_photo.md](../inbox/raw/20260123_135217_AlexeyDTC_msg532_photo.md)
- [20260122_182057_AlexeyDTC_msg413_photo.md](../inbox/raw/20260122_182057_AlexeyDTC_msg413_photo.md)

[^1]: [20260123_135217_AlexeyDTC_msg532_photo.md](../inbox/raw/20260123_135217_AlexeyDTC_msg532_photo.md)
[^2]: [20260122_182057_AlexeyDTC_msg413_photo.md](../inbox/raw/20260122_182057_AlexeyDTC_msg413_photo.md)
[^3]: [20260207_133114_AlexeyDTC_msg1090.md](../inbox/raw/20260207_133114_AlexeyDTC_msg1090.md) - GitHub repository link
[^4]: [20260207_133739_AlexeyDTC_msg1093_transcript.txt](../inbox/raw/20260207_133739_AlexeyDTC_msg1093_transcript.txt) - Release workflow
[^5]: [20260207_133836_AlexeyDTC_msg1094_transcript.txt](../inbox/raw/20260207_133836_AlexeyDTC_msg1094_transcript.txt) - Release notes automation
[^6]: [20260207_133954_AlexeyDTC_msg1096_transcript.txt](../inbox/raw/20260207_133954_AlexeyDTC_msg1096_transcript.txt) - Library analysis
[^7]: [20260207_135040_AlexeyDTC_msg1099_transcript.txt](../inbox/raw/20260207_135040_AlexeyDTC_msg1099_transcript.txt) - Init and release relationship
[^8]: [20260207_135254_AlexeyDTC_msg1101_transcript.txt](../inbox/raw/20260207_135254_AlexeyDTC_msg1101_transcript.txt) - GitHub repo creation
[^9]: [20260207_133907_AlexeyDTC_msg1095_transcript.txt](../inbox/raw/20260207_133907_AlexeyDTC_msg1095_transcript.txt) - Global command benefits
