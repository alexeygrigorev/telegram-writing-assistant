---
title: "Plan: Dianne Bronola"
created: 2026-05-02
updated: 2026-05-02
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Dianne Bronola

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: Dianne is an iOS engineer trying to pivot to data-heavy / AI-focused roles. She is on the AI Engineering Buildcamp and wants to recreate the DE Zoomcamp experience (project-based, code-along, active community). She has a capstone idea - a Learning Companion Agent for knowledge retention, interview prep, and code review - but no implementation yet.
- Goal for the next 6 weeks: ship a working first version of the Learning Companion Agent as the Buildcamp capstone, sized so she finishes the course and the project together.
- Main gap to close: turning the capstone idea into a concrete data structure and a manual workflow before automating it with an agent. The FOMO blocker ("too many possible directions") gets resolved by committing to one project and one data structure for the sprint.
- Weekly time commitment: 10-15 hours per week.
- Why this plan is the right next step: the capstone pick is hers, she has a clear longer-term arc (internal AI tool in 3 months, AI engineering role in 12 months), and the build pattern - design the data structure first, do the workflow manually, then automate - matches her engineering background and avoids the typical "agent first, structure later" mistake.

## Plan

## Focus

- Main focus: design the Learning Companion Agent end to end - what knowledge it stores, how it surfaces it for retention, how it asks interview questions, how it reviews code. Ship a first version as the Buildcamp capstone.
- Supporting focus: do the workflow manually first. Build the data structure and process a few real learning sessions by hand before introducing an agent. The agent only enters once the manual process is clear.
- Supporting focus: keep the focus on the capstone. The internal AI tool at her company is parked behind the capstone for now - that is a 3-month goal, not a 6-week one.

## Timeline

Week 1:

- Conceptual design before any code. Two questions to answer in writing:
  - What data structure does the Learning Companion hold? (Notes, code snippets, interview questions, review feedback - what fields, what relationships, what tags.)
  - How would Dianne want to receive this data herself? (Daily review prompt? Spaced repetition? Search-on-demand? A "what did I learn last week" digest?)
- Look at Obsidian as a reference for how a knowledge base for personal learning can be shaped. The relevant question is not "should I use Obsidian" - it is "what does a working personal knowledge tool look like, and what would the agent layer add on top of it?"
- Pick one coding assistant (Claude Code, Codex, or similar) for boilerplate. Avoid free tiers.

Week 2:

- Build the data structure. A simple schema is fine - Markdown files with frontmatter, or a small SQLite store, or whatever fits. The point is that you can write to it, query it, and read it back.
- Run the workflow manually. Take three or four real learning sessions from the Buildcamp this week and feed them into the structure by hand. Note which steps feel tedious - those are the ones the agent should automate.

Week 3:

- Add the first agent capability. Pick the manual step that felt most tedious and automate it. Common candidates: extracting key concepts from a session, generating spaced-repetition prompts, suggesting interview questions based on a topic.
- Keep it simple - one tool, one prompt, called from a CLI or a small UI. No multi-agent orchestration.

Week 4:

- Add the second agent capability. The natural one for this project is the code review feedback loop - paste a snippet, get a review with reference to material she has already studied.
- Run the agent on a real piece of code from her current work or a Buildcamp exercise. Compare the output to what she would have written manually.

Week 5:

- Iterate based on actual use. Whatever the first weeks of using the tool surface (prompts that under-deliver, missing data fields, a step the agent gets wrong) is the priority for this week.
- Add a small UI if it would make daily use realistic - even a Streamlit page is enough.

Week 6:

- Wrap to a state that can be demoed at the sprint and submitted as the Buildcamp capstone. README that explains the data structure, the manual workflow, and what the agent automates.
- Decide what the next iteration looks like - more agent capabilities, deeper integration with course materials, or moving on to the internal-AI-tool design once she has more exposure to her team's problems.

## Project approach

- Manual first, automation second. The data structure and the workflow live in the design step. The agent is a wrapper that automates a manual process you already understand. Trying to design the agent before you understand the manual workflow is the most common way these projects stall.
- One project at a time. The capstone is the one project. The internal AI tool at her company is a 3-month goal and is parked until she has more exposure to her team's problems.
- Address FOMO by committing. The "too many possible directions" blocker does not get solved by reading more - it gets solved by picking one and shipping. The plan won't fully eliminate it. Consistent weekly progress on one project is what dampens it.
- Use the active community. The DE Zoomcamp experience Dianne wants to recreate ("someone is always there to answer questions") is what AI Shipping Labs Slack is for. Asking questions there - and answering them once she is past a step - is the structural equivalent.
- Keep the longer arc visible. Capstone in 6 weeks, internal AI tool in 3 months, AI-heavy engineering role in 12 months. The capstone is the foundation that makes the next two possible.

