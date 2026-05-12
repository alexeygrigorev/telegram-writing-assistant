---
title: "Plan: Manjunath Yelipeta"
created: 2026-05-06
updated: 2026-05-12
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Manjunath Yelipeta

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: traditional ML engineer (CV/recommendation/classical ML) without LLM or agentic experience. Jobless for two months, sole bread-earner. Originally leaned toward AI Platform Engineer / MLOps for stability after a difficult prior role, but after his own role research and current referrals he is pivoting the first sprint toward AI Engineering (RAG, agentic patterns, evals, cost/latency). The platform direction stays as the longer-term end goal, and he is parallel-learning Docker, Kubernetes, and DevOps fundamentals in his own time to bridge to it.
- Goal for the next 6 weeks: complete AI Hero in weeks 1-2 as the agent-building foundation, then ship one deployed LLM application end to end on Manjunath's own corpus - applying the AI Hero patterns (RAG, agent loop, eval, deployment) and then going further with a real eval set, a cost-and-latency optimization pass, and portfolio polish. One shipped project covering the four areas Manjunath named (RAG, agents, evals, cost/latency) is more honest at 8-10 hr/week than two half-built ones.
- Main gap to close: the entire LLM and agentic application stack - RAG, prompt and tool design, agent loops, evaluation of LLM systems, and cost/latency optimization. Evaluation maps directly to Manjunath's existing strength (eval + failure-mode analysis from his ML work), so it is the natural bridge from his old skills to the new ones.
- Weekly time commitment: 8-10 hours per week on the sprint, extendable as the job search and family situation allow. Docker/Kubernetes/DevOps self-study happens in parallel, outside this budget.
- Why this plan is the right next step: AI Engineer roles are where the immediate market demand and his referrals are. Building one deployed end-to-end LLM system with honest eval numbers and measured cost/latency improvements is the fastest path to interviews and produces the raw material needed to build a better AI Platform in a later sprint.

## Plan

### Focus

- Main focus: complete AI Hero in weeks 1-2 as the foundation, then ship one deployed LLM application end to end on your own corpus in weeks 3-6 - applying the AI Hero patterns and then going beyond them with a real eval set and a cost-and-latency optimization pass.
- Supporting focus: in week 1, do role research - pull 10 AI Engineer / Applied AI Engineer job descriptions, ask ChatGPT/Claude to summarise responsibilities, watch the relevant role webinars in the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide).
- Parallel track (outside the 8-10 hour budget): Docker, Kubernetes, and DevOps fundamentals self-study. This keeps the AI Platform direction alive for the post-sprint pivot.

### Timeline

Week 1:

- Role research. Pull 10 recent job descriptions for AI Engineer and Applied AI Engineer roles (job boards + the field guide). Ask ChatGPT/Claude to summarise responsibilities and stack. Watch the role webinars in the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide). Output: a one-paragraph note on which patterns (RAG, agents, evals, cost/latency) show up most in current AI Engineer listings.
- Pick the first project (the RAG). Keep it small: a documentation site, a paper collection, internal notes - something with five real questions you would actually want to ask. Sketch the architecture on paper before any code.
- Pick one coding assistant and one paid plan. Avoid free tiers.
- Start AI Hero core course in the background. Cover the agent-loop and tool-calling modules - they are the foundation for the second project in week 3.

Week 2:

- Finish AI Hero (days 4-7): function calling and Pydantic AI agents, logging + LLM-as-judge + synthetic data + metrics, Streamlit + deployment, README + demo. By end of day 7 you have a deployed RAG agent on the course default data - treat this as the foundation pattern, not the portfolio piece.
- Write a one-paragraph project card for your own sprint project (the RAG dataset you picked in week 1): who the user is (often you), what input the system takes, what it produces, what "useful" looks like.
- Find or prepare your corpus - documentation, papers, internal notes, scraped content - whatever fits the five real questions you sketched in week 1.

Week 3:

