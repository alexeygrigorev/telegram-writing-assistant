---
title: "Plan: Manjunath Yelipeta"
created: 2026-05-06
updated: 2026-05-06
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Manjunath Yelipeta

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: traditional ML engineer (CV/recommendation/classical ML) without LLM or agentic experience. Jobless for two months and is the sole bread-earner for his family, so the sprint has to lead to a shippable project that helps him land a job. He had a difficult prior role with unrealistic timelines and weak evaluation culture, so he is leaning away from AI-first roles toward AI Platform Engineer / MLOps Engineer / Applied AI Engineer titles, but admits the titles feel confusing.
- Goal for the next 6 weeks: ship a RAG system with comprehensive evaluation as a deployed application. Use the build to figure out which path - AI Engineer (build LLM systems) or AI Platform Engineer (build infrastructure for LLM systems) - actually fits how he wants to work. The role direction is a sprint output, not a precondition.
- Main gap to close: the entire LLM and agentic application stack - RAG, prompt and tool design, backend engineering beyond FastAPI/Docker, observability, deployment. The ML side (evaluation, failure-mode analysis) is strong and should be visible in the project from week 1.
- Weekly time commitment: 8-10 hours per week, extendable as the job search and family situation allow.
- Why this plan is the right next step: he has written and shipped traditional ML, so the engineering instinct is there - what is missing is hands-on experience with LLM applications. Shipping one well-evaluated, deployed RAG project closes that gap and produces the live link he asked for. The role question is best resolved by doing the work, not by reading more job descriptions.

## Plan

### Focus

- Main focus: ship a RAG system with comprehensive evaluation, deployed to a live URL, by end of week 6. The project is the portfolio piece for the job search and the testing ground for the role question.
- Supporting focus: do a small piece of role research in week 1 - 10 job descriptions for AI Platform Engineer / MLOps Engineer / AI Engineer, what responsibilities they list, what stack they expect. The point is to mirror that language in the CV and LinkedIn, not to commit to a title before the project is built.
- Supporting focus: AI Hero in parallel, only the modules that fill agent-fundamentals gaps. Skim, do not complete cover-to-cover.

### Timeline

Week 1:

- Concept and data design. Pick the dataset for the RAG system - something concrete and small enough to reason about (e.g., a documentation site, a paper collection in his domain, internal notes). Write a one-page note answering:
  - What questions should the system answer? Five real questions you want to ask.
  - What does "good" look like? Right passage retrieved, right answer, source cited - or stricter (full reference, multi-hop reasoning).
  - What is the failure mode you most care about avoiding? Hallucination is the obvious one; coming from your ML background, frame this as "an evaluation set that catches it before users do".
- Light role research. Pull 10 recent job descriptions for AI Platform Engineer, MLOps Engineer, and AI Engineer (use the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide) and standard job boards). Note responsibilities, stack, and seniority. The output is a one-paragraph summary of "the bar I am building toward" for the CV/LinkedIn - not a final career commitment.
- Pick one coding assistant and one paid plan. Avoid free tiers.
- Start AI Hero in the background. Cover the agent-loop and tool-calling sections only - skip anything you already understand.

Week 2:

- Build a minimal end-to-end RAG: ingestion → indexing → retrieval → answer with citations. Plain Python, FastAPI for the API, Docker for the container. No agentic framework yet - keep it as straight Python so you can see every step.
- Write the evaluation harness on day one of the build - five to ten golden questions with expected sources or expected answer fragments. Run it after every meaningful change. This is your strength and the part that should be obvious in the README.

Week 3:

- Deploy the v0 RAG somewhere with a public URL. Pick a low-friction target (Render, Fly.io, a small VM). Deployment is part of the build, not a final-week sprint. Why this early: the live link is what hiring committees click; everything after this iterates on a deployed thing rather than a localhost demo.
- Add observability. Pick one tool (Logfire, Langfuse, OpenTelemetry + a simple dashboard) and wire it in so every retrieval and every LLM call is traceable. This is also the kind of work AI Platform Engineer roles want to see.

