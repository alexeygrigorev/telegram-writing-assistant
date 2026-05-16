---
title: "Social Post Ideas"
created: 2026-02-07
updated: 2026-03-12
tags: [social-media, twitter, content-ideas, ai-engineering]
status: draft
---

# Social Post Ideas

A collection of interesting social media posts and content ideas for newsletters, curated for future reference and inspiration.

## AI Projects for 2026

Post by Rimsha Bhardwaj: "10 AI projects that will get you hired in 2026" - a comprehensive list of project ideas with tech stacks and learning resources[^1][^14].

The projects cover:
1. RAG App with Real Evaluations - OpenAI/Claude + vector DB + evals
2. Autonomous Research Agent - LangGraph + tools + citations
3. AI Customer Support Copilot - OpenAI + Zendesk/Intercom + moderation
4. Voice AI Agent - Twilio + Whisper + LLM
5. AgentOps Dashboard - OpenTelemetry + evals
6. AI Data Extraction Pipeline - Vision models + schema validation
7. Code Review AI for GitHub - GitHub Actions + LLM
8. Multi-Agent Planner for Workflows - LangGraph or CrewAI
9. AI Search Engine with Fresh Data - Search APIs + rerankers
10. Enterprise Prompt Security Tool - policy checks + red teaming

This aligns well with AI Engineering Buildcamp content and could be adapted into a "projects list" format.

## LLM Engineering Roadmap

Post by Inference: "The LLM Engineering Roadmap" - a structured learning path from foundations to production[^2].

The roadmap covers 10 stages:
1. LLM Foundations - Python/TypeScript, APIs, prompt engineering, structured outputs, function calling
2. Vector Stores - Embedding models, vector databases, chunking strategies, similarity search
3. RAG - Orchestration frameworks, document ingestion, retrieval methods, reranking
4. Advanced RAG - Query transformation, HyDE, corrective RAG, self-RAG, graph RAG
5. Fine-Tuning - Data preparation, LoRA/QLoRA/DoRA, SFT/DPO/RLHF, training tools
6. Inference Optimization - Quantization, serving engines, KV cache, flash attention, speculative decoding
7. Deployment - GPU scheduling, cloud platforms, Docker, Kubernetes, FastAPI
8. Observability - Tracing, latency tracking, token usage, cost tracking
9. Agents - Frameworks, function calling, memory systems, patterns
10. Production and Security - Prompt injection defense, guardrails, semantic caching, fallbacks

This could be adapted specifically for AI Engineering Buildcamp as a roadmap variant.

## Python Learning with Projects

Post by Paul Iusztin: "If I had to start learning AI engineering from scratch today" - emphasizes learning Python through building real projects rather than isolated syntax exercises[^5].

Key points from the post:

Gap 1: Python with real-world context

Most beginners learn Python in isolation - lists, loops, functions, dictionaries - but never build anything meaningful. The fastest way to learn Python is building small, complete tools:
- A personal finance dashboard
- A script that automates boring tasks
- A mini ETL pipeline pulling data from APIs
- A real project that organizes files, reads spreadsheets, plots charts

When learning Python for AI engineering, syntax isn't the goal - building things is.

Gap 2: Understanding RAG beyond the buzzwords

Engineers jump into complex architectures without mastering basics. A reliable RAG pipeline needs only four parts:
1. Clean data ingestion
2. Simple chunking and metadata design
3. A retrieval setup you can debug
4. A UI or API layer to expose it

Paul promotes two courses that teach these fundamentals: Beginner Python Primer for AI Engineering and Full-Stack AI Engineering.

## AI Evals Resources

Post by Paul Iusztin: "Every day, 100+ people ask me, 'How can I learn AI evals?'" - a curated list of 10 needed resources[^6].

The recommended resources cover:
1. Using LLM-as-a-judge (hamel.dev)
2. Demystifying evals for AI agents (Anthropic)
3. There are only 6 RAG Evals (jxnl.co)
4. Evaluation-driven development (decodingai.com)
5. Binary evals vs Likert scales (decodingai.com)
6. The mirage of generic AI metrics (decodingai.com)
7. Error analysis (YouTube)
8. Carrying out error analysis (YouTube)
9. Evaluating the effectiveness of LLM-evaluators (eugeneyan.com)
10. LLM judges aren't the shortcut you think (YouTube)

