---
title: "Building Projects with Agent Teams"
created: 2026-03-14
updated: 2026-03-25
tags: [claude-code, agents, multi-agent, process]
status: draft
---

# Building Projects with Agent Teams

I've been using a specific approach for building applications with Claude Code over the last few weeks. Not simple one-pagers where you just start a session and go, but more complex projects.

## The Approach

For simple things, I can just open a Claude Code session and start working. For complex projects, I do something different. My main Claude Code session becomes an orchestrator that manages a team of agents[^1].

### The Team

Four agents handle the full lifecycle:

- [Product Manager](https://github.com/AI-Shipping-Labs/website/blob/main/.claude/agents/product-manager.md) (PM) - grooms raw tasks into detailed specs with acceptance criteria, and does final acceptance review from the user's perspective
- [Software Engineer](https://github.com/AI-Shipping-Labs/website/blob/main/.claude/agents/software-engineer.md) (SWE) - implements code and writes tests, doesn't commit until the PM accepts
- [Tester](https://github.com/AI-Shipping-Labs/website/blob/main/.claude/agents/tester.md) (QA) - runs all tests, verifies every acceptance criterion with evidence, reports pass/fail
- [On-Call Engineer](https://github.com/AI-Shipping-Labs/website/blob/main/.claude/agents/oncall-engineer.md) - monitors CI/CD after code is pushed, fixes pipeline failures

<figure>
  <img src="../assets/images/community-platform-implementation/agent-roles-renamed.jpg" alt="Agent roles table showing Product Manager, Software Engineer, Tester, and On-Call Engineer">
  <figcaption>The agent roles: PM, Software Engineer, Tester, and On-Call Engineer</figcaption>
</figure>

The orchestrator (the main Claude Code session) is a manager, not an implementer. It launches agents, routes work between them, and commits code only after the PM accepts. It never writes or modifies application code itself.

Everything is defined in markdown files in the repo:

- [`.claude/agents/`](https://github.com/AI-Shipping-Labs/website/tree/main/.claude/agents) - agent definitions
- [`PROCESS.md`](https://github.com/AI-Shipping-Labs/website/blob/main/_docs/PROCESS.md) - the full development process
- [`CLAUDE.md`](https://github.com/AI-Shipping-Labs/website/blob/main/CLAUDE.md) - project-level instructions for Claude Code
- [`execute` skill](https://github.com/AI-Shipping-Labs/website/blob/main/.claude/skills/execute/SKILL.md) - kicks off the whole pipeline

### The Pipeline

Every task goes through the same pipeline:

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/pipeline.svg" alt="Pipeline flowchart: PM grooms, SWE implements, QA verifies (fail loops back to SWE), PM accepts (reject loops back to SWE), then commit">
  <figcaption>The pipeline: every task goes through PM, SWE, QA, and back to PM before commit</figcaption>
</figure>

The PM grooms a raw task into a spec with user stories, acceptance criteria, and test scenarios. The Software Engineer picks it up, writes code and tests. QA runs everything and verifies each acceptance criterion with actual evidence - test output, screenshots, logs. If QA fails it, the Engineer fixes and QA re-verifies. If QA passes, the PM does a final acceptance review from the user's perspective. If the PM rejects, it goes back to the Engineer. Only after the PM accepts does the orchestrator commit[^1].

### Parallel Batches

Two tasks get worked on in parallel. When a batch finishes, the orchestrator pulls the next two from the backlog:

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/batches.svg" alt="Parallel batch processing: two tasks go through PM, SWE, QA, PM accept in parallel, then pull next 2 and repeat">
  <figcaption>Two tasks processed in parallel, then the next batch is pulled from the backlog</figcaption>
</figure>

To keep the loop going, there's always a task that says "when you finish all current tasks, pull the next two issues from the backlog." This creates a self-sustaining loop until the backlog is empty[^1].

<figure>
  <img src="../assets/images/community-platform-implementation/claude-code-task-list.jpg" alt="Claude Code task list with agents running in parallel">
  <figcaption>Task list with agents running in parallel</figcaption>
</figure>

### Task Tracking

I've tried two approaches for tracking tasks:

- GitHub Issues with labels (`needs grooming`, priority, area) - agents comment on issues with detailed reports. Used this for AI Shipping Labs and Data Tasks
- File-based tracking in a `tracker/` folder - the file name encodes the status (`.todo.md` → `.groomed.md` → `.in-progress.md` → `done/`). Used this for Merm, Rustkyll, and Codehive

The file-based approach works well when I don't want to create a GitHub project upfront. I just do `git init`, create a tracker folder, and tell the agents to use it. The file system becomes the issue tracker.

### Grooming and Acceptance

A groomed task must have concrete user stories - not abstract requirements like "page loads correctly" but specific scenarios like "user opens dashboard, clicks New Project, types a path, clicks Create, gets redirected to the project page." Each story has to be specific enough that an engineer can translate it directly into a Playwright test[^1].

"Done" means something different at each stage:

- SWE done: code works, tests pass, lint clean, actual test output included as evidence
- QA done: ran every test, walked through every user story, took screenshots, each criterion marked pass/fail with evidence
- PM done: reviewed every screenshot, verified user stories match the evidence, confirmed "if the user checks this right now, they'll be satisfied"

The key principle: every claim needs evidence. "Tests pass" is not evidence. Actual test output showing results is evidence. "It looks right" is not evidence. A screenshot is evidence[^1].

### No Silent Descoping

If the PM decides something is out of scope, it can't just be dropped. Two rules:

1. Every decision gets logged - what was decided and why
2. Descoped items become new tasks - requirements don't get forgotten, they get deferred[^1]

## AI Shipping Labs Website

My first attempt at this approach was the [AI Shipping Labs](https://github.com/AI-Shipping-Labs/website) community platform. The [full story is in a separate article](ai-shipping-labs/platform-implementation.md)[^1].

I started by gathering requirements through the Telegram bot and ChatGPT, then told Claude Code to turn them into specifications. It created a "specification" folder with 15 files. After reviewing and giving feedback, I said: now turn these specs into tasks. I tried GitHub Projects for task tracking. The initial decomposition wasn't great - tasks were too granular, no acceptance criteria, no clear format. I iterated on the task format until I liked it, then transferred everything to GitHub Issues[^1].

This is where the approach took shape. I started with just a Software Engineer and a Tester, then added the On-Call Engineer and PM roles as I discovered what was missing. Communication happened through GitHub - agents pushed code and left comments on issues. Everyone worked on main, no branches or pull requests - too much overhead during intensive development[^1].

The setup took about 1.5 hours. The agent then worked autonomously through the night and completed most of the tasks[^1].

<figure>
  <img src="../assets/images/community-platform-implementation/claude-code-morning-progress.jpg" alt="Task progress after overnight autonomous work - 46 tasks, 41 completed">
  <figcaption>Morning after: 41 out of 46 tasks completed overnight without intervention</figcaption>
</figure>

## Data Tasks

The second project was a to-do list for DataTalks.Club called [Data Tasks](https://github.com/alexeygrigorev/datatasks). I launched it, looked at what it was doing, and honestly never came back to check properly - I just didn't have time[^1].

I wanted Node.js, everything serverless so I wouldn't have to pay for it, and all data in DynamoDB. I took the same approach: look at the specs, copy the subagents and the process from AI Shipping Labs, and repeat. Different technologies, same methodology[^1].

The project is currently on hold. It seems to work, but it's at a stage where I need to actually use it and give feedback - the agents can't do that part. The idea is to have something completely serverless so it costs nothing to run. I'll get back to it eventually, but right now I don't have the bandwidth[^2].

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/datatasks-dashboard.png" alt="Data Tasks dashboard showing Active Bundles on the left and Today's Tasks on the right">
  <figcaption>Data Tasks dashboard - built entirely by the agent team</figcaption>
</figure>

## Merm (Mermaid Diagrams)

Same approach, one difference - I didn't want to create a project on GitHub. I didn't know if this would even be useful. But I'd already described the problem and decided this was big enough to give to the agents as a background task[^2].

Instead of GitHub Issues, I used the file-based tracker. I created a folder, did `git init`, and said: put all tasks in a "tracker" folder. The file name encodes the status - `.todo.md`, `.groomed.md`, `.in-progress.md`, then moved to a `done/` folder. Same pipeline, no GitHub needed[^2].

My involvement was minimal. I'd check in occasionally, say what I didn't like, describe clear criteria. At the end I also asked for benchmarks to see if it's actually faster[^2].

[Merm](https://github.com/alexeygrigorev/merm) turned out very successful. There were clear acceptance criteria - that diagrams are generated properly. I also looked at them visually because the agent rendered to SVG and PNG but didn't always see details that needed attention. I needed to point out specific things to look at. No miracle happened where it did everything completely without me, but it was a fairly large and successful project[^3].

The agent worked on it for about two or three days total. At some point I said: now that everything's ready, publish it on GitHub. It did. I already have skills for publishing to PyPI, and it handled all of that. I'm actually using it now for generating diagrams - including the ones in this article[^2][^3].

Here are a few examples from the gallery:

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/merm-example-ci-pipeline.svg" alt="CI pipeline diagram with Build, Test, and Deploy stages rendered by Merm">
  <figcaption>CI pipeline with subgraphs for Build, Test, and Deploy stages</figcaption>
</figure>

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/merm-example-sequence.svg" alt="Sequence diagram with three participants, a loop fragment, and notes rendered by Merm">
  <figcaption>Sequence diagram with participants, loops, and notes</figcaption>
</figure>

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/merm-example-state.svg" alt="State diagram with nested states and transitions rendered by Merm">
  <figcaption>State diagram with nested states and transitions</figcaption>
</figure>

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/merm-example-mindmap.svg" alt="Mind map diagram rendered by Merm">
  <figcaption>Mind map</figcaption>
</figure>

## Rustkyll (Jekyll to Rust)

I've had this idea for a long time to rewrite Jekyll. It's a static site generator written in Ruby. For small sites it works great, but when sites grow, it gets slow. Our DataTalks.Club site takes about a minute to build on my computer. I make a change and have to wait a minute to see it, even with incremental builds[^3].

Jekyll also doesn't have all the features I need. Instead of doing a lookup, you have to loop through everything, check if the ID matches, and break. Can't install plugins because of GitHub Pages[^3].

The idea: take Jekyll as is and rewrite it in Rust. The project is called [Rustkyll](https://github.com/alexeygrigorev/rustkyll/). Not by looking at Jekyll source code and translating it - by taking an existing site and saying "I want a Rust engine that generates the same output." I started with the DataTalks.Club site[^3].

I used the same approach. I said: go look at how Merm has its process set up, adapt it for us, I want to use Rust. I didn't have Rust on that machine - it installed Rust. Go figure it out, use this process[^3].

After a day I opened the code. It was very specifically tailored to our site, not generic. So I said: find other Jekyll sites and make it work for those too[^3].

### Out of Memory

When it was doing `cargo build`, I noticed Claude sessions started crashing. I'd open my terminal (remote computer, SSH, all sessions in tmux) and the tmux session was gone. I'd resume the Claude Code session and ask what happened. It didn't know[^3].

I created a separate session and said: investigate. Out of memory. The `cargo` process was eating all the memory, crashing Claude Code, and crashing the tmux session[^3].

I told it to solve this problem. It set up cgroups - I'd never worked with those before. Now the cargo process runs inside a cgroup, and if it crashes, nothing else goes down with it. I've never done native development like this before - always Java, Python, Ruby. This is new territory[^3].

## AI Hero Migration

I also used the same approach through GitHub for migrating the AI Hero course to the new AI Shipping Labs platform. I just shared a link to the existing course and said "migrate this." The agents created a [detailed GitHub issue](https://github.com/AI-Shipping-Labs/website/issues/128) with full specifications - course data, module structure, all seven units with descriptions and homework, acceptance criteria, and Playwright test scenarios. Then they executed the migration on their own[^14][^15].

The course is now live at https://aishippinglabs.com/courses/aihero[^15].

## Agents Slack Off

This isn't something I can fully leave without supervision. Agents slack off. A lot. It's like managing a team of students who aren't getting paid - they're only there because they need course credits. Everything they do is reluctant, through force[^4].

Each role cuts corners in its own way:

- The PM says "this is too complex, let's descope it" and simplifies the task as much as possible
- The Software Engineer leaves things unfinished
- The Tester says "I can't run this, I won't do it"

This is a feature of working with agents. You need to push them, guide them, and organize the process so it's harder for them to cut corners[^4].

<figure>
  <img src="../assets/images/community-platform-implementation/agent-picking-issues.jpg" alt="Agent listing issues with blocking dependencies">
  <figcaption>An agent picking issues from the backlog</figcaption>
</figure>

### The Descoping Problem

With the Rustkyll project, I asked to compile for Linux, Mac, and Windows, for both AMD64 and ARM64. It compiled for all platforms except Windows ARM64 - it just silently dropped that target. When I asked what happened, it turned out the PM had descoped it. There were no logs, so I couldn't even see when or why[^4][^6].

That's what led to the "no silent descoping" rule in the process. I don't have a problem with descoping itself - sometimes a task is too big. But requirements must not be quietly forgotten[^4].

### Checking Under the Hood

You still need to occasionally look under the hood. It cooks on its own mostly fine, but sometimes you need to lift the lid and check[^4].

With the Jekyll project I wanted pixel-perfect matching. I asked the agents to create tasks based on benchmarks comparing the output. After some time I checked the report - it said everything was fine, pixel-perfect match, and the few percent of different pixels were "font rendering artifacts." A few percent of pixels on a large screenshot is thousands of pixels. I looked at it myself and it was clearly not just font rendering[^4].

Same problem with Mermaid diagrams - the output is visual, and agents struggle to evaluate images. We fixed one thing and broke two others. Tests didn't catch it because it's visual, hard to test automatically. I had to write a visual guideline checklist for the agents to follow[^4].

I haven't found a way to fully automate this. It seems very project-dependent. My goal right now is to do as many projects as possible with this methodology. Each project sharpens it. I think after about 10 more projects I'll have a solid system[^4].

## Codehive (Custom Coding Agent)

I applied the same methodology to building my own coding agent called [Codehive](https://github.com/alexeygrigorev/codehive)[^5].

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/codehive-project-summary.jpg" alt="Summary of Codehive project: 96 issues done, ~2,195 tests across backend, web, mobile">
  <figcaption>Codehive project summary - 96 issues, ~2,195 tests across all components</figcaption>
  <!-- Screenshot showing the full scope of the Codehive project: FastAPI backend, React web, Android mobile, TUI, Telegram bot, CLI, and Docker infrastructure -->
</figure>

I haven't tested Codehive yet because I don't have time[^8].

The YOLO loop turned out to be useless. If you run it, it'll do something, but most likely not what you need. The task decomposition approach works better - set a high-level task, decompose it, define specs, then the PM grooms, the Engineer implements, the Tester tests[^5].

### Problems with the Current Setup

The main orchestrator has several problems[^5].

The agent stops for no reason[^7].

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/codehive-agent-stopping.jpg" alt="Claude Code terminal showing agent stopping and user asking why did you stop">
  <figcaption>The orchestrator stops and waits instead of continuing with the next task</figcaption>
</figure>

It also refuses to pick up the next task on its own, even when tasks are explicitly listed in the backlog[^13].

<figure>
  <img src="../assets/images/building-projects-with-agent-teams/agent-refusing-next-tasks.jpg" alt="Claude Code terminal showing agent completing a task and asking if it should proceed instead of automatically picking the next one">
  <figcaption>The agent finishes a task and asks instead of picking the next one</figcaption>
</figure>

And it asks unnecessary questions. In the todo list there's always an item that says "pull next 2" and "add another pull-next-2 item" to create the loop. But sometimes the orchestrator asks "shall we proceed?" Of course we proceed. Why are you asking? That's wasted time, especially when I'm not nearby[^5].

I also can't see what subagents are doing. Sometimes I want to peek inside a subagent. The orchestrator launches one and it does something for 30 minutes or an hour. Is it stuck? Does it need a restart? When I'm at my computer, I want to look and maybe correct the process. Right now I don't have that ability[^5].

### What I Want to Build

I want my own agent that uses Claude as a subagent and runs the whole process. It'd always have a task pool and a todo list. Instead of asking questions when I'm not around, it just takes tasks from the pool and works on them. If it has questions for me, they get written to a separate list. When I have time, I come and answer them. The work itself doesn't depend on the questions - no blocker, the agent can always continue[^5].

I dictated the project vision to ChatGPT while walking outside. It produced a summary. I fed that to the agents and launched the process. I haven't looked at it since - it's cooking. This is probably the most complex project of all because I want a mobile app, a website, a backend, and a Telegram client[^5].

### The Goal

I want to learn to run complex projects with agent teams with minimal intervention. I'm like a CEO in a small startup with several teams. I have many projects and little time for each one. I check in, see what's happening, correct course, and go back to other things[^5].

The ultimate goal for Codehive is to embed all the best practices I've discovered into the application itself - task tracker, todo lists for each session, everything built in. Instead of copying the approach from one project to another, I'd just launch a project inside Codehive and agents follow my methodology automatically. Right now they have too much freedom. I want to constrain it so they actually stick to the process[^11].

## When This Works Best

This specification-driven development process works best when agents can easily get feedback on their own work[^9].

### Ranking the Projects

Out of the five projects, the Jekyll-to-Rust reimplementation works best. I was able to define clear criteria that the agent uses to test itself:

1. Generate a site with Jekyll, generate the same site with our Rust engine, compare the HTML output, and create tasks based on the differences
2. Open a page rendered by Jekyll in a browser, take a screenshot, do the same with our engine, and compare pixel differences[^9]

Both criteria are maximally clear - hard to do anything wrong. I can leave the agent completely alone. I only check in occasionally to remind them about benchmarks, because I want it fast and don't want them to forget about performance[^9].

Reimplementation projects are perfect for this kind of development. A team of agents can set its own tasks, solve them, and verify the results[^9].

<figure>
  <img src="../assets/images/community-platform-implementation/unsupervised-agents-16-hours.jpg" alt="Multiple agents working in parallel on background tasks">
  <figcaption>Agents working autonomously for 16 hours</figcaption>
</figure>

### The Visual Component Challenge

The other projects are harder because they have a visual component, and visual components are harder to evaluate[^10].

Merm is the next best fit. I can give the agent clear criteria for what the output should look like, but it doesn't always work. The agent converts SVG to PNG and inspects it, but TDD works worse here. Sometimes visual regressions happen even though tests pass. I had to write a visual guideline checklist because testing SVG is hard - it's a visual thing but also code, and when you look at the code, you don't necessarily understand how it'll look[^10].

The remaining three projects (AI Shipping Labs, Data Tasks, Codehive) are the hardest because they have both frontend and backend. I haven't been able to get agents to write proper end-to-end tests. I know Playwright exists, but my agents are lazy about writing good tests. Despite telling them how to write tests, they write them poorly, they cut corners. In these projects, I'm the bottleneck - I need to sit down, thoroughly check everything, and that can take half a day or more[^10].

I think I just need to do more projects with this methodology. Each one teaches me something new. Maybe I need to define clear scenarios and have a framework that agents can use to write those scenarios properly[^10].

## The Overall Philosophy

None of these projects require much active time. I occasionally check in, see what's happening, set the direction, and let them continue. The process is still evolving[^3].

The cost is currently zero thanks to the Pro Max subscription, but these projects aren't fast - they take days. The tradeoff works because the required intervention is minimal: check in, give feedback, set new tasks[^3].

## Sources

[^1]: [20260314_082315_AlexeyDTC_msg2918_transcript.txt](../inbox/used/20260314_082315_AlexeyDTC_msg2918_transcript.txt)
[^2]: [20260314_083004_AlexeyDTC_msg2920_transcript.txt](../inbox/used/20260314_083004_AlexeyDTC_msg2920_transcript.txt)
[^3]: [20260314_083813_AlexeyDTC_msg2922_transcript.txt](../inbox/used/20260314_083813_AlexeyDTC_msg2922_transcript.txt)
[^4]: [20260315_101106_AlexeyDTC_msg2934_transcript.txt](../inbox/used/20260315_101106_AlexeyDTC_msg2934_transcript.txt)
[^5]: [20260315_101751_AlexeyDTC_msg2936_transcript.txt](../inbox/used/20260315_101751_AlexeyDTC_msg2936_transcript.txt)
[^6]: [20260315_103325_AlexeyDTC_msg2950_transcript.txt](../inbox/used/20260315_103325_AlexeyDTC_msg2950_transcript.txt)
[^7]: [20260316_072803_AlexeyDTC_msg2956_photo.md](../inbox/used/20260316_072803_AlexeyDTC_msg2956_photo.md)
[^8]: [20260317_104201_AlexeyDTC_msg2972_photo.md](../inbox/used/20260317_104201_AlexeyDTC_msg2972_photo.md)
[^9]: [20260318_103704_AlexeyDTC_msg2978_transcript.txt](../inbox/used/20260318_103704_AlexeyDTC_msg2978_transcript.txt)
[^10]: [20260318_104207_AlexeyDTC_msg2980_transcript.txt](../inbox/used/20260318_104207_AlexeyDTC_msg2980_transcript.txt)
[^11]: [20260318_104313_AlexeyDTC_msg2984_transcript.txt](../inbox/used/20260318_104313_AlexeyDTC_msg2984_transcript.txt)
[^12]: [20260318_105138_AlexeyDTC_msg2990_transcript.txt](../inbox/used/20260318_105138_AlexeyDTC_msg2990_transcript.txt)
[^13]: [20260318_174724_AlexeyDTC_msg3000_photo.md](../inbox/used/20260318_174724_AlexeyDTC_msg3000_photo.md)
[^14]: [20260318_180542_AlexeyDTC_msg3002.md](../inbox/used/20260318_180542_AlexeyDTC_msg3002.md)
[^15]: [20260318_180716_AlexeyDTC_msg3004.md](../inbox/used/20260318_180716_AlexeyDTC_msg3004.md)
