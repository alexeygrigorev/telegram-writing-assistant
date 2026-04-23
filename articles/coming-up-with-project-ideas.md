---
title: "Coming Up with Project Ideas"
created: 2026-04-23
updated: 2026-04-23
tags: [projects, ai-buildcamp, design-thinking, capstone]
status: draft
---

# Coming Up with Project Ideas

I keep seeing the same problem: people don't know how to choose a project.

AI Engineering Buildcamp V2 already has over 150 project ideas across the project-work files[^1][^2][^3]. That helps with the blank-page problem. It doesn't solve selection.

If you're trying to choose between a portfolio project, a course capstone, and a small tool for yourself, this article is for you. I'll split those three cases first. Then I'll look at where the Buildcamp ideas come from, what V2 already gives you besides idea lists, and how I'd narrow a project down to something you can actually ship.

## Project types

The first decision is not which idea sounds interesting. The first decision is what kind of project you're trying to build.

<!-- illustration: three lanes for portfolio projects, course capstones, and small self-projects, each with different selection criteria -->

### Portfolio projects

Portfolio projects help you get hired, get clients, or show the kind of work you want to do more of.

The project needs to do a few things well:

- solve a recognizable problem
- show engineering quality, not only prompting
- make the tradeoffs easy to explain
- give you something solid to put in a README and talk through in interviews

For portfolio work, I wouldn't start with random brainstorming. I'd use a tighter process.

1. Select a domain.

Look at job postings in your area or remote roles you would realistically take. Group them into domains such as e-commerce, healthcare, finance, education, or developer tools. Then pick one domain and stay with it for now. Too many options create choice paralysis.

2. Research specific companies.

Pick a few companies in that domain. Read their websites, product pages, and blog posts. Read their job descriptions too. If you're building an AI engineering portfolio, pay attention to where they already use AI and where AI could help but doesn't seem to exist yet.

3. Build one use case.

Make a list of use cases from that research and choose one. Then find, scrape, or generate a realistic dataset for it. It doesn't need to be the company's real data, but it does need to feel believable for that domain and that workflow.

4. Cap the time.

Give yourself 10 hours. Don't spend more than that. An okay finished project teaches you more than a perfect project that drags on for weeks.

This approach makes the project easier to explain. You can say which domain you chose, which companies you looked at, which workflow you focused on, and why your dataset is realistic.

Examples from Buildcamp V2:

- Bug Report Telegram Bot: takes voice messages, classifies them across repositories, structures them, evaluates bug quality, and opens GitHub issues with deployment and monitoring in the loop[^2]
- AI Engineering Job Market Explorer: uses job-listing data to suggest what skills to learn next and what companies match a profile[^2]

### Course projects

Course projects work differently. Here you are not trying to build your life's mission. You are trying to build something that fits the course and lets you practice the full engineering process.

In Buildcamp V2, a strong course project takes you through five steps[^4]:

1. identify a real problem
2. build a simple proof of concept
3. improve the code and test it
4. add monitoring and collect usage data
5. evaluate how well it works

That is why V2 pushes project work into week 1 instead of leaving it for the end[^4][^5]. A course project needs to be small enough to start early and structured enough to keep improving during the course.

Examples from Buildcamp V2:

- Medical Chart Generator: transcribes a patient-doctor conversation and turns it into a structured chart[^2]
- Documentation Chatbot with Handoff: answers support questions from grounded documentation and hands off when confidence is low[^3]

### Small self-projects

Small self-projects come from everyday friction. They often make the best starting point because the user is obvious, the feedback loop is short, and the first version can stay small.

I usually see these projects appear in a simple sequence:

1. I work on something real.
2. I notice something annoying, suboptimal, or missing.
3. I build a tool that removes that friction.

That is where most of my own projects come from. I am usually not trying to invent a project from zero. I'm already in the middle of some other workflow, I hit a pain point, and that pain point becomes the next thing I build.

It helps to keep a running note of small annoyances. Most of them won't become projects. A few of them will turn into exactly the kind of useful, finishable tool that is worth building.

<!-- TODO: link relevant Alexey On Data Substack articles with examples of projects that started from day-to-day friction -->

Examples from Buildcamp V2:

- Voice-to-Todo Agent: talks to a todo app instead of making you type tasks manually[^3]
- Restaurant Receipt Splitter: takes a photo of a bill, extracts line items, and splits the total among a group[^2]

## Buildcamp V2 idea sources

The Buildcamp project pool is not random. It comes from recurring sources that reflect real demand[^1][^2][^3]:

- what students say they want to build for their projects
- what appears in scholarship applications and similar intake material
- supporting sources such as office-hours discussions, older course material, and previous demo projects

