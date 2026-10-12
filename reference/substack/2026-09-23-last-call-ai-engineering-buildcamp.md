---
title: "Last Call: AI Engineering Buildcamp Cohort 4"
date: 2026-09-23
url: https://aishippingblog.com/p/last-call-ai-engineering-buildcamp
---

We started the new cohort of AI Engineering Buildcamp this Monday, but you can still join.

[![Image 1](https://substackcdn.com/image/fetch/$s_!bRe3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ebf638a-b71b-4ae4-bd40-34a68d083e27_1280x777.jpeg)](https://substackcdn.com/image/fetch/$s_!bRe3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ebf638a-b71b-4ae4-bd40-34a68d083e27_1280x777.jpeg)

We had our first live session, where I went through the course structure, talked about projects, and answered questions from the participants.

In this post, I want to focus on what we discussed during the launch session.

In particular, I’ll cover:

* Course curriculum
* How the capstone project works
* How to come up with a project idea
* How I’ll help with the project scope
* How we’ll use coding agents
* Common questions

Registration is still open until next Monday, September 28, and there’s one buffer week to catch up if you’re joining late.

[Join AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents)

## Course Overview

I already wrote about the course in detail in my previous post. I covered the curriculum, homework projects, projects from the previous cohorts, workload, and other details in that post.

[AI Engineering Buildcamp Starts Next Week](https://aishippingblog.com/p/ai-engineering-buildcamp-starts-next)

Let me do a quick recap:

* Week 1 is about the foundations. We prepare the environment, learn how to work with LLMs, and then focus on RAG and search.
* Week 2 is a buffer week. I want to make sure everyone has enough time to prepare the environment. If you’re joining a bit late, you will use this time to catch up.
* Week 3: agents. We go from regular RAG to agentic RAG, learn about tool calling, and implement the agent loop ourselves, and then use an agentic framework.
* Week 4: testing. We add tests to our agent and make sure it behaves as expected.
* Week 5: monitoring. We log all the interactions between the users and the agent.
* Week 6: evaluation. We create evaluation datasets, use LLM judges, and systematically evaluate the system.
* Weeks 7 and 8: focused project work.
* Week 9: peer review and demo day.

[![Image 2](https://substackcdn.com/image/fetch/$s_!TqWv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc45ab45e-b901-4d49-98cf-b7c4a2448954_1672x721.png)](https://substackcdn.com/image/fetch/$s_!TqWv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc45ab45e-b901-4d49-98cf-b7c4a2448954_1672x721.png)

The course takes 9 weeks: 6 week of core work and 3 weeks of project work.

## The Capstone Project

The project is the most important part of the course. I want everyone to finish with a project that you can add to your project portfolio, use at work or show it to potential clients.

For the capstone, you need to come up with a project idea and implement it end-to-end. It’ll be a RAG application, an agent, or something in between. You will cover it with tests, add monitoring, evaluate it and deploy to the cloud.

In our curriculum, weeks 7 and 8 are specifically dedicated to project work, but I want you to start working on your projects from week 1. This way, by the end of week 6 you have something working, and you can spend weeks 7 and 8 polishing it and finishing the missing parts.

I you already have an idea - that’s great, I’ll help you refine it.

But if you don’t, I’ll give you a project ideation process that you can follow to select a meaningful idea to work on. This approach uses design thinking to discover problems you can solve with AI.

[![Image 3](https://substackcdn.com/image/fetch/$s_!LLyp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdeb5b3b8-a6e1-425e-b62f-53d4b6c819eb_1707x921.png)](https://substackcdn.com/image/fetch/$s_!LLyp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdeb5b3b8-a6e1-425e-b62f-53d4b6c819eb_1707x921.png)

## Coding Agents

I also want to encourage you to use coding agents during the course.

During the lessons, we write code together. When I cover something in the coding sessions, I want you to understand how things work. For example we first implement the tool-calling loop ourselves before using any agent framework.

But once you understand the core concepts and the code from the lessons, you can give it to a coding agent:

> Based on the code we created in the lesson, I want to create <YOUR PROJECT IDEA>. Please use this implementation as a reference and adapt it to my project.

[![Image 4](https://substackcdn.com/image/fetch/$s_!8aOo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe46add96-5d0b-4421-a38a-4ce62d66ee68_1952x1243.png)](https://substackcdn.com/image/fetch/$s_!8aOo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe46add96-5d0b-4421-a38a-4ce62d66ee68_1952x1243.png)

It makes the project development much faster. Instead of starting from zero, the coding agent already has an example that it will use for your own project. You already understand the original implementation, so understanding the code for your project will be much easier.

This is how I recommend using coding agents: not as a replacement for learning, but as a tool that can get us from an idea to a working implementation faster.

See what people from Cohort 3 implemented:

[13 AI Projects from AI Engineering Buildcamp Cohort 3](https://aishippingblog.com/p/13-ai-projects-from-ai-engineering)

## Questions From the Launch Session

We had a few questions during the launch stream and I think they are quite interesting, so I wanted to cover them here too.

### Is RAG Dead?

No, it’s not dead. On the contrary, according to my analysis for [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide), the majority of jobs require it. That’s why we start the course from RAG and cover it in detail.

The reasons we need it:

* The model doesn’t have access to proprietary data. If your company has an internal knowledge base, the model has never seen it. With RAG, you can search this knowledge base, retrieve the relevant information, and include it in the context.
* These knowledge bases are usually not that large. With models capable of processing 128 million tokens and more, we can fit the entire dataset into the context window. The RAG is still needed though: if you send the entire dataset to the model, it will have hard time figuring out what’s useful. But if you retrieve only the relevant pieces, you send less data. This makes it faster and cheaper, and it also gives the model more focused context.

### Are We Going to Cover Fine-Tuning?

No. Fine-tuning is slow, expensive, and often not needed.

If we have our internal documentation, we can prepare a training dataset in a special format, take a model with open weights, rent a GPU, and spend a day or two fine-tuning it, so it actually learns from our data. Next time we use it, we don’t need to inject the context with RAG: the model already has our knowledge base internally in its weights.

There are a few problems with fine-tuning though:

* You need to have a lot of data and prepare it in a special way
* GPUs aren’t cheap and not always available
* It requires time to tune the model
* It’s difficult to enforce answering with the learned information instead of the general knowledge it had
* The worst part: you update the dataset by including one new page and you need to fine-tune again

Now compare it with RAG: we just update the documents in the search index and that’s it. These problems make fine-tuning impractical for the majority of use-cases. And my job analysis shows that most companies don’t actually require it.

That’s why we don’t cover it in the course.

### Do We Need Multiple Agents?

In most cases you don’t. In many cases you don’t even need an agent, just RAG is enough.

I will help you understand when you need what, and scope your project in a way that it’s focused, manageable - and also possible to implement during the course.

We do have a few places where I cover multi-agent setup. For example, the Deep Research Agent uses multiple agents for different parts of the research process, or the Coding Agent that uses the plan-then-implement pattern.

But it’s not the focus of the course. It’s more important to first understand how to create one agent well, test it, add monitoring and evaluate it to make sure it works properly. And then, only if the problem actually requires more complexity, add it. (In many cases it doesn’t.)

## Can I Use Another Technology Stack?

In the course we use OpenAI, Python, Pydantic AI and other technologies to implement agents.

But you don’t have to use these specific technologies in your capstone. If you want to build your project in TypeScript - that’s fine. You want to learn LangChain and use it instead of Pydantic AI - totally fine too. Anthropic, Gemini, or another provider work well instead of Open AI.

If you don’t have a strong reason to choose something else, I recommend using the same stack as in the course. It will be easier for me to help you.

But it’s not a requirement.

## Do I Need an Expensive Coding Agent Subscription?

No. In fact, even a free subscription will be sufficient. There are a few places in the course where I use a coding agent to generate code - for example, for creating a streamlit tool for evals. But for that I use free Antigravity, so everyone can reproduce it. Some students prefer not to use any coding agent at all and it works too.

I’d still recommend investing at least $10 in getting an OpenCode subscription or $20 for Claude Code Pro or ChatGPT Plus, so you don’t need to worry about hitting the usage limits with the free subscriptions.

Also check my recent post about free and affordable coding agents:

[Free and Affordable AI-Native Development](https://aishippingblog.com/p/free-and-affordable-ai-native-development)

## What If I Can’t Attend the Live Sessions?

The course is designed to be asynchronous.

Each week we have a live office hour session. On these sessions we discuss questions, project ideas, architecture decisions, and other things that come up during the week.

If you can’t attend, it’s recorded and shared shortly after. You can also ask your questions in advance and we will cover them during the session.

Most of the content is already recorded as videos (with text articles along them), which you can watch whenever it’s convenient for you.

## Can It Help me Transition into AI Engineering?

Yes.

In previous cohorts we had participants from different backgrounds: software engineers, DevOps engineers, data scientists, researchers, and others. For many people the course helped them start doing AI engineering work in their existing company. Others used what they learned when looking for a new role. Some use these skills for freelancing.

If finding an AI engineering job after this course is one of your goals, I recommend thinking about the capstone as a portfolio project from the beginning. Build something you can include in your CV.

If you need help with that, I’ll be very happy to support.

I always enjoy our launch streams and this one was not an exception. It’s going to be a lot of fun!

[![Image 5](https://substackcdn.com/image/fetch/$s_!maJv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb31eb9d6-bd76-4aaa-9d29-ab844b168f42_2762x1120.png)](https://substackcdn.com/image/fetch/$s_!maJv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb31eb9d6-bd76-4aaa-9d29-ab844b168f42_2762x1120.png)

Registration closes next Monday, September 28. Use code “SUBSTACK” to get 20% off.

[Join Cohort 4](https://maven.com/alexey-grigorev/from-rag-to-agents)

See you on Monday!
