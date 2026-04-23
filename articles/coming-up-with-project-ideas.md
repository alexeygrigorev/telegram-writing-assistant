---
title: "Coming Up with Project Ideas"
created: 2026-04-23
updated: 2026-04-23
tags: [projects, ai-buildcamp, design-thinking, capstone]
status: draft
---

# Coming Up with Project Ideas

I keep having the same conversation. Someone asks me how to find a junior AI engineering job. I say: do projects. Then they ask: how do I choose a project? That's the question I want to answer here, because I've been repeating the same answer for months.

This article is for two groups of people. The first is AI Engineering Buildcamp students who have to pick a capstone project and don't know where to start. The second is anyone going through the same blank-page problem on their own - deciding what to build, whether for a portfolio, for practice, or to scratch a personal itch.

A big part of what I care about in Buildcamp is that each new cohort has a higher percentage of people who actually finish their projects. Finishing is what gets people hired. So if you're in the course, I want to help you be more effective at picking something you can ship[^7]. If you're not in the course, the same process should still work for you.

## Idea lists on their own don't solve it

In Buildcamp, we already have more than 150 project ideas collected across several idea lists[^1][^2][^3]. That pool comes from what students have asked to build, from scholarship applications, from office-hours conversations, and from older course material. It isn't random brainstorming. It's a collection of things real people wanted to build.

And yet, people still get stuck. I've seen this happen enough times to understand why. You open the list, skim it, something sort of catches your eye, and then you close the tab without starting anything. The list helps a little, but a list of ideas doesn't answer the harder question: which one is right for me, right now, and how do I scope it so I can finish it?

That's what this article tries to fix. Not by adding more ideas to the pile, but by giving you a way to decide.

## Three kinds of projects

Before picking an idea, pick the kind of project you're building. The criteria are completely different.

<!-- illustration: three lanes for portfolio projects, course capstones, and small self-projects, each with different selection criteria -->

A portfolio project exists to help you get hired or win clients. A course project exists to teach you the full engineering process during the course. A self-project exists because you personally want the thing to exist. These goals can overlap, but if you don't pick one as the primary goal, the criteria stay fuzzy and you end up trying to make one project do everything.

## Portfolio projects

A portfolio project has one job: make it easy for a hiring manager or client to say yes to a conversation. To do that, the project has to solve a recognizable problem, show real engineering quality rather than just prompting, and make the tradeoffs easy to explain. You want something you can point to in a README and talk through in an interview.

Hiring managers don't spend a lot of time looking. Recruiters often move on after a minute or two, and hiring managers usually have five or ten minutes before an interview to scan your GitHub. They want to see immediately what the project does, why it exists, and whether it's close to production - tests, evaluation, CI/CD, a deployment link[^8].

That changes how I'd pick a portfolio project. I wouldn't start with random brainstorming. I'd start with where I want to work.

Pick a domain first. Look at job postings in your area or remote roles you would realistically take, and group them into domains like e-commerce, healthcare, finance, education, or developer tools. Then pick one and stay with it for a while. Too many options cause choice paralysis, and targeting one domain means you can also talk fluently about it in interviews.

From there, look at actual companies in that domain. Read their websites, product pages, and blog posts, and pay attention to where they already use AI and where it could help but doesn't seem to exist yet. Make a short list of possible use cases and pick one. Then find, scrape, or generate a realistic dataset for it. It doesn't have to be the company's real data, but it does have to feel believable for that domain.

Finally, cap the time. Give yourself something like ten hours, or a couple of weekends. An okay finished project teaches you more than a perfect project that drags on for weeks, and most of the learning is in shipping and explaining it afterwards.

This approach also makes the project much easier to talk about. You can say which domain you chose, which companies you looked at, which workflow you focused on, and why your dataset is realistic - instead of "I built a RAG thing with LangChain".

A couple of Buildcamp examples that fit this pattern:

- Bug Report Telegram Bot: takes voice messages, classifies them across repositories, structures them, evaluates bug quality, and opens GitHub issues with deployment and monitoring in the loop[^2]
- AI Engineering Job Market Explorer: uses job-listing data to suggest what skills to learn next and what companies match a profile[^2]

## Course projects

Course projects work differently. You aren't trying to build your life's mission. You're trying to build something that fits the course and lets you practice the whole engineering loop.

In Buildcamp, a strong course project takes you through five things: identify a real problem, build a simple proof of concept, improve the code and add tests, add monitoring and collect usage data, and evaluate how well it works[^4]. That's the reason the course pushes project work into week 1 instead of saving it for the end[^4][^5]. A course project needs to be small enough to start on day one, and structured enough that you can keep improving it week by week.

The common mistake here is choosing something too big or too vague, and then spending weeks stuck on scoping instead of building. If you can start a repo in week 1 and already have something running that you can test, monitor, and evaluate, you're in good shape.

