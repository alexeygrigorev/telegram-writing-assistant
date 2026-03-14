---
title: "gstack: Garry Tan's Claude Code Workflow Skills"
created: 2026-03-14
updated: 2026-03-14
tags: [research, ai-tools]
status: draft
---

# gstack: Garry Tan's Claude Code Workflow Skills

## What it is

gstack is an open-source set of eight opinionated workflow skills for Claude Code, created by Garry Tan, President and CEO of Y Combinator. The project turns Claude Code from a single generic assistant into a team of specialists that can be summoned on demand via slash commands. Each skill puts the AI into a distinct cognitive mode: founder, engineering manager, staff engineer, release engineer, or QA engineer.

The core idea is that planning is not review, review is not shipping, and founder taste is not engineering rigor. Blurring these together produces mediocre results. gstack gives explicit gears for switching between modes.

The project launched on GitHub on March 11, 2026, and quickly gained traction (7,200+ stars within three days). It is MIT-licensed and built on Bun and Playwright.

## The eight skills

`/plan-ceo-review` is the founder mode. Instead of taking a request literally, it asks what the product is actually for and finds the "10-star version" hiding inside the request. Tan describes this as "Brian Chesky mode" - rethinking the problem from the user's perspective to find something inevitable and delightful.

`/plan-eng-review` is the engineering manager mode. Once product direction is locked, this mode produces architecture diagrams, data flow models, state machines, failure modes, edge cases, trust boundaries, and test coverage plans. The key insight here is that forcing the LLM to draw diagrams (sequence, state, component, data-flow) makes hand-wavy planning much harder and surfaces hidden assumptions.

`/review` is the paranoid staff engineer mode. This runs a structural audit looking for N+1 queries, stale reads, race conditions, bad trust boundaries, missing indexes, broken invariants, and tests that pass while missing real failure modes. It also triages Greptile review comments.

`/ship` is the release engineer mode. It syncs main, runs tests, resolves Greptile reviews, pushes the branch, and opens a PR - all in one command. Designed for a branch that is ready to go, not for deciding what to build.

`/browse` gives the agent eyes. It launches a persistent headless Chromium browser, logs into the app, clicks through pages, takes screenshots, and catches visual breakage. A full QA pass in about 60 seconds.

`/qa` is the systematic QA lead. On a feature branch, it auto-analyzes the diff, identifies affected pages and routes, and tests them against localhost. It also supports full exploration mode, quick smoke tests, and regression testing.

`/setup-browser-cookies` imports cookies from a real browser (Chrome, Arc, Brave, Edge, Comet) into the headless session so authenticated pages can be tested without manual login.

`/retro` runs an engineering retrospective. It produces per-person praise and growth opportunities for every contributor, and saves JSON snapshots to `.context/retros/` for trend tracking.

## Architecture

The most technically interesting part of gstack is the browser automation system. The rest of the skills are essentially well-crafted Markdown prompt files, but the browser component is a compiled CLI binary backed by a persistent Chromium daemon.

The architecture has three layers:

1. A compiled Bun binary (about 58MB) that acts as a thin CLI client
2. A Bun HTTP server that dispatches commands to Playwright
3. A headless Chromium instance managed by Playwright

The first call to the browser takes about 3 seconds to start everything up. Every subsequent call is just an HTTP POST to localhost, taking 100-200ms round-trip. The server auto-starts on first use and auto-shuts down after 30 minutes of idle time.

The server binds to localhost only, generates a random UUID bearer token per session, and writes it to a state file with 0600 permissions. This prevents other processes on the machine from controlling the browser.

A key innovation is the ref system for element selection. Instead of injecting data attributes into the DOM (which breaks on CSP-protected sites, framework hydration, and shadow DOM), gstack uses Playwright's accessibility tree API. It assigns refs like `@e1`, `@e2` to elements and builds Playwright Locators from `getByRole()` queries. The agent can then say `click @e3` without writing CSS selectors or XPath. Refs are cleared on navigation, so stale refs fail loudly rather than clicking the wrong element.

There is also a `-C` flag for cursor-interactive refs that finds clickable elements not in the ARIA tree, things styled with `cursor: pointer` or custom `tabindex`. These get `@c1`, `@c2` refs in a separate namespace.

Logging uses three ring buffers (50,000 entries each) for console messages, network requests, and dialog events. Buffers flush to disk every second, so HTTP request handling is never blocked by disk I/O.

## Why Bun

The project uses Bun instead of Node.js for four specific reasons:

1. `bun build --compile` produces a single executable binary with no runtime dependencies - important because gstack installs into `~/.claude/skills/` where users do not expect to manage a Node.js project
2. Native SQLite support (`new Database()`) for reading Chromium's cookie database without `better-sqlite3` or native addon compilation
3. Native TypeScript execution during development with no compilation step
4. Built-in HTTP server (`Bun.serve()`) without needing Express or Fastify

## Scaling with Conductor

gstack is designed to work with Conductor (`conductor.build`), a tool that runs multiple Claude Code sessions in parallel, each in its own isolated workspace. This means one person can have ten parallel agents, each with its own cognitive mode and isolated browser instance. Each workspace gets its own Chromium process, cookies, tabs, and logs stored in `.gstack/`. Port selection is randomized (10000-60000) to avoid collisions across workspaces.

## Skill documentation system

The SKILL.md files that tell Claude how to use the browse commands are generated from `.tmpl` templates using metadata extracted from source code. This prevents documentation drift - if a command exists in code, it appears in docs; if it does not exist, it cannot appear.

The project has three tiers of testing:

- Tier 1 (static validation): parses every `$B` command in SKILL.md and validates it against the command registry. Free, runs in under 2 seconds.
- Tier 2 (E2E via Agent SDK): spawns a real Claude session, runs `/qa`, checks for errors. Costs about $0.50 per run.
- Tier 3 (LLM-as-judge): uses Haiku to score docs on clarity, completeness, and actionability. Costs about $0.03 per run.

## What makes it interesting

gstack is a practical example of how prompt engineering scales when you give it structure. Each slash command is essentially a carefully designed system prompt that puts Claude into a specific cognitive mode, but the project wraps this in a real engineering workflow with proper tooling.

The browser automation piece is genuinely novel. Most AI coding assistants are "half blind" - they can write code but cannot see the running application. By giving the agent a persistent browser with sub-second command latency, gstack closes that loop. The ref system built on the accessibility tree is a clean solution to the DOM mutation problems that plague other browser automation approaches.

The project also demonstrates Garry Tan's thesis about AI-augmented development: that the right abstraction is not "AI writes code" but "AI fills engineering roles." By separating planning, review, shipping, and testing into distinct modes, gstack avoids the failure mode where an AI assistant tries to do everything at once and does nothing well.

The Conductor integration points toward a future where a single developer can run an entire engineering team of AI agents in parallel, each specialized for a different task. This is a different model from the single-agent paradigm that most AI coding tools currently follow.

## Sources

[^1]: [GitHub: garrytan/gstack](https://github.com/garrytan/gstack)
[^2]: [20260314_051307_AlexeyDTC_msg2904.md](../../inbox/used/20260314_051307_AlexeyDTC_msg2904.md)
