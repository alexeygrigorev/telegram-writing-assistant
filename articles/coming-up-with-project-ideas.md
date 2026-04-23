---
title: "Coming Up with Project Ideas"
created: 2026-04-23
updated: 2026-04-23
tags: [projects, ai-buildcamp, design-thinking, capstone]
status: draft
---

# Coming Up with Project Ideas

One thing still feels confusing to many people: how to actually choose a project.

This article exists because the problem is not a shortage of ideas. The problem is selection.

Before looking at any project list, it helps to separate three different cases:

- a **portfolio project** you want to show to employers or clients
- a **course project** that should fit the structure and rubric of a program
- a **small self-project** you build to remove friction from your own life

This is true even though the AI Engineering Buildcamp V2 materials already contain a large pool of ideas. Across the V2 project-work files, we already have **over 150 project ideas**[^1][^2][^3].

So the problem is not that we do not have enough ideas. The problem is that people still do not know **which** idea to choose, **why** they are choosing it, and **what kind of project** they are actually trying to build.

That is why I want this article.

## Not all projects are the same

Before choosing a project, the first question is not "what sounds cool?" It is:

**What kind of project am I trying to build?**

There are at least three different cases, and they should be approached differently.

### 1. Portfolio projects

These are projects you want to show to employers, clients, or collaborators.

The main question is not just whether the project is interesting. The question is whether it signals the right skills.

A good portfolio project should:

- solve a recognizable problem
- have a clear README and problem statement
- show engineering quality, not just prompting
- make it easy to talk about tradeoffs, tests, evaluation, and deployment

For this kind of project, it is often useful to choose something close to real business workflows or production tooling.

Examples from Buildcamp V2:

- **Bug Report Telegram Bot**: takes voice messages, classifies them across repositories, structures them, evaluates bug quality, opens GitHub issues, and includes deployment and monitoring elements[^2]
- **AI Engineering Job Market Explorer**: uses job-listing data to recommend what skills to learn next and what companies match a profile[^2]

### 2. Course projects

These are capstone-style projects where the main goal is to go through the full learning process of the course.

Here the project does not need to be your life's mission. It needs to be a good fit for the course structure.

In Buildcamp V2, a good course project is one that lets you go through the full engineering cycle[^4]:

1. identify a real problem
2. build a simple proof of concept
3. improve code quality and testing
4. add monitoring and collect usage data
5. build evaluation so you know how well it works

This is why V2 explicitly says to start project work in week 1 and submit an idea early, even if it is not perfect[^4][^5].

Examples from Buildcamp V2:

- **Medical Chart Generator**: a patient-doctor conversation gets transcribed and turned into a structured chart[^2]
- **Documentation Chatbot with Handoff**: a grounded support assistant with clear evaluation and handoff logic[^3]

### 3. Small projects for yourself

These are small tools you build because something in your own life is annoying.

This is actually one of the best ways to get started, because the user is obvious and the feedback loop is immediate.

A good self-project should:

- solve a problem you actually have
- be narrow enough to finish quickly
- have a simple first version
- give you a visible improvement in daily life

These projects do not need to be grand. In many cases, they are better if they are not grand.

Examples from Buildcamp V2:

- **Voice-to-Todo Agent**: talk to a todo app instead of typing tasks manually[^3]
- **Restaurant Receipt Splitter**: take a photo of a bill, extract line items, and split the total among a group[^2]

## What the Buildcamp V2 project pool is based on

One useful thing about the V2 materials is that the project list is not random. It is built from recurring sources that reflect real demand[^1][^2][^3]:

- what students say they want to build for their capstones and projects
- what appears in scholarship applications and similar intake material
- related supporting sources such as office-hours discussions, previous demo projects, and older course material

That mix matters.

Some ideas are realistic because someone already built them. Some are realistic because someone needed them at work. Some are useful because they are evergreen patterns that keep coming up: support bots, research agents, document extraction, workflow automation, knowledge management, developer tooling.

So again: the problem is not lack of ideas.

## What Buildcamp V2 already gives you besides ideas

The V2 folder does not only give people idea lists. It already contains a full "start now" path for choosing and starting a project[^4][^5][^7]:

- a project-work overview that says to pick a project today and start from week 1
- an "idea to submission" page with different paths depending on whether you already have an idea, a vague idea, or no idea
- a capstone homework that tells students to describe the problem, scaffold the repo, and add their own data in the first week
- a starter project so people can move from "idea" to "something running" quickly

That is useful context for this article. The goal is not to replace the V2 material. The goal is to make the selection logic more explicit, because this is still where many people get stuck.

