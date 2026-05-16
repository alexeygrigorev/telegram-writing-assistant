---
title: "Design Thinking for Finding Project Topics"
created: 2026-03-05
updated: 2026-03-20
tags: [research, projects, design-thinking, teaching]
status: draft
---

# Design Thinking for Finding Project Topics

Many students and people in general struggle with finding project ideas. They have time, motivation, and willingness, but ideas don't come naturally. This is especially important in Zoomcamps, where guidance from the instructor side is minimal and a lot depends on the participants' own enthusiasm[^1].

Despite offering help, datasets, and suggestions, people still find it hard to pick a project. The goal is to create a general framework - a set of questions people can answer to figure out what they want to build. This framework should work for any course, not just a specific one[^1].

## Why problem finding matters

The book "To Sell is Human" by Daniel Pink discusses the difference between problem finders and problem solvers in chapter 7. Research shows that problem finders are more successful in life[^7].

Short-term results: experts rated the work of problem finders as more creative. Long-term results (18 years later): problem finders became significantly more successful artists, as measured by the artistic community's criteria. The key quote from the research: "The quality of the found problem predicts the quality of the solution"[^7][^8].

<figure>
  <img src="../../assets/images/design-thinking-for-projects/problem-finders-research.jpg" alt="ChatGPT summary of problem finders research results">
  <figcaption>Research results on problem finders: short-term creativity and long-term career success</figcaption>
  <!-- Screenshot from the book discussion showing the key research findings about problem finders -->
</figure>

This serves as motivation for the framework below. People who are more skilled at finding problems, not just solving them, are generally more successful. This is a useful skill worth learning, and like any other skill, it just requires the right approach and willingness to practice[^7].

## How projects emerge naturally

For some people, finding projects is not a problem at all. The problem is the opposite - there are more ideas than free time. Here is how projects naturally come up[^2][^3][^4]:

## Source 1: Noticing suboptimal things while working

The most reliable source of project ideas is simply doing things - working on projects, pet projects, anything. While working, things come up that are suboptimal, could be improved, or have no existing solution[^3][^4].

Example from today: while working on a course, a lecture needed a Mermaid diagram converted to an image. During the video recording, the diagram was drawn on a tablet. But when converting to course notes (Markdown to HTML to Maven), Mermaid diagrams don't automatically become images[^2].

There is a templating system for course content preparation - a Markdown document template where content gets inserted. The next step is converting Markdown to HTML. At this stage, Mermaid diagrams need to be rendered as images[^2].

Looking for a Python solution, the only library available internally launches a browser to render SVG. This works for one or two images but is slow and inconvenient for large volumes. There is no Python API for it. A Rust library exists but was not explored. Claude Code was asked to implement a Python solution instead[^2].

This is how many libraries and projects were born: MinSearch, CQ, LightSearch. They all appeared because there was no existing solution for a specific need. For example, there was surprisingly no suitable in-memory search library for Python. The problem was solved relatively quickly even before AI assistants were popular. More time was spent figuring out how to publish the library than writing it[^4].

## Source 2: Wanting to understand how something works

The best way to understand something is to implement it yourself. Now with AI agents, you don't even have to implement it yourself - the agent writes the code and you understand how things work by reading it[^3].

Example: the automatic SSH port forwarding project. After getting a new server, the goal was to automatically forward ports from anything running on the server to localhost through the firewall, keeping everything blocked except SSH (port 22). A solution might already exist, but the point was to understand how it works[^3].

## Source 3: Someone asks a question

Hearing questions frequently leads to project ideas. This happens at meetups and other events where people ask how to do something or what the current state of something is[^5].

Example: a student asked what tasks AI Engineers get in interviews. This was so interesting that it turned into a whole series about AI Engineers[^5].

## The goal

The goal is to help people who don't find ideas as naturally. Many people have no ideas and don't know what to implement. If they just need any project, they can ask and get one. But if they want something personal, a framework or set of questions would help them discover what they want to build[^1][^5].

A ChatGPT conversation explored this topic using Design Thinking methodology and several other frameworks[^6].

## Frameworks for idea generation

The ChatGPT conversation identified several established frameworks that can be adapted for helping students find project ideas[^6]:

## Design Thinking

The most popular approach for student projects. The standard framework for finding product or project ideas.

The core logic has 5 stages:

1. Empathize - understand the user or yourself
2. Define - formulate the problem
3. Ideate - generate ideas
4. Prototype
5. Test

For choosing a project idea, the first three stages are enough.

Questions for students:

Life context:
- What tasks repeat every week?
- What annoys you or takes too much time?
- What do you constantly do manually?
- What tasks could be automated?

Problem:
- What exactly is inconvenient in this process?
- Who else faces this problem?
- Why is this a problem?

Technology opportunity:
- Can this be solved with ML, data engineering, automation, API, scraping, or AI?

