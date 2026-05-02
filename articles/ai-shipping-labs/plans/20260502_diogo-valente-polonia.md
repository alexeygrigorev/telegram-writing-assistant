---
title: "Plan: Diogo Valente Polónia"
created: 2026-05-02
updated: 2026-05-02
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Diogo Valente Polónia

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: Diogo has three candidate project ideas (scraping + structured datasets, public-data explorer/fetcher, multi-agent expert elicitation) but has not picked one yet. He works at the European Environment Agency on the European Climate Risk Assessment and wants a tool he actively uses at work.
- Goal for the next 6 weeks: a working, deployed first version of one project, using a single agent rather than a multi-agent system. Picked project: the third one (expert elicitation) - reframed to use one agent only.
- Main gap to close: choosing a project and starting. Once the project is picked, the path is the same as for other course members - conceptually describe what the agent should do, write the underlying logic as functions, then wrap them in an agent.
- Weekly time commitment: ~10 hours per week of build time on top of course content consumption. Realistic average closer to 5 hours, but plan is sized for the higher end.
- Why this plan is the right next step: Diogo is already on the Buildcamp; the course covers the build pattern. The blocker is choice paralysis, which is why this plan picks the project for him. Multi-agent systems are dropped because they make everything more complex and tangled at this scope.

## Plan

### Focus

