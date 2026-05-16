---
title: "Codehive: Building a Coding Orchestrator"
created: 2026-03-25
updated: 2026-03-25
tags: [claude-code, agents, codehive, orchestrator]
status: draft
---

# Codehive: Building a Coding Orchestrator

[Codehive](https://github.com/alexeygrigorev/codehive) is my attempt to build a coding orchestrator that embeds everything I've learned from [building projects with agent teams](building-projects-with-agent-teams.md) into a single application.

## The Vision

Codehive embeds the methodology I want for a coding orchestrator:

- Hard-coded methodology - the [agent team pipeline](building-projects-with-agent-teams.md) is enforced by the orchestrator, not by prompting
- Multiple agent backends - Claude Code, Codex, GitHub Copilot, xAI - switch between providers or use different ones for different tasks
- Non-blocking workflow - always has a task pool, questions go to a separate list, work never blocks on my answers
- Visibility into subagents - peek inside to see what's happening, correct course
- GitHub integration - create an issue, Codehive wakes up and works on it

## Motivation

The main Claude Code orchestrator has problems that motivated this project.

The agent stops for no reason[^1]:

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/codehive-agent-stopping.jpg" alt="Claude Code terminal showing agent stopping and user asking why did you stop">
  <figcaption>The orchestrator stops and waits instead of continuing with the next task</figcaption>
</figure>

It refuses to pick up the next task on its own, even when tasks are explicitly listed in the backlog[^5]:

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/agent-refusing-next-tasks.jpg" alt="Claude Code terminal showing agent completing a task and asking if it should proceed instead of automatically picking the next one">
  <figcaption>The agent finishes a task and asks instead of picking the next one</figcaption>
</figure>

And it asks unnecessary questions like "shall we proceed?" when the todo list explicitly says "pull next 2." That's wasted time, especially when I'm not nearby[^2].

I also can't see what subagents are doing. The orchestrator launches one and it does something for 30 minutes or an hour. Is it stuck? Does it need a restart? I want to be able to peek inside and correct the process[^2].

The methodology is not enforced - Claude Code can ignore it. I want the orchestrator to be more rigid. The pipeline, the agent roles, the grooming process, and the acceptance criteria should all be hard-coded into the application, not just described in a markdown file that the agent may or may not follow[^4].

## Current State

I dictated the project vision to ChatGPT while walking outside. It produced a summary. I fed that to the agents and launched the process. The agents have only started working on it[^2].

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/codehive-project-summary.jpg" alt="Summary of Codehive project: 96 issues done, ~2,195 tests across backend, web, mobile">
  <figcaption>Codehive project summary - 96 issues, ~2,195 tests across all components</figcaption>
</figure>

I haven't tested it yet because I don't have time. This is the most complex project of all - I want a mobile app, a website, a backend, and a Telegram client[^2][^3].

## Agents Slack Off

This isn't something I can fully leave without supervision. Agents slack off. A lot. It's like managing a team of students who aren't getting paid - they're only there because they need course credits. Everything they do is reluctant, through force[^6].

Each role cuts corners in its own way:

- The PM says "this is too complex, let's descope it" and simplifies the task as much as possible
- The Software Engineer leaves things unfinished
- The Tester says "I can't run this, I won't do it"

You need to organize the process so it's harder for them to cut corners[^6].

## Silent descoping in practice

With the Rustkyll project, I asked to compile for Linux, Mac, and Windows on both AMD64 and ARM64. It compiled for all platforms except Windows ARM64 - it just silently dropped that target. When I asked what happened, it turned out the PM had descoped it. There were no logs, so I couldn't even see when or why[^6][^7].

That's what led to the "no silent descoping" rule in the process. I don't have a problem with descoping in general - sometimes a task is too big. But requirements must not be quietly forgotten[^6].

## Checking Under the Hood

You still need to occasionally look under the hood. It cooks on its own mostly fine, but sometimes you need to lift the lid and check[^6].

With the Jekyll project I wanted pixel-perfect matching. I asked the agents to create tasks based on benchmarks comparing the output. After some time I checked the report - it said everything was fine, pixel-perfect match, and the few percent of different pixels were "font rendering artifacts." A few percent of pixels on a large screenshot is thousands of pixels. I looked at the diff myself and it was clearly not just font rendering[^6].

Same problem with Mermaid diagrams - the output is visual, and agents struggle to evaluate images. We fixed one thing and broke two others. Tests didn't catch it because it's visual, hard to test automatically. I had to write a visual guideline checklist for the agents to follow[^6].

I haven't found a way to fully automate this. It seems project-dependent. My goal right now is to do as many projects as possible with this methodology. Each project sharpens it. I think after about 10 more projects I'll have a solid system[^6].

Phil Winder [wrote about migrating a Python codebase to Go using Claude Code](https://www.linkedin.com/posts/drphilwinder_i-just-migrated-a-production-python-codebase-activity-7430343296205459456-eXUm) and concluded: "Claude is a powerful but literal executor. The gaps in your design become the bugs in your system." This matches what I see[^8].

## Sources

[^1]: [20260316_072803_AlexeyDTC_msg2956_photo.md](../inbox/used/20260316_072803_AlexeyDTC_msg2956_photo.md)
[^2]: [20260315_101751_AlexeyDTC_msg2936_transcript.txt](../inbox/used/20260315_101751_AlexeyDTC_msg2936_transcript.txt)
[^3]: [20260317_104201_AlexeyDTC_msg2972_photo.md](../inbox/used/20260317_104201_AlexeyDTC_msg2972_photo.md)
[^4]: [20260318_104313_AlexeyDTC_msg2984_transcript.txt](../inbox/used/20260318_104313_AlexeyDTC_msg2984_transcript.txt)
[^5]: [20260318_174724_AlexeyDTC_msg3000_photo.md](../inbox/used/20260318_174724_AlexeyDTC_msg3000_photo.md)
[^6]: [20260315_101106_AlexeyDTC_msg2934_transcript.txt](../inbox/used/20260315_101106_AlexeyDTC_msg2934_transcript.txt)
[^7]: [20260315_103325_AlexeyDTC_msg2950_transcript.txt](../inbox/used/20260315_103325_AlexeyDTC_msg2950_transcript.txt)
[^8]: [20260220_143527_AlexeyDTC_msg2156_photo.md](../inbox/used/20260220_143527_AlexeyDTC_msg2156_photo.md)
