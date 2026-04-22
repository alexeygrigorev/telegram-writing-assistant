---
title: "Plan: Nirajan Acharya"
created: 2026-04-20
updated: 2026-04-22
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Nirajan Acharya

Nirajan reached out via Valeriia after topping the leaderboard of AI Engineering Buildcamp Cohort 2. He wants to take the next step toward being job-ready for real-world AI roles and asked for a personalized plan from Alexey[^1].

## AI Shipping Labs Personal Plan Intake

### 1) Your Initial Input

Hi Valeriia, thanks for reaching out!

Topping the leaderboard of AI Engineering Buildcamp: from RAG to Agents Cohort 2 has been a big milestone for me, and I want to take this further toward becoming job-ready in real-world AI roles.

I'd especially like to focus on:

- Building and deploying production-ready AI agents
- Working with real-world datasets and scalable systems
- Understanding industry workflows (from development to shipping)
- Strengthening problem-solving for competitive AI roles

A personalized plan from Alexey would be really valuable for aligning my progress with these goals. I'm ready to put in the work and would love to grow within this ecosystem.

Looking forward to your guidance!

### 2) Questions

#### What would be most useful for you to achieve in the next 2 to 3 months?

In the next 2-3 months, the most useful outcome would be to refine and extend my existing deployed AI project into a more production-grade system, focusing on scalability, robustness, monitoring, and continuous improvement.

#### If you want to become "job-ready," what do you feel is still missing today?

I have already built and deployed a complete AI project during the capstone. What I feel is still missing is deeper exposure to production-level standards such as system optimization, handling edge cases, advanced evaluation, and working within team-based development environments.

#### If you were applying for AI roles in the next 2 to 3 months, what would you want to be able to show that you cannot show today?

I would want to demonstrate multiple production-level projects or an advanced version of my current system with strong evaluation metrics, real user interaction, and clear evidence of scalability and reliability in real-world scenarios.

#### Which part of the workflow do you most want hands-on practice with next?

I want to focus on post-deployment workflows monitoring, evaluation, iterative improvement, and scaling AI systems based on real usage.

#### What do you mean by "understanding industry workflows"?

I refer to the end-to-end lifecycle followed in real companies especially collaboration, version control, deployment pipelines, performance tracking, user feedback integration, and iterative development in production environments.

#### What do you hope to achieve with this plan in the next 6 to 8 weeks? If you had to choose one concrete outcome for the next 6 weeks, what should it be?

(No answer provided)

#### How much time can you realistically commit each week over the next 6 to 8 weeks?

I can commit around 30-40 hours per week with full focus and consistency.

#### What strengths from your background should the plan build on?

(No answer provided)

#### What is blocking you most right now from moving forward?

(No answer provided)

#### What type of accountability would be most effective for you?

(No answer provided)

#### What would make you feel that, at the end of the next 6 to 8 weeks, the plan was worthwhile?

If I can confidently position myself for AI roles with a strong, production-level portfolio and a clear understanding of real-world workflows, I would consider the plan highly successful.

## Alexey's Recommendations

Nirajan is already quite advanced, so it is hard to give direct advice right away. What Alexey wants first is to understand from him specifically what he is currently planning, what he is working on right now, and what his next concrete steps are. Since he is on the more advanced side, he should himself understand what he wants to do. The topics he lists - "Building, Deploying, Production-Ready AI Agents" or "Working with Real-World Data Sets and Scalable Systems, Industry Workflows" - are all abstract, so the first thing to clarify is what concretely is in his plans[^3].

He writes that he wants to define and extend his existing deployed AI project. Alexey does not want to dictate what he should want - even if Nirajan does not know how to get there, the first thing to understand is what he himself wants to do. The concrete ask is for Nirajan to write down:

1. His current project, and the state it is in right now.
2. The state he wants the project to be in.

From there we can think together about how to get from the current state to the target state. It is quite possible that while doing this exercise he will already figure out the answer himself.

### On "deeper exposure to production-level standards"

He writes "what I feel is still missing is deeper exposure". The question is why he thinks he needs this. If his goal is to find a job, then the question is whether this is actually needed for the job. If his goal is to push his own project, then the question is what specifically he needs for that.

### On multiple projects vs focusing on one

