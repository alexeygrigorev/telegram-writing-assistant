# Durable Agents: Stop Losing Step 37 of 40

> Subtitle: What durable execution actually does for AI agents, how replay survives non-deterministic models, and a four-rung ladder for choosing between Postgres, libraries, and workflow engines.

[IMAGE: Diagram of an agent workflow dying mid-run: steps 1 through 36 completed, step 37 marked with a crash, steps 38 through 40 greyed out, and an arrow looping back to a checkpoint that resumes at 37]
Caption: 1. Each step journals its result. 2. The process crashes at step 37. 3. Replay reloads the journal. 4. Execution resumes at the last completed step.

Picture a billing agent that runs for six hours. It reconciles 40 accounts, one per step, and writes each result to the payments API. At step 37 the process dies. A deploy, an OOM kill, a flaky network call, it doesn't matter what. Two questions now decide whether six hours of work survives:

Did the agent write down what it already did? And can it resume without doing any of it twice?

For most agents built in 2024 through 2026, both answers are no. The run state lives in process memory, the moment the process dies the state dies with it, and the only recovery options are starting over or hand-coding a resume path around every failure. Teams that run agents in production hit this early enough that [Temporal called AI reliability a decade-old problem](https://temporal.io/blog/ai-reliability-is-a-decade-old-problem): the failure modes agents hit now, partial completion, duplicated side effects, lost progress, are the ones workflow engines solved years ago for payments and bookings.

The response has a name, **durable execution**, and a fast-growing toolbench: [Temporal](https://temporal.io/blog/of-course-you-can-build-dynamic-ai-agents-with-temporal), [DBOS](https://www.dbos.dev/blog/durable-execution-crashproof-ai-agents), [Restate](https://restate.dev/blog/durable-ai-loops-fault-tolerance-across-frameworks-and-without-handcuffs/), [Resonate](https://docs.resonatehq.io/evaluate/why-resonate), plus durability layers landing inside agent frameworks themselves ([Pydantic AI](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/), LangGraph). This piece explains the mechanics, shows who runs agents this way in production, and ends with a ladder for deciding how much durability your agent actually needs. Spoiler: sometimes a Postgres table is enough, and sometimes it very much is not.

### Checkpoints, journals, and replay

The core mechanism is old and proven. A *durable* agent records each completed step's result in a journal: database rows, an event log, whatever survives the process. On crash, the engine restarts the workflow and *replays* the journal, feeding each recorded result back to the code at the exact point it was recorded, so execution picks up after the last completed step instead of redoing the work.

If you've ever lost an hour of a game and reloaded a save point, you know the model. The journal is the save file. A crash reloads it. The agent continues from the checkpoint, and steps one through 36 never run again.

Three properties make this work, and each one matters more with agents:

- **Persistence.** State lives outside the process, so restarts, deploys, and crashes don't erase it.
- **Determinism.** During replay, the workflow code must follow the same path it followed the first time, so the recorded results line up with the code that asks for them. That's why engines make you separate workflow logic from side effects: the workflow decides, the *activities* (or steps) do the doing, and only the doing gets journaled.
- **Idempotency.** When a step did run but the crash happened before its result landed in the journal, the engine re-runs it. Side effects that fire twice must be harmless, which is why durable designs lean on idempotency keys and deduplicated writes.

[Jack Vanlightly's deep dive on determinism in durable execution](https://jack-vanlightly.com/blog/2025/11/24/demystifying-determinism-in-durable-execution) (November 2025) is the best neutral walkthrough of how Temporal, Restate, DBOS, and Resonate each handle this, and it's worth an hour of anyone's time.

### The hard part: models refuse to be deterministic

Agents break the classic contract. A pure workflow function returns the same output for the same input, forever. An LLM call doesn't. Re-run the same prompt and you can get a different plan, different tool arguments, a different tone. If the engine journals every LLM response, replay stays safe: the recorded answer is fed back in, and the second run continues with the model's *first* answer rather than a fresh roll of the dice.

That inversion is the key insight for agents. Journaling turns your most expensive, least reliable component into a **durable cache**. The model call runs once. Crash, restart, replay: it never runs again. This is also how engines avoid the wallet-draining failure of replaying an entire multi-step run and re-paying for every token.

The side effects need the same care. If step 38 emails a customer, the engine must guarantee that on resume the email goes out exactly once, which means the email step needs an idempotency key the provider can dedupe on. This is where agent teams do the unglamorous work: making writes idempotent, putting charges behind dedupe keys, treating every external mutation as a potential double-fire.

The last piece is suspension. Long-running agents wait for slow things: a human approving a refund, a tool finishing a batch, a timer expiring at 9am Monday. Durable engines persist the wait itself, so a workflow can sleep for three days across any number of restarts and wake up exactly where it paused. Hand-rolled versions of this are where homegrown recovery code goes to die.

**Durability is what turns an agent from a demo into infrastructure: state that survives the process, side effects that fire once, and waits that survive the weekend.**

### Who actually runs agents this way

The production evidence clusters around Temporal, which has the loudest named deployments:

- [**OpenAI runs Codex on it**](https://temporal.io/blog/of-course-you-can-build-dynamic-ai-agents-with-temporal), with the web coding agent handling millions of requests.
- **Replit** runs millions of long-running sessions of Agent 3 on it, specifically because agents fail mid-run and need to keep their progress.
- **Gorgias** scaled customer-service agents across 15,000 brands, with retries, compensation logic, and human-in-the-loop approvals riding on the engine.
- [Maxim Fateev, Temporal's CEO, argues](https://workos.com/blog/maxim-fateev-temporal-durable-execution-ai-agents) this is the same problem the engine already solved for other workloads, with agents as the newest tenant.

The challengers take different shapes, and the differences are the interesting part:

- [**DBOS**](https://www.dbos.dev/blog/durable-execution-crashproof-ai-agents) is a library, not a cluster. Your workflow code runs in your own process, and the journal lives in Postgres. The [company's comparisons](https://www.dbos.dev/compare/dbos-vs-temporal) claim 2 to 10x lower cost than Temporal and step writes of 1 to 2 milliseconds, since a step is one Postgres write. You trade the dedicated cluster's queueing and scale for radically less infrastructure.
- [**Restate**](https://restate.dev/vs/temporal) runs as a service with journaled steps and a low-latency push model, claiming sub-170ms P99 latency for 10-step workflows under load, and integrates with the SDKs agent teams already use, OpenAI's and Vercel's included.
- [**Resonate**](https://docs.resonatehq.io/evaluate/why-resonate) positions itself as agent-native first, early in adoption but worth watching.

And the frameworks are absorbing the pattern. [Pydantic AI ships durable execution](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/) as a capability with pluggable engines, LangGraph persists graph state, and the cloud vendors have their own entries (Azure Durable Task, AWS and Cloudflare workflow services). A survey of the runtimes landscape, [Zylos's durable execution for AI agent runtimes](https://zylos.ai/research/2026-04-24-durable-execution-agent-runtimes/), maps who integrates with what.

One honesty note, and it shapes how I read all of the above: the numbers in this space come from engineering blogs and vendor comparisons, [including a coding-level comparison from DBOS itself](https://www.dbos.dev/blog/durable-execution-coding-comparison). There is no neutral benchmark of durable engines running agent workloads yet. Treat every claim as a data point from an interested party.

### Graph checkpointing is not durable execution

LangGraph earned two mentions already, so it deserves its own clarification, because it's the most common source of ladder confusion.

[LangGraph](https://docs.langchain.com/oss/python/langgraph/persistence) models agents as graphs and persists them through a **checkpointer**: after each node completes, the full graph state is serialized and attached to a thread, in Postgres (or Redis, SQLite, in-memory). Hand the same thread id back and the graph resumes from the last snapshot. You also get **time travel**: query the state history, fork from any past checkpoint, edit the state, continue down a different branch. For debugging and human-in-the-loop flows this is genuinely great, and nothing in the durable-engine world matches the ergonomics.

Here is the distinction that matters. **A checkpoint is a snapshot of state. A journal is a record of execution.** [Diagrid's comparison](https://www.diagrid.io/blog/checkpoints-are-not-durable-execution-why-langgraph-crewai-google-adk-and-others-fall-short-for-production-agent-workflows) puts it in the title: checkpoints are not durable execution. Three gaps follow.

- **The data survives, the run doesn't.** LangGraph executes in your process. A crash kills the run; the checkpoint lives on, but something external has to notice the death, load the thread id, and invoke the resume. [Temporal's LangGraph integration post](https://temporal.io/blog/temporal-langgraph-plugin-durable-execution) is explicit about the split: the engine owns failure detection and automatic resumption, the checkpointer owns the saved state.
- **Side effects can fire twice.** Nodes re-execute on resume, and the LangGraph docs themselves say to keep nondeterministic and mutating operations idempotent. Nothing in the checkpointer dedupes an email sent from inside a re-run node.
- **Boundaries only.** Checkpoints exist between nodes. Fail in the middle of a node, three of five API calls done, and the whole node re-runs unless you built inner bookkeeping yourself.

None of this makes LangGraph the wrong tool. On the ladder, a Postgres-backed checkpointer is a strong rung 1.5: durable state, manual recovery, excellent introspection. The popular production pattern is the hybrid: keep the graph in LangGraph, run it on a durable engine. [Temporal ships a LangGraph integration](https://docs.temporal.io/develop/python/integrations/langgraph) (public preview) that executes graphs as workflows, adding automatic recovery and durable interrupts, and [DBOS pairs naturally](https://www.dbos.dev/blog/durable-execution-crashproof-ai-agents) with the Postgres checkpointer for state plus execution durability. Practitioner guidance converges on a simple split: [LangGraph alone for short, read-heavy runs](https://cordum.io/blog/temporal-vs-langgraph), a durable engine underneath once the agent makes real mutations, pauses for humans, or runs longer than a coffee break.

### The Durability Ladder: four rungs, pick honestly

The real question is never "which engine." It's "how much durability does this agent owe its users." I think of it as a ladder, and you should be able to say out loud which rung you're on and why.

### Rung 0: Accept the loss

Restart the run on failure, duplicate nothing destructive, lose the progress. Costs nothing to build.

**Why it's fine:** for cheap, fast, read-only agents, a full redo is often cheaper than any infrastructure. Research agents that summarize and cite: rerun the whole thing.

**The trap:** silently assuming rung 0 when side effects exist. An agent that sends emails is never rung 0, no matter how cheap the model is.

### Rung 1: Hand-rolled state in Postgres

A `runs` table, a `steps` table, a status column, idempotency keys on external writes, and a resume path you test. The journal is a table you can SELECT.

**Why it works:** for a single team and a single service, this is genuinely enough. [The argument that Postgres covers a huge slice of workloads](https://tiarebalbi.com/en/blog/dbos-vs-temporal-postgres-durable-execution) is directionally right, and plenty of production agents run exactly this way, one careful status machine at a time.

**The trap:** the resume path is untested until the night it matters. Rung 1 without chaos drills is a hope, so kill the process in staging and watch it recover.

### Rung 2: Durability as a library

Adopt DBOS or the framework-level durability in Pydantic AI. Journaling, replay, and suspend-resume come along, still backed by your Postgres, still inside your process or service.

**Why it works:** you stop writing recovery code, and the guarantees (replay correctness, exactly-once side-effect wrappers) come from someone whose full-time job is getting them right. For most teams building real agents, this is the sweet spot.

**The trap:** the library only journals what flows through it. Side effects that bypass the durable layer, a raw HTTP call in a workflow body, keep their double-fire risk.

### Rung 3: A dedicated engine

Temporal as a cluster, Restate as a service. Task queues, signals, timers that fire days later, workers that scale independently, multi-region failover, and the operational maturity of engines that have run payments infrastructure for years.

**Why it's there:** OpenAI, Replit, and Gorgias are on this rung because millions of concurrent long-running agents with human approvals don't fit anywhere smaller.

**The trap:** the ops bill. Rung 3 arrives with a cluster to run, version, and monitor. If you can't name the failure that rung 2 couldn't survive, you probably can't name why you're paying for rung 3 either.

A note from my own desk: the assistant runtime I use daily sits deliberately low on the ladder. Its durable state is plain files (memory, logs, job state) plus a durable queue for detached multi-step tasks, so a restart loses nothing it cares about. It's rung 1 with a good filing system, and for personal automation that's the honest pick. ([OpenClaw](https://docs.openclaw.ai), if you're curious.) Two articles ago I used its memory design as a case study for context engineering: same principle, different subsystem. Pick the rung per subsystem, not per company.

### The checklist

Before your next agent goes to production, run it down:

- [ ] Name the rung out loud (0 through 3) and write one sentence defending it.
- [ ] List every **external side effect** the agent can trigger. Each needs an idempotency key or an acceptance of double-fire.
- [ ] Decide what happens to **in-flight LLM calls** on restart: re-run and pay, or journal and replay.
- [ ] Add a **chaos test**: kill the process at step 37 in staging and verify it resumes at 37 with no duplicated effects.
- [ ] If humans approve mid-run, verify the **wait survives a restart** and a weekend.
- [ ] Track **cost per completed run**, including retries and replay, so durability pays for itself in numbers you can see.

### Close

Here's what I believe: durability is the least glamorous and highest-leverage investment an agent team can make in 2026. The model will get better on its own. The context stack you have to build yourself. The reliability layer you can adopt wholesale from a decade of workflow engineering. Start at the lowest rung that tells the truth about your side effects, test the crash before your users do, and climb only when you can name the failure you're climbing away from. Step 37 has taken enough agents from us.

Sincerely,
Alexey

---

## Platform Deltas

**Substack (Alexey On Data):**
- URL: https://aishippingblog.com
- Subtitle: What durable execution actually does for AI agents, how replay survives non-deterministic models, and a four-rung ladder for choosing between Postgres, libraries, and workflow engines.
- Paywall: place `[PAYWALL BREAK — free preview ends here]` after "Who actually runs agents this way".
- Ends on the Sincerely / Alexey signoff.

**Medium:**
- 5 topic tags: Artificial Intelligence, AI Agents, Temporal, Distributed Systems, LLM
- Member-only: no
- Ends on the community CTA: "Thanks for reading! If you found this useful, subscribe for more AI engineering deep dives..."

---

## SEO Keywords

- durable execution AI agents
- durable agents
- Temporal AI agents
- DBOS vs Temporal
- agent crash recovery
- agent checkpointing replay
- LangGraph checkpointer durability
- idempotent agent side effects
- long-running agent reliability
- Restate durable execution
- LLM workflow durability

---

## Title & Subtitle Shortlist (for publish-time selection)

### Titles
1. Durable Agents: Stop Losing Step 37 of 40
2. Durable Execution for AI Agents, Explained (And How to Choose an Engine)
3. Postgres Is Enough for Agent Durability (Until It Isn't)
4. The Durability Ladder: From a Status Column to Temporal
5. Why Your Agent Can't Survive a Restart (And the Engines That Fix It)

### Subtitles
1. What durable execution actually does for AI agents, how replay survives non-deterministic models, and a four-rung ladder for choosing between Postgres, libraries, and workflow engines.
2. Journals, replay, idempotent side effects, and the honest choice between hand-rolled state, DBOS, Restate, and Temporal.
3. The mechanics of crash-proof agents, the production evidence from OpenAI, Replit, and Gorgias, and a checklist that starts with killing your own process.
