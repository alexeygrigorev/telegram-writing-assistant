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
- Goal for the next 6 weeks: break the existing plan into weekly milestones and ship a strong demo by the end of the sprint.
- Main gap to close: structure (weekly breakdown) and a coding-assistant workflow that keeps focus through 6-10 hours per week.
- Weekly time commitment: 6-10 hours per week, which is enough to finish a solid demo inside the 6-week sprint.
- Why this plan is the right next step: he does not need help inventing what to build - he needs a weekly cadence, the right tooling, and a few quick wins early on to keep momentum.

## Plan

### Focus

- Main focus: take the project Vishnu already described in the intake and turn it into a weekly sequence of small, shippable steps.
- Supporting focus: pick one coding assistant and use it consistently to maintain focus and offload routine work.
- Supporting focus: borrow the per-week structure (and the prompts) from the AI Engineering Buildcamp v2 capstone files so each week has a clear "what to do" template.

### Timeline

The project Vishnu has in mind can be built either as an agentic system or as a plain LLM call against the OpenAI or Anthropic SDK. Either is fine - the agentic flavour is not required.

Week 1:

- Pick a coding assistant and commit to it. Codex if Vishnu has a ChatGPT subscription; Claude Code if he is already using it. Any one of them is fine - the workflow matters more than the choice.
- Take the existing concrete plan from the intake and split it into 5-6 weekly goals. Each week should be small enough that it can plausibly be finished in 6-10 hours.
- Open the AI Engineering Buildcamp v2 capstone files (one per week) and use the per-week prompts as a starting template. They may not all be necessary because Vishnu already has a plan, but the structure and the prompts are useful as scaffolding.

Week 2:

- Build the first end-to-end version of the project. It should be simple - one input path, one output path, no agentic pieces yet.
- The goal for this week is a quick win: something that runs end-to-end, even if it is rough. Quick wins early are what keep motivation going across the rest of the sprint.

Week 3:

- Iterate on the first version. If the project will use RAG, add the search piece. If it will stay pure prompt, tighten the prompt and the data.
- Use the coding assistant aggressively here - let it handle boilerplate so Vishnu can stay focused on the parts that actually matter.

Week 4:

- Add the next layer planned for the project. If the plan calls for an agentic shape, this is the week to introduce it (tools, simple tool-calling loop). Otherwise keep building features on top of the LLM-only version.
- Cross-check progress against the original concrete plan and drop or defer anything that does not fit in the time left.

Week 5:

- Polish: data handling, prompts, error handling, simple monitoring.
- Start preparing a short README and a clear "what this does" description for the demo.

Week 6:

- Wrap up the project to a state where it can be demoed. Working deploy or running locally is fine; the bar is "someone can see it work."
- Record or write up the demo so it can be shared inside the community.

### Resources

- AI Engineering Buildcamp v2 capstone files (one per week) - use them as a structural template and copy the per-week prompts into Vishnu's own workflow when useful.
- Coding assistant of choice (Codex or Claude Code). If Vishnu has a ChatGPT subscription, Codex is the cheapest entry point. Free tiers should be avoided - hitting limits mid-session breaks the flow.
- OpenAI SDK or Anthropic SDK - either is enough for this project. No agent framework is required unless the project specifically calls for it.

### Deliverables

- A weekly breakdown of the existing concrete plan into 5-6 small, shippable goals.
- One project shipped end-to-end by week 6 with a short README and a runnable demo.
- A clear early-week win (week 2) so motivation stays through the rest of the sprint.

### Accountability

- Keep weekly effort in the 6-10 hour band so the 6-week plan stays finishable and consistent.
- Aim for one demoable project, not several parallel experiments.
- Use the coding assistant heavily; it doubles as a focus tool, not just a code generator.

### Next Steps

- [ ] [Vishnu] Pick a coding assistant (Codex or Claude Code) and confirm a paid plan that fits 6-10 hours per week.
- [ ] [Vishnu] Split the existing concrete plan from the intake into 5-6 weekly goals.
- [ ] [Vishnu] Ship a week-2 quick win: a rough end-to-end version of the project.
- [ ] [Alexey] Send the written plan plus links to the AI Engineering Buildcamp v2 capstone files for week-by-week prompts.

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

3. Reuse the structure of the AI Engineering Buildcamp v2 capstone files. Each week of the course has a capstone file that describes the process and includes prompts - copying those prompts into Vishnu's own workflow can speed him up. They are not strictly necessary because he already has a plan, but the per-week structure and the prompts are useful scaffolding.

4. 6-10 hours per week is a lot of time for a 5-6 week sprint. That is enough to build a solid demo by the end of the course, especially if Vishnu stays focused and uses an AI assistant aggressively.

5. Pick any coding assistant. Codex is a natural fit if he has a ChatGPT subscription; Claude Code is also fine if he already uses it. The point is to pick one and use it maximally - it helps with motivation as much as with productivity.

6. The goal for the early weeks is to land a few quick wins, so motivation carries through the rest of the sprint.

### Internal Action Items

- [ ] [Alexey] Send Vishnu the written plan and links to the AI Engineering Buildcamp v2 capstone files (one per week).
- [ ] [Valeriia] Confirm Vishnu's chosen coding assistant and the first weekly goal so the plan can be sanity-checked early.

### Sources

[^1]: [Google Doc](https://docs.google.com/document/d/1MLNJl3ku1ApQv5Nq9mJm9B3z_55Q2hyQcc2cHc4Qz5s/edit?usp=sharing) via [20260429_131353_AlexeyDTC_msg3733.md](../../../inbox/used/20260429_131353_AlexeyDTC_msg3733.md)
[^2]: [20260429_131714_AlexeyDTC_msg3735_transcript.txt](../../../inbox/used/20260429_131714_AlexeyDTC_msg3735_transcript.txt)
