---
title: "Plan: Vishnu"
created: 2026-04-29
updated: 2026-04-29
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Vishnu

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: Vishnu already has a very concrete project plan and clear intent. The remaining work is execution rather than ideation.
- Goal for the next 6 weeks: turn the existing plan into a weekly sequence of small, shippable steps and ship a strong demo by the end of the sprint.
- Main gap to close: structure (weekly breakdown) and a coding-assistant workflow that keeps focus through 6-10 hours per week.
- Weekly time commitment: 6-10 hours per week, which is enough to finish a solid demo inside the 6-week sprint.
- Why this plan is the right next step: he does not need help inventing what to build - he needs a weekly cadence, the right tooling, and a few quick wins early on to keep momentum.

## Plan

### Focus

- Main focus: take the project Vishnu already described in the intake and turn it into a weekly sequence of small, shippable steps.
- Supporting focus: pick one coding assistant and use it consistently to maintain focus and offload routine work.
- Supporting focus: use the per-week prompts below (lifted from the AI Engineering Buildcamp v2 capstones) as scaffolding to advance the project each week.

### Timeline

The project Vishnu has in mind can be built either as an agentic system or as a plain LLM call against the OpenAI or Anthropic SDK. Either is fine - the agentic flavour is not required. The week-by-week prompts below assume the agentic path because that is what the buildcamp uses; if Vishnu prefers a pure LLM path, weeks 3 onward can be adapted (skip the agent loop and keep iterating on the prompt and the data).

Before week 1, clone the buildcamp code repo so the prompts in later weeks can reference it:

```bash
git clone https://github.com/alexeygrigorev/ai-engineering-buildcamp-code.git
```

Note the absolute path - several prompts below need it.

#### Week 1 - Setup, scaffold, and first data

- Pick a coding assistant and commit to it. Codex if Vishnu has a ChatGPT subscription; Claude Code if he is already using it. Any one of them is fine - the workflow matters more than the choice. Free tiers should be avoided - hitting limits mid-session breaks the flow.
- Scaffold the project from the buildcamp project starter: https://github.com/alexeygrigorev/ai-buildcamp-project-starter. Three options: fork on GitHub, clone and re-point the remote, or download the zip. Pick whichever fits the workflow.
- Once scaffolded, paste this prompt into the coding assistant to make the starter his own:

```
I just cloned the AI Engineering Buildcamp project starter. Here is the
idea for my project:

[paste the project idea]

Help me make this starter mine:

1. Rewrite README.md so it describes my project. Keep the Setup and
   Notebooks sections from the original, but replace the placeholder
   problem description and "What It Does" section with my idea above.
2. Update the `name` and `description` in pyproject.toml to fit my
   project.
3. Run `uv sync` to install dependencies.
4. Run `notebooks/01-setup.ipynb` to confirm Jupyter and the OpenAI
   client work.
```

- Then add real data using `notebooks/02-rag.ipynb`. Replace `ABSOLUTE_PATH` with the absolute path where the buildcamp code repo was cloned:

```
I'm building an AI project. It [project description].

I just cloned the project starter. It has notebooks/02-rag.ipynb with
a minimal RAG pipeline that follows a specific structure: search,
build_prompt, llm, and rag functions. I want to replace the example
data with data for my project, keeping the same function structure.

Before you write any code, look at this reference notebook to see the
end-to-end pattern we use in the course:

ABSOLUTE_PATH/ai-engineering-buildcamp-code/01-foundation/02-rag/rag.ipynb

Then help me:

1. Suggest 2-3 realistic data sources I could use for this project:
   public datasets, APIs I could call, documents I could collect, or
   synthetic data I could generate as a prototype. Pick one we can
   use today, in the next 30 minutes.
2. Write code in the data loading cell to load that data. If the data
   lives in files, put them in data/ and load from there. If it's a
   public API, write a small fetcher that pulls it.
3. Update the minsearch Index configuration (text_fields and
   keyword_fields) to match the fields in my actual data.
4. Update the `instructions` string so it describes what my system
   should actually do, not generic "answer a question using context".
   If my data has different fields than the example, update
   build_prompt if needed - but keep the function structure the same
   (search, build_prompt, llm, rag).
5. Call rag("...") at the end with one representative query - the
   kind my real users would ask - so we can see it work end to end.

Commit the changes when it works.
```

- Goal for the week: a scaffolded project, real data loaded, one representative query working end to end through a basic RAG pipeline.

#### Week 2 - Iterate on RAG and shape the data