## Resources

- AI Engineering Buildcamp - already enrolled. The course modules are the primary reference for the build.
- Obsidian - reference for how a personal knowledge tool can be shaped. The reading is "what does Obsidian's data model look like, and what would an agent on top of it do?", not "use Obsidian as the storage layer". Worth a couple of hours, no more.
- AI Shipping Labs Slack - the active community substitute for the DE Zoomcamp experience Dianne specifically named.
- Coding assistant of choice (Claude Code or Codex). Pick one and commit.

## Deliverables

- Concept doc (data structure + how she wants to receive the data) - by end of week 1.
- Data structure built, workflow run manually on three or four real sessions - by end of week 2.
- First agent capability automating the most tedious manual step - by end of week 3.
- Second agent capability (code review or similar) - by end of week 4.
- Iterated version with prompts and data fields tightened from real use - by end of week 5.
- Capstone-ready demo, README, and submission - by end of week 6.

## Accountability

- Weekly check-in: what shipped, what is blocked, what is the goal for the next week. Dianne named "weekly progress and deliverables" as the format that works for her.
- 10-15 hours per week. The plan is sized for the lower end so a busy week can drop a stretch goal rather than the milestone.
- One project until it ships. The Learning Companion Agent is the only project. The internal AI tool at her company waits until after the capstone.
- Active in the AI Shipping Labs Slack - both asking questions and answering others' questions. This is the part that recreates the DE Zoomcamp experience.

## Longer arc

- 3-month goal: scope an internal AI tool at her company, once she has more exposure to her team's problems and the data + sponsorship constraints.
- 12-month goal: an AI-heavy engineering role. The capstone plus the internal-tool work plus a clearly-told portfolio is the path.

## Next Steps

- [ ] [Dianne] Write the concept doc (data structure + how she wants to receive the data) by end of week 1.
- [ ] [Dianne] Build the data structure and run the workflow manually on three or four real sessions by end of week 2.
- [ ] [Dianne] Pick a coding assistant (Claude Code or Codex) and confirm a paid plan that fits 10-15 hours per week.
- [ ] [Dianne] Share weekly progress in the AI Shipping Labs Slack.
- [ ] [Alexey] Send the written plan.
- [ ] [Valeriia] Confirm Dianne is on the AI Shipping Labs Slack channel and added to the May sprint roster.

## Internal Context

## Persona

Alex - The Engineer Transitioning to AI (preliminary, to confirm). Dianne is an iOS engineer with a platform-engineering background trying to move into a data-heavier / AI-focused role. She has gotten interviews but is gated by project evidence, interview readiness, and confidence. That maps to Alex.

See [personas.md](../personas.md) for full persona definitions.

## Background

Dianne is an iOS engineer with a background in platform engineering for mobile and web frameworks. She has been trying for years to move into a more data-heavy software engineering role but keeps running into the same wall: she either does not meet the requirements, or the available roles come with a pay cut. She has been typecast as a frontend/mobile engineer and is actively trying to change that narrative[^2][^3].

She specifically named the Data Engineering Zoomcamp as the experience she wants to recreate - project-based, code-along, with an active community where someone is always available to answer questions[^2].

## Intake

## Initial Input

Hi Val! I hope it's not too late. I'm still finding my rhythm with the course schedule[^3].

I'm looking for structure, accountability, and fun! My main goal is to start building in the LLM space, specifically with RAGs and agents[^3].

I'm an iOS engineer with a background in platform engineering for mobile and web frameworks[^3].

For years, I've been trying to move into a more data-heavy software engineering role, but I keep running into the same wall. I either don't meet the requirements, or the available roles come with a pay cut[^3].

Topics I'm most interested in: how to scope and pitch an internal AI tool, and how to build a portfolio that shifts how people perceive you. I've been typecast as a frontend/mobile engineer, and I'm actively trying to change that narrative[^3].

## Questions and Answers

1. What do you hope to achieve with this plan in the next 6 to 8 weeks?

At the minimum, finish the course and the projects. She would like to build the skills to build an AI tool for her team. Ideally she would have that project as her capstone, but the data is internal to her company and AI APIs need higher management sponsorship[^2].

2. If you had to choose one concrete outcome for the next 6 weeks, what should it be?

Finishing the capstone is enough for now. After 6 weeks, she thinks she will have the idea and confidence on what to build for her team[^2].

3. How much time can you realistically commit each week over the next 6 to 8 weeks?

