---
title: "Interesting Resources"
created: 2026-01-31
updated: 2026-02-05
tags: [resources, tools, ai, development]
status: draft
---

# Interesting Resources

A collection of interesting resources curated for the "Alexey On Data" newsletter and beyond.

<figure>
  <img src="../assets/images/interesting-resources/substack-resources-section.jpg" alt="Interesting Resources section in the newsletter">
  <figcaption>The Interesting Resources section as it appears in the Alexey On Data newsletter on Substack</figcaption>
  <!-- This shows the format and presentation of resources in the newsletter -->
</figure>

## Resource Format

Each resource entry follows this simple format:
- Title: the resource name (what it is)
- One paragraph description: what it does and why it's useful
- Keep it concise, 2-4 sentences max
- No bulleted lists, no code examples, no extra sections

## AI Development Tools

### Claude Code and Large-Context Reasoning

Materials from a hands-on O'Reilly Live Learning course by Tim Warner that teaches how to build production-ready AI-assisted development workflows with Claude Code. It covers large-context reasoning, MCP-based persistent memory, agents, and custom skills, with practical examples for code review, automation, and CI/CD[^1].

### awesome-slash

A curated GitHub list of tools, patterns, and projects built around slash-command interfaces. It's a practical reference for anyone designing command-driven workflows, bots, or developer tools that rely on concise, action-oriented commands instead of complex UIs[^1].

### Codex

An AI-powered CLI tool by antirez for complex debugging, code analysis, and technical questions. It handles file-based input for complex problems and can help with debugging subtle bugs, analyzing algorithms against specifications, and providing detailed code reviews[^2].

## Planning and Development Tools

### Gas Town

An orchestrator for managing multiple Claude Code instances simultaneously. Gas Town addresses the challenge of tracking work across many AI coding agents by providing a system for coordinating workers, managing merge queues, and maintaining persistent identities. It uses concepts from Kubernetes and Temporal, with tmux as the primary UI. The project represents a vision for what comes next after individual AI coding agents - coordinated workflows and "Kubernetes for agents"[^8].

### planning-with-files

A Claude Code skill that implements Manus-style persistent markdown planning. This is the workflow pattern behind Manus, the AI agent company that Meta acquired for $2 billion. The plugin transforms your workflow to use persistent markdown files for planning, progress tracking, and knowledge storage. It supports multiple IDEs including Claude Code, Cursor, Gemini CLI, Continue, and more[^6].

### Atomic Agents

A lightweight and modular framework for building AI agent pipelines and applications. Built on Instructor and Pydantic, Atomic Agents focuses on atomicity where each component (agent, tool, context provider) is single-purpose, reusable, composable, and predictable. It enables creating AI applications using familiar software engineering principles with clear input and output schemas for consistent behavior[^7].

### pro-workflow

Battle-tested Claude Code workflows from power users. Implements patterns like self-correcting memory, parallel worktrees, wrap-up rituals, and the 80/20 AI coding ratio. Features include agent teams, custom subagents, smart commit with quality gates, session analytics, and persistent SQLite storage for learnings with full-text search. Optimized for reducing correction cycles when working with AI coding assistants[^9].

### PaperBanana

An agentic framework for AI researchers that automates creation of high-quality academic illustrations. Generates methodology diagrams, flowcharts, and statistical plots from text descriptions or by polishing hand-drawn sketches. Uses a multi-step process with retrieve, plan, render, and refine agents powered by state-of-the-art vision and image generation models. Includes PaperBananaBench with 292 curated test cases from NeurIPS 2025[^10].

## Sources

[^1]: [20260131_191039_AlexeyDTC_msg741_photo.md](../inbox/used/20260131_191039_AlexeyDTC_msg741_photo.md)
[^2]: [https://gist.github.com/antirez/2e07727fb37e7301247e568b6634beff](https://gist.github.com/antirez/2e07727fb37e7301247e568b6634beff)
[^3]: [20260131_191025_AlexeyDTC_msg739_transcript.txt](../inbox/used/20260131_191025_AlexeyDTC_msg739_transcript.txt)
[^4]: [20260131_191153_AlexeyDTC_msg745_transcript.txt](../inbox/used/20260131_191153_AlexeyDTC_msg745_transcript.txt)
[^5]: [20260131_194824_AlexeyDTC_msg751_transcript.txt](../inbox/raw/20260131_194824_AlexeyDTC_msg751_transcript.txt)
[^6]: [20260202_122612_AlexeyDTC_msg848.md](../inbox/raw/20260202_122612_AlexeyDTC_msg848.md)
[^7]: [20260202_171315_AlexeyDTC_msg854.md](../inbox/raw/20260202_171315_AlexeyDTC_msg854.md)
[^8]: [20260203_134255_AlexeyDTC_msg884_transcript.txt](../inbox/raw/20260203_134255_AlexeyDTC_msg884_transcript.txt)
[^9]: [20260205_152323_AlexeyDTC_msg949.md](../inbox/raw/20260205_152323_AlexeyDTC_msg949.md)
[^10]: [20260205_162426_AlexeyDTC_msg950.md](../inbox/raw/20260205_162426_AlexeyDTC_msg950.md)
