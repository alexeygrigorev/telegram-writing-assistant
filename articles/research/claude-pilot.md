---
title: "Claude Pilot: Quality Automation for Claude Code"
created: 2026-02-14
updated: 2026-02-14
tags: [research, claude-code, automation, tdd, quality]
status: draft
---

# Claude Pilot: Quality Automation for Claude Code

Research into [Claude Pilot](https://github.com/maxritter/claude-pilot), a quality automation layer built on top of Claude Code. The goal is to understand how it works and learn patterns for building something similar.

## What I Want to Understand

How Claude Pilot enforces quality guardrails on Claude Code sessions, and what architectural patterns can be reused for building similar automation wrappers around AI coding agents.

## Resources

### GitHub: maxritter/claude-pilot

Source: https://github.com/maxritter/claude-pilot[^1][^2]

Claude Pilot is a quality automation layer built on top of Claude Code (Anthropic's CLI coding agent). Created by Max Ritter, a senior IT freelancer from Germany, it addresses a specific problem: Claude Code writes code fast but without structure, it skips tests, loses context, and produces inconsistent results. Pilot wraps Claude Code with enforced quality guardrails - linting, formatting, type checking, TDD enforcement, context monitoring, and verification sub-agents - so that you can start a task, walk away, and return to production-grade code.

It is a commercial, source-available product (not open source) with Solo and Team tiers, licensed through Polar. It works on macOS, Linux, and Windows (WSL2) and requires an existing Claude subscription (Max 5x/20x or Team Premium).

The tagline captures it well: "Claude Code is powerful. Pilot makes it reliable."

### Two Modes of Operation

Pilot offers two workflows:

1. Quick Mode - direct execution with zero overhead. You describe a task and it gets done. All quality hooks and TDD enforcement still apply, but there is no plan file, no approval gate, and no sub-agents.

2. /spec Mode (Spec-Driven Development) - for complex features. It follows a pipeline: Discuss, Plan, Approve, Implement, Verify, Done. Each task is implemented with strict TDD (RED, GREEN, REFACTOR). A plan-verifier sub-agent validates the plan before implementation. A spec-verifier sub-agent reviews the code after implementation. Issues loop back automatically.

### The Hooks Pipeline

The core enforcement mechanism is a pipeline of hooks that fire at every stage of development:

- SessionStart hooks: load persistent memory and initialize session tracking
- PostToolUse hooks (after every Write/Edit/MultiEdit): file_checker.py dispatches to language-specific checkers (Python: ruff + basedpyright, TypeScript: Prettier + ESLint + tsc, Go: gofmt + golangci-lint), tdd_enforcer.py checks if implementation files were modified without failing tests first, context_monitor.py tracks context window usage
- PreToolUse hooks: tool_redirect.py routes tools to appropriate contexts during plan/implement phases
- Stop hooks: spec_stop_guard.py blocks stopping if a spec has PENDING or COMPLETE status (forces verification to complete), session summarizer saves observations to persistent memory

### Smart Model Routing

Pilot routes different phases to different models based on reasoning requirements:

- Planning and Plan Verification use Opus (deep reasoning for architecture and catching gaps)
- Implementation uses Sonnet (fast, cost-effective when guided by a clear spec)
- Code Verification uses Opus (catching subtle bugs requires planning-level reasoning)

The insight: implementation is the easy part when the plan is good. Invest reasoning power in planning and verification, use fast execution where a clear spec makes quality predictable.

### Endless Mode

Context window management solved through real-time monitoring:

- Warns as context grows, forces handoff before hitting limits
- Session state saved to ~/.pilot/sessions/ with continuation files
- Next session picks up seamlessly
- During /spec, Pilot will not start a new phase when context is high - it hands off instead
- Multiple sessions can run in parallel on the same project

### /sync - Codebase Discovery

The /sync command explores the codebase, builds a semantic search index (using Vexor), discovers undocumented patterns, updates project documentation, and creates custom skills. It is a 10-phase process that reads existing rules, indexes the codebase, compares discovered vs documented patterns, syncs project.md, updates MCP server documentation, and creates new skills.

### /learn - Online Learning

Captures non-obvious discoveries as reusable skills. Triggered automatically after 10+ minute investigations, or manually. Skills are stored and can be shared across teams via /vault.

### /vault - Team Knowledge Sharing

A private Git repository for sharing rules, commands, and skills across a team. Assets are versioned automatically.

## Key Insights

1. Quality enforcement beats quality suggestion. Other frameworks suggest best practices via prompts. Pilot enforces them via hooks. When Claude ignores a suggestion under context pressure, hooks still catch the violation. The difference between "you should write tests" and "this hook blocks you until tests exist" is the difference between aspiration and enforcement.

2. Complexity is the enemy. Ritter explicitly rejects the "more agents, more scaffolding" approach. Other frameworks burn tokens on bloated prompts without proportional quality improvement. Pilot stays lean: quick mode has zero overhead, and even /spec only adds structure where it matters. More context goes to actual work.

3. Planning and verification deserve more reasoning power than implementation. This is the smart model routing insight. With a solid plan and thorough verification, implementation becomes the straightforward part. Spending Opus tokens on planning catches issues before they are coded. Spending Opus tokens on verification catches issues before they ship. Implementation with Sonnet in between is fast and cheap.

4. Context window management is a first-class concern. Most users of Claude Code hit context limits on complex tasks and lose progress. Pilot treats context as a finite resource with active monitoring, warnings, forced handoffs, and seamless continuation. This turns a single session tool into a multi-session workflow.

5. Every file edit is a checkpoint. The PostToolUse hook pattern means every single file write triggers linting, formatting, type checking, and TDD verification. Problems are caught immediately, not at the end. This is analogous to continuous integration but at the individual edit level.

6. Local-first architecture matters for enterprise adoption. No code, files, prompts, or project data leaves the machine. All tools (Vexor for search, Pilot Console for memory, hooks) run locally. The only external calls are for licensing.

## Actionable Patterns

### Pattern 1: Hook-Based Quality Gates

Instead of relying on prompts to encourage good behavior, use Claude Code's hook system to enforce it programmatically. Hooks fire at SessionStart, PreToolUse, PostToolUse, and Stop events. Each hook can be blocking (stops execution until resolved) or non-blocking (shows warnings). This is the most transferable pattern - any Claude Code wrapper can use hooks to enforce project-specific rules.

### Pattern 2: Sub-Agent Verification

Use separate Claude invocations (sub-agents) to verify work done by the main agent. The plan-verifier checks completeness before implementation. The spec-verifier performs code review after implementation. The key: the verifier has a different perspective than the implementer because it starts from the spec, not from the code.

### Pattern 3: Worktree Isolation

Use git worktrees to isolate experimental work. The main branch stays clean. When work is verified, squash merge back. This is a safety net that makes it possible to walk away - if the agent makes a mess, it is contained in a worktree.

### Pattern 4: Context Budgeting with Forced Handoffs

Monitor context usage in real-time. Define thresholds (warn, force handoff). Save continuation state to disk. Start new sessions that load the continuation state. This turns context limits from a hard wall into a managed transition.

### Pattern 5: Conditional Rule Loading

Rules (markdown files) can use frontmatter with `paths` to activate only when working with matching file types. Python rules load only when editing .py files. This keeps the context budget efficient - you are not spending tokens on irrelevant rules.

### Pattern 6: Persistent Memory Across Sessions

A 3-layer memory system: search past context, timeline of observations, and new observations saved at session end. This is implemented via MCP server (mem-search) and hooks that capture/load observations. The result: sessions are not isolated - they build on each other.

### Pattern 7: Semantic Code Search via Vexor

Instead of relying solely on grep and file glob, build a semantic search index of the codebase. Vexor creates vector embeddings for code, enabling natural language queries. This gives the agent better codebase understanding, especially for the planning phase.

### Pattern 8: The /sync Bootstrap

A single command that explores the codebase, discovers patterns, and generates documentation. This bootstrapping step means the agent starts every session with genuine understanding of the project, not generic assumptions.

## Technical Details

### Core Architecture

- Pilot CLI binary: installed to ~/.pilot/bin/pilot, manages sessions, worktrees, licensing, and context
- Shell alias: `pilot` or `ccp` starts Claude Code with Endless Mode, auto-update, and license check
- Configuration: .claude/ directory in each project holds rules, commands, hooks, skills, and MCP server configs
- Hooks: Python scripts in .claude/hooks/ that fire at Claude Code lifecycle events
- Rules: Markdown files in .claude/rules/ loaded into every session or conditionally by file type
- Commands: slash commands in .claude/commands/ for specific workflows
- Skills: reusable knowledge created by /learn, stored as files

### Tech Stack and Dependencies

- Runtime: Python 3.12+, Node.js
- Package manager: uv (for Python), npm/pnpm (for TypeScript)
- Installer: bash script with 8-step process, Homebrew-based, rollback on failure, idempotent
- Vector search: Vexor (local semantic search index)
- MCP servers: Context7 (library docs), mem-search (persistent memory), web-search (DuckDuckGo/Bing/Exa), grep-mcp (GitHub code search), web-fetch (documentation fetching), playwright-cli (browser automation)
- Language servers (LSP): basedpyright (Python), vtsls (TypeScript), gopls (Go) - configured via .lsp.json
- Quality tools: ruff (Python linting/formatting), basedpyright (Python type checking), Prettier (TypeScript formatting), ESLint (TypeScript linting), tsc (TypeScript type checking), gofmt (Go formatting), golangci-lint (Go linting)
- Licensing: Polar API (api.polar.sh), cached locally, works offline for up to 7 days
- Console: web-based UI at localhost:41777 for visualizing workflow

### Built-in Rules (22 total)

Quality Enforcement (4): TDD enforcement, verification before completion, execution verification, workflow enforcement

Context Management (3): context continuation (Endless Mode), persistent memory, coding standards

Language Standards (3): Python, TypeScript, Go

Tool Integration (6): Vexor search, Context7 docs, grep-mcp, web search, playwright-cli, mcp-cli

Development Workflow (6): git operations, GitHub CLI, systematic debugging, testing strategies, online learning, team vault

## Sources

[^1]: [20260214_060731_AlexeyDTC_msg1653.md](../../inbox/used/20260214_060731_AlexeyDTC_msg1653.md)
[^2]: [20260214_060806_AlexeyDTC_msg1654.md](../../inbox/used/20260214_060806_AlexeyDTC_msg1654.md)
