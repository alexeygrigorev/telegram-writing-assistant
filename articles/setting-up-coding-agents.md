---
title: "Setting Up Your Coding Agents"
created: 2026-06-04
updated: 2026-06-04
tags: [claude-code, codex, opencode, coding-agents, setup]
status: draft
---

# Setting Up Your Coding Agents

People often ask me how to get started with Claude Code. For me the question is not entirely clear at first - you just take it, download it, install it, and start using it. What is there to think about? But maybe it is more complex than that, and that is exactly what makes this worth writing about[^1].

There is real documentation from Anthropic, and there are even free courses on Claude Code. Launching the agent itself is not hard - a couple of commands and it is installed on your computer[^2].

So the real question people have is broader. From the start, they assume that Claude, like any agent, has certain capabilities - skills, MCP. People naturally get confused by this, and it feels like to build their own Claude Code setup they need to review all of it and figure out exactly which of these skills they need[^2].

What they are really asking is: show me which skills I definitely need, what I need to install, what folders exist, what helps and what does not, and how to structure my work - which folder to put things in, or how to work with the agent more effectively. In other words, the setup question is the question of all these things together[^2].

There is a lot of material online, so it is worth pointing to the courses and documentation that already exist before sharing how I personally would advise starting[^3].

## Existing material and resources

The official documentation and free courses below are the canonical starting points for getting set up.

### Claude Code official documentation