He writes he would like to demonstrate multiple production-level projects or an advanced version of his current system - strong evaluation metrics, real user interaction, and so on. This is something he needs to deploy and look for users. It is not clear how much specific help we can offer there beyond saying "you just need to do it, you need to invest in marketing." Alexey can give some advice, but mostly he can give feedback on what Nirajan wants to do - not prescribe specific steps for getting users.

In Nirajan's case, Alexey would recommend focusing on one project rather than several. He already has a working project and wants to do something with it, so the recommendation is to double down on that existing project.

### On evaluation metrics

Strong evaluation metrics will mostly come naturally once there are users. During the course he built some evaluation system, so the question is what metrics are missing and can be added. If he does not have specific metrics, the starting point is his business goals - derive the metrics from the business goals. Alexey would not focus on AI metrics directly, but on business metrics, and then translate those into AI metrics later.

For this, he needs to pick a domain area. He essentially needs to go through the same path as in the course: come up with a project and execute it step by step.

### On "post-deployment workflow, monitoring, evaluation, iterative improvement"

The foundation for this is already there from the course. Beyond that, he just needs to deploy. Alexey does not have a specific plan here beyond "just do it" - it becomes clear once you start.

### On "understanding industry workflows"

Version control is straightforward - if he is using deployment pipelines, he can use CI/CD in Git. Alexey showed some of this at Tuesday's workshop. "Performance tracking" probably means monitoring and user feedback integration - also shown in the workshop, but again if he is building a product he just needs to build the product and the tracking follows naturally. There are no secrets here, and Alexey does not see the point of a dedicated course on this beyond what the course already covers.

"Training deployment" and "production environment" are not entirely clear - Nirajan would need to elaborate.

### Summary of the situation

It looks like Nirajan wants everything but time is limited. The real problem is choosing, because he wants many things: multiple projects, his own project, and it is unclear which to pick up first. The recommendation is to focus:

- Understand what he actually wants.
- He has a product - whether he is using it with real users is not clear.
- Roll it out to real users and decide what to do next based on that.

From here we can put together a rough plan, but the first concrete ask from Nirajan is to describe the current project, describe the state he wants it to be in, and then we can work out how to get there. Plus clarification on the parts of his answers that were not clear.

### Cross-recommendation from other members

Several members have asked for project-related advice with similar profiles. The approach that keeps recurring in those plans is worth sharing with Nirajan if he is interested:

- Edu's plan: finish the current project and deploy it; pick a new direction (e.g., a company he would like to work at, build something similar end-to-end); add GitHub Actions CI/CD so pushes run tests and deploy to dev, with manual production deploys; look at Terraform for dev/prod setups; start with AWS Lambda as the first platform.
- Carlos's plan: build a step-by-step reference document based on the AI Engineering Buildcamp V2 homeworks, then apply that structure to his own project.
- Vancesca's plan: pick a concrete project from a ready list (DTC hackathon issues in this case) and develop it locally, then deploy to AWS Lambda in Python.
- Jakob's plan: use the gist with prompts for defining a project topic (from the V2 ChatGPT folder in the AI Engineering Buildcamp repo) to help frame a project idea.

The common thread: pick one concrete project, define current and target state, ship end-to-end, layer in CI/CD and cloud deployment, and let evaluation/metrics follow from real users and business goals.

### Action items for Alexey

- [ ] [Alexey] Create a general reference document on how to approach "take my project to production" requests. This is not the first person asking - it makes sense to have a reusable doc that captures the approach (pick one project, define current state and target state, step-by-step plan, CI/CD + deploy, metrics from business goals).

### Next steps for Nirajan

- [ ] [Nirajan] Describe the current state of his project in detail.
- [ ] [Nirajan] Describe the target state he wants the project to reach.
- [ ] [Nirajan] Clarify what he means by "training deployment" and "production environment" and any other parts that were not specific.

## Sources

[^1]: [20260420_093134_valeriia_kuka_msg3467.md](../../../inbox/used/20260420_093134_valeriia_kuka_msg3467.md)
[^2]: [Google Doc](https://docs.google.com/document/d/1Ausmg6-Ozwn7D3CXf4EdZLm6Xu9S12A8ZJFuB8HftaE/edit?usp=sharing)
[^3]: [20260422_092530_AlexeyDTC_msg3515_transcript.txt](../../../inbox/used/20260422_092530_AlexeyDTC_msg3515_transcript.txt)
[^4]: [20260422_071324_AlexeyDTC_msg3513.md](../../../inbox/used/20260422_071324_AlexeyDTC_msg3513.md)