Week 4:

- Iterate on the RAG itself based on the evaluation set. Prioritise the failure mode you flagged in week 1. Common moves: better chunking, a re-ranker, query rewriting, better passage selection. One change at a time, scored by the eval harness.
- Add one agent capability if the project genuinely benefits - e.g., a "follow-up question" loop or a tool that fetches an external reference. Skip if the RAG is already answering well; do not add an agent for the sake of it.

Week 5:

- Pick the single biggest weakness from week 4 and fix it. Either better evaluation coverage (multi-hop questions, robustness checks) or one production-shape concern: rate limiting, request logging, a minimal auth layer if the demo will be public.
- Write the README in the style hiring committees actually read: problem, dataset, architecture diagram, evaluation methodology, evaluation results, live URL, what you would do next.

Week 6:

- Wrap to demo state. Tag a release. Record a 3-5 minute demo video. Confirm the live URL is reachable from a fresh browser session. The README + live URL + repo is the artefact you point hiring committees at.
- Decide the role question now that you have built the thing. If the part you most enjoyed was "building the platform for the RAG to live in" (deployment, observability, infrastructure), the next sprint leans AI Platform / MLOps. If it was "making the RAG actually answer well" (retrieval, evaluation, prompts), the next sprint leans AI Engineer. Picking on evidence beats picking on theory.

### Project approach

- Strength first, gap second. Your evaluation and failure-mode analysis is the strongest signal in your background - put it in the project from day one. A RAG with a good eval harness reads as "this person actually knows what they are doing" to anyone hiring for AI Engineer or AI Platform roles.
- Functions before frameworks. Write the retrieval, the prompt assembly, and the answer step as plain functions you can call from a REPL. Wrap in FastAPI later. Skip agent frameworks until you have a reason for one.
- Deploy as part of building, not at the end. Live URL by end of week 3. Iterations after week 3 happen on the deployed thing.
- One coding assistant, paid plan, used for boilerplate - not as a black box. Conceptually work through the design first, then have the assistant implement; review every diff. The point is to understand each line, not to outsource the project.
- The role question is a sprint output. Manjunath's intake reads as "I do not yet know whether I want AI Engineer or AI Platform Engineer". The fastest way to find out is to build a project that touches both sides and notice which side felt energising.
- Plan can extend past 6 weeks if needed. The 6-week shape gets the v1 shipped; depth in observability/deployment/platform shape is genuinely a 12-week arc, and the sprint is the foundation.

### Resources

- AI Hero - free, useful for filling in agent fundamentals (agent loops, tool calling, evaluation). Skim, do not complete cover to cover.
- [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide) - browse recent AI Engineer / AI Platform / MLOps job listings to harvest the language and responsibilities to mirror in CV and LinkedIn. Also has the webinars walking through the role landscape.
- Logfire (or Langfuse / OpenTelemetry) - pick one for observability in week 3. The choice does not matter much; using one consistently does.
- A coding assistant of choice (Claude Code, Codex, or similar). Pick one and commit.

### Deliverables

- Concept doc (dataset + five real questions + failure mode you most care about) + 10 job descriptions analysed - by end of week 1.
- v0 RAG with evaluation harness running locally - by end of week 2.
- v0 RAG deployed to a public URL with observability wired in - by end of week 3.
- Iterated RAG with at least one substantial improvement scored by the eval harness - by end of week 4.
- Hardened version with one production-shape improvement and a hiring-ready README - by end of week 5.
- Tagged release, demo video, live URL, role-direction call - by end of week 6.

### Accountability

