# Articles Index

This file tracks all articles in this repository. Articles are organized into subfolders by category.

## Template for New Articles

When adding a new article, include:

```markdown
---
title: "Article Title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2, tag3]
status: draft|published
---

# Article Title

Brief description of what this article is about.
```

## Ready for Newsletter

Articles that are mostly ready for the newsletter. All necessary content is inside, may need final review or light editing.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Claude Code Experiments](ready-for-newsletter/claude-code-experiments.md) | draft | 2026-04-28 | Experiments and applications of Claude Code beyond coding, including challenges with communication; added new running-agents view in the Claude Code UI |
| [FAQ System for Course Management](ready-for-newsletter/faq-system.md) | draft | 2026-04-23 | Community-driven FAQ with RAG-based automation, Google Docs era, Alex Litvinov's Slack bot stack, custom Copilot-built static site generator, GPT-4o cleanup script, FAQ Automation Bot with Mermaid workflow, Claude Code PR review, illustration placeholders added |
| [Configuring Claude Code](ready-for-newsletter/configuring-claude-code.md) | draft | 2026-04-05 | Configuration, aliases, slash commands, skills, safety hooks, disabling bypass permissions, and token usage reduction |
| [OpenCode Experiments with GLM-5](ready-for-newsletter/opencode-experiments.md) | draft | 2026-03-19 | Trying OpenCode AI assistant with GLM-5 model, extracting JS from Claude binary, Claude Code flickering comparison |
| [What's New in the Telegram Writing Assistant](ready-for-newsletter/telegram-writing-assistant-updates.md) | draft | 2026-03-14 | Article idea: subagents, research section, link summaries, QA agent, YouTube and audio file processing |
| [Cross-Platform Environment Variable Management with dirdotenv](ready-for-newsletter/dirdotenv.md) | draft | 2026-03-13 | Python-based alternative to direnv, first Claude Code experiment |
| [Microphone Booster App](ready-for-newsletter/microphone-booster-app.md) | draft | 2026-03-12 | Windows microphone booster built with OpenCode/GLM-5 using Tauri + Rust, compilation on new Windows machine with Claude Code |
| [Benchmarking SQLiteSearch](ready-for-newsletter/benchmarking-sqlitesearch.md) | draft | 2026-02-26 | Benchmarking SQLiteSearch with Simple Wikipedia and vector search benchmarks from Milvus/Zilliz, HNSW and IVF implementations, v0.0.3 release |
| [Testing AI Agents with the Judge Pattern](ready-for-newsletter/testing-agents-with-judge-pattern.md) | draft | 2026-02-25 | Using agents to evaluate other agents |
| [Course Material Preparation](ready-for-newsletter/course-material-preparation.md) | draft | 2026-02-25 | Workflow for keeping code and documentation in sync |
| [SSH Auto Forward: Automatic Port Forwarding Tool](ready-for-newsletter/ssh-auto-forward.md) | draft | 2026-02-21 | Automatic SSH port forwarding tool built with Claude Code for remote development workflow, now published on GitHub and PyPI |
| [Certificates and AI Design Experiments](ready-for-newsletter/certificates-and-ai-design-experiments.md) | draft | 2026-02-16 | Creating workshop certificates and experiments with image-to-HTML/CSS conversion |
| [Nobook: Plain Python Files as Jupyter Notebooks](ready-for-newsletter/nobook.md) | draft | 2026-02-13 | Tool that uses plain .py files as Jupyter notebooks instead of .ipynb JSON |
| [Minsearch Benchmarking and Optimization](ready-for-newsletter/minsearch-benchmarking-optimization.md) | draft | 2026-02-09 | Optimizing the appendable index through iterative benchmarking |
| [Course Management Agent](ready-for-newsletter/course-management-agent.md) | draft | 2026-01-23 | Automating course administration tasks with Claude Skills |
| [Generating Books with AI](ready-for-newsletter/ai-book-generator.md) | draft | 2026-01-23 | Using AI to generate complete books with covers |
| [Minsearch: Simple Search for Small Datasets](ready-for-newsletter/minsearch-library.md) | draft | 2026-01-23 | Lightweight search library for small databases |
| [Streaming JSON Parsing with jaxn](ready-for-newsletter/jaxn-streaming-json.md) | draft | 2026-01-23 | Streaming parser for LLM structured output |

## AI Shipping Labs

Articles about the AI Shipping Labs paid community: vision, activities, courses, marketing, platform.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Personalised Plans](ai-shipping-labs/plans/_index.md) | draft | 2026-05-06 | Three new plans (Manjunath Yelipeta - traditional ML engineer pivoting to AI/AI Platform, ship deployed RAG with evaluation; Daniel Sa Earp - Brazilian analytics engineer prepping for June LLM Zoomcamp, build GitHub-issues ingestion pipeline; Valeriia Kuka - non-programmer team member, complete AI Hero) and Luca's plan updated with structured Q&A from his intake doc + follow-up notes (20 hr/week, framework leaning is pydantic-ai or smolagents) |
| [Activities](ai-shipping-labs/activities.md) | draft | 2026-04-30 | Regular sessions, accountability circles, mentoring, career development, knowledge sharing, member onboarding, Office Hours tied to LLM Zoomcamp, group course study in autumn, sprint weekly call format (status update with what-I-did/blockers/plans, week-1 intros, last-week demo, async via Slack) |
| [Individual Interviews](ai-shipping-labs/interviews/_index.md) | draft | 2026-04-29 | One file per participant with persona assignment: Koray Can Canut, Juan Perez Prim, Daniel Ibáñez, Jakob Zischka, Vancesca Dinh, Brad Smith, Leonor, and others |
| [Course Ideas](ai-shipping-labs/courses.md) | draft | 2026-04-27 | Spec-Driven Dev, Refactoring AI Slop, Python, Data Engineering, CloudCode, testing, DevOps, DDD module, Build Docker from scratch workshop |
| [Marketing and Content Strategy](ai-shipping-labs/marketing-and-content.md) | draft | 2026-04-24 | Marketing channels, funnel, lead magnets, content strategy, Lenny's inspiration, Paul Iusztin's Decoding AI newsletter as a model for naturally slotting course ads into free-newsletter content, overview articles that funnel into the community by keeping specifics (GitHub template, prompts, workshops, workflows) inside AI Shipping Labs |
| [Community Observations](ai-shipping-labs/community-observations.md) | draft | 2026-04-24 | Cross-member patterns: perfectionism / needing to understand everything, no clear picture of the role, idea for a Lightning Lesson on the depth of skills needed |
| [User Interviews (overview)](ai-shipping-labs/user-interviews.md) | draft | 2026-04-20 | Overview of the user interview effort, outreach status, and plan tracking. Individual interviews live in interviews/ folder |
| [How We Built AI Shipping Labs](ai-shipping-labs/how-we-built-it.md) | draft | 2026-04-07 | Valeriia's V0 website build story, MVP philosophy, hosting journey, agent-built Django platform |
| [Launch Announcement](ai-shipping-labs/launch-announcement.md) | draft | 2026-04-07 | Newsletter article: community announcement, activities, tiers, early member benefits |
| [Platform Ideas](ai-shipping-labs/platform-ideas.md) | draft | 2026-04-07 | Business case simulator, career help tools, data collection, cross-linking tools/concepts |
| [Vision](ai-shipping-labs/vision.md) | draft | 2026-03-20 | Vision, target audience, tier structure, pricing, design principles, next steps |
| [Building the Platform with Claude Code](ai-shipping-labs/platform-implementation.md) | draft | 2026-02-25 | Multi-agent build experiment: Product Manager, Software Engineer, Tester, On-Call Engineer |

