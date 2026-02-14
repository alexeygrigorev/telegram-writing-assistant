---
title: "AI Coding Agents for Note-Taking and Knowledge Management"
created: 2026-02-14
updated: 2026-02-14
tags: [research, obsidian, logseq, claude-code, opencode, knowledge-management]
status: draft
---

# AI Coding Agents for Note-Taking and Knowledge Management

Research into using AI coding agents (Claude Code, OpenCode) inside note-taking tools (Obsidian, Logseq) for personal knowledge management. These approaches are similar to the Telegram writing assistant - they all solve the same problem of turning scattered inputs into organized markdown articles.

## What I Want to Understand

How other people use AI coding agents for knowledge management, what tools and workflows they use, and what patterns can be borrowed for the Telegram writing assistant.

## Resources

### XDA: "I Put Claude Code Inside Obsidian, and It Was Eye-Opening"

Source: https://www.xda-developers.com/claude-code-inside-obsidian-and-it-was-eye-opening/[^1]

The article by Joe Rice-Jones describes embedding Claude Code directly inside Obsidian using the Terminal plugin. The author, a self-described late convert to Obsidian who is "terrible at taking notes," discovered that running an AI agent inside a note-taking environment lets you outsource both research and note organization to the AI. The core insight is that Obsidian vaults are just folders of markdown files on the filesystem, which makes them a natural workspace for Claude Code to read, create, and organize content.

### Setup

The setup starts with installing the Terminal plugin for Obsidian, which embeds a terminal window directly in the Obsidian interface. Claude Code runs inside this terminal, which means the user can chat with the AI agent while having their entire vault folder structure visible in the sidebar. The author describes this as "a constant reminder of what I'm doing, the context around it, and also see newly created resources as they appear."

Running `claude /init` in the vault root creates a CLAUDE.md file that serves as Claude's memory. This file is loaded into every chat session, giving the LLM context about the vault's structure, conventions, naming patterns, and rules.

### Agent Skills from Obsidian's CEO

Steph Ango (kepano), the CEO of Obsidian, released an open-source repository called obsidian-skills on GitHub. These are markdown-based skill definitions that teach Claude Code how to properly work with Obsidian-specific file formats: Obsidian Flavored Markdown, Obsidian Bases, and JSON Canvas. Installing them means copying the contents into a `.claude` folder in the vault root. The skills follow the Agent Skills open specification so they work with any compatible agent, not just Claude Code.

### Research Agent Replacing Google Search

The author states that "Google Search is broken" and that they "want to see resources and not summaries." Claude Code becomes a research agent that can browse the web, find resources, and organize findings directly into the vault. The author can outsource their browsing to Claude and have it research the next project while working on the current one.

### Web Clipper Integration

The author uses Obsidian Web Clipper across their browsers. Saved web content goes into the vault as markdown, and Claude can then read these clips to create summaries and find connections between new interests and previous research, building a web of knowledge over time.

### Related Obsidian Ecosystem Tools

- Claudian plugin: Embeds Claude Code directly in Obsidian as an AI collaborator
- Agent Client plugin: Brings Claude Code, Codex, and Gemini CLI into Obsidian
- claudesidian: Community plugin for Claude/Obsidian integration
- obsidian-claude-code-mcp: Connects Claude Code to Obsidian via Model Context Protocol
- COG-second-brain: A self-evolving second brain setup using Claude Code, Obsidian, and GitHub

### OpenCode + Logseq

Source: comments on the XDA article[^1]

"OpenCode + Logseq" was mentioned in the comments as an open-source alternative to the Obsidian + Claude Code workflow. Both tools are fully open source and local-first.

### What is OpenCode + Logseq?

OpenCode is a Go-based CLI application that provides AI-powered assistance in the terminal, supporting multiple providers (Anthropic Claude, OpenAI, Google Gemini, and others). It can read files, write files, execute shell commands, and define custom agents via markdown files.

Logseq is a privacy-first, open-source knowledge base built on top of local plain-text Markdown (and Org-mode) files. It uses an outliner/block-based approach where every piece of content is a block that can be individually referenced and linked, creating a personal knowledge graph.

There is no single official integration between OpenCode and Logseq. This is a conceptual pairing where both tools operate on local Markdown files, allowing an AI agent to read, write, and organize notes in a Logseq knowledge base.

### Three Ways They Work Together

1. Direct file access: Since Logseq stores all notes as plain Markdown files in a local directory, OpenCode can directly read and write these files from the terminal. No special plugin or API is needed - both tools work with the same Markdown files on disk.

2. MCP (Model Context Protocol) servers: Multiple community-built MCP servers exist for Logseq, including ergut/mcp-logseq (most popular, around 17k downloads), joelhooks/logseq-mcp-tools, and eugeneyvt/logseq-mcp-server. These allow any MCP-compatible AI client to interact with your Logseq graph through a standardized protocol.

3. Custom agents and commands: OpenCode supports defining custom agents as Markdown files in `~/.config/opencode/agents/` or `.opencode/agents/`. You could create a dedicated writing agent configured for knowledge management tasks - with a system prompt tailored for note-taking, restricted tool access, and a model optimized for writing.

### Logseq vs Obsidian for AI Integration

- Obsidian is proprietary (free for personal use); Logseq is fully open source
- Obsidian has a much larger plugin ecosystem for Claude Code integration
- Obsidian uses standard document-based Markdown; Logseq uses block-based outliner Markdown with unique IDs per block
- Logseq's block-based structure means an AI agent can link to specific ideas within a page, not just entire pages
- Logseq has built-in task management and daily journals; Obsidian requires plugins for these
- Logseq's daily journal workflow aligns well with AI-assisted capture - capture first, organize later

## Comparison to Telegram Writing Assistant

All three approaches solve the same fundamental problem: turning scattered inputs into organized, structured articles stored as markdown files.

### Shared Design Principles

- Markdown as the universal storage format
- An AI agent that understands the folder structure and naming conventions
- A configuration file that persists context across sessions (process.md vs CLAUDE.md)
- Git for version control and backup
- The "curator not writer" philosophy where the AI organizes rather than creates from scratch

### Key Differentiator: Input Method

The Telegram assistant has a unique advantage: voice messages. The user can dictate thoughts on the go, and the system transcribes and processes them. Both Obsidian and Logseq approaches require sitting at a computer and typing into a terminal or the editor. The Telegram assistant solves the capture problem for people who think out loud or are away from their desk.

### Separation of Capture from Processing

The Telegram assistant separates these cleanly: messages arrive in `inbox/raw/`, and the `/process` command runs Claude to categorize and organize them. The Obsidian setup could benefit from this same separation.

### Configuration as Memory

Both systems demonstrate that the key to making AI assistants useful for personal knowledge management is giving them persistent context. The Telegram assistant uses process.md (500+ lines of detailed instructions). The Obsidian setup uses CLAUDE.md plus Agent Skills. Without persistent configuration, the AI has no understanding of how you organize your knowledge, and every session starts from zero.

### Subagent Patterns

The Telegram assistant uses subagents for specialized tasks: article-summarizer, resource-describer, verify-content. The Obsidian approach achieves something similar through Agent Skills. Both recognize that different tasks benefit from specialized configurations.

## Sources

[^1]: [20260214_061215_AlexeyDTC_msg1655.md](../../inbox/used/20260214_061215_AlexeyDTC_msg1655.md)
