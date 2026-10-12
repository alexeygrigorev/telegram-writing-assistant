---
title: "Trends in AI Engineering: Lightning Lesson with Hugo Bowne-Anderson"
created: 2026-09-29
updated: 2026-10-11
tags: [ai-engineering, career, evals, job-market, hugo-bowne-anderson, lightning-lesson]
status: draft
---

# Trends in AI Engineering
## Webinar with Hugo Bowne-Anderson

Last week I ran a webinar with [Hugo Bowne-Anderson](https://substack.com/@hugobowne). Hugo and I met in Berlin about a month before, had a great breakfast, and decided to do something together.

The first step we decided on was an open ask-us-anything session - which was the webinar.

We had two goals for it:

- help the people who came to the webinar
- understand what we could create together for you longer term

https://youtu.be/whIdxTQsU0A

At the end of the session, Hugo and I decided to turn the webinar into a Substack article.

In the session, we talked about both AI engineering and agentic engineering. So I decided to split the content into two parts. In this article, I focus on AI engineering only.

In particular, I'll cover:

- Hugo's distinction between AI engineering and agentic engineering
- What we can see in nine monthly scrapes of AI engineering job postings
- Which skills will stay valuable, and why working with people still matters
- What to focus on if you want to become an AI engineer
- The course Hugo and I want to build

## Hugo and Me

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/hugo-and-alexey.jpg" alt="Alexey Grigorev and Hugo Bowne-Anderson in a cafe in Berlin">
  <figcaption>Hugo and I at our breakfast in Berlin</figcaption>
</figure>

Since you're reading this newsletter, I hope you already know a few things about me. I like calling myself a product AI engineer: I do whatever it takes to integrate AI from the user's perspective. I teach this in my courses.

Hugo's background is in mathematics, physics, and biology. He researched cell biology at the Max Planck Institute in Dresden and then at Yale. About 15 years ago he moved to industry, but he stayed in education. He worked at DataCamp, taught in the SciPy and PyData ecosystems, and did developer relations at startups such as Coiled and Outerbounds. He hosts the [Vanishing Gradients](https://vanishinggradients.fireside.fm/) podcast, and that's how we first met - we've done a bunch of podcasts together.

## AI Engineering vs Agentic Engineering

We talked about a lot of things in the session. One of them was Hugo's distinction between two terms that often get confused:

- In agentic engineering, you build software with agents. The agent is part of the dev team. Your job is specification, delegation, review, and orchestration.
- In AI engineering, you build agentic search, RAG, or an agent. AI is part of the product. You think about models, prompts, evals, harness engineering, and agentic loops.

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/agentic-vs-ai-engineering.jpg" alt="Two-column slide: in agentic engineering, the agent is part of the development team; in AI engineering, AI is part of the product">
  <figcaption>Hugo's slide comparing agentic engineering and AI engineering</figcaption>
</figure>

In practice, you do both. You build AI-powered products with agents. And for agentic engineering, you build up your own setup - skills in your AGENTS.md, MCP servers, sandboxes, and guardrails.

I see this confusion among people who join my courses too: they join a course about AI engineering wanting to learn how to use AI for coding. There's a lot of overlap, but the work is different. If you write code with AI, someone else takes care of evaluating and monitoring that tool. You focus on creating the proper specification, making sure the agent follows it, and enforcing the development lifecycle rules.

In this article, we focus on AI engineering, and in the next one, on agentic engineering.

## The Job Market

I maintain the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide) repository.

Every month since February 2026 I scrape job postings for the query "AI engineering" in six locations: Berlin, Amsterdam, London, New York, Los Angeles, and all of India. Then I use LLMs to extract skills, responsibilities, and use cases from each posting.

This is what one processed job posting looks like:

