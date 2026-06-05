---
title: "Setting Up Your Coding Agents"
created: 2026-06-04
updated: 2026-06-05
tags: [claude-code, codex, opencode, coding-agents, setup]
status: draft
---

# Setting Up Your Coding Agents

People often ask me how to get started with Claude Code. For me the question is not entirely clear at first - you just take it, download it, install it, and start using it. What is there to think about? But maybe it is more complex than that, and that is exactly what makes this worth writing about[^1].

There is real documentation from Anthropic, and there are even free courses on Claude Code. Launching the agent itself is not hard - a couple of commands and it is installed on your computer[^2].

So the real question people have is broader. From the start, they assume that Claude, like any agent, has certain capabilities - skills, MCP. People naturally get confused by this, and it feels like to build their own Claude Code setup they need to review all of it and figure out exactly which of these skills they need[^2].

What they are really asking is: show me which skills I definitely need, what I need to install, what folders exist, what helps and what does not, and how to structure my work - which folder to put things in, or how to work with the agent more effectively. In other words, the setup question is the question of all these things together[^2].

Before going into specifics, here is the one thing I want you to take away: you do not need to know everything at once. If you open Twitter, you see an endless stream of tools, skills, and tricks. Most of it can help in some situation, but trying to absorb all of it before you start is the wrong way around. It is far more important to start simple and discover the workflow that is actually useful for you. Begin with the basics, move forward step by step, and you will figure out for yourself what you need and what you do not. This is exactly how my own workflow came together: I have been using these agents actively for about half a year, I tried a great many things, and in the end I realized that the simpler I keep it, the better it works. So this article is not a catalog of everything that exists - it is a path you can actually walk[^34].

There is a lot of official material online too - documentation and free courses - and even with all of it already out there, people still ask whether I have my own take on it. That is what this article is[^33]. I have collected the docs and courses at the end, for when you want to go deeper[^3].

## Choosing where to start

The questions keep coming in. One person asked how to develop an agent with Claude Code and get hands-on with it[^4]. Another, who manages a team of over 60 people and is setting up dedicated spaces to tackle specific problems with AI, said the training they had introduced through their learning platform was not effective enough[^5]. People keep asking about setting up Claude Code and AI coding assistants in general[^6].

To me it is a little strange that people cannot just start - it seems like to begin working with coding agents you simply take one and start doing things. But apparently some people need a plan. So in this section I want to propose a plan for how to start at all - a zero-to-hero path: begin with simple things and gradually add more complex layers. The path is: first choose an assistant, then do tasks with that assistant directly, then make a skill, then make a subagent. After that everything is basically in place - you can build a team of subagents, you can do anything. This foundation is really all you need to be highly productive. And of course, read this Substack, where I constantly write about my experiments[^7].

### Step 1: Choose an assistant

I currently use three: Claude Code, Codex, and OpenCode[^7].

GitHub Copilot used to be a great deal - for ten dollars a month you could write a lot of code. Unfortunately that is no longer the case[^7].

Right now the best value for what you pay is, I think, ChatGPT - the regular Plus version. You use ChatGPT (GPT-5), and Codex comes with it, which you can also use. OpenCode is another decent alternative to start with[^7].

With Anthropic, on the twenty-dollar Claude Code plan you will not get much done - you will most likely hit the limits very quickly. So if you want Anthropic, it is better to choose at least the hundred-dollar plan, which is a more serious commitment. The tools are different, but I cannot say that one is clearly better than another. So at first it does not matter much to pick the absolute best - just pick the one that fits your budget[^7].

Antigravity is also an okay option to start, but the tokens run out too fast and you hit the limits very quickly, so I no longer recommend it as a first agent. I used to recommend it, but now the limits run out too fast. And even when they do not run out, on the free version it works unreliably[^7].

### Step 2: Solve a task with the assistant

The next step is to solve some task. You have chosen an agent, so give it a task - it could be homework from a course, or anything else you can do end-to-end and then check the result. At this stage you need to build some trust in the agent, so that you understand it can actually do things and produce good results. Try different things. You can pick a mini-project - for example the snake game project we did in the AI Dev Tools Zoomcamp, or some other game, or something else. You can look at the many utilities I have written about, find a problem in what you are doing, and solve it with a coding agent. This step is probably the obvious one[^8].

