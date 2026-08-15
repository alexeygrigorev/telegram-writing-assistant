---
title: "Research: MCP vs Code"
created: 2026-08-15
tags: [research, mcp, article-2]
---

# Article 2: "MCP Is Dead, Long Live Code?"

## The bearish case
- **Jasper Lu (@lu__jasper)**, Aug 5, 2026: "I was already bearish on MCPs after playing around with custom agent harnesses. But after seeing these results [Prime Agent], I'm convinced MCPs and custom tools were an expensive mistake. These models.. all they want to do is write code."
  https://x.com/lu__jasper/status/2085117746686083226
  - Problems: poor composition of tool calls, exporting results (re-emission of tokens), retrying code via tools forces re-emitting full code
  - Contrast: REPL/CLI harnesses store code in files/variables for in-place editing, loops for orchestration
  - Follow-up: https://x.com/lu__jasper/status/2085249778242224634
- **Matt Shumer (@mattshumer_)**: convert MCP specs into code functions — "Models have seen FAR more code than they have tool calls... instead of doing 50 calls... a model can just write a for loop... with way fewer tokens."

## The bullish case
- **Rhys Sullivan (@RhysSullivan)**, July 23, 2026: "There's basically no difference in the effectiveness of MCP and CLIs + skills for agents... CLIs are fine, but require basically a full sandbox... they're also lossy—you can't know without running a CLI what operations it contains... with MCP you can do tool search. Your users want both."
  https://x.com/RhysSullivan/status/2080117243405635832
- **Security/governance**: scoped identity-based tool lists, authorization checks, interceptors blocking dangerous commands / .env reads
  https://x.com/Mattjgale87/status/2088438982652654046
- **Scoping + registries**: tool groups instead of full server load → 80–90% context reduction; registries for discoverability
  https://x.com/zooper_man/status/2086821786856165771

## The hybrid (both sides converge here?)
"Code execution with MCP" — Python orchestration on top of MCP tools:
- AI Multiple benchmark: 100% success rate, ~78.5% input token reduction (15,417 → 3,310), +7% latency
  https://aimultiple.com/code-execution-with-mcp
- GetMaxim "Code Mode": 96→508 tools, 58–92.8% input token reduction, 55.7–92.2% cost cut, 100% pass rate
  https://www.getmaxim.ai/articles/code-execution-with-mcp-how-code-mode-cuts-agent-token-costs-by-90/
- CLI vs MCP token comparisons: 92–94% savings on repeated calls; near-zero init vs ~55k tokens for large MCP sets
  https://manveerc.substack.com/p/mcp-vs-cli-ai-agents
  https://vensas.de/en/blog/mcp-vs-cli-cost-comparison

## Angle (working thesis)
The MCP-vs-code fight is real and the data is surprisingly one-sided on tokens — but the answer isn't picking a side, it's the hybrid: MCP for discovery/governance, code for orchestration. When to choose which.

**Best template:** Strategic Essay + Framework
**Personal material:** OpenClaw itself (MCP tools + code via exec) is a living hybrid example.