- Checklist-based milestones with brief weekly reflections (Manjunath's stated preference). Each week's deliverable is a checkbox; the reflection is two or three lines on what was learned and what was harder than expected.
- 8-10 hours per week. The plan is sized for the lower end so a heavier job-search week can drop a stretch goal rather than the milestone.
- Active in the AI Shipping Labs Slack - both asking and answering questions. Stakeholder communication is one of the gaps Manjunath named; using the community as a low-stakes practice ground for explaining technical work is the cheapest path to closing it.

### Next Steps

- [ ] [Manjunath] Write the concept doc (dataset + five questions + failure mode) and the 10-job-description summary by end of week 1.
- [ ] [Manjunath] Pick a coding assistant + paid plan; pick the deployment target.
- [ ] [Manjunath] Share weekly progress and reflections in the AI Shipping Labs Slack.
- [ ] [Alexey] Send the written plan and confirm AI Hero is the right entry point for agent fundamentals.
- [ ] [Valeriia] Confirm Manjunath is on the AI Shipping Labs Slack channel and added to the May sprint roster.

## Internal Context

### Persona

Alex - The Engineer Transitioning to AI (preliminary). Manjunath has shipped traditional ML (CV/recommendation/classical), with limited backend exposure (FastAPI, Docker only) and no LLM/agentic experience. He fits Alex more than Taylor - he is not a researcher or theoretical specialist - though his engineering depth is closer to "ML engineer" than to "full-stack/backend engineer". The plan treats the LLM/RAG/agentic side as the main gap.

See [personas.md](../personas.md) for full persona definitions.

### Background

Manjunath is a traditional ML engineer pivoting to AI/LLM work. He is unemployed since around early March 2026 and is the sole bread-earner for his family, which constrains both weekly time (8-10 hours) and the urgency of shipping a portfolio piece that helps with the job search.

He has had a difficult prior role - his director pushed for production AI without proper evaluation or failure-mode analysis - and is wary of AI-first roles where the same dynamics could repeat. He is leaning toward AI Platform Engineer / MLOps Engineer roles for stability, but has flagged that "AI Platform Engineer" feels confusing as a title. He is open to Applied AI Engineering[^1].

The role question is unresolved and the sprint is partly a way to figure it out.

### Intake

#### Initial Input

Manjunath's free-form input from the intake document[^1]:

> Hi Valeriia and Alexey,
>
> I worked as a traditional ml engineer, but now the industry is going with llm and agentic ai. As per my limited knowledge I feel agentic ai is more backend heavy, I am in dilemma whether I need to prepare for Ai first or for Ai support roles. In my experience, Ai first roles are a bit stressful as the expectations from mgmt will not match reality.
> My previous team had a terrible experience as my director wants everything to be build in no time without proper evaluations, finding failure modes etc. With that bad experience in my mind I am thinking to go for Ai support roles that will have access to internal systems of the company and it would be more secure. Alexey can correct me if I am wrong.
>
> I am jobless from past 2 months and have decided to give my sincere efforts on learning by building. This is my context and hoping to see on what my personalized plan looks like.
>
> Thanks
> Manjunath

He referenced the AI Shipping Labs blog article on AI-first vs AI-support vs ML jobs as the source of the categories he is using.

#### Questions and Answers

1. Which career path should this sprint help you explore? - "These titles seems a bit confusing to me. As a result of my past experience I am leaning more towards AI platform engineer and MLops Engineer roles."

2. What kind of role are you applying for or planning to apply for? - (no answer provided)

3. What kind of AI work do you want to avoid in your next role? - (no answer provided)

4. What kind of AI work would feel healthy and sustainable for you? - "I am thinking on improving my skills on maintaining AI infrastructure, evaluating LLM systems, supporting product teams but I am open to Applied AI engineering too."

5. What project would help you prove your judgment? - "I will go with A RAG system with comprehensive evaluation."

6. What part of agentic AI feels most uncomfortable right now? - "The following topics orchestration, databases, authentication, deployment, observability, or designing systems that gracefully handle failure seems a bit challenging to me."

7. What is your current backend and deployment baseline? - "I dont have any handson on above components. I have used FAstapi, docker for building apps."

8. What ML engineering strengths should your plan make visible? - "Evaluation and failure mode analysis. But I need to improve on my stake holder communication too."

9. What gaps do you need to close for the roles you are considering? - "All of the above :)."

10. What would make a project job-search ready for the roles you are considering? - "A live deployment link."

11. What is your realistic weekly availability during the job search? - "I dont have much options now as I am the only bread earner for my family so I can dedicate 8-10 hrs per week. And going forward can extend on it."

12. What accountability format would help you keep momentum without adding pressure? - "Check list based milestones and brief reflections on my learning."

13. What would make this 6-week plan worthwhile? - "All of the above mentioned are required. But a shipped project would make much sense for me. I have joined this course to be industry ready and grab a job."

### Meeting Notes

No intake call yet - input collected via the Google Doc[^1].

### Internal Recommendations

Alexey's recommendations after reviewing Manjunath's intake[^2]:

1. He is moving from traditional ML to AI/LLM. The AI Engineering Field Guide already has a learning path for ML Engineers crossing into AI - point him there as the starting reference.

2. AI Platform Engineer is a confusing title to chase before he has built one LLM application. Recommend a small piece of role research in week 1 (10 job descriptions, ChatGPT analysis, the AI Engineering Field Guide webinars) to make sure he understands what the role actually involves. The decision should fall out of building a project, not out of reading more.

3. There is no ready plan for AI Platform Engineer specifically (LLM platforms are a different beast than the data platforms Alexey has built). For AI Engineer there is a known plan; for AI Platform Engineer the plan has to be co-built. The sprint deliberately gives him a shape that touches both - a deployed RAG with observability is recognisable to both kinds of hiring committee.

4. The platform-shaped end state - "drop in an agent and the platform automatically wires monitoring, instrumentation, log collection" - would be a genuinely interesting community project to build over time. For this sprint, frame it as the natural next step after a single deployed RAG, not the v1.

5. Project mechanics: build simple end-to-end pieces first (RAG, then maybe a small agent), notice what is shared between them, and only then think about what a platform on top would look like. Without two or three concrete deployed projects, "build a platform" is design without input.

6. Authentication, deployment, observability, durable execution - all genuinely important for the platform direction. Treat them as a layered build: deploy the simplest thing first, add monitoring next, then evaluation, then everything else. Do not try to design the full platform before the first thing is live.

7. Tech choices do not matter much - FastAPI is fine. The decision that does matter is "pick a coding assistant and use it for implementation, but think conceptually first". Outsourcing the design of the platform is the failure mode; outsourcing typing is the goal.

8. The plan can extend past 6 weeks. The 6-week shape gets v1 deployed; the platform-direction stuff is a 12-week arc. Make this explicit so the sprint feels like a foundation, not the whole picture.

9. Stakeholder communication is a flagged gap. The Slack channel and weekly reflections cover this naturally; no separate workstream needed.

### Internal Action Items

- [ ] [Alexey] Send Manjunath the written plan.
- [ ] [Alexey] Confirm AI Hero is the right entry point for agent fundamentals.
- [ ] [Valeriia] Confirm Manjunath is on the AI Shipping Labs Slack channel and added to the May sprint roster.

### Sources

[^1]: [Manjunath Yelipeta's intake (Google Doc)](https://docs.google.com/document/d/1ZpbzJzAmL9t7FcGlcLi8gIo-k5XiXwpAxzNj7kdoxNc/edit?usp=sharing), shared via [20260506_174247_AlexeyDTC_msg3872.md](../../../inbox/used/20260506_174247_AlexeyDTC_msg3872.md).
[^2]: [20260506_195055_AlexeyDTC_msg3878_transcript.txt](../../../inbox/used/20260506_195055_AlexeyDTC_msg3878_transcript.txt) - Alexey's recommendations after reading the Q&A.
