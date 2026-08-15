---
title: "Content Plan: Mid-August to Mid-September 2026"
created: 2026-08-15
tags: [content-plan, ideas]
status: draft
---

# Content Plan: 2026-08-15 → 2026-09-15

Based on Grok social-signal research (2026-08-15, `~/git/ai-engineering-field-guide/_work-in-progress/grok-responses/20260815_100630_monthly-topics-aug2026.json`) + existing backlog.

**What's hot this month (X/Twitter, AI eng community):**
1. MCP — architecture patterns, tool-count limits, bearish vs bullish debate
2. Agent evaluation — trajectories, final environment state, cost/variance
3. Context engineering — compression, memory, tool chaos in production agents
4. Agent runtimes / long-horizon reliability — state drift, checkpointing
5. Local models in agents — determinism problems

## The Plan (5 slots)

### Slot 1 (week of Aug 17) — MCP: Too Many Tools ✅ DRAFT READY
- **Combined article** (angles 1+3 merged per Alexey): `claw-drafts/mcp-vs-code.md`
- **Angle:** tool-count accuracy cliff + the "just write code" backlash + 5-rule hybrid framework ("Small Surface, Deep Reach") + OpenClaw case study
- **Corrections applied:** no finance jargon (bear/bull → critics/supporters), OpenClaw section added
- **Research:** `clo/research/mcp-server-design-patterns-2026-08-15.md`, `clo/research/mcp-vs-code-2026-08-15.md`

### Slot 2 (week of Aug 24) — Evaluating Agents (not just LLMs)
- **Template:** Concepts Explainer
- **Angle:** agents are trajectories, not outputs. Success = final environment state. Granular signals: tool-use efficiency, intermediate states. Cost/variance of eval runs.
- **Personal hook:** AI Shipping Labs students struggle with this exact thing.

### Slot 3 (week of Aug 31) — Batch Requests: Saving Money
- **Status:** already researched — workshop material, mentioned in weekly log as unpublished
- **Just needs writing.** Cheapest slot of the month.

### Slot 4 (week of Sep 7) — Context Engineering in Production
- **Template:** Strategic Essay + Framework
- **Angle:** compression, memory systems, multi-agent context splitting. Not hype — what actually survives contact with production.
- **Personal hook:** podwiki / Codex goal project = a real case of context management at scale.

### Slot 5 (week of Sep 14) — Coming Up with Project Ideas
- **Status:** draft exists (`ideas/coming-up-with-project-ideas.md`, updated Aug 9)
- Finish, add the 150-ideas catalog link, ship.

## Backlog (spare topics if a slot frees up)
- Local models + determinism in agents (Grok research slot)
- Agent runtimes / long-horizon reliability (Microsoft paper angle)
- FAQ assistant with Opik — customer story (file exists in ideas/content/)