```yaml
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

It's not enough data to predict the future, but I can already see where the market is going.

The overall market is growing, and there's a lot of demand for AI engineers.

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/postings-per-month.png" alt="Bar chart of AI engineering job postings per monthly scrape from February to September 2026, from 895 to 1,086 with a spring dip and a peak of 1,222 in August">
  <figcaption>AI engineering postings per monthly scrape</figcaption>
</figure>

Forward-deployed engineer (FDE) roles grow even faster than the market overall. The number of FDE postings has roughly doubled since February.

> If you want to learn more about FDEs, I have a separate analysis of this part of the AI jobs market: [What AI Forward-Deployed Engineers Do](https://aishippingblog.com/p/what-ai-forward-deployed-engineers).

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/fde-postings.png" alt="Bar chart of forward-deployed engineer postings per scrape, growing from 18 in February to 34-37 in July through September 2026">
  <figcaption>Forward-deployed engineer postings per scrape</figcaption>
</figure>

Roles that focus on training models are shrinking. Before, companies hired more people to train models with PyTorch. Now they post fewer of these roles. And I can see fewer inference and serving roles in the data too.

The data suggests that companies now mostly use "AI engineer" to mean someone who calls models through APIs and builds things around them.

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/integrator-vs-trainer.png" alt="Line chart: the share of AI-first postings that mention the integrator stack grew from 80% to 91%, while the trainer stack fell from 38% to 30%">
  <figcaption>Share of AI-first postings that mention the integrator stack (RAG, agents, LLM APIs) vs the trainer stack (PyTorch, fine-tuning, CUDA)</figcaption>
</figure>

Companies build agents and RAG around these models, and both keep growing. Agents went from 50% to 60% of all postings, RAG from 33% to 45%.

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/agents-and-rag.png" alt="Line chart: the share of postings that mention agents grew from 50% to 60%, and RAG from 33% to 45%, between February and September 2026">
  <figcaption>Share of all postings that mention agents and RAG</figcaption>
</figure>

There are almost no junior positions: only about 1% of job titles say junior or entry level. Half of the titles don't state a level, but among those that do, almost all are senior or above. Starting your career as an AI engineer is hard.

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/seniority.png" alt="Horizontal bar chart of seniority from job titles in the September 2026 scrape: junior or entry 1.1%, no level in title 49.8%, senior 27.8%, lead 7.0%, staff or principal 13.1%, manager or director 1.1%">
  <figcaption>Seniority from the job title, September 2026 scrape</figcaption>
</figure>

So AI engineering is not a junior role.

## Relevant Skills

We can observe the current situation on the market through data and by talking to friends and our network. But we don't have a crystal ball to see what roles, hiring processes, or even tools will look like in a year or two.

But based on our past experience, we can try to make an educated guess about the skills that will stay relevant and valuable in the future.

Hugo believes that it's a combination of:

- A hacker mentality - playing with new models when they come out, exploring what's possible and seeing how to use them to deliver business value or help people
- Data science skills - statistics, data analysis, using data to improve products
- Domain expertise - SRE, DevOps, marketing, or anything else

I can't argue with that, but I would also add the problem discovery skill.

There are so many problems around us waiting to be discovered and solved. Look at your own everyday life. You repeat many things, and many things are mildly annoying, but you aren't doing anything about them yet.

With AI, I can finally approach these problems. But before I can even approach them, I need to know they exist and identify them. Only then can I solve them with AI. AI can't find these problems for you, and you can stand out by learning how to find them.

And finally, we need the human skills.

## Human Skills: Working With People

We use agents to write code, and we write code to solve problems for our customers. Our customers are people, not agents. We still need the human connection, user interviews, and everything else that product managers and product designers have been doing for a long time.

As a solo founder, I can go far with AI. But my background is engineering, and I don't have marketing or sales skills. For me, it's hard to market and sell what I build.

Freelancers have the same problem. You need to explain to clients why you charge $2,000 per day when a Claude subscription costs $200 per month. At work, you still need to convince your manager to give you that promotion.

Hugo believes that the work of engineers is speaking with people, understanding their problems, and solving them in a way that gives them more value than they pay. Even this session exists because we (humans) met in Berlin and had breakfast.

## Becoming an AI Engineer

There are also technical skills that you need. If you want to become an AI engineer and have a limited amount of time, it makes sense to focus on the areas with the most return on investment: RAG, agents, and evaluations.

Evals are the most important part. Systems built on LLMs aren't deterministic, so we can't simply trust them. We need a framework to make sure they can be relied on - for example, an evaluation set built from real user data.

Most jobs assume you have evaluation skills, but we can also see that more and more positions explicitly list them as a requirement.

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/llm-evaluation.png" alt="Line chart: the share of AI engineering postings that mention LLM evaluation grew from 20% in February to 25% in September 2026">
  <figcaption>Share of AI engineering postings that mention LLM evaluation</figcaption>
</figure>

You learn evals by building a project: an agent or an AI-powered application with real users.

There are also things you can skip. The data shows that you don't need to focus on training and serving models. Hugo compared training models to working on an internal combustion engine. If you're a Formula One driver, it's good to know how it works, but most people who use a car don't need to. An AI engineer works on a product.

You don't need to know LLM internals to start working as an AI engineer. At the beginning, it's enough to know how to send a request to an LLM provider, build everything around it, and have the data science mindset. Some companies do lower-level work and may ask for it, but they're a minority in my data, and the share keeps falling.

But if you want to learn more about these things, I'd recommend Inference Engineering by Philip Kiely. Recently [we hosted a book club about it](https://aishippinglabs.com/books/inference-engineering), and it's a wonderful book if you want to know what happens after you send a request. But if your goal is to become an AI engineer, read it later and focus on building projects now. If you want to become an inference engineer, that's the book to read.

## Agentic Engineering

That was only half of our webinar with Hugo. In the second half, we talked about agentic engineering - using AI assistants to create code. I'm working on an article about that and will publish it soon.

In it, I'll cover:

- How agents changed the way we write code
- Why verification is now the bottleneck
- The implementer-reviewer pattern: letting one agent check another
- How to deal with sloppy agent code
- The rules for better code and better writing
- How to organize running many agents in parallel
- Dark software factories
- How I stay out of the loop in my own projects

Subscribe to make sure you don't miss it.

## Our Next Course

The main goal of our session was to find out how we can help you achieve your goals and what we can build for you through a course that we want to run together. There are infinitely many ideas, so we want to understand what the best direction is.

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/course-questionnaire.png" alt="Intro of the questionnaire Help Shape a New Practical AI Engineering Course by Hugo Bowne-Anderson and Alexey Grigorev: a paid hands-on course, tuition of about US$1,500, a 4 to 5 minute survey, and a 30% discount for respondents">
  <figcaption>The questionnaire we shared at the end of the session</figcaption>
</figure>

Tell us where you stand, what you want to build, where you're stuck, and what format you prefer. We want to hear both what frustrates you and what excites you about AI.

If you want to help us, fill in [this questionnaire](https://forms.gle/EjtBzfmZft15dCvY9). It takes about 5 minutes. As a thank you, people who fill it in will get a discount on the future course when we announce it.

Of course, I'll announce it here in this newsletter.