- Now that there is a working baseline, iterate on the data and the prompt. If the project will use retrieval, tighten the index fields and the search; if it will stay pure prompt, sharpen the prompt and the data shape.
- Use the coding assistant aggressively to handle boilerplate. Stay on the parts that actually matter: data quality and what the system should answer.
- Goal for the week: a noticeably better baseline on a few representative queries, and a clearer sense of what the system is actually for. Quick wins this early are what keep motivation through the rest of the sprint.

#### Week 3 - Add an agent layer with tools (optional)

If the project will stay as a plain LLM/RAG pipeline, skip this week and use it to keep iterating on the data and prompt. Otherwise, this is the week to introduce tools and an agent loop.

- Plan the tools first. Open the project so the coding assistant can see the week 1 notebook, then paste:

```
This week I'm turning my basic RAG pipeline into an agent that can
call tools. Look at my week 1 notebook (notebooks/02-rag.ipynb) and
the README to understand what the project is about and what I already
have (search, build_prompt, llm, rag).

Help me design the tools my agent should have. Do not write any code
yet - I just want to think through the design first.

1. Ask me what kinds of things my users will actually ask my agent.
   Push for concrete examples, not vague categories.
2. Based on my answers, propose 3-5 tools the agent needs. For each
   tool, give me:
   - A short name in snake_case (for example, search_docs, fetch_page)
   - A one-sentence description of what it does and when the agent
     should call it
   - The inputs it takes and what it returns
3. For each tool, tell me honestly whether it's essential or "nice to
   have". I want to start with the smallest useful set.
4. Flag any tools I'm likely missing - things that would make the
   agent much more useful but aren't obvious from my current idea.
5. Warn me about any tools that look redundant or overlap too much.
   Small focused tools are better than one big tool that does
   everything.

Keep asking me questions until we have a clear, short list.
```

- Then build the agent. Replace `ABSOLUTE_PATH` with the absolute path where the buildcamp code repo was cloned:

```
Right now I have a basic RAG pipeline with search, build_prompt, llm,
and rag functions in notebooks/02-rag.ipynb. This week I want to turn
it into an agent that can call tools. Read the README and 02-rag.ipynb
first so you understand what my project is about.

Before you write any code, look at these reference files to see how
tools and the agent loop are organized in the course:

ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/tools.py
ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/doc_agent.py

Here are the tools I want my agent to have:

[paste the tools list from the planning step]

Then help me:

1. Turn my existing `search` function into a tool the agent can call.
   Follow the same pattern as tools.py in the reference project.
2. Implement the other tools on my list. Keep them small and focused.
3. Write an agent loop that takes a user question, sends it to the LLM
   with the tool definitions, handles tool calls, and returns a final
   answer. Use the same pattern as doc_agent.py in the reference project.
4. Write an `instructions` string that tells the agent what to do and
   when to use each tool. Be specific - don't settle for generic
   "you are a helpful assistant".
5. Add a few print statements so I can see which tools the agent calls
   during a run.

Keep everything in one notebook for now. I'll refactor into modules
later.
```

- Run the agent on three queries: one that should hit the main tool, one that should hit a different tool, one that pushes the edge.
- Goal for the week: an agent that runs end to end on at least three real queries.

#### Week 4 - Tests and an LLM judge

- Brainstorm test scenarios with the coding assistant by opening the project and pasting:

```
Look at my agent code and tools to understand what my project does.

Help me think about what to test. Do not write any code yet - I just
want to brainstorm scenarios first.

1. Ask me what kinds of queries my users typically send and what I
   expect the agent to do with each one.
2. Based on my answers, propose at least 10 test scenarios covering:
   - Happy paths: queries the agent should handle well
   - Tool usage: does it call the right tools in the right order?
   - Edge cases: unusual inputs, ambiguous questions
   - Failure modes: things that might cause hallucination or wrong
     tool calls
3. For each scenario, tell me what the expected behavior is: which
   tools should be called, what the response should contain.
4. Flag any scenarios where my agent is likely to break - those are
   the most valuable tests to write.

Keep asking me questions until we have a good list.
```

- Implement at least one as a pytest test. Replace `ABSOLUTE_PATH`:

```
I want to write a pytest test for my agent. Before you write any code,
look at these reference files to see how tests are structured in the
course:

ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/tests/test_agent.py
ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/tests/conftest.py

Here is the scenario I want to test:

[paste one scenario]

Write a pytest test that:
1. Calls my agent with the test query
2. Checks which tools were called
3. Asserts something specific about the response

Follow the same patterns as the reference test file.
```