That matters because the list is not a collection of abstract brainstorms. Many of the ideas come from work problems, repeated frustrations, or things people already tried to build.

This is also why the list feels broad. It includes support bots, research agents, document extraction, workflow automation, knowledge management, and developer tooling. The breadth is useful. It can still leave people stuck.

## Buildcamp V2 project workflow

The V2 folder already gives you more than idea lists[^4][^5][^7].

- The project-work overview tells you to pick a project now and start from week 1.
- The idea-to-submission page gives you different paths depending on whether you already have an idea.
- The capstone homework tells you to describe the problem, scaffold the repo, and add your own data in the first week.
- The starter repo gives you a quick way to move from "idea" to something running.

<!-- illustration: flow from project idea -> starter repo -> first data -> first working version -->

If you're building a course project, this structure is already enough to get moving. Even outside the course, the same sequence is useful. Pick the problem, start the repo, add real data, and improve from there.

## The selection problem

Even with over 150 examples, people still get stuck. V2 says this directly: for most students, the hardest part is not building. It is deciding what to build[^4].

I usually see the same problems behind that hesitation:

- people start from technology instead of a problem
- people mix portfolio goals, course goals, and personal utility in one project
- people wait for the perfect idea instead of a workable one
- people try to prove too many things in one repo
- people don't yet have enough raw material from their own work and life

That creates a familiar loop. You read more idea lists, get more confused, postpone the decision, and still don't start.

## Project selection process

The next step is to narrow the field quickly enough that you can start building.

1. Pick the project type first.

Choose one primary goal: portfolio project, course project, or self-project. You can combine them later. If you don't choose a primary goal, the criteria stay fuzzy.

2. Start with a real problem.

V2 is very clear on this point. People who start with "I want to build an AI agent" usually get stuck[^4]. Start with something repetitive, annoying, slow, expensive, or hard to search.

3. Pick the smallest useful version.

Answer five questions in a few sentences:

- who is the user
- what is the input
- what is the output
- what is the smallest useful version
- how will you know it works

If you can't answer those questions cleanly, the project is still too vague.

4. Check the idea against the context.

Use the criteria from the matching project type:

- portfolio project: does this show the kind of work I want to get hired for
- course project: can I test it, monitor it, and evaluate it over several weeks
- self-project: will I actually use this in my own life soon

5. Start early and refine later.

This is another strong V2 lesson. Choose early, then learn by building[^4][^5][^7]. The first useful repo and README teach you more than another hour of browsing idea lists.

## Buildcamp V2 paths

The V2 "From Idea to Submission" page breaks this down into three paths[^5].

1. You already have an idea.

Run a quick fit check and submit it.

2. You have a vague idea.

Talk it through until it becomes concrete enough to fit in two or three sentences.

3. You have no idea yet.

Browse examples for inspiration, then use the interview prompt to pull problems out of your own life.

The V2 gist includes both prompts[^6]:

- [Project-Idea Brainstorming Prompt](https://gist.github.com/alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1)

That pairing works well because one prompt helps you generate ideas and the other helps you reject weak ones.

## Buildcamp-style capstones

The Buildcamp overview keeps the capstone standard fairly simple[^4]:

- solve a real problem that someone actually cares about
- use data or inputs you can get without heroic effort
- leave a clear path to testing, monitoring, and evaluation

RAG and agents can help, but they are not the point of the project. Some projects need them. Some do not. Don't bolt them on just to make the project sound more advanced[^4].

## Getting unstuck

If you're still stuck, stop reading idea lists for a moment and do this instead:

1. Keep a short note for two days called `annoying things`.
2. Write down repetitive workflows, frustrations, and delays as they happen.
3. Pick one item that feels both useful and finishable.
4. Write a one-paragraph project card.
5. Create the repo and start version 1.

You don't need the perfect idea. You need a real problem, a small scope, and a reason to start now.

## Sources

[^1]: [Project Ideas for Your AI Capstone](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/03-cohort-1-project-ideas.md)
[^2]: [Cohort 2 Project Ideas](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/04-cohort-2-project-ideas.md)
[^3]: [Other Project Ideas](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/05-other-project-ideas.md)
[^4]: [Project Work overview](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/01-section-overview.md)
[^5]: [From Idea to Submission](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/02-from-idea-to-submission.md)
[^6]: [Project Ideas: Prompts for Getting Unstuck](../../ai-engineering-buildcamp/gist-prompts/00-project-ideas.md)
[^7]: [Module 1 Capstone: Your AI Project](../../ai-engineering-buildcamp/v2/01-foundation/homework/02-capstone.md)
