---
title: "Building Projects with Agent Teams"
created: 2026-03-14
updated: 2026-03-14
tags: [claude-code, agents, multi-agent, process]
status: draft
---

# Building Projects with Agent Teams

This is about the approach I have been using over the last few weeks for creating applications with Claude Code. Not simple one-pagers where you just start a session and go, but more complex projects.

## The Approach

For simple things, I can just open a Claude Code session and start working. For complex projects, I use a different approach. My main Claude Code session becomes an orchestrator. It has several agents: a PM for task grooming, a Software Engineer for implementation, and a QA agent for testing[^1].

The process works like this: there is a pool of tasks. Tasks get pulled from the pool. A maximum of two tasks are worked on in parallel. The PM grooms a task - making it as specific as possible. Then the Software Engineer picks it up and works on it. QA checks the result afterwards. QA can send it back if something is wrong, and the Software Engineer has to fix it. When both agree, the PM looks at the task and checks the acceptance criteria - whether the task passes or not. The PM makes the final decision on whether the task is done[^1].

## Project 1: AI Shipping Labs Website

My first attempt at this approach was the Telegram Writing Assistant. But I thought about what the minimal set of agents would be. In the [previous article about the community platform](work-in-progress/community-platform-implementation.md), I described what I ended up with. For that project, I wanted to establish the workflow, and I used GitHub Issues for task tracking[^1].

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

## The Overall Philosophy

None of these projects require much active time. The goal is minimal involvement: occasionally check in, see what is happening, set the direction, confirm the agents are working correctly, and let them continue. The process is still evolving[^3].

Three projects use this approach so far with varying degrees of success. Pymermade is the completed end-to-end example. The Jekyll-to-Rust project is still in progress[^3].

The cost is currently zero thanks to the Pro Max subscription, but these projects are not fast - they take days. The tradeoff works because the required intervention is minimal: check in, give feedback, set new tasks[^3].

## Sources

[^1]: [20260314_082315_AlexeyDTC_msg2918_transcript.txt](../inbox/used/20260314_082315_AlexeyDTC_msg2918_transcript.txt)
[^2]: [20260314_083004_AlexeyDTC_msg2920_transcript.txt](../inbox/used/20260314_083004_AlexeyDTC_msg2920_transcript.txt)
[^3]: [20260314_083813_AlexeyDTC_msg2922_transcript.txt](../inbox/used/20260314_083813_AlexeyDTC_msg2922_transcript.txt)
