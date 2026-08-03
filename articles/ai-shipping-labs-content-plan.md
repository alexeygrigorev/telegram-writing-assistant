---
title: "AI Shipping Labs Content Plan"
created: 2026-08-03
updated: 2026-08-03
tags: [ai-shipping-labs, courses, workshops, planning]
status: draft
---

# AI Shipping Labs Content Plan

The content plan for AI Shipping Labs[^3]. It covers three things:

- The gaps in the current workshop catalog
- How to repackage the existing sessions into courses
- Which workshops to run next

## Missing pieces, ranked

The plan for the next workshops in AI Shipping Labs starts from the holes in what already exists[^1]:

1. Observability and tracing - the biggest hole. LangChain's survey found that 89% of teams run observability and 52% run evals. We are the exact inverse.
2. Human-in-the-loop and approvals - zero coverage.
3. Agent memory - zero coverage, heavily searched in 2026.
4. Multi-agent orchestration - deferred in coding-agent-v2, never revisited.
5. MCP refreshed - one session, from September 2025.
6. Security and prompt injection - guardrails cover topicality, not adversarial input.
7. Cost and latency engineering - buried inside the eval workshop.

## Ten sessions are already one course

Ten of the 24 sessions are the same FAQ agent: MCP/PydanticAI, both guardrails sessions, end-to-end deploy, Lambda, SQLite/Turso, Cloudflare, Vercel, evals, and the agentic loop. That is already a production-engineering course. It just is not packaged as one[^2].

## Six courses

The existing sessions fit into six courses[^2].

### 1. Ship an AI Agent to Production

Sessions: loop → FastAPI/Docker/Railway/CI → Turso → Lambda/Cloudflare/Vercel → Temporal.

State: the one people ask for. Needs 2 new sessions (tracing, cost).

### 2. Agent Reliability

Sessions: guardrails ×2, eval framework, Batch/Flex.

State: needs 4 new sessions - tracing, evals-in-CI, prompt injection, online evals.

### 3. Retrieval and Context Engineering

Sessions: search engine, RAG, agentic RAG, SQLite vectors, Vectorize.

State: nearly shippable today. Needs memory and context engineering.

### 4. Build Your Own Coding Agent

Sessions: tools compared, coding-agent-v2, vibe coding, CV pipeline.

State: needs subagents, sandboxing, MCP refresh.

### 5. Land the AI Engineering Job

Sessions: portfolio, CV, LinkedIn, live take-home.

State: nearly shippable today. Needs an AI system design interview session.

### 6. Own Your Model Stack

Sessions: vLLM/RunPod.

State: thin. Needs fine-tuning, routing, benchmarking. Lowest priority.

## Next eight sessions

The order to run them in[^2]:

1. LangGraph HITL (today)
2. Tracing end to end
3. Agent memory
4. MCP refreshed
5. Evals in CI
6. Prompt injection
7. Subagents
8. Cost and latency

## Sources

[^1]: [20260803_073841_AlexeyDTC_msg4829.md](../inbox/used/20260803_073841_AlexeyDTC_msg4829.md)
[^2]: [20260803_074337_AlexeyDTC_msg4831.md](../inbox/used/20260803_074337_AlexeyDTC_msg4831.md)
[^3]: [20260803_074432_AlexeyDTC_msg4833.md](../inbox/used/20260803_074432_AlexeyDTC_msg4833.md)
