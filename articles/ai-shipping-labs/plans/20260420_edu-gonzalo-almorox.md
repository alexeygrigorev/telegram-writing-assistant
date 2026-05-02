---
title: "Plan: Edu Gonzalo Almorox"
created: 2026-04-20
updated: 2026-04-23
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Edu Gonzalo Almorox

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: Senior data scientist in Madrid with solid RAG/agent experience, but limited ownership of the final deployment and production side.
- Goal for the next 6 weeks: have a deployed AI project that clearly demonstrates engineering depth to hiring managers.
- Main gap to close: deployment, CI/CD, monitoring, and the evaluation/improvement loop.
- Weekly time commitment: 8 to 10 hours.
- Why this plan is the right next step: Edu already understands the AI side reasonably well; the highest-leverage move is to ship and operationalize a project end to end.

## Plan

### Focus

- Main focus: finish the current project and deploy it properly.
- Supporting focus: add visible engineering signals such as tests, monitoring, and CI/CD.
- Supporting focus: define the next company/domain direction only after the first project is clearly shipped.

### Timeline

Week 1:

- Finish dockerizing the current project.
- Pick the first deployment target so the hosting decision does not drag on.

Week 2:

- Deploy the current project to a simple cloud target so it is no longer stuck on the laptop.
- Capture the first rough deployment notes and blockers.

Week 3:

- Add tests and basic monitoring.
- Fix the highest-friction issues discovered during deployment.

Week 4:

- Add a lightweight evaluation/improvement loop.
- Document the main system tradeoffs clearly enough that Edu can explain the architecture inside out.

Week 5:

- Add GitHub Actions so pushes run tests automatically and deploy to a dev environment.
- Keep production deployment manual so the workflow mirrors a more realistic engineering setup.

Week 6:

- Polish the deployed version and close the biggest engineering gaps.
- If useful, sketch the next layer: Terraform for cleaner infra or a second project brief in a target company/domain direction.

### Resources

- Edu's existing AI Buildcamp capstone - fastest path because the context already exists.
- Docker - makes the project runnable and easier to ship.
- GitHub Actions - adds an immediate portfolio signal around engineering discipline.
- AWS Lambda - simple first deployment platform.
- Terraform - optional next step once the basic deployment path works.

### Deliverables

- One deployed project that can be shown to employers.
- Dockerized app plus automated test/deploy workflow.
- Basic monitoring and one documented evaluation/improvement loop.
- Optional second project brief or prototype aligned to a target company or domain.

### Accountability

- Weekly async update covering what was shipped, what broke, and what the next deployment milestone is.
- Share one visible milestone with the community: deployed dev environment, production deploy, or evaluation report.
- Keep scope small enough that the plan still fits inside 8 to 10 hours per week.

### Next Steps

- [ ] [Edu] Finish dockerizing the current project and list the blockers.
- [ ] [Edu] Pick the first deployment target, starting with AWS Lambda if no stronger preference exists.
- [ ] [Alexey] Review the deployed version and the CI/CD setup once the first milestone is live.

## Internal Context

### Persona

Taylor - The Research-to-Engineering Transitioner. Strong data science background, but the main gap is production engineering, deployment, and MLOps.

### Background

Edu is a senior data scientist working in health economics in Madrid. He has built RAG and agentic systems, but mostly at PoC level and without owning the full deployment path. He wants to position himself for AI-engineering-type roles and needs more proof of engineering execution.

### Intake

#### Initial Input

A bit of background from me. I am a senior data scientist working for a health economics consultancy based in Madrid, Spain. I belong to the Data and Tech team, and our aim is to build data products that support the day-to-day of our colleagues in the business units. I have worked across several industries, academia, media, biotech, and now health economics. My roles have transitioned from analytics to ML - although, since this year, I am supporting the analytics tasks at my company too. As I mentioned above, my goal for the forthcoming months is to search for positions that have a greater AI component. In my current position I have had the chance to build some RAG but they were clearly PoC rather than products and I was contributing mainly to the initial stage - not being present in the whole pipeline (the deployment has been devoted to the DEs). I guess I would like to be involved in projects where I can have more hands-on real experience integrating AI.

