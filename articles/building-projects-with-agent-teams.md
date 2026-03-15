---
title: "Building Projects with Agent Teams"
created: 2026-03-14
updated: 2026-03-15
tags: [claude-code, agents, multi-agent, process]
status: draft
---

# Building Projects with Agent Teams

This is about the approach I have been using over the last few weeks for creating applications with Claude Code. Not simple one-pagers where you just start a session and go, but more complex projects.

## The Approach

For simple things, I can just open a Claude Code session and start working. For complex projects, I use a different approach. My main Claude Code session becomes an orchestrator. It has several agents: a PM for task grooming, a Software Engineer for implementation, and a QA agent for testing[^1].

The process works like this: there is a pool of tasks. Tasks get pulled from the pool. A maximum of two tasks are worked on in parallel. The PM grooms a task - making it as specific as possible. Then the Software Engineer picks it up and works on it. QA checks the result afterwards. QA can send it back if something is wrong, and the Software Engineer has to fix it. When both agree, the PM looks at the task and checks the acceptance criteria - whether the task passes or not. The PM makes the final decision on whether the task is done[^1].

## Project 1: AI Shipping Labs Website

My first attempt at this approach was the AI Shipping Labs community platform. For that project, I wanted to establish the workflow. The [full story is in a separate article](work-in-progress/community-platform-implementation.md), but here is the approach I developed there[^1].

I started by gathering requirements through the Telegram bot and ChatGPT, then told Claude Code to turn them into specifications. It created a "specification" folder with 15 files. After reviewing and giving feedback, I said: now turn these specs into tasks. I tried GitHub Projects for task tracking. The initial decomposition was not great - tasks were too granular, no acceptance criteria, no clear format. I iterated on the task format until I liked it, then transferred everything to GitHub Issues[^1].

The architecture that came out of this project: two core subagents - a Software Engineer and a Tester. The Software Engineer implements a feature, then the Tester checks it. They iterate until both agree the task is done. An orchestrator (manager) coordinates them - it has no biased relationship with the code. If everything ran in one session, the tester might say "it is fine" and do nothing. With separate subagents, the orchestrator passes feedback back and forth[^1].

I also added an On-Call Engineer subagent to monitor CI/CD. If something breaks after a push, this agent finds who is responsible, opens an issue, and tries to fix it. Later I added a Product Manager role for grooming tasks, writing issues with clear requirements, and having the final say in acceptance[^1].

The orchestrator looks at the task pool, pulls two tasks, launches Software Engineers and Testers for each. When it finishes, it pulls the next two. I added a trick to keep the loop going: a task that says "when you finish all current tasks, pull the next two issues from the backlog." This creates a self-sustaining loop until the backlog is empty[^1].

Communication happens through GitHub - agents push code and leave comments on issues. I chose not to use branches and pull requests because it would be too much overhead during intensive development. Everyone works on main. The setup took about 1.5 hours. The agent then worked autonomously through the night and completed most of the tasks[^1].

## Project 2: Data Tasks

The second project was a to-do list for our DataTalks Club called Data Tasks. I honestly launched it, looked at what it was doing, and never came back to check properly - I just did not have time. For this project I decided I wanted to use Node.js, I wanted everything to be serverless so I would not have to pay for it, and all data in DynamoDB. The technologies were DynamoDB and Lambda[^1].

I took the same approach. I said: look at the specs in the Telegram assistant brain dump about how this site should work, copy the subagents and the process from AI Shipping Labs, and let us repeat. It did the same thing. The approach was about using serverless - different technologies, same approach[^1].

The status of Data Tasks: I do not have time to work on it right now. It seems to work, but it is at a stage where I need to actually use it and give feedback. The agents cannot do that part. I use it, try things, say what to do next, and then the agents create tasks for themselves and execute. I do not have time for that right now[^2].

## Project 3: Pymermade (Mermaid Diagrams)

The next project I want to talk about is Mermaid diagrams. The approach was exactly the same, with one difference - I did not want to create a project on GitHub. I did not know if this would even be useful, if anything would come out of it. But I had already described the problem I had. I decided this was a big enough project. I was interested in doing it as a background task - just giving it to the agents because the task was fairly clear. The diagrams had already been generated[^2].

Instead of creating a GitHub repo, I just created a folder, did `git init` to have an empty project, and said: instead of GitHub Issues, put all tasks in a folder. I think I called it "tracker." The file name contained the status - like new task, groomed, in progress, done. So new task goes to groomed, then to in progress, then to done. The file system became the issue tracker. The same process otherwise[^2].

I said: I want to make Mermaid diagrams. Then after some time I checked, gave a bit of feedback about what I did not like. Then after some more time I looked at the files again, said what I did not like, described clear criteria. My involvement was minimal. At the end I also asked to run benchmarks to actually compare whether it is faster or not[^2].