It may be obvious, but many people want to do something advanced right away - they install Claude Code and immediately reach for MCP, skills, subagents, and so on. No - I think you need to start as simply as possible. Find some small problem and solve it with Claude Code, something small that you can scope as narrowly as possible. For example, write a Python or bash script, solve some homework, or write a small piece of code for something[^9].

### Permissions: agents ask a lot at first

When you start using these agents, you notice they ask a lot - for every action they ask for permission. At first this is a bit annoying. There are a few options here. You can run the agent in skip-permissions mode - for Claude this is the bypass-permissions option, for Codex it is YOLO mode. Then they will not ask anything: whatever you can do from the terminal, they can do too. You have to understand the risks. But sometimes speed matters more than control. For instance, you want to give the agent a task for the night and walk away, and you do not want to confirm or reject every single action[^10].

Most of my projects run in exactly this mode - the agent just does whatever it considers necessary. There are ways to constrain this, and I will write about how I handle it a bit later. But on serious tasks I do not do this. For example, my agents cannot get access to the database - I run them on a computer that simply has no access to production, so they cannot accidentally break anything. If I need to do something like Terraform, I never use YOLO mode. There I am careful[^11].

The idea is that you just start using it and figure out what suits you and what does not. There is no universal piece of advice that says always do it this way or never do it that way. You decide for yourself - you just try it and see what you like. It depends on how much you want to be in control, how much influence you want over what happens, or whether the result matters more to you. It comes down to how it feels clearer and more comfortable for you to work. Obviously, if you run in YOLO mode the agent works faster, but there is no control - if the agent decides to delete something, it will delete it[^12].

My first projects I did without YOLO mode. Each time Claude Code asked whether it could perform an action, I said yes - this specific action you can perform, do not ask me about it again. After a while, on that project I ended up with a config where for most things Claude does not have to ask me for permission - it should only ask for destructive things like rm and so on. As for best practices, you can of course run in a sandbox, run in Docker, or run on a remote machine the way I do, but none of that is needed to get started - that is already more advanced. So at first I recommend not bothering with it, just watch and solve your own problems[^13].

### Use agents for automation, not only coding

I also recommend using these agents not only for coding but for automation. For me, the moment I really understood the full value of these agents was when I started automating things. I had already been using agents for coding for quite a few years - well, since around the start of last year you could use one and it was reasonably capable for coding. But I truly understood all the advantages of these agents when I started using them to automate things[^14].

For example, I need to do something by hand: take a video, cut it, upload it to YouTube, rename it. Right now I am specifically doing this for Zoomcamp, for LLM Zoomcamp - rename all the videos, then look at the subtitles and form timecodes from them, and then insert each video into its specific place. Claude does most of this. My involvement is checking how good the cutting is - that it does not get cut off or come out confusing. Then I just take all the videos and upload them at once myself, because uploading has a daily quota, so it is easier for me to upload them. After that Claude finds the videos, pulls their IDs, renames them, and adds them to the right playlist in the right order. Then all that is left for me is to click the Save button on YouTube, since there is no API option for that final step. For automating things like this, Claude is really excellent. Everything you can do through the terminal - running shell commands and so on - can be automated. And automation happens through the creation of instructions[^14].

I have automated a lot of things - for example, creating and uploading homework for courses. I automate this because there is an API. If there is an API and something can be done through the terminal, all of it becomes possible to automate. For instance, I make homework for Zoomcamp, and there is an API through which I can push that homework to the platform. I tell Claude: here is the homework, use this API and upload it[^15].

These kinds of automations were exactly the step that made me realize how powerful these agents are and how much of my own work I can automate - anything I can reach through the terminal, whether it is some utility or an API or anything else[^16].

### Step 3: Make a skill

There is a problem that comes up when you automate something with these assistants: they do not have the context to understand what needs to be done. You say, here is the homework and here is the endpoint, upload it. The agent first goes and looks - okay, what endpoints are there, what can be used, oh, there is a POST here, what does it look like, what request do I need to send - and it tries to send something and does not get it right the first time. That loop, between "here is the homework, here is the endpoint, upload it" and the agent actually figuring it out and doing what is needed, can take a long time[^16].

How is this problem usually solved? You make an instruction for the agent. You say: here, look, I want to do this, and here is the instruction for how to do it. The agent reads it and immediately has all the context for what needs to happen. Such instructions are called skills. A skill is something reusable - something you need to do over and over again - that tells the agent how to do it[^16].

