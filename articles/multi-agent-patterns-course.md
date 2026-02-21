---
title: "Multi-Agent Patterns for the Course"
created: 2026-02-21
updated: 2026-02-21
tags: [ai-buildcamp, agents, multi-agent, course-content]
status: draft
---

# Multi-Agent Patterns for the Course

## Running Examples

We illustrate all patterns using three running examples. The first two are described conceptually to explain how each pattern works. The third one (Codebase Onboarding Guide) is what we actually implement with code.

### Example A: Conference Organization (conceptual)

Imagine you are organizing a tech conference. You give the system a brief: "Organize a 200-person AI conference in Berlin in June, budget 50K EUR." The system needs to handle:

- Finding speakers: search for AI practitioners, check their availability, send invitations, collect bios and talk abstracts
- Securing a venue: search venues in Berlin, compare capacity/price/AV equipment, negotiate contracts, put down deposits
- Coordinating sponsors: identify potential sponsors, draft sponsorship packages, send proposals, track responses
- Managing budget: allocate across venue/catering/speakers/marketing, track spending, flag when categories go over budget
- Handling registrations: set up ticketing, process payments, send confirmations, manage waitlists
- Publishing the schedule: assign talks to rooms and time slots, handle conflicts, publish the final program

This is a coordination-heavy task with multiple independent workstreams that need to stay aligned (budget constrains venue choice, venue constrains schedule, speaker availability constrains schedule, etc.). The system processes incoming information (emails, search results, spreadsheets), makes decisions, takes actions (sending emails, booking), and coordinates across all workstreams.

The user interacts with the system by giving high-level instructions ("find 5 more speakers on the topic of agents") and approving key decisions (venue contracts, speaker invitations, budget changes).

This example generalizes to other coordination-heavy planning tasks:

- Event/wedding planning (venue, catering, music, flowers, budget)
- Home renovation/interior design (contractors, materials, furniture, room-by-room planning)
- Meal planning and grocery shopping (recipes, dietary restrictions, shopping lists, ordering)
- Travel planning (flights, hotels, activities, transport, visa requirements)
- Relocation/moving to a new city (apartments, schools, jobs, visa, utilities)

### Example B: YouTube Video Processing (conceptual)

Imagine you have a YouTube video - say a 45-minute conference talk about building AI agents. You want to turn it into useful structured content. The system takes a video URL and produces:

- Clean transcript: fetches the auto-generated or manual captions, cleans up formatting, fixes obvious transcription errors
- Chapter timestamps: identifies topic changes in the video and creates timestamped chapters ("00:00 - Introduction", "05:23 - What are agents", etc.)
- Key topics: extracts the main themes and concepts discussed
- Summary: a concise overview of the talk's key points and takeaways
- Code examples: if the speaker shows code, extracts it with context about what it does
- Resources: all tools, libraries, papers, and URLs mentioned in the talk
- Blog post: combines everything into a publishable article

The user gives a video URL and optionally specifies what output they want ("just give me timestamps and a summary" or "full blog post with code examples"). The system processes the video end-to-end and returns structured results.

This is useful for content creators who want to repurpose video content, students who want study notes, or teams who want to document conference talks their colleagues gave.

This example generalizes to other content processing tasks:

- Deep research (gather sources, summarize each, synthesize findings, verify claims)
- Book/article writing (research, outline, draft chapters, review, revise)
- Podcast processing (transcribe, identify speakers, extract key points, generate show notes)
- Document analysis (parse PDFs, extract data, summarize, compare across documents)
- Course material creation (analyze source content, structure lessons, generate exercises)

### Example C: Codebase Onboarding Guide (implemented)

This is the example we actually build with code. The use case: you just joined a team or you want to contribute to an open source project, and you need to understand a large codebase quickly. You give the system a GitHub repository URL and it produces an onboarding guide.

We use scikit-learn as the example project. It has ~2,500 files, ~3,000 open issues, hundreds of contributors, and a complex internal architecture. A newcomer asking "how do I get started contributing to scikit-learn?" faces a significant ramp-up.

The system takes a repo URL and produces:

- Architecture overview: what are the main modules, how do they relate to each other, what are the key abstractions (e.g., scikit-learn's estimator API with `fit`/`predict`/`transform`)
- Getting started path: what to read first, what to install, how to run tests, where the contribution guide is
- Key patterns and conventions: coding style, common base classes, how new estimators are added
- Good first issues: which open issues are labeled for newcomers, what skills they require
- Who to ask: most active maintainers, what areas they own, where discussions happen (GitHub, mailing list, Discord)

The tools needed are all free and easy to set up:

- GitHub API via `gh` CLI (free, students already have GitHub accounts)
- File read/write for generating the guide
- LLM calls for analysis and summarization

The user gives a repo URL ("help me onboard onto https://github.com/scikit-learn/scikit-learn") and gets back a structured onboarding guide. This is practical - students can use it on their own projects, on repos they contribute to, or on libraries they want to understand.

This example generalizes to other codebase understanding tasks:

- Joining a new team (understand the codebase before your first PR)
- Open source contribution (find where to start, understand conventions)
- Library evaluation (should I adopt this library? is it well-maintained?)
- Technical due diligence (evaluate a codebase before acquisition or investment)
- Migration planning (understand a codebase before migrating frameworks)

## Workflows vs Orchestrated Patterns

Anthropic's key advice: "When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed." And more directly: "When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale." Most of the time, you do not need a full autonomous agent - a workflow is enough[^anthropic].

There are two fundamentally different ways to combine multiple agents. Anthropic calls these "workflows" and "agents"[^anthropic]. OpenAI SDK calls them "code-driven orchestration" and "LLM-driven orchestration"[^openai].

In a workflow (hard-coded pattern), the developer defines the flow in code. You decide which agent runs, in what order, and under what conditions. The agents themselves do not decide who runs next - your code does. Examples: run agent A, take its output, pass it to agent B, loop until a condition is met. This is predictable, debuggable, and you have full control over speed and cost.

In an orchestrated pattern, a central agent (the orchestrator) decides what to do next. The orchestrator is itself an LLM that has other agents available as tools or handoffs. It reasons about the task, decides which agent to invoke, interprets the results, and decides what to do next. This is flexible and adapts to novel inputs, but less predictable and harder to debug.

Pros and cons:

- Workflows: predictable, cheaper (fewer LLM calls for coordination), easier to debug and test, but rigid - they cannot adapt to unexpected inputs
- Orchestrated: flexible, can handle open-ended tasks, adapt dynamically, but more expensive (the orchestrator itself is an LLM call), less predictable, harder to debug

As Anthropic puts it: "Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."[^anthropic]

Many patterns have both a workflow and an orchestrated variant. For example, Evaluator-Optimizer can be a hard-coded while loop (Fixed Evaluator-Optimizer) or orchestrator-driven (Dynamic Evaluator-Optimizer). Plan-and-Execute can use a fixed plan (Static) or replan dynamically (Dynamic). We split these into separate sub-patterns below.

Each group contains sub-patterns that progress from workflow (simpler, hardcoded) to orchestrated (more flexible, LLM-driven). Each sub-pattern is marked as: `workflow` (hard-coded), `orchestrated` (LLM-driven), or `both`.

## Group 1: Routing Patterns `*`

All three patterns below answer the same question: which agent should handle this? The difference is in the lifecycle - what happens before and after the dispatch.

- Simple Routing: a task comes in, classify it, dispatch to one agent, done. The router is just a classifier. No surrounding context, no conversation. One-shot.
- Agents as Tools (Subagent): a parent agent is working on a bigger task, needs help with a subtask, dispatches to a subagent, gets results back, and continues its own work. There is a surrounding task context - the parent keeps working after the subagent returns.
- Handoffs: there is an ongoing conversation with a user. The current agent realizes someone else should take over and transfers the whole conversation. The original agent is done - the new agent continues talking to the user.

### 1a. Simple Routing `both`

The name "Routing" comes from Anthropic's "Building Effective Agents" article[^anthropic], which defines it as: "Routing classifies an input and directs it to a specialized followup task."

Also known as: Dynamic Dispatch (AWS[^aws]), Coordinator/Dispatcher (Google ADK[^google_adk]), Structured Output Routing (OpenAI[^openai]).

A classifier or router agent interprets the intent of an input and directs it to a specialized downstream handler. The router performs a one-time classification and dispatch - it does not synthesize results or maintain ongoing coordination[^anthropic].

How different frameworks implement it:

- Google ADK implements it with an `LlmAgent` using `AutoFlow` to route via `transfer_to_agent()` calls[^google_adk]
- OpenAI SDK implements it as "Structured Output Routing" - the LLM classifies a task into a structured output (e.g., `{"category": "billing"}`), then code selects the next agent based on that classification[^openai]

#### Conference example

Incoming emails to the conference inbox are classified and routed:

- Speaker submissions → program committee agent
- Sponsorship inquiries → sponsorship agent
- Attendee questions → support agent
- Venue-related messages → logistics agent

Each downstream agent has specialized prompts and tools for its domain. The router does not coordinate between them - it just dispatches.

#### YouTube example

Classify the video type and route to a specialized processing pipeline:

- Coding tutorial → extract code snippets, generate runnable examples
- Conference talk → speaker identification, slide extraction
- Podcast interview → conversation structure, key arguments
- Product demo → feature extraction, competitor comparison

#### Other examples

- Customer service: categorizing queries (general questions, refund requests, technical support) and routing each to a specialized handler[^anthropic]
- Model selection routing: routing easy questions to a cheaper model, hard questions to a capable model[^anthropic]
- Contract review: "Can you help me review my contract terms?" is classified as a legal task and routed to a contract review agent[^aws]

#### Codebase onboarding example (implemented)

The user asks a question about scikit-learn. The router classifies the intent and dispatches:

- "How do I set up the dev environment?" → development setup guide agent
- "What's the architecture of the estimator API?" → code architecture agent
- "Where can I find good first issues?" → issue analysis agent
- "What are the coding conventions?" → style and conventions agent

Each downstream agent has specialized prompts and access to relevant parts of the repo.

### 1b. Agents as Tools (Subagent) `*` `both`

The name "Agents as Tools" comes from the OpenAI Agents SDK[^openai].

Also known as: Subagent (this is how I prefer to call this pattern), Nested Chat (AutoGen[^autogen]), Hierarchical Decomposition (Google ADK[^google_adk]).

An agent uses another agent as a tool call - the sub-agent runs in isolation, returns a result, and the parent agent continues with that result. The parent retains control throughout.

The main idea: the problem the subagent solves is that all agents have a context window. The problem is that this context window gets full and the agent can no longer perform its task properly. For context-heavy tasks, we can launch a subagent. For example, an exploration task - we need to explore something. We can launch a subagent to do that[^1].

The subagents take on these heavy contextual tasks so that the main agent's context does not get bloated[^1]. We define agents as tools - an agent is just another tool that we can launch. This is how we build multi-agent systems[^4].

In Claude Code, there is a subagent that does exploration - this is a real-world example of this pattern[^3]. Google ADK implements this with `AgentTool`: a sub-agent is wrapped and included in a parent agent's `tools` list. The parent calls it synchronously, gets results back, and continues[^google_adk].

#### Conference example

The main conference organizer agent delegates to specialized subagents:

- Venue search subagent: searches for venues in Berlin that fit 200 people, checks availability for June, compares prices. Returns a shortlist of 3 venues with pros/cons. This is context-heavy (many search results) but the main agent only sees the clean shortlist.
- Sponsor research subagent: researches potential sponsors, checks their past conference sponsorships, returns a ranked list.
- Speaker search subagent: finds available speakers in the AI space, checks their schedules, returns candidates with bios.

#### YouTube example

The main processing agent delegates to specialized subagents:

- Transcript-fetching subagent: calls the YouTube API, handles pagination, cleans up the raw transcript. Returns a clean transcript without the main agent ever seeing the raw API response data.
- Topic extraction subagent: reads the full transcript, identifies themes, extracts key concepts. Returns a structured list of topics.
- Resource extraction subagent: scans the transcript for all URLs, tools, papers, and libraries mentioned. Returns a clean resource list.

#### Other examples

- In Claude Code, the exploration subagent searches the codebase and returns findings to the main coding agent[^anthropic]
- A ReportWriter agent delegates research to a ResearchAssistant subagent, which itself manages WebSearchAgent and SummarizerAgent[^google_adk]


#### Codebase onboarding example (implemented)

The user asks: "Help me onboard onto scikit-learn." The main agent needs to understand the project, but scikit-learn has ~2,500 files and ~3,000 open issues - too much for one agent's context.

The main agent calls an issue analysis subagent:

- The subagent fetches all 3,000+ open issues via `gh issue list`
- Reads through them, categorizes them (bug / feature / enhancement)
- Identifies "good first issue" labels, finds the most active discussion threads
- This is heavy context - thousands of issues, each with titles, labels, comments
- Returns a one-page summary: "there are 15 good first issues, mostly in `sklearn/preprocessing/` and `sklearn/metrics/`"

The main agent never sees the 3,000 raw issues - it just gets the clean summary and continues building the onboarding guide. The subagent exists because the data is too large for the main agent's context window.

### 1c. Handoffs `orchestrated`

The name "Handoffs" comes from the OpenAI Agents SDK[^openai_handoffs], where it is one of the two primary multi-agent mechanisms alongside Agents as Tools.

Also known as: Agent Transfer (Google ADK[^google_adk]).

The active agent transfers full control of the conversation to another agent. The original agent stops running and the new agent takes over entirely. The handoff is represented as a tool to the LLM - when an agent has a handoff to another agent, the LLM sees a tool named `transfer_to_<agent_name>`[^openai_handoffs]. Google ADK implements the same mechanism via `transfer_to_agent()` function calls within the `AutoFlow` system[^google_adk].

When multiple agents can hand off to each other in a network (without a central supervisor), each agent can transfer to any other agent it knows about, and the "active agent" shifts fluidly across the group.

#### Conference example

An attendee asks a question to the conference assistant chatbot:

- The triage agent determines the question is about visa invitation letters
- It hands off entirely to a visa/travel specialist agent
- That agent takes over the conversation, asks for the attendee's passport details, generates the invitation letter, and handles follow-ups
- If the attendee then asks about the schedule, the visa agent hands off to a program agent

#### YouTube example

A batch video processor receives a video URL. The dispatcher agent does initial analysis and discovers it is a 3-hour conference recording with multiple speakers. It hands off entirely to a "long-form multi-speaker" processing agent that specializes in speaker diarization, per-talk segmentation, and individual talk summarization. A short tutorial video would be handed off to a "tutorial processing" agent instead.

#### Other examples

- Customer support triage: triage agent hands off to billing agent, refund agent, or FAQ agent based on the issue type[^openai_handoffs]
- Escalation handoffs with structured data: the handoff includes a reason for escalation via a Pydantic model[^openai_handoffs]
- Google ADK's Coordinator/Dispatcher routes to specialists via `transfer_to_agent()` - billing vs. technical support[^google_adk]

#### Codebase onboarding example (implemented)

The user asks the onboarding assistant: "How do I run the tests in scikit-learn?"

- The triage agent determines this is about development setup and testing infrastructure
- It hands off entirely to a testing specialist agent
- That agent takes over the conversation, reads `Makefile`, `pytest.ini`, CI configs, and `CONTRIBUTING.md`, and walks the user through the test setup
- The user then asks "What module should I look at first?"
- The testing agent hands off to an architecture guide agent, which takes over the conversation

## Group 2: Pipeline Patterns `*`

All three patterns execute steps in sequence. The difference is how the sequence is determined.

- Prompt Chaining: the sequence is hardcoded. Step A → Step B → Step C. You know exactly what happens at each stage.
- Static Plan-and-Execute: an LLM creates the plan upfront, then the plan is executed step by step without changes. The plan is fixed once created.
- Dynamic Plan-and-Execute: an LLM creates an initial plan, but revises it after each step. Steps can be added, removed, or modified based on what the executor discovers.

### 2a. Prompt Chaining `workflow`

The name "Prompt Chaining" comes from Anthropic's "Building Effective Agents" article[^anthropic], which defines it as: "Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one."

Also known as: Sequential Pipeline (Google ADK[^google_adk]), Agent Chaining / Pipeline (OpenAI[^openai]), Sequential Chat (AutoGen[^autogen]), Prompt Chaining Saga (AWS[^aws]).

Programmatic checks called "gates" can be inserted between steps to verify the process stays on track[^anthropic]. AWS frames it as "Prompt Chaining Saga" - drawing a parallel to saga choreography in distributed systems, where each "thought" is a transaction that can be revisited[^aws].

The key difference from Orchestrator-Workers: in prompt chaining the sequence is fixed and predefined, not determined dynamically by a central agent.

#### Conference example

A fixed pipeline for processing each speaker submission:

1. Extract speaker bio, talk title, and abstract from the submission email
2. Gate: check that all required fields were extracted
3. Classify the talk topic (LLMs, agents, MLOps, etc.)
4. Generate a speaker profile page
5. Create a social media announcement

Each step's output feeds the next.

#### YouTube example

A fixed pipeline for processing the video:

1. Fetch transcript
2. Gate: check that the transcript is not empty
3. Extract key topics
4. Generate summary
5. Format as blog post

Each step's output feeds the next.

#### Other examples

- Generating marketing copy, then translating it to a different language[^anthropic]
- Writing a document outline, running a validation check against criteria, then drafting the full document[^anthropic]
- Blog writing pipeline: research agent → outline agent → drafting agent → critique agent → improvement agent[^openai]
- PDF processing: parser agent extracts text, extractor agent pulls structured data, summarizer agent creates a synopsis[^google_adk]

#### Codebase onboarding example (implemented)

A fixed sequence of LLM calls, each processing the previous one's output:

1. Read the README and produce a concise project overview (what it does, who it's for)
2. Take that overview and the directory listing, identify the key modules and how they relate
3. Take the module map and write a "where to start" section for newcomers
4. Take everything and format the final onboarding document

Each step transforms the previous output into something more refined. The sequence is fixed - always the same 4 steps in the same order.

### 2b. Static Plan-and-Execute `*` `workflow`

The name "Plan-and-Execute" comes from LangChain[^langchain], which defines it as: "a planner which prompts an LLM to generate a multi-step plan" and "executor(s) which accept the user query and a step in the plan and invoke 1 or more tools to complete that task."

Also known as: Planning (Andrew Ng[^ng]), Plan-and-Solve (Wang et al.[^plan_solve]). The concept originates from the Plan-and-Solve paper (Wang et al., 2023) which showed that explicit planning before execution reduces errors even within a single prompt[^plan_solve]. Andrew Ng includes "Planning" as one of his four foundational agentic design patterns[^ng].

The work is separated into two phases:

1. A planner generates a multi-step plan
2. Executor(s) carry out individual steps

In the static variant, the plan is created once and then executed without changes. There are two execution strategies:

- Hand off the entire plan to a single executor as one prompt. The executor receives the full list of steps and works through them in its own context. This works well when the task fits in one context window - e.g., "here are 6 things to analyze about this repo, go."
- Iterate through steps in a for loop, running each step as a separate LLM call. Each step either starts with fresh context (just the step instructions plus a summary from the previous step) or continues in the same context. Use this when individual steps are large enough to need their own context window.

The idea is to split things into two steps: planning and execution. The execution can happen in multiple steps, so the tasks are more granular for the agent. Because of the context window, the agent cannot just do a big task with 10 steps all at once. If you first plan, decompose it into 10 small steps, and then run each step separately, the agent handles it much better[^2].

In Claude Code, there is also planning - you give it a task, it writes a plan, then passes it to a regular agent[^3].

Benefits: faster execution (avoiding LLM calls between each action), cost reductions (using lighter models for sub-tasks), improved performance through explicit reasoning about complete task requirements[^langchain].

LangChain's ReWOO variant fits here - it adds variable references between steps (`#E1`, `#E2`) so steps can reference earlier outputs, but the plan itself is fixed upfront. This reduces LLM calls since there is no replanning[^langchain].

#### Conference example

Given "organize the conference", the planner creates a step-by-step plan:

1. Define conference theme and target audience
2. Research and shortlist venues
3. Set budget allocation
4. Open call for speakers
5. Contact potential sponsors
6. Set up registration system
7. Review speaker submissions
8. Finalize schedule
9. Send confirmations
10. Prepare day-of logistics

The plan is handed to an executor that works through each step in order. The plan does not change during execution.

#### YouTube example

Given "create a comprehensive analysis of this video", the planner creates a fixed plan:

1. Fetch and clean transcript
2. Identify main topics and structure
3. Generate chapter timestamps
4. Create executive summary
5. Extract code examples with context
6. List all tools and resources mentioned
7. Generate a blog post combining everything

The executor runs through all 7 steps regardless of what it finds.

#### Other examples

- Pose matching (HuggingGPT): detect the pose from a photo, then generate a new image matching that pose - a fixed two-step plan[^ng]
- ReWOO: plan with variable references (`#E1 = search("topic")`, `#E2 = summarize(#E1)`) executed without replanning[^langchain]

#### Codebase onboarding example (implemented)

The planner creates a fixed plan for generating the onboarding guide:

1. Fetch repo metadata and directory structure
2. Identify the main modules and their purposes
3. Read `CONTRIBUTING.md` and extract the contribution workflow
4. Analyze the estimator API pattern (base classes, mixins)
5. Find good first issues and categorize by difficulty
6. Compile the onboarding guide

The executor runs through all 6 steps in order without replanning.

### 2c. Dynamic Plan-and-Execute `*` `orchestrated`

The dynamic variant adds replanning: after each step, the planner reassesses and can add, remove, or modify remaining steps based on what the executor discovered.

LangChain's Plan-and-Execute with replanning fits here - the planner reassesses after each step[^langchain]. LLMCompiler takes this further by streaming a DAG of tasks with dependencies, enabling parallel execution of independent steps (claims 3.6x speedup)[^langchain].

#### Conference example

Given "organize the conference", the planner creates an initial plan. After step 2 (venues found), it reassesses - the best venue is more expensive than expected, so it adds a step to find additional sponsors. After step 7 (speaker submissions reviewed), it discovers too few submissions in the "MLOps" track, so it adds a step to do targeted outreach to MLOps speakers.

#### YouTube example

Given "create a comprehensive analysis of this video", the planner creates an initial plan. After step 2 (topics identified), it sees the video has no code - so it drops step 5 (extract code examples) and adds a step to extract diagrams instead. After step 4 (summary created), it discovers the speaker references 3 papers - it adds a step to fetch and summarize those papers.

#### Other examples

- Essay writing: plan an outline, decide what web searches are needed, write a first draft, review, revise, iterate - the plan evolves as the agent discovers gaps[^ng]
- Online research: break "research topic X" into subtopics, search for each, but add new subtopics as the agent discovers them during research[^ng]

#### Codebase onboarding example (implemented)

The planner creates an initial plan for the onboarding guide. After step 2 (identifying modules), it sees that scikit-learn has a `sklearn/utils/` module with many helper functions - it adds a step to document common utilities. After step 4 (analyzing the estimator API), it realizes the API is complex enough to warrant a separate "API cheat sheet" section and adds that step.

## Group 3: Feedback Patterns `*`

All three patterns check output quality. The difference is how the checking works.

- Fixed Evaluator-Optimizer: a while loop in your code. Run generator, run evaluator, check pass/fail, loop or break. The loop logic is hardcoded.
- Dynamic Evaluator-Optimizer: an orchestrator decides when to invoke evaluation, what to evaluate, and what to do with the feedback.
- Human-in-the-Loop: the agent pauses at critical checkpoints and asks a human to review and approve before proceeding.

### 3a. Fixed Evaluator-Optimizer `*` `workflow`

The name "Evaluator-Optimizer" comes from Anthropic's "Building Effective Agents" article[^anthropic], which defines it as: "one LLM call generates a response while another provides evaluation and feedback in a loop." Andrew Ng uses the broader term "Reflection", which also covers the single-agent variant where an agent critiques its own output[^ng].

Also known as: Reflection (Andrew Ng[^ng]), Generator-Critic (Google ADK[^google_adk]), Evaluator Reflect-Refine Loop (AWS[^aws]), Evaluation Looping (OpenAI[^openai]).

In the fixed variant, the loop is hardcoded: run generator → run evaluator → check result in code → loop or break. Google ADK calls this "Generator-Critic" and implements it with `LoopAgent` wrapping a `SequentialAgent` - the critic applies hard, binary pass/fail checks (syntax validity, compliance rules)[^google_adk].

We have a loop: one agent does something, a second one checks whether there are errors or not. The second agent can run things depending on the situation. They iterate until the result is good[^3].

This is how I use it: at the end of a task there is a QA loop. I have a task to write code, I have a coding agent, and I want the code to be verified and working. I create a separate agent whose main focus is specifically verification[^3].

Andrew Ng highlights that this is the most accessible pattern to adopt: "relatively quick to implement" yet yields "surprising performance gains". He showed that GPT-3.5 with an agentic Reflection workflow achieves 95.1% on HumanEval, compared to GPT-4 zero-shot at 67.0%[^ng].

#### Conference example

A schedule generator agent creates a draft conference schedule (talks, breaks, rooms). An evaluator agent checks for conflicts:

- Are two talks in the same room at the same time?
- Is there enough time between sessions for room changes?
- Does any speaker appear in two simultaneous slots?

If conflicts are found, the generator revises. The loop continues until the schedule passes all checks. The loop logic is in code: `while not evaluator.passes(schedule): schedule = generator.revise(schedule, evaluator.feedback)`.

#### YouTube example

A timestamp generator creates chapter timestamps for the video. A verifier agent checks whether each timestamp actually corresponds to a topic change in the transcript - it reads the transcript around each timestamp and verifies. If timestamps are off, it feeds back corrections. The loop continues until all timestamps are accurate[^3].

#### Other examples

- SQL query generation: generator creates queries, critic validates SQL syntax, looping until valid[^google_adk]
- Code generation: generate code, run tests, if tests fail feed errors back, regenerate, loop[^ng]
- Literary translation: a translator LLM drafts a translation, an evaluator critiques nuance, tone, and accuracy, they iterate in a fixed loop[^anthropic]

#### Codebase onboarding example (implemented)

The guide generator writes a section about scikit-learn's module structure. The evaluator checks it against the actual repo: does the file path `sklearn/ensemble/` actually exist? Is the API description correct - does `RandomForestClassifier` really inherit from `BaseEnsemble`? It calls `gh api` to verify file paths and reads actual source files to check class hierarchies. If the guide says something wrong, the evaluator feeds back corrections and the generator rewrites. The loop is hardcoded: generate section → verify facts → loop until all facts check out.

### 3b. Dynamic Evaluator-Optimizer `*` `orchestrated`

Also known as: Iterative Refinement (Google ADK[^google_adk]).

In the dynamic variant, an orchestrator decides when to invoke evaluation and what to do with the feedback. Google ADK calls this "Iterative Refinement" - the critic provides qualitative feedback ("improve X, consider Y") for gradual improvement over multiple passes. The focus is on convergence toward a quality bar rather than a simple pass/fail verdict[^google_adk].

The orchestrator might evaluate after some steps but not others, try a completely different approach if feedback is consistently negative, or escalate to a different agent if the current one cannot improve further.

#### Conference example

The orchestrator generates a budget breakdown. Instead of a fixed pass/fail loop, the orchestrator reads the evaluator's qualitative feedback ("catering budget seems high for 200 people, consider negotiating group rates") and decides what to do - maybe it calls a catering research agent to check market rates, then revises the budget with that new information. The orchestrator adapts its strategy based on the nature of the feedback.

#### YouTube example

The orchestrator generates a blog post from the video. The evaluator says "the section on tool use is too vague - the speaker gave specific examples that are missing." The orchestrator decides to re-read the relevant portion of the transcript, extract the specific examples, and regenerate just that section rather than the whole post.

#### Other examples

- Policy summary generation: generator drafts, evaluator checks coverage, tone, and legal correctness, orchestrator decides which aspects to prioritize[^aws]
- Code performance optimization: initial draft generated, critiqued for efficiency, orchestrator decides whether to optimize algorithm or just clean up implementation[^google_adk]

#### Codebase onboarding example (implemented)

The orchestrator generates the onboarding guide. The evaluator says "the architecture section is accurate but too dense for newcomers." The orchestrator decides to split it into a quick-start overview and a detailed deep-dive, rather than just simplifying. It re-invokes the generator with different instructions for each section.

### 3c. Human-in-the-Loop `workflow`

The name "Human-in-the-Loop" comes from Google ADK[^google_adk], which defines it as a pattern where agents pause execution at defined checkpoints to request human authorization.

Also known as: Human Input Modes (AutoGen[^autogen]). AutoGen implements the same concept via human input modes (`NEVER`, `ALWAYS`, `TERMINATE`) on `ConversableAgent`[^autogen].

Agents handle routine work autonomously but pause execution at defined checkpoints to request human authorization for high-stakes decisions.

When to use: critical decisions such as financial transactions, production deployments, sensitive data operations - any action that is irreversible and requires accountability[^google_adk]. This is a safety and governance pattern, not a performance or quality pattern.

#### Conference example

The agent researches venues and negotiates pricing autonomously. When it is ready to sign a contract and put down a deposit (irreversible financial commitment), it pauses and presents the recommendation to the human organizer for approval. Same for speaker invitations - the agent drafts the invitation but pauses before sending, since a sent invitation represents a commitment.

#### YouTube example

The agent processes the video and generates a blog post. Before publishing to the website or sending a newsletter, it pauses for human review. The human checks that the summary accurately represents the video and that no claims are misattributed.

#### Other examples

- A TransactionAgent processes routine analysis but invokes ApprovalTool before executing high-value transfers[^google_adk]
- Deployment pipelines: automated tests run, but a human must approve production deployment[^aws]

#### Codebase onboarding example (implemented)

The agent generates the onboarding guide for scikit-learn automatically. Before sharing it with the new contributor, it pauses for a senior maintainer to review: "Is the architecture description accurate? Are these really the best first issues to recommend? Is the contribution workflow up to date?" The maintainer corrects one outdated section about the CI setup (they migrated from Travis to GitHub Actions), approves the rest, and the guide is shared.

## Group 4: Coordination Patterns `*`

All three patterns involve multiple agents working on different parts of a problem. The difference is how the work is divided and coordinated.

- Parallelization: the subtasks are predefined and run simultaneously. A programmatic aggregation step combines results. No agent decides what to do - it is all fixed in code.
- Orchestrator-Workers: a central agent (the orchestrator) dynamically decides what subtasks are needed and delegates to workers. The orchestrator adapts based on each worker's results.
- Multi-Agent Collaboration: agents are peers with no supervisor. They share a conversation and collaborate, each contributing from their specialty. A speaker selection mechanism determines who acts next.

### 4a. Parallelization `workflow`

The name "Parallelization" comes from Anthropic's "Building Effective Agents" article[^anthropic], which defines it as: "LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically."

Also known as: Fan-Out/Gather (Google ADK[^google_adk]), Scatter-Gather (AWS[^aws]), Parallel Execution (OpenAI[^openai]).

Multiple agents or LLM calls run simultaneously and their outputs are aggregated. Anthropic distinguishes two sub-variants:

- Sectioning: breaking a task into independent subtasks that run in parallel
- Voting: running the same task multiple times to get diverse outputs

Google ADK calls this "Parallel Fan-Out/Gather" and implements it with `ParallelAgent` - agents run in separate threads sharing `session.state`, each writing to a unique `output_key` to prevent race conditions[^google_adk]. AWS calls it "Parallelization Scatter-Gather" and emphasizes that the aggregation step can itself involve semantic reasoning - identifying themes, contradictions, rather than simple merging[^aws]. OpenAI SDK implements this via Python's `asyncio.gather`[^openai].

#### Conference example

When evaluating a conference venue, run three checks in parallel (sectioning):

- Accessibility agent: checks wheelchair access and public transport
- Capacity agent: verifies room sizes and AV equipment
- Catering agent: checks dietary accommodation options

All three return results simultaneously, which are aggregated into a venue assessment report.

For speaker evaluation (voting): three different evaluation prompts independently rate a speaker submission on:

- Relevance
- Originality
- Speaker experience

The scores are aggregated to make an accept/reject decision.

#### YouTube example

Process a video transcript in parallel (sectioning):

- Summary agent: generates an overview
- Timestamp agent: creates chapter markers
- Quotes agent: extracts key quotes
- Links agent: identifies all URLs and tools mentioned

All run simultaneously on the same transcript, then results are combined into a single structured output.

#### Other examples

- Implementing guardrails: one LLM processes the user query while another screens for inappropriate content[^anthropic]
- Reviewing code for vulnerabilities with multiple prompts, each looking for different issues[^anthropic]
- Automated code review: SecurityAuditor, StyleEnforcer, PerformanceAnalyst running concurrently, then consolidated[^google_adk]
- "Summarize insights across these 10 reports" - scatter to 10 parallel summarization tasks, then aggregate[^aws]
- Evaluating content appropriateness with multiple reviewers, using threshold-based consensus (voting)[^anthropic]

#### Codebase onboarding example (implemented)

Analyze multiple aspects of scikit-learn in parallel (sectioning):

- Code structure agent: maps the module hierarchy and key abstractions
- Documentation agent: evaluates README, docstrings, and developer guides
- Community agent: analyzes issue activity, PR review times, maintainer responsiveness
- Testing agent: checks test coverage, CI configuration, how to run tests locally

All four run simultaneously via `asyncio.gather`, then results are combined into the onboarding guide.

### 4b. Orchestrator-Workers `*` `orchestrated`

The name "Orchestrator-Workers" comes from Anthropic's "Building Effective Agents" article[^anthropic], which defines it as: "a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results."

Also known as: Supervisor (LangGraph[^langgraph]), Manager Agent (CrewAI), Saga Orchestration (AWS[^aws]).

A central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. LangGraph calls this "Agent Supervisor" - "an agent whose tools are other agents" - and implements it with `create_supervisor`[^langgraph]. AWS frames it as the agentic evolution of Step Functions-style central orchestration[^aws].

The key difference from Parallelization: in orchestrator-workers, the subtasks are not pre-defined. The orchestrator determines them on-the-fly based on the specific input[^anthropic].

When we have agents running, the main agent gets output from one agent and the second agent and decides who to run at what moment. This is the orchestration pattern[^4].

LangGraph also defines a "Hierarchical Agent Teams" extension - a multi-tier architecture where supervisors connect to agents that are themselves full LangGraph graphs with their own teams. This creates tree-like structures for complex task decomposition[^langgraph].

#### Conference example

Given "Organize a 200-person AI conference in Berlin in June", the orchestrator agent dynamically decides what needs to happen:

- Asks the venue worker to find options
- Based on venue constraints (no outdoor space), decides to skip the networking garden idea
- Asks the catering worker to plan for indoor-only events
- Notices a speaker cancelled, asks the speaker search worker to find a replacement in the same topic area
- The orchestrator adapts its plan based on each worker's results - the subtasks are not predetermined

#### YouTube example

Given a video URL, the orchestrator examines the transcript and dynamically decides what processing is needed:

- Coding tutorial → calls code extraction worker + dependency identification worker
- Panel discussion → calls speaker identification worker + debate summarization worker
- Product demo → calls feature extraction worker + comparison worker

The orchestrator decides which workers to invoke based on the content it sees.

#### Other examples

- Coding tasks that require changes across multiple files, where the orchestrator identifies which files need changes and delegates each to a worker[^anthropic]
- Search tasks requiring information gathering from multiple sources, where the orchestrator decides what to search for[^anthropic]
- "Create a project brief and summarize top 5 competitors" - orchestrator assigns research agent, summarization agent, brief-writer agent[^aws]

#### Codebase onboarding example (implemented)

The user asks: "Help me understand scikit-learn well enough to contribute." The orchestrator examines the repo and dynamically decides what to investigate:

- Sees a `CONTRIBUTING.md` → dispatches a worker to extract the contribution workflow
- Reads the top-level `__init__.py` and discovers the estimator API is central → dispatches a worker to document the `BaseEstimator` pattern
- Checks recent PRs and notices most contributions are to `sklearn/ensemble/` → dispatches a worker to analyze that module specifically
- Finds that the project uses `pytest` with custom fixtures → dispatches a worker to document the test setup

The orchestrator adapts based on what it discovers - it does not follow a fixed checklist.

### 4c. Multi-Agent Collaboration `orchestrated`

The name "Multi-Agent Collaboration" comes from Andrew Ng's agentic design patterns[^ng], where he defines it as: "More than one AI agent work together, splitting up tasks and discussing and debating ideas, to come up with better solutions than a single agent would."

Also known as: Group Chat (AutoGen[^autogen]), Shared Scratchpad (LangGraph[^langgraph]). LangGraph uses the same name and calls the implementation "Shared Scratchpad"[^langgraph]. AutoGen implements it as "Group Chat" with a `GroupChatManager`[^autogen].

Multiple agents participate in a shared conversation where all agents see each other's intermediate work. There is no single supervisor that decomposes and delegates - instead, agents collaborate as peers with a speaker selection mechanism determining who acts next. AutoGen supports four speaker selection strategies: `auto` (LLM decides), `round_robin`, `random`, and `manual`[^autogen].

The key distinction from Orchestrator-Workers: in orchestrator-workers, a central agent decomposes the task and delegates. In multi-agent collaboration, agents are peers - no one agent owns the decomposition. The shared scratchpad means full transparency but higher verbosity[^langgraph].

LangChain explicitly contrasts the two: the supervisor pattern uses independent scratchpads with only final outputs shared, while multi-agent collaboration uses a shared scratchpad where all intermediate steps are visible to everyone[^langgraph].

#### Conference example

Three agents collaborate on designing the conference schedule: a content agent focuses on topic diversity and talk quality, a logistics agent focuses on room capacities and timing constraints, and a budget agent tracks costs. The content agent proposes adding a workshop track. The logistics agent responds that there are not enough rooms. The budget agent suggests renting an extra room and shows the cost impact. The content agent adjusts - maybe a panel instead of parallel workshops. They iterate in a shared conversation until they converge on a schedule that satisfies content quality, logistical feasibility, and budget constraints.

#### YouTube example

Three agents collaborate on creating course material from a video: a content expert agent identifies the key learning objectives, a pedagogy agent structures the lesson with exercises and quizzes, and a technical accuracy agent verifies all code examples and claims against the original transcript. The pedagogy agent proposes a hands-on exercise, the technical accuracy agent points out the code version in the video is outdated, the content expert suggests an alternative. They iterate in a shared thread until the course module is solid.

#### Other examples

- Virtual software company (ChatDev): CEO, designer, programmer, and tester agents collaborating to build software[^ng]
- Software development teams with agents as software engineer, product manager, designer, QA engineer - each with independent workflows[^ng]
- AutoGen Group Chat with coder, executor, scientist: custom speaker selection retries coder on execution failure[^autogen]

#### Codebase onboarding example (implemented)

Three agents collaborate on building the scikit-learn onboarding guide in a shared conversation:

- Architecture agent: maps the module structure, identifies key patterns (estimator API, transformer pipeline)
- Community agent: analyzes issues, PRs, and maintainer activity
- Pedagogy agent: structures the guide for a newcomer's learning path

The architecture agent describes the estimator inheritance hierarchy. The pedagogy agent responds: "This is too detailed for a first read - let's start with a simple example of `fit`/`predict` before diving into base classes." The community agent adds: "There are 15 open issues tagged 'good first issue' in `sklearn/preprocessing/` - that's a good module to start with since the estimator pattern is simple there." They iterate until the guide balances technical accuracy with approachability.

## Building Blocks

These are foundational capabilities that underpin the patterns above, rather than multi-agent patterns themselves.

### Tool Use (Augmented LLM)

Andrew Ng defines Tool Use as one of his four foundational agentic patterns: the LLM is given tools such as web search, code execution, or any function to help it gather information, take action, or process data[^ng]. Anthropic describes the building block as the "Augmented LLM" - an LLM enhanced with retrieval, tools, and memory[^anthropic]. This is mature enough "to work fairly reliably" in production[^ng].

## Cross-Reference Table

| Group | Pattern | Anthropic | OpenAI SDK | Google ADK | AWS | LangGraph | AutoGen | Andrew Ng |
|---|---|---|---|---|---|---|---|---|
| Routing | Simple Routing | Routing | Structured Output Routing | Coordinator/Dispatcher | Routing Dynamic Dispatch | - | - | - |
| Routing | Agents as Tools | - | Agents as Tools | AgentTool | - | - | Nested Chat | - |
| Routing | Handoffs | - | Handoffs | Agent Transfer / AutoFlow | - | - | - | - |
| Pipeline | Prompt Chaining | Prompt Chaining | Agent Chaining | Sequential Pipeline | Prompt Chaining Saga | - | Sequential Chat | - |
| Pipeline | Static Plan-and-Execute | - | - | - | - | Plan-and-Execute | - | Planning |
| Pipeline | Dynamic Plan-and-Execute | - | - | - | - | Plan-and-Execute (replanning) | - | Planning |
| Feedback | Fixed Evaluator-Optimizer | Evaluator-Optimizer | Evaluation Looping | Generator-Critic | Evaluator Reflect-Refine Loop | - | - | Reflection |
| Feedback | Dynamic Evaluator-Optimizer | Evaluator-Optimizer | Evaluation Looping | Iterative Refinement | Evaluator Reflect-Refine Loop | - | - | Reflection |
| Feedback | Human-in-the-Loop | - | - | Human-in-the-Loop | - | - | Human Input Modes | - |
| Coordination | Parallelization | Parallelization | Parallel Execution | Parallel Fan-Out/Gather | Scatter-Gather | - | - | - |
| Coordination | Orchestrator-Workers | Orchestrator-Workers | - | - | Saga Orchestration | Supervisor | - | - |
| Coordination | Multi-Agent Collaboration | - | - | - | - | Multi-Agent Collaboration | Group Chat | Multi-Agent Collaboration |

## My Proposed Order for the Course

1. Routing Patterns `*`
   - 1a. Simple Routing (classify and dispatch)
   - 1b. Agents as Tools / Subagent `*` (delegate subtask, get result back)
   - 1c. Handoffs (transfer the conversation)

2. Pipeline Patterns `*`
   - 2a. Prompt Chaining (fixed sequence)
   - 2b. Static Plan-and-Execute `*` (LLM creates plan, then execute without changes)
   - 2c. Dynamic Plan-and-Execute `*` (replan after each step)

3. Feedback Patterns `*`
   - 3a. Fixed Evaluator-Optimizer `*` (while loop: generate, evaluate, loop)
   - 3b. Dynamic Evaluator-Optimizer `*` (orchestrator decides when/how to evaluate)
   - 3c. Human-in-the-Loop (human approval)

4. Coordination Patterns `*`
   - 4a. Parallelization (fixed fan-out/gather)
   - 4b. Orchestrator-Workers `*` (supervisor delegates dynamically)
   - 4c. Multi-Agent Collaboration (peer-to-peer group chat)[^3]

I will iterate further with Claude Code on how to best decompose this into units[^4].

## Sources

[^1]: [20260221_193111_AlexeyDTC_msg2190_transcript.txt](../inbox/used/20260221_193111_AlexeyDTC_msg2190_transcript.txt)
[^2]: [20260221_193257_AlexeyDTC_msg2192_transcript.txt](../inbox/used/20260221_193257_AlexeyDTC_msg2192_transcript.txt)
[^3]: [20260221_193907_AlexeyDTC_msg2194_transcript.txt](../inbox/used/20260221_193907_AlexeyDTC_msg2194_transcript.txt)
[^4]: [20260221_194006_AlexeyDTC_msg2196_transcript.txt](../inbox/used/20260221_194006_AlexeyDTC_msg2196_transcript.txt)

## References

[^anthropic]: [Building Effective Agents - Anthropic](https://www.anthropic.com/research/building-effective-agents)
[^ng]: [Andrew Ng's Agentic Design Patterns](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
[^openai]: [OpenAI Agents SDK - Multi-agent](https://openai.github.io/openai-agents-python/multi_agent/)
[^openai_handoffs]: [OpenAI Agents SDK - Handoffs](https://openai.github.io/openai-agents-python/handoffs/)
[^langchain]: [Plan-and-Execute Agents - LangChain](https://blog.langchain.com/planning-agents/)
[^langgraph]: [Multi-Agent Concepts - LangGraph](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)
[^google_adk]: [Multi-Agent Patterns in ADK - Google](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
[^aws]: [Agentic AI Patterns - AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agentic-workflow-patterns.html)
[^autogen]: [Conversation Patterns - Microsoft AutoGen](https://microsoft.github.io/autogen/0.2/docs/tutorial/conversation-patterns/)
[^plan_solve]: [Plan-and-Solve Prompting - Wang et al. 2023](https://arxiv.org/abs/2305.04091)
