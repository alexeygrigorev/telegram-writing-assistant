---
title: "Plan: Motasem Salem"
created: 2026-04-27
updated: 2026-04-27
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Motasem Salem

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: ML engineer with a software engineering background. Already deploys models to production and works with databases. Wants to use AI assistants to build end-to-end products as a full-stack developer.
- Goal for the next 6 weeks: pick one project, get a first working version of a full-stack site in place, then continue building it through an agent team using spec-driven development.
- Main gap to close: experience working with a coding agent and structuring a project so that spec-driven development with a team of agents works (clean tests on frontend, backend, end-to-end).
- Weekly time commitment: 10-15 hours per week, which is enough to ship a first working version inside the 6-week sprint.
- Why this plan is the right next step: he already knows what he wants to build and has the engineering skills, so the highest-use move is to give him structure - pick a coding agent, pick one project, learn the agent-team / spec-driven workflow, and execute.

## Plan

## Focus

- Main focus: ship one full-stack project end-to-end, using a coding agent throughout.
- Supporting focus: learn the agent-team / spec-driven development workflow from the AI Dev Tools Zoomcamp module 2 and the article on managing agent teams.
- Supporting focus: set up a project structure with proper frontend, backend, and end-to-end tests so spec-driven development with multiple agents can run cleanly on top.

## Timeline

Week 1:

- Pick a coding agent and a paid plan. Claude Code or Codex are both fine - the framework does not matter, the workflow does.
- Recommended sizing: not the cheapest plan, not the most expensive. For 15 hours/week, the $100 Claude Code or Codex plan is comfortable. Starting with the cheapest Codex plan and upgrading if it runs out is also reasonable. Free plans will not cut it - too much waiting.
- Pick exactly one project. Two projects is not needed and will dilute focus.
- Decide on a tech stack by talking to an agent (or even ChatGPT) about pros and cons. Ask the agent to first list the criteria it would use to choose, explain why each matters for this project, then recommend a stack against those criteria.

Week 2:

- Watch module 2 of the AI Dev Tools Zoomcamp: it covers building a small site with frontend, backend, and an OpenAPI layer between them, plus CI/CD.
- Read the article on managing agent teams (spec-driven development).
- Start the first version of the project: build the core functionality of the site as a single human-driven pass with the coding agent. The goal is to have a working frontend and backend that do the core thing, end to end.

Week 3:

- Once the core functionality is in place, set up a clean project structure that supports spec-driven development:
  - Tests on the frontend.
  - Tests on the backend.
  - At least a couple of end-to-end tests.
- These tests are the substrate that lets a team of agents work safely. Without them, spec-driven development does not hold up.

Week 4:

- Switch to the agent-team workflow. Use spec-driven development to add the next set of features instead of driving the agent step-by-step.
- Treat this as the first real test of the workflow on his own project, on top of the existing core functionality.

Week 5:

- Continue building features through the agent team. Tighten the test coverage and the spec format as he learns what works.
- If the chosen agent plan is running out of room, upgrade rather than waiting. Do not switch to a free plan.

Week 6:

- Finish the project to a state where it can be demoed and shared. A short README, a working deploy, and a clear "what this does" is enough.
- If anything remains unclear about the agent-team workflow, ask the coding agent to explain how each piece works - it is fine to read along and learn while it builds.

## Resources

- AI Dev Tools Zoomcamp - module 2: walk-through of frontend + backend + OpenAPI layer + CI/CD on a small site. Use this as the structural reference for the project.
- Article on managing agent teams (spec-driven development): pattern for breaking work into specs and running multiple agents on top of a tested project.
- Coding agent of choice (Claude Code, Codex, or similar): paid plan in the $100/mo range for 15 hrs/week of work, or the cheapest Codex plan as a starting point with a planned upgrade.
- ChatGPT or the coding agent itself for tech-stack selection conversations - cheaper than burning agent credits on stack debates.

## Deliverables

- One full-stack project shipped end-to-end, with frontend, backend, and an API layer.
- Frontend, backend, and end-to-end tests in place to support spec-driven development.
- A working agent-team workflow on this project, where features are added through specs rather than direct agent prompts.
- Short README/demo so the project can be shared.

## Accountability

