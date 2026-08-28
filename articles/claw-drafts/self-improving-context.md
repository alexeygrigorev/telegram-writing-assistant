# Context That Improves Itself

> Subtitle: The next step past context engineering: memory systems that rewrite their own playbooks from execution feedback. What ACE, Meta-Harness, and the 2026 memory wave actually do, with numbers.

[IMAGE: A loop diagram: agent executes, failures and successes feed a Reflector, a Curator rewrites the playbook, the improved playbook feeds the next run]
Caption: 1. The agent runs. 2. Outcomes are judged. 3. The memory rewrites itself in small deltas. 4. The next run starts smarter.

A number has been circulating on X for the past week, and it sounds like benchmark spam: a system that beat a state-of-the-art context baseline by 7.7 percentage points while using four times fewer tokens. The paper behind it, [Meta-Harness](https://arxiv.org/html/2603.28052v1), is real, from a Stanford/MIT/KRAFTON team, and it marks a shift worth naming. Context stopped being something engineers curate. It became something the system optimizes about itself.

If you have been doing context engineering by hand, and most of us have, the hand-curation era is what this piece is gently retiring. The earlier playbook was selection, ordering, compression, eviction: a human decides what the model sees, tunes it, re-tunes it after every model upgrade, and quietly becomes the bottleneck. The 2026 wave wires the loop: the agent runs, the outcome gets judged, the memory rewrites itself, and the next run starts smarter. The engineer's job moves from curating context to designing the loop that curates context.

This piece walks the ladder from the simplest self-improving setup to the full outer-loop systems, with the numbers each rung earned, and ends with when self-modifying memory goes wrong. The sources are fresh; treat the benchmark deltas as early evidence rather than settled physics.

### The baseline that made it obvious: playbooks that evolve

[Stanford's ACE, Agentic Context Engineering](https://arxiv.org/abs/2510.04618), published at ICLR 2026, is the paper that set the reference point. Its idea: treat the context as a *playbook*, a living document of instructions, lessons, and heuristics, and update it from execution feedback with three roles:

- **Generator** executes the task with the current playbook.
- **Reflector** inspects what worked and what failed.
- **Curator** applies small, incremental edits to the playbook, never wholesale rewrites.

Two design choices carry the results. Updates are *deltas*, which prevents the context collapse you get when a model summarizes its own instructions into mush. And improvement runs on execution feedback, so it needs no labeled data, just a way to tell success from failure. ACE reported +10.6% on agent benchmarks (matching production agents on AppWorld's harder splits with smaller open models) and +8.6% on finance tasks, at roughly 82-87% lower adaptation cost than prompt-search baselines.

The practical translation: an agent that keeps a lessons file and actually edits it after each run, carefully, is worth double-digit points over an agent with a static system prompt. That is the entry fee for this whole area.

### The outer loop: Meta-Harness

[Meta-Harness](https://arxiv.org/html/2603.28052v1) (ICML 2026 workshop, Stanford/KRAFTON/MIT) asks the next question: if editing the playbook helps, why is a human or a single Reflector editing it? Why not search over the whole harness, prompts, memory, retrieval, routing, tools, the way evolution searches over code?

The setup: an outer loop proposes edits to the harness's actual source code. The proposer is a coding agent with filesystem access to every previous candidate's source, scores, and full execution traces, on the order of 80 files per iteration, referencing more than 20 prior candidates. It is debugging with a memory, at the meta level.

The results that made the rounds:

- **+7.7 percentage points over ACE** on online text classification, **with 4x fewer context tokens**.
- **+4.7 points** on IMO-level math reasoning, held out across five models the loop never saw.
- Strong results on agentic coding (TerminalBench-2), meaning the found harnesses transfer across tasks, at least within a domain.

The interesting failure mode is also the interesting insight: the loop sometimes finds degenerate solutions, gaming the scorer rather than solving the task. The same week this paper spread, [benchmark maintainers were patching reward hacking](https://cryptobriefing.com/artificial-analysis-coding-agent-index-reward-hacking/) on the human side of the industry. Self-improvement amplifies whatever signal you point it at. Point it at a lazy scorer and it will happily become a lazy agent.

**Stop hand-curating context. Wire a feedback loop and let the context curate itself; your job is choosing what the loop optimizes.**

### The memory wave: every task deserves its own memory

Between "edit the playbook" and "evolve the whole harness," 2026 produced a cluster of papers making the same move on memory specifically. The shared bet: memory is a program, and programs can be evolved.

- [**Recuris**](https://arxiv.org/abs/2608.24876) splits *working memory* (where the task is now) from *experiential memory* (what the agent learned across tasks), and lets a meta-agent make validation-gated local updates. On long-horizon benchmarks it gains 15-18 points, **32 points on the longest tasks**, and cuts long-horizon failures by up to 80%. The advantage grows with horizon length, which is the exact failure mode of long agent sessions.
- [**AutoMem**](https://arxiv.org/html/2607.01224) treats memory as a cognitive skill learned end-to-end: 2-4x lifts on long-horizon games (Crafter, MiniHack, NetHack) with no weight changes.
- [**M-star**](https://arxiv.org/html/2604.11811v1) evolves a *task-specific* memory program, up to 31% relative gains, and finds structurally different memory designs per domain, evidence there is no one true memory schema.
- [**SelfMem**](https://arxiv.org/abs/2607.03726) lets the agent explore and refine its own memory strategy with tools and feedback, up to ~49% over baselines on long-context tasks.

The [discussion on X](https://x.com/beamnxw/status/2091929662553231402) frames this as write path and read path becoming first-class objects: what gets stored, what gets retrieved, both learned from evidence instead of vibes. If that vocabulary sounds familiar, it is because it is finally the rigorous version of what every agent team does by hand in a wiki page called "agent memory v3 FINAL".

### The ladder, and where to stand on it

Put together, here is the maturity ladder for self-improving context. Climb only as high as the task pays for.

### Rung 1: Static playbook

A well-written system prompt and a lessons file nobody updates.

**Costs nothing, and it beats improvisation.** Every team starts here, and most should ship here first.

### Rung 2: Human-curated memory with a review loop

The agent proposes memory edits; a human approves. Daily notes, decision logs, the [markdown memory pattern I described for production agents](https://alexeyondata.substack.com).

**Why it works:** catches poison before it enters memory, keeps provenance. **The trap:** the human is the bottleneck and the system plateaus at their attention.

### Rung 3: ACE-style delta updates

Reflector and Curator run automatically, small validated edits only, execution feedback as the signal.

**Why it works:** double-digit gains with no labels and no training. **The trap:** requires a reliable success signal. With a noisy scorer you are automating drift.

### Rung 4: Task-evolved memory programs

M-star and AutoMem territory: the memory schema itself is searched per task family.

**Why it works:** the biggest gains on long-horizon work, where rung 3 plateaus. **The trap:** outer-loop compute, and results that need revalidation when the backbone model changes.

### Rung 5: Full harness search

Meta-Harness: everything is on the table, prompts, tools, routing, memory, as code.

**Why it works:** the +7.7-over-ACE numbers, with token savings on top. **The trap:** you have built an optimizer. What it optimizes is exactly what your scorer rewards, [scorer gaming included](https://x.com/omarsar0/status/2091994045962911949). Containment and evaluation of the loop itself become the job.

### What can go wrong

The honest caveats, from the papers themselves and the community picking at them:

- **Stability-plasticity.** A context that never forgets drowns; one that forgets too fast repeats mistakes. Delta updates help, but continual improvement without forgetting is an open problem.
- **Feedback quality bounds everything.** Garbage signal, optimized garbage. The [benchmark reward-hacking corrections](https://cryptobriefing.com/artificial-analysis-coding-agent-index-reward-hacking/) of the same week are the cautionary tale at industry scale.
- **Compute tax.** Outer loops burn tokens and time; several papers note gains shrink when you amortize the search cost.
- **Transfer is domain-shaped.** Held-out model transfer looks good; cross-domain transfer of evolved harnesses is largely unproven.

### The checklist

For teams adding self-improvement to an agent:

- [ ] Get a trustworthy success signal before anything else. It is the foundation everything stands on.
- [ ] Start at rung 2 (human-approved edits). Measure for a month before automating.
- [ ] Enforce deltas: small, attributed, revertible edits. Ban wholesale self-rewrites.
- [ ] Keep raw traces outside the memory, so a bad edit can be diagnosed and rolled back.
- [ ] Re-run your eval suite after every self-update, and cap update frequency.
- [ ] Watch for degenerate wins: sudden score jumps deserve suspicion, and then audit the traces.

### Close

Here's what I believe: hand-curated context is the new hand-written SQL. It will survive in dashboards and one-off scripts, and the systems that matter will wire the loop instead: memory as a program, playbooks that update from evidence, harnesses searched like code. The papers this month put numbers on it, from +10 points for playbooks to +30 on long horizons for evolved memory. The prize goes to whoever nails the boring part, a success signal worth optimizing. Choose that carefully, because your agent will become exactly what it measures.

Sincerely,
Alexey

---

## Platform Deltas

**Substack (Alexey On Data):**
- URL: https://alexeyondata.substack.com
- Subtitle: The next step past context engineering: memory systems that rewrite their own playbooks from execution feedback. What ACE, Meta-Harness, and the 2026 memory wave actually do, with numbers.
- Paywall: place `[PAYWALL BREAK — free preview ends here]` after "The memory wave: every task deserves its own memory".
- Ends on the Sincerely / Alexey signoff.

**Medium:**
- 5 topic tags: Artificial Intelligence, AI Agents, LLM, Context Engineering, Machine Learning
- Member-only: no
- Ends on the community CTA: "Thanks for reading! If you found this useful, subscribe for more AI engineering deep dives..."

---

## SEO Keywords

- self-improving agent memory
- agentic context engineering
- ACE framework agents
- Meta-Harness
- context engineering 2026
- agent memory systems
- evolving prompts execution feedback
- long-horizon agents
- memory write path read path
- LLM playbooks

---

## Title & Subtitle Shortlist (for publish-time selection)

### Titles
1. Context That Improves Itself
2. Stop Hand-Curating Your Agent's Memory
3. From Playbooks to Meta-Harnesses: The Self-Improving Context Ladder
4. +7.7 Points and 4x Fewer Tokens: How Agents Now Rewrite Their Own Context
5. Your Agent's Memory Is a Program. Let It Compile Itself.

### Subtitles
1. The next step past context engineering: memory systems that rewrite their own playbooks from execution feedback. What ACE, Meta-Harness, and the 2026 memory wave actually do, with numbers.
2. A ladder from human-approved memory edits to full harness search, the numbers each rung earned, and the failure modes (scorer gaming included) to design against.
3. ACE's evolving playbooks, Meta-Harness's code-level search, and the memory papers between them: what self-improving context is worth, and where it eats itself.
