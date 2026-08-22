---
title: "Shipping Features from my Smartphone with GitHub Copilot"
date: 2025-12-26
url: https://aishippingblog.com/p/shipping-features-from-a-tram-stop
---

Hi everyone,

Before going into the main topic of today’s newsletter, I want to wish you a happy holiday season. Merry Christmas, Hanukkah, Kwanzaa, Yule, and a happy New Year to everyone who celebrates!

I started this newsletter less than a month ago, and we're already almost 1,000 subscribers.

[![Image 1](https://substackcdn.com/image/fetch/$s_!aI0v!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5aec257a-292f-4063-b55c-f78079c36c95_1804x1080.png)](https://substackcdn.com/image/fetch/$s_!aI0v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5aec257a-292f-4063-b55c-f78079c36c95_1804x1080.png)

Thank you for your support and for subscribing! I decided to create a [referral program](https://alexeyondata.substack.com/p/my-newsletter-now-has-a-referral) to reward you for sharing my newsletter and add a small [competitive element](https://alexeyondata.substack.com/leaderboard).

Here are the terms:

* **Refer 3 friends** to get access to the Tutorial Library, a curated collection of study resources focused on learning by doing and solving real engineering problems.
* **Refer 10 friends** to get an rarly access to an Exclusive Mini-Course on building an action-oriented AI agent.
* **Refer 25 friends** and join a private 30-minute Zoom conversation with me to discuss career decisions, learning paths, technical challenges, or project feedback, with no fixed agenda.

[Refer a friend](https://aishippingblog.com/leaderboard?&utm_source=post)

Now, to the main topic!

## One Idea I Want to Share this Week

Last week, I merged a pull request into the [DataTalks.Club course management platform](https://courses.datatalks.club/), the system we use to manage course homework and projects. The PR added a [Spotify Wrapped-style experience](https://courses.datatalks.club/wrapped/2025/) to the platform: 2025 community highlights, the most popular courses, top learners, and individual, shareable Wrapped pages for each participant.

Most of the work happened on my smartphone while I was commuting to pick up my kid.

[![Image 2](https://substackcdn.com/image/fetch/$s_!oEBW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff834b337-acf2-477c-83af-3efdb018d048_1300x792.png)](https://substackcdn.com/image/fetch/$s_!oEBW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff834b337-acf2-477c-83af-3efdb018d048_1300x792.png)

A preview of the Wrapped page on the course platform

### Starting the PR from a Tram Stop

The idea came to me while I was standing at a tram stop: it would be useful to have a single page summarizing what learners achieved across our Zoomcamps throughout the year.

I opened GitHub on my phone, dictated a rough issue description using voice input, and assigned it to Copilot. About 20-30 minutes later, Copilot opened a PR with [working pages, code, and screenshots](https://github.com/DataTalksClub/course-management-platform/pull/115).

Here’s what it looks like:

[![Image 3](https://substackcdn.com/image/fetch/$s_!UMHL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdcf7e15-62f7-46b2-9033-82324edd4442_2516x1502.png)](https://substackcdn.com/image/fetch/$s_!UMHL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdcf7e15-62f7-46b2-9033-82324edd4442_2516x1502.png)

The initial PR generated from a spoken issue

### Iterating Without a Laptop

Once the PR is open, I review the changes, and Copilot updates the code based on my comments. I can handle this entire back-and-forth from my phone.

Here’s how I iterate: I scroll through the code changes on my phone, leave comments, tag Copilot, and ask it to make specific updates. After Copilot pushes a new version, I review it again and repeat the process if needed. This works well for small changes like copy tweaks, layout adjustments, and minor logic updates.

Of course, voice recognition sometimes gets things wrong. In the original issue, I said “top 100,” which became “top 1200,” and that ended up in an early version of the PR. But these kinds of mistakes are easy to fix: I spot them during review, leave a comment, and reassign Copilot.

[![Image 4](https://substackcdn.com/image/fetch/$s_!WOB0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08443bbe-7ce5-4ff2-bf56-40f845c65eb2_1920x1424.png)](https://substackcdn.com/image/fetch/$s_!WOB0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08443bbe-7ce5-4ff2-bf56-40f845c65eb2_1920x1424.png)

One particularly useful detail is that Copilot can run the project itself, generate UI screenshots, and attach them directly to the PR. That means I can check that the page renders correctly and that buttons and links behave as expected.

The screenshots aren’t perfect because Copilot has no internet access, and some styles don’t load. But they’re sufficient to confirm that nothing is obviously broken.

[![Image 5](https://substackcdn.com/image/fetch/$s_!9GsH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc933e8dc-9fe5-45bb-80eb-c6e6d3353454_1758x902.png)](https://substackcdn.com/image/fetch/$s_!9GsH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc933e8dc-9fe5-45bb-80eb-c6e6d3353454_1758x902.png)

Example screenshots attached to the PR

### Phone vs. Laptop Work

After each new comment, Copilot takes about 10-30 minutes to update the PR with a new version. I go through this review-and-comment cycle several times a day right from my smartphone, often in short windows between other tasks. For small and medium-sized changes, it’s remarkably effective.

[![Image 6](https://substackcdn.com/image/fetch/$s_!n41U!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33f3708f-88c4-4e90-a029-d0373c89f453_1080x1101.jpeg)](https://substackcdn.com/image/fetch/$s_!n41U!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33f3708f-88c4-4e90-a029-d0373c89f453_1080x1101.jpeg)

CI/CD workflows

What I don’t do from my phone is final approval for complex changes. For larger features, deeper testing, or anything that could break production, I still sit down at my laptop. CI/CD helps here. Once I merge a PR, the changes are automatically deployed to our dev environment, where I can test things visually.

If everything looks good, deploying to production is a single button in GitHub.

### My Takeaways

For many routine engineering tasks, I don’t need a laptop anymore.

Most of the work becomes writing clear instructions, reviewing output, and correcting mistakes.

If you’re comfortable with that loop, you can close multiple PRs a day from a tram stop.

> If there’s interest, I can record a short video showing this flow end to end: how I structure issues and how I review PRs entirely from my phone. Let me know in the comments if that would be useful.

[Leave a comment](https://aishippingblog.com/p/shipping-features-from-a-tram-stop/comments)

## Project Idea: What You Can Build This Week

One of the [AI Bootcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) graduates shared her [final project](https://github.com/sanjana14srini/capstone_project_ai-bootcamp) and that could be a great place to start. For her capstone, she built a full-stack agentic research assistant that can answer research questions based on arXiv papers by actively searching, indexing, summarizing, and checking whether the retrieved information is sufficient.

[![Image 7](https://substackcdn.com/image/fetch/$s_!rnc2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5194f804-f8a2-4c7d-9ad2-98db721905f9_1754x1100.png)](https://substackcdn.com/image/fetch/$s_!rnc2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5194f804-f8a2-4c7d-9ad2-98db721905f9_1754x1100.png)

The project is public, so you can explore how it’s structured end-to-end

If you want to try something similar this week, don’t aim for the full system right away. Pick a narrow slice: ingest a small set of arXiv papers, build a search index, and add a simple loop that decides whether the answer is “good enough” or if another search is needed. Even that small version already teaches you most of the hard parts of building agents.

Once it works, you can extend it incrementally: experiment with different models, or make the agent more explicit about its reasoning and verification steps.

If you’re looking for more concrete project directions in the same spirit, I’ve described several other agent ideas here:

[5 ideas for AI agents and OpenAI's hidden skills](https://alexeyondata.substack.com/p/5-ideas-for-ai-agents-and-openais)

[AI Agents Email Crash-Course](https://alexeygrigorev.com/aihero/) is a good entry point if you want to start building projects like this.

> If you’re looking for deeper coverage, live support, creating several projects, and access to provate course community, the next iteration of my [AI Bootcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) starts on January 26, 2026. I’m also offering a [limited number of scholarship slots](https://docs.google.com/forms/d/e/1FAIpQLSdH-TfBvQeQzagl2JMyr9HOmqXsP2SjIvMDSj-495ycatm05w/viewform) for this cohort.

## What I’ve Been Working On Recently

In my [latest newsletter](https://alexeyondata.substack.com/p/5-ideas-for-ai-agents-and-openais), I looked into an interesting detail that surfaced around ChatGPT and agent skills.

[![Image 8](https://substackcdn.com/image/fetch/$s_!JZMA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F210edd2c-4133-46a1-b537-9dbba43243a7_1742x1448.png)](https://substackcdn.com/image/fetch/$s_!JZMA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F210edd2c-4133-46a1-b537-9dbba43243a7_1742x1448.png)

My latest newsletter

Anthropic introduced [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) as an open standard, building on the ideas behind MCP and making skills portable across tools and models. OpenAI quietly [adopted a similar concept in Codex](https://developers.openai.com/codex/skills/). [Visual Studio Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills), [Cursor](https://cursor.com/docs/context/skills), [GitHub](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) and other platforms added support for the open Agent Skills spec.

That motivated me to put together a new live workshop on [agent skills](https://alexeyondata.substack.com/i/181879156/homeoai-folder-from-chatgpt-and-openai-skills).

[![Image 9](https://substackcdn.com/image/fetch/$s_!S-O1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3badc3bb-3af5-4503-bc1a-7fa29328475e_1200x628.png)](https://substackcdn.com/image/fetch/$s_!S-O1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3badc3bb-3af5-4503-bc1a-7fa29328475e_1200x628.png)

It focuses on understanding the skills.md model from first principles, implementing a simple skill registry, and using skills inside an agent loop for real coding tasks.

[Register here](https://maven.com/p/1b423c/skills-md-from-scratch-build-a-skill-driven-coding-agent)

## Courses

[![Scholarship application page for an AI Bootcamp titled "From RAG to Agents," detailing course goals, eligibility, fee USD 1,799, and links to apply.](https://substackcdn.com/image/fetch/$s_!7GQk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8615e545-17e0-485b-9b22-9ede9799a702_1200x846.png)](https://substackcdn.com/image/fetch/$s_!7GQk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8615e545-17e0-485b-9b22-9ede9799a702_1200x846.png)

AI Bootcamp scholarship application form

* **[AI Agents Email Crash-Course (Cohort Edition)](https://alexeygrigorev.com/aihero/):** I’m running a free cohort-based version of the AI Agents Email Crash-Course this December and January. To complete the cohort, you’ll finish the project and review three other submissions; in return, you’ll receive a certificate of completion signed by me.
* **[AI Bootcamp Scholarships (New Cohort)](https://forms.gle/u1SYszg4R6kzdjrS8):** I’m launching a new iteration of the AI Bootcamp, and this time I’m also offering several scholarship spots. I know that not everyone has the budget for a paid program, but many people are highly motivated to learn, practice, and build real systems.
* **[Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp):** New cohort starts on January 12, 2026. A free 9-week course on building production-ready data pipelines: ingestion, orchestration, warehousing, analytics, and more.
* **[dlt Fundamentals](https://dlthub.learnworlds.com/course/dlt-fundamentals?utm_source=alexey_linkedin):** My friends from dltHub created a course on building robust ELT pipelines. Register now to join our new holiday lesson on December 22, where you will integrate LLMs into your workflow and compete for 50 swag packs.

## Interesting Models and Tools

* **[MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1):** an open-weight reasoning model that combines a large MoE backbone with hybrid attention, supporting up to 1M-token context while using significantly less test-time compute than comparable models. It’s shows strong results against other open models, especially in software engineering and extended-input settings.
* **[collaborating-with-codex](https://github.com/GuDaStudio/collaborating-with-codex):** an Agent Skill that lets Claude delegate coding tasks to the OpenAI Codex CLI, enabling multi-model collaboration within a single workflow. Claude coordinates the task and refines results, while Codex handles implementation, debugging, and code analysis in a sandboxed execution environment.

[Share](https://aishippingblog.com/p/shipping-features-from-a-tram-stop?utm_source=substack&utm_medium=email&utm_content=share&action=share)

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