- [Overview](https://code.claude.com/docs/en/overview) - what Claude Code is and install commands for every surface (terminal, VS Code, JetBrains, desktop, web). The first stop for picking an environment and installing.
- [Quickstart](https://code.claude.com/docs/en/quickstart) - walks a first-time user through their first real task: exploring a codebase, making an edit, committing a fix.
- [Advanced setup](https://code.claude.com/docs/en/setup) - system requirements, platform-specific installation (including apt/dnf/apk on Linux), version management, uninstall.
- [Settings](https://code.claude.com/docs/en/settings) - reference for global and project-level settings.json plus environment variables.
- [Memory (CLAUDE.md)](https://code.claude.com/docs/en/memory) - how to give Claude persistent project instructions via CLAUDE.md files and how auto-memory accumulates learnings across sessions.
- [Skills](https://code.claude.com/docs/en/skills) - how to create, manage, and share skills (packaged repeatable workflows and custom commands).
- [MCP](https://code.claude.com/docs/en/mcp) and [MCP Quickstart](https://code.claude.com/docs/en/mcp-quickstart) - connecting Claude Code to external tools and data sources via the Model Context Protocol, with a hands-on first-server walkthrough.
- [Subagents](https://code.claude.com/docs/en/sub-agents) - creating specialized subagents for task-specific workflows and better context management.
- [Hooks](https://code.claude.com/docs/en/hooks) and the [Hooks guide](https://code.claude.com/docs/en/hooks-guide) - run shell commands before and after Claude Code actions (auto-format on edit, lint before commit, notifications).
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview) - an orientation map for deciding when to use CLAUDE.md vs skills vs subagents vs hooks vs MCP vs plugins.

### Claude Code free course (Anthropic Academy)

- [Anthropic Academy](https://anthropic.skilljar.com/) - Anthropic's official free training platform. Self-paced courses, no Anthropic account required.
- [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) - the flagship free getting-started course, aimed at people new to AI coding agents. Goes from installation through customization.
- [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) - a deeper, more practical free course for building real work, a good follow-on after the 101.

### OpenAI Codex official docs

- [Codex Quickstart](https://developers.openai.com/codex/quickstart) - covers the four ways to run Codex (desktop app, IDE extension, CLI, cloud), installation, and ChatGPT / API-key sign-in.
- [Codex developer docs](https://developers.openai.com/codex) and the [Codex CLI](https://developers.openai.com/codex/cli) page for the terminal agent.
- [Codex GitHub repo](https://github.com/openai/codex) - the open-source CLI, with a docs/ folder that supplements the hosted docs.

### OpenCode official docs

- [OpenCode docs intro](https://opencode.ai/docs/) - install via script or Homebrew tap, configure an LLM provider, initialize a project (which creates an AGENTS.md), and the built-in build and plan agents.
- [OpenCode homepage](https://opencode.ai/) and the [GitHub repo](https://github.com/anomalyco/opencode). Note: the older sst/opencode URL now redirects here.

### Other free getting-started material

- [Build with Claude](https://www.anthropic.com/learn/build-with-claude) - Anthropic's developer learning hub linking the Academy courses, cookbook, and quickstarts.
- [Anthropic Quickstarts](https://github.com/anthropics/claude-quickstarts) - official runnable example projects, including an autonomous coding agent built on the Claude Agent SDK.

## What we already have in our notes

This section gathers what already exists across our own drafts about setting up and configuring Claude Code, Codex, and OpenCode, grouped by tool. It is raw material to build the article from.

### Claude Code

Installing and launching:

- On Windows the native installer is now used (previously a global npm install was simpler). The terminal/CLI is the primary interface.
- Claude Code can run remotely on a cloud server (Hetzner, AWS) over SSH, which is the basis of the phone-based workflow.
- Short shell aliases speed up daily use: a single letter for claude, one for continue-session, one for skip-permissions, and combined variants.

Configuration files and structure:

- A central .claude/ dotfiles repo is synced across devices through GitHub. It holds commands/, skills/, shell config, and CLAUDE.md. Skills and commands are symlinked from the repo into ~/.claude/.
- CLAUDE.md files give project-scoped instructions, loaded hierarchically by walking up the directory tree (like .gitignore).
- .claude/settings.json sets project-level config: disabling bypass permissions, choosing the model, adjusting compaction thresholds, and configuring subagent models.
- Memory is auto-managed through a MEMORY.md index plus topic files, with frontmatter-typed entries that get consolidated automatically and capped in size.

Slash commands:

- Custom commands live as markdown files in .claude/commands/ and are user-triggered with the / syntax. Examples in use: a release command that runs the full Python publish pipeline, an init-library command that scaffolds a new package, a create-github-repo command, and the /process workflow for this Telegram writing assistant.

Skills:

- Skills are reusable workflows encoded as step-by-step instructions that the agent discovers and loads on its own. The difference from commands: skills are agent-discovered, commands are user-triggered, and Claude Code merges both.
- They load lazily, so only what the agent needs gets pulled in.
- A practical way to build a skill: interact with the agent, correct its mistakes, then ask it to summarize the corrected behavior as a skill. Improve a skill the same way over time.
- Examples include a fetch-youtube skill and a refactor-pass skill. A public skills repository is at github.com/alexeygrigorev/.claude.

Subagents and agent teams:

- Subagents are separate agents with fresh context windows, so context-heavy work does not pollute the main agent's memory. Good for analyzing large files, parallel processing, and verification with a clean perspective. They are defined as markdown files in .claude/agents/ with YAML frontmatter (name, description, tools, model, instructions).
- The planner-executor pattern has a planner produce a detailed plan and executor agents run each step with clean context.
- Agent teams are an experimental step beyond subagents (enabled via an environment variable or settings.json): one team lead plus several teammates that are independent Claude Code sessions. Unlike subagents, teammates talk directly to each other, coordinate through a shared task list with file locking, and message or broadcast.

Safety and permissions:

- Permission modes range from default (ask) through auto (approve) and plan (read-only) to bypassPermissions (dangerous).
- For high-risk projects, add a .claude/settings.json that disables bypass-permissions mode. Hooks can intercept and block dangerous operations (for example, blocking force pushes).

Token usage and performance:

- Switch to Sonnet instead of Opus to cut cost, and use Haiku for subagents.
- Raise the compaction threshold to delay message truncation, lower the effort level during a session, and turn off verbose output via /config.

Usage habits:

- Use plan mode for non-trivial tasks (three or more steps, or architectural decisions). Never mark a task complete without proving it works.
- Track work in a tasks/todo.md with checkable items, and capture corrections in a tasks/lessons.md so mistakes do not repeat.

### OpenAI Codex

- A clean, minimalist interface. Run it from the terminal.
- Supports an agent workflow with multiple subagents running in parallel, driven by an explicit task list. The orchestrator does not auto-continue when agents finish, so it needs manual prompting to keep work flowing.
- Advantage in practice: it is not hit by weekly limits as aggressively as Claude Code, so it can keep going when Claude Code is exhausted. This is what motivated trying it as an alternative.

### OpenCode

- The desktop app (a VS Code-like fork adapted for AI) is preferred over the terminal mode, though the terminal mode exists. It can also run as a web service with less setup effort than Claude Code.
- Easy to switch models, including pointing it at other providers (for example Z.AI's GLM-5) with an API key.
- It can sync skills and commands from Claude Code through the shared dotfiles repo, so hooks and skills carry over.
- The interface is smooth without the flickering Claude Code had. A subagent feature gap was noted but not yet explored.

### Cross-tool setup

- A dedicated remote server (for example Hetzner) runs the agents 24/7 in tmux sessions, with tmuxctl simplifying session management and Termius for SSH from Android. Only SSH is open on the firewall; other ports are reached via forwarding.
- Base development setup (especially on Windows): Terminal with bash, Python via UV, NodeJS via NVM, Docker, VS Code, GitHub CLI, plus the agents themselves. SSH keys are generated and added to GitHub for private repos.
- Makefiles keep commands short behind targets, which matters for phone-based work.
- Credentials should not sit on agent-accessible servers - use temporary sessions or a vault. Documenting every setup step makes it reproducible and lets an agent re-run it.

## How I would personally advise getting started

To be added: Alexey's own recommendation for how to start with Claude Code and what to do.

## Sources

[^1]: [20260604_145544_AlexeyDTC_msg4359_transcript.txt](../inbox/used/20260604_145544_AlexeyDTC_msg4359_transcript.txt)
[^2]: [20260604_145558_AlexeyDTC_msg4361_transcript.txt](../inbox/used/20260604_145558_AlexeyDTC_msg4361_transcript.txt)
[^3]: [20260604_145702_AlexeyDTC_msg4363_transcript.txt](../inbox/used/20260604_145702_AlexeyDTC_msg4363_transcript.txt)
</content>
</invoke>
