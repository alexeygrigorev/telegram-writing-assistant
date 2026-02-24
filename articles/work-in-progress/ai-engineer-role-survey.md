---
title: "AI Engineer Role Survey"
created: 2026-02-22
updated: 2026-02-22
tags: [ai-engineer, career, survey, interview]
status: draft
---

# AI Engineer Role Survey

A document collecting answers from real practitioners about their experience working as AI Engineers. The goal is to build a picture of what the role actually looks like in practice, based on first-hand accounts rather than job descriptions[^1][^3].

So far only one person has responded, but the plan is to gradually fill this article with more responses over time[^3].

## The Questionnaire

Questions about the AI Engineer role (LLM / GenAI). You can answer briefly or in detail, by text or voice. If something is uncomfortable, skip it[^2].

### Interviews

If you recently interviewed for an AI/LLM role, answer the questions below. If you interviewed at multiple companies, it would be helpful to describe each process separately.

1. What was the position title you interviewed for?
2. What does the company do approximately? (no name needed, just the domain/product type)
3. What stages did the process consist of, and how many interviews were there in total?
4. What questions or tasks were given at each stage? (examples if you remember)
5. Was there a take-home assignment? If yes, what did you need to do and how long did it take?

### Real Work with AI

If you already work with AI/LLM, answer the questions below.

1. What is your role?
2. What does your company and team do? What problem does AI solve in your product?
3. What typical tasks do you do?
4. What tools and technologies do you use?
5. Do you work with: RAG, agents, fine-tuning, evals, dataset preparation, production infrastructure? Which ones?
6. More engineering or research?
7. What would you advise someone who wants to enter this role?

## Response: Nick

### Real Work with AI

Role: Data Engineer at a B2B tech company[^4].

The company does a lot of different things. The specific team works on anonymization of unstructured data - text, NLP, and audio[^4].

The problem AI solves: data anonymization and validation that data has been properly anonymized[^4].

### Typical Tasks

Three main areas of work[^4]:

1. Data preparation for validation of results through human annotations. This includes sampling, preparation, validation, distribution, and then post-processing of the annotated data.

2. Measuring the correctness of anonymization. Evaluating anonymization solutions against golden truth datasets - a calibration and validation task using evals and guardrails.

3. Data Engineering and human-in-the-loop workflows.

### Tools and Technologies

Everything available on the market. For coding, and not just coding but also research, document search, writing documentation, etc. - Claude Code is used with all possible extensions and tooling[^4].

Beyond Claude Code, there are custom agentic solutions where under the hood you can run various models - pretty much everything on the market: Opus, Codex, Gemini, and other solutions[^4].

Also frequently uses agentic tools developed within the company - either in the format of chat bots or data agents that do data processing for you[^4].

### RAG, Agents, Fine-Tuning, Evals, Datasets, Production Infra

All of it is present, both at the corporation level and at the specific team level. Everything on the market and things that don't exist on the market yet are being used to optimize agentic solutions[^4].

### Engineering vs Research

Engineering in its pure form. Evals, guardrails, LLM-as-judge, assisted coding, and any agents running in autonomous mode[^4].

### Advice for Entering the Role

Don't start with autonomous agents. Build a good agentic solution that requires human-in-the-loop first, because having collected all that information, it will be much easier to build an autonomous agent on evals and guardrails later[^4].

Ask right away about what is asked in interviews - understand the general landscape and limitations when working in a company[^4].

In startups, enterprise, and big tech, agentic development evolves completely differently and there are completely different tasks for implementing agentic solutions[^4].

Be in the top 10% of the industry. This is almost impossible right now - follow trends, while somehow filtering the digital stream, and try to optimize yourself. Working with a single context is already becoming a critically lacking skill. If you're not working in three, four, five contexts in parallel, it will be very difficult to enter the industry, and even more so to maintain yourself in this industry at top companies[^4].

### Interview Process Opinions

First: no coding at all. None whatsoever. If you want to understand how a person thinks, it's either debugging or working with a project for an hour to an hour and a half. Ideally in a setup where the person can show their own environment - come with prepared skills and show how they work. In companies where there are no restrictions, ideally the person should demonstrate their own setup[^4].

Test assignments: an interesting approach, but only if the company is ready to give feedback and actually look at the test assignment[^4].

Third, what's becoming critical: system design with AI elements. For example, if we're building AI capabilities in a company, we absolutely need to understand how a person will think about building any service or any component with interfaces for AI, with tooling for AI. Understanding the limitations on security, access rights, and everything related to AI integration. And understanding that AI will need to scale to a thousand-plus nodes, potentially 5-10x compared to the current load[^4].

## Sources

[^1]: [20260222_093944_AlexeyDTC_msg2205_transcript.txt](../inbox/used/20260222_093944_AlexeyDTC_msg2205_transcript.txt)
[^2]: [20260222_093955_AlexeyDTC_msg2206.md](../inbox/used/20260222_093955_AlexeyDTC_msg2206.md)
[^3]: [20260222_094007_AlexeyDTC_msg2207_transcript.txt](../inbox/used/20260222_094007_AlexeyDTC_msg2207_transcript.txt)
[^4]: [20260221_200011_AlexeyDTC_msg2202_transcript.txt](../inbox/used/20260221_200011_AlexeyDTC_msg2202_transcript.txt)