10-15 hours a week[^2].

4. What kind of LLM project would feel most useful or exciting to build?

No answer provided in the questionnaire[^2].

5. Are there any internal AI tool ideas you already have in mind?

Not yet - she joined her current team only a few months ago and does not have enough exposure to the problems yet. She thinks this will be a goal in 3 months and prefers to focus on the capstone for now[^2].

6. What would make an internal AI tool pitch credible in your company context?

See answer 5 - parked behind the capstone project for now[^2].

7. What part of the transition into more data-heavy or AI-focused engineering feels hardest right now?

She framed it as her own effort and pickiness - at the time she did not want to move companies, so the available roles were limited. She has had two interviews since. The biggest concrete gaps: project evidence, interview readiness, and confidence[^2].

8. What kind of accountability would be most effective for you?

Weekly progress and deliverables[^2].

9. What would make the process feel fun for you?

When she said accountability, structure, and fun, she was describing her experience with the Data Engineering Zoomcamp - one of the best free courses she has taken. The format is project-based with a code-along teaching style, which is how things stick for her. What made it especially great was the active community: someone was always there to answer questions when she was stuck, and once she finished an assignment, she could turn around and help others who were just starting[^2].

10. What is blocking you most right now from moving forward?

Probably FOMO with AI - too much noise. It is not that she is not moving forward, but she feels there are too many possible directions[^2].

11. What would make you feel that, at the end of the next 6 to 8 weeks, the plan was worthwhile?

For the 6-8 weeks, she will focus on her capstone project. She wants to build a Learning Companion Agent - something that would help her retain her knowledge, start adding interview questions, review her code with, etc. She is still brainstorming the features but the main goal is to make sure she retains all the knowledge she is learning while building. AI tool within her company is a 3-month goal. AI-heavy engineering position is a 12-month goal[^2].

## Meeting Notes

No intake call yet - input collected via the Google Doc[^2] and Dianne's initial reply to Valeriia's outreach[^3].

## Internal Recommendations

Alexey's recommendations after reviewing Dianne's intake[^4]:

1. She is a Buildcamp student, so the build pattern in the course applies directly. Same approach as for other course members - portfolio help, internal-tool help, capstone shipped in 6 weeks.

2. The Learning Companion Agent is a strong capstone pick. It is conceptually similar to the Telegram writing assistant (a personal tool that captures inputs, structures them, and surfaces them later) - same shape, different content domain.

3. The build pattern: design the data structure first, do the workflow manually, then automate. This is the part to highlight. Dianne's instinct will be to think about the agent first. She should think about the data and the manual workflow first. Once she understands how she would do it manually, the agent's job becomes mechanical.

4. Obsidian is a useful reference for what a personal knowledge tool can look like. Worth a few hours of looking at it - the question is not "use Obsidian" but "what does this data model look like, and what would an agent on top of it add?"

5. Conceptual exercise to push hard:
   - What data structure does she see? (Notes, snippets, questions, fields, tags, relationships.)
   - How would she want to receive the data herself? (Daily prompt, spaced repetition, search-on-demand, weekly digest.)
   - These two questions are the core of the design step. Everything else flows from them.

6. The FOMO blocker ("too many possible directions") will not be solved by a plan alone. Committing to one project for the sprint and shipping weekly is the only thing that reliably dampens it. The plan should make this explicit so she doesn't read the lack of FOMO-elimination as a plan failure.

7. 15 hours per week is a strong fit. Internal AI tool stays parked behind the capstone for now (her own framing - 3-month goal, not 6-week one). AI-heavy engineering role is the 12-month frame.

## Internal Action Items

- [ ] [Alexey] Send Dianne the written plan.
- [ ] [Valeriia] Confirm Dianne is on the AI Shipping Labs Slack channel and added to the May sprint roster.

## Sources

[^1]: [20260501_085705_AlexeyDTC_msg3818.md](../../../inbox/used/20260501_085705_AlexeyDTC_msg3818.md) - shared as plan number 13.
[^2]: [Dianne Bronola's intake (Google Doc)](https://docs.google.com/document/d/1M2UgXpocJiZq2rMjcI-7O6sN9f2ov4U3BizyHm1axoU/edit?usp=sharing)
[^3]: [20260430_162513_valeriia_kuka_msg3798.md](../../../inbox/used/20260430_162513_valeriia_kuka_msg3798.md) - Dianne's initial response to Valeriia's outreach.
[^4]: [20260502_175908_AlexeyDTC_msg3827_transcript.txt](../../../inbox/used/20260502_175908_AlexeyDTC_msg3827_transcript.txt)