It is a set of instructions, the same way we have them for people. Think of standard operating procedures, or process documents, that describe some process: to do this, you need to do that. For example, to edit a file on GitHub you open GitHub, find the file, click the Edit button, make the change you want, click Commit, and it saves and creates a commit. That is a set of instructions. You can make the same thing for an agent: to change something in git, you do git clone, find the file, change it, then git commit and git push. It is the same idea - in the first case it is the browser, in the second a set of terminal commands. This way you can essentially describe how a great many tasks should be done and put it into a markdown document. That can be called a skill[^17].

Not just any markdown document automatically becomes a skill. Skills have a specific format - they need to be put in a specific folder and named in a specific way. The beauty of skills is that agents pick them up automatically. Back to the task: I have homework and I need to enter the questions on the platform. Without a skill, I can say, I have homework and I need to put it on the platform, and point to the instructions[^17].

With a skill in the right format, I can just throw the request to Claude as is: here is the homework, upload it to the platform, and the agent understands what I want from it. It has a list of available skills, it sees that this skill fits the current problem, it loads that skill and does everything that is needed. I do not need to tell it what to do. The alternative, without a skill, is just documentation - I can say, I need to upload this file, upload the homework here, see the instruction over there. Essentially there is no difference between that and a skill. The only thing a skill does is automatically recognize that I need to do something[^18].

The way I build a skill: I start doing something, I ask the agent to do it, and once we have finished, I say, look, we just did this, I want you to document all of it. The agent documents it into a file and saves it. If I need to do it again, I ask the agent to turn it into a skill. As a rule, both Claude Code and Codex have a built-in skill for making skills, so the agent understands what you want and creates the file in the right format. It is enough to just ask: look, here are my instructions, I want to make a skill, please make it. And the agent does everything right away. That is basically enough. My skills can be seen in the .claude folder in my GitHub repository[^18].

A question that comes up a lot is what should become a skill and what should not. My honest advice is not to overthink it - it is better to make a skill than not make one, just to get a feel for how they work, and over time you will start to see for yourself what is worth turning into a skill. If you want a more structured take, Anthropic published an article on exactly this just a couple of days ago: [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills). It walks through the kinds of skills they use and what you can put inside one[^36][^37].

One point from that article is worth highlighting, because I used to get it wrong myself. There is a common misconception that a skill is just a markdown file. It is not - a skill is a folder, and you can put more than instructions in it: scripts, helper libraries, templates, and other resources, with the SKILL.md pointing to them so the agent only reads what it needs. I do this in my own skills too[^37].