- Build the simplest working end-to-end version on your own corpus, applying the AI Hero day 1-4 patterns: chunking → indexing → retrieval → agent with the search tool. Functions first, then the Pydantic AI agent loop on top. FastAPI for the API if you want a real backend, or Streamlit if reusing the AI Hero day-6 pattern is the faster path.
- Deploy by end of week 3. Reuse the AI Hero day-6 deployment pattern, or wrap the FastAPI app in Docker and ship to Render, Fly.io, or a small VM. The shape that matters is "deployed thing on your own data", not polish.

Week 4:

- Apply the AI Hero day-5 evaluation pattern to your project: logging agent interactions, LLM-as-judge for the open-ended answers, automatic test data generation, and a metric per dimension you care about. Build the eval set on your own corpus rather than the course default - the questions should be ones a real user would ask of your data.
- Add a short failure-mode breakdown for the misses - this is the workstream that maps directly to your stated strength (evaluation + failure-mode analysis from your ML work). Output: a runnable eval script committed to the repo + baseline numbers + a one-paragraph failure-mode note. Redeploy.

Week 5:

- Cost-and-latency optimization - the focus area you flagged in your feedback and one that AI Hero does not directly cover. Measure baseline cost-per-query and latency-per-query (the logging from week 4 gives you the data). Identify the biggest line items. Pick a couple of optimizations to try, re-measure each, record before/after. The eval set from week 4 is the regression gate - improvements that hurt answer quality are not improvements. Redeploy.

Week 6:

- Polish the project for portfolio shape, applying the AI Hero day-7 pattern: README that covers problem, architecture, eval results, cost/latency numbers, lessons learned. Architecture diagram and short demo if energy allows. Update LinkedIn and resume with the live URL.
- Sketch the post-week-6 platform direction. The platform-shaped end state (drop in an agent, get monitoring + deployment for free) is the next sprint's seed. Sketch only - input contract, deployment target, the rough roadmap - do not build.
- Decide the next-sprint direction. If interview pipeline lights up on AI Engineer roles, the next sprint deepens AI Engineering. If the platform-shaped work feels more energising and the K8s/DevOps self-study is paying off, the next sprint pivots to the v0.0.1 deployment platform.

### Project approach

- One project, deepened week by week. The single project covers all four areas Manjunath named (RAG, agents, evals, cost/latency) by growing in capability rather than spreading thin across multiple builds. Each week's redeploy proves the previous week's work actually shipped.
- Strip ruthlessly in week 2. No monitoring, no evaluation, no auth in the first build. Evaluation is the week-4 workstream by design - keep the initial build simple enough that there is time to evaluate it properly later.
- Functions before frameworks. Write retrieval, prompt assembly, and answer steps as plain functions you can call from a REPL. Wrap in FastAPI later. Wrap in an agent only after the underlying functions work; the agent's nondeterminism stays contained because the deterministic parts are real tested functions.
- One coding assistant, paid plan. Conceptually work through the design first, then have the assistant implement. Review every diff. Outsourcing the eval design or the cost analysis is the failure mode; outsourcing typing is the goal.
- Tech choices do not matter much. FastAPI is fine. Pick whatever the coding assistant suggests when in doubt. Optimise for shipping, not for the right framework.
- Plan extends past 6 weeks. The 6-week shape gets one deployed project with eval and cost stories. The platform direction (monitoring, log aggregation, automatic instrumentation, durable execution, auth) is the next sprint. The AI Engineering work is the foundation the platform sits on, not a detour from the platform goal.
- Docker/K8s/DevOps self-study runs in parallel, outside the sprint budget, to keep the platform skills warm for the post-sprint pivot.

### Resources

- AI Hero core course: https://aishippinglabs.com/courses/aihero - the foundation course, completed in weeks 1-2. Its day-by-day shape (chunking, search, agent, eval, deployment, README) is also the template you apply to your own project in weeks 3-6.
- [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide) - browse recent AI Engineer / Applied AI Engineer job listings, watch the role webinars.
- A coding assistant of choice (Claude Code, Codex, or similar). Pick one, commit, paid plan only.
- Deployment target: Render, Fly.io, or a small VM. The choice does not matter; using one consistently does.