## Work in Progress

Unfinished articles that need more information, experimentation, or testing before they are ready for the newsletter.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [AI Engineer Role Survey](work-in-progress/ai-engineer-role-survey.md) | draft | 2026-02-22 | Survey collecting first-hand accounts from AI Engineer practitioners about their roles, tools, and interview experiences |
| [AI Engineer Role Research](work-in-progress/ai-engineer-role-research.md) | draft | 2026-02-19 | Research into AI Engineer positions and interview process |
| [Services Website Testimonials](work-in-progress/services-testimonials.md) | draft | 2026-02-15 | Collection of testimonials for the services website |
| [AI Engineer RPG Game](work-in-progress/ai-engineer-rpg-game.md) | draft | 2026-02-13 | RPG game for interview practice built with OpenCode/GLM-5 in Rust |
| [Hetzner Server Setup](work-in-progress/hetzner-server-setup.md) | draft | 2026-02-21 | Setting up a dedicated Hetzner server for running bots, AI workloads, and development environments |
| [From Vague Ideas to Concrete Results with ChatGPT](work-in-progress/idea-to-concrete-iteration.md) | draft | 2026-01-31 | Process for iterating from undefined ideas to actionable plans |

## Ideas

Recorded ideas without much detail. Just the idea itself, useful for not forgetting and reviewing later.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [DataTalks.Club Platform Idea](ideas/data-talks-club-platform.md) | draft | 2026-04-27 | Idea to build (or copy AI Shipping Labs' platform for) a custom DataTalks.Club site with on-site events, registration, follow-up summary emails, calendar, and integrated course management. Revisit in ~3 months, possibly for ML Zoomcamp in September |
| [Project Approach Reference Doc](ideas/project-approach-reference-doc.md) | draft | 2026-04-22 | Reusable doc for "take my project to production" requests from AI Shipping Labs members - pick one project, describe current + target state, ship end-to-end, metrics from business goals |
| [Social Post Ideas](ideas/social-post-ideas.md) | draft | 2026-03-12 | Curated social media content ideas and inspiration |
| [Python Primer Course Idea](ideas/python-primer-course-idea.md) | draft | 2026-03-05 | Paid Python prerequisite course for AI Engineering and Zoomcamps - "Python for AI Engineering" with podcast aggregator project |
| [Task Management App Idea](ideas/task-management-app-idea.md) | draft | 2026-02-24 | Unified task management system combining Trello and todo lists, with serverless AWS implementation (datatasks) |
| [Multi-Agent Patterns for the Course](ideas/multi-agent-patterns-course.md) | draft | 2026-02-22 | Multi-agent patterns for the AI Buildcamp course module: evaluation, subagent, planner-executor, orchestration |
| [Voice-Controlled Development Bot](ideas/voice-controlled-dev-bot.md) | draft | 2026-02-20 | Idea for a general-purpose Telegram bot that executes development commands via voice |
| [AI Hero Course Rebranding for AI Shipping Labs](ideas/ai-hero-rebranding.md) | draft | 2026-02-17 | Rebranding the existing AI Hero course to fit under the new AI Shipping Labs community |
| [AI-Assisted Automation Course Idea](ideas/ai-assisted-automation-course-idea.md) | draft | 2026-01-29 | Concept for a paid course on AI-assisted automation |
| [Google Stitch: Design-First AI Development](ideas/google-stitch.md) | draft | 2026-01-23 | Google's design-focused AI development tool |
| [New Website Services Section](ideas/new-website-services-section.md) | draft | - | Adding a workshops section to the website |
| [Resources and Articles Tracking](ideas/resources-and-articles-tracking.md) | draft | - | Tracking resources and draft articles with a table on GitHub |
| [Testing Workshop Idea](ideas/testing-workshop-idea.md) | draft | - | Workshop idea about testing practices |

## Talks

Notes and preparation materials for upcoming presentations and talks.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Building Blocks of Modern Code Agents](talks/code-agents-building-blocks.md) | draft | 2026-02-18 | Map of code agent types and the two key building blocks: skills and subagents |
| [AI as Personal Analyst](talks/ai-as-personal-analyst.md) | draft | 2026-02-12 | Talk about using AI for Excel automation, data cleaning, and scaling document review |

