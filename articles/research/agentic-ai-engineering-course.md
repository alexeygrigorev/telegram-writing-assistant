---
title: "Agentic AI Engineering Course (Towards AI)"
created: 2026-03-12
updated: 2026-03-12
tags: [research, ai-engineering, courses, agents, competitor]
status: draft
---

# Agentic AI Engineering Course (Towards AI)

A paid course ($499) called "Agentic AI Engineering" by Towards AI (Louis-Francois Bouchard / @Whats_AI) and Decoding AI (Paul Iusztin). It teaches production-grade AI agent development through 34 lessons, 17 Jupyter notebooks (available free on GitHub), and a complete multi-agent project. Self-paced with lifetime access[^1].

Source tweet: https://x.com/Whats_AI/status/2032064189141856572

Course page: https://academy.towardsai.net/courses/agent-engineering

GitHub repo (free notebooks): https://github.com/towardsai/agentic-ai-engineering-course

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

2. Brown Writing Workflow - transforms research into polished content. Uses evaluator-optimizer pattern with iterative quality improvement. Implements MCP servers for human-in-the-loop review. Handles multi-format output (markdown, HTML, presentations).

## Notes

Competitor course - worth studying to see their approach to teaching AI agent development. Paul Iusztin (Decoding AI) is also behind posts on learning AI engineering and AI evals that appeared in social-post-ideas.md. The free notebooks on GitHub could be useful as reference material.

## Sources

[^1]: [20260312_173801_AlexeyDTC_msg2884.md](../../inbox/used/20260312_173801_AlexeyDTC_msg2884.md) - Research request