### Deliverables

- 10-job-description analysis (AI Engineer / Applied AI Engineer) + project scoping note + corpus identified - by end of week 1.
- AI Hero completed (deployed RAG agent on course default data) + project card + corpus secured - by end of week 2.
- Simplest end-to-end RAG with agent on your own corpus, deployed to a public URL - by end of week 3.
- Eval set on your own corpus + baseline numbers + failure-mode note, redeployed - by end of week 4.
- Cost/latency optimization pass with before/after numbers, redeployed - by end of week 5.
- README + LinkedIn/resume update + post-week-6 platform sketch + next-sprint direction call - by end of week 6.

### Accountability

- Checklist-based milestones with brief weekly reflections (Manjunath's stated preference). Each week's deliverable is a checkbox; the reflection is two or three lines on what was learned and what was harder than expected.
- 8-10 hours per week on the sprint. The plan is sized for the lower end so a heavier job-search week can drop a stretch goal rather than the milestone.
- Active in the AI Shipping Labs Slack - both asking and answering questions. Stakeholder communication is one of the gaps Manjunath named; using the community as a low-stakes practice ground for explaining technical work is the cheapest path to closing it.

### Next Steps

- [ ] [Manjunath] Pull 10 AI Engineer / Applied AI Engineer job descriptions and write the role-research note by end of week 1.
- [ ] [Manjunath] Pick the first project (RAG dataset + five real questions) and the deployment target.
- [ ] [Manjunath] Pick a coding assistant + paid plan; start AI Hero core course in parallel.
- [ ] [Manjunath] Run Docker/Kubernetes/DevOps self-study in parallel as a longer-term track.
- [ ] [Manjunath] Share weekly progress and reflections in the AI Shipping Labs Slack.
- [ ] [Alexey] Send the updated written plan and confirm AI Hero core is the right entry point for agent fundamentals.
- [ ] [Valeriia] Confirm Manjunath is on the AI Shipping Labs Slack channel and added to the May sprint roster.

## Internal Context

### Persona

Alex - The Engineer Transitioning to AI (preliminary). Manjunath has shipped traditional ML (CV/recommendation/classical), with limited backend exposure (FastAPI, Docker only) and no LLM/agentic experience. He fits Alex more than Taylor - he is not a researcher or theoretical specialist - though his engineering depth is closer to "ML engineer" than to "full-stack/backend engineer". The plan treats the LLM/RAG/agentic side as the main gap.

See [personas.md](../personas.md) for full persona definitions.

### Background

Manjunath is a traditional ML engineer pivoting to AI/LLM work. He is unemployed since around early March 2026 and is the sole bread-earner for his family, which constrains both weekly time (8-10 hours) and the urgency of shipping a portfolio piece that helps with the job search.

He has had a difficult prior role - his director pushed for production AI without proper evaluation or failure-mode analysis - and is wary of AI-first roles where the same dynamics could repeat. He initially leaned toward AI Platform Engineer / MLOps roles for stability, but after his own role research and current referrals he is pivoting the first sprint to AI Engineering (RAG, agents, evals, cost/latency). The platform direction remains his longer-term end goal.

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

#### Member Feedback (2026-05-12)

Manjunath sent the following after reading the v1 plan:

> Hi Alexey,
> After diving into the Job Descriptions for AI Engineer vs. AI Platform Engineer, I've realized that while my end goal remains the Platform side (K8s, serving, GPU infra), the immediate market demand and my current referrals are leaning heavily toward AI Engineering (RAG, Agentic patterns, Evals, and Cost/Latency optimization).
> I'd like to adjust my 6-week plan to focus on building production-grade end-to-end pipelines first. This will give me the "raw material" and empathy needed to build a better AI Platform later. I am also teaching myself Docker, Kubernetes, and DevOps fundamentals in parallel to bridge this gap.

This drove the v2 plan above. The first sprint pivots from "two projects then a v0.0.1 deployment platform" to "two projects deepened with capability + eval + cost/latency, all redeployed". Deployment stays as the through-line. The platform direction is preserved as the next-sprint arc.

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

10. Direction adjustment (2026-05-12): Manjunath did the role research without prompting and concluded that AI Engineer roles are the immediate market match. The plan now follows the standard one-project AI Engineering shape used for Daiyaan ([20260509_daiyaan-shaik.md](20260509_daiyaan-shaik.md)), anchored explicitly in AI Hero modules - weeks 1-2 finish AI Hero (the foundation course Manjunath has access to), weeks 3-6 apply the same day-by-day shape (build, eval, deploy, polish) to his own corpus, with week 5 carved out for the cost/latency focus area Manjunath named (AI Hero does not directly cover this). The platform direction is preserved as the next-sprint target. The v1 two-project + platform plan is kept below for reference.

### Internal Action Items

- [ ] [Alexey] Send Manjunath the updated written plan reflecting the AI Engineering pivot.
- [ ] [Alexey] Confirm AI Hero is the right entry point for agent fundamentals.
- [ ] [Valeriia] Confirm Manjunath is on the AI Shipping Labs Slack channel and added to the May sprint roster.

### Previous Plan (v1, 2026-05-06)

The original plan version, before Manjunath's 2026-05-12 feedback shifted the first sprint toward AI Engineering depth. Kept here for reference.

#### v1 Summary

- Current situation: traditional ML engineer (CV/recommendation/classical ML) without LLM or agentic experience. Jobless for two months and is the sole bread-earner for his family, so the sprint has to lead to a shippable project that helps him land a job. He had a difficult prior role with unrealistic timelines and weak evaluation culture, so he is leaning away from AI-first roles toward AI Platform Engineer / MLOps Engineer / Applied AI Engineer titles, but admits the titles feel confusing.
- Goal for the next 6 weeks: build two small deployed LLM projects (a RAG, then a small agent), then start a v0.0.1 deployment platform that makes shipping the next agent trivial. The two projects are the raw material for the platform - by building them you see what is common, and that commonality becomes the platform's first cut. The platform deliberately ships with no monitoring and no evaluation in v0.0.1; those layers are added gradually after week 6.
- Main gap to close: the entire LLM and agentic application stack - RAG, prompt and tool design, backend engineering beyond FastAPI/Docker, deployment. Observability and evaluation are deferred on purpose so the v0.0.1 platform stays simple enough to actually ship.
- Weekly time commitment: 8-10 hours per week, extendable as the job search and family situation allow. The 6-week shape is explicitly a foundation, not the whole picture - the platform direction is a 12-week-plus arc.
- Why this plan is the right next step: he is leaning toward AI Platform Engineer but has not yet built one LLM application. The fastest way to test whether the platform direction actually fits is to build two simple things, notice what is shared, and start abstracting. That also produces the deployed live URLs hiring committees want to see, even if the platform itself is a v0.0.1.

#### v1 Focus

- Main focus: build a small RAG, then a small agent, then a v0.0.1 deployment platform that makes shipping the next agent trivial. The platform is the 6-week deliverable; the two projects are scaffolding that lets you see what the platform should actually do.
- Supporting focus: in week 1, do role research - pull 10 AI Platform Engineer / MLOps / AI Engineer job descriptions, ask ChatGPT/Claude to summarise responsibilities, watch the relevant webinars in the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide). "AI Platform Engineer" is a confusing title to chase before understanding what the role really involves.
- Supporting focus: AI Hero core course as the entry point for agent fundamentals (agent loops, tool calling). Several of its homework projects can also serve as the seed projects you deploy in weeks 2-3.

