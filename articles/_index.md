# Articles Index

This file tracks the article collections in this repository. Articles are organized into the most specific matching subfolder.

## Template for New Articles

When adding a new article, include this frontmatter and opening:

    ---
    title: "Article Title"
    created: YYYY-MM-DD
    updated: YYYY-MM-DD
    tags: [tag1, tag2, tag3]
    status: draft|published
    ---

    # Article Title

    Brief description of what this article is about.

Keep the Description column to one short sentence - what the article is about, not an inventory of everything inside it.

## Special Documents

Repository-wide indexes and long-running collections with special underscore-prefixed filenames.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Substack Archive Index](_substack-archive-index.md) | draft | 2026-08-08 | Lookup table of all published Substack posts (title, description, URL), used to insert direct links to things Alexey has already shared |
| [Interesting Resources](_interesting-resources.md) | draft | 2026-07-13 | Curated collection of tools, resources, and project ideas for the newsletter |
| [Weekly Log](_weekly-log.md) | draft | 2026-07-09 | Running log of what was done each week. Topics with their own dedicated article appear as short summaries with links; smaller items stay inline |

## Metadata

Reference documents used by the writing system rather than article drafts.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Substack Writing Style](_meta/substack-writing-style.md) | draft | 2026-07-31 | How the Substack posts are written, distilled from the last 20 of them |

## AI Shipping Labs

Community strategy, platform notes, member research, plans, workshops, and courses.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [AI Shipping Labs Content Plan](ai-shipping-labs/ai-shipping-labs-content-plan.md) | draft | 2026-08-03 | Gap analysis of the current workshop catalog, a repackaging of the existing sessions into six courses, and the next eight workshops to run |
| [Mini-Course Proposal: LLM Wikis as Agent Memory](ai-shipping-labs/content/llm-wikis-agent-memory-mini-course.md) | draft | 2026-07-31 | Vendor-neutral 90-minute mini-course with theory, a reusable wiki skill, two demos, fit boundaries and a two-part publishing plan |
| [AI Shipping Labs Course Ideas](ai-shipping-labs/content/courses.md) | draft | 2026-07-30 | Course and workshop ideas for the community, with the member requests behind them. |
| [AI Shipping Labs Website Feedback (2026-07-13)](ai-shipping-labs/ai-shipping-labs-feedback-2026-07-13.md) | draft | 2026-07-13 | Team member feedback on the AI Shipping Labs website: main page vs Community Overview split, sprint landing pages, free-sample section, Activities page navigation, and the Workshops section |
| [Course Idea: Safely Running Agents Around Production](ai-shipping-labs/content/agent-production-safety-course.md) | draft | 2026-07-03 | Small course on setting up production alongside agents safely - sandbox account and isolated machine, temporary sandbox-only access, moving work to prod via CI/CD with OIDC, and how to do the projects |
| [Community Session Ideas](ai-shipping-labs/content/community-session-ideas.md) | draft | 2026-07-03 | Session ideas from community members: memory layer for AI agents, documenting agent learnings, refactoring AI slop, mock interviews and resume reviews, interview-prep topics, book-reading sprints, system design with an AI interviewer, pitch practice, mastermind format |
| [Workshop and Course Ideas from Member Plans](ai-shipping-labs/workshop-and-course-ideas-from-member-plans.md) | draft | 2026-06-25 | Member-data-grounded synthesis of AI Shipping Labs blockers, 10 workshop ideas, and 3 five-day mini-course ideas mapped to personas |
| [Workshop Ideas: Agent Durability and Caching Internals](ai-shipping-labs/content/agent-durability-caching-workshops.md) | draft | 2026-06-17 | Two interview-driven workshop ideas: agent durability/idempotency/resumption (LangGraph, Pydantic AI) and caching internals (KV cache) |
| [AI Shipping Labs Community Activities](ai-shipping-labs/activities.md) | draft | 2026-05-21 | Community activities, accountability formats, mentoring, office hours, and sprint calls. |
| [Community Observations](ai-shipping-labs/community-observations.md) | draft | 2026-04-24 | Cross-member patterns: perfectionism / needing to understand everything, no clear picture of the role, idea for a Lightning Lesson on the depth of skills needed |
| [AI Shipping Labs Marketing and Content Strategy](ai-shipping-labs/marketing-and-content.md) | draft | 2026-04-24 | Marketing channels, funnel, lead magnets, and content strategy for the community. |
| [User Interviews](ai-shipping-labs/user-interviews.md) | draft | 2026-04-20 | Overview of the AI Shipping Labs member interview effort and its findings. |
| [Community Platform Feature Ideas](ai-shipping-labs/platform-ideas.md) | draft | 2026-04-07 | Feature ideas and product notes for the AI Shipping Labs platform. |
| [AI Shipping Labs - Target Personas](ai-shipping-labs/personas.md) | draft | 2026-03-21 | Target personas used to understand and support AI Shipping Labs members. |
| [Python Primer Course Idea](ai-shipping-labs/content/python-primer-course-idea.md) | draft | 2026-03-05 | Paid Python prerequisite course for AI Engineering and Zoomcamps - "Python for AI Engineering" with podcast aggregator project |
| [Multi-Agent Patterns for the Course](ai-shipping-labs/content/multi-agent-patterns-course.md) | draft | 2026-02-22 | Multi-agent patterns for the AI Buildcamp course module: evaluation, subagent, planner-executor, orchestration |
| [AI-Assisted Automation Course Idea](ai-shipping-labs/content/ai-assisted-automation-course-idea.md) | draft | 2026-01-29 | Concept for a paid course on AI-assisted automation |
| [Testing Workshop Idea](ai-shipping-labs/content/testing-workshop-idea.md) | draft | - | Workshop idea covering practical software testing foundations. |
| [AI Shipping Labs User Interviews](ai-shipping-labs/interviews/_index.md) | draft | - | Index of individual AI Shipping Labs member interviews and persona assignments. |
| [AI Shipping Labs Personalized Plans](ai-shipping-labs/plans/_index.md) | draft | - | Index of personalized learning and sprint plans for AI Shipping Labs members. |

