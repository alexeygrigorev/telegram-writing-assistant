---
title: "Project Discovery AI Agent"
created: 2026-03-05
updated: 2026-03-05
tags: [research, agents, design-thinking, projects]
status: draft
---

# Project Discovery AI Agent

An AI agent that acts as a Design Thinking facilitator, guiding people through multiple sessions to go from "I don't know what to do" to a concrete engineering project idea[^1].

This is not a regular Q&A bot. It is closer to coaching and discovery. The agent asks questions, clarifies, and helps think - it does not immediately propose ideas.

See also: [Design Thinking for Finding Project Topics](design-thinking-for-projects.md) - the frameworks and methodology this agent is based on.

## Overall structure

The process is split into 4 sessions, each about 15-30 minutes. Between sessions there are homework assignments[^1].

Session flow:
1. Session 1: Interests and Context
2. Session 2: Problem Discovery
3. Session 3: Idea Generation
4. Session 4: Project Selection

## Session 1: Interests and Context

Goal: understand what the person's life looks like[^1].

The agent asks open-ended questions and follows up with clarifications.

## Hobbies block

Questions:
- What hobbies do you have?
- What do you enjoy doing in your free time?
- What do you like to read or watch videos about?
- What topics can you talk about for hours?

Follow-ups:
- How long have you been doing this?
- What tools do you use?
- Are there communities around this?

## Work and activity block

- What are you currently doing (work, study, projects)?
- What tasks do you do most often?
- What takes the most time?

## Interests block

- What technologies interest you?
- What projects do you consider cool?
- What would you like to learn to do?

## Session result

The AI creates a profile with key areas, interests, technologies, and tools.

## Homework

The AI asks the person to pay attention to their daily routines during the next few days and write down things that annoy them, take too long, or feel manual.

## Session 2: Problem Discovery

Goal: find real problems[^1].

Questions:
- What problems did you notice in the last few days?
- What tasks repeat?
- What annoys you?

## Category-specific questions

Automation: What do you do manually?

Information: What is hard to find?

Data: What data do you have?

Tools: What apps annoy you?

## Hobby-specific questions

- What is inconvenient in your hobby?
- What tasks repeat there?
- What do people discuss as a problem in those communities?

## Expanding the list

The AI helps expand the problem list based on the person's profile from Session 1.

## Homework

Talk to colleagues, friends, and online communities. Ask them: "What problem would you solve if you could?"

## Session 3: Idea Generation

Goal: turn problems into many solutions[^1].

## Step 1: Select 3 problems

The AI asks:
- Which problem seems the most interesting?
- Which one comes up most often?
- Which one do you understand best?

## Step 2: Generate ideas

Rule: at least 10 ideas per problem.

## Catalyst questions

The AI uses directed questions to trigger ideas:

- Automation: can this be automated?
- Prediction: can something be predicted?
- Recommendation: can something be recommended?
- Classification: can something be classified?
- Search: can search be improved?
- Analysis: can data be analyzed?

## Result

A list of 10+ ideas grouped by problem.

## Session 4: Project Selection

Goal: choose the best project and formulate it[^1].

## Evaluation criteria

The AI asks the person to rate each idea:

| Criterion | Question |
|-----------|----------|
| Interest | Is it interesting to work on? |
| Usefulness | Does it solve a problem? |
| Data | Is data available? |
| Complexity | Can it be done? |

## Technical specification

After choosing an idea, the agent asks engineering questions:

- Data: what data is needed?
- Input: what does the user enter?
- Processing: what algorithm?
- Output: what does the system produce?
- Evaluation: how to measure success?

## Final result

The AI generates a project card with the problem, solution, data, model, output, and evaluation metric.

## Detailed conversation tree (state machine)[^2][^3][^4]

The conversation follows a tree structure with branches. Each node has a goal, 1-2 questions, and a next step.

## Stage 0 - Setup (2-3 minutes)

Goal: set the constraints so it is easier to filter ideas later.