- Add an LLM judge test using `assert_criteria` with at least 2 specific criteria. Replace `ABSOLUTE_PATH`:

```
I want to add an LLM judge test for my agent. Before you write any
code, look at these reference files:

ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/tests/test_judge.py
ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/tests/judge.py

Write a test using assert_criteria with at least 2 criteria. The
criteria must be specific to my agent's behavior - not generic things
like "the response is helpful". Think about:
- What specific content should be in the response?
- Which tools should have been called?
- What format or structure should the answer have?

Follow the same patterns as the reference files.
```

- Goal for the week: tests that catch the failures Vishnu actually cares about, not generic ones.

#### Week 5 - Monitoring and a small app

- Instrument the agent with Logfire (or OpenTelemetry) so every LLM call, tool call, and full session trace is visible. Replace `ABSOLUTE_PATH`:

```
I want to add monitoring to my agent so I can see what it does on
every run. Before you write any code, look at these reference files
to see how monitoring is set up in the course:

ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/otel_test.py
ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/cost_tracker.py

Then help me:
1. Instrument my agent with Logfire (or OpenTelemetry) so I can see
   every LLM call, tool call, and full session trace
2. Add per-session cost tracking based on token usage
3. Run the agent on one query and show me how to check the trace

Follow the same patterns as the reference files.
```

- Build a simple Streamlit app so the agent can be used outside the notebook. Replace `ABSOLUTE_PATH`:

```
I want to build a simple Streamlit app for my agent so I can interact
with it and collect usage data. Before you write any code, look at
this reference app:

ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/app.py

Then help me:
1. Build a Streamlit app that lets me type a question and see the
   agent's response
2. Wire monitoring into the app so every interaction is captured
   as a trace
3. Show which tools were called during each interaction

Keep it simple - I just need a working chat interface.
```

- Run the agent through the app on at least 10 queries. The traces collected this week feed into evaluation next week.
- Goal for the week: a small app, full traces, and a sense of typical session cost.

#### Week 6 - Evaluation pipeline and demo

- Design 50 evaluation scenarios and run the agent on all of them in batch. Open the project so the assistant can see the agent code and paste:

```
Look at my agent code, tools, and README to understand what my project
does.

Help me design 50 evaluation scenarios. Do not run any code yet - I
just want the scenarios first.

1. Ask me what my users typically ask and what edge cases I've seen.
2. Based on my answers, generate 50 scenarios as a CSV with columns:
   question, category, type (happy_path, varied_phrasing, edge_case,
   out_of_scope, breaking)
3. Make sure each scenario is specific to my agent - not generic
   questions that could apply to any chatbot.
4. Include at least 5 scenarios designed to break the agent or cause
   hallucination.

Save the CSV to evals/scenarios.csv.
```

- Label at least 15 of the responses good/bad with a failure category. Adapt the reference labeling app:

```
I ran my agent on 50 evaluation scenarios and saved the results. Now I
need a tool to label each response as good or bad. Before you write
any code, look at this reference labeling app:

ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/evals/label_evals.py

Adapt it to work with my results. Show the question and response, let
me label good/bad with one click, add a failure category dropdown for
bad responses, and save labels to a CSV.
```

- Build an LLM judge with structured output and validate it against the labels. Replace `ABSOLUTE_PATH`:

```
I have labeled data with good/bad labels for my agent's responses. Now
I want to build an LLM judge that can evaluate responses automatically.
Before you write any code, look at the reference evals folder:

ABSOLUTE_PATH/ai-engineering-buildcamp-code/documentation-agent/evals

Then help me:
1. Write a judge with structured output (reasoning + label fields)
   that evaluates my agent's responses as good or bad
2. Run the judge on all my labeled data
3. Calculate accuracy, precision, and recall against my labels
4. Show me the disagreements so I can improve the judge prompt

Use the failure patterns I found during labeling to write the judge
prompt.
```

- Wrap up to a state where the project can be demoed. A short README, a working deploy or running locally, and a clear "what this does" is enough.
- Goal for the week: a demoable project plus a small evaluation pipeline that can keep being run after the sprint ends.

### Resources

