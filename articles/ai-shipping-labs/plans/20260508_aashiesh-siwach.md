---
title: "Plan: Aashiesh Siwach"
created: 2026-05-08
updated: 2026-05-09
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Aashiesh Siwach

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: ML engineer based in the UK with a Master's in Business Analytics from the University of Exeter. Has shipped a hybrid search and reranking pipeline, an archive research-paper retrieval pipeline, an AI text detection project, and a climate misinformation RAG tool during a university internship. Currently working as a retail assistant at Primark while looking for a full-time AI/ML role; already enrolled in the 7-day agents course (AI Hero)[^1][^2][^3].
- Goal for the next 6 weeks: complete AI Hero as the foundation, pick one project he genuinely wants to use himself, and ship it end to end with tests, monitoring, and evaluation. Aashiesh's existing climate misinformation work is a strong default starting point if he wants to continue in that area.
- Main gap to close: a concrete project he commits to and ships, plus the production-side skills (CI/CD, MLOps, experiment tracking, deployment to AWS / GitHub Actions / Google Cloud) that he has identified as the most-asked-for AI engineering job requirements.
- Weekly time commitment: not yet quantified - Aashiesh is between his full-time AI/ML job search and a retail role at Primark, so realistic hours need to be confirmed. Plan is sized as a typical 6-week sprint and can be adjusted once he confirms.
- Hard deadline he has set: needs a full-time AI/ML role by end of August or September 2026 - roughly four months from intake[^3].
- Why this plan is the right next step: Aashiesh already has the project pieces (RAG, hybrid search, fine-tuning, FastAPI, Streamlit). What is missing is one polished end-to-end demo that puts production engineering on top - exactly what employers in the AI engineering market are asking for. Picking the project himself is part of the exercise.

## Plan

## Focus

- Main focus: pick one project he wants to use himself, ship a simple end-to-end version, then layer in tests, monitoring, and evaluation.
- Supporting focus: complete AI Hero in parallel as the agent-building foundation.

## Timeline

Week 1:

- Start AI Hero from day 1: https://aishippinglabs.com/courses/aihero. Treat it as the agent-building foundation, not a side track.
- Use the project-idea brainstorming prompt below to come up with 5-10 candidate ideas based on his own friction, hobbies, work, and the ML/AI engineering work he has already done.
- Look at his existing projects (hybrid search + reranking, deployed retrieval API, internship work) and decide whether one of them is worth turning into the sprint project, or whether a fresh project is better.

Week 2:

- Run each candidate idea through the project fit-check prompt below. Pick one - ideally a problem he actually wants solved, with data he already has or can get easily.
- Write a one-paragraph project card: who the user is, what input the system takes, what it produces, and what "good enough" looks like.
- Find or prepare the dataset the project needs.
- Continue AI Hero.

Week 3:

- Build the simplest end-to-end version: input, processing, output. No tests, no monitoring, no evaluation yet - just a working pipeline that produces an answer he himself would use.
- Keep scope narrow enough that the first version actually runs by end of week.
- Continue AI Hero.

Week 4:

- Add tests: unit tests for the deterministic parts, judge-style tests for the LLM parts. Prefer to write the underlying logic as plain functions first, then wrap them in agent calls - that makes testing much simpler.
- Finish AI Hero if not already done.

Week 5:

- Add monitoring with Logfire (the lightest path) so failures and unusual outputs become visible as he uses the system.
- Build a small evaluation set (20-50 examples is plenty) and run an LLM-as-judge eval. Use what you learn to tune prompts, retrieval, or model choice.

Week 6:

- Polish the README so the problem, the architecture, the run instructions, and the evaluation results are clear.
- Deploy somewhere (Streamlit Community Cloud, a small Lambda, or a small VM) so the system is reachable, not just runnable on his laptop.
- Record a short walkthrough/demo and decide what the next iteration looks like.

## How to pick the project

The single most important criterion for the project is that it solves a real problem for a real person - even if that person is Aashiesh himself. A finished okay project beats an unfinished ambitious one.

Two prompts help with the picking. They are intended for ChatGPT or Claude (voice mode works much better than typing):

