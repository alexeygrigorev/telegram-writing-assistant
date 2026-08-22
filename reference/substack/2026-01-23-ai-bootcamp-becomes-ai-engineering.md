---
title: "AI Bootcamp Becomes AI Engineering Buildcamp, with 90% of the Course Re-Recorded"
date: 2026-01-23
url: https://aishippingblog.com/p/ai-bootcamp-becomes-ai-engineering
---

## One Thing I Want to Share This Week

I have a few important updates about my [AI agents course](https://maven.com/alexey-grigorev/from-rag-to-agents?promoCode=SUBSTACK):

1. I’ve renamed the course
2. Significantly restructured it
3. Expanded the optional framework coverage

All of these changes are a result of feedback from the participants of the first cohort.

Based on that feedback, I’m re-recording around 90% of the material for the [second cohort](https://maven.com/alexey-grigorev/from-rag-to-agents?promoCode=SUBSTACK), which starts in 2 days.

In this newsletter, I want to explain why the name changed, how the course was redesigned, and share what’s new in this iteration.

### 1. New Name: AI Engineering Buildcamp

I decided to rename the course because the new name better reflects what it is about: building AI systems with an engineering mindset through hands-on work instead of learning theory in isolation.

Each course participant will:

* Build real systems
* Practice an engineering mindset (trade-offs, reliability, maintainability)
* Do a lot of hands-on work
* Finish with concrete, reusable results

[![Image 1](https://substackcdn.com/image/fetch/$s_!uUjQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fbcca97-29b7-48d0-9eb1-50efc519e437_1472x916.png)](https://substackcdn.com/image/fetch/$s_!uUjQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fbcca97-29b7-48d0-9eb1-50efc519e437_1472x916.png)

AI Engineering Buildcamp is a project-driven course.

From the first week, course participants start working toward their final Capstone Project. In Week 1, participants define what they want to build. As the course progresses, they gradually refine this idea, first conceptually and then through implementation, with the final two weeks dedicated entirely to building and polishing the system.

Alongside the Capstone, course participants work on 6+ guided mini-projects through homework assignments. These include FAQ assistants, YouTube Q&A systems, documentation agents, coding agents, and deep research agents. These smaller projects are designed to reinforce individual topics and support gradual material absorption, independent of the final Capstone.

### 2. New Structure

Some of the AI Engineering Buildcamp course participants from the first cohort shared this feedback with me:

> “The content is extremely dense and valuable, but the pace felt too fast.”

The new structure maintains the same technical depth and focus of the course but makes it realistic for people with full-time jobs to follow, complete, and apply the material.

The new version is longer, less dense, and more focused:

* There is now a main path built around one primary framework and a selected set of projects.
* Each module also includes optional bonus material for those who want broader coverage, alternative tools, or additional hands-on work.

In other words, there’s a clearer separation between core material and optional depth, so you can easily understand where to put your focus. And you also have more time to process concepts and practice.

[![Image 2](https://substackcdn.com/image/fetch/$s_!8q0_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f4b8266-b828-4cc2-bbba-f4ae90d69230_1382x782.png)](https://substackcdn.com/image/fetch/$s_!8q0_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f4b8266-b828-4cc2-bbba-f4ae90d69230_1382x782.png)

A screenshot of a [document with redesigned AI Engineering Buildcamp curriculum](https://docs.google.com/document/d/1n9D_QlIOGQBtFfsxAeFtOW0AK6u3TT6n3MFz3lc0lkM/edit?usp=sharing)

The full redesigned curriculum is already laid out week by week. You can check it out [in this document](https://docs.google.com/document/d/1n9D_QlIOGQBtFfsxAeFtOW0AK6u3TT6n3MFz3lc0lkM/edit?usp=sharing).

### 3. Frameworks Philosophy and Updates

The course is not framework-driven.

The agents section starts without any framework. We first build agents from scratch and implement tool calling and control loops manually. This makes the underlying mechanics explicit before any abstractions are introduced.

This approach allows you to:

* Understand how agent frameworks actually work internally
* Read and reason about framework source code
* Debug unexpected behavior instead of guessing
* Implement your own framework when existing ones do not fit your constraints

Only after this foundation is in place do we introduce PydanticAI and use it as the primary framework throughout the main path. Focusing on a single framework reduces context switching and allows us to go deeper into typing, validation, testing, and production concerns.

We’ll also cover other widely used frameworks as optional material:

* LangChain and LangGraph
* OpenAI Agents SDK
* Google Agent Development Kit
* CrewAI

We use OpenAI as the main model provider, but the course is not tied exclusively to it. We also cover alternatives such as Groq, Anthropic, Gemini, and Z.ai.

This structure keeps the course focused on engineering fundamentals, while still giving participants enough exposure to confidently navigate the broader AI agent ecosystem.

### Join AI Engineering Buildcamp with a Special Discount

[![Image 3](https://substackcdn.com/image/fetch/$s_!h1IF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08cd9cae-2600-48fd-a51f-103da8d84450_2121x1187.png)](https://substackcdn.com/image/fetch/$s_!h1IF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08cd9cae-2600-48fd-a51f-103da8d84450_2121x1187.png)

If you’d like to join the AI Engineering Buildcamp, I’m offering a special discount for newsletter subscribers.

Use the SUBSTACK promo code at checkout to get 20% off the AI Engineering Buildcamp.

The course starts in 2 days.

[Sign up here (20% off)](https://maven.com/alexey-grigorev/from-rag-to-agents?promoCode=SUBSTACK)

## My Experiments

### 1. Using Claude to learn new products

I recently tried using Claude to get up to speed on a new technical product before working with it.

Instead of manually going through documentation, tutorials, and example code, I gave Claude Code the setup instructions and links to the available materials and asked it to explore the product and solve a set of concrete tasks.

After analyzing everything, it produced a structured Markdown document with working examples, practical notes, and pointers to potential pitfalls.

Delegating this exploration to Claude significantly reduced the upfront effort. It helped me quickly understand the core features and identify which parts of the product were worth testing myself, which is especially valuable when documentation is incomplete or fragmented.

### 2. Telegram Assistant

[![Image 4](https://substackcdn.com/image/fetch/$s_!IjU_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83b8b171-bdf3-4a88-8de5-b9aceca8b30b_1888x876.png)](https://substackcdn.com/image/fetch/$s_!IjU_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83b8b171-bdf3-4a88-8de5-b9aceca8b30b_1888x876.png)

I’m building a small writing assistant that works in a Telegram chat and turns my raw ideas into structured notes. I decided to create it to reduce friction between thinking and writing by turning unstructured input into publishable content.

I send text messages, voice notes, screenshots, and files to the Telegram chat with this bot. The bot stores everything, transcribes voice messages, analyzes the materials, and gradually organizes them into article drafts. When I run a processing command, an agent updates existing drafts or creates new ones and commits the result to GitHub.

### 3. Phone-as-server experiment

I’ve also been experimenting with using Claude Code beyond typical coding workflows. I wanted to test my idea of setting up Claude Code on an old Android phone as a lightweight alternative to a cloud instance: install Linux or a minimal Android setup, run Claude Code locally, and connect it to search.

This specific attempt failed due to Samsung’s firmware protections, and the phone briefly turned into a brick before Claude helped me restore it to factory settings. With different hardware, the setup would likely work. Nevertheless, this experiment helped me clarify the boundaries of using Claude Code in unconventional environments.

## What I’ve Been Working On Recently

### 1. Two-Day In-Person Workshop in Berlin

[![Image 5](https://substackcdn.com/image/fetch/$s_!mRG2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad628737-e42c-4581-bd3f-d330c41f8456_1024x768.jpeg)](https://substackcdn.com/image/fetch/$s_!mRG2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad628737-e42c-4581-bd3f-d330c41f8456_1024x768.jpeg)

This week, I ran a two-day, in-person workshop on AI agents with the data team at NOW GmbH.

Day 1 focused on fundamentals, built bottom-up and directly in code. We covered the OpenAI API and its alternatives like Groq, Anthropic, Bedrock, and Gemini; RAG with text, vector, and hybrid search; agentic RAG patterns; tool calling and agent loops; MCP; and, finally, how to orchestrate agents with PydanticAI. Day 2 was fully hands-on: we built a custom coding agent from scratch, set up a Django-based working environment, implemented tools for code and command execution, and added monitoring with Pydantic Logfire and basic guardrails.

The group was highly engaged, asked sharp questions, and worked through the exercises together. Thanks to the NOW GmbH team for two focused and productive days!

### 2. Course Management Platform Updates

[![Image 6](https://substackcdn.com/image/fetch/$s_!gyMC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd72adc96-3c80-4aa0-a8a7-bb4e59e91cf1_576x547.jpeg)](https://substackcdn.com/image/fetch/$s_!gyMC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd72adc96-3c80-4aa0-a8a7-bb4e59e91cf1_576x547.jpeg)

PRs created by GitHub Copilot

I was also working on a new feature for our course management platform to reduce manual administrative work. Previously, many tasks required clicking through the Django admin interface, which was slow and tedious. I decided to build a custom admin interface to speed up common operations.

For that, I used Copilot. I already shared my process for working on new features with it in one of my [previous newsletter editions](https://alexeyondata.substack.com/p/shipping-features-from-a-tram-stop). I create a GitHub issue, assign it to Copilot, and review the pull request when it’s ready. If the implementation is solid, I merge it. If not, I iterate with feedback. This setup helps me iterate much faster and implement features that I used to postpone because they took too much of my time.

### 3. Wikidata Workshop

I hosted a [workshop on fact-checking with Wikidata,](https://github.com/philippesaade-wmde/WikidataTextifier) led by Philippe Saadé, that demonstrated why relying on an LLM’s internal knowledge is not enough. We built a system that retrieves structured facts from Wikidata via MCP and checks whether a claim is true or false using external data.

In the second part, Philippe demonstrated a practical fact-checking pipeline that uses one model to select relevant facts and another to verify the claim. If you’re interested in grounding LLMs in verifiable data, this is a solid example of how you can do it. So, try to implement a similar system yourself.

[Check out the workshop](https://youtu.be/eT_VTTeaig4)

## Courses

* **[AI Agents Email Crash-Course](https://alexeygrigorev.com/aihero/):** a free AI Agents Email Crash-Course. In 7 days, build a complete AI agent that deeply understands your codebase and can help with real development tasks.
* **[Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp):** a free 9-week course on building production-ready data pipelines: ingestion, orchestration, warehousing, analytics, and more. The new cohort started on January 12, and more than 25,000 people have registered for this course. You can still join and catch up with Module 1 learning materials.
* **[LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp):** a free online course about real-life applications of LLMs. In 10 weeks, you will learn how to build an AI system that answers questions about your knowledge base. A new cohort will start around May-June 2026.

## Interesting Tools

[![Playwriter - For browser automation MCP](https://substackcdn.com/image/fetch/$s_!JvBA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91c68682-134d-4360-b682-6f1aa38bdeef_1200x834.png)](https://substackcdn.com/image/fetch/$s_!JvBA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91c68682-134d-4360-b682-6f1aa38bdeef_1200x834.png)

[Playwriter MCP](https://github.com/remorses/playwriter/tree/main)

* **[Playwriter MCP](https://github.com/remorses/playwriter/tree/main):** lets AI agents control your existing Chrome browser via a lightweight extension, using the full Playwright API with minimal context overhead. It’s useful when you need reliable, real-world browser automation, such as generating screenshots, validating flows, or working with logged-in pages, without building or maintaining custom automation code.
* **[oh-my-claude-sisyphus](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/tree/main):** a Claude Code plugin that adds native multi-agent orchestration, with specialized subagents, hooks, and slash commands to run complex coding tasks in parallel. It’s useful because it automates delegation, search, planning, and “keep going until it’s done” workflows, while also routing tasks to the right Claude model tier for speed and cost.

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