## DataTalks.Club

DataTalks.Club platform, event, publishing, and product-planning material.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [DataTalks.Club Unified Platform](datatalksclub/datatalks-club-unified-platform.md) | draft | 2026-08-11 | Planning document for consolidating DataTalks.Club's fragmented surfaces (course repos, docs, FAQ, course management platform) into one unified portal - problem statement, vision, how to approach the redesign, and a map of the current org |
| [Playbooks and Agents for DataTalks.Club Events and Content](datatalksclub/datatalks-club-playbooks-and-agents.md) | draft | 2026-07-20 | Ideas for extending the course promotion playbooks to events and other recurring activities, handing post creation to agents, and replacing the podcast guest back-and-forth with a form |
| [Product Shipping Zoomcamp](datatalksclub/product-shipping-zoomcamp.md) | draft | 2026-07-01 | Concept for an end-to-end product development Zoomcamp - six modules plus midterm and capstone, taking students from idea to a deployed, measured, publicly launched, peer-reviewed product, with build-in-public starting from Module 1 |
| [Publishing Zoomcamp Lessons in Text Form](datatalksclub/zoomcamp-text-course-publishing.md) | draft | 2026-04-30 | Idea to publish each LLM Zoomcamp / DataTalks.Club lesson as a long written conspectus with diagrams (Paul Iusztin's Substack format), to own destination traffic, show page-level stats, and attract more sponsors |

## Marketing

General marketing, distribution, social-content, SEO, and search-visibility material.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Social Post Ideas](marketing/social-post-ideas.md) | draft | 2026-03-12 | Curated social media content ideas and inspiration |
| [Ranking for AI Search: LinkedIn Visibility and AI Overview Tracking](marketing/ai-search-visibility.md) | draft | 2026-03-10 | LinkedIn AI visibility study findings and AI Overview Tracker concept for monitoring brand presence in AI search |

## Raw Articles

Draft articles and talk material whose core substance has already been collected.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Diagram Creator: Declarative SVG and PNG Workflows](raw-articles/diagram-generator.md) | complete | 2026-08-09 | How the deterministic diagram creator turns JSON specifications into editable SVG and PNG diagrams. |
| [Stylint: Enforcing My Writing Style on AI Assistants](raw-articles/stylint.md) | draft | 2026-05-19 | Python linter (github.com/alexeygrigorev/stylint) that codifies writing-style rules as code instead of long markdown style guides, so agents stop skipping them |
| [DataTalks.Club Platform Idea](raw-articles/data-talks-club-platform.md) | draft | 2026-04-27 | Custom DataTalks.Club site with on-site events, registration, summary emails, and course management. Revisit ~September for ML Zoomcamp |
| [Configuring Claude Code](raw-articles/configuring-claude-code.md) | draft | 2026-04-05 | Configuration, aliases, slash commands, skills, safety hooks, disabling bypass permissions, and token usage reduction |
| [Benchmarking SQLiteSearch](raw-articles/benchmarking-sqlitesearch.md) | draft | 2026-02-26 | Benchmarking SQLiteSearch with Simple Wikipedia and vector search benchmarks from Milvus/Zilliz, HNSW and IVF implementations, v0.0.3 release |
| [Testing AI Agents with the Judge Pattern](raw-articles/testing-agents-with-judge-pattern.md) | draft | 2026-02-25 | Using agents to evaluate other agents |
| [Course Material Preparation](raw-articles/course-material-preparation.md) | draft | 2026-02-25 | Workflow for keeping code and documentation in sync |
| [Coding Agent Building Blocks: Reusable Skills and Specialized Subagents](raw-articles/code-agents-building-blocks.md) | draft | 2026-02-18 | Article about making coding agents more reliable with reusable skills and specialized subagents. |
| [AI as Personal Analyst](raw-articles/ai-as-personal-analyst.md) | draft | 2026-02-12 | Talk about using AI for Excel automation, data cleaning, and scaling document review |
| [Streaming JSON Parsing with jaxn](raw-articles/jaxn-streaming-json.md) | draft | 2026-01-29 | Streaming parser for LLM structured output |
| [Course Management Agent](raw-articles/course-management-agent.md) | draft | 2026-01-23 | Automating course administration tasks with Claude Skills |