- Project-idea brainstorming prompt: https://gist.github.com/alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1 - the gist contains both prompts. Use the interview prompt if there is no concrete idea yet, and the fit-check prompt to validate one before committing weeks to it.

When picking, score candidates against four criteria and pick the highest total: genuine interest (will he stay engaged for several weeks), usefulness (does it solve a real problem), data availability (does he already have or can he easily get the data), and feasibility (can a usable version ship in 4-6 weeks).

Lean toward projects that naturally use multiple LLM tool calls, RAG over a real document set, or an agentic flow with a clear input and output. Avoid topics the course does not cover end to end (training/fine-tuning models, computer vision, self-hosting open-source LLMs, mobile apps).

A climate-related project is a strong default starting point. Aashiesh has already built a climate misinformation RAG pipeline at the University of Exeter and interviewed for a climate-data role in London - that domain knowledge is real and reusable[^3]. There are two community members working in or interested in climate (Diogo Valente Polónia at the European Environment Agency, plus another member - confirm with Valeriia); they are useful contacts for project framing, data sources, and feedback. Reach out via Slack or ask Valeriia for an introduction. Climate is a suggestion, not a constraint - if a different problem scores higher on the four criteria above, pick that.

## After this sprint - LLM Zoomcamp

After AI Hero, the natural next step is LLM Zoomcamp (re-recorded version starting in June, with five workshops mapped to the modules). Plan to bring a project into LLM Zoomcamp that you actually want to ship - the course homework arc is much easier to complete when it is producing something you care about. The 6-week sprint project here can become the LLM Zoomcamp project too if it is sized right.

## Project approach

A few principles that apply to whatever project Aashiesh picks:

- One project at a time. The 6-week bar is much easier to clear when nothing competes for attention.
- Frame the work as current state to target state. The weekly plan is the delta between where the project is now and where it should be in 6 weeks.
- Ship end to end early. A working simple version in week 3 is the anchor; tests, monitoring, and evaluation grow on top of it.
- Let evaluation follow business goals. The metrics that matter are problem-specific - "the system answers correctly", "the agent picks the right tool", "the output does not contradict the source data" - not generic AI benchmarks.
- Treat deployment, monitoring, and iteration as part of building, not separate phases. Real users (or himself as a user) generate the next list of issues to fix.

## Resources

- AI Hero course: https://aishippinglabs.com/courses/aihero
- Project-idea brainstorming prompts (gist): https://gist.github.com/alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1
- Logfire for monitoring once the simple version works.
- Community accountability channel (`#plan-sprints`).

## Deliverables

- A project card (one paragraph: problem, user, input, processing, output, success metric) by end of week 2.
- Simple end-to-end version of the project by end of week 3.
- Tests, monitoring, and evaluation in place by end of week 5.
- Deployed demo with a clean README and a short walkthrough by end of week 6.

## Accountability

- Weekly async update on what shipped, what is blocked, and the goal for the next week.
- Weekly check-ins land best on the same day each week so the cadence sticks.
- One project. Do not let a "next idea" pull attention until the chosen project is demoable.

## Next Steps

- [ ] [Aashiesh] Run the project-idea brainstorming prompt and produce 5-10 candidate ideas. The climate misinformation work is a starting point if no other idea wins out.
- [ ] [Aashiesh] Run the fit-check prompt on the top 1-2 candidates and pick one.
- [ ] [Aashiesh] Confirm a realistic weekly time commitment so the plan can be sized correctly.
- [ ] [Aashiesh] Continue AI Hero (the 7-day agents course) - already in progress.
- [ ] [Aashiesh] If picking a climate-adjacent project, ask Valeriia for an intro to the community members already working in that area.
- [ ] [Alexey] Send the written plan and the project-idea brainstorming prompt.
- [ ] [Valeriia] Connect Aashiesh with Diogo Valente Polónia (and the other climate-interested community member) once Aashiesh confirms he wants to continue in that area.

## Internal Context

## Persona

Alex - The Engineer Transitioning to AI. Aashiesh has machine learning engineering foundations and has already shipped retrieval and reranking pipelines; he is now looking to round those out into production-grade AI engineering work with agentic systems[^1]. This places him squarely in the Alex archetype - an engineer crossing into LLM and agent work from an existing ML/engineering base.

