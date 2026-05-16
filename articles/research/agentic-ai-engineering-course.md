---
title: "Agentic AI Engineering Course (Towards AI)"
created: 2026-03-12
updated: 2026-03-12
tags: [research, ai-engineering, courses, agents, competitor]
status: draft
---

# Agentic AI Engineering Course (Towards AI)

A paid course ($499) called "Agentic AI Engineering" by Towards AI (Louis-Francois Bouchard / @Whats_AI) and Decoding AI (Paul Iusztin). It teaches production-grade AI agent development through 34 lessons, 17 Jupyter notebooks (available free on GitHub), and a complete multi-agent project. Self-paced with lifetime access[^1].

[Source tweet](https://x.com/Whats_AI/status/2032064189141856572)

[Course page](https://academy.towardsai.net/courses/agent-engineering)

[GitHub repo (free notebooks)](https://github.com/towardsai/agentic-ai-engineering-course)

## Course Structure

Part 1 - Foundations (Lessons 1-11, first 6 lessons free preview):
- Structured Outputs
- Workflow Patterns
- Tools
- ReAct Practice
- Memory and Knowledge Access
- Multimodal

Part 2 - System Design (Lessons 12-14):
- Central project scoping and design
- Agent frameworks overview and comparison
- LLM agent system design considerations

Part 3 - Research Agent "Nova" (Lessons 15-19):
- End-to-end project walkthrough
- Foundations with FastMCP
- Data ingestion and tooling
- Research loop with query generation, Perplexity, and human feedback
- Final outputs and agent completion

Part 4 - Writing Workflow "Brown" (Lessons 20-26):
- Iterating AI architectures
- Writing workflow foundations
- Evaluator-optimizer pattern
- Human-in-the-loop via MCP servers
- Orchestrate and integrate capstone agents
- End-to-end demo: generating a course lesson

Part 5 - LLMOps and Deployment (Lessons 27-34):
- Agent observability with Opik
- Creating datasets for AI evals
- Evaluation processes and metrics theory
- Evaluating the writing workflow
- Continuous Integration for AI engineering
- Deployment prep: authentication (Descope), Docker, Cloud SQL
- Continuous Deployment for AI engineering

Part 6 - Certification Project:
- Build your own MCP server implementing advanced agent patterns, evaluation systems, and observability

## Two Production Agents Built in the Course

1. Nova Research Agent - an autonomous research system that crawls websites, GitHub repos, and YouTube videos. Uses ReAct reasoning loops for iterative research. Integrates Firecrawl, gitingest, Gemini, and Perplexity via function calling. Has human-in-the-loop feedback with user-approved query workflows.

2. Brown Writing Workflow - transforms research into publication-ready content. Uses multi-modal generation (text, Mermaid diagrams, images). Chain-of-thought prompting for long-form content. Evaluator-optimizer pattern for automated quality control loops. Orchestrator-worker architecture with context engineering for style control. MCP-based editing tools for real-time collaboration with Cursor. LangGraph workflows for production pipeline orchestration.

## Technology Stack

- Language model: Google Gemini (primary), also references Perplexity
- Frameworks: LangGraph (functional API for stateful orchestration)
- MCP: FastMCP for tool integration
- Tools: Firecrawl (web crawling), gitingest (GitHub repos)
- Observability: Opik (monitoring, debugging, tracing)
- Auth: Descope
- Database: Cloud SQL
- Deployment: Docker, Google Cloud Run, CI/CD pipelines
- Package management: uv (with pyproject.toml)
- IDE integration: Cursor, Claude

## Key Themes

1. "Notebooks are not enough" - the course argues that production agent engineering requires real codebases, Docker, CI/CD, and deployment pipelines beyond notebooks.

2. Decision framework for "to agent or not to agent" - when to use deterministic routing vs agent autonomy, when to keep humans in the loop.

3. Evaluator-optimizer pattern - automated quality control loops where an evaluator LLM judges agent outputs and an optimizer refines them.

4. Mental models over framework knowledge - building understanding that outlasts any particular framework.

5. MCP as the integration layer - FastMCP used for both research agent tools and human-in-the-loop editing. The certification project is to build your own MCP server.

6. Context engineering for style control - the writing workflow uses an orchestrator-worker architecture with deliberate context engineering to maintain consistent writing style.

## GitHub Repo Details

Repository: towardsai/agentic-ai-engineering-course (25 stars, 12 forks, 4 contributors, 231 commits). 87.1% Jupyter Notebook, 12.9% Python. Uses uv for package management. All notebooks in the lessons/ directory. Has .mcp.json and .cursor directory (Cursor IDE integration).

The 17 notebooks are freely available without purchasing the course. They cover: structured outputs, workflow patterns, tools, ReAct practice, memory/knowledge access, multimodal, FastMCP, data ingestion, research loops, writing workflow foundations, evaluator-optimizer, human-in-the-loop, agent integration, AI evals, and CI.

## Relevance

Competitor course worth studying. The "Research Agent + Writing Workflow" pattern is essentially what the telegram-writing-assistant project does at a high level - research/ingest content, then produce structured written output.

Connects to existing research topics: spec-driven development / multi-agent teams, MCP servers, context engineering. Paul Iusztin (Decoding AI) also appears in social-post-ideas.md with posts on learning AI engineering and AI evals.

The free notebooks on GitHub could be useful as reference material.

## Sources

[^1]: [20260312_173801_AlexeyDTC_msg2884.md](../../inbox/used/20260312_173801_AlexeyDTC_msg2884.md) - Research request