#### Questions and Answers

**What do you feel is currently missing between your profile today and the type of role you want next?**

I feel I lack experience on more engineering side of AI. I have managed to build a RAG/Agent systems that deliver very decent results. However, I have missed the last step - deploy it as a solution that can be accessible to people and that is scalable.

**If you were applying in 2 to 3 months, what would you want to be able to point to?**

I am able to explain a system inside out. What I mean by this is that I am able to propose a reasonable solution that solves a business problem through AI. I have a clear idea of what the identify potential problems and trade-offs associated with that solution such as choosing certain strategies for chunking, validating the results, evaluating the system and deploying well the solution - i.e. without blowing up resources once the solution has escalated.

**What do you feel you need to demonstrate more clearly to be a stronger candidate for AI-engineering-type roles?**

I think I should demonstrate better the skills that define me as an Engineer. Moving from "this is a guy that has some understanding of how agents work to this is a guy that understands how an agent works because this agent that built shows reliable results and it is deployed".

**What is blocking you most right now from building that proof?**

I feel I need more practice. I understand high level how it should work but I don't have the chance to put on more time to actually look at this in detail. I also would like to keep an eye at the costs. I know I need to invest but since I am doing this as a personal project that funding out my pocket I want to contain the costs.

**What have you already tried, and where did it usually stop?**

As part of the AI Buildcamp I did the capstone project and I am currently in the process of deployment. At the moment dockerizing the app and hopefully deploying it in cloud. Normally my projects do not go beyond my laptop and remain local.

**Do you already have a project idea that feels relevant for this transition?**

Literally any solution I can think about that can be deployed somewhere. Yet, perhaps we can discuss ideas that are more business oriented. I tend to think about questions that have some sort of social impact but that I may be less profitable.

**Which part of the AI pipeline do you most want to get hands-on experience with?**

Possibly the end of the pipeline. In addition to deploying the results of the app, learn how to integrate the improvement loop by which I can improve the app by including results of the evaluation so the system "learns" about past errors and gets better.

**What strengths from your background should the plan build on?**

Agentic systems that improve the decision making in health economics / pharma / biotech; strengthen the MLOps and cloud practices around the current system I built and/or others I may build in the forthcoming weeks; and position myself as the guy who integrates AI into traditional questions in those industries.

**How much time can you realistically commit each week over the next 6 to 8 weeks?**

Around 8 - 10 h.

**If you had to choose one concrete outcome for the next 6 weeks, what should it be?**

Have a proper product/project that can I can be attractive to hiring managers and that proves I am decently competent at AI.

### Meeting Notes

No separate intake call notes are currently attached in this file.

### Internal Recommendations

Edu already completed the course and his interest is more around growing as an engineer, so the plan should lean heavily toward deployment and DevOps[^3].

Alexey's rough recommendation:

1. Finish the current project and deploy it.
2. If possible, build a second end-to-end project as an additional portfolio signal.
3. Pick a direction by looking at a company or domain Edu wants to work in and building something adjacent.
4. Make sure the project includes tests, monitoring, and deployment rather than stopping at a local demo.
5. Add GitHub Actions with automatic test and dev deploy on push, plus manual production deploy.
6. If engineering is the main focus, Terraform is worth exploring for dev/prod setup.
7. Start with a simple platform such as AWS Lambda before anything more complex.

### Internal Action Items

- [ ] [Edu] Finish the current project deployment.
- [ ] [Edu] Decide whether to deepen the existing project or build a second one after deployment.
- [ ] [Alexey] Review Edu's chosen deployment path and give feedback on the CI/CD setup.

### Sources

[^1]: [Google Doc](https://docs.google.com/document/d/1vSXH0Tvr47d62qCm7llK5AAjUWmDJpE3NB_X5TR4N6U/edit?usp=sharing)
[^2]: [20260420_083739_AlexeyDTC_msg3445.md](../../../inbox/used/20260420_083739_AlexeyDTC_msg3445.md)
[^3]: [20260420_102138_AlexeyDTC_msg3469_transcript.txt](../../../inbox/used/20260420_102138_AlexeyDTC_msg3469_transcript.txt)
