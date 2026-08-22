---
title: "I Built an AI Agent Team for Software Development and Tested on 5 Real Projects"
date: 2026-04-03
url: https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software
---

Over the past few weeks, I’ve been trying out a new way of working with agent teams for software development using Claude Code. Instead of just seeing it as a single tool, I’ve started thinking of the main session as an orchestrator that directs a small team of agents.

[![Image 1](https://substackcdn.com/image/fetch/$s_!pZuV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda57c184-fd22-42f9-a1ab-522f1b6f3e6c_2779x1378.png)](https://substackcdn.com/image/fetch/$s_!pZuV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda57c184-fd22-42f9-a1ab-522f1b6f3e6c_2779x1378.png)

I’ve tested this setup on a few projects now, and while it’s still a work in progress, I can already see what works, what doesn’t, and what controls are needed to let the agents build real projects with minimal oversight.

In this post, I’ll share what my setup looks like: how I describe the agents, how they interact, how it all fits into a single-team workflow, and how I used this approach to build five different projects.

## Background

For small tools, I usually dump my idea into my [Telegram Writing Assistant](https://alexeyondata.substack.com/p/telegram-assistant) or [talk to ChatGPT](https://alexeyondata.substack.com/p/how-i-built-sqlitesearch-a-lightweight) to refine it (or both). I iterate with Claude until the concept works. This approach is sufficient for smaller utilities or projects that I can easily manage.

But it falls short for more complex projects with too many moving parts and tasks at different stages. For example, it doesn’t provide a way to verify the agent’s claims that a task is complete or test that it was implemented correctly according to the plan.

[![Agent roles table showing Product Manager, Software Engineer, Tester, and On-Call Engineer](https://substackcdn.com/image/fetch/$s_!A7QA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4282e631-9593-454f-8aba-39465e635922_1280x581.jpeg)](https://substackcdn.com/image/fetch/$s_!A7QA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4282e631-9593-454f-8aba-39465e635922_1280x581.jpeg)

That’s why I decided to try building a team of agents, each with their own role, with the main session serving as the orchestrator: it launches agents, assigns tasks among them, ensures compliance with the process, and only commits the work after the final acceptance step is completed.

## The Team and the Process

[![Image 3](https://substackcdn.com/image/fetch/$s_!Vxsq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feaf5feaf-adf8-4ae6-8b75-1e995392bd60_2899x1440.png)](https://substackcdn.com/image/fetch/$s_!Vxsq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feaf5feaf-adf8-4ae6-8b75-1e995392bd60_2899x1440.png)

The agent roles: PM, Software Engineer, Tester, and On-Call Engineer

In my current setup, the work is split across four roles.

* The [Product Manager](https://github.com/AI-Shipping-Labs/website/blob/main/.claude/agents/product-manager.md) (PM) takes a raw task and turns it into something implementable: a spec with user stories, acceptance criteria, and test scenarios. Later, after implementation and QA, the PM reviews the result from the user’s perspective and decides whether the task is actually complete.
* The [Software Engineer](https://github.com/AI-Shipping-Labs/website/blob/main/.claude/agents/software-engineer.md) (SWE) implements the code and writes tests.
* The [Tester](https://github.com/AI-Shipping-Labs/website/blob/main/.claude/agents/tester.md) (QA) runs those tests, checks each acceptance criterion, and reports pass or fail with evidence.
* The [On-Call Engineer](https://github.com/AI-Shipping-Labs/website/blob/main/.claude/agents/oncall-engineer.md) monitors CI/CD after code is pushed and fixes pipeline failures.

Each role has a narrow set of responsibilities, which makes it harder to skip steps and easier to see where something went wrong. For example, this task distribution allows me to avoid a situation in which the same agent writes the code and decides whether it’s correct.

[Share](https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software?utm_source=substack&utm_medium=email&utm_content=share&action=share)

### Pipeline

Every task moves through the same sequence. I ask the orchestrator to create the task and add it to the backlog. The PM picks it up and grooms it. The SWE implements it. QA verifies it. If QA rejects the task, it goes back to the SWE for fixes. If QA accepts it, the PM does a final acceptance review. Only after the PM accepts does the orchestrator commit the code and close the task.

[![Image 4](https://substackcdn.com/image/fetch/$s_!QESf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F732331c7-693b-46cb-9053-7161a130d3d6_2779x1378.png)](https://substackcdn.com/image/fetch/$s_!QESf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F732331c7-693b-46cb-9053-7161a130d3d6_2779x1378.png)

The pipeline: every task goes through PM, SWE, QA, and back to PM before commit

The final PM review is important for making sure the result aligns with the user story, which is a key requirement beyond just passing tests. A feature might seem done from an engineering standpoint, but can still flop in real-life situations.

The process is written down in the repository so the agents can follow it consistently:

* [.claude/agents/](https://github.com/AI-Shipping-Labs/website/tree/main/.claude/agents) contains the role definitions
* [PROCESS.md](https://github.com/AI-Shipping-Labs/website/blob/main/_docs/PROCESS.md) describes the development workflow
* [CLAUDE.md](https://github.com/AI-Shipping-Labs/website/blob/main/CLAUDE.md) contains project-level instructions
* The [execute](https://github.com/AI-Shipping-Labs/website/blob/main/.claude/skills/execute/SKILL.md) skill starts the pipeline

### Parallel Batches

I usually run two tasks in parallel. When that batch is finished, the orchestrator pulls the next two from the backlog.

[![Image 5](https://substackcdn.com/image/fetch/$s_!YEYL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8506fd-5c65-40b8-b688-d30c59996ce7_1224x1416.png)](https://substackcdn.com/image/fetch/$s_!YEYL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8506fd-5c65-40b8-b688-d30c59996ce7_1224x1416.png)

Two tasks processed in parallel, then the next batch is pulled from the backlog

To keep the loop going without manual intervention, I keep a recurring instruction in the task list that tells the orchestrator to fetch the next batch and then add the same instruction again. That way, the process continues until the backlog is empty, rather than stopping after each batch is completed.

[![Claude Code task list with agents running in parallel](https://substackcdn.com/image/fetch/$s_!me35!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6ef47ca-1f72-4197-becb-e6ef5f6cc06d_1129x400.jpeg)](https://substackcdn.com/image/fetch/$s_!me35!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6ef47ca-1f72-4197-becb-e6ef5f6cc06d_1129x400.jpeg)

Task list with agents running in parallel

## Task Tracking

For tracking, I use either GitHub Issues or a file-based tracker/ folder. GitHub Issues work well when I want visible coordination and agent reports attached to each task. The file-based approach is lighter: task status is encoded in the filename, moving from .todo.md to .groomed.md to .in-progress.md, and eventually into done/.

[![Image 7](https://substackcdn.com/image/fetch/$s_!dBiL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F203f5e07-e011-4dc1-9cae-3d1fa1a11758_1600x1069.png)](https://substackcdn.com/image/fetch/$s_!dBiL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F203f5e07-e011-4dc1-9cae-3d1fa1a11758_1600x1069.png)

GitHub issues as the task tracker

In the following sections, I describe the projects I implemented using the agent team approach. For task tracking, I used GitHub for some projects and a file-based version control system for others.

The tool itself matters less than the workflow around it. In both cases, the same PM -> SWE -> QA -> PM loop stays in place.

[Share](https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## 1) AI Shipping Labs Website

My first serious attempt at this approach was the [AI Shipping Labs community platform](https://github.com/AI-Shipping-Labs/website). I will describe it in more detail in a separate article, but here I want to focus on how the process worked.

[![Image 8](https://substackcdn.com/image/fetch/$s_!8mOQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60443459-4bca-4dc2-b2da-8feccf3c74f8_1600x845.png)](https://substackcdn.com/image/fetch/$s_!8mOQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60443459-4bca-4dc2-b2da-8feccf3c74f8_1600x845.png)

When Valeriia and I decided to create a new community, we started by collecting requirements for the platform that would host it. We recorded a lot of voice messages and had multiple sessions with ChatGPT, and eventually it became clear that no existing platform matched what we wanted, so building our own made more sense.

At that point, the requirements already existed, but they were spread across multiple sources. I pulled everything into one file, asked Claude Code to turn it into specifications and then into tasks, and used [GitHub Issues](https://github.com/AI-Shipping-Labs/website/issues) as the tracker.

Once the setup was ready, I let the agents run through the night. The next morning, 41 out of 46 tasks were already done.

[![Task progress after overnight autonomous work - 46 tasks, 41 completed](https://substackcdn.com/image/fetch/$s_!wctE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f80cc95-9a9e-4d4b-8358-71cc181f932d_976x562.jpeg)](https://substackcdn.com/image/fetch/$s_!wctE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f80cc95-9a9e-4d4b-8358-71cc181f932d_976x562.jpeg)

Morning after: 41 out of 46 tasks completed overnight without intervention

That was the first time I saw that this workflow could handle a non-trivial project. Since then, I have iterated on the methodology many times, but the structure stayed the same: I talk to the orchestrator, it creates an issue, and then it launches the implementation pipeline of grooming, implementation, testing, and acceptance.

If you want to see how these issues look in practice, check this one about [adding comments](https://github.com/AI-Shipping-Labs/website/issues/147). The PM described the requirements, acceptance criteria, and test scenarios, the SWE reported that the feature was implemented, QA verified it, and the issue includes screenshots of the final result.

[![Image 10](https://substackcdn.com/image/fetch/$s_!sc91!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63e8cf8c-eb19-4c4c-b83d-21591080e257_1600x724.png)](https://substackcdn.com/image/fetch/$s_!sc91!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63e8cf8c-eb19-4c4c-b83d-21591080e257_1600x724.png)

## 2) DataTasks for DataTalks.Club

After AI Shipping Labs, I wanted to see whether the same methodology would work on a different kind of project.

The first candidate was a task tracker for the DataTalks.Club team. At the moment, our work is split across a Trello board, different spreadsheets, and a Telegram channel with a TODO bot.

This setup works, but it creates a lot of cognitive load. I’ve been planning to replace it with a custom solution, but I haven’t had the time to build one. With coding agents, that became realistic.

[![Telegram TODO bot channel with task list](https://substackcdn.com/image/fetch/$s_!vjBT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdd05621-6623-4a0b-a805-5cc4f1d63ce2_1316x1032.png)](https://substackcdn.com/image/fetch/$s_!vjBT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdd05621-6623-4a0b-a805-5cc4f1d63ce2_1316x1032.png)

Our current task tracking in a Telegram channel with a TODO bot

I dictated the requirements through the Telegram bot, added one technical constraint, that the application had to be serverless and run on AWS Lambda with DynamoDB, and let the team choose the rest.

The result is [DataTasks](https://github.com/alexeygrigorev/datatasks). I spent about 20 minutes dictating the requirements, another 20 minutes starting the Claude Code session, and another 20 minutes giving some feedback the next day.

[![Data Tasks dashboard showing Active Bundles on the left and Today's Tasks on the right](https://substackcdn.com/image/fetch/$s_!kgiq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facc532a5-c3b1-44cb-b25f-52a8c22049a5_1600x815.png)](https://substackcdn.com/image/fetch/$s_!kgiq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facc532a5-c3b1-44cb-b25f-52a8c22049a5_1600x815.png)

DataTasks dashboard showing Active Bundles on the left and Today’s Tasks on the right

I paused the project for now because I do not have time to evaluate it properly, and our current task-tracking setup still works well enough. But as an experiment, it proved useful, showing that the methodology can be applied beyond a single project.

[Share](https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## 3) Merm (Mermaid Diagrams)

The next project came from a more specific technical need.

While working on the [AI Engineering Buildcamp course](https://maven.com/alexey-grigorev/from-rag-to-agents), I needed to include diagrams in one of the lessons, and Mermaid was the obvious format for that.

When I tried to render Mermaid diagrams to images from Python, I ran into two limitations. I could not find a Python library that rendered them directly, and the available Node.js solution launched a full browser under the hood. For something as common as Mermaid, that felt unnecessarily heavy.

[![Mermaid .mmd diagram file for the course](https://substackcdn.com/image/fetch/$s_!ht2z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6265a115-b255-4343-9696-6e5810aef255_1600x974.png)](https://substackcdn.com/image/fetch/$s_!ht2z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6265a115-b255-4343-9696-6e5810aef255_1600x974.png)

Mermaid diagrams

So I asked Claude Code to implement a pure Python renderer.

I followed the same overall methodology, but used the file system instead of GitHub Issues because I did not yet know whether the project would be useful enough to justify a full setup. I created a folder, initialized a Git repository, asked the agent to put all tasks into a tracker folder, and let the filenames encode the state of each task, from .todo.md to .groomed.md to .in-progress.md, and finally into done/.

My role here was mostly to check in occasionally, point out what I did not like, and define clearer criteria when needed. Toward the end, I [also asked for benchmarks](https://github.com/alexeygrigorev/merm/tree/main/benchmark), because it was not enough for the renderer to work; it also needed to be fast enough to justify using it.

[![Merm performance benchmarks comparing rendering times](https://substackcdn.com/image/fetch/$s_!_9tF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54e81600-5a1a-4afa-b4de-83ffc94e01d0_923x487.png)](https://substackcdn.com/image/fetch/$s_!_9tF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54e81600-5a1a-4afa-b4de-83ffc94e01d0_923x487.png)

Merm performance benchmarks

The results were good enough that I published them as [merm](https://github.com/alexeygrigorev/merm), and now I use it to generate diagrams, including the ones in this article.

[![Image 15](https://substackcdn.com/image/fetch/$s_!_bq3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71d43f40-e176-4e07-9e81-b0aa40dc74bb_1600x809.png)](https://substackcdn.com/image/fetch/$s_!_bq3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71d43f40-e176-4e07-9e81-b0aa40dc74bb_1600x809.png)

Here are a few examples from the [gallery](https://github.com/alexeygrigorev/merm/tree/main/docs/examples):

[![Image 16](https://substackcdn.com/image/fetch/$s_!dgEX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22db35bf-4cbe-40b0-94d5-fd44c78cab80_1600x488.png)](https://substackcdn.com/image/fetch/$s_!dgEX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22db35bf-4cbe-40b0-94d5-fd44c78cab80_1600x488.png)

[CI pipeline diagram](https://github.com/alexeygrigorev/merm/tree/main/docs/examples#ci-pipeline) with Build, Test, and Deploy stages rendered by Merm

[![Image 17](https://substackcdn.com/image/fetch/$s_!uDvL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f6540f7-a8da-4e7c-84d7-7668921ecd04_1600x1263.png)](https://substackcdn.com/image/fetch/$s_!uDvL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f6540f7-a8da-4e7c-84d7-7668921ecd04_1600x1263.png)

[Sequence diagram](https://github.com/alexeygrigorev/merm/tree/main/docs/examples#mermaid-readme-6) with three participants, a loop fragment, and notes rendered by Merm

## 4) Rustkyll (Jekyll to Rust)

Our [DataTalks.Club](https://datatalks.club/) website uses [Jekyll](https://github.com/DataTalksClub/datatalksclub.github.io), a static site generator written in Ruby. I still think it is a good choice for small sites, but the DataTalks.Club website has been growing for more than five years, and at this point, building it takes more than a minute on my computer.

[![DataTalks.Club website](https://substackcdn.com/image/fetch/$s_!noqu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc4b47e6-4b0f-4b2c-b19e-62ae15aa4534_1600x932.png)](https://substackcdn.com/image/fetch/$s_!noqu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc4b47e6-4b0f-4b2c-b19e-62ae15aa4534_1600x932.png)

DataTalks.Club website

That delay is long enough to interrupt the workflow. I make a small change, wait more than a minute, check the result, and repeat. Recently, I was adding a new sponsor logo, Snowplow, and even that small edit reminded me how much friction had accumulated.

[![Snowplow logo added as a new sponsor on DataTalks.Club](https://substackcdn.com/image/fetch/$s_!3Dbn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a0eb450-6e8e-4bbc-ac54-cc526708646a_1600x530.png)](https://substackcdn.com/image/fetch/$s_!3Dbn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a0eb450-6e8e-4bbc-ac54-cc526708646a_1600x530.png)

Snowplow logo added as a new sponsor on DataTalks.Club

I had wanted to rewrite Jekyll in Rust for months, and this seemed like a good project to further test the methodology, so I started [Rustkyll](https://github.com/alexeygrigorev/rustkyll/).

[![Image 20](https://substackcdn.com/image/fetch/$s_!0ZGr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cdca80d-bdcc-4a4f-90b3-cfcd55d604de_1600x854.png)](https://substackcdn.com/image/fetch/$s_!0ZGr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cdca80d-bdcc-4a4f-90b3-cfcd55d604de_1600x854.png)

Here, I skipped the requirements step, which turned out to be a mistake. I simply pointed Claude to our website and said, “Reimplement it in Rust using this methodology.”

The next day, I checked the output and saw that the result was tailored to our site rather than a generic engine that could support other Jekyll websites. So I had to correct the direction and ask it to find other Jekyll sites and make the implementation work for those too.

[![Image 21](https://substackcdn.com/image/fetch/$s_!Rx_0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca01131c-79e2-483d-8b44-c60aa4281be9_1600x342.png)](https://substackcdn.com/image/fetch/$s_!Rx_0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca01131c-79e2-483d-8b44-c60aa4281be9_1600x342.png)

The project has now been running for three weeks, and it is far more complex than I expected. What makes it a good fit for the methodology is that the optimization target is very clear: minimize the differences between Jekyll’s output and Rustkyll’s. Once the backlog is exhausted, the agents can compare the results, identify mismatches, and create new tasks from them.

[![Image 22](https://substackcdn.com/image/fetch/$s_!O5li!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e702a17-04d8-4ed3-89ef-994e85ad1bdb_1366x882.png)](https://substackcdn.com/image/fetch/$s_!O5li!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e702a17-04d8-4ed3-89ef-994e85ad1bdb_1366x882.png)

Median time over 3 runs, clean builds, no caching with Jekyll and Rustkyll compared. You can check out the full results in [docs/benchmark/results.md](https://github.com/alexeygrigorev/rustkyll/blob/main/docs/benchmark/results.md).

It is still a work in progress, but for the DataTalks.Club website is already much faster, and the visible differences between Jekyll and Rustkyll are now very small.

Here’s a video of the website running on Rustkyll. I recorded it last week, and since then I’ve improved it to roughly 2x the speed shown here:

My role is mostly to check in occasionally, make sure the agents are not idle, and push them forward when needed.

[![Rustkyll comparison showing DOM tree differences across multiple Jekyll sites](https://substackcdn.com/image/fetch/$s_!CDkg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F685b2a05-7a7b-4e32-9500-8ab91434c3cb_1051x676.png)](https://substackcdn.com/image/fetch/$s_!CDkg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F685b2a05-7a7b-4e32-9500-8ab91434c3cb_1051x676.png)

Comparing DOM trees across multiple sites to find differences between Jekyll and Rustkyll output

## 5) Codehive (Coding Orchestrator)

After running several projects using this methodology, I started seeing the same problems repeatedly.

The most common one is that the Claude Code orchestrator stops when it should continue. It can ask “shall we proceed?” and wait for hours, or report that the work is done even though there are still items in its task widget.

[![Claude Code agent stopping and asking for confirmation instead of continuing](https://substackcdn.com/image/fetch/$s_!GCHr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b121337-d4a9-45b8-94e3-6c3b326d90c9_1264x839.jpeg)](https://substackcdn.com/image/fetch/$s_!GCHr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b121337-d4a9-45b8-94e3-6c3b326d90c9_1264x839.jpeg)

Claude Code stopping and waiting for input instead of continuing autonomously

Another limitation is visibility. A subagent can spend an hour doing something, and I have no way to see whether it is making progress or is stuck.

And sometimes the orchestrator ignores the process altogether. Instead of sending a task through PM grooming and QA verification, it launches the SWE directly. I had to notice that and force it back into the intended workflow.

[![Claude Code skipping the process and launching SWE directly without PM grooming or QA verification](https://substackcdn.com/image/fetch/$s_!qO4T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59e84ebb-281c-485a-9801-2dc76a7fe2ad_1522x924.png)](https://substackcdn.com/image/fetch/$s_!qO4T!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59e84ebb-281c-485a-9801-2dc76a7fe2ad_1522x924.png)

Claude Code skipping the process and launching SWE directly without PM grooming or QA verification

On top of that, I started hitting Claude Code usage limits, which made me want a setup where I can switch between tools rather than relying on a single provider.

[![Claude Code plan usage limits showing 100% used, resets in 14 minutes](https://substackcdn.com/image/fetch/$s_!DS3s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57e6bce0-e441-4c42-aed9-a942f098c9bb_1280x228.jpeg)](https://substackcdn.com/image/fetch/$s_!DS3s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57e6bce0-e441-4c42-aed9-a942f098c9bb_1280x228.jpeg)

Claude Code session at 100%, even on a simple task

That is why I started building [Codehive](https://github.com/alexeygrigorev/codehive), a coding orchestrator that follows the methodology outlined in this article but enforces it more rigorously.

[![Image 27](https://substackcdn.com/image/fetch/$s_!uqSe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5dadc81-229b-4230-92e4-d96dac32efd3_1600x875.png)](https://substackcdn.com/image/fetch/$s_!uqSe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5dadc81-229b-4230-92e4-d96dac32efd3_1600x875.png)

Right now, the methodology lives in markdown files, which means the agent can ignore parts of it. What I want instead is an orchestrator in which the pipeline itself is built into the application: PM grooms, SWE implements, QA verifies, PM accepts, and the role responsibilities, grooming process, acceptance criteria, and definition of done are enforced by the tool rather than through prompts.

There are a few things I want Codehive to provide:

* hard-coded methodology instead of prompt-based discipline
* multiple agent backends, including Claude Code, Codex, GitHub Copilot, and Z.ai
* non-blocking workflow, so if one task is waiting for my input, the system continues with others
* visibility into subagents, so I can inspect what they are doing and intervene when needed
* GitHub integration, so new issues automatically enter the task pool

I only started working on it recently. Right now, my main focus is still the AI Shipping Labs website, but eventually I want to invest much more into this project and write about it separately.

[![Summary of Codehive project: 96 issues done, ~2,195 tests across backend, web, mobile](https://substackcdn.com/image/fetch/$s_!Pcgr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a2caf83-6242-4202-84fd-493b60e94779_1600x762.jpeg)](https://substackcdn.com/image/fetch/$s_!Pcgr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a2caf83-6242-4202-84fd-493b60e94779_1600x762.jpeg)

Summary of Codehive project: 96 issues done, ~2,195 tests across backend, web, mobile

## What I’ve Learned

Over the past month, I tried this approach on five different projects, and the main thing I learned is that complex projects benefit a lot from explicit specifications, assigned agent roles, and a defined process. Without those three elements, agents drift, skip steps, and declare things finished too early.

It still requires supervision, and I want to keep reducing my involvement so I only step in when the agents actually need me. That is the direction I am working toward now.

I will write more about this in future articles. If you want to follow along, don’t forget to subscribe.

If you want to learn about building projects with agents, we will also have a course on this as part of the [AI Shipping Labs](https://github.com/AI-Shipping-Labs/website) community.

## What I’ve Been Working On Recently

### 1. Workshop at Data Makers Fest 2026

[![A man with short brown hair and a light jacket is featured prominently next to a workshop outline on implementing agentic search.](https://substackcdn.com/image/fetch/$s_!V-xS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7a973e6-686a-4232-b6a1-0e71abdfe5f0_1200x707.png)](https://www.datamakersfest.com/hands-on-tutorials)

I’ve been preparing a [hands-on workshop](https://www.datamakersfest.com/hands-on-tutorials) for [Data Makers Fest 2026](https://www.datamakersfest.com/) in Porto.

During this session, I’ll show how to go from a simple RAG system to an agentic search workflow. It’s designed to be practical, so you can build the system step by step and leave with a much clearer understanding of how these applications work in practice.

If you’d like to join, you can [use the code DATATALK10 for 10% off](https://tickets.datamakersfest.com/). [Tutorial tickets](https://tickets.datamakersfest.com/tutorials) are available until April 24.

### 2. AI Shipping Labs Launch

[![Image 30](https://substackcdn.com/image/fetch/$s_!bEAt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1493c59d-74ab-4957-a8e6-f737856c9d9a_2192x802.png)](https://luma.com/3b4y49nm)

I’ve also been working on the launch of [AI Shipping Labs](https://aishippinglabs.com/), a new community for people who want to build and ship AI products with more structure, support, and accountability. The idea came from a pattern I keep seeing: many people are learning in a fragmented way, jumping between tools, tutorials, and unfinished projects without a clear system around their progress.

In the [launch session](https://luma.com/3b4y49nm), we’ll explain what AI Shipping Labs is, why we decided to build it, who it’s for, and what happens inside. That includes building sessions, group learning, accountability circles, career support, and mini-courses. If you’ve been learning on your own and want a more structured way to keep moving, this is what we’ve been building for.

### 3. AI Engineering Buildcamp

[![Image 31](https://substackcdn.com/image/fetch/$s_!f-Kf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e1a8c0a-b71c-4fb7-b5ca-476c3ede4e12_2050x888.png)](https://maven.com/alexey-grigorev/from-rag-to-agents)

A lot of my attention has also been devoted to the current [AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) cohort. I’ve refreshed 90% of the content and restructured it.

A few people have been asking about the next cohort of AI Engineering Buildcamp. At the moment, I’m not planning another one right away.

After this April cohort wraps up, I’m taking a break from the course to focus on AI Shipping Labs. So if you’ve been thinking about joining, don’t wait too long. I’m not sure when the next cohort will happen. [Registration is still open](https://maven.com/alexey-grigorev/from-rag-to-agents/3/join), and it closes on April 13.

## 4. New cohort of the AI Agents Email Crash Course

[![Image 32](https://substackcdn.com/image/fetch/$s_!zLwc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79cb3015-4854-4187-81b5-c1ca2d56ad29_1872x798.png)](https://substackcdn.com/image/fetch/$s_!zLwc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79cb3015-4854-4187-81b5-c1ca2d56ad29_1872x798.png)

I started a [new cohort of the AI Agents Email Crash Course](https://aishippinglabs.com/courses/aihero). It’s a free, structured, project-based way to learn how AI agents work.

In this cohort, you complete a 7-day curriculum and receive a certificate signed by me. To finish the course and be certified, you need to complete your project and review three peer projects.

## Tools

[![Image 33](https://substackcdn.com/image/fetch/$s_!CxSa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe5d447c-da58-4c7e-a6a8-e948bfbb2de6_1764x1082.png)](https://substackcdn.com/image/fetch/$s_!CxSa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe5d447c-da58-4c7e-a6a8-e948bfbb2de6_1764x1082.png)

[Lightpanda Browser](https://github.com/lightpanda-io/browser) is an open-source headless browser built from scratch.

* [Lightpanda Browser](https://github.com/lightpanda-io/browser) is an open-source headless browser built from scratch in Zig, designed specifically for AI agents, web scraping, and automation. It claims 11x faster execution and 9x lower memory usage than headless Chrome, while remaining compatible with Playwright, Puppeteer, and other tools via the Chrome DevTools Protocol. With over 12,000 GitHub stars, it is a promising lightweight alternative for anyone running browser automation at scale without needing graphical rendering
* [QMD](https://github.com/tobi/qmd) is a local-first search engine for Markdown files that combines BM25 keyword search, vector semantic search, and LLM re-ranking - all running on-device. It works as a CLI tool, a Node.js/Bun library, or an MCP server, making it easy to plug into agentic workflows for searching across notes, docs, and meeting transcripts. Similar in spirit to minsearch but designed for Markdown collections, it is especially convenient for giving AI agents fast access to your local knowledge base

## Resource

[![Image 34](https://substackcdn.com/image/fetch/$s_!1hug!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff78cbd04-e5fb-4e43-bf0d-3c91fd587b8a_1024x768.png)](https://substackcdn.com/image/fetch/$s_!1hug!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff78cbd04-e5fb-4e43-bf0d-3c91fd587b8a_1024x768.png)

[Public APIs](https://github.com/public-apis/public-apis) is a community-curated collection of over 1,400 free APIs organized by category, from weather and finance to games and machine learning. With over 400k GitHub stars, it is one of the most popular repositories on the platform. Whether you are building a side project, prototyping a new product, or teaching students how to work with APIs, this list saves hours of searching by putting hundreds of well-documented, freely available endpoints in one place. Could be very useful for projects

[Share](https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software?utm_source=substack&utm_medium=email&utm_content=share&action=share)

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