## Other

Files at the articles root that don't fit into the above categories.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Community Session Ideas](community-session-ideas.md) | draft | 2026-05-06 | Added Carlos Pumar's two ideas for the next freestyle workshop: documenting "learnings" from agent-built projects so they can be reused, and refactoring agent-generated code with named software principles. Existing entries: Sai Kumar G interview-questions / mock-interviews request, "how to pitch your idea" Toastmasters-style session, group-learning/mastermind format, cross-cultural feedback note |
| [Weekly Log](weekly-log.md) | draft | 2026-05-05 | Added Week of 2026-05-04: Data Makers Fest in Porto - Monday Introduction to Agentic RAG workshop (simplified LLM Zoomcamp / RAG modules), interviews on Tuesday for an upcoming podcast episode, panel discussion participation, and moderated session on production LLMs |
| [AI Engineering Buildcamp Cohort 2 - Demo Day](demo-day-cohort-2.md) | draft | 2026-05-02 | Capstone projects from Cohort 2 demo: Edu's bikepacking recommender, Pavlo Skorodziievskyi's family meal-map, Camila's engineering decision memory agent, Mladen Marić's voice-to-issue Telegram bot (with cloud deployment and Presidio PII scrubbing detail), Spyros' offline medical SOAP notes; plus submitted-but-not-presented projects from Nirajan (Cyber Sachet/Nepal), James Watkins (SnapSplit, private repo), Juan Prim (AMR), and Léonore Tideman (AI regulation assistant) |
| [AI Dev Tools Zoomcamp Testimonials](ai-dev-tools-zoomcamp-testimonials.md) | draft | 2026-05-02 | Testimonials from AI Dev Tools Zoomcamp participants: Carina Ye on finding the course while job-hunting and going on to ship her first iOS app (Prana: Breathwork Meditation) |
| [Publishing Zoomcamp Lessons in Text Form](zoomcamp-text-course-publishing.md) | draft | 2026-04-30 | Idea to publish each LLM Zoomcamp / DataTalks.Club lesson as a long written conspectus with diagrams (Paul Iusztin's Substack format), to own destination traffic, show page-level stats, and attract more sponsors |
| [Data Engineering Zoomcamp Testimonials](data-engineering-zoomcamp-testimonials.md) | draft | 2026-04-30 | Collected DE Zoomcamp testimonials in one place: anonymous "new neural pathways" thank-you, Freeman Onah on the clear course structure, Evgeniia on Spark/Flink/Kestra modules and the overall experience |
| [Interesting Resources](interesting-resources.md) | draft | 2026-04-27 | Curated collection of tools, resources, and project ideas for the newsletter: added Tech Debt Audit and Coding Challenges newsletter |
| [OpenClaw Experiments](openclaw-experiments.md) | draft | 2026-04-24 | Testing the OpenClaw bootstrap flow (CLI and Telegram), including WhisperX install, ahead of an AI Shipping Labs group session |
| [Coming Up with Project Ideas](coming-up-with-project-ideas.md) | draft | 2026-04-23 | Reframed as recurring conversation across workshops/AI Shipping Labs/course students, three project types as a list with overlap, cap-the-time general rule with tech-learning combo, mermaid flowchart for portfolio workflow, Buildcamp cohort 1 demo day examples (cybersecurity, client satisfaction, habit builder, email agent), personal projects section with Alexey's Substack write-ups (dirdotenv, ssh-auto-forward, nobook, microboost, bot master, telegram assistant) |
| [Deterministic Coding with Agent Teams](litehive.md) | draft | 2026-04-10 | litehive file-based task manager, tmuxctl, GoZ engine, self-writing system, recovery agent, multiple engines, usage quota tracking, stale agent killing, self-improving tools |
| [AI Engineering Buildcamp Course Announcement](ai-buildcamp-course-announcement.md) | draft | 2026-04-06 | Course announcement: syllabus, projects, homework agents, capstone progression, hands-on focus |
| [AI Engineering Field Guide](ai-engineering-field-guide.md) | draft | 2026-03-27 | Job listing pipeline for AI Engineer roles - scraping, deduplication, LLM enrichment |
| [Trying OpenAI Codex as a Claude Code Alternative](codex-experiments.md) | draft | 2026-03-25 | Trying Codex after hitting Claude Code session limits, agent workflow comparison, no task widget, auto-continue differences, orchestrator idea |
| [Running Local LLMs for Coding on a Hetzner Server](local-llm-experiments.md) | draft | 2026-03-19 | Hitting Claude Code weekly limits, experimenting with quantized Qwen2.5 and DeepSeek on CPU |
| [Building Projects with Agent Teams](building-projects-with-agent-teams.md) | draft | 2026-03-19 | Approach to building complex projects with Claude Code multi-agent teams: AI Shipping Labs, Data Tasks, Pymermade, Jekyll-to-Rust, custom coding agent (Codehive), AI Hero migration, agent management challenges |
| [Zoland Talk](zoland-talk.md) | draft | 2026-03-14 | Talk at Zoland meetup about the Telegram writing assistant, code agents, and slides preparation workflow with Claude Code |
| [Starting Projects with GitHub Copilot](starting-projects-with-github-copilot.md) | draft | 2026-03-13 | Using GitHub Copilot to start projects from the browser, limitations and best workflow with ChatGPT |
| [Exasol Workshop Infrastructure Setup](exasol-workshop-infrastructure.md) | draft | 2026-03-12 | Secure AWS access setup for Exasol workshop using temporary credentials, Lambda, CodeSpaces/DevContainers, credential flow diagram, open-source project |
| [Setting Up a Windows Computer for Development](windows-dev-setup.md) | draft | 2026-03-11 | Step-by-step guide to setting up a fresh Windows computer for development: Terminal, Git Bash, Python/UV, NodeJS, Docker, VS Code, Claude Code |
| [Ranking for AI Search: LinkedIn Visibility and AI Overview Tracking](ai-search-visibility.md) | draft | 2026-03-10 | LinkedIn AI visibility study findings and AI Overview Tracker concept for monitoring brand presence in AI search |
| [Take-Home Assignments for AI Engineers: Webinar Q&A](ai-engineer-webinar-qa.md) | draft | 2026-03-10 | Q&A from webinar on take-home assignments for AI engineers: career advice, hiring without CS degree, data scientist transitions |
| [Google Docs Voice Feedback Tool](google-docs-voice-feedback.md) | draft | 2026-03-02 | Voice-powered Google Docs editor built with Claude Code, using LLM to understand edit requests and apply changes via Google Docs API |
| [Personal Project Ideas](personal-project-ideas.md) | draft | 2026-03-02 | Personal project ideas to implement: voice-based document editing, notebook server for Claude Code, voice-controlled dev bot, DataTasks, content reuse system |
| [Pet Projects](pet-projects.md) | draft | 2026-02-28 | Karpathy's advice on becoming an expert through depth-first projects, teaching, and self-comparison |
| [Getting a Data Science Job](getting-a-data-science-job.md) | draft | 2026-02-28 | Summary of a presentation on the full data science job search process: networking, applying, interviewing, and negotiating offers |
| [AI Agent Project Ideas](agent-project-ideas.md) | draft | 2026-02-26 | Collection of AI agent project ideas for AI Buildcamp students: GitHub issue bot, idea generator, job analytics, knowledge management, journaling |
| [Recreating a PNG Logo as SVG with Claude Code](svg-logo-recreation.md) | draft | 2026-02-26 | Converting a ChatGPT-generated PNG logo to SVG using Claude Code with OpenCV and potrace |
| [Writing Assistant Improvement Ideas](writing-assistant-improvement-ideas.md) | draft | 2026-02-20 | Feedback and improvement ideas for the Telegram writing assistant bot |

## Research

See [Research Articles](research/_index.md) for research and investigation topics.

## How to Use

1. Articles are stored as Markdown files in this directory and its subfolders
2. Each article follows the template above
3. Use this index to track all articles and their status
4. The Telegram bot collects materials in `inbox/raw/`
5. Use `/process` command to commit and push materials
6. New articles are created in `articles/` root by default; manually move to the right subfolder later
