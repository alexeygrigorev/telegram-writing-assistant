---
title: "Research: OpenExecutive (open-source AI CEO)"
created: 2026-08-28
tags: [research, openexecutive, agents, viral]
source: Repo clone /tmp/open-executive (2026-08-28) + Grok `openexecutive-deep` (20260828_210858)
---

# OpenExecutive — Sente Labs

## The story
- Viral ~Aug 27, 2026: "CEO fired developers to make room for AI. Developers create open source AI CEO" — HN https://news.ycombinator.com/item?id=49459063 (~1000 pts, 693c)
- Origin: engineers laid off in a company's "AI Transformation" founded Sente Labs; OpenExecutive as revenge/turnabout. Poster: GitHub user GrumpySciGuy. Company unnamed.
- Timeline caveat: repo created ~June 11, 2026; v0.1.0 released June 30 (CHANGELOG). Viral framing came later; skeptics note the gap. Blend of satire + serious product.
- HN via site: https://news.ycombinator.com/from?site=github.com/sentelabsai ; gate.com backstory post: https://www.gate.com/zh-tw/post/status/23761544
- X reactions: @midudev thread (1k+ likes) https://x.com/midudev/status/2093339071892357125 ; @Gojo_Sekai https://x.com/Gojo_Sekai/status/2093356852814000312 ; also @KevinhoMorales, @kaz_066, @uni_amazigh
- Funnies: "CEO here, thanks just fired all my C suite team"; "if the board replaces workers with AI, maybe replace the guy making those decisions too"; Spanish/Chinese posts: "correct plot twist", "revenge of the nerds"

## What it is (from the repo)
- Apache 2.0, self-hostable. Python 3.11/FastAPI core + Next.js 15 UI; Claude backbone: sonnet-4-6 default, opus-4-7 w/ extended thinking for CSO/CFO/GC/Board, haiku-4-5 for routing/memory extraction. Direct Anthropic SDK, no LangGraph/CrewAI.
- One "Executive" persona (style presets incl. Huang/Zuckerberg/Nadella-inspired) backed by 8 specialists: CSO, CFO, CHRO, General Counsel, COO, CMO, CPO, Board Communications Director. Internal routing via tool calls, parallel dispatch, single synthesized voice.
- Dual-layer RAG: builtin MBA knowledge (knowledge/builtin/, git-tracked markdown → ChromaDB at startup) + uploaded company docs (separate collection). RAG context injected into user turn, never cached system prompt.
- Episodic memory: background haiku pass extracts decisions/initiatives → SQLite; next session opens with <past_decisions> block.
- Scheduler: job runner claims due actions via UPDATE...RETURNING; single-instance API, honest warning about horizontal scaling.
- Prompt caching: persona/profile/knowledge cached separately, "up to 85% cache hit rate", no dynamic content in cached blocks.
- Cost: visible token/dollar tracking and caps. Integrations: Slack, Discord, email. Demo video: https://youtu.be/O_g97xxVTMk ; site https://sentelabs.ai/
- Agents dir reveals extras beyond the 8: executive_proxy, engagement_intake, quality_judge, research_council, fixture_generator, overrides. Eval suite ships in repo (evals/run_evals.py + judges).

## Article angle (used)
Tool Teardown lite + essay: the revenge story as hook; real architecture underneath; engineering patterns worth stealing (single-voice fan-out, background memory extraction, cache-safe prompt structure, cost caps); the serious question = delegation ladder + governance (ties: Temporal 56.7% juniors, OpenAI swarm spoofing scorers). Satire is the demo; delegation design is the product.