- Main focus: build the first version of the expert-elicitation agent (project #3 from the candidate list) using a single agent, not a multi-agent system. The single-agent constraint is deliberate - multi-agent makes things much more complex and tangled, especially in a 6-week build with limited weekly hours.
- Supporting focus: deploy the agent so it is actually usable at work. The deliverable is "a tool I'm actively using now at work", not a notebook.
- Supporting focus: implement the underlying logic (data lookups, expert-perspective prompts, synthesis step) as plain Python functions first, then wrap them in an agent that decides when to call which one.

### Why this project

All three candidate projects are interesting and any of them could be built in 6 weeks. The third one (expert elicitation) is picked here for two reasons:

- It is the most distinctive and the one Diogo cannot easily get from existing tools. The scraping/structured-dataset and data-explorer ideas are useful but closer to traditional data engineering with an LLM bolted on; expert elicitation maps onto the domain expertise (climate assessment statements, multi-perspective discussions) that Diogo already has access to at the EEA.
- Reducing it to a single agent removes the multi-agent complexity while keeping the interesting part - the agent reasoning about a problem from multiple expert perspectives in sequence rather than running multiple agents in parallel.

If Diogo strongly prefers one of the other two, both are also sensible. The data-explorer/fetcher option in particular is a fine alternative because the team often hits the "does this data exist somewhere?" question. The principle is: pick one this week and start, do not shop the list further.

### Timeline

Week 1:

- Lock the project. The default pick is the expert-elicitation agent with a single agent. If Diogo wants to switch to one of the other two, decide this week and stop comparing.
- Conceptually describe what the agent should do. The exercise is small and important: a user submits a question (e.g. "what does the panel say about flood risk in southern Europe?") - what should happen, where should the agent go, what should it do, what should it return. Write this down in plain English before any code.
- Pick one coding assistant for boilerplate (Claude Code, Codex, or similar). Avoid free tiers.

Week 2:

- Implement the underlying functions as plain Python: data fetchers (existing reports, public datasets, internal docs), an "expert perspective" prompt template for each role the agent should role-play, a synthesis function that combines the perspectives. No agent yet - just functions you can call from a notebook or a CLI and get reasonable answers.
- Confirm the functions return useful output on a real EEA-relevant question.

Week 3:

- Introduce the agent. Wrap the functions as tools and let the agent decide which to call and in what order for a given input. Keep the agent loop simple - one model, one tool list, no sub-agents.
- Run the agent on three or four representative questions and compare the output to the function-only baseline.

Week 4:

- Deploy a first version. Streamlit Community Cloud, a small VM, an internal app inside the EEA stack - whatever lets you actually use the tool at work. The goal is "Diogo opens the tool during his actual workflow", not a public launch.
- Add basic logging so failures and slow tool calls are visible.

Week 5:

- Iterate based on actual use. Whatever the first weeks of real use surface (missing data sources, prompts that need tightening, a tool that the agent never picks correctly) is the priority for this week.
- Tighten prompts for the expert-perspective roles based on what the synthesis step is missing.

Week 6:

- Wrap to a state where the tool is used at least once a week as part of Diogo's actual work. Update the README so the next iteration (more perspectives, deeper data sources, a multi-agent split if it becomes necessary) is easy to plan.
- Decide what the next 6-week iteration looks like, or whether to switch to a second project at this point.

### Project approach

- Pick one project and start. Choice paralysis is the actual blocker; the project pick above resolves it. Switching projects mid-sprint is more expensive than picking the wrong one and finishing.
- One agent, not multi-agent. Multi-agent looks elegant in diagrams; in code it usually means tangled message passing and many places where things can fail silently. Single agent with a good toolset is the right starting point. If a multi-agent split becomes necessary later, the existing tools and prompts carry over.
- Concept first, implementation second. Describing what the agent does in plain English before writing any code is the cheap step that prevents three days of throwaway implementation.
- Functions before agent. If you can call the tools directly and get good answers, the agent's job is orchestration rather than reasoning from scratch. Easier to debug, easier to iterate.
- Deployment is part of building. The 10 hours per week budget includes deployment - the tool is not "done" until Diogo is actually using it at work.

### Resources

- AI Engineering Buildcamp - already enrolled. The course covers the conceptual-to-implementation pattern for agents; following the modules is the primary reference.
- AI Shipping Labs first workshop on Telepot agents and deployment to Render (community recording, week of 2026-04-20) - useful as a deployment-walkthrough reference if Diogo wants to see one path end to end. Available to community members; ask Valeriia for the link.
- Coding assistant of choice (Claude Code or Codex). Pick one and commit.
- The EEA's existing reports and the multi-perspective expert engagement materials Diogo already has access to - the source content for the agent's tools.

### Deliverables

- Concept doc + project pick locked - by end of week 1.
- Underlying functions returning useful output on a real question - by end of week 2.
- Agent wrapping the functions, validated against three or four questions - by end of week 3.
- First deployed version Diogo uses at work - by end of week 4.
- Iterated version with prompts and tools tightened from real use - by end of week 5.
- Tool in regular use, README updated, next-iteration plan written - by end of week 6.

### Accountability

- Weekly check-in: what shipped, what is blocked, what is the goal for the next week. Diogo named "discussion-based, someone he can ask 'is this feasible'" as the format that works for him; the weekly cadence is built around that.
- 10 hours per week build budget on top of course time. If a week slips, drop a stretch goal rather than extending the week.
- Share progress in the AI Shipping Labs Slack - other members work in adjacent domains and can help calibrate "is this a 2-week or a 4-week task" questions.

### Next Steps

- [ ] [Diogo] Complete the questionnaire so the plan has a clean intake on file.
- [ ] [Diogo] Confirm the project pick (default: expert-elicitation single-agent) by end of week 1.
- [ ] [Diogo] Write the concept doc (what the agent does in plain English) before any code.
- [ ] [Alexey] Send the written plan and confirm the location of the AI Shipping Labs workshop recording.
- [ ] [Valeriia] Confirm Diogo is on the AI Shipping Labs Slack channel and added to the May sprint roster.

## Internal Context

### Persona

Undetermined - to assign once Diogo has selected a project and answered the questionnaire. Provisionally close to Sam (technical professional moving deeper into AI), since he has industrial engineering plus data-engineering experience and wants to add AI engineering on top.

See [personas.md](../personas.md) for full persona definitions.

### Background

Diogo's background is in industrial engineering with a data-science specialization. His first job was a traineeship at the EU in Brussels, where most of his time was actually data engineering rather than data science (organizations typically hire data scientists without first putting good data engineering in place). He moved to Copenhagen earlier this year and now works at the European Environment Agency on data integration across multiple projects, with the European Climate Risk Assessment as his main focus[^2].

He no longer codes most of the day - his role is closer to managing what needs to happen and coordinating with contractors. AI engineering is still very recent, with few people or contractors who can actually implement it, so he wants to test it himself first to understand the possibilities before he can manage or outsource such projects later[^2].

Email: diogovalentepcs@gmail.com[^2]

### Intake

#### Initial Input

Diogo joined AI Shipping Labs as part of the AI Engineering Buildcamp paid course (which includes free access to the community). He requested a clarification call to understand the course and the community before deciding what to commit to[^2].

#### Questions and Answers

Questionnaire not yet completed. Notes below come from the 2026-04-30 intake call with Valeriia[^2].

- How can the community be most helpful?

Three things, in order: assessing the feasibility of project ideas (so he can manage expectations - "can I do this in two weeks, three weeks?"); getting new project ideas and tools that he can adapt to his use case; and sharing his work back so it can be useful for other community members. He prefers a discussion-based format - someone he can ask "what do you think, would this take me long to do, is this feasible?"[^2].

- What is the ideal 6-8 week result?

A working, deployed project that is actively usable in his current job - "a usable tool that I'm actively using now at the work"[^2].

- Has the project been selected?

Not yet. Selecting the project itself is one of the things he wants help with[^2].

- How much time per week?

Roughly 5 to 10 hours per week building, outside the course content (with course time on top). He framed the realistic average as closer to 5 hours per week[^2].

- Long-term goals

Personal productivity, not promotion or job change. He started his current job two months ago and is not looking to move. He wants to understand AI engineering possibilities so he can eventually manage and outsource such projects effectively[^2].

#### Candidate project ideas

Diogo brought three candidate ideas to the call. Final pick is still open[^2]:

1. Scraping plus structured datasets. Scrape information that member states report to the EU (for example on climate policy) from the public web, build a structured dataset, and add an evaluation step on top so the dataset quality can be measured. He noted that the team already creates such datasets, but there is no efficient way to evaluate or test the results.
2. Data explorer / data fetcher. Many of the questions in his organization are "does this data exist somewhere?". Public data on topics like economic losses from extreme floods is held by national organizations but is hard to locate, and access varies (public, request-only, paid). The agent would help locate it and, if a request is needed, automatically file the request.
3. Multi-agent expert elicitation. Replicate expert engagements - for example, the multi-perspective discussions used to issue a climate assessment statement - as a multi-agent system.

#### Main blocker

Time to decide which of the three ideas is most feasible, most interesting, and best on time-versus-output. He explicitly does not have much time and wants the highest-value choice for the smallest time spend[^2].

### Meeting Notes

2026-04-30 - intake call with Valeriia[^2]:

- Introduction to AI Shipping Labs and the sprint format. Valeriia explained that the AI Engineering Buildcamp is a paid course and participants gain free access to the AI Shipping Labs paid community. Sprints provide accountability for people aiming to build projects or transition to AI engineering roles.
- Sprint structure. Weekly meetings where participants share progress and blockers. New members create personalized 6-week plans, prepared by Alexey based on questionnaire answers. Sprints are not strictly bounded by course topics.
- Next steps agreed in the call:
  - [Valeriia] Send the questionnaire to Diogo.
  - [Diogo] Complete the questionnaire to define goals and constraints.
  - [Alexey] Assess feasibility and prepare the 6-week plan.
  - [Valeriia] Communicate the plan and feedback back to Diogo.

### Internal Recommendations

Alexey's recommendations after reviewing Diogo's intake[^3]:

1. Same approach as for other course members. Diogo is a Buildcamp student, so the build pattern in the course (concept → tools → tests → monitoring → evolution) applies directly. He just needs a project pick and a step-by-step plan.

2. The blocker is choice paralysis. Pick the project for him to remove the blocker. Default pick: project #3 (multi-agent expert elicitation), reduced to a single agent. Reasoning:
   - All three projects are interesting and doable in 6 weeks.
   - Multi-agent makes everything more complex and tangled - drop the multi-agent framing and use a single agent regardless of which project he picks.
   - The data-explorer/fetcher option (project #2) is a fine alternative if Diogo strongly prefers it - it sounds slightly more interesting on paper. The first project ("end-to-end process to create and evaluate structured datasets") is also a real and useful information-extraction problem.

3. Conceptual exercise before code. The user-submits-a-request → what-happens → where-does-the-agent-go → what-does-it-do walk-through is the cheap step that defines the tools. Once that is written down, the implementation falls out as plain functions, and the agent's only job is choosing which function to call.

4. 10 hours per week of build time on top of course content is good. Diogo framed the realistic average as closer to 5 hours; the plan above is sized for 10 with the deliverables sized so a 5-hour week can drop a stretch and still ship the weekly milestone.

5. Deployment inspiration: the AI Shipping Labs first workshop (week of 2026-04-20) walked through deploying a Telepot agent to Render end-to-end. The recording is community-only - Valeriia can share the link.

6. Goal alignment is correct. Diogo wants personal productivity (a tool he uses at work), not a job change. The plan should hold to that - "do I use this tool weekly?" is the real success metric, not portfolio polish.

### Internal Action Items

- [ ] [Diogo] Complete the questionnaire so the plan has a clean intake on file.
- [ ] [Diogo] Confirm the project pick (default: expert-elicitation single-agent) by end of week 1.
- [ ] [Alexey] Send the written plan.
- [ ] [Alexey] Confirm Diogo can access the AI Shipping Labs workshop recording on Telepot deployment.
- [ ] [Valeriia] Confirm Diogo is on the AI Shipping Labs Slack channel and added to the May sprint roster.

### Sources

[^1]: [20260430_162055_AlexeyDTC_msg3795.md](../../../inbox/used/20260430_162055_AlexeyDTC_msg3795.md) - shared as plan number 12.
[^2]: [Diogo Valente Polónia's intake meeting notes (Google Doc)](https://docs.google.com/document/d/1uildbS9wgPuyHAeF2xnfzmztjHYbxwDjew6_FXtLouY/edit?usp=sharing)
[^3]: [20260502_175544_AlexeyDTC_msg3826_transcript.txt](../../../inbox/used/20260502_175544_AlexeyDTC_msg3826_transcript.txt)