## Work in Progress

Unfinished articles that still need information, experimentation, or testing.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Interview Experiment](work-in-progress/interview-experiment.md) | draft | 2026-08-11 | Running log of the experiment of interviewing at different companies, starting with the first interview at Deriv |
| [AI Engineer Role Survey](work-in-progress/ai-engineer-role-survey.md) | draft | 2026-02-22 | Survey collecting first-hand accounts from AI Engineer practitioners about their roles, tools, and interview experiences |
| [Hetzner Server Setup](work-in-progress/hetzner-server-setup.md) | draft | 2026-02-21 | Setting up a dedicated Hetzner server for running bots, AI workloads, and development environments |
| [Services Website Testimonials](work-in-progress/services-testimonials.md) | draft | 2026-02-15 | Collection of testimonials for the services website |
| [AI Engineer RPG Game](work-in-progress/ai-engineer-rpg-game.md) | draft | 2026-02-13 | RPG game for interview practice built with OpenCode/GLM-5 in Rust |

## Ideas

Recorded content, project, and workflow ideas for later development.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Opik Customer Story: Evaluating and Improving the DataTalks.Club FAQ Assistant](ideas/content/faq-assistant-opik-customer-story.md) | draft | 2026-07-31 | Proposal and future Substack placeholder for adding Opik traces, test suites and prompt optimization to the production FAQ assistant |
| [Coming Up with Project Ideas](ideas/coming-up-with-project-ideas.md) | draft | 2026-04-23 | How to pick portfolio projects: three project types, cap-the-time rule, a portfolio-workflow flowchart, Buildcamp demo-day examples, and Alexey's own pet-project write-ups |
| [Project Approach Reference Doc](ideas/project-approach-reference-doc.md) | draft | 2026-04-22 | Reusable doc for "take my project to production" requests from AI Shipping Labs members - pick one project, describe current + target state, ship end-to-end, metrics from business goals |
| [Personal Project Ideas](ideas/projects/personal-project-ideas.md) | draft | 2026-03-02 | Personal project ideas to implement: voice-based document editing, notebook server for Claude Code, voice-controlled dev bot, DataTasks, content reuse system |
| [Pet Projects](ideas/projects/pet-projects.md) | draft | 2026-02-28 | Karpathy's advice on becoming an expert through depth-first projects, teaching, and self-comparison |
| [AI Agent Project Ideas](ideas/projects/agent-project-ideas.md) | draft | 2026-02-26 | Collection of AI agent project ideas for AI Buildcamp students: GitHub issue bot, idea generator, job analytics, knowledge management, journaling |

## Testimonials

Testimonial collections grouped by program.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [AI Engineering Buildcamp Testimonials](testimonials/ai-buildcamp-testimonials.md) | draft | 2026-06-19 | Collected testimonials from AI Engineering Buildcamp participants |
| [AI Dev Tools Zoomcamp Testimonials](testimonials/ai-dev-tools-zoomcamp-testimonials.md) | draft | 2026-05-02 | Testimonials from AI Dev Tools Zoomcamp participants: Carina Ye on finding the course while job-hunting and going on to ship her first iOS app (Prana: Breathwork Meditation) |
| [Data Engineering Zoomcamp Testimonials](testimonials/data-engineering-zoomcamp-testimonials.md) | draft | 2026-04-30 | Collected DE Zoomcamp testimonials in one place: anonymous "new neural pathways" thank-you, Freeman Onah on the clear course structure, Evgeniia on Spark/Flink/Kestra modules and the overall experience |

## Claw Drafts

Articles drafted by Clo from topic research and voice templates.

| Title | Status | Last Updated | Description |
|-------|--------|--------------|-------------|
| [Prompt Engineering Is Dead. Long Live Context Engineering.](claw-drafts/context-engineering.md) | draft | 2026-07-24 | Strategic Essay + Framework (~2,000 words). Prompt engineering evolved into context engineering with 1M-token windows. Four-layer framework: Selection, Ordering, Compression, Eviction |

## Research

See [Research Articles](research/_index.md) for the current research and investigation topics.

## Workflow

1. Store each Markdown article in the most specific matching subfolder.
2. Route all AI Shipping Labs material under articles/ai-shipping-labs/; use its content/, plans/, and interviews/ subfolders where appropriate.
3. Put general marketing and distribution material in articles/marketing/.
4. Keep special repository documents underscore-prefixed and metadata in articles/_meta/.
5. Search all subfolders before creating a new article, then update this index and any applicable child index.
6. The Telegram bot collects new materials in inbox/raw/; use /process to turn them into article updates.
