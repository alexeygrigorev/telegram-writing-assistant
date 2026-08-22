---
title: "How I Built a Telegram Assistant That Turns Brain Dumps into Structured Markdown"
date: 2026-01-30
url: https://aishippingblog.com/p/telegram-assistant
---

## One Thing I Want to Share This Week

I work on many projects, and most of the work happens before anything becomes public. This includes early thinking, small experiments, and intermediate workflows that usually disappear once a final result is ready.

That means you can only see the final results of my work: finished projects, talks, or materials. Everything that led to them remains invisible.

As I started this Substack, I realized I want to share my background work too because it’s an important part of what I do. It helps you understand how I approach my projects and, hopefully, gives you new ideas.

[![Image 1](https://substackcdn.com/image/fetch/$s_!uP4T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F867054d5-9074-4e9d-8dd9-18b22a7aefb3_1946x964.png)](https://substackcdn.com/image/fetch/$s_!uP4T!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F867054d5-9074-4e9d-8dd9-18b22a7aefb3_1946x964.png)

Repository with my [Telegram-based writing assistant](https://github.com/alexeygrigorev/telegram-writing-assistant/tree/master)

To help myself capture that background work, I built a [Telegram-based writing assistant](https://github.com/alexeygrigorev/telegram-writing-assistant/tree/master) using Claude Code agents. It can process my raw voice notes, files, and text messages into structured articles and store them in a GitHub repository.

I want to explain how I built the system, how it works, and how you can adapt the same approach for your own workflow.

### Origin Story

Initially, when I started recording ideas using Telegram as a brain dump, there was no assistant to help me. I just created a new chat for my team and me, and collected my ideas there so we could use them to produce content. That was a great starting point and a key factor in creating the [first editions of this newsletter](https://alexeyondata.substack.com/).

[![Image 2](https://substackcdn.com/image/fetch/$s_!w4-0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6e961ce-5b4f-4cef-b962-9c1d2d240222_1600x862.png)](https://substackcdn.com/image/fetch/$s_!w4-0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6e961ce-5b4f-4cef-b962-9c1d2d240222_1600x862.png)

Initial Telegram chat where I dumped my ideas

But it had one limitation: manual processing. Over time, my Telegram became overloaded with voice notes that quickly piled up into a long, unstructured list of raw materials. Some pieces belonged to the same topic. Others were partial thoughts, corrections, or follow-ups.

[![Image 3](https://substackcdn.com/image/fetch/$s_!66ST!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea606288-28d3-42b9-ac52-406794bfd07a_1510x886.png)](https://substackcdn.com/image/fetch/$s_!66ST!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea606288-28d3-42b9-ac52-406794bfd07a_1510x886.png)

We had a lot of pending voice messages, files, and screenshots to process before publishing a new edition of the newsletter. At some point, it was hard to categorize them and required back-and-forth switching between voice messages, links, and files. That created additional friction for content creation.

Turning this stream into something structured required rereading, sorting, and stitching everything together by hand. This was slow and mentally expensive.

This is how I started thinking about how to handle an incoming stream of background work so it can be organized and transformed into pieces I could share publicly.

### How I Implemented the Telegram Assistant

I had an initial vision for how the assistant should work and decided to iterate on it using ChatGPT.

[![Image 4](https://substackcdn.com/image/fetch/$s_!QfaN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd03a9d4c-bebd-43ab-860f-8849c75bfcf3_1280x718.jpeg)](https://substackcdn.com/image/fetch/$s_!QfaN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd03a9d4c-bebd-43ab-860f-8849c75bfcf3_1280x718.jpeg)

Repo structure suggested by ChatGPT

I recorded voice messages, discussed the workflow, and refined the process description until it was clear enough to write down. At the end, I asked ChatGPT to save our conversation as a [summary.md](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/SUMMARY.md) file, which became the system specification. It was initially in Russian, but I translated it into English for you.

I usually use ChatGPT to refine my vision before starting any new project. It helps me to better understand what I want to build and how I want to do it.

[![Image 5](https://substackcdn.com/image/fetch/$s_!N96O!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe14c8eb8-915b-4ce7-8190-3a5e4398463d_862x672.jpeg)](https://substackcdn.com/image/fetch/$s_!N96O!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe14c8eb8-915b-4ce7-8190-3a5e4398463d_862x672.jpeg)

Workflow suggested by ChatGPT

I didn’t want to implement the system described in `summary.md` myself. Instead, I asked the Claude Code agent to follow that description and build it. This produced the first working version.

Claude created a Telegram bot that lives in my chat and connected it to a GitHub repository that stores the specification and all subsequent updates from the chat.

I then tested the system by using it as intended: sending messages and recording improvement ideas as voice notes, without leaving the same workflow I was trying to optimize. Claude processed those messages and updated the system.

Here is what the final version looks like.

### How the Final Version Works

Telegram Assistant follows this workflow:

#### 1. Capturing

[![Image 6](https://substackcdn.com/image/fetch/$s_!wA81!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fe5e0af-9182-4b65-b1b9-995f096d59d7_1180x416.png)](https://substackcdn.com/image/fetch/$s_!wA81!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fe5e0af-9182-4b65-b1b9-995f096d59d7_1180x416.png)

Telegram Chat

All interaction starts in a Telegram chat. I send text messages, voice notes, images, or files to the bot. Everything is saved locally on my laptop as raw input.

#### 2. Processing

[![Image 7](https://substackcdn.com/image/fetch/$s_!77fk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da3c3de-a051-4893-bc75-85d9efa48d2f_1162x866.png)](https://substackcdn.com/image/fetch/$s_!77fk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da3c3de-a051-4893-bc75-85d9efa48d2f_1162x866.png)

How I run /process command and the assistant processes a new batch of input

When I run the `/process` command, the assistant reads all accumulated materials as a batch. For each item, it decides whether the content belongs to an existing article or should start a new one. Articles are updated incrementally rather than regenerated from scratch.

#### 3. Versioning and Feedback

[![Image 8](https://substackcdn.com/image/fetch/$s_!Nl09!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b6da959-a6b3-4f32-80d0-890b73141cb2_2158x1044.png)](https://substackcdn.com/image/fetch/$s_!Nl09!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b6da959-a6b3-4f32-80d0-890b73141cb2_2158x1044.png)

GitHub commit created by the assistant with a clear description of what was changed

Once processing is complete, all changes are committed to a GitHub repository. The commit is created by the assistant. It shows what it changed and why. The agent also sends a link to the commit back to the Telegram chat.

#### 4. Updating the Configuration

[![Image 9](https://substackcdn.com/image/fetch/$s_!_2dJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5338b457-18c0-4769-a64a-ae8108bdd4ad_1996x992.png)](https://substackcdn.com/image/fetch/$s_!_2dJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5338b457-18c0-4769-a64a-ae8108bdd4ad_1996x992.png)

Here’s how I specify what the assistant needs to extract from the text to collect improvement ideas and issues it has to work on

If I need the agent to update its configuration, including the system prompt and the code it’s based on, I can record improvement ideas as voice notes in the same chat. I can also add images if necessary. I then run the `/check-tasks` command. The assistant processes all the messages in the chat and looks for bug reports, feature suggestions, etc. After that, it updates the prompt or code accordingly, and commits updates to the repository.

### Technical Capabilities

The final version of the assistant combines a small set of focused technical capabilities:

#### 1. Voice Transcription

[![Image 10](https://substackcdn.com/image/fetch/$s_!Efmj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb09105c2-0ae0-43ee-bf73-977e566e8104_1492x750.png)](https://substackcdn.com/image/fetch/$s_!Efmj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb09105c2-0ae0-43ee-bf73-977e566e8104_1492x750.png)

How the assistant transcribes voice messages

Voice messages are transcribed automatically using Whisper via Groq. After transcription, the original audio files are removed. Only the extracted text is kept and used for further processing. This ensures that all downstream steps operate on text, regardless of how the input was originally captured.

#### 2. Image Processing

Images sent to the bot are processed and described using Groq Vision. Each image is then moved into a structured directory under `assets/images/{article_name}/`. This makes images first-class inputs that can be referenced in articles rather than remaining as detached chat artifacts.

#### 3. Multilingual Input Handling

[![Image 11](https://substackcdn.com/image/fetch/$s_!5fcw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea181618-9d31-4117-ba16-c3d9894fa137_1320x570.png)](https://substackcdn.com/image/fetch/$s_!5fcw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea181618-9d31-4117-ba16-c3d9894fa137_1320x570.png)

The assistant can transcribe my messages in Russian and then translate them into English

In practice, voice notes are often recorded in Russian, while articles are written in English. During processing, Claude translates all content into English, which is treated as the target language for articles. This removes language constraints from the capture phase.

#### 4. Link Fetching and Summarization

Links dropped into the chat are fetched during processing. Relevant content is summarized and incorporated into the appropriate article, rather than being stored as raw URLs. This keeps external references integrated with the surrounding context.

#### 5. Git-Based Orchestration

[![Image 12](https://substackcdn.com/image/fetch/$s_!vYbV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dfbb663-59ee-4f5a-9338-1497b640d099_1280x402.jpeg)](https://substackcdn.com/image/fetch/$s_!vYbV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dfbb663-59ee-4f5a-9338-1497b640d099_1280x402.jpeg)

How I updated config to do git pull before pushing a new commit to the repo

All updates are committed to a GitHub repository. Each processing run results in a concrete diff that shows exactly what changed. The agent can also follow natural-language instructions such as running `git pull` before processing to ensure it is working with the latest state.

### Demo

Here’s a demo of the entire process

The source code is here: https://github.com/alexeygrigorev/telegram-writing-assistant

Let me know in the comments if you liked it and want to try creating something similar!

## My Experiment

End-to-end testing is one of the most painful parts of web development. Verifying full user flows is slow, and traditional tools like Selenium or Playwright produce tests that are hard to read and fragile, especially when AI coding assistants increase the risk of regressions.

I recently experimented with TestMu AI and its [KaneAI automation test agent](https://www.testmuai.com/kane-ai/?utm_source=linkedin&utm_medium=alexey&via=vibetest). Instead of writing browser scripts, I described test scenarios in plain English and let the agent execute them. I tried this on parts of the DataTalks.Club course platform. The tool still needs fine-tuning, but it already removes much of the friction of maintaining Selenium-style tests.

The main shift is how tests are defined. Writing intent in natural language makes them easier to reason about and verify. You still need to confirm that tests fail when something breaks, but tools like TestMu AI make end-to-end testing easier to work with and faster to iterate on.

## What I’ve Been Working On Recently

### 1. AI Engineering Buildcamp

[![Image](https://substackcdn.com/image/fetch/$s_!3nfa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69df46fc-a937-4b90-ad5a-cfbb59bdc39b_1107x814.png)](https://substackcdn.com/image/fetch/$s_!3nfa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69df46fc-a937-4b90-ad5a-cfbb59bdc39b_1107x814.png)

We began the second cohort of the [AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) this Monday. It was great to see so many people live, meet the group, and set the tone from the first session. I walked through the full course structure, explained how everything connects, and outlined what we’ll be building over the coming weeks.

If you’re still considering joining, I’ve extended the payment deadline to next week. Even if you join a bit late, you can still catch up. You can enroll here: <https://maven.com/alexey-grigorev/from-rag-to-agents>

### 2. Community Survey on Tools for ML, Data Engineering, AI Engineering and Chatbots

[![Image 14](https://substackcdn.com/image/fetch/$s_!Fj1-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f06575e-d41c-4961-a106-d7881defb386_1198x866.png)](https://substackcdn.com/image/fetch/$s_!Fj1-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f06575e-d41c-4961-a106-d7881defb386_1198x866.png)

The certificate showing that I used One Tree Planted for each survey response

At DataTalksClub, we also published the [results of our latest survey](https://datatalks.club/surveys/) on how professionals use AI, data engineering, MLOps, and developer-focused AI tools in practice. We had slightly fewer participants this year, but the results are still very interesting. They show what teams are experimenting with and where they plan to invest next.

We’ll use these insights to shape future courses and events in the community. For each survey submission, we also planted a tree as a small way to give something back. Thanks to Valeriia for preparing the survey and building the visualizations.

## Courses

[![Image 15](https://substackcdn.com/image/fetch/$s_!wqSB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6622b7ed-769b-4aef-ac4a-661d5a984b73_1080x1023.jpeg)](https://substackcdn.com/image/fetch/$s_!wqSB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6622b7ed-769b-4aef-ac4a-661d5a984b73_1080x1023.jpeg)

A great review of my [AI Agents Email Crash-Course](https://alexeygrigorev.com/aihero/)

* **[AI Agents Email Crash-Course](https://alexeygrigorev.com/aihero/):** a free AI Agents Email Crash-Course. In 7 days, build a complete AI agent that deeply understands your codebase and can help with real development tasks.
* **[Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp):** a free 9-week course on building production-ready data pipelines: ingestion, orchestration, warehousing, analytics, and more. The new cohort started on January 12, and more than 25,000 people have registered for this course. You can still join and catch up with Module 1 learning materials.
* **[LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp):** a free online course about real-life applications of LLMs. In 10 weeks, you will learn how to build an AI system that answers questions about your knowledge base. A new cohort will start around May-June 2026.

## Interesting Resources

* **[Claude Code and Large-Context Reasoning](https://github.com/timothywarner-org/claude-code)**: materials from a hands-on O’Reilly Live Learning course by Tim Warner that teaches how to build production-ready AI-assisted development workflows with Claude Code. It covers large-context reasoning, MCP-based persistent memory, agents, and custom skills, with practical examples for code review, automation, and CI/CD.
* **[awesome-slash](https://github.com/avifenesh/awesome-slash)**: a curated GitHub list of tools, patterns, and projects built around slash-command interfaces. It’s a practical reference for anyone designing command-driven workflows, bots, or developer tools that rely on concise, action-oriented commands instead of complex UIs.

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