Questions:
- How much time/weeks are you willing to spend on the project?
- Do you want more: usefulness or learning (or 50/50)?
- What constraints do you have: data/hardware/language/domains/ethics?

Output: project constraints.

## Stage 1 - Domain Scan (10 minutes)

Goal: find 2-4 domains where the person genuinely cares.

Questions (quick scan):
- Top 3 hobbies/topics you voluntarily spend time on?
- Top 3 types of tasks at work/in life that repeat?

If the person doesn't know or answers vaguely, use the help branch:
- If you had 5 extra hours per week, what would you spend them on?
- What do you most often read/watch online "just because"?

Output: shortlist of domains.

## Stage 2 - Problem Harvest (15-25 minutes)

The most important stage. Goal: collect raw material - 20+ problems, frictions, manual work.

Questions:
- What in these domains most often annoys you or takes too much time?
- What do you do manually over and over?
- Where do you regularly search for information and can't find it quickly?

Facilitator rule: do not discuss solutions. Only "what happens."

Output: raw problem list.

## Stage 3 - Problem Shaping (10-15 minutes)

Goal: turn raw material into good problem statements and select 3-5 best ones.

Questions:
- Which problem occurs most often?
- Which one is most annoying?
- Which one is closest to data/engineering?

Formulation template: [Who] experiences [what] in [context] because [why].

Output: 3-5 clear problems.

## Stage 4 - Solution Sprint (15-20 minutes)

Goal: 10 ideas for 1 problem (or 30 ideas for 3 problems).

Micro-rules:
- 10 ideas without criticism
- Bad ideas are allowed (they accelerate good ones)

Catalyst questions:
- Can this be automated?
- Can this be predicted?
- Can this be recommended?
- Can search be improved?
- Can this be summarized?
- Can anomalies be detected?

Output: list of solutions.

## Stage 5 - Feasibility Gate (10 minutes)

Goal: filter out what won't work.

4 quick filters:
- Data: does data exist or can it be collected?
- Time: can an MVP be built in N weeks?
- Eval: how to measure success?
- Scope: can a simple version be made?

Output: 1-3 finalists.

## Stage 6 - Project Definition (5-10 minutes)

Goal: lock in the project so work can start tomorrow.

Template:
- I will build X for Y to solve Z
- MVP: input, processing, output
- Quality metric
- Plan for 3 sprints

## Stage 7 - Homework Loop (between sessions)

If the person "doesn't know" or "nothing comes to mind," the agent gives short assignments:

- Observation diary (2 days): write down 10 things that annoy/take too long/are manual
- Community mining (30 minutes): find 10 complaints from forums/Reddit/Discord/Telegram
- Data check (20 minutes): find 2-3 data sources, APIs, or datasets

## Problem Discovery Framework - 8 lenses[^2][^3]

A systematic approach to generate 30-60 problems. Go through 8 lenses. Target: 5-10 problems per lens.

## Lens A - Friction

- What annoys you?
- Where does "something always break"?
- Where do you have to do extra clicks/steps?

## Lens B - Time sinks

- What takes disproportionately long?
- What do you end up doing "in batches" on weekends?

## Lens C - Manual repetition

- What repeats weekly?
- What gets copied between services?
- Where do you have to "combine" data manually?

## Lens D - Decision pain

- Where is it hard to choose?
- Where are there too many options?
- Where do you lack confidence/data?

## Lens E - Information chaos

- Where is it hard to find what you need?
- Where are documents/chats/emails too long?
- Where is it hard to identify the main point?

## Lens F - Tracking and accountability

- What do you want to track but find tedious?
- Where is there no transparency of progress?

## Lens G - Quality and errors

- Where do people often make mistakes?
- Where are deadlines/steps missed?
- Where are there "typical" failures?

## Lens H - Community complaints

- What do people argue about or complain about?
- What questions repeat "every day"?

## Practice: 50 problems in 30 minutes

