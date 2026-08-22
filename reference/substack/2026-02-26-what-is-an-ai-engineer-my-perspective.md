---
title: "What Is an AI Engineer? My Perspective After 15+ Years in Software and ML"
date: 2026-02-26
url: https://aishippingblog.com/p/what-is-an-ai-engineer-my-perspective
---

Hey there,

I got two to share with you:

## 1) The AI Shipping Labs community is now open for early members

[![Image 1](https://substackcdn.com/image/fetch/$s_!-LkD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81c12769-25ff-470b-9c7c-250f2ea6439f_1982x1402.png)](https://substackcdn.com/image/fetch/$s_!-LkD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81c12769-25ff-470b-9c7c-250f2ea6439f_1982x1402.png)

We are actively building the [AI Shipping Labs](https://aishippinglabs.com/) community and recently integrated Stripe into the website. Early members [can already join](https://aishippinglabs.com/#tiers).

At this stage, the community is intentionally small and evolving. If you join now, you can influence the structure, session formats, and priorities. You also get direct access to me to discuss your projects, positioning, or career questions.

Based on your votes, we chose Slack as the main platform. It was the clear winner in the poll. Thanks to everyone who participated!

[Join here](https://aishippinglabs.com/#tiers)

## 2) New Wednesday series on AI Engineering

[![Image 2](https://substackcdn.com/image/fetch/$s_!zrKY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ff9be0e-ae98-4f82-9990-2afe2ead6877_1200x675.png)](https://substackcdn.com/image/fetch/$s_!zrKY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ff9be0e-ae98-4f82-9990-2afe2ead6877_1200x675.png)

I started sharing results of [my research on the AI Engineer role through a live event series](https://alexeyondata.substack.com/p/what-is-an-ai-engineer-in-2026-join), and the first two events collected 1,700+ registrations.

As interest grew, it became clear that we could not cover everything during those sessions. Some of the material I had prepared did not fit within the agenda, and several of your questions remained unanswered due to time constraints.

So I decided to continue this work in a structured newsletter series.

Every Wednesday, you will receive a focused article that explores one aspect of the AI Engineer role in depth. The newsletter will contain a concise version, with a link to a more detailed article on the AI Shipping Lab website.

I am starting today with a piece that outlines my current view of the AI Engineer role. Later in the series, we will use it as a baseline and compare it with market signals from both companies and candidates.

> Before we move to the article, one important note: this series is evolving and builds largely on your questions and requests about AI Engineering.
>
> If there is something you find unclear about the role, something you struggle with, or a specific topic you want me to analyze next, just reply and let me know. Your input will directly shape the upcoming articles.

[![User's avatar](https://substackcdn.com/image/fetch/$s_!lKbC!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54a0ec21-251b-49e2-aba6-93c13f3cd8cb_800x800.jpeg)

Join Alexey Grigorev’s subscriber chat

Available in the Substack app and on web](https://open.substack.com/pub/alexeyondata/chat?utm_source=chat_embed)

## What Is an AI Engineer? My Perspective

[![Image 4](https://substackcdn.com/image/fetch/$s_!UZ-z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10f21aa8-7eb7-457a-9922-47809605eea3_2048x901.png)](https://substackcdn.com/image/fetch/$s_!UZ-z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10f21aa8-7eb7-457a-9922-47809605eea3_2048x901.png)

​​I worked for around 15 years in software engineering and 12 years building machine learning systems. I teach the AI Engineering Buildcamp on production-ready AI agents and systems, and I regularly talk with people in the field. So I consider myself someone who can speak about the role.

### What is an AI Engineer?

I consider an AI engineer to be someone responsible for integrating AI into the product. They build and operate AI-powered systems, ensuring the AI component runs reliably, can be evaluated, and can be maintained and improved over time.

### What does an AI Engineer Do?

[![Image 5](https://substackcdn.com/image/fetch/$s_!-Nw2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f555e42-3118-409a-ae6a-a5c7240c0237_1404x646.png)](https://substackcdn.com/image/fetch/$s_!-Nw2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f555e42-3118-409a-ae6a-a5c7240c0237_1404x646.png)

An AI Engineer is usually responsible for:

* Translating product requirements into well-scoped AI problems
* Selecting and integrating appropriate foundation models and tools
* Crafting effective prompts and versioning them
* Defining success metrics and building comprehensive test suites
* Managing deployment, monitoring system performance, and handling cost optimization
* Implementing security measures

### How Does AI Engineering Relate to ML Engineering and Data Science?

AI engineering shares many production concerns with ML engineering and data science, but the focus of the effort differs.

Data scientists typically focus on building models, while ML engineers are responsible for deploying them to production.

AI engineers operate in both domains, but with an important distinction: in most contemporary AI applications, the foundational model is a third-party service accessed via an API (such as OpenAI, Anthropic, or Google). This shifts the focus from model development to various engineering tasks, including system integration, prompt design, output structuring, evaluation, and ensuring operational reliability.

### Where the AI Engineer Sits in an Organization

[![Image 6](https://substackcdn.com/image/fetch/$s_!8x8w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2c0f698-cf8f-44d7-a167-31cfbcca6d66_1418x528.png)](https://substackcdn.com/image/fetch/$s_!8x8w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2c0f698-cf8f-44d7-a167-31cfbcca6d66_1418x528.png)

The title “AI engineer” can mean different things depending on an organization’s maturity, structure, and existing technical capabilities.

In organizations with established ML teams, AI engineering work can be:

* Distributed among existing team members. In that case, data scientists expand their scope to include model interaction tasks, and ML engineers and software engineers take on integration responsibilities. Team members balance their existing responsibilities with new AI-related work, often resulting in a substantial increase in workload.
* Or delegated to dedicated AI engineers. In that case, the role tends to be more specialized and focused. The AI engineer may sit within a product engineering team, a centralized AI platform team, or an applied ML group.

In startups, the AI engineer typically acts as a product-focused generalist. The same person may move from experimentation to production hardening once a feature proves valuable. Because teams are small, responsibilities are fluid, and boundaries between product engineering, ML work, and infrastructure are less rigid.

### Key Skills of an AI Engineer

Shipping and maintaining an AI feature in production requires discipline across evaluation, engineering, and operations.

Here are the core skills that matter in the AI Engineering practice:

#### 1. Building RAG Systems

The ability to design and implement Retrieval-Augmented Generation pipelines.

This includes ingesting data from sources, chunking and embedding content, implementing semantic search, and generating grounded responses using LLMs.

#### 2. Designing Agentic Systems with Tool Use

The ability to move beyond simple chat interfaces and build tool-using agents.

This includes implementing function calling, exposing structured tools, and integrating MCP to extend agent capabilities. It also includes designing reasoning flows that determine when and how agents use tools.

#### 3. Prompt and System Evaluation

The ability to design and execute structured evaluations for AI features.

This includes creating automated tests that send real inputs through the system and verify structured outputs, developing and maintaining evaluation datasets, establishing quality metrics, and re-running evaluations after every prompt or model update to identify regressions.

#### 4. Monitoring and Observability

The ability to make AI systems inspectable in production.

This includes logging inputs and outputs, tracking error rates and failure modes, building dashboards, and analyzing logs to detect misalignment or quality drift.

#### 5. End-to-End System Design

The ability to design, build, evaluate, and monitor a full AI application.

This includes defining use cases, structuring data pipelines, integrating retrieval, agents, evaluation, and monitoring into a coherent architecture. It culminates in a capstone project built from scratch and presented as a portfolio artifact.

### AI Engineering Work

In the article on the website, I show what an AI Engineer does using an example of an online classifieds website. We move from integrating a simple AI feature into the website to adding retrieval-augmented generation (RAG) to agentic systems.

I recommend reading the full article for a detailed explanation and screenshots. The article also has an FAQ with answers to relevant questions.

[Read the full article](https://aishippinglabs.com/blog/what-is-an-ai-engineer-alexey-grigorev-perspective)
