---
title: "Interesting Resources"
created: 2026-01-31
updated: 2026-02-18
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
- First sentence: must include a link to the resource
- One paragraph description: what it does and why it's useful
- Keep it concise, 2-4 sentences max
- No bulleted lists, no code examples, no extra sections

### pro-workflow

[pro-workflow](https://github.com/rohitg00/pro-workflow) is a collection of battle-tested Claude Code workflows from power users. It implements patterns like self-correcting memory, parallel worktrees, wrap-up rituals, and the 80/20 AI coding ratio. Features include agent teams, custom subagents, smart commit with quality gates, session analytics, and persistent SQLite storage for learnings with full-text search. Optimized for reducing correction cycles when working with AI coding assistants[^9].

### PaperBanana

[PaperBanana](https://paperbanana.org/) is an agentic framework for AI researchers that automates creation of high-quality academic illustrations. It generates methodology diagrams, flowcharts, and statistical plots from text descriptions or by polishing hand-drawn sketches. Uses a multi-step process with retrieve, plan, render, and refine agents powered by state-of-the-art vision and image generation models. Includes PaperBananaBench with 292 curated test cases from NeurIPS 2025[^10].

### Dexter

[Dexter](https://github.com/virattt/dexter) is an autonomous financial research agent that thinks, plans, and learns as it works. It performs analysis using task planning, self-reflection, and real-time market data. Think Claude Code, but built specifically for financial research. It features intelligent task planning, autonomous execution, self-validation, real-time financial data access, and safety features like loop detection and step limits[^11].

### nao

[nao](https://github.com/getnao/nao) is an open source analytics agent that combines a CLI tool for creating context with a deployable chat interface for teams. It allows data teams to set up a chat interface over their data sources, with the nao-core CLI handling context creation and indexing. The project supports self-hosting via Docker and provides a web UI for business users to interact with data through natural language queries[^17].

### Claude Pilot

[Claude Pilot](https://github.com/maxritter/claude-pilot) is a quality automation layer built on top of Claude Code that enforces production-grade quality on every coding session through automated linting, formatting, type checking, and mandatory test-driven development. It adds spec-driven planning with verifier sub-agents, persistent memory across sessions, isolated git worktrees for safe experimentation, and an "Endless Mode" that handles session continuity automatically. The idea is simple: start a task, walk away, and come back to tested, verified code ready to ship[^20].

### RTK (Rust Token Killer)

[RTK](https://github.com/rtk-ai/rtk) is a CLI proxy that cuts Claude Code token usage by 89% by filtering and compressing command output before it reaches the LLM context. Most of what Claude Code reads from commands like test runs, git status, and logs is noise - passing tests, verbose output, status bars - and RTK strips it down to just the essentials. The author reported saving 10.2 million tokens over two weeks, with compressions like cargo test going from 155 lines to 3 lines[^21].

### Voicebox

[Voicebox](https://github.com/jamiepine/voicebox) is an open-source, local-first voice cloning studio powered by Qwen3-TTS. It provides DAW-like features including a multi-track timeline editor, voice profile management, and a REST API for integrating voice synthesis into other applications. Think of it as a local, free alternative to ElevenLabs - download models, clone voices from a few seconds of audio, and generate speech entirely on your machine with no cloud dependency[^25].

### You Could've Invented OpenClaw

[You Could've Invented OpenClaw](https://gist.github.com/dabit3/bc60d3bea0b02927995cd9bf53c3db32) is a tutorial by Nader Dabit that walks through building a persistent AI assistant from scratch, starting with a simple Telegram bot using the Anthropic API. It incrementally adds sessions, personality, tool use, multi-channel support, memory, and scheduled tasks, arriving at a ~400-line "mini OpenClaw" clone. I already built my own Telegram bot - this is an interesting look at how someone else approached the same problem[^22][^23].

### Zvec

[Zvec](https://github.com/alibaba/zvec) is an open-source, in-process vector database from Alibaba, built on their battle-tested Proxima vector search engine. It can search billions of vectors in milliseconds while supporting both dense and sparse embeddings, hybrid search with structured filters, and multi-vector queries. Unlike client-server vector databases, Zvec embeds directly into your application with no infrastructure overhead, making it a compelling option for RAG pipelines and similarity search on notebooks, servers, or edge devices. I was looking for something like this very recently[^24].

## Sources

[^1]: [20260131_191039_AlexeyDTC_msg741_photo.md](../inbox/used/20260131_191039_AlexeyDTC_msg741_photo.md)
[^2]: [https://gist.github.com/antirez/2e07727fb37e7301247e568b6634beff](https://gist.github.com/antirez/2e07727fb37e7301247e568b6634beff)
[^3]: [20260131_191025_AlexeyDTC_msg739_transcript.txt](../inbox/used/20260131_191025_AlexeyDTC_msg739_transcript.txt)
[^4]: [20260131_191153_AlexeyDTC_msg745_transcript.txt](../inbox/used/20260131_191153_AlexeyDTC_msg745_transcript.txt)
[^5]: [20260131_194824_AlexeyDTC_msg751_transcript.txt](../inbox/used/20260131_194824_AlexeyDTC_msg751_transcript.txt)
[^6]: [20260202_122612_AlexeyDTC_msg848.md](../inbox/used/20260202_122612_AlexeyDTC_msg848.md)
[^7]: [20260202_171315_AlexeyDTC_msg854.md](../inbox/used/20260202_171315_AlexeyDTC_msg854.md)
[^8]: [20260203_134255_AlexeyDTC_msg884_transcript.txt](../inbox/used/20260203_134255_AlexeyDTC_msg884_transcript.txt)
[^9]: [20260205_152323_AlexeyDTC_msg949.md](../inbox/used/20260205_152323_AlexeyDTC_msg949.md)
[^10]: [20260205_162426_AlexeyDTC_msg950.md](../inbox/used/20260205_162426_AlexeyDTC_msg950.md)
[^11]: [20260206_074649_valeriia_kuka_msg971.md](../inbox/used/20260206_074649_valeriia_kuka_msg971.md)
[^12]: [20260207_215252_AlexeyDTC_msg1182.md](../inbox/used/20260207_215252_AlexeyDTC_msg1182.md)
[^13]: [20260209_170808_AlexeyDTC_msg1244.md](../inbox/used/20260209_170808_AlexeyDTC_msg1244.md)
[^14]: [20260209_170914_AlexeyDTC_msg1246_transcript.txt](../inbox/used/20260209_170914_AlexeyDTC_msg1246_transcript.txt)
[^15]: [20260209_171006_AlexeyDTC_msg1248.md](../inbox/used/20260209_171006_AlexeyDTC_msg1248.md)
[^16]: [20260210_084748_AlexeyDTC_msg1267.md](../inbox/used/20260210_084748_AlexeyDTC_msg1267.md)
[^17]: [20260210_150732_AlexeyDTC_msg1291.md](../inbox/used/20260210_150732_AlexeyDTC_msg1291.md)
[^18]: [20260211_131904_valeriia_kuka_msg1441.md](../inbox/used/20260211_131904_valeriia_kuka_msg1441.md)
[^19]: [20260211_130747_valeriia_kuka_msg1433.md](../inbox/used/20260211_130747_valeriia_kuka_msg1433.md)
[^20]: [20260214_060731_AlexeyDTC_msg1653.md](../inbox/used/20260214_060731_AlexeyDTC_msg1653.md)
[^21]: [20260214_063326_AlexeyDTC_msg1656.md](../inbox/used/20260214_063326_AlexeyDTC_msg1656.md)
[^22]: [20260214_103313_AlexeyDTC_msg1673.md](../inbox/used/20260214_103313_AlexeyDTC_msg1673.md)
[^23]: [20260214_103407_AlexeyDTC_msg1675_transcript.txt](../inbox/used/20260214_103407_AlexeyDTC_msg1675_transcript.txt)
[^24]: [20260215_214321_AlexeyDTC_msg1701.md](../inbox/used/20260215_214321_AlexeyDTC_msg1701.md)
[^25]: [20260218_141744_AlexeyDTC_msg1945.md](../inbox/used/20260218_141744_AlexeyDTC_msg1945.md)
[^26]: [20260218_145313_valeriia_kuka_msg1949.md](../inbox/used/20260218_145313_valeriia_kuka_msg1949.md)
