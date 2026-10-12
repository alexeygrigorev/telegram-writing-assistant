---
title: "Trends in AI Engineering"
date: 2026-10-12
url: https://aishippingblog.com/p/trends-in-ai-engineering
---

Last week I ran a webinar with [Hugo Bowne-Anderson](https://open.substack.com/users/63978139-hugo-bowne-anderson?utm_source=mentions). Hugo and I met in Berlin about a month before, had a great breakfast, and decided to do something together.

The first step we decided on was an open ask-us-anything session - which was the webinar.

We had two goals for it:

* help the people who came to the webinar
* understand what we could create together for you longer term

At the end of the session, Hugo and I decided to turn the webinar into a Substack article.

In the session, we talked about both AI engineering and agentic engineering. It was a lot of content, so I decided to split it into two parts. In this article, I focus on AI engineering only.

In particular, I’ll cover:

* Hugo’s distinction between AI engineering and agentic engineering
* What we can see in nine monthly scrapes of AI engineering job postings
* Which skills will stay valuable, and why working with people still matters
* What to focus on if you want to become an AI engineer
* The course Hugo and I want to build

## **Hugo and Me**

[![Alexey Grigorev and Hugo Bowne-Anderson in a cafe in Berlin](https://substackcdn.com/image/fetch/$s_!Nu4P!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d4afd7c-0138-4d60-be1a-01f30f76dc2c_1600x1200.jpeg)](https://substackcdn.com/image/fetch/$s_!Nu4P!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d4afd7c-0138-4d60-be1a-01f30f76dc2c_1600x1200.jpeg)

Hugo and I at our breakfast in Berlin

Since you’re reading this newsletter, I hope you already know a few things about me. I like calling myself a product AI engineer: I do whatever it takes to integrate AI from the user’s perspective. I teach this in my courses.

Hugo’s background is in mathematics, physics, and biology. He researched cell biology at the Max Planck Institute in Dresden and then at Yale. About 15 years ago he moved to industry, but he stayed in education. He worked at DataCamp, taught in the SciPy and PyData ecosystems, and did developer relations at startups such as Coiled and Outerbounds. He hosts the [Vanishing Gradients](https://vanishinggradients.fireside.fm/) podcast, and that’s how we first met - we’ve done a bunch of podcasts together.

## **AI Engineering vs Agentic Engineering**

We talked about a lot of things in the session. One of them was Hugo’s distinction between two terms that often get confused:

* In agentic engineering, you build software with agents. The agent is part of the dev team. Your job is specification, delegation, review, and orchestration.
* In AI engineering, you build agentic search, RAG, or an agent. AI is part of the product. You think about models, prompts, evals, harness engineering, and agentic loops.

[![Two-column slide: in agentic engineering, the agent is part of the development team; in AI engineering, AI is part of the product](https://substackcdn.com/image/fetch/$s_!_xCj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32b4eff4-92ba-4126-afef-ec0411708cae_1600x902.jpeg)](https://substackcdn.com/image/fetch/$s_!_xCj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32b4eff4-92ba-4126-afef-ec0411708cae_1600x902.jpeg)

Hugo’s slide comparing agentic engineering and AI engineering

In practice, you do both. You build AI-powered products with agents. And for agentic engineering, you build up your own setup - skills in your AGENTS.md, MCP servers, sandboxes, and guardrails.

I see this confusion among people who join my courses too: they join a course about AI engineering wanting to learn how to use AI for coding. There’s a lot of overlap, but the work is different. If you write code with AI, someone else takes care of evaluating and monitoring that tool. You focus on creating the proper specification, making sure the agent follows it, and enforcing the development lifecycle rules.

In this article, we focus on AI engineering, and in the next one, on agentic engineering.

## **The Job Market**

I maintain the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide) repository.

Every month since February 2026 I scrape job postings for the query “AI engineering” in six locations: Berlin, Amsterdam, London, New York, Los Angeles, and all of India. Then I use LLMs to extract skills, responsibilities, and use cases from each posting.

This is what one processed job posting looks like:

```
company:
  name: Ecolab
  focus: Water, hygiene and infection prevention solutions
position:
  title: Senior AI Engineer
  ai_type:
    type: ai-first
  responsibilities:
  - Lead development of scalable GenAI-powered systems
  - Design intelligent workflows leveraging LLMs, vector-based retrieval, and multi-agent
    orchestration
  - Drive solution architecture for AI applications
  - Mentor junior engineers
  - Deliver production-ready applications integrated with business processes and platforms
  use_cases:
  - Intelligent business process workflows powered by LLMs
  - Vector-based retrieval and multi-agent orchestration for enterprise applications
  - GenAI applications integrated with business platforms
  skills:
    genai: [Generative AI, LLMs, RAG, Multi-Agent Systems]
# ...
```

It’s not enough data to predict the future, but I can already see where the market is going.

The overall market is growing, and there’s a lot of demand for AI engineers.

[![Bar chart of AI engineering job postings per monthly scrape from February to September 2026, from 895 to 1,086 with a spring dip and a peak of 1,222 in August](https://substackcdn.com/image/fetch/$s_!UVDQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbab5810c-8093-4fa3-a7a5-b7844aa5bce3_1600x864.png)](https://substackcdn.com/image/fetch/$s_!UVDQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbab5810c-8093-4fa3-a7a5-b7844aa5bce3_1600x864.png)

AI engineering postings per monthly scrape

Forward-deployed engineer (FDE) roles grow even faster than the market overall. The number of FDE postings has roughly doubled since February.

> If you want to learn more about FDEs, I have a separate analysis of this part of the AI jobs market:
>
> [What AI Forward-Deployed Engineers Do](https://aishippingblog.com/p/what-ai-forward-deployed-engineers)

[![Bar chart of forward-deployed engineer postings per scrape, growing from 18 in February to 34-37 in July through September 2026](https://substackcdn.com/image/fetch/$s_!5MWL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ce25ae9-1849-4f81-ba54-e6fcff969331_1600x864.png)](https://substackcdn.com/image/fetch/$s_!5MWL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ce25ae9-1849-4f81-ba54-e6fcff969331_1600x864.png)

Forward-deployed engineer postings per scrape

Roles that focus on training models are shrinking. Before, companies hired more people to train models with PyTorch. Now they post fewer of these roles. And I can see fewer inference and serving roles in the data too.

[![Line chart: the share of AI-first postings that mention inference and serving skills fell from 20% in February to 16% in September 2026, with a dip to 10% in August](https://substackcdn.com/image/fetch/$s_!wgkx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1438780c-60c5-4bff-a93c-23ffd3734be6_1600x864.png)](https://substackcdn.com/image/fetch/$s_!wgkx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1438780c-60c5-4bff-a93c-23ffd3734be6_1600x864.png)

Share of AI-first postings that mention inference and serving skills

The data suggests that companies now mostly use “AI engineer” to mean someone who calls models through APIs and builds things around them.

[![Line chart: the share of AI-first postings that mention the integrator stack grew from 80% to 91%, while the trainer stack fell from 38% to 30%](https://substackcdn.com/image/fetch/$s_!KDqu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62f9eaf1-1974-4df9-b30b-e770d4784a52_1600x864.png)](https://substackcdn.com/image/fetch/$s_!KDqu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62f9eaf1-1974-4df9-b30b-e770d4784a52_1600x864.png)

Share of AI-first postings that mention the integrator stack (RAG, agents, LLM APIs) vs the trainer stack (PyTorch, fine-tuning, CUDA)

Companies build agents and RAG around these models, and both keep growing. Agents went from 50% to 60% of all postings, RAG from 33% to 45%.

[![Line chart: the share of postings that mention agents grew from 50% to 60%, and RAG from 33% to 45%, between February and September 2026](https://substackcdn.com/image/fetch/$s_!KqJE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F839c18ef-2578-4bc0-b9f1-154fc078ac0d_1600x864.png)](https://substackcdn.com/image/fetch/$s_!KqJE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F839c18ef-2578-4bc0-b9f1-154fc078ac0d_1600x864.png)

Share of all postings that mention agents and RAG

There are almost no junior positions: only about 1% of job titles say junior or entry level. Half of the titles don’t state a level, but among those that do, almost all are senior or above. Starting your career as an AI engineer is hard.

[![Horizontal bar chart of seniority from job titles in the September 2026 scrape: junior or entry 1.1%, no level in title 49.8%, senior 27.8%, lead 7.0%, staff or principal 13.1%, manager or director 1.1%](https://substackcdn.com/image/fetch/$s_!zlJ6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c19de25-a6a3-469a-aa76-a58fda687b1f_1600x864.png)](https://substackcdn.com/image/fetch/$s_!zlJ6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c19de25-a6a3-469a-aa76-a58fda687b1f_1600x864.png)

Seniority from the job title, September 2026 scrape

So AI engineering is not a junior role.

## **Relevant Skills**

We can observe the current situation on the market through data and by talking to friends and our network. But we don’t have a crystal ball to see what roles, hiring processes, or even tools will look like in a year or two.

But based on our past experience, we can try to make an educated guess about the skills that will stay relevant and valuable in the future.

Hugo believes that it’s a combination of:

* A hacker mentality - playing with new models when they come out, exploring what’s possible and seeing how to use them to deliver business value or help people
* Data science skills - statistics, data analysis, using data to improve products
* Domain expertise - SRE, DevOps, marketing, or anything else

I can’t argue with that, but I would also add the problem discovery skill.

[![A 2x2 grid of four skills that stay valuable: hacker mentality, data science, domain expertise, and problem discovery](https://substackcdn.com/image/fetch/$s_!WAzi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fff884f-e533-4a20-9c85-747dfaa4a229_780x300.png)](https://substackcdn.com/image/fetch/$s_!WAzi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fff884f-e533-4a20-9c85-747dfaa4a229_780x300.png)

Four skills to stay valuable

There are so many problems around us waiting to be discovered and solved. Look at your own everyday life. You repeat many things, and many things are mildly annoying, but you aren’t doing anything about them yet.

With AI, I can finally approach these problems. But before I can even approach them, I need to know they exist and identify them. Only then can I solve them with AI. AI can’t find these problems for you, and you can stand out by learning how to find them.

And finally, we need the human skills.

## **Human Skills: Working With People**

We use agents to write code, and we write code to solve problems for our customers. Our customers are people, not agents. We still need the human connection, user interviews, and everything else that product managers and product designers have been doing for a long time.

As a solo founder, I can go far with AI. But my background is engineering, and I don’t have marketing or sales skills. For me, it’s hard to market and sell what I build.

Freelancers have the same problem. You need to explain to clients why you charge $2,000 per day when a Claude subscription costs $200 per month. At work, you still need to convince your manager to give you that promotion.

Hugo believes that the work of engineers is speaking with people, understanding their problems, and solving them in a way that gives them more value than they pay. Even this session exists because we (humans) met in Berlin and had breakfast.

[Share](https://aishippingblog.com/p/trends-in-ai-engineering?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## **Becoming an AI Engineer**

There are also technical skills that you need. If you want to become an AI engineer and have a limited amount of time, it makes sense to focus on the areas with the most return on investment: RAG, agents, and evaluations.

Evals are the most important part. Systems built on LLMs aren’t deterministic, so we can’t simply trust them. We need a framework to make sure they can be relied on - for example, an evaluation set built from real user data.

Most jobs assume you have evaluation skills, but we can also see that more and more positions explicitly list them as a requirement.

[![Line chart: the share of AI engineering postings that mention LLM evaluation grew from 20% in February to 25% in September 2026](https://substackcdn.com/image/fetch/$s_!ADO8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa914cd3b-063d-4ca3-bb8e-8c9e64272ab0_1600x864.png)](https://substackcdn.com/image/fetch/$s_!ADO8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa914cd3b-063d-4ca3-bb8e-8c9e64272ab0_1600x864.png)

Share of AI engineering postings that mention LLM evaluation

You learn evals by building a project: an agent or an AI-powered application with real users.

There are also things you can skip. The data shows that you don’t need to focus on training and serving models. Hugo compared training models to working on an internal combustion engine. If you’re a Formula One driver, it’s good to know how it works, but most people who use a car don’t need to. An AI engineer works on a product.

You don’t need to know LLM internals to start working as an AI engineer. At the beginning, it’s enough to know how to send a request to an LLM provider, build everything around it, and have the data science mindset. Some companies do lower-level work and may ask for it, but they’re a minority in my data, and the share keeps falling.

But if you want to learn more about these things, I’d recommend Inference Engineering by Philip Kiely. Recently [we hosted a book club about it](https://aishippinglabs.com/books/inference-engineering), and it’s a wonderful book if you want to know what happens after you send a request. But if your goal is to become an AI engineer, read it later and focus on building projects now. If you want to become an inference engineer, that’s the book to read.

[![Cover of Inference Engineering by Philip Kiely](https://substackcdn.com/image/fetch/$s_!j2Df!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23703efb-5c17-4b94-a141-d11a40975b96_911x481.png)](https://substackcdn.com/image/fetch/$s_!j2Df!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23703efb-5c17-4b94-a141-d11a40975b96_911x481.png)

Inference Engineering by Philip Kiely

## **Agentic Engineering**

That was only half of our webinar with Hugo. In the second half, we talked about agentic engineering - using AI assistants to create code. I’m working on an article about that and will publish it soon.

[![Hugo's slide of the agentic software lifecycle: a spec goes to an agent-driven build, then to verification by human review, agent review, LLM as judge, and automated tests, and only working code ships](https://substackcdn.com/image/fetch/$s_!4P0X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57f338f2-aa85-4fdd-a0fe-f17ce992d1a9_1600x859.jpeg)](https://substackcdn.com/image/fetch/$s_!4P0X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57f338f2-aa85-4fdd-a0fe-f17ce992d1a9_1600x859.jpeg)

Hugo’s slide on the agentic software lifecycle

In it, I’ll cover:

* How agents changed the way we write code
* Why verification is now the bottleneck
* The implementer-reviewer pattern: letting one agent check another
* How to deal with sloppy agent code
* The rules for better code and better writing
* How to organize running many agents in parallel
* Dark software factories
* How I stay out of the loop in my own projects

Subscribe to make sure you don’t miss it.

## **Our Next Course**

The main goal of our session was to find out how we can help you achieve your goals and what we can build for you through a course that we want to run together. There are infinitely many ideas, so we want to understand what the best direction is.

[![Intro of the questionnaire Help Shape a New Practical AI Engineering Course by Hugo Bowne-Anderson and Alexey Grigorev: a paid hands-on course, tuition of about US$1,500, a 4 to 5 minute survey, and a 30% discount for respondents](https://substackcdn.com/image/fetch/$s_!K7j-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16a0b9ac-a8d5-4272-b3af-52a441586903_1676x1120.png)](https://substackcdn.com/image/fetch/$s_!K7j-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16a0b9ac-a8d5-4272-b3af-52a441586903_1676x1120.png)

The questionnaire we shared at the end of the session

Tell us where you stand, what you want to build, where you’re stuck, and what format you prefer. We want to hear both what frustrates you and what excites you about AI.

If you want to help us, fill in [this questionnaire](https://forms.gle/EjtBzfmZft15dCvY9). It takes about 5 minutes. As a thank you, people who fill it in will get a discount on the future course when we announce it.

Of course, I’ll announce it here in this newsletter.