- Keep effort at 10-15 hours/week so the 6-week plan stays finishable.
- Resist the urge to add a second project. One shipped end-to-end project is the goal.
- Do not get stuck on framework choice. Pick one (e.g. React on the frontend), commit, and move on.

## Next Steps

- [ ] [Motasem] Pick one project and a coding agent + plan.
- [ ] [Motasem] Watch module 2 of the AI Dev Tools Zoomcamp and read the article on managing agent teams.
- [ ] [Motasem] Build the first working version of the site (frontend + backend, core functionality only) before switching to spec-driven development.
- [ ] [Alexey] Send the written plan plus links to module 2 and the agent-team article.

## Internal Context

## Persona

Alex (The Engineer Transitioning to AI. He already has the engineering skills (software engineering background, currently deploys ML models to production, works with databases). The transition here is into using AI assistants to build end-to-end products as a full-stack developer, not into AI engineering itself) his stated focus is AI-assisted software development rather than building AI-native products[^2].

## Background

Motasem Salem is an ML engineer with a software engineering background. He deploys models to production and works with databases. His main interest is using AI to build end-to-end products that look like full-stack software development work. When asked whether he was also interested in AI-native products of the kind the community typically builds, he said yes, but his actual focus is on regular software development with AI assistants[^2].

The plan number in the inbox marks this as the 8th personalised plan in the current batch[^3].

## Intake

The intake is the Google Doc with Motasem's input collected ahead of this plan[^1]. The contents of the doc are not duplicated here.

## Internal Recommendations

Alexey's recommendation after reviewing Motasem's input[^4]:

1. He already knows what he wants to do. The job is to give him structure so 10-15 hours per week become productive.

2. Step one is picking a coding agent and committing to it. Claude Code, Codex, or anything similar - the choice does not matter much, the workflow does. Cursor's pricing is unclear. Claude Code and Codex have a $100/mo plan that fits ~15 hrs/week. Starting on the cheapest Codex plan and upgrading is also fine. Free plans should be avoided.

3. He has several full-stack project ideas (frontend + backend with an OpenAPI layer in between). Module 2 of the AI Dev Tools Zoomcamp shows exactly that pattern, including CI/CD, so it is a strong reference.

4. The article on managing agent teams (spec-driven development) is the second piece. He should try to implement this himself: first get the core of the site working, then keep building through a team of agents driven by specs.

5. For spec-driven development to work, the project needs proper test scaffolding: frontend tests, backend tests, end-to-end tests. The agent-team framework lays cleanly on top of that structure. Without the tests it falls apart.

6. He should pick one project, not two. Six weeks should be enough to get a first working version. The rest of the project can stretch beyond that.

7. Framework choice is secondary. React rather than Next.js is fine (Alexey himself does not know Next.js well and is not a JavaScript expert, so he would default to React. The general approach is to ask the agent to list the criteria it would use to choose a stack, justify why those criteria matter for this project, then pick. ChatGPT is enough for that conversation. No need to spend coding-agent budget on it. For his own projects Alexey defaults to Django because he already knows it) the same logic applies here, but the criteria-first conversation can override the default.

8. He can read along and ask the coding agents to explain how things work if he wants to understand the system, not just ship it.

## Internal Action Items

- [ ] [Alexey] Send Motasem the written plan plus the links to module 2 of the AI Dev Tools Zoomcamp and the agent-team article.
- [ ] [Valeriia] Confirm the project Motasem ends up choosing so we can sanity-check the scope against the 6-week sprint.

## Sources

[^1]: [Google Doc](https://docs.google.com/document/d/1CiMQn77AE7wtcId_qXSi7bVI0FMFOgJ4vKukeg1QUxo/edit?usp=sharing)
[^2]: [20260427_185609_AlexeyDTC_msg3711_transcript.txt](../../../inbox/used/20260427_185609_AlexeyDTC_msg3711_transcript.txt)
[^3]: [20260427_185529_AlexeyDTC_msg3707.md](../../../inbox/used/20260427_185529_AlexeyDTC_msg3707.md), [20260427_185617_AlexeyDTC_msg3713.md](../../../inbox/used/20260427_185617_AlexeyDTC_msg3713.md)
[^4]: [20260427_185554_AlexeyDTC_msg3709_transcript.txt](../../../inbox/used/20260427_185554_AlexeyDTC_msg3709_transcript.txt)