#### v1 Timeline

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
- Decide the platform's input contract: what does an agent author hand the platform? (A code repo with a manifest file? A container image plus a config? A Python module conforming to a known interface?) Pick on paper - this is the decision that shapes everything else.
- Decide the deployment path: what does the platform do with that input to produce a live URL? Pick the deployment target (Render, Fly.io, a VM) and the glue (a Python CLI, a Makefile, a GitHub Actions workflow). Pick on paper.
- Write a unified deployment script - one script you run from your terminal that takes either of the two projects as input (per the contract above) and brings up a live URL. Most of week 4's hours go here. By end of week 4 you should be able to point the script at either repo and watch it deploy. This script is the platform v0.0.1 in its earliest form - everything in week 5 is making it less embarrassing.

Week 5:

- Turn the week-4 script into a proper platform skeleton: a small repo of its own, a config format you can document on one page, a CLI or single-command entry point, a README an outsider could follow. Re-deploy the RAG through this cleaned-up path. If the RAG comes up via the new entry point with a config file rather than ad-hoc args, the skeleton is real.

Week 6:

- Re-deploy the second project (the agent) through the same platform path. Two projects coming up via one path is the v0.0.1 acceptance bar.
- Write the post-week-6 roadmap: monitoring, log aggregation, automatic instrumentation, evaluation hooks, durable execution, auth - in the order you would add them. Sketch only, do not build.
- Decide the role question now that you have built the thing. If the platform-shaped work felt energising, the next sprint leans AI Platform / MLOps and the post-week-6 roadmap is your next 6-week plan. If the project work itself felt better than the platform around it, the direction shifts toward AI Engineer.

