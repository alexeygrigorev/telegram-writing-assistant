---
title: "I Turned My Telegram Bot into a Multi-Agent Writing System"
date: 2026-03-20
url: https://aishippingblog.com/p/i-turned-my-telegram-bot-into-a-multi
---

In one of my previous newsletters, I wrote about my [Telegram Writing Assistant](https://alexeyondata.substack.com/p/telegram-assistant), a bot that takes raw voice notes, text messages, and links sent to a private Telegram channel and turns them into structured Markdown drafts.​

Over time, the system expanded. It no longer transcribed voice notes. It fetched external links, summarized long articles, organized research topics, and prepared newsletter resources. All of this happened inside a single context window.​

[![Image 1](https://substackcdn.com/image/fetch/$s_!Ir-5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c81e30d-ab2b-40b2-b575-75fa886417fb_1162x866.jpeg)](https://substackcdn.com/image/fetch/$s_!Ir-5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c81e30d-ab2b-40b2-b575-75fa886417fb_1162x866.jpeg)

When multiple URLs or messages were processed together, the context filled up quickly. That led to compaction, slower responses, and occasional loss of detail. The limitation was architectural. One agent was responsible for everything.

To address this, I refactored the workflow using Claude Code subagents. Instead of a single overloaded process, the system is now split into specialized agents with defined roles. The main agent coordinates and processes voice messages. Separate subagents handle research, link curation, and verification.

In this newsletter, I describe the subagents and new capabilities that I introduced to my Telegram Assistant.

[Share](https://aishippingblog.com/p/i-turned-my-telegram-bot-into-a-multi?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## Creating Subagents and Their Benefits

Claude Code allows you to create subagents via the /agents command. You define their responsibility and constraints, and they become available immediately. Restarting the session sometimes helps ensure they are properly initialized.

[![Image 2](https://substackcdn.com/image/fetch/$s_!bqam!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc33c2477-1a92-4c42-b47b-19d2c4fe7f82_1694x963.jpeg)](https://substackcdn.com/image/fetch/$s_!bqam!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc33c2477-1a92-4c42-b47b-19d2c4fe7f82_1694x963.jpeg)

Subagents are useful when a single agent handles too many heterogeneous tasks.

They allow you to:

* Keep the main agent focused on orchestration instead of heavy processing
* Prevent context window overflow caused by large external documents
* Isolate responsibilities so individual agents can be adjusted without affecting the rest of the system

## My Subagents

For research-related workflows, I introduced two dedicated subagents: [article-summarizer](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/.claude/agents/article-summarizer.md) and [resource-describer](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/.claude/agents/resource-describer.md). I also added a [verify-content](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/.claude/agents/verify-content.md) subagent that checks whether the main agent has unintentionally summarized parts of my voice notes or omitted important details or context.

### 1. Article-summarizer Subgent

[![image.png](https://substackcdn.com/image/fetch/$s_!aro1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec3d1adb-677e-475b-bc76-2d4049f81249_1600x754.png)](https://substackcdn.com/image/fetch/$s_!aro1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec3d1adb-677e-475b-bc76-2d4049f81249_1600x754.png)

The [article-summarizer](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/.claude/agents/article-summarizer.md) takes a single external URL and turns it into easy-to-understand research material, adding organized insights from that source to an existing article.

When I submit a URL, a documentation page, or a long technical article, the subagent uses Jina Reader to extract the content, reviews it, and adds a structured summary to the relevant research article. The summary includes a clear overview, important ideas, technical details, insights, and practical takeaways.

### 2. Resource-describer Subgent

[![image.png](https://substackcdn.com/image/fetch/$s_!2Eys!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3e210bd-ba64-42a3-a5ca-8fd1002a34ae_1600x799.png)](https://substackcdn.com/image/fetch/$s_!2Eys!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3e210bd-ba64-42a3-a5ca-8fd1002a34ae_1600x799.png)

​The [resource-describer](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/.claude/agents/resource-describer.md) generates brief descriptions for valuable links featured in the newsletter’s “Tools” and “Resources” sections.

​When I share a URL worth including, it retrieves the content using Jina Reader, similar to how Research Agent does. Then it writes a short 2-4 sentence description of the resource and adds it to interesting-resources.md, an article that lists all resources.

### 3. Verify-content Subagent

[![image.png](https://substackcdn.com/image/fetch/$s_!sCs5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0869536f-d784-4fe6-80a2-a41b08cfdf90_1600x682.png)](https://substackcdn.com/image/fetch/$s_!sCs5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0869536f-d784-4fe6-80a2-a41b08cfdf90_1600x682.png)

The [verify-content](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/.claude/agents/verify-content.md) subagent checks the content created by the main agent. I set it up to make sure the main agent doesn’t summarize information from voice messages, because that can lead to missing important details. Even though I’ve instructed the main agent not to summarize voice notes, it still sometimes does so when analyzing them.

The verification subagent starts working after the main agent has finished processing. It reviews what was generated, compares it to the original voice messages, and fills in any gaps if something was left out.

This two-step process makes sure all content from the voice messages is kept intact.

### 4. Main Agent

The Main Agent retains a narrow responsibility and doesn’t handle tasks that are intended for research subagents.

It processes voice messages, orchestrates the overall workflow, and delegates external content processing to subagents.

By keeping the main agent focused on transcription, formatting, and coordination, its context remains clean. It does not need to ingest full research papers or multiple URLs. It works with the structured outputs returned by subagents.

This separation significantly reduces context window pressure and keeps the system predictable.

## New Features

Alongside the architectural changes, I added practical capabilities to expand the types of input the assistant can handle.

### 1. Audio File Processing

[![image.png](https://substackcdn.com/image/fetch/$s_!9aXy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f66b17e-a312-4ed3-b880-2034f6b86559_1600x427.png)](https://substackcdn.com/image/fetch/$s_!9aXy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f66b17e-a312-4ed3-b880-2034f6b86559_1600x427.png)

Telegram voice notes stop recording when the app goes to the background. That makes it inconvenient to capture longer thoughts. To work around this, I added support for sending regular audio files instead of native voice notes.​

Now, when the bot receives an audio file such as MP4 or M4A, it treats it as speech input. The file is transcribed and processed through the same pipeline as a standard voice message.​

This required adding explicit handling for custom audio formats. The first implementation attempt failed, and earlier experiments did not complete the full pipeline. After debugging the ingestion and transcription steps, the process now works end-to-end. Audio files are correctly detected, transcribed, and integrated into the drafting workflow.

### 2. YouTube Transcript Processing

[![image.png](https://substackcdn.com/image/fetch/$s_!Z4C_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91d23f13-ebdf-443c-b7bb-1b7e241b73e9_1600x677.png)](https://substackcdn.com/image/fetch/$s_!Z4C_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91d23f13-ebdf-443c-b7bb-1b7e241b73e9_1600x677.png)

The assistant can now process YouTube links directly.

When a message contains a YouTube URL, the system retrieves the video transcript and treats it as source material.

The transcript is processed in the same way as voice message transcripts. It can be incorporated into research articles or drafts depending on context.​

This allows long-form video content to be converted into structured written material without manual transcript extraction.

[Share](https://aishippingblog.com/p/i-turned-my-telegram-bot-into-a-multi?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## Claude Code Skills

In addition to subagents, I also started using [Claude Code skills](https://code.claude.com/docs/en/skills) to automate parts of my repeatable workflows.

[![Image 8](https://substackcdn.com/image/fetch/$s_!69OY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44bf7967-3a74-4de5-8052-458344aee0d4_1506x798.png)](https://substackcdn.com/image/fetch/$s_!69OY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44bf7967-3a74-4de5-8052-458344aee0d4_1506x798.png)

A skill becomes useful when you notice you are correcting the same kind of behavior repeatedly. Instead of re-explaining the workflow every time, you encode it once. From that point on, the agent has a clearer path to follow.

Skills are especially useful for tasks where the overall goal stays the same, but the content changes. Rather than prompting from scratch each time, you give the agent a defined process for the task.

### How to Create and Iterate on Skills

The simplest way to create one is to let the agent perform the task first, observe where it goes wrong, and correct it in the session. After going back and forth until the result is right, you can ask the agent to summarize the discussion and corrections and turn them into a skill.

Improving an existing skill follows the same principle. With the Telegram writing assistant, for example, the /process command keeps improving through repeated use. When it makes a mistake, I correct it in the session. After resolving the issue, I ask the agent to analyze its actions and my corrections and determine what should change in the process to avoid that mistake in the future. The agent updates the command file.

## My Claude Code Skills

In addition to new agent features, I also added two Claude skills: [create-slides](https://github.com/alexeygrigorev/telegram-writing-assistant/tree/master/.claude/skills/create-slides) and [slides-to-pdf](https://github.com/alexeygrigorev/telegram-writing-assistant/tree/master/.claude/skills/slides-to-pdf), which I use to prepare slides for workshops and talks.

![Image 9](https://substackcdn.com/image/fetch/$s_!BTW_!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe59fd4b7-f5d8-413a-832e-4eb07c9925c0_1886x778.png)![Image 10](https://substackcdn.com/image/fetch/$s_!yHMV!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93df1806-915e-42d1-ba55-da57f3b749cc_1882x790.png)

My Claude Code skills

The workflow usually looks like this:

* I dictate ideas into the Telegram assistant as voice messages
* I open an interactive Claude Code session and tell it what material to work with
* I use the [create-slides](https://github.com/alexeygrigorev/telegram-writing-assistant/tree/master/.claude/skills/create-slides) skill to generate slides
* I review the result, give feedback, and iterate until the slides are right

This way, tasks like organizing content, deciding on layout, and figuring out where to place elements on the slide are no longer fully manual. Claude handles much of that process. I describe what I want to see, review the output, and refine it.

[![image.png](https://substackcdn.com/image/fetch/$s_!ykYW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7738579-9621-40c2-bdd8-1df462f56469_1280x896.png)](https://substackcdn.com/image/fetch/$s_!ykYW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7738579-9621-40c2-bdd8-1df462f56469_1280x896.png)

I first developed this approach while preparing slides for my Zalando workshop. It proved usable, and since then, I have kept using it for other workshops. The first time took longer, but over time the process became faster. Each workshop created more examples to reference, making it easier to say things like “do it like last time” and get closer to the right result immediately.

So it’s an iterative system that improves as the number of prior examples grows. The more concrete references the agent has, the less time I spend shaping the output from scratch.

## Impact

Overall, these changes made the workflow more manageable and reliable.

Subagents made it possible to split research, drafting, and verification into separate steps. Skills made repeated tasks more consistent and reduced the need to explain the same process again in each session.

The Telegram Assistant became easier to work with, easier to extend, and better suited for repeated use in real workflows.

## What I’ve Been Working On Recently

### 1) AI Hero Course Migration

[![Image 12](https://substackcdn.com/image/fetch/$s_!FVWL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd553f54-e4ef-424e-a6e9-ff3dc6e11234_1894x1120.png)](https://substackcdn.com/image/fetch/$s_!FVWL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd553f54-e4ef-424e-a6e9-ff3dc6e11234_1894x1120.png)

Migrated the AI Hero course to the new AI Shipping Labs platform using my “agent teams approach” that I’ll describe and share with you in more detail in the upcoming newsletter.

I shared a link to the existing course content, told the agents “migrate this,” and they handled everything. The agents created [a detailed GitHub issue](https://github.com/AI-Shipping-Labs/website/issues/128) on the AI Shipping Labs GitHub repo with full specifications and completed the migration autonomously.

The course is now live at <https://aishippinglabs.com/courses/aihero>.

### 2) Python for AI Engineering course

I’m also creating a short “Python for AI Engineering” course for AI Shipping Lab members. It will cover the basics you need to work with our AI Engineering materials, even if you have no prior Python knowledge. Like the DataTalks.Club Zoomcamps, the course will use a project-based approach.

### 3) Windows 11 Dev Setup: Git, Python, NodeJS, Docker, VS Code

I recently got a new Windows computer and recorded the full setup process so you can follow along. I set up a development environment with a terminal, bash, Python, Node.js, Docker, VS Code, and other tools I use often.

I also plan to write an article about this and share it soon.

## Tools

[![Image 13](https://substackcdn.com/image/fetch/$s_!_yJk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a693e71-8499-4b6d-acd2-1d42897a55c7_1069x248.png)](https://substackcdn.com/image/fetch/$s_!_yJk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a693e71-8499-4b6d-acd2-1d42897a55c7_1069x248.png)

[Scrapling](https://github.com/D4Vinci/Scrapling): an adaptive Python web scraping framework that covers everything from one-off requests to full concurrent crawls.

* **[Scrapling](https://github.com/D4Vinci/Scrapling)**: an adaptive Python web scraping framework that covers everything from one-off requests to full concurrent crawls. Its standout feature is an adaptive parser that learns from website changes and automatically relocates CSS/XPath selectors when pages redesign, so scraping scripts don’t silently break. It also includes stealth fetchers that bypass Cloudflare Turnstile out of the box, a Scrapy-like spider framework with pause/resume and proxy rotation, and a built-in MCP server for AI-assisted data extraction. Could be useful for collecting data from Twitter, Reddit, Blind, and other sites where Playwright-based scraping struggles
* **[Pinchtab](https://github.com/pinchtab/pinchtab)**: a standalone browser automation server that exposes Chrome control via a plain HTTP API, making it usable from any AI agent, language, or even curl. Unlike framework-locked tools such as Playwright MCP or Browser Use, Pinchtab ships as a single 12MB Go binary with zero config, built-in stealth mode for bypassing bot detection, persistent login sessions across restarts, and accessibility-tree-based page snapshots that use 5-13x fewer tokens than screenshots. It also includes a dashboard for managing multiple browser profiles and a headed mode where a human can handle CAPTCHAs and 2FA while the agent continues automation through the same session
* **[Humanizer](https://github.com/blader/humanizer)**: a Claude Code skill that removes signs of AI-generated writing from text. Based on Wikipedia’s “Signs of AI writing” guide, it detects 24 patterns across 5 categories: content patterns (significance inflation, promotional language), language patterns (AI vocabulary, synonym cycling), style patterns (em dash overuse, boldface), communication patterns (chatbot artifacts, sycophantic tone), and filler/hedging.

## Resource

[![Image 14](https://substackcdn.com/image/fetch/$s_!3pG2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e40b032-2fa8-4e06-880b-09e16bcd6431_1024x768.png)](https://substackcdn.com/image/fetch/$s_!3pG2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e40b032-2fa8-4e06-880b-09e16bcd6431_1024x768.png)

**[Production Agentic RAG Course](https://github.com/jamwithai/production-agentic-rag-course)**: a free 7-week hands-on course that teaches you to build a production-grade RAG system by constructing an arXiv research paper assistant from scratch. It takes a “foundations first” approach - starting with infrastructure setup (Docker, FastAPI, PostgreSQL, OpenSearch), then building BM25 keyword search before adding semantic embeddings for hybrid retrieval, and progressively layering on a local LLM, Langfuse monitoring, Redis caching, and finally agentic RAG with LangGraph and a Telegram bot. Each week has a companion blog post, Jupyter notebook, and tagged code release

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