See [personas.md](../personas.md) for full persona definitions.

## Background

Aashiesh is an ML engineer transitioning to a production-ready AI Engineer role. He has built systems including a hybrid search and reranking pipeline and a deployed retrieval API, plus applied AI/NLP work during an internship. He wants to refine these into production-grade applications and build an agentic AI system end to end, and is using AI Shipping Labs sprints for accountability, architecture/deployment feedback, and consistent shipping[^1].

The intake call (2026-05-08, with Valeriia) added significant background detail[^3]:

- Currently in the UK; completed his Master's in Business Analytics at the University of Exeter in September 2024.
- Originally from India, with a Bachelor's in Business Administration. Worked in his father's manufacturing business, dropped out of computer science engineering due to personal troubles, picked up coding during COVID through a small business analytics course (Python, Tableau, basic ML).
- Tried to find data analysis / data science roles in India but was told repeatedly that age was a barrier - a final-round interview rejected him explicitly on that basis. One interviewer suggested European countries would not have the same age problem, which led him to apply for UK programmes.
- Did not get into a data science Master's but was admitted to a Business Analytics Master's, which he used to take optionals in machine learning and prompt engineering.
- Built a research-paper recommendation system using sentence transformers and cosine similarity during the ML coursework.
- Built an AI-text-detection project using chain-of-thought prompting during the prompt engineering course (ROC ~0.71).
- Did an AI/NLP internship at the University of Exeter on a climate misinformation detection tool. First attempted with fine-tuning of an existing fact-checking model (using OpenAI to relabel a dataset into a "football language" - red card / yellow card style); the supervisor was not satisfied with the result. After the three-month internship and a one-month return to India, he came back to the project as a volunteer and rebuilt it using RAG over a corpus of official climate documents, returning grounded answers with references in the same football language style.
- Currently working as a retail assistant at Primark while looking for a full-time AI/ML role.
- Hard deadline: full-time role by end of August or September 2026 (~four months from intake).
- Has already had one AI-related interview (a London climate company, data science role) - went through 2-3 rounds, was rejected because the company filled the role internally; feedback was otherwise positive.
- Open to both AI engineering and machine learning roles; happy to switch between them.
- Existing tooling familiarity: Streamlit and FastAPI.
- Currently doing the 7-day agents course (AI Hero) and aware of the upcoming LLM Zoomcamp re-recording. Posts on LinkedIn about his projects (most recent: a search retrieval pipeline).

See his interview file at [../interviews/aashiesh-siwach.md](../interviews/aashiesh-siwach.md) for more background.

## Intake

## Initial Input

Aashiesh's free-form input from the intake document[^1]:

> Hi Valeriia,
>
> Thanks for the warm welcome. I am really excited to join the community.
>
> My goal is to transition into a production-ready AI Engineer role, with a strong foundation in machine learning engineering, focusing on building LLM-based systems such as retrieval pipelines, RAG applications, and agent-based workflows.
>
> So far, I've built systems like a hybrid search and reranking pipeline and a deployed retrieval API, and I've also worked on applied AI/NLP problems during my internship, which gave me exposure to real-world use cases.
>
> I'm now looking to refine these into more production-grade applications and build an agentic AI system end-to-end.
>
> I'd love to use the community sprints to stay accountable, get feedback on architecture and deployment, and consistently ship practical AI products.
>
> Happy to jump on a short call to discuss this further.
>
> Thanks again!
> Ashish

## Questions and Answers

The intake document lists the following ten questions. As of 2026-05-08, Aashiesh has not yet filled in answers - the questions are recorded here verbatim so the structure stays comparable to other plans.

1. What do you hope to achieve with this plan in the next 6 to 8 weeks? You mentioned that your goal is to transition into a production-ready AI Engineer role. What should this plan help you with most: shipping a new agentic AI project, improving an existing RAG/retrieval project, strengthening production engineering skills, or preparing your portfolio for job applications? - (no answer provided)

