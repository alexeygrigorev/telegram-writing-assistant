---
title: "Plan: Nirajan Acharya"
created: 2026-04-20
updated: 2026-04-23
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Nirajan Acharya

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: already one of the strongest builders in the group, with a deployed AI project and strong motivation to become more job-ready for real-world AI roles.
- Goal for the next 6 weeks: turn one existing deployed project into a more production-grade system with clearer metrics, reliability, and real user signals.
- Main gap to close: focus and specificity. The bottleneck is no longer "learning AI" in general, but choosing one concrete target state and executing against it.
- Weekly time commitment: 30 to 40 hours.
- Why this plan is the right next step: Nirajan is advanced enough that another abstract roadmap will not help much. The use is in defining the project state clearly and shipping against that definition.

## Plan

## Focus

- Main focus: double down on one existing project instead of splitting attention across several.
- Supporting focus: derive evaluation and monitoring from business goals rather than chasing abstract AI metrics.
- Supporting focus: add the production signals that matter most: clearer scope, deployment flow, monitoring, and iterative improvement.

## Timeline

Week 1:

- Write down the current state of the existing project in concrete terms.
- Write down the target state for the next 6 weeks: what should be better, more reliable, or more visible.
- Define the business goal of the project and the open questions that still need clarification.

Week 2:

- Prioritize the top 1 to 2 gaps between current state and target state.
- Translate business goals into concrete metrics and evaluation checks.
- Remove or postpone any work that does not support the chosen target state.

Week 3:

- Implement the highest-priority reliability and deployment improvements.

Week 4:

- Add or tighten CI/CD, monitoring, and feedback collection around the main workflow.

Week 5:

- Put the upgraded project in front of real users or realistic usage scenarios.
- Track failures, missing instrumentation, and user-facing friction.

Week 6:

- Summarize what improved, what the metrics now say, and what the next iteration should be.
- Decide whether the next step is deeper hardening of the same project or a second project only after the first one is truly in a stronger state.

## Resources

- Nirajan's existing deployed project - the fastest route to job-ready proof.
- AI Engineering Buildcamp material on evaluation and deployment - enough foundation already exists there.
- Tuesday workshop material on version control and deployment pipelines - useful for tightening the production workflow.

## Deliverables

- A written current-state vs. target-state document for the project.
- One upgraded deployed project with clearer monitoring, evaluation, or reliability signals.
- Metrics tied to business goals rather than generic AI claims.
- A prioritized backlog for the next iteration, based on real usage or realistic feedback.

## Accountability

- Weekly shipped-change update: what changed in the product, what was learned, and what is next.
- Resist the urge to open parallel projects before the chosen one reaches the target state.
- Use real user feedback or realistic usage evidence as the main checkpoint, not just personal intuition.

## Next Steps

- [ ] [Nirajan] Describe the current state of the project in detail.
- [ ] [Nirajan] Describe the target state he wants the project to reach.
- [ ] [Nirajan] Clarify ambiguous terms such as "training deployment" and "production environment" so the plan can be grounded properly.

## Internal Context

## Persona

Priya - The Improver. Already capable and already shipping, but now needs sharper focus, stronger production patterns, and a clearer approach to evaluation and iteration.

## Background

Nirajan reached out after topping the leaderboard of AI Engineering Buildcamp Cohort 2. He already has a deployed AI project and wants to become more job-ready for real-world AI roles. The challenge is not lack of effort or time. It is defining the next concrete step instead of speaking at the level of abstractions.

## Intake

## Initial Input

Hi Valeriia, thanks for reaching out!

Topping the leaderboard of AI Engineering Buildcamp: from RAG to Agents Cohort 2 has been a big milestone for me, and I want to take this further toward becoming job-ready in real-world AI roles.

I'd especially like to focus on:

- Building and deploying production-ready AI agents
- Working with real-world datasets and scalable systems
- Understanding industry workflows (from development to shipping)
- Strengthening problem-solving for competitive AI roles

