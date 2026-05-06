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
- Goal for the next 6 weeks: build two small deployed LLM projects (a RAG, then a small agent), then start a v0.0.1 deployment platform that makes shipping the next agent trivial. The two projects are the raw material for the platform - by building them you see what is common, and that commonality becomes the platform's first cut. The platform deliberately ships with no monitoring and no evaluation in v0.0.1; those layers are added gradually after week 6.
- Main gap to close: the entire LLM and agentic application stack - RAG, prompt and tool design, backend engineering beyond FastAPI/Docker, deployment. Observability and evaluation are deferred on purpose so the v0.0.1 platform stays simple enough to actually ship.
- Weekly time commitment: 8-10 hours per week, extendable as the job search and family situation allow. The 6-week shape is explicitly a foundation, not the whole picture - the platform direction is a 12-week-plus arc.
- Why this plan is the right next step: he is leaning toward AI Platform Engineer but has not yet built one LLM application. The fastest way to test whether the platform direction actually fits is to build two simple things, notice what is shared, and start abstracting. That also produces the deployed live URLs hiring committees want to see, even if the platform itself is a v0.0.1.

## Plan

### Focus

- Main focus: build a small RAG, then a small agent, then a v0.0.1 deployment platform that makes shipping the next agent trivial. The platform is the 6-week deliverable; the two projects are scaffolding that lets you see what the platform should actually do.
- Supporting focus: in week 1, do role research - pull 10 AI Platform Engineer / MLOps / AI Engineer job descriptions, ask ChatGPT/Claude to summarise responsibilities, watch the relevant webinars in the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide). "AI Platform Engineer" is a confusing title to chase before understanding what the role really involves.
- Supporting focus: AI Hero core course as the entry point for agent fundamentals (agent loops, tool calling). Several of its homework projects can also serve as the seed projects you deploy in weeks 2-3.

### Timeline

Week 1:

- Role research. Pull 10 recent job descriptions for AI Platform Engineer, MLOps Engineer, and AI Engineer (job boards + the field guide). Ask ChatGPT/Claude to summarise responsibilities and stack. Watch the role webinars in the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide). Output: a one-paragraph note on what "AI Platform Engineer" actually means in current listings - is it what you thought it was?
- Pick the first project (the RAG). Keep it small: a documentation site, a paper collection, internal notes - something with five real questions you would actually want to ask. Sketch the architecture on paper before any code.
- Pick one coding assistant and one paid plan. Avoid free tiers.
- Start AI Hero core course in the background. Cover the agent-loop and tool-calling modules - they are the foundation for the second project in week 3.

Week 2:

- Build and deploy the first project (the RAG). Plain Python end to end - ingestion → indexing → retrieval → answer with citations. FastAPI for the API, Docker for the container. No agent framework yet. Push to a low-friction target (Render, Fly.io, a small VM) so the live URL is up by end of week 2. The shape that matters here is "deployed thing", not "polished thing" - skip evaluation harnesses and observability for now; they come later.

Week 3:

- Build and deploy the second project (a small agent). Take one of the AI Hero homework projects or one of the webinar projects from the field guide as the seed - do not invent from scratch. The point is to have a second deployed thing whose deployment story you can compare to the RAG, not to invent a new product. Push it live by end of week 3.

Week 4:

- Compare the two deployed projects. How are they packaged? What config do they need? How do they get a live URL? What runtime do they expect? Write a one-page note on the shared shape - that note is the seed of the platform.
- Sketch the v0.0.1 platform on paper before any code: the input contract (what does an agent author hand the platform?), the deployment path (what does the platform do with it?), the output (live URL, nothing else). No monitoring, no evaluation, no auth. Naming what is out of scope is as important as naming what is in.

Week 5:

- Build the v0.0.1 platform skeleton. Goal: a single deployment path - drop in a new agent (single repo or single config) and the platform deploys it to a live URL. Re-deploy the first project (the RAG) through this path. If the RAG comes up via the platform, the skeleton is real.

