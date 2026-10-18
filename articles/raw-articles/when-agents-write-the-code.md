---
title: "Agentic Engineering"
created: 2026-10-11
updated: 2026-10-11
tags: [agentic-engineering, coding-agents, verification, hugo-bowne-anderson, lightning-lesson]
status: draft
---


A few weeks ago [Hugo Bowne-Anderson](https://substack.com/@hugobowne) and I ran a webinar about trends in AI Engineering.

https://youtu.be/whIdxTQsU0A

At the beginning, Hugo defined two terms that people nowadays often confuse:

- AI engineering, where AI is part of the product
- Agentic engineering, where agents help you build the product

<figure>
  <img src="../../assets/images/when-agents-write-the-code/agentic-vs-ai-engineering.jpg" alt="Slide from Hugo's talk comparing agentic engineering, building software with agents where the agent is part of the development team, with AI engineering, building AI-powered products where AI is part of the product">
  <figcaption>Hugo's slide: in agentic engineering the agent is part of the development team</figcaption>
</figure>

At the end of the session we decided to write based on what we talked about. Since we covered both topics, I decided to split the article into two parts. The [first article about AI engineering](https://aishippingblog.com/p/trends-in-ai-engineering) was published earlier this week. This one is about agentic engineering.

In particular, I'll cover:

- How agents changed the way we write code
- Why verification is now the bottleneck
- Dealing with sloppy agent code
- Using good books and rules to help agents write better code
- Organizing work across multiple agents
- Dark software factories

TODO update the outline


## TODO Our work has changed (?)

Hugo ran a survey on how people do agentic engineering in data science. 34 people said that AI changed their worflow "fundamentally", and 39 said "significantly".

Hugo wanted to see what exactly was different, so he followed up and visualized the results with a heatmap.

TODO: use codex imagegen to regenerate it in high-res and remove all the artifacts/noise 
<figure>
  <img src="../../assets/images/when-agents-write-the-code/agentic-verification-heat-map.jpg" alt="Heat map of verification methods by how much AI agents changed people's workflow. In the group whose workflow changed fundamentally, 59% ask another agent to critique the work and 62% write tests">
  <figcaption>From Hugo's survey: how people verify AI-generated work, grouped by how much agents changed their workflow</figcaption>
</figure>

Amonth the significant and fundamental groups, 59% ask another agent to critique the work.

The less impact people reported, the less common this practice was. It's not causal, but the people who changed their workflow the most also verify using agents the most.

## Agents Controlling Agents

Even frontier models give you pages and pages of absolute slop. With this amount of output it's very hard to review every line of code ourselves, so we use agents to control agents.

I call it the "implementer-reviewer" pattern.

The implementer is doign the work, and the reviewer is validating it. They iterate until the second agent accepts the output of the first agent.

It works very well for coding. The implementer is a software engineer working on a task, and the reviewer is a tester whose goal is to find holes in the implementation. A feature may take a few hours instead of 20 minutes, but the quality at the end is better.

<figure>
  <img src="../../assets/images/when-agents-write-the-code/adversarial-loop.png" alt="An implementer agent builds, a reviewer agent checks the result against shared rules such as a design system or Clean Code, and sends rejected work back until it accepts it">
  <figcaption>One agent builds, another tries to reject the result</figcaption>
</figure>
TODO: let's remove the subtitles from the last row 

It works outside of coding tasks too.

Agents usually produce terrible and complicated designs, so I use the same implementer-reviewer approach:

- The implementer is a designer, who creates the interface
- The reviewer is a senior designer who tries to find reasons to reject the design 

They share a design system and a rubrik for evaluating the interface. After each iteration the senior designer scores the system, and they iterate until the score is 10/10.

I call this "adversarial design" (todo include the link).

TODO add the screenshot from the adversarial design

TODO find a way to include my artcile about design - like if you want to know how do I approach design wtih AI as a non-designer you can check this article

## Rules for Coding

The implementer and reviewer need a common set of rules. For coding tasks, it can be the acceptance criteria and the coding standards document. For design, it's the design system and the evaluation rubrick.

But instead of describing the entire system and list all the criteria, I often take a shortcut and refer to books.

For coding, I can say "follow the principles from the Clean Code book by Robert Martin", then code improves.

Sometimes I add details to make it more specific:

- Functions no longer than 30 lines
- Files no longer than 300 lines

TODO: add picture of clean code

Referencing a well-known book is a convenient way for getting better quality results.

I tested these rules on a fairly large and relatively old codebase. I started it in 2023. I developed it with AI, first by copy-pasting from ChatGPT and then fully with coding agents. When the code inevitably turned into a pile of slop, I asked the agent to refactor the entire coodebase using these this approach.

It took two banked Codex resets, but after that I could read the code without crying.

## Rules for Writing

Hugo does the same for writing with Strunk and White's The Elements of Styledd. Its rules include "omit needless words" and "use the active voice".

The agents don't always follow them, so he runs three extra verification agents in parallel. Then there a final agent performs the edit.

<figure>
  <img src="../../assets/images/when-agents-write-the-code/editing-pipeline.png" alt="AGENTS.md with the Strunk and White rules feeds three verification agents that work in parallel, and an editor agent makes the final edit">
  <figcaption>Hugo's editing setup: three checkers in parallel, then one editor</figcaption>
</figure>


## Organizing Agents Like a Team

In the implementer-reviewer pattern we have two agents. But we can scale this idea to a full team by adding a product manager and on-call engineer.

You describe the reponsibilities of each team member, and let them work together on a project:

- PM grooms the tasks and adds acceptance criteria
- Software engineer implements the task
- QA engineer checks that the code works against the criteria
- PM runs acceptance tests though a browser
- On-call engineer makes sure that CI/CD stays green 
 
I described this approach in detail in my <TODO team of agents article> and [the first lesson of the AI Dev Tools Zoomcamp course](TODO add link).

When [OpenAI announced its Navier-Stokes result](https://techspot.com/news/113785-openai-claims-10000-ai-agents-solved-one-mathematics.html), I read the article too. I don't know much about math and I didn't even know that Navier-Stokes existed, but I still found the article quite interesting. The the most interesting part was how exactly they achived this result - by 10,000 running agents in parallel.

It took me quite some time to figure out the setup with one team of 5 agents, and I still haven't nailed scaling it to a departament (although I think I'm pretty close). So getting this up to a whole enterprise-lever corporation and organizing it across 10,000 agents is really the next level.

Natutally, I startied thiniking how I'd organize this work. IN my mind, this requires a hierarchy:

- a chief scientist setting the directios
- heads controlling each part of their work
- many agents under them trying to explore a different part of the solution space


<figure>
  <img src="../../assets/images/when-agents-write-the-code/agent-hierarchy.png" alt="Tree diagram: a chief scientist agent assigns approaches A, B, and C to three team lead agents, and each team lead directs its own team of agents">
  <figcaption>How I would organize 10,000 agents</figcaption>
</figure>

I probably will never have a problem that will require 10,000 agents, but now I can reliably manage 30-50. 

TODO: add a teaser from my cloudflare competition where I tried 

## Dark Software Factories

I recently had a chat with a company that has a policy of "no handwritten code". There, you aren't allowed to write code yourself, only through an agent. When some engineers threathened to resign, the company said "nobody is forcing you to work here, you're welcome to explore other options". 

TODO Transition?

Today we write code very differently compared to one year ago. Even half a year ago I was still checking my code from time to time, but now I only do that when I prepare materials for my workshops and courses.

When a team of agents is working through your backlog, you can imagine a conveyor belt with features processed by the agents. That's a software factory.

TODO add illustation via imagegen

Hugo takes this futher and describes a dark software factory. A dark factory is factory with no humans, only robots build robots. SO there's no light inside. 

TOOD find pcitures on the internet from it

In a dark software factory, humans aren't allowed to look at the code. They get artifacts that let them make business decisions and verify that everything is correct, but they're separated from the generated code.

<figure>
  <img src="../../assets/images/when-agents-write-the-code/dark-factory.png" alt="You give specs to a dark factory where agents build and verify the code and nobody reads it, and the factory returns artifacts such as dashboards and cards, which you accept or reject">
  <figcaption>In a dark software factory you work with specs and artifacts, never with the code</figcaption>
</figure>

Hugo doesn't suggest that everyone should start building a dark software factory today. But he thinks that's soon it will be economically viable to skip reading code and focus on the business.

Just like we don't read machine code anymore because we trust compilers, we can trust our agents by following good software engineering processes and practices. 

And I agree. I'm a solo founder, so my time is very limited. If I check everything that agents write, I will be the bottleneck. But once I let the agents run without my involvement, I can focus on more high-level and impactful work.


## XXX

TODO Short conclusion