Validation:
- Can an MVP be built in 2-6 weeks?
- Is there data available?
- Is there a success metric?

## SCAMPER

A checklist method for creative thinking through directed questions: Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse.

Example: if a student chose "task calendar" as a theme, SCAMPER questions help explore it from different angles - can ML replace something? Can calendar be combined with email and notes? Can it be made real-time or into a recommender?

## CDIO framework

A popular model in engineering universities: Conceive, Design, Implement, Operate. Questions guide students from "what do we want to improve?" through "how will it work?" to "how to verify it works?"

## Engineering idea generation framework

From engineering literature, ideas go through 4 stages: Framing (problem context), Ideation (generating ideas), Selection (choosing an idea), Evaluation (assessment).

## Universal Design Thinking framework for choosing a project

An adapted version simplified to 4 steps, designed to work for anyone - students, professionals, freelancers, hobbyists[^6]:

## Step 1: Observe - observation of life

Goal: find real problems. Best projects come from work, personal life, hobbies, information, data, digital tools.

Question blocks:

Daily life:
- What tasks do I do every week?
- What processes take too much time?
- What do I do manually?
- What tasks repeat?

Digital tools:
- What apps do I use every day?
- What is inconvenient in them?
- What is missing?
- What do I constantly copy between services?

Work:
- What processes at work are inefficient?
- What tasks can be automated?
- Where do people spend too much time?

Information:
- What is hard to find?
- What data is hard to analyze?
- What knowledge is hard to organize?

Data (especially useful for AI projects):
- What data do I already have?
- What data can be collected?
- What data does nobody analyze?

Exercise: make a list of at least 20 problems. Problems can be small. The first ten ideas are almost always obvious - the interesting ones come after.

## Step 2: Define - formulate the problem

Pick 3-5 problems from the list and turn them into clear formulations.

Wrong: "I want to make an AI project."
Right: "Students spend too much time searching for learning materials."

Clarifying questions: Who faces the problem? How often does it occur? Why is it a problem? What happens now?

## Step 3: Ideate - generate solutions

Generate many solutions. Questions to drive generation:

- Can this be automated?
- Can something be predicted?
- Can something be recommended?
- Can something be classified?
- Can information be extracted?

## Step 4: Select - choose a project

Evaluate ideas using a matrix:

- Interest: is it interesting to work on?
- Usefulness: does it solve a problem?
- Feasibility: can it be done?
- Data: is data available?

After selection, answer technical questions: what data is needed, what is the input, what algorithm is used, what does the system output, how to measure success.

## Key insight

Research in engineering education shows that students struggle with ideas because they start with the technology, not with the problem. The wrong approach: "I'll make an ML project." The right approach: "There is a problem, and it can be solved with ML."

The best projects sit at the intersection of interest, problem, and technology.

## Idea sources for students

Five categories of project ideas that help students think in the right direction:

1. Task automation
2. Data analysis
3. AI assistants
4. Recommendation systems
5. Information search

## Running this as a workshop

The framework can be delivered as a 1-hour workshop:

1. Stage 1 (10 min) - list problems
2. Stage 2 (10 min) - select 3 problems
3. Stage 3 (15 min) - generate 10 solutions
4. Stage 4 (10 min) - evaluate ideas
5. Stage 5 (10 min) - formulate the project

See also: [Project Discovery AI Agent](project-discovery-agent.md) - an AI agent that facilitates this process through guided sessions.

## Sources

[^1]: [20260305_142756_AlexeyDTC_msg2744_transcript.txt](../../inbox/used/20260305_142756_AlexeyDTC_msg2744_transcript.txt)
[^2]: [20260305_143249_AlexeyDTC_msg2746_transcript.txt](../../inbox/used/20260305_143249_AlexeyDTC_msg2746_transcript.txt)
[^3]: [20260305_143447_AlexeyDTC_msg2748_transcript.txt](../../inbox/used/20260305_143447_AlexeyDTC_msg2748_transcript.txt)
[^4]: [20260305_143650_AlexeyDTC_msg2750_transcript.txt](../../inbox/used/20260305_143650_AlexeyDTC_msg2750_transcript.txt)
[^5]: [20260305_144010_AlexeyDTC_msg2752_transcript.txt](../../inbox/used/20260305_144010_AlexeyDTC_msg2752_transcript.txt)
[^6]: [20260305_145128_AlexeyDTC_msg2754.md](../../inbox/used/20260305_145128_AlexeyDTC_msg2754.md)
[^7]: [20260320_070215_AlexeyDTC_msg3027_transcript.txt](../../inbox/used/20260320_070215_AlexeyDTC_msg3027_transcript.txt)
[^8]: [20260320_070215_AlexeyDTC_msg3026_photo.md](../../inbox/used/20260320_070215_AlexeyDTC_msg3026_photo.md)
