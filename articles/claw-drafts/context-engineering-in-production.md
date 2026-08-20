# Context Engineering in Production: What Survives Long Sessions

> Subtitle: Context rot is measurable, external memory is real, and the single-versus-multi-agent fight finally has data. A practical stack for agents that last longer than a demo.

[IMAGE: Diagram of an agent context window filling up over a long session: raw tool outputs accumulating, then compacted into summaries, with state persisted to external memory files]
Caption: 1. Session starts lean. 2. Tool outputs and history accumulate. 3. Compaction summarizes the past. 4. Durable state moves to external memory. 5. The window stays small.

A model provider advertises a million-token window. Your agent starts losing the plot somewhere around 100k. Same model, same prompts, same tools. The only thing that changed was how much history the agent was carrying.

That gap, between the advertised window and the window you can actually ship on, is where production context engineering lives. [Chroma tested 18 frontier models](https://www.trychroma.com/research/context-rot) on long-context tasks and found performance degrading non-linearly and unpredictably as input grows, often far below advertised limits. Practitioners who run long sessions see the same thing: quality holds for a while, then drops off a cliff that no changelog explains.

The field has converged on a name for this, **context rot**, and on a set of responses: compaction, external memory, and context isolation. This piece walks through what the evidence says about each, then assembles it into a stack you can apply to your own agents. I'll close with the memory system running on my own desk, because it turns out an assistant's brain is a decent case study.

### Context rot: the effective window is smaller than the sticker

[Chroma's technical report](https://www.trychroma.com/research/context-rot) ("Context Rot: How Increasing Input Tokens Impacts LLM Performance", July 2025) ran 18 models, including GPT-4.1, Claude 4, and Gemini 2.5, through needle-in-haystack variants, distractor interference, conversational QA, and repeated-word tasks. Findings in one paragraph: degradation is real, non-linear, and model-specific. Adding tokens can help one task and hurt another on the same model. Many models advertise far more context than they can use at high quality, and the effective window for demanding work is often cited below 256k tokens.

The mechanism is attention dilution. As context grows, the model's attention spreads across more tokens, and recall, instruction following, and reasoning all take hits. [Anthropic's engineering post on context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) describes the same pattern from the practitioner side: every token competes with every other token, so each addition dilutes the whole.

The production rule that falls out of this is unglamorous: treat your context budget like a memory budget in an older systems sense. You have an allocation. Everything in the window pays rent. [Redis's practitioners' guide](https://redis.io/blog/context-rot/) collects the field observations, including the common one that sessions degrade badly past roughly 100k tokens and may need a handoff or a fresh start.

**The window is a budget, and every token in it pays rent.**

### Compaction: shrink the past without lying about it

The first response to rot is to shrink what's in the window. **Compaction** summarizes older history so the session can continue: past tool outputs collapse into their conclusions, old decisions stay as one-liners, recent actions stay raw.

The technique is now standard equipment. [Anthropic describes Claude Code's compaction](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) as preserving key decisions and unresolved bugs while dropping redundant output. [LangChain's Deep Agents](https://www.langchain.com/blog/context-management-for-deepagents) trigger compression automatically at window thresholds, part of their four-strategy model: **Write** state externally, **Select** what enters, **Compress** what stays, **Isolate** contexts from each other.

The debates are in the details, and they matter:

- **What to preserve.** Architecture decisions age well. Verbatim tool output does not. The recurring practice is to keep recent actions raw and compress the older past, so the model can still quote the last error message while treating last week as a summary.
- **Reversibility.** A summary that loses the one detail you later need has quietly poisoned every downstream step. Keeping raw artifacts recoverable outside the window (a file, a log) turns lossy compression into an acceptable trade.
- **Evaluating compression.** Almost nobody measures whether their summaries are good. That's starting to change as teams treat compaction quality as a tested component rather than a hope.

The trap: compaction is an LLM call, so it costs tokens and latency, and its failures are silent. A bad summary looks exactly like a good one until three turns later.

### Memory outside the window

Compaction manages the session. **External memory** manages everything the session should stop carrying: facts, preferences, decisions, skills that survive across sessions.

The field has a working taxonomy, borrowed from cognitive science: *episodic* memory (what happened, when), *semantic* memory (facts and knowledge), and *procedural* memory (how to do things, playbooks). Production systems layer them: recent episodic detail stays hot, semantic facts get retrieved on demand, procedures live as files the agent loads when a task matches.

This area moved fast in 2026. [Mem0's State of AI Agent Memory report](https://mem0.ai/blog/state-of-ai-agent-memory-2026) compares about ten approaches head to head. Benchmarks like MemoryAgentBench and MemoryArena now evaluate incremental, multi-session tasks, profiling the write path and the read path separately, because a memory system is really two systems wearing a trenchcoat. The [Awesome-Memory-for-Agents](https://github.com/) collections curate the paper landscape: hierarchical memory, multi-agent memory, modular procedural designs.

Two arguments are live:

- **Simple vector stores versus structured memory.** Vector retrieval is easy to ship and weak on structure: it can't update a fact, it can only bury it under a newer similar fact. Knowledge graphs and actor-aware tagging (who wrote this memory, when, from what session) cost more to build and pay off in multi-agent settings where provenance prevents cross-agent contamination.
- **Memory shifts the bottleneck.** With a good external store, the constraint moves from window size to retrieval quality and consistency. An agent with a perfect memory it can't search is a filing cabinet with the keys lost inside.

On the research frontier, [Stanford's ACE framework](https://arxiv.org/abs/2510.04618) (Agentic Context Engineering) treats context as evolving playbooks: a Generator explores, a Reflector extracts insights, a Curator organizes them, and the playbook improves from execution feedback without fine-tuning. Reported gains: +10.6% on agent benchmarks, with cost and latency reductions. The direction is clear. Context stops being something you design once and becomes something the system maintains.

### Isolation: split the context, split the failure

The third response is architectural: stop giving one agent everything. [Sub-agent isolation](https://redis.io/blog/sub-agents-splitting-context-specialized-ai-agents/) scopes each context to a domain, role, or toolset, which buys precision and parallelism.

Isolation earns its keep in specific situations: when logical entities separate cleanly (one agent per repository, per customer, per data domain), when tool volume is high, or when precision matters more than conversational continuity. A research sub-agent that reads 40 documents and returns five findings keeps the 40 out of everyone else's window.

The costs are real and now measured. The [MAST taxonomy](https://www.oreilly.com/radar/why-multi-agent-systems-need-memory-engineering/), built from an analysis of 1,600+ real traces across AutoGen, CrewAI, and LangGraph, catalogs 14 multi-agent failure modes clustered around design, misalignment, and verification: agents losing track of each other, duplicating work, acting on stale state. One analysis links a large share of multi-step failures (on the order of two-thirds [VERIFY: pin down primary source before publishing]) to drift and memory loss. Coordination is a system you build, with shared memory rules and message-passing discipline, and it's the part teams underestimate.

Single agent with good compaction or team of isolated specialists: the honest answer is that it depends on whether your task decomposes cleanly. And increasingly, both sides need the same foundation, which brings us to the stack.

### The Production Context Stack

Five stages, in the order you should implement them.

### 1. Measure the effective window

Run your own degradation test: your tasks, your tools, growing history. Find the point where your agent's accuracy drops. That number, often far below the advertised limit, is your real budget.

**Practical:** reuse Chroma's needle-plus-distractor methodology on your own workload, or simply replay real sessions with history truncated at different lengths and compare outcomes. One afternoon of testing replaces a quarter of guessing.

### 2. Compact with a raw floor

Summarize the older past automatically. Keep the last N turns and the most recent errors raw and verbatim, and keep full logs recoverable in a file so compression is reversible in practice.

**Practical:** trigger compaction at a threshold (say, half your measured budget), preserve decisions and unresolved issues by name, and write the compacted summary to the session log alongside the raw history it replaced.

### 3. Externalize what survives the session

Move durable facts and procedures out of the window entirely: memory files the agent reads on demand. Episodic detail ages out, semantic facts get retrieved when relevant, procedures load when a task matches.

**Practical:** start with plain markdown files, loaded lazily. It's unglamorous and it works. Reach for graph memory and provenance tagging when multiple agents share one store.

### 4. Isolate contexts that don't belong together

Split by domain, toolset, or entity when precision beats continuity. Give each sub-agent a narrow window and a clear interface: what it receives, what it returns.

**Practical:** one research agent that reads a lot and returns little beats a chat agent that carries every document. Count the MAST failure modes against your design before you ship it: who owns shared state, who verifies results.

### 5. Evaluate context like a pipeline component

Test compaction quality and retrieval quality directly, with fixed suites. A memory system has a write path and a read path; both need tests, or rot comes back through the side door.

**Practical:** keep ten golden sessions, compact them, and check that the summaries preserve the facts each session later needed. Track tokens per completed task weekly, the number that pays the bill.

### OpenClaw: a memory system I run on daily

The most honest case study I have is the assistant writing this paragraph. It runs on [OpenClaw](https://github.com/openclaw/openclaw), a self-hosted assistant gateway, and its context design is a working version of the stack above.

At session start, the runtime injects a curated bootstrap: workspace instructions, user profile, and a slice of recent memory. Long-term memory lives in a markdown file the agent maintains itself. Daily notes capture raw events. Nothing loads twice: the startup context carries indexes and summaries, and full files load lazily when a task actually needs them. Compaction happens at the file level, where a human can read the diff.

It maps cleanly onto the stages: measured budget (curated startup slice), raw floor (daily notes stay verbatim), externalized memory (markdown, chosen over a vector store on purpose), isolation (skills and sub-agents with scoped contexts). The failure modes are also instructive: memory needs periodic maintenance or it goes stale, and a badly written memory file is a bad summary that loads every single session. Context engineering turns out to be a gardening job, with the garden mostly made of plain text files.

(The OpenClaw docs](https://docs.openclaw.ai) describe the memory layout if you want to compare designs. And yes, this is the second article in a row where the assistant's own runtime is the case study. When your hammer is also your workshop, everything starts looking like a nail.)

### The checklist

Run it against your agent this week:

- [ ] Measure your **effective window** on real tasks. Write the number down.
- [ ] Set a **compaction threshold** at half that budget, with a raw floor for recent turns.
- [ ] Move durable facts to **external memory files**, loaded on demand.
- [ ] **Isolate** sub-agent contexts by domain or toolset, with explicit interfaces.
- [ ] Build a **golden-session suite** that tests compaction and retrieval, and run it in CI.
- [ ] Track **tokens per completed task** weekly. It's the cost line that context engineering moves.

### Close

Here's what I believe: the million-token window is marketing, and the effective window is an engineering constraint you measure yourself. The teams shipping reliable long-running agents stopped asking the model to remember and started building the memory around it: compact the past, externalize the durable, isolate the conflicting, and test all of it like a pipeline. That stack is boring, it's mostly plain files and thresholds, and it's what separates an agent that demos well from one that still works on Friday.

Sincerely,
Alexey

---

## Platform Deltas

**Substack (Alexey On Data):**
- URL: https://aishippingblog.com
- Subtitle: Context rot is measurable, external memory is real, and the single-versus-multi-agent fight finally has data. A practical stack for agents that last longer than a demo.
- Paywall: place `[PAYWALL BREAK — free preview ends here]` after "Isolation: split the context, split the failure".
- Ends on the Sincerely / Alexey signoff.

**Medium:**
- 5 topic tags: Artificial Intelligence, Machine Learning, LLM, AI Agents, Context Engineering
- Member-only: no
- Ends on the community CTA: "Thanks for reading! If you found this useful, subscribe for more AI engineering deep dives..."

---

## SEO Keywords

- context engineering production
- context rot LLM
- effective context window vs advertised
- agent memory systems
- LLM compaction and summarization
- sub-agent context isolation
- multi-agent failure modes MAST
- agent memory benchmark
- AI agent long session degradation
- markdown agent memory

---

## Title & Subtitle Shortlist (for publish-time selection)

### Titles
1. Context Engineering in Production: What Survives Long Sessions
2. The Million-Token Window Is Marketing: Measuring Context Rot in Real Agents
3. Your Agent Forgets: A Production Stack for Context, Memory, and Isolation
4. Context Rot, Compaction, and Memory: What Production Agents Actually Run On
5. Stop Asking the Model to Remember (A Practical Context Stack)

### Subtitles
1. Context rot is measurable, external memory is real, and the single-versus-multi-agent fight finally has data. A practical stack for agents that last longer than a demo.
2. From Chroma's 18-model degradation study to a five-stage stack: measure the window, compact the past, externalize memory, isolate contexts, evaluate everything.
3. What changes when your agent runs for a week instead of a demo: rot, compaction, external memory, and the gardening job nobody expected.
