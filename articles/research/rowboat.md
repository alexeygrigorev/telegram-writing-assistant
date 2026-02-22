---
title: "Rowboat: Open-Source AI Coworker with Memory"
created: 2026-02-22
updated: 2026-02-22
tags: [research, ai-agents, memory, knowledge-graph]
status: draft
---

# Rowboat: Open-Source AI Coworker with Memory

https://github.com/rowboatlabs/rowboat

Rowboat is an open-source, local-first AI coworker built by a YC S24 company. It connects to your email and meeting notes, builds a long-lived knowledge graph, and uses that accumulated context to help you act[^1].

## What It Does

- Connects to email (Gmail) and meeting notes (Granola, Fireflies)
- Builds a knowledge graph stored as an Obsidian-compatible Markdown vault with backlinks
- Uses accumulated context for meeting prep, email drafting, docs/decks (including PDF slides), follow-ups
- Supports background agents for repeatable automated tasks (e.g., draft email replies, daily voice notes, recurring project updates)
- Bring-your-own model (Ollama, LM Studio, or hosted APIs)
- Extensible via MCP (Model Context Protocol) for connecting external tools (Exa, Slack, Linear, GitHub, etc.)
- Optional integrations: Deepgram for voice notes, Brave/Exa for web search

## What to Investigate

- How does it build and maintain the knowledge graph?
- How is memory structured and queried?
- Uses Qdrant vector DB (there is a `Dockerfile.qdrant` in the repo)
- How does it decide what to remember vs forget?
- How do background agents work?
- Desktop app available for Mac/Windows/Linux (uses Electron)

## Sources

[^1]: [20260222_181134_AlexeyDTC_msg2218.md](../../inbox/used/20260222_181134_AlexeyDTC_msg2218.md)