## Data Engineering vs AI Engineering Market Comparison

Post idea: scrape current job postings for data engineering and AI engineering positions and compare them. Look at which field has more stable market demand, which has more positions available, and which is more remote-friendly. This could be a data-driven analysis project - scrape the data and analyze it[^8].

## How to Select a Portfolio Project

Post idea: guide on how to choose projects for your portfolio. I've talked about this many times but never made a dedicated article. This would cover how to pick projects that show relevant skills, stand out to employers, and align with career goals in AI engineering[^8].

People often ask at office hours how to prepare a portfolio project. This needs to become a post because I always have to repeat the same things[^10].

## Office Hours FAQ Analysis

Idea: analyze all past office hours since the beginning and see what the most frequently asked questions are, what questions come up in general. Writing a pipeline in code that would do this is not that hard. A small mini-project[^11].

## GitHub Resources for Prompting and LLM Fundamentals

Post by aditya (@adxtyahq): "Complete GitHub Resources to Learn Prompting and LLM Fundamentals" - a curated list of GitHub repositories for learning prompt engineering and LLM fundamentals[^9].

The repositories are organized into categories:

Fundamentals:
1. dair-ai/Prompt-Engineering-Guide - comprehensive prompt engineering guide
2. promptslab/Awesome-Prompt-Engineering - curated list of prompt engineering resources
3. snwfdhmp/awesome-gpt-prompt-engineering - GPT-focused prompt engineering list

Prompting Techniques and Hands-On:
4. NirDiamant/Prompt_Engineering - prompt engineering techniques
5. brexhq/prompt-engineering - Brex's prompt engineering guide
6. anthropics/prompt-eng-interactive-tutorial - Anthropic's interactive prompt engineering tutorial

Plus a roadmaps section.

## Practical Programming Projects for Beginners