Week 6:

- Re-deploy the second project (the agent) through the same platform path. Two projects coming up via one path is the v0.0.1 acceptance bar.
- Write the post-week-6 roadmap: monitoring, log aggregation, automatic instrumentation, evaluation hooks, durable execution, auth - in the order you would add them. Sketch only, do not build.
- Decide the role question now that you have built the thing. If the platform-shaped work felt energising, the next sprint leans AI Platform / MLOps and the post-week-6 roadmap is your next 6-week plan. If the project work itself felt better than the platform around it, the direction shifts toward AI Engineer.

### Project approach

- Two small things, then a platform - in that order. The two projects exist to surface what the platform should actually do. Skipping straight to "design the platform" is design without input; this is the failure mode to avoid.
- Strip ruthlessly for v0.0.1. No monitoring, no evaluation, no auth in v0.0.1. Adding them later is straightforward; trying to add them now will mean nothing ships. This is deliberate sequencing, not laziness - the layered build is the whole point.
- Functions before frameworks. Write retrieval, prompt assembly, and answer steps as plain functions you can call from a REPL. Wrap in FastAPI later. Skip agent frameworks until you have a reason for one.
- One coding assistant, paid plan. Conceptually work through the design first, then have the assistant implement. Review every diff. The point is to understand each line and have a high-level mental model of how components interact - not to outsource the project. Outsourcing the platform design is the failure mode; outsourcing typing is the goal.
- Tech choices do not matter much. FastAPI is fine. Pick whatever the coding assistant suggests when in doubt. Optimise for shipping, not for the right framework.
- Plan extends past 6 weeks. The 6-week shape gets v0.0.1 deployed and the two seed projects shipped. Monitoring, observability, evaluation, durable execution, auth - these are a 12-week-plus arc. Make this explicit so the sprint feels like a foundation, not the whole picture.

### Resources

- AI Hero core course - the entry point for agent fundamentals. Several homework projects can double as the seed projects you deploy in weeks 2-3.
- [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide) - browse recent AI Engineer / AI Platform / MLOps job listings, watch the role webinars to clarify what AI Platform Engineer actually means. The webinar projects are also viable seeds for the second project.
- A coding assistant of choice (Claude Code, Codex, or similar). Pick one, commit, paid plan only.
- Deployment target: Render, Fly.io, or a small VM. The choice does not matter; using one consistently does.

### Deliverables

- 10-job-description analysis + first-project scoping note - by end of week 1.
- Project 1 (RAG) deployed to a public URL - by end of week 2.
- Project 2 (small agent) deployed to a public URL - by end of week 3.
- Shared-shape note + v0.0.1 platform sketch - by end of week 4.
- Platform skeleton with the RAG redeployed through it - by end of week 5.
- Both projects redeployable via the platform path + post-week-6 roadmap + role-direction call - by end of week 6.

### Accountability

- Checklist-based milestones with brief weekly reflections (Manjunath's stated preference). Each week's deliverable is a checkbox; the reflection is two or three lines on what was learned and what was harder than expected.
- 8-10 hours per week. The plan is sized for the lower end so a heavier job-search week can drop a stretch goal rather than the milestone.
- Active in the AI Shipping Labs Slack - both asking and answering questions. Stakeholder communication is one of the gaps Manjunath named; using the community as a low-stakes practice ground for explaining technical work is the cheapest path to closing it.

### Next Steps

- [ ] [Manjunath] Pull 10 job descriptions and write the role-research note by end of week 1.
- [ ] [Manjunath] Pick the first project (RAG dataset + five real questions) and the deployment target.
- [ ] [Manjunath] Pick a coding assistant + paid plan; start AI Hero core course in parallel.
- [ ] [Manjunath] Share weekly progress and reflections in the AI Shipping Labs Slack.
- [ ] [Alexey] Send the written plan and confirm AI Hero core is the right entry point for agent fundamentals.
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
