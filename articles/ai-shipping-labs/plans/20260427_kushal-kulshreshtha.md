---
title: "Plan: Kushal Kulshreshtha"
created: 2026-04-27
updated: 2026-04-27
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Kushal Kulshreshtha

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: an engineer who wants to move into AI engineering and is targeting roles that fit his location preferences (likely Europe-based or relocation/remote-friendly companies).
- Goal for the next 6 weeks: ship one end-to-end AI project aligned with the kind of company and domain he wants to work in next, with monitoring included.
- Main gap to close: a portfolio project that points at concrete employer-relevant problems instead of generic exercises.
- Weekly time commitment: not explicitly stated yet; the plan is sized as a tight 6-week sprint.
- Why this plan is the right next step: as an engineer he already has the core skills; the highest-leverage move is to anchor his project work to specific target companies and domains rather than building in the abstract.

## Plan

### Focus

- Main focus: pick one end-to-end AI project tied to a specific target company/domain and ship it within the 6-week sprint.
- Supporting focus: run AI Hero in parallel as a fast overview of how to build agents.
- Supporting focus: add monitoring with Logfire so the project has a visible engineering signal beyond a working demo.

### Timeline

Week 1:

- Filter for companies that fit (Europe-based, willing to relocate, remote-friendly, or similar criteria) and pick a shortlist.
- From that shortlist, pick the most interesting domain that several companies share.
- Read the tech blogs of the shortlisted companies and a few similar ones in the same domain.
- Start AI Hero from day 1 alongside this research.

Week 2:

- From the tech-blog reading, write down about 10 typical problems these companies are solving with agents, RAG, and similar patterns.
- Pick 1 problem (2 only if it is realistic) that is genuinely interesting and clearly relevant to the target roles.
- Prepare or find the data needed for that problem.
- Continue AI Hero.

Week 3:

- Build the first agent end-to-end for the chosen problem: input, processing, output.
- Keep the scope narrow enough that there is something working by the end of the week.
- Continue AI Hero.

Week 4:

- Add monitoring with Logfire to the project.
- Use AI Hero only for the concept that monitoring is needed; keep the actual implementation simple with Logfire.
- Finish the remaining AI Hero material if not already done.

Week 5:

- Add the agentic part and any other course-level pieces (RAG, evaluation, etc.) so the project covers what is taught in the course end to end.
- Tighten the data flow and fix the biggest weaknesses.

Week 6:

- Polish the project, write a short README, and prepare a demo.
- If time clearly allows, start scoping a second project; otherwise stay focused on finishing one strong project rather than two half-finished ones.

### Resources

- AI Hero course: https://dev.aishippinglabs.com/courses/aihero[^3] - fast overview of how to build agents; use it for the concepts, not for heavy monitoring.
- Logfire - simpler monitoring tool to attach to the project after the first agent works.
- Tech blogs of target companies and similar companies in the chosen domain - source for the list of typical problems.
- Project-idea brainstorming prompt: https://gist.github.com/alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1
- Community accountability channel (`#plan-sprints`): https://app.slack.com/client/T0AFSRP234M/C0AUQBSP4ER

### Deliverables

- Shortlist of target companies plus the chosen domain.
- List of about 10 typical problems those companies solve with AI/agents/RAG.
- One end-to-end AI project addressing one of those problems, with Logfire monitoring attached.
- Short README/demo so the project can be shared with the community and used in job applications.

### Accountability

- Cap weekly effort at a realistic number of hours so the 6-week plan is actually finishable.
- Weekly async update on what moved from research to artifact.
- Aim for one project shipped by the end of the 6 weeks; treat a second project as a stretch goal, not a baseline.

### Next Steps

- [ ] [Kushal] Pick the company filters (e.g. Europe, relocation, remote) and produce a shortlist.
- [ ] [Kushal] From that shortlist, pick the domain and write down about 10 typical problems they solve.
- [ ] [Kushal] Start AI Hero in parallel with the company/domain research.
- [ ] [Alexey] Send the written plan and the project-idea brainstorming prompt.

## Internal Context

### Persona

Alex - The Engineer Transitioning to AI. Already has engineering skills; the gap is AI-specific project experience and a portfolio that maps to the kind of role he is looking for.

### Background

Kushal is an engineer who wants to move into AI engineering. Alexey's read from the intake is that he is currently not in Europe and would like to work there, though Alexey was not fully sure about this and noted that the recommendation works either way. Valeriia had already shared a learning path with him before this plan was drafted.

### Intake

The intake is the Google Doc shared by Valeriia, which is meeting notes from the Kushal/Valeriia call on 2026-04-27 at 14:02 CEST[^1]. The contents of the doc are not duplicated here.

### Meeting Notes

#### Intake Call with Valeriia (Apr 27, 2026)

40-minute call between Kushal and Valeriia. Notes captured in the shared Google Doc[^1].

### Internal Recommendations

Alexey's recommendation after reviewing Kushal's input[^2]:

1. Focus on projects, but choose them based on the kind of job Kushal wants:
   - Filter companies first (e.g. Europe-based, willing to relocate, remote-friendly).
   - From the shortlist, pick the most interesting domain.
   - Read the tech blogs of those companies and similar companies in the domain.
   - Identify about 10 typical problems they solve with agents, RAG, and similar patterns.
   - Pick 1-2 of those problems and implement them end-to-end with all the pieces taught in the course (agents, etc.).

2. If Kushal is on the course, he should follow AI Hero PID for monitoring. AI Hero touches monitoring, but Alexey would recommend something simpler in practice: use AI Hero just to get the concept that monitoring is needed, then plug Logfire into the actual project.

3. Concrete sequence: study problems → pick a problem he himself wants to solve → prepare or find the data → build the first agent → add monitoring with Logfire.

4. In parallel, go through the AI Hero course - it should not take much time and gives a quick overview of how to build agents.

5. As an engineer, Kushal already has the core skills, and Valeriia has already shared a learning path, so the focus is on execution: pick a few portfolio-relevant projects and work on them.

6. Be realistic about scope. Over the next 6-week sprint, one finished project is a solid outcome; two projects is a stretch goal but should not push him into doing both half-way.

### Internal Action Items

- [ ] [Alexey] Send Kushal the written plan and the project-idea brainstorming prompt.
- [ ] [Alexey] Confirm whether Kushal is enrolled in the course; if yes, point him at AI Hero PID specifically.
- [ ] [Kushal] Share the company shortlist and chosen domain so the project scope can be reviewed before he starts building.

### Sources

[^1]: [Google Doc](https://docs.google.com/document/d/1UWS00jLXlLXM9GmNyO-WKIopiGYlyjf2gOzWQN7NLVg/edit?usp=sharing)
[^2]: [20260427_141109_AlexeyDTC_msg3699_transcript.txt](../../../inbox/used/20260427_141109_AlexeyDTC_msg3699_transcript.txt)
[^3]: [20260427_140659_AlexeyDTC_msg3697.md](../../../inbox/used/20260427_140659_AlexeyDTC_msg3697.md), [20260427_141140_AlexeyDTC_msg3701.md](../../../inbox/used/20260427_141140_AlexeyDTC_msg3701.md)