A personalized plan from Alexey would be valuable for aligning my progress with these goals. I'm ready to put in the work and would love to grow within this ecosystem.

Looking forward to your guidance!

## Questions and Answers

What would be most useful for you to achieve in the next 2 to 3 months?

In the next 2-3 months, the most useful outcome would be to refine and extend my existing deployed AI project into a more production-grade system, focusing on scalability, robustness, monitoring, and continuous improvement.

If you want to become "job-ready," what do you feel is still missing today?

I have already built and deployed a complete AI project during the capstone. What I feel is still missing is deeper exposure to production-level standards such as system optimization, handling edge cases, advanced evaluation, and working within team-based development environments.

If you were applying for AI roles in the next 2 to 3 months, what would you want to be able to show that you cannot show today?

I would want to demonstrate multiple production-level projects or an advanced version of my current system with strong evaluation metrics, real user interaction, and clear evidence of scalability and reliability in real-world scenarios.

Which part of the workflow do you most want hands-on practice with next?

I want to focus on post-deployment workflows monitoring, evaluation, iterative improvement, and scaling AI systems based on real usage.

What do you mean by "understanding industry workflows"?

I refer to the end-to-end lifecycle followed in real companies especially collaboration, version control, deployment pipelines, performance tracking, user feedback integration, and iterative development in production environments.

What do you hope to achieve with this plan in the next 6 to 8 weeks? If you had to choose one concrete outcome for the next 6 weeks, what should it be?

(No answer provided)

How much time can you realistically commit each week over the next 6 to 8 weeks?

I can commit around 30-40 hours per week with full focus and consistency.

What strengths from your background should the plan build on?

(No answer provided)

What is blocking you most right now from moving forward?

(No answer provided)

What type of accountability would be most effective for you?

(No answer provided)

What would make you feel that, at the end of the next 6 to 8 weeks, the plan was worthwhile?

If I can confidently position myself for AI roles with a strong, production-level portfolio and a clear understanding of real-world workflows, I would consider the plan highly successful.

## Meeting Notes

No separate intake call notes are currently attached in this file.

## Internal Recommendations

Nirajan is already quite advanced, so Alexey does not want to jump straight into prescribing work without first understanding what Nirajan himself wants the current project to become[^3].

The main issue with the current intake is that many goals are still abstract: "production-ready AI agents," "real-world datasets," "industry workflows," and similar phrases do not yet define a build plan.

The core recommendation is:

1. Write down the current state of the project.
2. Write down the target state of the project.
3. Use that gap to decide what to build next.

Other important internal notes:

- Alexey would recommend focusing on one project rather than several.
- Strong evaluation metrics should come from business goals and real users, not from AI metrics in isolation.
- Much of the desired "industry workflow" experience will emerge naturally once the project is deployed and iterated on.
- If Nirajan wants help, the most useful thing is not more general advice but clearer specificity about the project and the desired outcome.

## Internal Action Items

- [ ] [Alexey] Create a general reference document on how to approach "take my project to production" requests.
- [ ] [Nirajan] Describe the current state of the project in detail.
- [ ] [Nirajan] Describe the target state he wants the project to reach.
- [ ] [Nirajan] Clarify the parts of his answers that were still abstract or unclear.

## Sources

[^1]: [20260420_093134_valeriia_kuka_msg3467.md](../../../inbox/used/20260420_093134_valeriia_kuka_msg3467.md)
[^2]: [Google Doc](https://docs.google.com/document/d/1Ausmg6-Ozwn7D3CXf4EdZLm6Xu9S12A8ZJFuB8HftaE/edit?usp=sharing)
[^3]: [20260422_092530_AlexeyDTC_msg3515_transcript.txt](../../../inbox/used/20260422_092530_AlexeyDTC_msg3515_transcript.txt)
[^4]: [20260422_071324_AlexeyDTC_msg3513.md](../../../inbox/used/20260422_071324_AlexeyDTC_msg3513.md)
