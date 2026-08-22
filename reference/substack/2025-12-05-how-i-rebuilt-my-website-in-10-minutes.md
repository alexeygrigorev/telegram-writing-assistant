---
title: "How I Rebuilt My Website in 10 Minutes With AI"
date: 2025-12-05
url: https://aishippingblog.com/p/how-i-rebuilt-my-website-in-10-minutes
---

I haven’t properly updated [my personal website](https://alexeygrigorev.com/) since 2012.

Yesterday I tried a small experiment: I asked Lovable to generate a GitHub-style template for my homepage.

Surprisingly, the *first iteration* was already good enough.

I then exported the generated project to GitHub and asked GitHub Copilot to rewrite it in Jekyll, since Lovable is built with React, but GitHub Pages needs Jekyll.

After a few minor fixes, the site was ready, all in under ten minutes.

[![Image 1](https://substackcdn.com/image/fetch/$s_!EHfJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcff4f356-e692-4a72-9297-fa97e0f7935f_2712x1622.png)](https://substackcdn.com/image/fetch/$s_!EHfJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcff4f356-e692-4a72-9297-fa97e0f7935f_2712x1622.png)

My updated website: https://alexeygrigorev.com/

## How I Did It With AI

My initial prompt to Lovable was simple:

> I want to create my personal page that looks like a github profile: **<https://github.com/alexeygrigorev>**
>
> userpic **<https://avatars.githubusercontent.com/u/875246?v=4>** name: Alexey Grigorev (alexeygrigorev)
>
> instead of “Overview Repositories Projects Packages Stars” we can have “Overview Courses Projects CV”

Then I asked it to add my [README](https://github.com/alexeygrigorev/alexeygrigorev/blob/master/README.md) and support dark/light mode:

> Add dark/light more for overview use the alexeygrigorev/README.md
>
> <CONTENT OF README.md>

Lovable produced [this version](https://neo-github-me.lovable.app/):

[![Image 2](https://substackcdn.com/image/fetch/$s_!svGP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F678b5aaa-b79e-4428-bca3-6f54ca14a890_2880x1626.png)](https://substackcdn.com/image/fetch/$s_!svGP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F678b5aaa-b79e-4428-bca3-6f54ca14a890_2880x1626.png)

Lovable version

From there, the workflow was straightforward:

I exported the project to GitHub, opened an issue, and assigned it to Copilot, saying:

> Redo it with Jekyll
>
> This page can be served statically. I want to use Jekyll for that.

After cloning the repo to my local computer, I asked Copilot in VS Code to make a few other edits:

* Make each tab a separate page, instead of showing tabs dynamically via JavaScript

* Move the data from HTML to YAML files in `_data/` to make updates easier

I refreshed my CV, let Copilot polish the layout, replaced the old site files, and added the courses and resources sections.

### Tools I Used

* Lovable handles layout and UI: You can use 5 free daily credits
* Copilot handles framework translation: It’s included in my GitHub Pro plan
* GitHub Pages handles hosting: It’s free to use

It’s amazing how easy it has become to build a clean, functional homepage using AI tools that take natural-language instructions.

[Share](https://aishippingblog.com/p/how-i-rebuilt-my-website-in-10-minutes?utm_source=substack&utm_medium=email&utm_content=share&action=share)

### Project Idea: **What You Can Build This Week**

If you’re inspired by my story, try rebuilding a small part of your personal site or a simple app using an AI tool like Lovable, Cursor, or Claude Code.

Give it one prompt, export the result, and see how far you can get in 15–20 minutes. The goal is to experiment with how quickly modern AI tools can turn your idea into working code.

If you want to go deeper into workflows like this, we cover them in the **[AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)**.

Here’s what our course participants built during the first module (the task was to create a simple Django to-do app with AI):

![Image 3](https://substackcdn.com/image/fetch/$s_!IkOl!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34d2f9e8-77c3-4ad4-8387-9a6f154068e1_2716x1466.png)![Image 4](https://substackcdn.com/image/fetch/$s_!RmAD!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ef84e6a-81d1-4e4d-b983-df31d96dc229_1329x551.png)![Image 5](https://substackcdn.com/image/fetch/$s_!7BNF!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff448078-213b-4978-a5b2-299252a66e36_1898x784.png)

![Image 6](https://substackcdn.com/image/fetch/$s_!_3CA!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0a68ed2-41f3-4a94-99d9-9d675f66f9bf_928x518.png)![Image 7](https://substackcdn.com/image/fetch/$s_!M5oy!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc49b093-8ab1-4adb-9587-d5a5254c2840_1358x733.png)![Image 8](https://substackcdn.com/image/fetch/$s_!zma7!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc64d1a5d-246a-40f9-9e27-ad01eb7855f6_1482x793.png)

![Image 9](https://substackcdn.com/image/fetch/$s_!p3an!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffccad04c-c4d0-41a6-b8fd-1ecc579057b1_1366x768.png)![Image 10](https://substackcdn.com/image/fetch/$s_!uUgt!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81c3b30c-3feb-4f41-bf76-eb6d54cc1c4e_1876x1168.png)![Image 11](https://substackcdn.com/image/fetch/$s_!lXiy!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d9db03b-36bc-42b4-a582-e8f76115c1cd_1080x573.jpeg)

Simple to-do apps built with AI by AI Dev Tools Zoomcamp course participants

We’ve just started **Module 2: Building an End-to-End Application**, moving from small tasks to generating a complete, deployable app.

## What I’ve Tried Recently

![Image 12](https://substackcdn.com/image/fetch/$s_!jqDT!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa940a191-7b9f-4580-8191-0b1a772c666f_896x552.jpeg)![Image 13](https://substackcdn.com/image/fetch/$s_!_in9!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa20566f4-fbfc-4ef0-8d50-c1632c192fff_1280x796.jpeg)

* Tried Gemini Nano Banana Pro to tweak one of my photos. Try to guess which one is the original. I’m honestly not sure anymore.
* I also played with Google Antigravity and asked it to build an end-to-end Snake game: frontend, backend, tests, deployment, CI/CD. It actually did it. And it’s 100% free.

## Interesting Tools

* **[goose agent](https://www.linkedin.com/posts/eddiejaoude_i-used-an-open-source-ai-agent-mcp-to-automate-activity-7397682906615234560-OVRj?utm_source=share&utm_medium=member_desktop&rcm=ACoAADJu9vMBW6iyIYswCQnN6t8UJLkXH2tQPi4)**: an open-source coding assistant that runs locally, either from the desktop app or the CLI.
* **[Blueprint MCP](https://github.com/ArcadeAI/blueprint-mcp)**: generates diagrams to help understand codebases and system architecture. Powered by Nano Banana Pro.
* **[GitHub Wrapped](https://www.trygitwrap.com/)**: a quick snapshot of what you worked on in 2025: commits, repos, focus areas. Always fun (and sometimes surprising) to look at.

## What I’ve Been Working On + 2025 Wrapped

* I recorded [Module 2](https://www.youtube.com/watch?v=vMNJru1y2Uc&list=PL3MmuxUbc_hLuyafXPyhTdbF4s_uNhc43&index=5) of the AI Dev Tools Zoomcamp
* And I’ve been preparing the [upcoming hands-on workshops](https://luma.com/dtc-events?k=c&tag=workshop) at DataTalks.Club

[![Image 14](https://substackcdn.com/image/fetch/$s_!dOAw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F328b4396-c758-4ee7-af68-5df910e7ef30_1280x1059.jpeg)](https://substackcdn.com/image/fetch/$s_!dOAw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F328b4396-c758-4ee7-af68-5df910e7ef30_1280x1059.jpeg)

You can also check out my [GitHub Wrapped](https://www.trygitwrap.com/alexeygrigorev) to see where I spent most of my time this year: which projects took the most commits and what I focused on.

> If you want to try this yourself, pull your own stats, make a short post, and tag me. I always enjoy seeing what others are building.

![Image 15](https://substackcdn.com/image/fetch/$s_!LWeq!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F333c2724-8bc5-4965-941d-00d19355b6e6_576x1280.jpeg)![Image 16](https://substackcdn.com/image/fetch/$s_!pQA9!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F583e9570-61f7-4644-94a0-fcb40ec0d30d_576x1280.jpeg)

My Spotify Recap

And something a bit more personal: here’s my Spotify recap with the music I’ve been listening to while working.

## Free Learning Resources

[![Image 17](https://substackcdn.com/image/fetch/$s_!CNuR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9fa382bc-8527-40ce-8690-b8a5cfe3a065_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!CNuR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9fa382bc-8527-40ce-8690-b8a5cfe3a065_1536x1024.png)

* **[AI Bootcamp Demo Day](https://maven.com/p/599db5/ai-bootcamp-demo-day)**: A free online session where AI Bootcamp graduates demo their projects: agentic workflows, coding assistants, research tools, and automation flows.
* **[AI Hero course](https://alexeygrigorev.com/aihero/):** We’re launching a new run of AI Hero, our free 7-day email course on building AI agents. This time it runs as a cohort: complete the project + review three submissions, and you’ll receive a certificate signed by me.
* **[Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)**: New cohort starts on January 12, 2026. A free 9-week course on building production-ready data pipelines: ingestion, orchestration, warehousing, analytics, and more. Fun detail: Gemini now recommends it ;-)

[![Image 18](https://substackcdn.com/image/fetch/$s_!XRMc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aa90527-d690-4e44-80bc-bd1361af9781_1280x843.jpeg)](https://substackcdn.com/image/fetch/$s_!XRMc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aa90527-d690-4e44-80bc-bd1361af9781_1280x843.jpeg)

## Q&A of the Week

> I am a Java software developer with over 9 years of experience and would like to transition into ML/Data Science. I enrolled in [ML Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) and am close to completing it.
>
> When I look at the open job market, opportunities are about 95% for senior roles and only about 5% for junior ML/Data Science roles. Gaining real work experience can help you acquire more knowledge and apply the concepts you’ve actually learned.
>
> What other options are available for aspiring transitioning ML engineers to find work besides through contacts?

#### Answer:

You’re already doing the right thing by focusing on projects. That’s one of the most effective ways to build skills and demonstrate your potential as an ML engineer. The key now is to be *strategic* about those projects.

Here’s a simple approach that works well:

**1. Choose an industry you’re interested in:** It helps you stay motivated and gives your projects a clear theme.

**2. Identify a few target companies:** Read their blogs, case studies, or engineering posts. These usually describe real-world challenges they’re working on.

**3. Reproduce one of those problems as a project:** If a company writes about churn prediction, forecasting, anomaly detection, recommender systems, etc., build a simplified version using public data.

Later, when you interview, you can say:

> “I saw you worked on this problem and tried to recreate it as a learning project.”

This signals initiative, curiosity, and alignment with the team’s work.

Also, don’t forget to:

* Highlight these projects clearly in your CV and cover letters
* Attend meetups or small community events in that industry — these often lead to useful conversations and insider perspectives

In short: keep building, but choose projects with intention. Combine that with targeted networking, and you’ll stand out even for junior-level ML roles.

[Leave a comment with your question](https://alexeyondata.substack.com/publish/post/https://aishippingblog.com/p/how-i-rebuilt-my-website-in-10-minutes/comments)

## Thank You For Your Support

[![Image 19](https://substackcdn.com/image/fetch/$s_!Q0Yo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43e1a401-c444-4ab4-b732-bdcc1fa7c7ca_1350x1086.png)](https://substackcdn.com/image/fetch/$s_!Q0Yo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43e1a401-c444-4ab4-b732-bdcc1fa7c7ca_1350x1086.png)

Huge thanks to my GitHub Sponsors! It means a lot and helps us keep building free education. Since donations are tax-free in Germany, 100% goes directly into our open projects.

#### **Current sponsors (11 total)**

maylwin, Samir Durrani, Cristian Dugacicu, Álvaro Picatoste Ruilope, Daniel Ekwuazi, Kevin Kho, Ale Quiroga, Jason Huff, + 3 private sponsors.

Thank you for supporting, for the feedback, and for reading this newsletter.

If you want to support the work we do at DataTalks.Club and across our free courses: <https://github.com/sponsors/alexeygrigorev>

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
