---
title: "Trends in Agentic Engineering"
date: 2026-10-20
url: https://aishippingblog.com/p/trends-in-agentic-engineering
---

A few weeks ago [Hugo Bowne-Anderson](https://substack.com/@hugobowne) and I ran a webinar about trends in AI engineering.

At the beginning, Hugo defined two terms that people often confuse:

* AI engineering - AI is part of the product
* Agentic engineering - agents help you build the product

[![Slide from Hugo's talk comparing agentic engineering, building software with agents where the agent is part of the development team, with AI engineering, building AI-powered products where AI is part of the product](https://substackcdn.com/image/fetch/$s_!xq9d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66e70343-401e-4420-a80c-fccced6775cc_1600x902.jpeg)](https://substackcdn.com/image/fetch/$s_!xq9d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66e70343-401e-4420-a80c-fccced6775cc_1600x902.jpeg)

Hugo’s slide: in agentic engineering the agent is part of the development team

At the end of the session we decided to write an article about the webinar. When I started writing it, I realized that it makes sense to cover each topic separately. Last week I published [the first article about AI engineering](https://aishippingblog.com/p/trends-in-ai-engineering), and in this article, I focus on agentic engineering.

In particular, I’ll cover:

* Using one agent to review another’s code and designs
* Giving agents rules for coding and writing
* Organizing agents into teams and larger hierarchies
* Running software factories where humans focus on outcomes

## **Verifying Agent-Generated Work**

Hugo ran a survey on how people do agentic engineering in data science. 34 people said that AI changed their workflow “fundamentally”, and 39 said “significantly”.

Hugo wanted to see what exactly was different, so he followed up and visualized the results with a heatmap.

[![Heat map of verification methods by how much AI agents changed people's workflow. In the group whose workflow changed fundamentally, 59% ask another agent to critique the work and 62% write tests](https://substackcdn.com/image/fetch/$s_!1uB2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F009c5f5a-bf85-4fbd-a69d-8005efbc854a_1703x924.png)](https://substackcdn.com/image/fetch/$s_!1uB2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F009c5f5a-bf85-4fbd-a69d-8005efbc854a_1703x924.png)

Hugo’s survey, redrawn for readability: verification methods grouped by how much agents changed people’s workflow

Among people whose workflow changed fundamentally, 59% ask another AI tool or agent to critique the work. In the significantly changed group, it’s 54%.

The less impact people reported, the less common this practice was. It’s not causal, but the people who changed their workflow the most also verify using agents the most.

I can clearly see the reason: the more you delegate your work to agents, the more you need to check the output.

## **Agents Controlling Agents**

Even frontier models give you pages and pages of absolute slop. With this amount of output it’s hard to review every line of code ourselves, so we use agents to control agents.

I call it the “implementer-reviewer” approach.

I have the implementer do the work and the reviewer validate it. I let them iterate until the second agent accepts the output of the first agent.

For coding, I assign one agent to implement the task as a software engineer. Then I ask another to act as a tester and find problems in the implementation. A feature may take a few hours instead of 20 minutes, but the quality at the end is better.

[![I ask an implementer agent to build and a reviewer agent to check the result against shared rules such as a design system or Clean Code, sending rejected work back until it accepts it](https://substackcdn.com/image/fetch/$s_!yf4V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fded229-a370-45b3-8b4a-bac5cdda0115_1080x360.png)](https://substackcdn.com/image/fetch/$s_!yf4V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fded229-a370-45b3-8b4a-bac5cdda0115_1080x360.png)

I ask one agent to build and another to try to reject the result

It works outside of coding tasks too.

Agents usually produce terrible and complicated designs, so when I need to work on UI, I use the same implementer-reviewer approach:

* The implementer is a designer who creates the interface
* The reviewer is a senior designer who tries to find reasons to reject the design

I give both agents a design system and a rubric for evaluating the interface. After each iteration I have the senior designer score the interface, and I have them iterate until the score is 10/10.

I call this [adversarial design](https://github.com/alexeygrigorev/.agents/blob/main/skills/adversarial-design-review/SKILL.md).

[![My instructions for an implementer and an independent senior design reviewer in the adversarial design review skill on GitHub](https://substackcdn.com/image/fetch/$s_!PZXW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5f3e69a-45f2-4478-9336-3b7809329b2b_957x645.png)](https://substackcdn.com/image/fetch/$s_!PZXW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5f3e69a-45f2-4478-9336-3b7809329b2b_957x645.png)

The skill that defines the designer and reviewer roles

> Interested in how I approach design with AI? I described my approach here:
>
> [AI Design for Non-Designers](https://aishippingblog.com/p/ai-design-for-non-designers)

## **Shared Rules for Coding and Design**

In these cases both the implementer and reviewer share a common set of rules:

* For coding tasks - the acceptance criteria and a coding standards document
* For design - a design system and an evaluation rubric

But instead of describing the entire system and listing all the criteria, I often take a shortcut and refer to books.

[![Cover of Clean Code: A Handbook of Agile Software Craftsmanship by Robert C. Martin](https://substackcdn.com/image/fetch/$s_!dp61!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72f34540-474f-4736-912d-10ec8986f3ce_1024x1353.jpeg)](https://substackcdn.com/image/fetch/$s_!dp61!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72f34540-474f-4736-912d-10ec8986f3ce_1024x1353.jpeg)

Clean Code by Robert C. Martin. Cover: [Pearson / InformIT](https://www.informit.com/store/clean-code-a-handbook-of-agile-software-craftsmanship-9780132350884)

For coding, I can say “follow the principles from the Clean Code book by Robert Martin”. I use that instruction to improve code quality.

In some cases I add details to make it more specific:

* Functions no longer than 30 lines
* Files no longer than 300 lines

I tested these rules on [a fairly large codebase I started in 2023](https://github.com/DataTalksClub/course-management-platform). I developed it with AI, first by copy-pasting from ChatGPT and then fully with coding agents. When the code turned into a pile of slop, I asked the agent to refactor the entire codebase using this approach.

It took two banked Codex resets, but after that I could read the code without crying.

This is how [some functions](https://github.com/DataTalksClub/course-management-platform/blob/0b9ed3152d5420813e86f56d8f14cb72f82ead4e/courses/homework_score_calculation.py) now look like:

```
def submission_total_score(submission: Submission, questions_score_value: int):
    lip_score = update_learning_in_public_score(submission)
    faq_score = update_faq_score(submission)
    return questions_score_value + lip_score + faq_score
```

## **Rules for Writing**

Hugo does the same for writing with The Elements of Style from Strunk and White. Its rules include “omit needless words” and “use the active voice”.

The agents don’t always follow them, so he runs three extra verification agents in parallel. Then he has a final agent edit the text.

[![Hugo gives three verification agents the Strunk and White rules in AGENTS.md, runs them in parallel, then has an editor agent edit the text](https://substackcdn.com/image/fetch/$s_!AmyJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aab3fa0-2881-4f1b-95db-0769164f7f20_1100x440.png)](https://substackcdn.com/image/fetch/$s_!AmyJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aab3fa0-2881-4f1b-95db-0769164f7f20_1100x440.png)

Hugo’s editing setup: three checkers in parallel, then one editor

## **Organizing Agents Like a Team**

With an implementer and reviewer we have two agents. But we can scale this idea to a full team by adding a product manager and on-call engineer.

We give each agent a job and ask them to work together on a project:

* PM plans the tasks and adds acceptance criteria
* Software engineer implements the task
* QA engineer checks that the code works against the criteria
* PM runs acceptance tests through a browser
* On-call engineer makes sure that CI/CD checks pass

I described this approach in [I Built an AI Agent Team for Software Development](https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software) and in [AI-Native Development: Specifications, Loop and Graph Engineering](https://aishippingblog.com/p/ai-native-development-specifications).

When I read [OpenAI’s Navier-Stokes result](https://openai.com/index/navier-stokes-solution/), I found it interesting. I know little about the mathematics. But the report described 10,000 agents running in parallel, and I tried to imagine how I’d manage that too.

It was interesting for me because it’s far from trivial. It took me quite some time to figure out how to run a single team of five agents. I still haven’t made a department of teams work reliably, although I hope I’m pretty close.

I experimented with scaling beyond one team - most recently while working on [Cloudflare’s Git platform competition](https://alexeygrigorev.com/cloudflare-agent-git/). Keeping them working was harder than I imagined. The agents were failing, stalling, or waiting for my input or approval. They do that even with `--dangerously-skip-permissions`, sometimes producing no output for hours or days.

[![Conceptual illustration: an unread message waits beside an idle agent while requests are moved onto an open task board.](https://substackcdn.com/image/fetch/$s_!W75b!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5d195ba-bf09-43a8-8947-077069858a01_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!W75b!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5d195ba-bf09-43a8-8947-077069858a01_1536x1024.png)

Illustration from [a daily competition report](https://alexeygrigorev.com/cloudflare-agent-git/daily/2026-10-07/): “an unread message waits beside an idle agent while requests are moved onto an open task board.”

I did get some teams working, and now I can run 30-50 agents in parallel working on different projects. I’ll definitely write more about them soon.

I’ll probably never have a problem that requires 10,000 agents, but if I needed that, I’d organize them into a hierarchy:

* A chief scientist setting the direction
* Team heads coordinating each part of the work
* Many agents under them exploring different approaches

[![Tree diagram: I would ask a chief scientist agent to assign approaches A, B, and C to three team lead agents, and ask each team lead to direct its own team of agents](https://substackcdn.com/image/fetch/$s_!GwJM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3d1bc72-76ca-441f-97eb-9e9cae2164fc_1060x580.png)](https://substackcdn.com/image/fetch/$s_!GwJM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3d1bc72-76ca-441f-97eb-9e9cae2164fc_1060x580.png)

How I would organize 10,000 agents

With so many agents running in parallel, you can’t expect humans to be able to review any of this code.

## **Dark Software Factories**

I recently had a chat with a company that has a policy of “no handwritten code”. There, you aren’t allowed to write code yourself, only through an agent. When some engineers threatened to resign, the company said “nobody is forcing you to work here, you’re welcome to explore other options”.

Our industry has changed significantly over the last year. Today we write code differently. Even half a year ago I was still checking my code from time to time, but now it’s over. I do this only when I prepare materials for my workshops and courses.

Some time ago I heard the term “software factory”. It made sense to me: you have a team of agents and they work through your backlog. So I can imagine a conveyor belt of features, each agent is adding something to it, and the result is a product.

Hugo takes this further and describes a dark software factory. The name comes from lights-out manufacturing: when machines work without people on the factory floor, there’s no need to keep the lights on. [FANUC’s factories](https://en.wikipedia.org/wiki/Lights_out_%28manufacturing%29#Existing_%22lights-out_factories%22) are a physical example of this kind of automation.

![Yellow industrial robots in FANUC's robot factory in Japan](https://substackcdn.com/image/fetch/$s_!2buf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07dece2b-82ab-4653-8e15-5627fde4c132_320x213.jpeg)

FANUC’s robot factory. Photo: [FANUC](https://www.fanuc.co.jp/en/profile/production/factory1.html), which describes automatic transport and continuous testing of assembled robots

In a dark software factory, humans aren’t allowed to look at the code. They get artifacts that let them make business decisions and verify that everything is correct, but they’re separated from the generated code.

![You give specs to a dark factory. Agents build and verify code without human code review, then return dashboards and cards for you to accept or reject](https://substackcdn.com/image/fetch/$s_!ON2F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F007e7d7c-9d6a-46d5-a3e5-913e11172519_1122x264.png)

In a dark software factory you work with specs and artifacts, never with the code

Hugo doesn’t suggest that everyone should start building a dark software factory today. But he thinks it’ll soon be economically viable to skip reading code and focus on the business.

He compares this to trusting compilers without reading the machine code they produce. With agents, we need tests, independent checks and clear specifications to earn that trust.

I agree with that direction. I’m a solo founder with limited time, so if I check everything that agents write, I’ll never be able to finish anything. Once I let the agents run without my involvement, I can spend more time on product and architecture decisions.

I started reading more about dark software factories and realized that I’ve been doing some of this for quite some time too. I’m writing a separate article to explore how other people keep their factories running and what I can learn from them.

## **Keeping the Factory Running**

Humans are still needed to keep the factory running. First of all, it doesn’t just happen, people build it. And once it’s running, it needs attention. Even the FANUC factory needs a maintenance every month.

It’s the same with agents. You can polish your process and let your agentic teams run unsupervised, but only up to a point. Eventually, you’ll still become the bottleneck - or else the agents will build something you don’t need.

And we’re still learning how to build it.

[Share](https://aishippingblog.com/p/trends-in-agentic-engineering?utm_source=substack&utm_medium=email&utm_content=share&action=share)