A couple of Buildcamp examples that fit well as course projects:

- Medical Chart Generator: transcribes a patient-doctor conversation and turns it into a structured chart[^2]
- Documentation Chatbot with Handoff: answers support questions from grounded documentation and hands off when confidence is low[^3]

## Small self-projects

Self-projects come from everyday friction. For me, these are often the best starting point. The user is obvious (it's you), the feedback loop is short, and the first version can stay small and still be useful.

My own self-projects almost always start the same way. I'm already working on something real, I notice something annoying, suboptimal, or missing, and I build a small tool that removes that friction. I'm not usually trying to invent a project from zero - I'm already in the middle of some other workflow, I hit a pain point, and the next project is the tool that fixes it.

One thing that helps is keeping a running note of small annoyances. Most of them won't become projects. A few of them will turn into exactly the kind of small, useful, finishable tool that's worth building - and those also make good portfolio pieces later, because you can tell a concrete story about the problem and the fix.

<!-- TODO: link relevant Alexey On Data Substack articles with examples of projects that started from day-to-day friction -->

A couple of Buildcamp examples that fit this pattern:

- Voice-to-Todo Agent: talks to a todo app instead of making you type tasks manually[^3]
- Restaurant Receipt Splitter: takes a photo of a bill, extracts line items, and splits the total among a group[^2]

## Narrowing down from an idea

Even once you know which kind of project you're doing, an idea isn't a project yet. You still need to narrow it down to something you can actually start this week. The trap most people fall into is technology-first thinking - "I want to build an agent" or "I want to use RAG" - which makes it hard to tell when you're done, and easy to over-engineer the thing before you've even written a useful version[^4].

The way I get past that is to force myself to answer five questions in a few sentences each. Who is the user. What is the input. What is the output. What is the smallest useful version. And how will I know it works. If I can't answer those cleanly, the project is still too vague and I keep going.

Once I can answer them, I check the idea against the type of project I'm building. For a portfolio project, I ask whether it shows the kind of work I want to be hired for. For a course project, I ask whether I can test it, monitor it, and evaluate it over several weeks. For a self-project, I ask whether I'll actually use this in my own life soon.

After that, I start. The first rough repo and README teach me more than another hour of browsing idea lists.

The Buildcamp "From Idea to Submission" material splits this into three situations based on where you're starting from[^5]. If you already have an idea, you run a quick fit check and submit it. If you have a vague idea, you talk it through until it fits in two or three sentences. If you have no idea yet, you browse examples for inspiration, then use an interview-style prompt to pull problems out of your own life. That last path uses the project-idea brainstorming prompt from the Buildcamp gist[^6], which works well paired with a fit-check prompt - one helps you generate candidate ideas, the other helps you reject weak ones.

## The capstone bar

For Buildcamp capstones, the standard is fairly simple[^4]. Solve a real problem that someone actually cares about. Use data or inputs you can get without heroic effort. Leave a clear path to testing, monitoring, and evaluation from the start. RAG and agents can help, and some projects genuinely need them, but they aren't the point of the project. Don't bolt them on just to make the project sound more advanced[^4].

The same bar works outside the course too. A project that solves a real problem with honest data and can be tested, monitored, and evaluated is far more valuable than a showier project that can't be.

And if you're planning to talk about this project in interviews later, the field guide makes one thing very clear: hiring managers can tell the difference between a course you followed step by step and something you built yourself[^8]. A project you genuinely owned - where you chose the problem, scoped it, hit real issues, and fixed them - gives you something to talk about for the whole interview, because you lived through it.

## If you're still stuck

If after all of this you still don't have an idea, stop reading idea lists for a moment and try this instead. For the next two days, keep a short note called "annoying things" and write down repetitive workflows, frustrations, and delays as they happen. Then pick one item that feels both useful and finishable, write a one-paragraph project card for it, and start version 1.

You don't need the perfect idea. You need a real problem, a small scope, and a reason to start now.

## Sources

[^1]: [Project Ideas for Your AI Capstone](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/03-cohort-1-project-ideas.md)
[^2]: [Cohort 2 Project Ideas](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/04-cohort-2-project-ideas.md)
[^3]: [Other Project Ideas](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/05-other-project-ideas.md)
[^4]: [Project Work overview](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/01-section-overview.md)
[^5]: [From Idea to Submission](../../ai-engineering-buildcamp/v2/01-foundation/07-project-work/02-from-idea-to-submission.md)
[^6]: [Project Ideas: Prompts for Getting Unstuck](../../ai-engineering-buildcamp/gist-prompts/00-project-ideas.md)
[^7]: [20260423_182032_AlexeyDTC_msg3559_transcript.txt](../inbox/used/feedback/20260423_182032_AlexeyDTC_msg3559_transcript.txt)
[^8]: [AI Engineering Field Guide - Portfolio](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/portfolio/README.md)
