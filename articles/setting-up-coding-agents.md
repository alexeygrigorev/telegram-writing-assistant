---
title: "Setting Up Your Coding Agents"
created: 2026-06-04
updated: 2026-06-05
tags: [claude-code, codex, opencode, coding-agents, setup]
status: draft
---

# Setting Up Your Coding Agents

There is no shortage of getting-started material for coding agents.

Anthropic ships a free [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) course and full [docs](https://code.claude.com/docs/en/overview). OpenAI has a [Codex Quickstart](https://developers.openai.com/codex/quickstart).

However, people continue asking me over and over again how to get started with coding assistants. I'm usually puzzled when I hear it. To me it's obvious: you just install it and start using it.

But when I think about it, I realize that it's not the real question that people ask. What they ask is probably closer to "How do I configure Claude Code properly with the right model and the right permissions, and use all the slash commands, skills, subagents, plugins and the MCP servers? Should I run it locally or in Docker or remotely? How do I configure it to run on my phone? And what about all these tricks that people post on X every day, like the Ralph loop, or running a team of agents? Show me exactly which buttons to press and in which order."

And that's a very different question. 

I understand where this is coming from. Open X and you see an endless stream of people sharing what they built and the tricks they used. I also realize that I contribute to that stream with this newsletter.

Of course, this creates FOMO and the desire to know everything before you even start.

## Choosing where to start

In this article I want to show a sipmple "from zero to hero" path. The main idea is that you don't need to know everything at once - or you risk getting even more confused.

Instead, start simple, and use AI to solve the actual problems you have. Over time you will discover the workflow that fits you.

So this article is not a catalog of everything that exists, but a path you can actually follow.

This path is:

1. pick an assistant
2. start using it directly, without any extra setup
3. document your processes
4. turn repetitive tasks into skills
5. use subagents for context-heavy tasks

Work through them in order, and don't move on until the current step feels natural. That gives you all the foundation you need to be productive with AI assistants[^7].

## Step 1: Choose an assistant

There are many AI coding assistants:

- Claude Code
- Codex
- OpenCode
- GitHub Copilot
- Antigravity
- Cline

The first step is picking one of these tools and start using it. 

Previously I'd recommend GitHub Copilot as the first tool: for $10 you could get quite far, but that is no longer the case[^7]. With Antigravity's free plan you could also do a lot but not anymore.

<figure>
  <img src="../assets/images/setting-up-coding-agents/copilot-cost.png" alt="Headlines about GitHub Copilot's switch from a flat-rate plan to token-based billing: 'What a joke: GitHub Copilot's new token-based billing spurs consternation among devs' (TechCrunch), 'GitHub Copilot Pricing Change Drives Backlash: Agentic Bills Jump 10x to 50x for Power Users' (Tech Times), and 'Microsoft's GitHub shifts to metered AI billing amid cost crisis' (The Register)">
  <figcaption>GitHub Copilot's shift from a flat ten-dollar plan to token-based billing - bills jumping 50x</figcaption>
</figure>


Right now you can get the best value with the $20/month ChatGPT Plus subscription: Codex is included.

OpenCode is another decent place to start.

With Anthropic, the $20 plan won't get you far - you hit the limits quickly. For Claude, you'd need to start from the $100 one.

The tools are different, and I cannot say that one is clearly better than another, so at first just pick the one that fits your budget[^7].

## Step 2: Solve a task with the assistant

After selecting a coding agent, start using it. 

Start as simply as possible. Give the agent a task you can do end-to-end and then check:

- write a Python or bash script
- solve homework from a course
- a mini-project like the snake game we did in [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)
- any small problem you have

You don't need MCPs, skills, or subagents. Not yet.

The goal at this stage is to see that the agent can actually solve many of your problems, and understand how exactly you can use it. 


## Permissions

When you start, the agent asks for permission on every action.

It gets annoying fast. So you either start building a white list of allowed actions (when agent prompts you for approval, you say "Yes and don't ask me again for this action")

Or you run it in the skip-permissions/YOLO mode.

You have to understand the risks: the agent can execute any command on your computer. But sometimes speed matters more than control: you want to hand the agent a task for the night and walk away without having to approve every single action[^10].

I run agents on most of my projects run in this mode. 

Only for serios tasks I use the white list approach. For example, when I need to set up infra for the productio environment. If I need to do something like Terraform, I never use YOLO mode[^11].

There is no universal rule. It depends on how much you want to be in control and how much the result matters to you. In YOLO mode the agent works faster, but if it decides to delete something, it will[^12].

## Use agents for automation, not only coding

I had been using agents for coding for more than a year. And they have been very useful

But only when I started using them for automating tasks, I undestood how valuable they are.[^14].

For example, right now I'm preparing the videos for LLM Zoomcamp.

I need download the videos from YouTube, cut them into separate chunks, and upload them back to YouTube separately. On top of that, I want these videos to have timecodes, so I download the subtitles and turn them into chapters. 

I can delegate most of it to Claude. I only need to check that the cuts are clean, bulk-upload the videos (it's problematic with YouTube API), and then hit save so it goes from draft to "published" (there's no API call for that too). 

The rest is on Clade: it can see the videos I uploaded, then it pulls their IDs, updates the title and the description, adds timecodes, puts them into the playlist in the right order. [^14][^42]

This saves a lot of time.

Picture: screenshot of youtube playlist

The flow is very simple. I described to Claude what I exactly I needed and pointed to the location with the uncut videos. It fetched the tracripts and cut the videos using ffmpeg, and then described what I need to do to set the API access to YouTube. Then I checked the cuts and uploaded the videos. That was it. 

Last year I started automating many things in my workflow.

- Creating homework submission forms for https://courses.datatalks.club/
- Creating github repositories 
- Publishing new versions of libraries I maintain 
- 

If there's an API for a service or a command line tool, AI agents can figure out how to use them and automate your work using only the terminal. 

[^16].


## Step 3: Document your processes

Once you figure out how to automate something, the next step is to document it. 

Especially when you know that you're going to need this again. 

Usually I interact with the assistant until the task is done, and at the end I ask it to document everything to a markdown file. For LLM Zoomcamp the process is [here](https://github.com/DataTalksClub/llm-zoomcamp/tree/8c1834d114754cc0e0d65544b8589ef7d94b81cf/docs
) 

Then you can do it again and just point the agent to this documentation. 

When I needed to add more videos to the LLM Zoomcamp playlist, that's exactly what I did.

<figure>
  <img src="../assets/images/setting-up-coding-agents/youtube-playlist-automation.jpg" alt="Terminal prompt asking the agent to pull module 3 videos from a playlist into the course playlist, pointing it at the docs for the YouTube API">
  <figcaption>Automating YouTube playlist management - the agent is told to pull the module videos and place them in the course playlist at the right spot, pointed at the docs for the API</figcaption>
</figure>


If you don't document it, the agent will have to start from stract and spend time (and tokens) to figure out how to solve the problem again.

For YouTube videos it might not be a big problem because there's a lot of information online about it so the agent already knows many things.

But for other things it doesn't have all the right context. For example, I use agents to publish the homework to https://courses.datatalks.club/. 

In this case the agent needs to know:

- What's the URL for the production website
- Where's the API key
- What's available in the API 
- How exactly the payload shold look like 
- What to do when things go wrong 

If you don't document it, you'll have to explain the agent what to do every single time you ask it to help you. 

## Step 4: Turn repetitive tasks into skills

Once you have a document, you can turn it into a skill.

A skill is md document saved in a specific location with a specific name... TODO more 

todo add links that describe skills  

example: 

```markdown
---
name: course-content
description: Manage courses, homeworks, and projects via REST API
---

# Course Content API

## Overview

This skill provides commands to manage courses, homeworks, and projects via the REST API. Supports list, create, update state/dates/description, and guarded delete.
```
from here https://raw.githubusercontent.com/alexeygrigorev/course-management-agent/refs/heads/master/.claude/skills/course-content/SKILL.md

This skill needs to be in `.claude/skills/<SKILL-NAME>/SKILL.md` (for codex it's `.codex`)

The only required part is name and description. that's it. 



Once you put the md doc in that location, the agent can pick them up automatically.

With a skill in place I can throw the request at Claude as is - "here is the homework, upload it" - and the agent recognizes which skill fits, loads it, and does the rest. Otherwise I'd have to point to the docs every single time I ask the assitant to help with it.

You don't actually need to write the skills by hand and figure out the locatins and the format. What you can do is

- Ask the agent to document the process
- Then ask it to save it as a skill


Both Claude Code and Codex ship a built-in skill for making skills, so they can easity take your docs and put them in the correct place so it becomes the skill.[^18].

If you're wondering if you should make something a skill or not, don't overthing it. I'd suggest to always document what you do at the end of each coding session, and if you need to come back to this documentation repeatedly, turn it into a skill. 

For a more structured take, Anthropic recently published [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills).


## Step 5: Use subagents

As you work with an agent, every question and answer accumulates in its context. Eventually the context fills up and quality drops[^21][^22].

I first realized how useful subagets are when setting up the telegram writing assistnat (TODO substack link)

This is how it works:

- I send it a lot of content like voice notes, text messages, links and videos
- I execute /process from telegram when I want claude to turn this pile into articles

The /process command is a [skill](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/process/process.md) which describes how exactly to turn the input into articles.

However with time I started asking it to do some context-heavy tasks:

- fetch a youtube transcript and summarize it
- explore a github repository and explain how it works
- do research on a certain topic


Imagine I send this:

- ten voice notes about my ideas that need to be arranged into 2-3 articles
- a tweet I liked that I want to save
- a three-hours long youtube video that I want to summarize 

I execute /process and the agent needs to put all these things together in the same context.
The three-hour transcript will pollute everything the model has been working on. The article it was drafting gets worse, the summary comes out poorly, and there is no clean way to continue afterward[^23][^24][^25].


One way of solving it would be to first process the simple things and once they are done, we can launch a separate session for the youtube video. 

But instead, the main agent  can launch a separate subagent for the heavy task. It will have specific instructions "summarize this transcript", run in its own context, save the result, and report back when the work is done. The main agent only sees "started" and "finished", so its context stays clean[^25].

Another benefit of running subagents is parallelism. The main agent (the orchestrator) can launch several subagents at once - one writing the article, another summarizing the video - and stitch their results together when they finish[^26].

## The path from zero to hero

That covers the essentials: start using the agent, turn repeated tasks into skills, and reach for subagents when context becomes a problem. If you go through these steps in order, you can already do almost anything with it. The order matters - if you start with subagents, you may never figure out the simpler pieces[^27].

There are a couple more tricks worth mentioning before the end.

## Project context files (CLAUDE.md and AGENTS.md)

In your own projects you should always create a CLAUDE.md (read by Claude Code) and an AGENTS.md (read by Codex and OpenCode). The agent reads these every time it starts - that is where the description of the project lives and the things the agent needs to know. It saves you from explaining the project from scratch each session, and it saves the agent from crawling through the whole repository to figure things out[^28].

## Reset (or new) to keep the context clean

The subcommand I use most often is the one that resets the session - called `reset` or `new` depending on the agent. Every new task starts with a clean context, so only what is important lands in it. This is exactly where a good CLAUDE.md or AGENTS.md matters: it makes starting from a clean slate painless[^28].

## Goal: keep the agent working until it is done

The other command I use actively right now is `goal`. You give the agent a completion condition in plain language - "all tests pass and the lint step is clean" - and it keeps starting new turns on its own until the condition is met. It is the productized version of the Ralph Loop: a loop that feeds the same prompt to a fresh agent over and over, with progress accumulating in files and git history rather than in the model's context[^28][^29].

Codex shipped it first. Claude Code added a near-identical version shortly after, with a separate small evaluator model that checks after each turn whether the condition is satisfied and, if not, sends back guidance and starts another turn. It pairs well with skip-permissions mode so each turn runs without approval prompts. Official references: [Claude Code goal docs](https://code.claude.com/docs/en/goal) and [Codex follow-goals docs](https://developers.openai.com/codex/use-cases/follow-goals). This used to require a plugin in Claude Code, but now it is built in[^29][^35].

The one real caveat is cost and runaway risk. Each turn costs two model calls (the main turn plus the validator), and there is no hard spending cap by default. Phrase the end state as something binary and machine-checkable, name the verification command explicitly, and bake a turn limit into the condition[^29].

Beyond `reset` and `goal`, I do not use any other subcommands[^30].

## My setup: the .claude dotfiles repo

To make this concrete, my own setup lives in a public repository: [github.com/alexeygrigorev/.claude](https://github.com/alexeygrigorev/.claude). Despite the name, it bootstraps and configures all three agents from one shared clone, so every machine and every assistant ends up with the same setup[^31][^32].

The structure:

- An installer script clones the repo and a configure script wires everything into the right home-directory locations. The configure step takes a target (claude, codex, opencode, or all).
- A `config/` folder holds per-assistant settings: `settings.json` for Claude and OpenCode, `config.toml` for Codex.
- A `skills/` folder holds the shared skills, symlinked into each assistant so all three share them. Examples: create-github-repo, fetch-youtube, fetch-loom, fetch-google-recorder, init-library, jina-reader, openai-transcribe, regular-ping, release, setup-pypi-ci, stylint.
- A shared `.bashrc` is sourced from the repo, so a git pull propagates new aliases and functions. It defines the short aliases I use daily - `c` for claude, `cc` for continue-session, `csp` for claude with skip-permissions, `cy` for codex in bypass mode, and an `oc` function for OpenCode.

The repo also encodes the safety guardrails I mentioned in the permissions section. The Claude settings register a PreToolUse hook that blocks dangerous commands (`rm -rf /`, force pushes, dropping a database, `terraform apply`) unless confirmed. The `oc` function strips a denylist of provider API-key environment variables before launching, so leaked credentials never reach the agent[^31].

## Sources

[^1]: [20260604_145544_AlexeyDTC_msg4359_transcript.txt](../inbox/used/20260604_145544_AlexeyDTC_msg4359_transcript.txt)
[^2]: [20260604_145558_AlexeyDTC_msg4361_transcript.txt](../inbox/used/20260604_145558_AlexeyDTC_msg4361_transcript.txt)
[^3]: [20260604_145702_AlexeyDTC_msg4363_transcript.txt](../inbox/used/20260604_145702_AlexeyDTC_msg4363_transcript.txt)
[^4]: [20260604_154535_AlexeyDTC_msg4369_photo.md](../inbox/used/20260604_154535_AlexeyDTC_msg4369_photo.md)
[^5]: [20260604_154535_AlexeyDTC_msg4370_photo.md](../inbox/used/20260604_154535_AlexeyDTC_msg4370_photo.md)
[^6]: [20260604_154536_AlexeyDTC_msg4371_transcript.txt](../inbox/used/20260604_154536_AlexeyDTC_msg4371_transcript.txt)
[^7]: [20260604_155257_AlexeyDTC_msg4375_transcript.txt](../inbox/used/20260604_155257_AlexeyDTC_msg4375_transcript.txt)
[^8]: [20260604_155424_AlexeyDTC_msg4377_transcript.txt](../inbox/used/20260604_155424_AlexeyDTC_msg4377_transcript.txt)
[^9]: [20260604_155513_AlexeyDTC_msg4379_transcript.txt](../inbox/used/20260604_155513_AlexeyDTC_msg4379_transcript.txt)
[^10]: [20260604_160026_AlexeyDTC_msg4381_transcript.txt](../inbox/used/20260604_160026_AlexeyDTC_msg4381_transcript.txt)
[^11]: [20260604_160117_AlexeyDTC_msg4383_transcript.txt](../inbox/used/20260604_160117_AlexeyDTC_msg4383_transcript.txt)
[^12]: [20260604_160204_AlexeyDTC_msg4385_transcript.txt](../inbox/used/20260604_160204_AlexeyDTC_msg4385_transcript.txt)
[^13]: [20260604_160325_AlexeyDTC_msg4387_transcript.txt](../inbox/used/20260604_160325_AlexeyDTC_msg4387_transcript.txt)
[^14]: [20260604_160723_AlexeyDTC_msg4389_transcript.txt](../inbox/used/20260604_160723_AlexeyDTC_msg4389_transcript.txt)
[^15]: [20260604_160940_AlexeyDTC_msg4391_transcript.txt](../inbox/used/20260604_160940_AlexeyDTC_msg4391_transcript.txt)
[^16]: [20260604_161327_AlexeyDTC_msg4393_transcript.txt](../inbox/used/20260604_161327_AlexeyDTC_msg4393_transcript.txt)
[^17]: [20260604_161537_AlexeyDTC_msg4395_transcript.txt](../inbox/used/20260604_161537_AlexeyDTC_msg4395_transcript.txt)
[^18]: [20260604_161907_AlexeyDTC_msg4397_transcript.txt](../inbox/used/20260604_161907_AlexeyDTC_msg4397_transcript.txt)
[^19]: [20260604_162008_AlexeyDTC_msg4399_transcript.txt](../inbox/used/20260604_162008_AlexeyDTC_msg4399_transcript.txt)
[^20]: [20260604_162037_AlexeyDTC_msg4401_transcript.txt](../inbox/used/20260604_162037_AlexeyDTC_msg4401_transcript.txt)
[^21]: [20260604_162151_AlexeyDTC_msg4403_transcript.txt](../inbox/used/20260604_162151_AlexeyDTC_msg4403_transcript.txt)
[^22]: [20260604_162254_AlexeyDTC_msg4405_transcript.txt](../inbox/used/20260604_162254_AlexeyDTC_msg4405_transcript.txt)
[^23]: [20260604_163158_AlexeyDTC_msg4407_transcript.txt](../inbox/used/20260604_163158_AlexeyDTC_msg4407_transcript.txt)
[^24]: [20260604_163639_AlexeyDTC_msg4409_transcript.txt](../inbox/used/20260604_163639_AlexeyDTC_msg4409_transcript.txt)
[^25]: [20260604_163843_AlexeyDTC_msg4411_transcript.txt](../inbox/used/20260604_163843_AlexeyDTC_msg4411_transcript.txt)
[^26]: [20260604_164159_AlexeyDTC_msg4413_transcript.txt](../inbox/used/20260604_164159_AlexeyDTC_msg4413_transcript.txt)
[^27]: [20260604_164402_AlexeyDTC_msg4415_transcript.txt](../inbox/used/20260604_164402_AlexeyDTC_msg4415_transcript.txt)
[^28]: [20260604_212206_AlexeyDTC_msg4421_transcript.txt](../inbox/used/20260604_212206_AlexeyDTC_msg4421_transcript.txt)
[^29]: [20260604_212216_AlexeyDTC_msg4423_transcript.txt](../inbox/used/20260604_212216_AlexeyDTC_msg4423_transcript.txt)
[^30]: [20260604_212249_AlexeyDTC_msg4425_transcript.txt](../inbox/used/20260604_212249_AlexeyDTC_msg4425_transcript.txt)
[^31]: [20260604_212310_AlexeyDTC_msg4427_transcript.txt](../inbox/used/20260604_212310_AlexeyDTC_msg4427_transcript.txt)
[^32]: [20260604_212340_AlexeyDTC_msg4429.md](../inbox/used/20260604_212340_AlexeyDTC_msg4429.md)
[^33]: [20260604_212423_AlexeyDTC_msg4431_transcript.txt](../inbox/used/20260604_212423_AlexeyDTC_msg4431_transcript.txt)
[^34]: [20260604_213015_AlexeyDTC_msg4436_transcript.txt](../inbox/used/20260604_213015_AlexeyDTC_msg4436_transcript.txt)
[^35]: [20260604_213120_AlexeyDTC_msg4437_transcript.txt](../inbox/used/20260604_213120_AlexeyDTC_msg4437_transcript.txt)
[^36]: [20260605_040543_AlexeyDTC_msg4441.md](../inbox/used/20260605_040543_AlexeyDTC_msg4441.md)
[^37]: [20260605_040700_AlexeyDTC_msg4443_transcript.txt](../inbox/used/20260605_040700_AlexeyDTC_msg4443_transcript.txt)
[^38]: [20260605_040737_AlexeyDTC_msg4445_transcript.txt](../inbox/used/20260605_040737_AlexeyDTC_msg4445_transcript.txt)
[^39]: [20260605_052456_AlexeyDTC_msg4451.md](../inbox/used/20260605_052456_AlexeyDTC_msg4451.md)
[^40]: [20260605_052621_AlexeyDTC_msg4452.md](../inbox/used/20260605_052621_AlexeyDTC_msg4452.md)
[^41]: [20260605_052657_AlexeyDTC_msg4453.md](../inbox/used/20260605_052657_AlexeyDTC_msg4453.md)
[^42]: [20260605_052249_AlexeyDTC_msg4450_photo.md](../inbox/used/20260605_052249_AlexeyDTC_msg4450_photo.md)
