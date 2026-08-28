---
title: "Research: Hot Topics Late August 2026"
created: 2026-08-28
tags: [research, trends, hot-topics]
source: Grok `hot-topics-aug28-2026` (20260828_203350), raw JSON in
`~/git/ai-engineering-field-guide/_work-in-progress/grok-responses/`
---

# Hot topics mid-to-late August 2026 (for Alexey On Data)

## 1. Durable / production agents (fresh data)
- **Temporal "State of Development Report: AI Agents" (Aug 25)**, 550+ engineers: 80%+ daily agent use, median 5 agents/team (some >100), 91% claim productivity gains, **41% face daily reliability issues**; error recovery + governance lag; "SaaSpocalypse" rebuilding internal tools.
  https://apnews.com/press-release/business-wire/press-release-c981d312a26f4cbeae42036dae277c3c
- Aaron Levie thread (Aug 19) on applied-AI layer: harnesses, domain context, evals, multi-model workflows https://x.com/levie/status/2089921630650925170
- Laminar on proper agent rollouts vs naive model swaps https://x.com/skull8888888888/status/2092640313802211352
- Cloudflare Agents changelog (Aug 22): tracing, computer runtime preview
- → Feeds existing `durable-agents.md` draft (add report numbers)

## 2. Harnesses > models (JIT-Agent, hottest paper)
- **JIT-Agent paper (arXiv 2608.25593, Aug 25-27)**: just-in-time task-adaptive harness generation; beats or matches OpenCode/Claude Code on some benchmarks; harness edits give **33-60% relative gains** vs model changes; harnesses "trainable", orthogonal to scaling.
  https://huggingface.co/papers/2608.25593 + https://huggingface.co/JIT-Agent/jit-27b
- arXiv surveys on harness engineering (Aug 24): https://arxiv.org/html/2604.08224v1
- @omarsar0 thread on context/memory papers (Aug 22, high engagement): https://x.com/omarsar0/status/2091199978014458081
- GitHub "best-of-Agent-Harnesses" curated list
- → Natural sequel to `deepseek-harness.md` teardown

## 3. GLM-5.3 open weights (released TODAY Aug 28)
- 744B total / 40B active MoE, 1M context, day-0 vLLM support
  https://x.com/AGTPinsights/status/2093406210519183497
- Debate: open weights + JIT harness competitive with GPT-5.6; local viability, cost, sovereignty
- → Newsy; pairs with harness angle

## 4. Inference cost economics (unit economics of agents)
- @johniosifov thread (Aug 24, citing Gartner etc.): cheaper tokens did NOT reduce bills — agentic chaining 8-15 calls/task, reasoning models 10-40x cost, data engineering 25-40% of spend, budget overruns
  https://x.com/johniosifov/status/2091969700884345213
- Focus shifting to workflow-level ROI, unit economics, hidden multipliers
- → Pairs with unpublished batch-requests slot (Slot 3)

## 5. Context engineering as active inference
- Self-improving memory harnesses: 7.7pp accuracy gain, 4x token reduction; context acquisition as first-class optimization
  https://x.com/beamnxw/status/2090388376444719470 + omarsar0 thread above
- → Overlaps existing `context-engineering-in-production.md` draft (could refresh)

## 6. MCP's biggest update ever (VentureBeat)
- Stateless/serverless scaling, long-running tasks, OAuth/auth/permissions for agents, async roadmap; MuleSoft/Supademo/Cloudflare/Salesforce connector explosion (Aug 28 posts)
  https://venturebeat.com/infrastructure/mcp-just-got-its-biggest-update-ever-heres-what-changes-for-ai-agents
- → Feeds existing `mcp-vs-code.md` draft (add update section)
