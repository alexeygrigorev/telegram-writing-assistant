---
title: "Project Approach Reference Doc"
created: 2026-04-22
updated: 2026-04-22
tags: [ai-shipping-labs, community, reference-doc, project-planning]
status: draft
---

# Project Approach Reference Doc

Several AI Shipping Labs members have come in with a similar ask: they have an existing project (often the Buildcamp capstone) and want to take it to a "production-level" state, but they do not have a concrete plan for how to get there[^1].

Nirajan is not the first person to ask this, so it makes sense to create a reusable reference document on how to approach these requests, rather than rewriting the same recommendations into each individual plan.

## What the doc should cover

Based on the recommendations already given to Edu, Carlos, Vancesca, Jakob, and now Nirajan, the recurring approach is:

- Pick one project (do not spread across multiple).
- Describe the current state of the project and the target state - then the plan is the delta between them.
- Go through the same step-by-step flow as the AI Engineering Buildcamp V2 homeworks.
- Ship end-to-end, with CI/CD (GitHub Actions), a concrete cloud platform (start with AWS Lambda), and Docker.
- Let evaluation and metrics follow from real users and business goals - derive AI metrics from business metrics, not the other way around.
- Deployment, monitoring, and iteration are not things to study separately - they are what happens when you ship.

## Why it helps

- Saves time when a new member asks the same question.
- Gives members a single place to walk through the approach themselves.
- Keeps individual plan files focused on what is specific to that person.

## Sources

[^1]: [20260422_092530_AlexeyDTC_msg3515_transcript.txt](../inbox/used/20260422_092530_AlexeyDTC_msg3515_transcript.txt)
