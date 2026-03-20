---
title: "New Course Ideas for the Paid Community"
created: 2026-03-01
updated: 2026-03-20
tags: [courses, paid-community, ideas]
status: draft
---

# New Course Ideas for the Paid Community

Several ideas for courses that could be offered in the paid community.

## Specification-Driven Development for AI

A course about becoming a good product manager to effectively communicate with AI agents. The core insight: programmers now need to become good product managers to tell agents what to do. When the specification is not good, the agent produces garbage. If the agent misunderstands the request and does something completely different, it is the programmer's fault for not communicating clearly enough[^1].

The course would teach how to properly communicate to agents what they need to do and how to manage development when the team is made of agents[^1].

### Course structure

The course can cover software development methodologies more broadly - how teamwork happens, what roles exist in a team. Then map this to agents: you are now the product manager, the agents are the implementers[^2].

Topics to cover[^2]:
- How to set tasks in a way that is maximally clear
- What grooming is
- Product management in general
- Acceptance criteria - they must be clear
- Specifications - they must exist
- Kanban

### Final project

The course output will be a kanban board for agents - an application that everyone builds together throughout the course. The graduation project is to build any project of their choosing[^2].

There is already research on spec-driven development patterns and tools collected in the [Spec-Driven Development research article](../research/spec-driven-development.md).

## Data Engineering for AI

A course about building data pipelines for AI systems[^1].

## AI for Data Engineering

A course about using AI effectively to be a more efficient data engineer[^1].

## Refactoring AI Slop

A course called "Refactoring AI Slop." The idea came from thinking about learned helplessness - people who used to know how to program now fully delegate to LLMs and lose the skill. People who never programmed do not learn either[^3].

We can now generate large amounts of code, but then we need to look at what we got and manage the project in a way that minimizes the amount of slop. The course would cover how to set up a project so that slop is minimized from the start, how often to do code reviews, and how to organize the development process with agents[^3].

The course would also cover removing slop: examining examples of slop, dealing with defensive coding (which causes many problems), how to fight it, how to refactor it, and how to make sure it does not keep happening[^3].

AI-generated code has specific problems: it contains too much boilerplate, too much defensive coding, it is hard to read, and it is often overly complex. LLMs also tend to reuse things that could easily be replaced with a library, which results in a lot of unmaintainable code[^3][^4].

The idea is to transform unmaintainable code into maintainable code - following clean code recommendations, checking that tests are meaningful (not written just for test count), and actually useful[^4].

This is related to the idea of the Spec-Driven Development course but with a different focus. Spec-Driven Development is about communicating with agents effectively. Refactoring AI Slop is about what to do with the code afterwards - how to bring it to a normal state[^3].

The course can also serve as a reminder of best coding practices, clean code from Robert Martin, and how we used to write code versus how we write it now. It could cover reading tests, deleting useless tests, and making agents work properly[^3].

One caveat: when I am the only user of the code, if something breaks, I just run an agent to fix it. But when we talk about a platform used by multiple people or a library that many people use, the requirements are different. And since I work in education and show code to students, I want the code to be maximally understandable. AI-generated code is not always understandable, which makes it hard to use as teaching material[^3].

## Sources

[^1]: [20260301_085144_AlexeyDTC_msg2642_transcript.txt](../../inbox/used/20260301_085144_AlexeyDTC_msg2642_transcript.txt)
[^2]: [20260301_092840_AlexeyDTC_msg2648_transcript.txt](../../inbox/used/20260301_092840_AlexeyDTC_msg2648_transcript.txt)
[^3]: [20260320_063747_AlexeyDTC_msg3022_transcript.txt](../../inbox/used/20260320_063747_AlexeyDTC_msg3022_transcript.txt)
[^4]: [20260320_063926_AlexeyDTC_msg3024_transcript.txt](../../inbox/used/20260320_063926_AlexeyDTC_msg3024_transcript.txt)