2. If you had to choose one concrete outcome for the next 6 weeks, what should it be? You already have experience with hybrid search, reranking, a deployed retrieval API, and applied AI/NLP work. What would make the next 6 weeks successful: a production-grade RAG application, an end-to-end agentic AI system, a deployed demo, or a polished job-ready case study? - (no answer provided)

3. How much time can you realistically commit each week? The plan should match your actual schedule. How many hours per week can you consistently spend on building, testing, writing, and sharing progress? - (no answer provided)

4. What projects do you already have that could be refined into stronger portfolio pieces? You mentioned a hybrid search and reranking pipeline, a deployed retrieval API, and applied AI/NLP work from your internship. Which project should we build on first, and what is its current status? - (no answer provided)

5. What makes the project not yet "production-grade" in your view? What is missing right now: evaluation, deployment quality, monitoring, tests, CI/CD, logging, security, documentation, error handling, cost control, or cleaner architecture? - (no answer provided)

6. What kind of agentic AI system do you want to build end-to-end? You mentioned wanting to build an agentic AI system. What specific problem should it solve, who is the user, and what useful output should the system produce? - (no answer provided)

7. What is blocking you most right now from moving forward? You are not starting from zero, so the blocker may be choosing the right scope, making prototypes production-ready, getting architecture feedback, staying consistent, or positioning the work for AI Engineer roles. What is the main blocker for you? - (no answer provided)

8. What kind of feedback would be most useful during the sprint? You mentioned wanting feedback on architecture and deployment. What would help most: project scope review, architecture review, code review, API design feedback, deployment review, evaluation plan review, or portfolio/GitHub feedback? - (no answer provided)

9. What type of accountability would be most effective for you? You said you want to use community sprints to stay accountable and consistently ship practical AI products. What format would help you most: weekly deliverables, GitHub issues, demo-based milestones, async Slack updates, short reflections, or public build-in-progress updates? - (no answer provided)

10. What would make you feel that, at the end of the next 6 to 8 weeks, the plan was worthwhile? By the end of the plan, what result would feel meaningful: a shipped agentic AI system, a production-grade RAG app, stronger deployment confidence, a polished portfolio project, or clearer readiness for AI Engineer roles? - (no answer provided)

## Meeting Notes

Aashiesh and Valeriia held an intake call on 2026-05-08 (~25 minutes). Alexey was not on the call[^3].

Key points raised by Aashiesh during the call (in addition to the background notes above):

- Market research read: AI engineering job descriptions consistently ask for the ability to productionise a project using GitHub Actions / AWS / Google Cloud, CI/CD, MLOps tooling, and experiment tracking. He flagged this as the gap he most wants to close.
- He wants "proper direction" from the community so he does not waste time on things that are not industry-oriented. Direction is what he is asking for, not specific feedback on a finished project.
- Self-described as "very interested" in AI engineering after the climate RAG work.
- Wrote his Q&A answers in detail in the intake document and felt there was not much to add live.

Key things Valeriia surfaced during the call[^3]:

- Mentioned a community member working in the climate department of a European nation, with a use case around collecting unstructured climate-related PDFs from member states for retrieval - flagged as a possible future connection if Aashiesh continues in the climate space. (This is Diogo Valente Polónia at the EEA - see [his plan](20260502_diogo-valente-polonia.md) for context.)
- Walked Aashiesh through the new AI Shipping Labs platform (login via Slack/Gmail, lesson tracking) and confirmed he can already see the AI Hero modules.
- Explained that the LLM Zoomcamp content is being re-recorded with a workshop per module (workshop on 2026-05-11 is the kick-off), and that those workshops will be cut into the course.

Action items added by this call:

- [ ] [Aashiesh] Continue market research on AI engineering job descriptions to refine the production-skills focus.
- [ ] [Valeriia] Share the link to the AI Shipping Labs / DataTalks.Club workshop series so Aashiesh can attend the LLM Zoomcamp introduction workshop on 2026-05-11.
- [ ] [Valeriia] Follow up on the climate community connection if Aashiesh decides to continue in that area.

## Internal Recommendations

Alexey's recommendation after reviewing Aashiesh's input[^2]:

1. The intake is too thin to design the project for him. The follow-up answers have not come back, and from the initial input alone there is no specific problem to build against. Treat that as a feature of the exercise, not a blocker.

