---
title: "Research: Durable Agents & Durable Execution"
created: 2026-08-18
tags: [research, durable-agents, durability, agent-runtimes]
source: Grok `durable-agents-aug2026` (20260818_163736), raw JSON in
`~/git/ai-engineering-field-guide/_work-in-progress/grok-responses/`
---

# Durable Agents / Durable Execution (for agents)

## What it is
Durable execution engines (Temporal, Restate, DBOS, Resonate, Inngest, cloud offerings) give agents checkpointing, journaling/replay, crash recovery, retries, timers, state persistence. Solves: partial failures in tool calls/LLM invocations, lost progress on restart, duplicated side effects, human-in-the-loop without hand-rolled recovery.

Core idea: agent steps (especially non-deterministic ones: LLM calls, tools) become durable primitives. Completed work persists (event history / journal / DB) → deterministic replay or resume from last checkpoint. Frameworks (LangGraph, Pydantic AI, OpenAI Agents SDK) now integrate these layers.

## Who runs it in production
- **Temporal** — strongest footprint:
  - OpenAI Codex (web coding agent, millions of requests)
  - Replit Agent 3 (millions of long-running agents)
  - Gorgias (customer service across 15,000 brands; retries, sagas, human-in-the-loop)
  - ZoomInfo, NVIDIA (GPU orchestration)
- **DBOS** — Postgres-backed library, LangGraph/OpenAI Agents integrations, crashproof agents; fewer mega-scale named deployments
- **Restate** — journaled steps, low-latency push model, Vercel/OpenAI SDK support
- **Resonate** — "agent-native" positioning, Synadia/NATS partnership, Supabase-backed durable agents; early
- Cloud: AWS Durable Functions, Cloudflare Workflows, Azure Durable Task for agents

## Key sources
- Jack Vanlightly, "Demystifying Determinism in Durable Execution" (Nov 2025) — the best neutral deep-dive covering Temporal/Restate/DBOS/Resonate:
  https://jack-vanlightly.com/blog/2025/11/24/demystifying-determinism-in-durable-execution
- Temporal: "AI reliability is a decade-old problem" https://temporal.io/blog/ai-reliability-is-a-decade-old-problem
- Temporal: dynamic agents on Temporal https://temporal.io/blog/of-course-you-can-build-dynamic-ai-agents-with-temporal
- DBOS: "Durable Execution for Building Crashproof AI Agents" (Feb 2025) https://www.dbos.dev/blog/durable-execution-crashproof-ai-agents
- DBOS vs Temporal comparison: https://www.dbos.dev/compare/dbos-vs-temporal + https://tiarebalbi.com/en/blog/dbos-vs-temporal-postgres-durable-execution
- Restate vs Temporal latency: https://restate.dev/vs/temporal (claims sub-170ms P99 for 10-step workflows)
- Restate: durable AI loops across frameworks https://restate.dev/blog/durable-ai-loops-fault-tolerance-across-frameworks-and-without-handcuffs/
- Maxim Fateev (Temporal CEO) interview on agents (Apr 2026): https://workos.com/blog/maxim-fateev-temporal-durable-execution-ai-agents
- Zylos survey "Durable Execution for AI Agent Runtimes" (Apr 2026): https://zylos.ai/research/2026-04-24-durable-execution-agent-runtimes/
- Pydantic AI durable execution docs: https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/
- Resonate why-page: https://docs.resonatehq.io/evaluate/why-resonate

## The debates
1. **Determinism vs AI non-determinism** — engines need deterministic workflow code; LLM calls isolated as steps/activities. Exactly-once semantics, avoiding re-execution of expensive LLM/tool steps on replay (Vanlightly dissects this).
2. **Simplicity vs features** — DBOS "Postgres is enough" (library, 2-10x cheaper, 1-2ms step writes) vs Temporal (dedicated cluster, task queues, signals, multi-region) vs Restate (service, low-latency push).
3. **Checkpoint granularity** — every step vs coarser; suspend/resume for human-in-the-loop; multi-agent state sharing; avoiding duplicated side effects (double emails/bookings) on resume.
4. **Integration vs lock-in** — durability embedded in agent frameworks vs dedicated engines; does determinism constrain dynamic agents (Temporal argues no).
5. **"Persistence is the whole ballgame"** — X/Reddit consensus: long-horizon agents fail on infra gaps, not models. "Resume from step 37 of 40" framing.

## Numbers worth citing
- DBOS: 2-10x lower cost, 1-2ms Postgres step writes vs Temporal cluster overhead
- Restate: sub-170ms P99 for 10-step workflows under load
- Replit: millions of long-running agents on Temporal (Agent 3)
- OpenAI Codex on Temporal: millions of requests
- No peer-reviewed papers; content is engineering blogs + vendor comparisons (note for credibility framing)

## Fits content plan
Backlog slot: "Agent runtimes / long-horizon reliability". Pairs naturally with:
- context-engineering-in-production (memory/state) — durability = the execution side of the same problem
- MCP article (tool surface) — different layer

## Angle candidates
1. "Durable Agents: Stop Losing Step 37 of 40" — Practical Workflow: the failure modes of non-durable agents + engine landscape (Temporal/DBOS/Restate/Resonate) + when you actually need one vs a Postgres table
2. "Durable Execution for Agents, Demystified" — Concepts Explainer on replay/journaling/checkpointing mechanics (Vanlightly-based), with agent-specific twists (non-determinism, idempotent side effects)
3. "Postgres Is Enough for Agent Durability (Until It Isn't)" — tension piece: DBOS-style minimalism vs Temporal-scale, with decision framework

## Addendum: LangGraph checkpointing vs durable execution (17:22)
Grok `langgraph-checkpointing-vs-durable` (20260818_172330). Raw JSON in field-guide grok-responses.
- Checkpointer = thread-scoped state snapshots after each node (Postgres/Redis/SQLite). Gives resume, time travel (fork from any checkpoint), HITL interrupts.
- NOT durable execution: snapshots preserve data, journal preserves the run. Crash kills run; external code must detect + re-invoke thread_id. Nodes re-execute on resume (docs say keep mutations idempotent). Boundaries-only checkpointing (mid-node failures re-run whole node).
- Diagrid: "Checkpoints are not durable execution" https://www.diagrid.io/blog/checkpoints-are-not-durable-execution-why-langgraph-crewai-google-adk-and-others-fall-short-for-production-agent-workflows
- Temporal LangGraph plugin (public preview mid-2026): graphs as workflows, auto recovery + durable interrupts https://temporal.io/blog/temporal-langgraph-plugin-durable-execution + https://docs.temporal.io/develop/python/integrations/langgraph
- DBOS pairs with Postgres checkpointer for state+execution durability
- When LangGraph alone: short (<30s), read-heavy, prototypes, time-travel-first workflows. Add engine: >=3 external calls, mutations, human pauses. https://cordum.io/blog/temporal-vs-langgraph
- Also: https://appscale.blog/en/blog/durable-execution-llm-agents-temporal-langgraph-checkpointing-2026 ; older SQLite/Redis checkpointers had security issues (CSA note) https://labs.cloudsecurityalliance.org/research/csa-research-note-langgraph-rce-chain-20260614-csa-styled/
- Added as section "Graph checkpointing is not durable execution" in the article (before Durability Ladder); rung 2 wording adjusted (Pydantic AI only); SEO keyword added