#### v1 Project approach

- Two small things, then a platform - in that order. The two projects exist to surface what the platform should actually do. Skipping straight to "design the platform" is design without input; this is the failure mode to avoid.
- Strip ruthlessly for v0.0.1. No monitoring, no evaluation, no auth in v0.0.1. Adding them later is straightforward; trying to add them now will mean nothing ships. This is deliberate sequencing, not laziness - the layered build is the whole point.
- Functions before frameworks. Write retrieval, prompt assembly, and answer steps as plain functions you can call from a REPL. Wrap in FastAPI later. Skip agent frameworks until you have a reason for one.
- One coding assistant, paid plan. Conceptually work through the design first, then have the assistant implement. Review every diff. The point is to understand each line and have a high-level mental model of how components interact - not to outsource the project. Outsourcing the platform design is the failure mode; outsourcing typing is the goal.
- Tech choices do not matter much. FastAPI is fine. Pick whatever the coding assistant suggests when in doubt. Optimise for shipping, not for the right framework.
- Plan extends past 6 weeks. The 6-week shape gets v0.0.1 deployed and the two seed projects shipped. Monitoring, observability, evaluation, durable execution, auth - these are a 12-week-plus arc. Make this explicit so the sprint feels like a foundation, not the whole picture.

#### v1 Deliverables

- 10-job-description analysis + first-project scoping note - by end of week 1.
- Project 1 (RAG) deployed to a public URL - by end of week 2.
- Project 2 (small agent) deployed to a public URL - by end of week 3.
- Shared-shape note + unified deployment script that brings up either project from a single command - by end of week 4.
- Platform skeleton (own repo, config format, CLI, README) with the RAG redeployed through it - by end of week 5.
- Both projects redeployable via the platform path + post-week-6 roadmap + role-direction call - by end of week 6.

### Sources

[^1]: [Manjunath Yelipeta's intake (Google Doc)](https://docs.google.com/document/d/1ZpbzJzAmL9t7FcGlcLi8gIo-k5XiXwpAxzNj7kdoxNc/edit?usp=sharing), shared via [20260506_174247_AlexeyDTC_msg3872.md](../../../inbox/used/20260506_174247_AlexeyDTC_msg3872.md).
[^2]: [20260506_195055_AlexeyDTC_msg3878_transcript.txt](../../../inbox/used/20260506_195055_AlexeyDTC_msg3878_transcript.txt) - Alexey's recommendations after reading the Q&A.