2. Have Aashiesh pick his own project. Real AI engineering experience starts with picking a problem - the same exercise students go through on the course. He chooses an area he wants to learn more about, brainstorms problems within it, and picks one.

3. Use the brainstorming gist as the tool for picking, not a one-off conversation. Send him the project-idea gist link directly. He runs the interview prompt to surface candidates, then the fit-check prompt to validate the top one or two before committing.

4. Plan structure: AI Hero first as the foundation, then a more complex project on top. Start with a simple end-to-end version, then add tests, monitoring, and evaluation in that order. That sequence mirrors the Buildcamp arc and is what turns a prototype into a portfolio-grade project.

5. Keep the recommendation short for him - a summary of how to pick a project plus the gist link is enough. Internal course material (the V2 capstone homework) does not need to land in the shareable plan; the principles distilled from it do.

Updates after reviewing the 2026-05-08 call notes[^4]:

6. Climate is a sensible default project area. Aashiesh has already done a climate misinformation RAG project at university and even interviewed at a London climate company. That domain knowledge is reusable, and the RAG-over-PDFs shape lines up well with the production-engineering skills he wants to add (deployment, evaluation, CI/CD). It is not the only option - if his brainstorming surfaces something he genuinely wants more, take that - but it is the best fallback.

7. Connect him with the community members working on climate. Diogo Valente Polónia at the EEA is the obvious one. There is also a second community member (Carmina, exact name to be confirmed with Valeriia) who works on climate projects. Both are useful contacts for project framing, possible data sources, and feedback. He should partner with them where it helps, not work in isolation.

8. He is doing well on AI Hero - he is already going through the 7-day agents course on his own initiative. Do not slow him down; that is the foundation in place.

9. Frame LLM Zoomcamp as the next step after AI Hero. He already plans to attend the introduction workshop on 2026-05-11. The 6-week sprint project should be designed so it can grow into the LLM Zoomcamp project rather than competing with it - one ship, not two.

10. Open question on dev skill level. From Aashiesh's messages alone it is hard to tell how strong his hands-on engineering is in practice. Treat the first week's project work as the signal and adjust scaffolding (more or less explicit guidance) accordingly.

## Internal Action Items

- [ ] [Alexey] Send Aashiesh the written plan plus the project-idea brainstorming gist link.
- [ ] [Valeriia] Confirm Aashiesh is on the AI Shipping Labs Slack channel and added to the May sprint roster.
- [ ] [Valeriia] Follow up with Aashiesh on the open Q&A items in the intake doc and on his weekly time commitment.
- [ ] [Valeriia] Confirm the second community member's name (Carmina or similar) so Aashiesh can be connected if he chooses the climate angle.
- [ ] [Valeriia] Send Aashiesh the link to the LLM Zoomcamp introduction workshop on 2026-05-11.

## Sources

[^1]: [Aashiesh Siwach's intake (Google Doc)](https://docs.google.com/document/d/1RRtifMVLX_isgrn-TbJAyMEObrZgQx0i/edit?usp=sharing&ouid=103720991008355605122&rtpof=true&sd=true), shared via [20260508_084825_AlexeyDTC_msg3954.md](../../../inbox/used/20260508_084825_AlexeyDTC_msg3954.md).
[^2]: [20260508_135759_AlexeyDTC_msg3970_transcript.txt](../../../inbox/used/20260508_135759_AlexeyDTC_msg3970_transcript.txt)
[^3]: [Aashiesh Siwach intake call notes, 2026-05-08 (Google Doc with Gemini summary and transcript)](https://docs.google.com/document/d/1IRMJ0DlZc7viLpX4ds3LQ_iVzKAoWPlmgqAToUpyTYE/edit?usp=drivesdk), shared via [20260509_112920_AlexeyDTC_msg3982.md](../../../inbox/used/20260509_112920_AlexeyDTC_msg3982.md).
[^4]: [20260509_113207_AlexeyDTC_msg3984_transcript.txt](../../../inbox/used/20260509_113207_AlexeyDTC_msg3984_transcript.txt) - Alexey's recommendations after reviewing the call notes.
