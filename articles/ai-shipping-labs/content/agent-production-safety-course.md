---
title: "Course Idea: Safely Running Agents Around Production"
created: 2026-07-03
updated: 2026-07-03
tags: [ideas, course, agents, security, ci-cd]
status: draft
---

# Course Idea: Safely Running Agents Around Production

An idea inspired by my article on how I dropped our production database [^1]. People keep reminding me about that story, and it got fairly wide recognition. I want to turn the lesson into a small course about how to set up production alongside agents so that it stays safe and agents cannot get access to prod.

Agents are smart enough that, in principle, they will find a way in. There are ways to set things up so that even when the agent tries, it cannot reach prod. The goal is a maximally locked-down environment where the agent cannot do anything harmful.

The course has two parts. I already wrote about one piece - how to manage access to the database [^1]. The other part is about how to do the projects themselves.

## Part 1: A safe sandbox environment for agents

This part is about how to organize a sandbox account where you can run agents safely.

- Create a sandbox account and a dedicated machine where agents run, so they do not have access to your laptop, where your credentials and prod access live. The agents are maximally isolated.
- Do the work so that agents can experiment with the data but cannot drop anything serious.
- Move that work into production afterwards.
- Do all deployment through CI/CD, and configure the CI/CD correctly so the agent still cannot get access to things it should not.
- Use OIDC. With CI/CD you can grant access to certain things to the pipeline but not to your agent.
- Give agents only temporary access to the sandbox account, not permanent access.
- Cover the staging account and the production account, and the staging environment and the production environment.

## Part 2: How to do the projects

The second part is about how to actually do the projects inside this setup.

## Sources

[^1]: [How I Dropped Our Production Database and Now Pay 10% More for AWS](https://aishippingblog.com/p/how-i-dropped-our-production-database)
[^2]: [20260703_133204_AlexeyDTC_msg4682_transcript.txt](../../../inbox/used/20260703_133204_AlexeyDTC_msg4682_transcript.txt)