1. Pick 2 domains (e.g. hobby + work)
2. For each lens, write at least 3 items
3. Do not discuss solutions - only problems
4. Then cluster: combine repeating ones

## Trigger Library[^3][^4]

Not project ideas but triggers that give the brain something to latch onto. Each trigger comes with questions and example project types.

## Trigger 1 - Data inventory

Questions:
- What data do you already have? (files, notes, trackers, logs, histories)
- What data do you regularly create?
- What data is easy to get from the internet for your hobby?

Project types: dashboard/analytics, forecast/scoring, anomaly detection, search/indexing.

## Trigger 2 - Routine automation

Questions:
- What do you do by hand every week?
- What do you copy between tools?
- What "mini-processes" repeat?

Project types: ETL pipeline, API integrations, workflow automation, "assistant bot" for routine.

## Trigger 3 - Knowledge search and navigation

Questions:
- Where do you most often search for things?
- What documents/chats/materials are hard to "dig through"?

Project types: semantic search, RAG / Q&A on personal data, summarization + action item extraction, knowledge graph (light version).

## Trigger 4 - Recommendations

Questions:
- Where do you choose from thousands of options? (books, courses, games, exercises, recipes)
- What would you like the system to "surface at the right time"?

Project types: recommender system, personalized collections, ranking/scoring.

## Trigger 5 - Planning and habits

Questions:
- Where do you break down?
- What is hard to keep regular?

Project types: tracker + "will I break down" prediction, smart reminders (context-aware), behavior pattern analysis.

## Trigger 6 - Quality evaluation

Questions:
- Where is result quality important but evaluation is subjective? (photos, texts, workouts)
- What do you want to compare "before/after"?

Project types: scoring model, "good/bad" classification, progress analysis.

## Trigger 7 - Community and content

Questions:
- What chats/forums do you participate in?
- What questions repeat there?
- What is hard to moderate/structure there?

Project types: topic classification, chat search, auto-FAQ / bots, toxicity/spam detection (if applicable).

## Trigger 8 - Marketplaces and prices

Questions:
- What do you buy/compare?
- Where do prices fluctuate?
- Where do you want to "catch" good moments?

Project types: data collection + monitoring, forecast/alerts, product clustering.

## Universal project templates[^4]

Ready-made "skeletons" the agent can suggest:

1. Data pipeline to dashboard
2. Search / semantic search over a corpus
3. RAG assistant on personal/domain data
4. Recommender / ranking
5. Classifier (topic/tone/genre/type)
6. Extractor (from PDF/web/email) to structured data
7. Anomaly detection / monitoring
8. Forecasting / prediction
9. Clustering / segmentation
10. Optimization / scheduling

## Agent implementation details[^4]

## State the agent maintains

- domains[]
- problems_raw[]
- problems_shaped[]
- ideas[]
- finalists[]
- constraints (time, data, tooling)
- homework_log

## Behavior rules

- 1-2 questions per turn
- Every 5-7 messages: brief summary + what's next
- If "I don't know," activate the Homework Loop or Trigger Library

## Agent tone

Open question: should the agent be strict (like an interviewer) or soft (like a coach)? The tone of the prompt and answer structure needs to be tuned accordingly[^4].

## Sources

[^1]: [ChatGPT conversation on project frameworks](https://chatgpt.com/share/69a997f4-9d50-800a-a2e7-32823e7b293b) via [20260305_145128_AlexeyDTC_msg2754.md](../../inbox/used/20260305_145128_AlexeyDTC_msg2754.md)
[^2]: [20260305_145306_AlexeyDTC_msg2759.md](../../inbox/used/20260305_145306_AlexeyDTC_msg2759.md)
[^3]: [20260305_145306_AlexeyDTC_msg2760.md](../../inbox/used/20260305_145306_AlexeyDTC_msg2760.md)
[^4]: [20260305_145306_AlexeyDTC_msg2761.md](../../inbox/used/20260305_145306_AlexeyDTC_msg2761.md)
