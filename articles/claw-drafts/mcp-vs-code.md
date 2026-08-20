# Too Many Tools: What the MCP Backlash Gets Right, and What It Misses

> Subtitle: The evidence on when tool-calling breaks down, when writing code wins, and a framework for giving agents the right surface area.

[IMAGE: Line chart of agent accuracy vs number of tools, with breakpoints marked at 10, 15, 20, and 30 tools]
Caption: 1. Claude Haiku 4.5 drops below 90% accuracy between 10 and 15 tools. 2. Sonnet 4 holds on until 20 to 30. Source: arXiv 2606.30317.

91% accuracy at 10 tools. 87% at 15. [A June 2026 paper](https://medium.com/@meshuggah22/91-at-10-tools-87-at-15-the-five-architecture-patterns-behind-reliable-mcp-servers-11fef1bbe401) put hard numbers on something most of us have already felt: somewhere between "a few tools" and "all the tools," agents get worse at picking the right one.

Around the same time, a second argument started circulating among practitioners: stop adding tools altogether. Models have seen far more code than tool calls during training, so let them write code instead of poking an API one call at a time. The people making this argument have benchmarks too, and their numbers look even more dramatic: token cuts of 58 to 94% when generated code replaces repeated tool calls.

Both camps have a point, and both overreach. The tool-count research is solid, and it points at design problems, not at a broken protocol. The code-first results are real, and they quietly assume things most teams can't give an agent: a sandbox, a filesystem, and someone watching what the code does.

This piece walks through the evidence on both sides, then combines them into one framework you can apply on Monday. I'll also show a working example of the hybrid running on my own desk.

### The accuracy cliff is real

[MCP Server Architecture Patterns for LLM-Integrated Applications](https://arxiv.org/abs/2606.30317) (arXiv, June 2026, lead author Carson Rodrigues) tested how agent accuracy scales with tool count. The breakpoints:

- Claude Haiku 4.5 drops below 90% accuracy somewhere between **10 and 15 tools**.
- Sonnet 4 holds on until roughly **20 to 30 tools**.

Stronger models buy you headroom, and every model eventually hits the same wall. More candidate tools mean more ways to pick the wrong one, more tokens spent on descriptions, and more chances for two tools to look interchangeable.

The paper's answer is architectural. The authors catalogued five patterns in the GoF style (context, problem, solution, consequences): **Resource Gateway**, **Tool Orchestrator**, **Stateful Session Server**, **Proxy Aggregator**, and **Domain-Specific Adapter**, plus four anti-patterns and the cross-cutting concerns everyone forgets: auth, versioning, observability. There's a [replication package on GitHub](https://github.com/rodriguescarson/mcp-patterns-icsme2026) if you want to rerun the study.

Production teams arrived at the same place from the other direction. [Datadog's engineering team](https://www.datadoghq.com/blog/engineering/mcp-server-agent-tools/) recommends flexible, multi-purpose tools, default toolsets (a small core set exposed out of the box), and layered tools that chain into each other. [Gravitee](https://www.gravitee.io/blog/what-is-a-composite-mcp-server) builds composite servers that bundle multiple backends into role-based exposures. And [Qualys called MCP servers "the new shadow IT"](https://blog.qualys.com/product-tech/2026/03/19/mcp-servers-shadow-it-ai-qualys-totalai-2026), describing the current situation as API sprawl 2.0: everyone mounts another server, nobody tracks what's mounted.

Think of it as a toolbox. Hand a new hire a rolling cabinet with 300 drawers and ask for a #2 Phillips. They'll find it eventually, after opening the wrong drawer a few times. Hand them a belt with six tools and they'll reach without looking. Agent context works the same way: every tool description is a drawer label the model has to read, compare, and discard.

### The case for writing code instead

The strongest version of this argument comes from [Jasper Lu](https://x.com/lu__jasper/status/2085117746686083226), who benchmarked agents on custom harnesses and [Prime Agent](https://x.com/lu__jasper/status/2085249778242224634) results in August 2026 and concluded that "these models... all they want to do is write code." His complaints about tool-calling are structural:

- **Poor composition.** Chaining tool outputs into the next call is fragile; models fumble the plumbing.
- **Token re-emission.** Every call re-sends context. If a tool call fails and you retry through the model, the full payload goes over the wire again.
- **No in-place editing.** Code stored in files or variables can be patched. Code that lives inside a tool-call argument has to be regenerated from scratch.

[Matt Shumer](https://x.com/mattshumer_) pushes the same line: convert MCP specs into plain code functions, because "models have seen FAR more code than they have tool calls." Instead of 50 sequential calls, the model writes a for loop.

The benchmarks back this up more than I expected. [AI Multiple's "code execution with MCP" benchmark](https://aimultiple.com/code-execution-with-mcp) hit a 100% success rate with Python orchestrating MCP tools, cut input tokens by about 78.5% (15,417 down to 3,310), at the cost of 7% more latency. [GetMaxim's "Code Mode"](https://www.getmaxim.ai/articles/code-execution-with-mcp-how-code-mode-cuts-agent-token-costs-by-90/) grew a catalog from 96 to 508 tools while cutting input tokens by 58 to 92.8% and cost by up to 92%, with a 100% pass rate on their suite. Independent [CLI-vs-MCP](https://manveerc.substack.com/p/mcp-vs-cli-ai-agents) [comparisons](https://vensas.de/en/blog/mcp-vs-cli-cost-comparison) found 92 to 94% savings on repeated calls, and near-zero startup cost versus roughly 55,000 tokens to initialize a large MCP toolset.

Read that last number again. Loading a big tool catalog into context can cost more than most entire tasks.

### The case the backlash misses

Here is where the code-first crowd waves too fast past the costs. [Rhys Sullivan](https://x.com/RhysSullivan/status/2080117243405635832) ran the comparison and found "basically no difference in the effectiveness of MCP and CLIs + skills for agents." But his two caveats matter:

- **CLIs require basically a full sandbox.** If your agent executes arbitrary shell, you've given it the keys to wherever the shell runs.
- **CLIs are lossy.** "You can't know without running a CLI what operations it contains." With MCP, the tool list is a machine-readable contract, and you can do **tool search** over it.

That contract is worth more than it looks. Because tool calls are structured and declared up front, you can govern them: [scoped, identity-based tool lists](https://x.com/Mattjgale87/status/2088438982652654046) with authorization checks, interceptors that block dangerous commands and .env reads before they execute. And because discovery is declarative, you don't need the full catalog in context: [tool groups and registries](https://x.com/zooper_man/status/2086821786856165771) load tools on demand and cut context usage by 80 to 90%.

Code gives you none of that for free. A generated for loop with a bug in it is just... a bug, executed at full speed, with whatever permissions the sandbox has. As Sullivan put it: "Your users want both."

Back to the workshop metaphor. Code is the workbench: unlimited flexibility, real power, and the occasional severed finger. Tools are the labeled drawers: findable, checkable, lockable. A workshop with only drawers can't build anything new. A workshop with only a bench and no storage spends half the day hunting for the screwdriver. You need the room, with both in it.

**Tools for discovery, permissions, and audit. Code for everything else.**

### The framework: Small Surface, Deep Reach

Five rules, each with why it matters, how to apply it, and the trap waiting for you.

### 1. Budget tools like a scarce resource

Pick a tool budget per agent and enforce it. For smaller models, aim for about 10 active tools; frontier models stay reliable up to roughly 25. Everything else goes behind groups or search.

**Why it matters:** the accuracy cliff is measurable and steep. Below 90% tool-selection accuracy, your agent is wrong one time in ten before it even starts the actual task.

**Practical applications:**
- **Default toolsets.** [Datadog's approach](https://www.datadoghq.com/blog/engineering/mcp-server-agent-tools/): expose a small core set out of the box, expand on demand.
- **Role-based composite servers.** [Gravitee](https://www.gravitee.io/blog/what-is-a-composite-mcp-server) bundles backends and exposes slices per role instead of everything to everyone.

**The trap to avoid:** counting servers instead of tools. Three "small" servers with 15 tools each is a 45-tool agent.

### 2. Prefer flexible tools over many narrow ones

One tool that covers a family of use cases beats five variants with slightly different names.

**Why it matters:** near-duplicate tools are the fastest way to confuse selection. The model spends its attention discriminating between options instead of doing the job.

**Practical applications:**
- **Multi-purpose tools.** [Datadog](https://www.datadoghq.com/blog/engineering/mcp-server-agent-tools/) designs one tool to serve several use cases, with parameters doing the work.
- **Layered tools.** Coarse tools for common paths, fine-grained ones reachable through chaining.

**The trap to avoid:** the god tool with 20 required parameters. Flexible means good defaults, not a config form.

### 3. Make discovery lazy

Keep descriptions out of context until something needs them.

**Why it matters:** initializing a large catalog can cost ~55k tokens [before the task even starts](https://vensas.de/en/blog/mcp-vs-cli-cost-comparison). Registries and tool groups cut context usage by [80 to 90%](https://x.com/zooper_man/status/2086821786856165771).

**Practical applications:**
- **Tool search.** Expose a searchable index instead of the full list, [as Sullivan describes](https://x.com/RhysSullivan/status/2080117243405635832).
- **On-demand groups.** Load a domain's tools when the task touches that domain.

**The trap to avoid:** lazy discovery that's also lazy documentation. The index entry still has to be good enough to rank the right tool.

### 4. Govern at the tool boundary

Treat every tool as an API endpoint with auth, scopes, and an audit log.

**Why it matters:** Qualys calls MCP sprawl [the new shadow IT](https://blog.qualys.com/product-tech/2026/03/19/mcp-servers-shadow-it-ai-qualys-totalai-2026). Ungoverned tool access is how an agent ends up reading .env files or deleting production data with valid credentials.

**Practical applications:**
- **Scoped credentials per tool.** Zero-trust, sandboxing, short-lived tokens.
- **Interceptors.** [Identity-based authorization checks](https://x.com/Mattjgale87/status/2088438982652654046) and command filters that block dangerous operations before execution.

**The trap to avoid:** one admin token in the environment, shared by every tool on the server.

### 5. Keep a code escape hatch

Give the agent a way to write a loop, a script, or a one-off transformation when tools run out.

**Why it matters:** the code-mode numbers ([58 to 93% input token cuts](https://www.getmaxim.ai/articles/code-execution-with-mcp-how-code-mode-cuts-agent-token-costs-by-90/), 100% pass rates in the [AI Multiple benchmark](https://aimultiple.com/code-execution-with-mcp)) come precisely from the cases where tools are worst: repetition and composition.

**Practical applications:**
- **Code orchestration over MCP tools.** Python for the loop, tool calls for the actions.
- **In-place editing.** Store generated code in files so retries patch instead of regenerate, [Lu's core point](https://x.com/lu__jasper/status/2085117746686083226).

**The trap to avoid:** code execution without approvals and sandboxing. That's a remote code execution service with a chat UI bolted on.

### OpenClaw: the hybrid on my desk

I've been running [OpenClaw](https://github.com/openclaw/openclaw), an open-source, self-hosted assistant gateway ([docs here](https://docs.openclaw.ai)), as my daily Telegram assistant. It's a useful case study because it implements all three extension mechanisms side by side:

- **Skills:** markdown playbooks in a workspace. Only the index (name + description) sits in context; the body loads when a task matches. Lazy discovery, human format.
- **Structured tools:** shell, file I/O, browser, web search, and MCP servers. Permissioned, observable, some gated behind explicit approval before they run.
- **Raw code:** the agent can write and execute scripts on the host whenever composition beats tool calls.

In daily use, the split is exactly what the framework predicts. Single lookups and defined actions go through tools, where the permissioning and logging live. Anything repetitive or compositional, batch processing, data munging, multi-step research, becomes a script. The agent decides per task, and it's usually right.

(The assistant that helps draft my articles runs on this setup too. Make of that what you will: either a conflict of interest, or the most honest case study I have.)

### The checklist

Copy, paste, and run against your own agent:

- [ ] Count **tools per agent**, not servers. Under ~10 for smaller models, under ~25 for frontier.
- [ ] Audit for near-duplicates. Merge into one flexible tool with parameters and defaults.
- [ ] Move full catalogs behind **search or groups**. Measure context usage before and after.
- [ ] Scope **credentials per tool**. Add interceptors for destructive operations.
- [ ] Provide a **code path** for loops and composition, sandboxed and approval-gated.
- [ ] Track three numbers weekly: tokens per task, tool-selection accuracy, cost per completed run.

### Close

Here's what I believe: the MCP backlash will lose the war and win the argument. Tool catalogs will keep growing because integrations keep growing, and that's fine. The teams that win are the ones that stop treating tools as plugins to collect and start treating them as a product surface: few of them, flexible, lazily discovered, tightly governed, with code waiting behind them for everything else.

Sincerely,
Alexey

---

## Platform Deltas

**Substack (Alexey On Data):**
- URL: https://aishippingblog.com
- Subtitle: The evidence on when tool-calling breaks down, when writing code wins, and a framework for giving agents the right surface area.
- Paywall: place `[PAYWALL BREAK — free preview ends here]` after "The case the backlash misses".
- Ends on the Sincerely / Alexey signoff.

**Medium:**
- 5 topic tags: Artificial Intelligence, Machine Learning, LLM, AI Agents, MCP
- Member-only: no
- Ends on the community CTA: "Thanks for reading! If you found this useful, subscribe for more AI engineering deep dives..."

---

## SEO Keywords

- MCP design patterns
- how many tools for AI agent
- MCP vs code execution
- agent tool selection accuracy
- code mode LLM agents
- MCP tool sprawl
- AI agent token cost reduction
- MCP server architecture
- tool calling best practices
- OpenClaw self-hosted AI assistant

---

## Title & Subtitle Shortlist (for publish-time selection)

### Titles
1. Too Many Tools: What the MCP Backlash Gets Right, and What It Misses
2. 91% at 10 Tools, 87% at 15: The Real Limits of MCP (and Where Code Wins)
3. MCP vs Code: What the Numbers Actually Say
4. Your Agent Doesn't Need More Tools. It Needs Better Ones (and a Place to Write Code)
5. The MCP Backlash, Settled With Numbers

### Subtitles
1. The evidence on when tool-calling breaks down, when writing code wins, and a framework for giving agents the right surface area.
2. Tool-count research, code-mode benchmarks, and five rules for the hybrid that beats both extremes.
3. From a June 2026 accuracy study to a home-server case study: how to give agents few tools, good tools, and code for the rest.
