# How to Do Agent Evals in 2026

> Subtitle: A practical, tool-agnostic framework for evaluating AI agents across coding, RAG, and workflow use cases, from offline test design to production observability.

[IMAGE: Diagram showing the three layers of agent evaluation: final answer quality, trajectory quality, and system behavior, with feedback arrows from production back to test cases]
Caption: 1. Final answer quality. 2. Trajectory and tool-call quality. 3. System behavior (cost, latency, safety). Production feedback loops feed all three.

I analyzed 4,894 AI engineering job descriptions for the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide). Across all of them, one topic shows up in interview questions more than almost anything else: evaluation. "How do you evaluate a RAG pipeline?" "How do you measure agent performance?" "How do you build a golden dataset?" Companies ask these questions because they've learned the hard way that evaluation is where projects die.

The data backs this up. According to a [2026 analysis by Digital Applied](https://www.digitalapplied.com/blog/88-percent-ai-agents-never-reach-production-failure-framework), 88% of AI agents never reach production. [Fiddler's AI agent research](https://www.fiddler.ai/blog/ai-agent-failure-rate) reports similar numbers. The ones that ship often get pulled within weeks. The cause is rarely the model. It's the evaluation. Teams test the model, deploy the agent, and discover too late that they tested the wrong thing.

A [recent survey from arXiv](https://arxiv.org/html/2503.16416v2) makes the gap concrete: standard model benchmarks correlate poorly with agentic task performance. A model that scores 90% on a coding benchmark can still fail at a multi-step task because it picks the wrong tool on step two and never recovers. [Microsoft's agentic AI red-teaming team](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) documented the same pattern: the failure modes that matter in production (compounding errors, silent tool misuse, context degradation across turns) are invisible to single-turn evals.

Here's what happens in practice. You run the eval suite. Twenty test cases, all green. Your agent retrieves the right documents, calls the right tools, produces clean answers. You deploy on Monday. By Wednesday, a user asks something your suite never covered. The agent calls a tool that doesn't exist. It invents a file path. It answers with perfect confidence and zero correctness. The test set was a comfort blanket.

The problem isn't that agents are hard to build. Tools like [LangGraph](https://blog.langchain.dev/), [LlamaIndex](https://www.llamaindex.ai/), [Pydantic AI](https://ai.pydantic.dev/), and [CrewAI](https://www.crewai.com/) have made agent construction almost routine. The problem is that most teams evaluate agents the way they evaluate models: single-turn inputs and outputs, a handful of test questions, maybe a benchmark score. Agents don't work that way. They take multi-step trajectories. They call tools. They make decisions that compound across turns. A model gives you an answer. An agent gives you a sequence of actions that sometimes produces an answer.

**Agent evaluation needs to test the journey, not just the destination. If you're only checking the final answer, you're evaluating the wrong thing.**

The good news: software engineers have been solving a version of this problem for decades. Equivalence partitioning, boundary testing, integration tests, regression suites. These patterns transfer to agents. This guide shows how, tool-agnostic and framework-agnostic, across the three agent patterns you're most likely shipping: coding agents, RAG agents, and workflow/task agents.

### Why agent evaluation is fundamentally different

Evaluating a model is straightforward. You give it an input, you check the output. Maybe you score it against a reference answer, or use a metric like BLEU or ROUGE, or run it through a benchmark. The interaction is one turn, one response.

Agents break this model entirely. An agent receives a task, decides which tools to use, calls them in sequence, reads the results, adjusts its plan, and eventually produces an output. The same input can produce completely different trajectories on different runs. A coding agent might solve the same bug through five different tool-call sequences, some efficient and others wasteful. All of them might produce the correct final answer. But only the efficient ones are production-ready.

[LangSmith's trajectory evaluation docs](https://docs.langchain.com/langsmith/trajectory-evals) describe this well: evaluating an agent means evaluating a *sequence* of decisions, each of which constrains the next. A wrong tool call at step two might not surface as a failure until step seven, when the agent is working with stale or irrelevant context.

[Confident AI's multi-turn evaluation guide](https://www.confident-ai.com/blog/multi-turn-llm-evaluation-in-2026) breaks the failure modes into categories that single-turn evals simply miss:

- **Tool selection errors:** the agent calls the wrong tool for the task
- **Ordering errors:** the right tools, but in the wrong sequence
- **Argument errors:** the right tool, but with wrong or hallucinated parameters
- **Context degradation:** the agent loses track of earlier context across turns
- **Compounding failures:** a small error in step one cascades into a completely wrong answer by step five
- **Silent failures:** the agent produces a plausible-looking answer that is subtly incorrect, and nobody notices for days

The last category is the most dangerous. A hallucination that obviously looks wrong gets caught quickly. A hallucination that looks correct and confident can persist in production for weeks, eroding user trust before anyone notices.

### The three layers of agent evaluation

If you're only checking the final answer, you're doing one layer out of three. Here's the full picture.

**Layer 1: Final answer quality.** Did the agent produce the right answer? This is the baseline. For a RAG agent, does the answer match the retrieved documents? For a coding agent, does the code work? For a workflow agent, was the task completed? You can check this with exact match, semantic similarity, or LLM-as-judge scoring. This layer is necessary. It's also where most teams stop.

**Layer 2: Trajectory quality.** Did the agent take a reasonable path to get there? Did it call the right tools in the right order? Did it make unnecessary calls? Did it hallucinate tool arguments? For a RAG agent, you might check that it searched before fetching documents, and that the documents it fetched were actually relevant. For a coding agent, you might check that it read the file before editing, or that it ran the tests after making changes. For a workflow agent, you might verify that it followed the required step sequence.

This is where you catch the agent that arrives at the right answer through a terrible trajectory. It called six tools when two would suffice. It retrieved ten documents and used one. It retried a failed call three times before trying an alternative. In testing, the answer looks fine. In production, the cost adds up and the latency kills the experience.

**Layer 3: System behavior.** How does the agent behave as a system? What's the cost per task? What's the latency profile? How does it handle errors and edge cases? Does it recover gracefully from tool failures? Does it stay within safety boundaries? This layer is about the operational properties that determine whether the agent is viable in production.

A [2026 IBM guide on AI agent testing](https://www.ibm.com/think/topics/ai-agent-testing) emphasizes that teams often treat these three layers as separate concerns, handled by different people at different stages. The testing engineer handles Layer 1. The developer handles Layer 2 informally. The ops team handles Layer 3 after deployment. The result: nobody owns the full picture, and gaps fall through the cracks.

The fix: treat all three layers as one evaluation pipeline, run continuously, from development through production.

### Designing test cases: borrow from QA, not from ML

Most agent test suites I've seen are built on vibes. Someone writes ten questions they think are important, checks the answers manually, and calls it an evaluation. This is the equivalent of writing unit tests by typing whatever comes to mind. Software testing solved this problem decades ago.

**Equivalence partitioning.** Divide the input space into groups where inputs within each group should produce similar behavior. For a RAG agent, your partitions might be: questions about topics in the documentation, questions about topics not in the documentation, ambiguous questions, questions with multiple valid answers, and questions in different languages. You test one representative from each partition, not randomly.

**Boundary testing.** Edge cases are where agents fail in production. Test the boundaries of each partition. For a RAG agent: a query that exactly matches a document title (easy case), a query that's semantically related but uses different words (typical case), a query that's semantically related to multiple documents (ambiguous case), and a query that's completely off-topic (boundary case).

**Corner cases.** These are combinations of boundary conditions. A user asks an off-topic question in a language the agent partially supports. A user provides context that conflicts with the documentation. A user asks a follow-up question that changes the topic mid-conversation. These are the scenarios that break in production, and they're almost never in your test suite.

Here's what this looks like in practice, for the three common agent patterns:

**Coding agent test cases:**
- Simple bug fix in a single file (happy path)
- Bug fix that requires understanding cross-file dependencies (integration)
- Bug fix where the obvious fix is wrong (boundary)
- Task where the repository doesn't contain enough information (corner case)
- Task with ambiguous requirements (boundary)
- Large codebase navigation (performance boundary)
- Task that requires running tests to verify (trajectory check)

**RAG agent test cases:**
- Direct factual question from the documentation (happy path)
- Question that requires synthesizing information from multiple documents (integration)
- Ambiguous term with multiple meanings (boundary, like the word "judge" meaning both a legal official and an LLM evaluation pattern)
- Completely off-topic question (corner case)
- Question with context that should personalize the answer (boundary, like "I have a dataframe with columns X, Y, Z")
- Question in a different language (corner case)
- Follow-up question that changes topic mid-conversation (trajectory check)

**Workflow/task agent test cases:**
- Simple task with clear steps (happy path)
- Task where a tool is unavailable or returns an error (error handling)
- Task with multiple valid approaches (boundary)
- Task that requires retrying a failed step (trajectory check)
- Task with conflicting constraints (corner case)
- Long-running task that tests context limits (boundary)
- Task where the user changes requirements mid-way (trajectory check)

### Building test data when you don't have users yet

The hardest part of agent evaluation is the cold-start problem. You know you need a golden dataset. You don't have users yet, so you don't have real conversations. What do you do?

**Start with synthetic data, but treat it as a placeholder, not a destination.** Generate test cases with an LLM. Give it your tool definitions, your system prompt, and your expected behavior, and ask it to generate diverse test scenarios. Be specific: "Generate 50 test queries that cover happy path, edge cases, off-topic questions, and adversarial inputs for a RAG agent that answers questions about Python documentation."

The problem with synthetic data: LLMs generate the same patterns they already understand well. They'll give you plenty of happy-path cases and miss the weird, creative, adversarial inputs that real users produce. A synthetic test suite feels comprehensive and isn't.

**Manual testing is your bridge to real data.** Use your own agent. A lot. Open it up, talk to it, try to break it. A workflow that works well: open a voice dictation tool, narrate what you're doing and what you expect, and then convert that narration into structured test cases. You talk through your testing session: "I asked about X, I expected Y, the agent did Z, that's wrong because..." A minute of narration becomes a structured test case.

This is uncomfortable. It feels slow and manual. But every hour you spend as your own user produces more valuable test cases than an LLM generates in an hour of synthetic data. You find the awkward phrasings, the ambiguous queries, the places where the agent's confidence doesn't match its correctness. Synthetic data gives you volume. Manual testing gives you signal.

**Get real users as fast as humanly possible.** Every conversation a real user has with your agent is worth ten synthetic test cases. Instrument your agent from day one with logging that captures the full conversation (with user consent), the tool calls, the retrieved documents, and the final answer. Then mine those conversations for test cases.

The [Confident AI guide on LLM agent evaluation](https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide) recommends a ratio: aim for 60% real conversation-derived test cases, 30% manually crafted edge cases, and 10% synthetic data for coverage gaps, within the first few months of having users. Before users, flip it: 60% manual, 30% synthetic, 10% anticipated edge cases.

### Scoring agents: LLM-as-judge and where it falls short

Once you have test cases, you need to score them. For final answer quality, traditional metrics (exact match, BLEU, ROUGE) are mostly useless for agents because the output is free-form text or structured data, not a translation or summary.

**LLM-as-judge** has become the dominant approach. You send the agent's output to another LLM with evaluation criteria in plain English, and the judge returns a structured pass/fail with an explanation. [DeepEval's guide on LLM-as-judge](https://deepeval.com/blog/llm-as-a-judge) covers the pattern in detail.

The pattern works like this. Define your criteria as natural language statements:

```python
criteria = [
    "the answer is grounded in the retrieved documents",
    "the agent called search before fetching files",
    "the response includes relevant code examples",
    "follow-up questions are relevant to the topic",
]
```

Send these along with the agent's output and trajectory to a judge LLM, which returns structured feedback. Each criterion gets a pass/fail and an explanation.

This works well for criteria that are hard to express as assertions. "The response adapts to the user's specific context" is easy to describe in English and painful to check with code. The judge handles it naturally.

**Where it falls short:**

LLM judges have biases. They prefer longer answers, agree with the agent more often than they should, and can be inconsistent across runs. [Research compiled by Arize](https://galileo.ai/blog/ai-agent-evaluation) and [MLflow's evaluation framework comparison](https://mlflow.org/top-5-agent-evaluation-frameworks/) show that judge accuracy varies significantly by model, with smaller models (like GPT-4o-mini) struggling with nuanced criteria like code formatting or logical reasoning quality.

Practical mitigations:

- **Use a stronger model for the judge than for the agent.** If your agent runs on GPT-4o-mini, judge with GPT-4o or Claude Sonnet. The cost is worth it.
- **Force the judge to explain before deciding.** Structure the judge output so the reasoning comes before the pass/fail. This alone improves accuracy significantly.
- **Track judge agreement with human review.** Sample 10-20% of judge results and review them yourself. When the judge and the human disagree, improve the criterion description.
- **Watch for judge position bias.** If you show the agent output and a reference answer, the judge may prefer whichever comes first. Shuffle the order.

For trajectory evaluation specifically, check the tool-call sequence directly with assertions when you can. It's cheaper and more reliable than a judge:

```python
tool_calls = collect_tool_calls(result.messages)

assert len(tool_calls) >= 2
assert tool_calls[0].name == "search"
assert tool_calls[1].name == "get_file"
```

This doesn't need an LLM. You know the expected sequence. Check it directly.

### Production observability: closing the loop

Offline evaluation catches problems before deployment. Production observability catches the problems your offline tests missed. You need both.

The [Algolia guide on agent evaluation frameworks](https://www.algolia.com/blog/ai/ai-agent-evaluation-frameworks-metrics-testing-strategies) makes a clear distinction between offline and online evaluation that's worth repeating:

**Offline evaluation** runs your agent against a fixed test suite before deployment. It answers: "Does the agent work on the cases we've anticipated?" It's deterministic, repeatable, and limited to what you've already thought of.

**Online evaluation** monitors the agent in production, on real traffic. It answers: "What's the agent actually doing with real users?" It catches the cases you didn't anticipate.

The connection between them is the feedback loop. Every production failure should become an offline test case. A user reports a wrong answer. You reproduce the conversation, add it to your test suite, and now that failure mode is covered forever. Over time, your offline test suite becomes a record of every production incident you've ever learned from.

[Tools like LangSmith](https://docs.langchain.com/langsmith/trajectory-evals), [Langfuse](https://langfuse.com/), [Arize Phoenix](https://phoenix.arize.com/), and [Braintrust](https://www.braintrust.dev/) provide the tracing infrastructure for this. Every LLM call, every tool call, every retrieval becomes a span in a trace. You can see exactly where the agent went wrong, cluster similar failures, and export failing traces as test cases.

Key metrics to track in production:

- **Task completion rate:** what percentage of conversations end with a successful resolution?
- **Tool call accuracy:** are the tools being called with correct arguments?
- **Cost per task:** how much does each conversation cost in API fees?
- **Latency:** time to first token, total conversation time, per-turn latency.
- **Hallucination rate:** how often does the agent produce ungrounded claims? (This requires sampling and human or LLM review.)
- **User satisfaction:** explicit feedback (thumbs up/down) or implicit signals (did the user rephrase and retry?).

### The agent evaluation checklist

A copy-pasteable checklist for evaluating your agent before shipping and in production.

**Before shipping (offline evaluation):**

*Final answer quality:*
- [ ] Test suite covers all equivalence partitions (happy path, edge cases, corner cases)
- [ ] At least 20% of test cases are derived from real usage (or manual testing if no users yet)
- [ ] LLM-as-judge criteria are written and validated against human review
- [ ] Off-topic and adversarial inputs are tested
- [ ] Structured output schema is validated (all required fields present and correctly typed)

*Trajectory quality:*
- [ ] Tool call sequence is verified for at least the happy path cases
- [ ] Agent handles tool failures gracefully (simulate a tool returning an error)
- [ ] No unnecessary tool calls on simple tasks
- [ ] Multi-turn conversations are tested (at least 3-5 turns)

*System behavior:*
- [ ] Cost per test run is tracked and within budget
- [ ] Latency is within acceptable bounds for the use case
- [ ] Error recovery is tested (what happens when the LLM output is malformed?)
- [ ] Safety boundaries are tested (does the agent refuse inappropriate requests?)

**In production (online evaluation):*

- [ ] Full conversation traces are logged (LLM calls, tool calls, retrievals)
- [ ] Task completion rate is monitored
- [ ] Cost per task is tracked and alerted on
- [ ] Failing traces are exported and added to the offline test suite regularly
- [ ] User feedback (explicit or implicit) is collected
- [ ] Hallucination sampling is in place (review 5-10% of outputs)

### How to know your evals are working

**Good signs:**
- Your test suite catches regressions before users do
- Production incidents are decreasing over time
- New failures map to gaps in your test coverage (which you then fill)
- The judge's verdicts align with your own assessment most of the time
- Cost and latency are predictable, not surprising

**Warning signs:**
- All tests pass but users complain about quality
- The same type of production failure keeps recurring
- Your test suite never fails when you change the agent's prompt or tools
- The judge disagrees with your assessment frequently
- You have no idea what your agent costs per conversation

If you see warning signs, the fix is almost always the same: get more real conversation data, add the failing cases to your test suite, and iterate. Your test suite should grow every time production breaks. That's the system working.

### What I believe

Agent evaluation is software testing applied to nondeterministic systems. The fundamentals transfer. Equivalence partitioning, boundary testing, regression suites, integration tests. These are not new ideas. They're old ideas applied to a new kind of system.

Start small. Write five test cases. Use your own agent until it breaks. Turn that breakage into a test case. Repeat. In a few weeks, you'll have a test suite that catches real problems. In a few months, you'll wonder how you ever shipped without one.

The teams that ship reliable agents in 2026 are the ones that treat evaluation as a first-class engineering discipline. The teams that don't are the 88%.

If you want to practice this hands-on, the [AI Engineering Buildcamp: From RAG to Agents](https://maven.com/alexey-grigorev/from-rag-to-agents) covers the full evaluation pipeline with real code, real tools, and real agents. The next cohort starts September 21.

Sincerely,
Alexey

---

## Platform Deltas

**Substack (Alexey On Data):**
- URL: https://alexeyondata.substack.com
- Subtitle: A practical, tool-agnostic framework for evaluating AI agents across coding, RAG, and workflow use cases, from offline test design to production observability.
- Paywall: place `[PAYWALL BREAK — free preview ends here]` after "Why agent evaluation is fundamentally different" section.
- Ends on the Sincerely / Alexey signoff.

**Medium:**
- 5 topic tags: Artificial Intelligence, Machine Learning, LLM, AI Agents, Software Testing
- Member-only: yes
- Ends on the community CTA: "Thanks for reading! If you found this useful, subscribe to [Alexey On Data](https://alexeyondata.substack.com) for more AI engineering deep dives, practical guides, and the occasional production war story. Or just share it with someone who's debugging their agent evals at 2am."

---

## SEO Keywords

- AI agent evaluation
- LLM agent testing
- agent evaluation framework 2026
- how to evaluate AI agents
- RAG evaluation
- coding agent evaluation
- LLM-as-judge
- agent observability
- agent trajectory evaluation
- golden dataset for LLM
- equivalence partitioning for AI agents
- production agent monitoring

---

## Title & Subtitle Shortlist (for publish-time selection)

### Titles
1. How to Do Agent Evals in 2026
2. How to Actually Evaluate AI Agents: A practical framework for testing what matters
3. Your Agent Benchmarks Are Lying: What to test instead before shipping to production
4. The Agent Evaluation Gap: Why 88% of agents never reach production (and how to be in the 12%)
5. Stop Testing Agents Like Models: A practical guide to multi-turn evaluation

### Subtitles
1. A practical, tool-agnostic framework for evaluating AI agents across coding, RAG, and workflow use cases, from offline test design to production observability.
2. How to move beyond single-turn benchmarks and build an evaluation pipeline that actually catches what breaks in production.
3. From equivalence partitioning to LLM-as-judge to production observability: the complete guide to agent evaluation in 2026.