[Post by @vivoplt](https://x.com/vivoplt/status/2029082939921965428): "Don't overcomplicate it" - a list of 8 practical project ideas for learning by building, not following tutorials[^12].

The projects and what they teach:
1. Password Manager - file handling, hashing
2. URL Shortener - routing, IDs, persistence
3. Todo App with deadlines - CRUD, basic state
4. Web Scraper - requests, parsing, rate limits
5. CLI Expense Tracker - logic, files, edge cases
6. Log Analyzer - files, timestamps, patterns
7. Simple Recommender - similarity rules (not ML)
8. Email Automation Script - SMTP, scheduling

Good list of beginner-friendly projects that people can try to learn something new.

## Build Your Own X - 59 Project Ideas

[Post by Abhishek B R (@abhitwt)](https://x.com/abhitwt/status/2029534779272782250): "For people who keep asking what to build" - a comprehensive list of 59 systems programming project ideas[^13].

The projects span multiple domains:
- Operating systems - OS, kernel in assembly, bootloader, scheduler, memory allocator, embedded OS
- Languages and compilers - programming language, compiler, compiler backend (LLVM target), compiler optimizer, scripting language
- Databases and storage - database, query language, key-value store, cache system (like Redis), file system, distributed file system
- Networking - web server, network protocol, networking stack (TCP/IP), API gateway, reverse proxy, load balancer
- DevTools - text editor, IDE, version control system, package manager, shell, debugger, profiler, static code analyzer, disassembler, CI/CD system
- Virtualization and containers - virtual machine, container runtime, container orchestrator (like Kubernetes), hypervisor, microkernel, CPU emulator
- Graphics and audio - game engine, graphics renderer (rasterizer or ray tracer), physics engine, audio engine, GUI toolkit, window manager
- Web and runtime - browser, browser engine (HTML/CSS/JS parser and renderer), runtime (like Node.js), scripting sandbox
- Distributed systems - message broker (like Kafka), search engine
- Security and crypto - encryption algorithm, blockchain, blockchain consensus algorithm, zero-knowledge proof system, authentication server (OAuth2/OpenID Connect)
- AI/ML - machine learning framework
- Database drivers

A good reference list for deeper systems-level learning projects.

## Claude Code Mastery Levels

[Post by David Arnoux](https://www.linkedin.com/feed/update/urn:li:activity:7437793319134498816) (42,800+ followers, GenAI Circle community of 350+ builders): "10 Levels of Claude Code Mastery" framework, claiming most users are stuck at level 2. The levels range from basic prompting (level 0) to autonomous loops with agents building agents (level 10). The post got 1,468 reactions and 1,406 comments[^15].

The levels cover: basic prompting, CLAUDE.md files, MCP servers, custom skills, context engineering with memory files, multi-phase skills and subagents, headless mode with JSON piping, Playwright browser control, parallel sessions with orchestrator agents, cron jobs with background agents, and autonomous agent loops[^15].

They also built a `/level-up` tool that scans your Claude Code environment and gives a personalized roadmap. The post uses engagement-bait (comments required to access the resource)[^15].

These levels are not great - we can come up with something more interesting as content[^16].

David Arnoux runs GenAI Circle, a competitor AI community. Worth following to see what they do[^15].

## Sources

[^1]: [20260207_143150_AlexeyDTC_msg1103.md](../inbox/used/20260207_143150_AlexeyDTC_msg1103.md) - 10 AI projects post
[^2]: [20260207_143229_AlexeyDTC_msg1104.md](../inbox/used/20260207_143229_AlexeyDTC_msg1104.md) - LLM Engineering Roadmap
[^3]: [20260207_143658_AlexeyDTC_msg1105_transcript.txt](../inbox/used/20260207_143658_AlexeyDTC_msg1105_transcript.txt) - Create social post ideas article
[^4]: [20260207_143709_AlexeyDTC_msg1106_transcript.txt](../inbox/used/20260207_143709_AlexeyDTC_msg1106_transcript.txt) - Put in ideas like resources article
[^5]: [20260208_155633_AlexeyDTC_msg1224.md](../inbox/used/20260208_155633_AlexeyDTC_msg1224.md) - Paul Iusztin LinkedIn post on learning AI engineering
[^6]: [20260209_101213_AlexeyDTC_msg1226.md](../inbox/used/20260209_101213_AlexeyDTC_msg1226.md) - Paul Iusztin X post on AI evals
[^7]: [20260209_101233_AlexeyDTC_msg1228.md](../inbox/used/20260209_101233_AlexeyDTC_msg1228.md) - Additional reference to LinkedIn post
[^8]: [20260216_183357_AlexeyDTC_msg1801_transcript.txt](../inbox/used/20260216_183357_AlexeyDTC_msg1801_transcript.txt) - Post ideas from AI engineer webinar Q&A
[^9]: [20260217_211618_AlexeyDTC_msg1923.md](../inbox/used/20260217_211618_AlexeyDTC_msg1923.md) - GitHub resources for prompting/LLM fundamentals
[^10]: [20260219_121518_AlexeyDTC_msg2064_transcript.txt](../inbox/used/20260219_121518_AlexeyDTC_msg2064_transcript.txt) - Portfolio project post idea
[^11]: [20260219_121518_AlexeyDTC_msg2065_transcript.txt](../inbox/used/20260219_121518_AlexeyDTC_msg2065_transcript.txt) - Office hours FAQ analysis idea
[^12]: [20260305_080533_AlexeyDTC_msg2718.md](../inbox/used/20260305_080533_AlexeyDTC_msg2718.md) - Practical programming projects post
[^13]: [20260305_201330_AlexeyDTC_msg2774.md](../../inbox/used/20260305_201330_AlexeyDTC_msg2774.md) - Build your own X post
[^14]: [20260308_162743_AlexeyDTC_msg2778.md](../../inbox/used/20260308_162743_AlexeyDTC_msg2778.md) - 10 AI projects post (duplicate of [^1])
[^15]: [20260312_152230_AlexeyDTC_msg2880.md](../../inbox/used/20260312_152230_AlexeyDTC_msg2880.md) - Claude Code mastery levels LinkedIn post
[^16]: [20260312_152330_AlexeyDTC_msg2882_transcript.txt](../../inbox/used/20260312_152330_AlexeyDTC_msg2882_transcript.txt) - Reaction to levels post