For more examples of what skills look like in the wild, you can look at OpenAI's. People discovered the internal skill files that ship inside OpenAI's environment under /home/oai/ - I wrote about what is in there in [this Substack post](https://alexeyondata.substack.com/p/5-ideas-for-ai-agents-and-openais). And my own skills are all in my public [.claude dotfiles repo](https://github.com/alexeygrigorev/.claude), which I describe at the end of this article[^38].

### Sharing skills across multiple assistants

A problem with skills appears when you use several different assistants. In my case I use three, and they expect skills in slightly different places. The skills are the same, but each tool looks for them in a different folder. For example, OpenCode can load skills from Claude's folder and also has its own, while Codex can only load skills from the .codex folder. What I do in these cases is symlinks. All my skills live in one place, and a symlink is created automatically for both Codex and Claude, so they end up with the same skills. If I add a skill, it immediately appears in all three: OpenCode reads skills from Claude's folder, Codex reads from the .codex folder, and because I use symlinks everything is picked up automatically[^19].

### Disabling Claude's commit co-authorship

One setting I forgot to mention: I do not like that Claude adds itself as a co-author of commits. This is one of the things I disable immediately when I first start using it. You can do it with a Claude settings entry that turns this off[^20].

### Step 4: Use subagents

Now about subagents - why are they needed at all? Imagine you are working on some task through an agent, you have an agent session. As you work and work, your context gets used up. Every time you ask a question or ask the agent to do something, all of it gets added to the context[^21]. When you talk with the assistant, everything we have discussed so far accumulates in the context[^22].

Here is another example of a skill. This Telegram writing assistant, which I am using right now to dictate all of this, is one of those examples that uses skills. There is a skill called "process": what it does is take all the files in a folder, read them, and based on that create an article. The advantage of agents is that they can start from zero context. Imagine the situation where the process assistant has everything I dictated into the phone, and one of the messages says: here is an article, please read it and make a summary. Or: here is a video on YouTube, take the transcript and make a summary[^23].

What happens when this comes up is that the model has to process everything that is there - it reads all the input files - and then it needs to rewrite this into an article, into a draft[^24].

So it needs to rewrite this draft, and then a task comes up like: please take this YouTube transcript of a three-hour video and make a summary. In that case you get a very large transcript that lands in the context, and because of it everything the model read and saw before gets polluted. There is more of it, and the model focuses more on this text, so first of all you will not be able to make a proper article out of what was there before, the transcript itself may not come out well, and afterward you will not be able to continue - some other instruction might be there too, and it all ends up in one pile, and nothing good comes of it[^25].

What can you do instead? Instead, when the agent sees that the task is to analyze some text or analyze something and make a summary, rather than adding it to the existing context, the agent can create another agent and give that agent an instruction, saying: look, you need to take this YouTube transcript and make a summary of it. It then runs in a separate process, or at least with only one clear, specific task; it does not see everything else that happened. It completes the task and saves the result somewhere. Meanwhile the main agent that launched it just knows that this agent started and that it finished. So the main agent's context does not get polluted[^25].

Beyond having the context free of these large chunks, new benefits appear, because several such agents can be launched at once. The main agent - let us call it the orchestrator - can see two related tasks: one task to make the article itself, and another task to make a summary of the video. These tasks can be run in parallel, and while they run the agent does other things. Then when they finish, it says, okay, this one is done, and I have just finished writing the article draft, so let me put this into it. This way you parallelize the work. That is for these context-related tasks[^26].

I also often use agents for coding. My approach is often like this: one agent needs to write the code, and a tester agent looks at the code, checks it, and gives a review. Until the tester says the code is okay and that there are no errors, it is not accepted. Why can you not just use a single agent? You can, of course, and in many cases it will be fine. But this also works the way it does with real people: the person who wrote the code tests it worse afterward. Their view is, so to speak, blurred, or the context is overflowing, so it is hard to concentrate on actually finding the bugs in your own code. When someone from the outside comes in, someone who did not write the code and can look at it with a fresh perspective and an unfilled context, they can test and verify better that the code has no bugs. That is the pattern I use. I use more subagents too. You can read about how my team of subagents solves tasks in a separate article[^26]: [I Built an AI Agent Team for Software Development and Tested on 5 Real Projects](https://alexeyondata.substack.com/p/i-built-an-ai-agent-team-for-software).

### The path from zero to hero

That is basically all the essentials. For me the main thing is to just start doing something. Then, when you see that some things keep repeating, you write them into skills, and the next time you can simply tell the agent "do this," and it will understand and take the skill. You will not have to repeat the same thing every time. And when you hit a context problem, you use subagents - if you know that a task requires analyzing and looking through a large amount of information, you launch a subagent. That is the most important part. There are a couple more tricks I will talk about later[^27].

But overall, I think that if you go through this path - from just using an assistant, to adding skills, to starting to use subagents - then you can already do basically anything with it. That is exactly the from-zero-to-hero path, because once you understand that these things exist and what kinds of problems they solve, you can already get going. But you need to go through this path from the very beginning. I do not recommend starting right away with subagents and trying to understand how they work, because that will take some time. If you start with the complex things, you may not figure out the simple ones, and there is a risk that nothing will come out properly[^27].

## Context files and the subcommands I actually use

A couple of extra things worth mentioning at the end.

### Project context files (CLAUDE.md and AGENTS.md)

One thing I should have mentioned earlier: the context files. In your own projects you should always create these files - CLAUDE.md and AGENTS.md - so the agent has context. Every time the agent starts, it reads them, and that is where the description of the project lives, the things the agent specifically needs to know. Claude Code reads CLAUDE.md, while Codex and OpenCode read AGENTS.md[^28].

This is useful to set up, and it is really the step between just using the agent and working with it more deliberately. When you first start, you realize it is a useful thing: instead of explaining to the agent every single time what this project is, or letting it crawl through the whole repository to figure things out, the agent reads the context file straight away and knows what it needs[^28].

### Reset (or new) to keep the context clean

The subcommand I use most often is the one that resets the session - it is called reset or new depending on the agent. The point is not to overload the context. Every time I start a new task, I want to clear the context so that only what is important lands in it[^28].

This is exactly where a good CLAUDE.md or AGENTS.md matters: it makes starting from a clean slate painless, and when compaction happens, everything important is still at hand[^28].

### Goal: keep the agent working until the goal is reached

The other command I use very actively right now is goal. It works in both Codex and Claude Code. You give the agent a goal, and it does not stop until that goal is reached. It is something like the Ralph Loop we talked about. The common problem is that an agent waits for some input from you - "what do you think about this?" - even when the work is not actually done. The goal loop forces it to keep working and not wait for anything from you[^28][^29].

Importantly, this is built in - you do not need to install any plugins for it. It works out of the box in the latest versions of both tools. In Codex it was there from the start; for Claude Code you used to need a plugin for this kind of loop, but now it works without one[^35].

Codex shipped it first (Greg Brockman described it as a built-in Ralph Loop), and Claude Code added a near-identical version shortly after. You type the command followed by a completion condition in plain language, for example a goal that all tests pass and the lint step is clean. The agent then keeps starting new turns on its own until the condition is met. In Claude Code a separate small evaluator model checks after each turn whether the condition is satisfied and, if not, sends back guidance and starts another turn; the goal clears automatically on success. It also runs headless, and it pairs well with auto / skip-permissions mode so each turn runs without approval prompts. Official references: [Claude Code goal docs](https://code.claude.com/docs/en/goal) and [Codex follow-goals docs](https://developers.openai.com/codex/use-cases/follow-goals)[^29].

The Ralph Loop it descends from is an autonomous-coding pattern: a loop that feeds the same prompt to a fresh agent over and over until the task is done, with progress accumulating in files and git history rather than in the model's context. The goal command is the productized, in-process version of the same idea[^29].

The one real caveat is cost and runaway risk. Each turn now costs two model calls (the main turn plus the validator), so it is more expensive than a normal session, and there is no hard spending cap by default. It helps to phrase the end state as something binary and machine-checkable, name the verification command explicitly, and bake a limit into the condition itself (for example, stop after a set number of turns)[^29].

Beyond these, I do not really use anything else. I used some other plugin with subcommands before, but now I do not see anything useful in it. For me it comes down to just two commands - reset or new, and goal - and I use goal very actively. Everything else, I do not use[^30].

## My setup: the .claude dotfiles repo

To make this concrete, my own setup lives in a public repository: [github.com/alexeygrigorev/.claude](https://github.com/alexeygrigorev/.claude) [^31][^32]. Despite the name, it is broader than Claude Code - it is a single source of truth for bootstrapping and configuring all three agents (Claude Code, Codex, and OpenCode) from one shared clone, so every machine and every assistant ends up with the same setup[^31].

The structure:

- An installer script clones the repo and runs a configure script that wires everything into the right home-directory locations. The configure step takes a target - claude, codex, opencode, or all.
- A config/ folder holds per-assistant settings (a settings.json for Claude and OpenCode, a config.toml for Codex). For Claude it merges in a settings.json; for Codex it syncs into the Codex config and symlinks skills into the Codex skills folder; for OpenCode it symlinks skills into the OpenCode config.
- A skills/ folder holds the shared skills (one folder per skill, each with a SKILL.md), symlinked into each assistant so all three share the same skills. Examples include create-github-repo, fetch-youtube, fetch-loom, fetch-google-recorder, init-library, jina-reader, openai-transcribe, regular-ping, release, setup-pypi-ci, and stylint.
- A shared .bashrc is sourced from the repo, so a git pull propagates new aliases and functions automatically. It defines the short aliases I use daily - for example c for claude, cc for continue-session, csp for claude with skip-permissions, cy for codex in bypass mode, and an oc function for OpenCode.

It also encodes the safety guardrails I described earlier. The Claude settings register a PreToolUse hook that runs a check-destructive script, which blocks dangerous commands (things like rm -rf /, force pushes, dropping a database, or terraform apply) unless confirmed. The oc function for OpenCode strips a long denylist of provider API-key environment variables before launching, so leaked credentials never reach the agent[^31].

There are no custom slash commands or subagents committed in this particular repo - its extensibility is entirely through skills[^31].

## Where to read more: docs and free courses

The official documentation and free courses below are the canonical starting points for getting set up.

### Start here

The full list further down is long. If you only open a few things, open these:

- [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) - the flagship free getting-started course, from installation through customization.
- [Claude Code Overview](https://code.claude.com/docs/en/overview) - what Claude Code is and the install commands for every surface.
- [Codex Quickstart](https://developers.openai.com/codex/quickstart) - the four ways to run Codex and how to sign in with ChatGPT or an API key.
- [OpenCode docs intro](https://opencode.ai/docs/) - install, configure a provider, and the built-in agents.

### Claude Code official documentation

- [Overview](https://code.claude.com/docs/en/overview) - what Claude Code is and install commands for every surface (terminal, VS Code, JetBrains, desktop, web). The first stop for picking an environment and installing.
- [Quickstart](https://code.claude.com/docs/en/quickstart) - walks a first-time user through their first real task: exploring a codebase, making an edit, committing a fix.
- [Advanced setup](https://code.claude.com/docs/en/setup) - system requirements, platform-specific installation (including apt/dnf/apk on Linux), version management, uninstall.
- [Settings](https://code.claude.com/docs/en/settings) - reference for global and project-level settings.json plus environment variables.
- [Memory (CLAUDE.md)](https://code.claude.com/docs/en/memory) - how to give Claude persistent project instructions via CLAUDE.md files and how auto-memory accumulates learnings across sessions.
- [Skills](https://code.claude.com/docs/en/skills) - how to create, manage, and share skills (packaged repeatable workflows and custom commands).
- [MCP](https://code.claude.com/docs/en/mcp) and [MCP Quickstart](https://code.claude.com/docs/en/mcp-quickstart) - connecting Claude Code to external tools and data sources via the Model Context Protocol, with a hands-on first-server walkthrough.
- [Subagents](https://code.claude.com/docs/en/sub-agents) - creating specialized subagents for task-specific workflows and better context management.
- [Hooks](https://code.claude.com/docs/en/hooks) and the [Hooks guide](https://code.claude.com/docs/en/hooks-guide) - run shell commands before and after Claude Code actions (auto-format on edit, lint before commit, notifications).
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview) - an orientation map for deciding when to use CLAUDE.md vs skills vs subagents vs hooks vs MCP vs plugins.

### Claude Code free course (Anthropic Academy)

- [Anthropic Academy](https://anthropic.skilljar.com/) - Anthropic's official free training platform. Self-paced courses, no Anthropic account required.
- [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) - the flagship free getting-started course, aimed at people new to AI coding agents. Goes from installation through customization.
- [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) - a deeper, more practical free course for building real work, a good follow-on after the 101.

### OpenAI Codex official docs

- [Codex Quickstart](https://developers.openai.com/codex/quickstart) - covers the four ways to run Codex (desktop app, IDE extension, CLI, cloud), installation, and ChatGPT / API-key sign-in.
- [Codex developer docs](https://developers.openai.com/codex) and the [Codex CLI](https://developers.openai.com/codex/cli) page for the terminal agent.
- [Codex GitHub repo](https://github.com/openai/codex) - the open-source CLI, with a docs/ folder that supplements the hosted docs.

### OpenCode official docs

- [OpenCode docs intro](https://opencode.ai/docs/) - install via script or Homebrew tap, configure an LLM provider, initialize a project (which creates an AGENTS.md), and the built-in build and plan agents.
- [OpenCode homepage](https://opencode.ai/) and the [GitHub repo](https://github.com/anomalyco/opencode). Note: the older sst/opencode URL now redirects here.

### Other free getting-started material

- [Build with Claude](https://www.anthropic.com/learn/build-with-claude) - Anthropic's developer learning hub linking the Academy courses, cookbook, and quickstarts.
- [Anthropic Quickstarts](https://github.com/anthropics/claude-quickstarts) - official runnable example projects, including an autonomous coding agent built on the Claude Agent SDK.

## Notes by tool

These are condensed notes on the specifics of each tool, kept here as reference for when you want to go deeper than the walkthrough above.

### Claude Code

Installing and launching:

- On Windows the native installer is now used (previously a global npm install was simpler). The terminal/CLI is the primary interface.
- Claude Code can run remotely on a cloud server (Hetzner, AWS) over SSH, which is the basis of the phone-based workflow.
- Short shell aliases speed up daily use: a single letter for claude, one for continue-session, one for skip-permissions, and combined variants.

Configuration files and structure:

- A central .claude/ dotfiles repo is synced across devices through GitHub. It holds commands/, skills/, shell config, and CLAUDE.md. Skills and commands are symlinked from the repo into ~/.claude/.
- CLAUDE.md files give project-scoped instructions, loaded hierarchically by walking up the directory tree (like .gitignore).
- .claude/settings.json sets project-level config: disabling bypass permissions, choosing the model, adjusting compaction thresholds, and configuring subagent models.
- Memory is auto-managed through a MEMORY.md index plus topic files, with frontmatter-typed entries that get consolidated automatically and capped in size.

Slash commands:

- Custom commands live as markdown files in .claude/commands/ and are user-triggered with the / syntax. Examples in use: a release command that runs the full Python publish pipeline, an init-library command that scaffolds a new package, a create-github-repo command, and the /process workflow for this Telegram writing assistant.

Skills:

- Skills are reusable workflows encoded as step-by-step instructions that the agent discovers and loads on its own. The difference from commands: skills are agent-discovered, commands are user-triggered, and Claude Code merges both.
- They load lazily, so only what the agent needs gets pulled in.
- A practical way to build a skill: interact with the agent, correct its mistakes, then ask it to summarize the corrected behavior as a skill. Improve a skill the same way over time.
- Examples include a fetch-youtube skill and a refactor-pass skill. A public skills repository is at github.com/alexeygrigorev/.claude.

Subagents and agent teams:

- Subagents are separate agents with fresh context windows, so context-heavy work does not pollute the main agent's memory. Good for analyzing large files, parallel processing, and verification with a clean perspective. They are defined as markdown files in .claude/agents/ with YAML frontmatter (name, description, tools, model, instructions).
- The planner-executor pattern has a planner produce a detailed plan and executor agents run each step with clean context.
- Agent teams are an experimental step beyond subagents (enabled via an environment variable or settings.json): one team lead plus several teammates that are independent Claude Code sessions. Unlike subagents, teammates talk directly to each other, coordinate through a shared task list with file locking, and message or broadcast.

Safety and permissions:

- Permission modes range from default (ask) through auto (approve) and plan (read-only) to bypassPermissions (dangerous).
- For high-risk projects, add a .claude/settings.json that disables bypass-permissions mode. Hooks can intercept and block dangerous operations (for example, blocking force pushes).

Token usage and performance:

- Switch to Sonnet instead of Opus to cut cost, and use Haiku for subagents.
- Raise the compaction threshold to delay message truncation, lower the effort level during a session, and turn off verbose output via /config.

Usage habits:

- Use plan mode for non-trivial tasks (three or more steps, or architectural decisions). Never mark a task complete without proving it works.
- Track work in a tasks/todo.md with checkable items, and capture corrections in a tasks/lessons.md so mistakes do not repeat.

### OpenAI Codex

- A clean, minimalist interface. Run it from the terminal.
- Supports an agent workflow with multiple subagents running in parallel, driven by an explicit task list. The orchestrator does not auto-continue when agents finish, so it needs manual prompting to keep work flowing.
- Advantage in practice: it is not hit by weekly limits as aggressively as Claude Code, so it can keep going when Claude Code is exhausted. This is what motivated trying it as an alternative.

### OpenCode

- The desktop app (a VS Code-like fork adapted for AI) is preferred over the terminal mode, though the terminal mode exists. It can also run as a web service with less setup effort than Claude Code.
- Easy to switch models, including pointing it at other providers (for example Z.AI's GLM-5) with an API key.
- It can sync skills and commands from Claude Code through the shared dotfiles repo, so hooks and skills carry over.
- The interface is smooth without the flickering Claude Code had. A subagent feature gap was noted but not yet explored.

### Cross-tool setup

- A dedicated remote server (for example Hetzner) runs the agents 24/7 in tmux sessions, with tmuxctl simplifying session management and Termius for SSH from Android. Only SSH is open on the firewall; other ports are reached via forwarding.
- Base development setup (especially on Windows): Terminal with bash, Python via UV, NodeJS via NVM, Docker, VS Code, GitHub CLI, plus the agents themselves. SSH keys are generated and added to GitHub for private repos.
- Makefiles keep commands short behind targets, which matters for phone-based work.
- Credentials should not sit on agent-accessible servers - use temporary sessions or a vault. Documenting every setup step makes it reproducible and lets an agent re-run it.

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