## Why choosing is still confusing

Even with over 150 examples, people still get stuck. V2 says this directly: for most students, the hardest part is not building, but deciding what to build[^4].

I think there are a few reasons:

- People start from technology instead of the problem.
- They mix different goals together: portfolio, capstone, and personal utility.
- They try to find the perfect idea instead of a workable one.
- They want the project to prove too many things at once.
- They do not yet have enough raw material from their own life or work.

The result is a familiar loop: read more ideas, get more confused, postpone the decision, watch more course videos, still do not start.

This article is meant to break that loop.

## A practical way to choose a project

Here is the approach I would suggest.

### Step 1: Decide the project type first

Pick one primary goal:

- portfolio project
- course project
- small self-project

You can later combine them, but if you do not choose a primary goal, the selection criteria stay fuzzy.

### Step 2: Start with a problem, not with a technology

The V2 materials are very clear about this: students who start with "I want to build an AI agent" usually get stuck. The better path is to start with something real that is annoying, repetitive, or expensive in time[^4].

Good starting points:

- something you do manually every week
- something people in your team or community complain about
- something that is hard to search, summarize, classify, or extract
- something you personally wish existed

### Step 3: Pick the smallest useful version

A good project is not the biggest one. It is the one with the clearest version 1.

Ask:

- who is the user?
- what is the input?
- what is the output?
- what is the smallest useful version?
- how would I know it works?

If you cannot answer these in a few sentences, the project is still too vague.

### Step 4: Check whether it fits the context

This is where the three project types diverge.

For a **portfolio project**, ask:

- Will this signal the kind of work I want to be hired for?
- Can I explain the engineering decisions clearly?
- Does it show more than just prompting?

For a **course project**, ask:

- Can I use this idea to go through the full course process?
- Can I add tests, monitoring, and evaluation later?
- Is it a good fit for the rubric without forcing unnecessary features?

For a **self-project**, ask:

- Will I actually use this?
- Can I build version 1 in a few days or a couple of weeks?
- Does it remove real friction from my life?

### Step 5: Submit early, refine later

This is another important V2 lesson: the project should be chosen early, not after finishing the course content[^4][^5][^7].

A finished okay project is better than an unfinished ideal one.

Clarity often comes from building. In V2, the capstone homework starts on day 1: pick the idea, scaffold the repo, and put your own data into the starter[^7]. The first useful repo and README teach you more than another hour of browsing idea lists.

## The three Buildcamp V2 paths

The V2 "From Idea to Submission" page already defines three useful paths[^5]:

### Path A: you already have an idea

Do a quick fit check and submit.

### Path B: you have a vague idea

Talk it through until it becomes concrete enough to fit in 2-3 sentences.

### Path C: you have no idea

Do two things:

- browse examples for inspiration
- use the interview prompt to surface problems from your own life

The V2 gist provides both prompts[^6]:

- [Project-Idea Brainstorming Prompt](https://gist.github.com/alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1)

That pairing is useful:

- one prompt helps you discover ideas
- the other helps you reject weak ones

## What makes a good Buildcamp-style capstone

Based on the V2 project-work overview, a good capstone has three things[^4]:

- a real problem someone actually cares about
- data or inputs you can realistically access
- a clear path to testing, monitoring, and evaluation

RAG and agents can help, but V2 makes another useful point: they are not the point of the project. They are tools. Some projects need them naturally; some do not. Do not bolt them on just to sound more advanced[^4].

## If you are still stuck

Do this instead of reading more idea lists:

1. Keep a short note for 2 days called `annoying things`.
2. Write down every repetitive or frustrating workflow.
3. Pick one item that feels both useful and finishable.
4. Write a one-paragraph project card.
5. Create a repo and start version 1.

The goal is not to find the perfect idea.

The goal is to choose something real, choose it early, and start building before the confusion turns into avoidance.

## Sources

[^1]: [Project Ideas for Your AI Capstone](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/03-cohort-1-project-ideas.md)
[^2]: [Cohort 2 Project Ideas](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/04-cohort-2-project-ideas.md)
[^3]: [Other Project Ideas](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/05-other-project-ideas.md)
[^4]: [Project Work overview](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/01-section-overview.md)
[^5]: [From Idea to Submission](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/02-from-idea-to-submission.md)
[^6]: [Project Ideas: Prompts for Getting Unstuck](../../ai-engineering-buildcamp/gist-prompts/00-project-ideas.md)
[^7]: [Module 1 Capstone: Your AI Project](../../ai-engineering-buildcamp/v2/01-foundation/homework/02-capstone.md)