The experience with Pymermade (I think I just called it "mate") turned out very successful. It really worked out and produced what was needed. There were clear acceptance criteria - that diagrams are generated properly. I also looked at them visually because the agent rendered to SVG and PNG but did not always see details that needed attention. I needed to point out specific things to look at. So my input was still required - no miracle happened where it did everything completely without me. But it was a fairly large and successful project[^3].

The agent worked on it for about two or three days total. My involvement was minimal. I just occasionally checked what it was doing, gave feedback, set some new tasks like running benchmarks. At some point during the process I said: now that everything is ready, publish it on GitHub. It did. We found a suitable name for the project because I originally wanted to call it "pymermaid" but that was already taken, so I had to experiment with the name a bit. I already have skills for publishing to PyPI, and it did all of that[^2].

I am actually using it now for generating diagrams[^3].

## Project 4: Jekyll to Rust

The last thing I did - I have had this idea for a long time to rewrite Jekyll. Jekyll is a static site generator written in Ruby. For small sites it works great. When sites grow, it gets slow. Our DataTalks Club site takes about a minute to build on my computer. I make a change and have to wait a minute to see it, even with incremental builds enabled[^3].

I have been thinking about rewriting this to something faster for a long time. Plus Jekyll does not have all the features I need. For example, instead of doing a lookup, you have to do a loop, check if the ID matches, and then break. That is just a Jekyll limitation. Cannot install plugins because of GitHub Pages[^3].

The idea right now is: let us just take Jekyll as is and rewrite it in Rust. I am not saying go look at Jekyll source code and write the same thing in Rust. I am saying: here is a site, it needs to work. I initially took the DataTalks Club site and said I want a Rust engine that generates the same output as Jekyll[^3].

I used the same approach. I said: go look at how Pymermade has its process set up, adapt it for us, I want to use Rust. I did not have Rust on that machine - it installed Rust. I want to use Rust, go figure it out, use this process[^3].

After a day I opened the code and looked at what was there. The code was very specifically tailored to our site - not generic. I said: now here is your task - find other Jekyll sites and make it work for those too[^3].

It is currently in progress. I do not know how it will end. I recently opened it, looked at what was happening. I do not understand Rust, so it is hard for me to quickly understand what is going on like I would with Python. But I was not really trying either - I just looked, it seemed OK, and I let it keep working[^3].

### Out of Memory Issues

One thing that happened: when it was doing `cargo build` or similar (Cargo is the build tool in Rust), I noticed Claude sessions started crashing. I would open my terminal - I have a remote computer, I connect via SSH, all sessions in tmux - and the tmux session was gone. I would open a new terminal, resume the Claude Code session, ask what happened, why it crashed. It did not know[^3].

Then I saw it crash again. I created a separate Claude Code session and said: investigate. Out of memory. The `cargo` process was eating all the memory, crashing Claude Code, and crashing the tmux session[^3].

I told it to solve this problem. It set up cgroups - I had never worked with those before. Now it runs the cargo process inside a cgroup, and if it crashes, nothing else crashes[^3].

For me this is all fairly new territory. I have never done this kind of native development. I always had Java, Python, Ruby - languages that are not native. I wrote a little C once, but nothing serious. This is my first experience like this, and I am discovering new things like cgroups[^3].

## Agents Slack Off

This is not something I can fully leave without supervision. Agents slack off. A lot. It is like managing a team of students who are not getting paid. They are only there because they need course credits. Everything they do is reluctant, through force. Sometimes they work, sometimes they slack off terribly. This applies to all agents[^4].

Take the three agents - PM, Software Engineer, and Tester. The PM can say "this is too complex, let us descope it" and starts simplifying the task as much as possible. The Software Engineer can leave things unfinished. The Tester can say "I cannot run this, I will not do it." You need to understand that this is a feature of working with agents - they slack off, they do things reluctantly, you need to push them, guide them, and organize the process so it is harder for them to cut corners[^4].

### The Descoping Problem

The PM is supposed to properly scope the issue - define clearly what goes in, what the acceptance criteria are. But here is what actually happened[^4].

With the Rust project, I have a Windows tablet with ARM64 architecture. I said: make it compile for Mac, Windows, and Linux on both AMD64 and ARM64. That requirement just disappeared. The PM descoped it and it was not preserved anywhere. There were no logs at that point, so I had no way to even see when or why it was dropped[^4].

That is when I added the first rule: start keeping a log. Every time a decision is made, write it in the log - what the decision is and why. But even with logging in place, I started noticing the PM would say "this is out of scope" and silently drop the feature anyway. So I added another rule: if you decide to descope something from the task, do not silently drop it - always create a new task for it[^4].

I have no problem with descoping itself. Sometimes a task is too big and some things genuinely do not belong in its scope. That is normal. But they must not be quietly forgotten. When I have a requirement, I do not care whether it gets implemented in this task or some time later. The important thing is that it is preserved somewhere. Now I have logs being kept and a process, so at least there is a trail[^4].