- AI Engineering Buildcamp project starter: https://github.com/alexeygrigorev/ai-buildcamp-project-starter - the scaffold for week 1.
- AI Engineering Buildcamp code repo: https://github.com/alexeygrigorev/ai-engineering-buildcamp-code - the reference project the prompts above point at; clone it once at the start.
- Coding assistant of choice (Codex or Claude Code). If Vishnu has a ChatGPT subscription, Codex is the cheapest entry point. Free tiers should be avoided - hitting limits mid-session breaks the flow.
- OpenAI SDK or Anthropic SDK - either is enough for this project. No agent framework is required unless the project specifically calls for it.

### Deliverables

- A scaffolded project with real data loaded by end of week 1, and a representative query working end to end.
- A noticeably better baseline by end of week 2 (the early quick win).
- Tests and an LLM judge by end of week 4.
- Monitoring, a small app, and at least 10 traced sessions by end of week 5.
- An evaluation pipeline (50 scenarios, labels, validated judge) plus a demoable project by end of week 6.

### Accountability

- Keep weekly effort in the 6-10 hour band so the 6-week plan stays finishable and consistent.
- Aim for one demoable project, not several parallel experiments.
- Use the coding assistant heavily; it doubles as a focus tool, not just a code generator.

### Next Steps

- [ ] [Vishnu] Pick a coding assistant (Codex or Claude Code) and confirm a paid plan that fits 6-10 hours per week.
- [ ] [Vishnu] Clone https://github.com/alexeygrigorev/ai-engineering-buildcamp-code so the per-week prompts can reference it.
- [ ] [Vishnu] Scaffold from the project starter and ship the week 1 quick win (data loaded, one representative query working).
- [ ] [Alexey] Send the written plan.

## Internal Context

### Persona

Undetermined. The voice note focuses on execution and time commitment but does not provide enough background to pick a persona confidently. Update once the intake doc is read.

See [personas.md](../personas.md) for full persona definitions.

### Background

Vishnu's input is collected in the Google Doc shared in the inbox[^1]. He has a very concrete project plan already and 6-10 hours per week to spend on it - enough for a serious demo by the end of a 6-week sprint, especially if he stays focused and leans on a coding assistant.

The plan number in the inbox marks this as the 9th personalised plan in the current batch[^1].

### Intake

The intake is the Google Doc with Vishnu's input collected ahead of this plan[^1]. The contents of the doc are not duplicated here.

### Internal Recommendations

Alexey's recommendation after reviewing Vishnu's input[^2]:

1. Vishnu already has a concrete plan. The job is mainly to break it into weeks and figure out how to implement it - not to redesign anything.

2. The project can be built as something agentic, but it can equally be done with a plain OpenAI or Anthropic SDK call. Do not force the agentic shape if it is not needed.

3. The per-week prompts above were lifted from the AI Engineering Buildcamp v2 capstone files (`/home/alexey/git/ai-engineering-buildcamp/v2/{01-foundation,03-agents,04-testing,05-monitoring,06-evaluation}/homework/02-capstone.md`). They are scaffolding - useful even though Vishnu already has a project plan, because they give him a concrete "what to do this week" template. Module 02 has no capstone file, so week 2 in this plan is a freeform RAG iteration week.

4. 6-10 hours per week is a lot of time for a 5-6 week sprint. That is enough to build a solid demo by the end of the course, especially if Vishnu stays focused and uses an AI assistant aggressively.

5. Pick any coding assistant. Codex is a natural fit if he has a ChatGPT subscription; Claude Code is also fine if he already uses it. The point is to pick one and use it maximally - it helps with motivation as much as with productivity.

6. The goal for the early weeks is to land a few quick wins, so motivation carries through the rest of the sprint.

### Internal Action Items

- [ ] [Alexey] Send Vishnu the written plan (the per-week prompts are embedded in the plan itself - no extra link to the capstone files needed).
- [ ] [Valeriia] Confirm Vishnu's chosen coding assistant and the first weekly goal so the plan can be sanity-checked early.

### Sources

[^1]: [Google Doc](https://docs.google.com/document/d/1MLNJl3ku1ApQv5Nq9mJm9B3z_55Q2hyQcc2cHc4Qz5s/edit?usp=sharing) via [20260429_131353_AlexeyDTC_msg3733.md](../../../inbox/used/20260429_131353_AlexeyDTC_msg3733.md)
[^2]: [20260429_131714_AlexeyDTC_msg3735_transcript.txt](../../../inbox/used/20260429_131714_AlexeyDTC_msg3735_transcript.txt), [20260429_134248_AlexeyDTC_msg3741_transcript.txt](../../../inbox/used/feedback/20260429_134248_AlexeyDTC_msg3741_transcript.txt)
