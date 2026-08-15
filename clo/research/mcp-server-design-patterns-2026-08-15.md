---
title: "Research: MCP Server Design Patterns"
created: 2026-08-15
tags: [research, mcp, article-1]
---

# Article 1: "How Many Tools Is Too Many? MCP Design Patterns That Actually Work"

## Core paper
**"MCP Server Architecture Patterns for LLM-Integrated Applications"** (arXiv, submitted June 29, 2026)
- Lead author: Carson Rodrigues (Celabe), co-author Oysturn Vas
- https://arxiv.org/abs/2606.30317
- Replication package: https://github.com/rodriguescarson/mcp-patterns-icsme2026

### Key findings
- Accuracy drops below 90% between **10–15 tools** for Claude Haiku 4.5
- Between **20–30 tools** for Sonnet 4
- Five patterns (GoF style — context/problem/solution/consequences):
  1. Resource Gateway
  2. Tool Orchestrator
  3. Stateful Session Server
  4. Proxy Aggregator
  5. Domain-Specific Adapter
- Plus 4 anti-patterns, cross-cutting concerns (auth, versioning, observability)
- Cohen's κ = 0.76 inter-rater reliability; stdio transport ~0.01 ms p50

## Production experience: tool sprawl
- **Datadog engineering blog** — "Designing MCP tools for agents": flexible/multi-purpose tools (one tool serving multiple use cases), toolsets (default core sets), layering (chained tools). Trade-off: added latency for chaining.
  https://www.datadoghq.com/blog/engineering/mcp-server-agent-tools/
- **Gravitee** — composite/virtual MCP servers: bundling multiple servers into role-based exposures, explicit handles for stateful workflows.
  https://www.gravitee.io/blog/what-is-a-composite-mcp-server
- **Qualys** — "MCP Servers: The New Shadow IT for AI in 2026": sprawl as API sprawl 2.0; zero-trust, sandboxing, scoped credentials.
  https://blog.qualys.com/product-tech/2026/03/19/mcp-servers-shadow-it-ai-qualys-totalai-2026
- Medium summary with the headline numbers: "91% at 10 tools, 87% at 15"
  https://medium.com/@meshuggah22/91-at-10-tools-87-at-15-the-five-architecture-patterns-behind-reliable-mcp-servers-11fef1bbe401

## X/Twitter signal
- @rohanpaul_ai paper breakdown thread: https://x.com/rohanpaul_ai/status/2072499557712507190
- @DavidLinthicum on MCP stack fragility: https://x.com/DavidLinthicum/status/2088385546578018582
- @Aurimas_Gr on MCP in agentic RAG: https://x.com/Aurimas_Gr/status/2084608000610754903

## Angle (working thesis)
Most teams don't need more tools — they need fewer, grouped better. Practical guide through the 5 patterns + Datadog/Gravitee production lessons + the hard numbers on when accuracy breaks.

**Best template:** Practical Workflow / Tool Teardown
**Personal material:** OpenClaw/ClawHub MCP setups used daily.
