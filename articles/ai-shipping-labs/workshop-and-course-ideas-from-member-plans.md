---
title: "Workshop and Course Ideas from Member Plans"
created: 2026-06-25
updated: 2026-06-25
tags: [ai-shipping-labs, courses, workshops, ideas]
status: draft
---

# Workshop and Course Ideas from Member Plans

A set of workshop and course ideas grounded in member data: 22 individual member plans, the four-persona synthesis, the cross-cutting patterns doc, the production sprint rosters (29 plans in May 2026, 16 in July 2026), and the underlying zoom-call and interview corpus[^1].

## What the CRM and plans show people struggle with

Ranked by how often the blocker appears across plans, interviews, and 1:1 calls[^1]:

| Problem | How it shows up | Who (examples) |
|---------|-----------------|----------------|
| The last-mile deploy gap | "It doesn't go beyond my laptop." PoC/notebook never becomes a live URL | Edu, Juan, Manjunath, Nirajan, Luca |
| No evaluation discipline | Can't tell if changes help; no eval set; "no eval culture" in prior roles | Universal - every plan has an eval week |
| Choosing one project / FOMO / analysis paralysis | "More ideas than time"; "content isn't the problem, accountability is" | Daiyaan, Diogo, Dianne, Jakob, Koray |
| AI as a black box | Heavy coding-agent use but "I don't understand what it's doing/why" | Daniel, Koray, Sergey, Jakob |
| Scripts -> systems engineering gap | Fine with pandas/functions, lost on project structure, classes, APIs, Docker | Daniel, Sai, Valeriia, Jakob (the Sam persona) |
| Jumping to agents too early | Reach for multi-agent before plain functions work | Sai, Diogo (named anti-pattern in every plan) |
| Monitoring / observability | No traces; failures and slow tool calls invisible | Alex + Priya plans (Logfire pattern) |
| Production patterns / system design | Dockerization, scalability, security, multi-tenant | Juan, Nirajan, Luciano |
| CI/CD + eval gating | GitHub Actions, regression gating, dev/prod split, Terraform | Edu, Juan, Manjunath |
| Career positioning | Portfolio that reads to a hiring committee, JD mining, LinkedIn cadence, applying early | Manjunath, Kushal, Luca, Aashiesh, Sai |
| RAG / retrieval depth | Chunking, hybrid retrieval, reranking, measured tuning | Aashiesh, Juan, Daniel (LLM ZC prep) |
| Coding-agent team workflows | Want the spec-driven manager/dev/tester sub-agent pattern | Motasem, Ivan Dubograi, Chandra, Eva |
| Cost / latency | Optimize spend and speed with measured before/after | Manjunath, Chandra |

## 10 workshop ideas

Single live sessions, each ends in a shippable artifact[^1].

1. Laptop PoC -> Live URL in one session - Dockerize a working prototype and deploy it to a Hugging Face Space / Fly.io / Lambda with HTTPS and basic auth. Attacks the #1 most-named gap. Serves Edu, Juan, Manjunath, Luca, Nirajan.

2. Build Your First Eval Set - Assemble 20-50 representative inputs, choose LLM-as-judge vs assertion checks, turn it into a scoreboard you can rerun. The universal week-4 need, made standalone.

3. Eval Gating in CI - Wire the eval set into GitHub Actions so failing scores block a merge; dev-deploy-on-push with a manual production gate. Serves Edu, Juan, Manjunath.

4. Functions First, Agent Second - Build plain-function tools, call them from a REPL, then wrap them in a single agent loop; explicit guidance on when multi-agent is and isn't worth it. Directly counters the most common anti-pattern (Sai, Diogo).

5. Stop Treating AI as a Black Box - Set up a Python project by hand (`uv`, `pyproject.toml`, package layout), then read AI-generated code line by line and rebuild one component yourself. Serves Daniel, Koray, Jakob, Sergey.

6. Pick One Project and Actually Commit - Run the brainstorming-gist + four-criterion fit-check live (voice/dictation brainstorming), kill FOMO, leave with one scoped project card. Serves the analysis-paralysis cluster (Daiyaan, Diogo, Dianne, Jakob).

7. See Inside Your LLM App: Tracing with Logfire - Add monitoring so an end-to-end trace from user input to final answer is readable; spot slow/failing tool calls. Serves the Alex/Priya production cohort.

8. Productionizing a RAG: Chunking, Hybrid Retrieval, Reranking - Run principled retrieval experiments scored against your eval set instead of vibes. Serves Aashiesh, Juan, and everyone heading into LLM Zoomcamp.

9. Spec-Driven Development with a Team of Coding Agents - The manager/dev/tester sub-agent pattern in Claude Code/Codex, spec-first discipline, frontend+backend+e2e through agents. Serves Motasem, Ivan Dubograi, Chandra, Eva.

10. From Build to Hired - Mine 10 job descriptions for the language to mirror, write a README a hiring committee can read, start the one-post-per-week LinkedIn series, and apply early to surface real interview questions. Serves Manjunath, Kushal, Luca, Aashiesh, Sai, Koray.

Bench ideas (alternates): Cost & Latency Optimization (measure, then cut - Manjunath, Chandra); Secrets & Security for Solo Builders (env/secret stores, basic auth, not indexing your demo)[^1].

## 3 mini-course ideas (5-day, AI-Hero-style)

Mapped to the three biggest gaps; each picks up where AI Hero leaves off rather than overlapping it[^1].

### Course 1 - Production AI in 5 Days (the universal next step after AI Hero)

The single most common gap across all four personas: a working prototype that never becomes a real, trustworthy, deployed system.

- Day 1: Deploy your PoC to a live URL (Docker + host + HTTPS + auth)
- Day 2: Build a 20-50 input eval set with LLM-as-judge
- Day 3: Eval gating in GitHub Actions
- Day 4: Monitoring and tracing
- Day 5: Cost/latency pass + README + demo

Serves Edu, Juan, Manjunath, Nirajan, Luca, Aashiesh.

### Course 2 - Scripts to Systems: Python Engineering for AI Builders (the Sam persona, longest path)

For people who can write data scripts but not software systems, and who lean on AI as a black box.

- Day 1: Project structure by hand (`uv`, packages, entry points)
- Day 2: Functions and classes you can read and reason about
- Day 3: APIs and HTTP clients
- Day 4: Docker and environments
- Day 5: First LLM integration + critically reading AI-generated code

Serves Daniel, Jakob, Sai, Sergey, Koray, and the non-programmer Sams.

### Course 3 - Agentic Coding: Build with a Team of AI Agents (the power-user / Alex-Priya track)

For heavy coding-agent users who want the spec-driven multi-agent workflow instead of one-shot prompting.

- Day 1: Pick one assistant + paid plan, set up the workspace
- Day 2: Spec-driven development discipline
- Day 3: The manager/dev/tester sub-agent pattern
- Day 4: End-to-end tests driven by agents
- Day 5: Ship a full-stack feature through the agent team

Serves Motasem, Ivan Dubograi, Chandra, Eva.

## Strongest single bet

The deploy-eval-monitor-CI arc (Course 1 / Workshops 1-3) is the one gap that literally every plan hits in months 2-3, regardless of persona[^1].

## Sources

[^1]: [20260625_095357_AlexeyDTC_msg4631.md](../../inbox/used/20260625_095357_AlexeyDTC_msg4631.md)
