---
title: "Plan: Carlos Pumar"
created: 2026-04-20
updated: 2026-04-23
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Carlos Pumar

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: Economist at the German Savings Banks with a fairly concrete project idea already in mind: a personal agent for SMEs that turns manual financial notes into structured data and answers business questions from that data.
- Goal for the next 6 weeks: turn the idea into a scoped build plan and a first working prototype rather than another loose concept.
- Main gap to close: structure. The idea is promising, but it needs a clearer engineering sequence and a tighter project outline.
- Weekly time commitment: not explicitly stated; this should be treated as a tight 6-week sprint.
- Why this plan is the right next step: Carlos already has a strong domain-specific idea, so the highest-leverage move is to scope the first version tightly and build from that.

## Plan

### Focus

- Main focus: define the SME agent clearly enough that the first version can actually be built.
- Supporting focus: break the project into two concrete parts: data ingestion from manual notes and business-question answering over the stored data.
- Supporting focus: separately reproduce and analyze the stability/security concern from the previous project.

### Timeline

Week 1:

- Translate the SME agent idea into a clear outline: user flow, inputs, outputs, database structure, and success criteria.
- Decide what the first version should and should not do.

Week 2:

- Collect a small example dataset of manual notes and define the extraction format.
- Write down a simple test set of example business questions the final system should be able to answer.

Week 3:

- Build the first tool: ingest pictures of manual notes, extract the relevant financial data, and write it into a database.
- Keep the scope narrow: one reliable ingest flow is better than many half-working paths.

Week 4:

- Build the second tool: query the stored data through natural-language business questions.
- Define a small set of example questions and expected answers to test the system end to end.

Week 5:

- Connect the ingestion and query parts into one end-to-end prototype.
- Fix the biggest gaps in the workflow, data model, or output quality.

Week 6:

- Review the prototype against the original outline and decide the next iteration.
- Revisit the previous project's stability/security issue, try to reproduce it, and write down what is actually known vs. still unknown.

### Resources

- Carlos's own project notes and examples - the main raw material for scoping the first version correctly.
- Carlos's previous Buildcamp project - useful both as a reference point and for reproducing the reported instability issue.
- Claude Code analysis, with review by Alexey - acceptable for exploratory stability analysis, but it should be framed honestly as a first-pass investigation rather than a security audit.

### Deliverables

- A written outline for the SME agent: problem definition, workflow, data model, and first-version scope.
- A small example dataset plus a test set of business questions for validation.
- A first working prototype covering note ingestion plus database querying.
- A short internal note on the previous project's stability/security question, including what could and could not be reproduced.

### Accountability

- Weekly async check-in focused on what moved from idea to artifact.
- One review milestone after the first-version scope is fixed, before implementation starts.
- One review milestone after the first end-to-end prototype works locally.

### Next Steps

- [ ] [Carlos] Confirm that the SME agent is the main project to prioritize over the next 6 weeks.
- [ ] [Carlos] Write down what the first version must do and what it should explicitly exclude.
- [ ] [Carlos] Share the link to the previous project and any details he still remembers about the instability feedback.
- [ ] [Alexey] Review the scoped first version before implementation starts.

## Internal Context

### Persona

Sam - The Technical Professional Moving to AI. Domain expert with some technical project experience, but still needs a clearer engineering framework to turn ideas into a structured build.

### Background

Carlos works as an economist for the German Savings Banks. He already has a concrete AI project idea and has also built at least one prior project through the AI Engineering Buildcamp context. The main need here is not ideation but structuring the work into a buildable sequence.

#### Previous Project: User Satisfaction Analyst Agent

Carlos's earlier project was the **User Satisfaction Analyst Agent**. The goal was to analyze client satisfaction using Stack Exchange data, with a focus on user-interface discussions to identify frustration patterns.

Architecture notes:

- A Docker-based pipeline fetches the data and stores it in two systems:
- MongoDB for unstructured data
- Neo4j for graph data
- An orchestrator agent decides how to route user questions
- Questions about "what" or "how" go to a MongoDB-focused agent
- Relationship-oriented questions go to a Cypher agent that translates natural language into graph queries
- Carlos noted that the orchestrator often called both agents in parallel to be on the safe side

### Intake

#### Initial Input

Hi Valeriia, thx for the clarification...definitely neat it will be for free (tho I would also understand if it would cost, I realize it's a time investment (and more) for both of you...I'd be happy to chat!

I'm an Economist and work for the German Savings Banks.

The next project will include a personalized agent, which is supposed to read financial data of a small entrepreneur (based on pictures taken from manual notes, tool 1) and write the data into a DB. The second tool will be to query the DB based on the questions the user makes (all related to understanding better the business: which months were good, which less good, how has the cost of purchased goods changed over time, what profits were made in which month, etc.). So this time it's a bit less about orchestration, but more on having a performing "personal agent" for SME (small and medium enterprises).

Another thing I would like to work on is understanding better security risks of my prior project as well as to test the "long run performance" of the project you refer to above. I received feedback on LinkedIn on it related to it being "unstable" after running it for "n" iterations (unfortunately, I can't find the message anymore) and never really understood what the feedback was about. I still would be very interested in understanding it better (maybe Alexey can help me 1. finding that comment again and 2. thinking about the stability of the project).

#### Questions and Answers

No separate follow-up questionnaire was sent. Valeriia noted that Carlos had already provided enough detail in his initial message to work from.[^2]

### Meeting Notes

No separate intake call notes are currently attached in this file.

### Internal Recommendations

Carlos already has fairly concrete ideas. The most useful move is to help him write them out in more detail rather than asking him to start from zero again[^3].

For the SME agent idea, the recommendation is to give Carlos something structured to react to. The plan should be framed as a review and a suggestion, not as the final answer.

For the prior project's security/stability issue, Alexey does not want to overclaim expertise. The practical recommendation is:

- help Carlos find the old project and any missing context
- try to reproduce the issue
- be explicit that any deeper analysis is exploratory and not a formal security review

For the main project plan, the practical next step is to turn Carlos's idea into a concrete first-version spec: what goes in, what comes out, what gets stored, and which business questions must work in the first prototype.

### Internal Action Items

- [ ] [Alexey] Help locate the link to Carlos's User Satisfaction Analyst Agent project if it is not easy for Carlos to find himself.
- [ ] [Alexey] Review Carlos's first-version scope and help tighten it if it is too broad.
- [ ] [Carlos] Try to reproduce the reported instability issue and capture any observations.

### Sources

[^1]: [Google Doc](https://docs.google.com/document/d/1eACirruKSSj-n0SI2XWMQwW7nnhWG8vQ93m-nam-9Co/edit?usp=sharing)
[^2]: [20260420_083739_AlexeyDTC_msg3442.md](../../../inbox/used/20260420_083739_AlexeyDTC_msg3442.md)
[^3]: [20260420_102138_AlexeyDTC_msg3472_transcript.txt](../../../inbox/used/20260420_102138_AlexeyDTC_msg3472_transcript.txt)
