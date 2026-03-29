---
title: "724 Office: Self-Evolving AI Agent System"
created: 2026-03-29
updated: 2026-03-29
tags: [research, ai-agents, self-evolving, memory, tools]
status: draft
---

# 724 Office: Self-Evolving AI Agent System

GitHub: https://github.com/wangziqi06/724-office

A production-running AI agent built in around 3,500 lines of pure Python with zero framework dependency. No LangChain, no LlamaIndex, no CrewAI - just the standard library plus 3 small packages (croniter, lancedb, websocket-client). 26 tools, 8 files, runs 24/7. Built solo with AI co-development tools in under 3 months[^1][^2].

## Key Features

Three-layer memory system that actually works:
- Layer 1 (session): last 40 messages per session in JSON. Overflow triggers compression
- Layer 2 (compressed long-term): LLM extracts structured facts from evicted messages, deduplicates at 0.92 cosine similarity, stores as vectors in LanceDB
- Layer 3 (retrieval): user message gets embedded, vector search finds relevant memories, injects them into system prompt before the model sees the input

Runtime tool creation - one `create_tool` command and the agent writes a new Python function, saves it to disk, and loads it into its own process without restarting.

Self-repair - daily self-checks run automatically. Error log analysis, session health diagnostics. If something fails, it notifies the owner. The agent monitors itself.

Cron scheduling - one-shot and recurring tasks, persistent across restarts, timezone-aware.

Multimodal out of the box - images, video, voice, files, speech-to-text, vision via base64, video trimming, background music, AI video generation. All exposed as tools through ffmpeg.

Multi-engine web search across Tavily, GitHub, and HuggingFace with auto-routing per query.

Multi-tenant via Docker - one container per user, auto-provisioned, health-checked.

## Architecture

The system is organized as: Messaging Platform -> router.py (multi-tenant routing) -> xiaowang.py (entry point, HTTP server) -> llm.py (tool use loop, session management, memory injection) -> three subsystems: tools.py (26 tools + plugin system + MCP bridge), memory.py (3-stage pipeline), and scheduler.py (cron + one-shot jobs).

## Design Principles

- Zero framework dependency - every line is visible and debuggable, no hidden abstractions
- Single-file tools - adding a capability means adding one function with a @tool decorator
- Edge-deployable - designed to run on Jetson Orin Nano (8GB RAM, ARM64 + GPU), under 2GB RAM budget
- Self-evolving - can create new tools at runtime, diagnose its own issues, and notify the owner
- Offline-capable - core functionality works without cloud APIs (except the LLM itself)

License: MIT.

## Sources

[^1]: [20260329_100432_AlexeyDTC_msg3123.md](../../inbox/used/20260329_100432_AlexeyDTC_msg3123.md)
[^2]: https://x.com/aigleeson/status/2037848861591703914