### Checking Under the Hood

You still need to occasionally look under the hood, stir the pot. It cooks on its own mostly fine, but sometimes you need to lift the lid, check, and give directions. For instance, with the Jekyll project I wanted pixel-perfect matching. I asked the agents to create tasks based on benchmarks comparing the output. After some time I checked the report - it said everything was fine, there was a pixel-perfect match, and the few percent of different pixels were just "font rendering artifacts." A few percent of pixels on a large screenshot is thousands of pixels. I looked at it myself and it was clearly not just font rendering[^4].

The same problem with Mermaid diagrams - the output is visual, and agents struggle to evaluate images. There are no clear criteria they can check automatically. I told them: let us make a visual checklist, because we fixed one thing and broke two others. Why did tests not catch this? Because it is a visual thing, hard to test automatically[^4].

I have not found a way to fully automate this so my involvement is minimal. It seems very project-dependent - one project needs one kind of oversight, another needs something different. My goal right now is to do as many projects as possible with this methodology. Each project sharpens it. I am learning how to approach this, understanding the limitations, and refining the methodology. I think after about 10 more projects I will have a solid system for how to approach this[^4].

## Project 5: Custom Coding Agent

I applied the same methodology to another project - building my own coding agent. There are things in Claude Code that I do not like[^5].

The YOLO loop turned out to be useless. If you run it, it will do something, but most likely not what you need. The task decomposition approach works better - I set a high-level task, we decompose it, define a plan, define specs, then the PM grooms them, the Engineer implements, the Tester tests. That approach works OK[^5].

### Problems with the Current Setup

The main orchestrator (the main Claude Code session) has several problems[^5].

The first problem: it asks stupid questions. The way it works now - I say there is a pool of tasks, and the orchestrator should ask the PM to pick the next two issues from the backlog. In the todo list there is always an item that says "pull next 2" and also "add another pull-next-2 item" to create the loop. But sometimes the orchestrator asks things like "shall we proceed?" Of course we proceed. Why are you asking? That is wasted time, especially when I am not nearby[^5].

The second problem: I cannot see what subagents are doing. Sometimes I want to peek inside a subagent and just look at what is happening. Right now there is no such ability. The orchestrator launches a subagent and it does something for 30 minutes or an hour. Is it stuck? Does it need a restart? When I am at my computer, I want to look and maybe correct the process - "no, do it differently, that is not what I want." Right now I do not have that ability[^5].

### What I Want to Build

I want my own agent that uses Claude as a subagent and starts this whole process. It would always have a task pool, a todo list. Instead of asking stupid questions when I am not around, it just takes tasks from the pool and works on them. If it has questions for me, those questions get written to a separate list. When I have time, I come and answer them. The work itself does not depend on the questions - there is no blocker, the agent can always continue working. I just need to occasionally check that nothing went wrong[^5].

I want the application to have a separate place for questions to the user, an always-available todo list where agents can pull tasks from, and the ability to peek inside subagents[^5].

I dictated the project vision to ChatGPT while walking outside. It produced a summary. I already had the approach described, so I fed that summary to the agents and launched the process. I have not looked at it since - it is cooking in the pot. This is probably the most complex project of all I have tried because I want a mobile app, a website, a backend, and a Telegram client[^5].

### The Goal

My goal is to learn to run complex projects with agent teams with minimal intervention. I am like a CEO or VP of Product in a small startup with several teams. I have many projects and little time for each one. I just occasionally check in, see what is happening, correct course, and go back to other things. I want to build a process where this works[^5].

## The Overall Philosophy

None of these projects require much active time. The goal is minimal involvement: occasionally check in, see what is happening, set the direction, confirm the agents are working correctly, and let them continue. The process is still evolving[^3].

The cost is currently zero thanks to the Pro Max subscription, but these projects are not fast - they take days. The tradeoff works because the required intervention is minimal: check in, give feedback, set new tasks[^3].

## Sources

[^1]: [20260314_082315_AlexeyDTC_msg2918_transcript.txt](../inbox/used/20260314_082315_AlexeyDTC_msg2918_transcript.txt)
[^2]: [20260314_083004_AlexeyDTC_msg2920_transcript.txt](../inbox/used/20260314_083004_AlexeyDTC_msg2920_transcript.txt)
[^3]: [20260314_083813_AlexeyDTC_msg2922_transcript.txt](../inbox/used/20260314_083813_AlexeyDTC_msg2922_transcript.txt)
[^4]: [20260315_101106_AlexeyDTC_msg2934_transcript.txt](../inbox/used/20260315_101106_AlexeyDTC_msg2934_transcript.txt)
[^5]: [20260315_101751_AlexeyDTC_msg2936_transcript.txt](../inbox/used/20260315_101751_AlexeyDTC_msg2936_transcript.txt)
