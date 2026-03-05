---
title: "Weekly Log"
created: 2026-02-26
updated: 2026-03-05
tags: [weekly, log]
status: draft
---

# Weekly Log

A running log of what was done each week. When a topic has its own detailed article, this log contains a short summary with a link. When there is not much content for a topic, the details go here directly.

## Week of 2026-03-03

AI Buildcamp course - monitoring module: finished the DIY Monitoring Platform section, which was slightly behind schedule. Changed the approach from the previous cohort - Pydantic LogFire is now the main focus because it is very simple to integrate. The DIY Monitoring Platform is now an optional section. Getting data out of LogFire is not as straightforward as it could be, but covered how to do that for students. Incorporated all the feedback from the previous cohort[^16][^17].

AI Engineering Field Guide - webinar and curation: prepared for and ran the Tuesday webinar on AI Engineering job search. The title was "AI Engineer in Berlin, London, Amsterdam, New York, and Los Angeles." For February, added India as a whole country, making 6 geographies total. Considering expanding Berlin to all of Germany in the future. After all deduplication, there are now over 1,600 job listings in the Field Guide. Analyzed over 700 different sources - reports, social media posts (Twitter, Reddit), YouTube videos. Extracted a large number of interview questions from these sources, then curated the most relevant ones. Prioritized questions that had real support from people in social media confirming they were actually asked in interviews. Avoided SEO-optimized sites that may have just used ChatGPT to generate question lists without real research behind them. Removed trivial encyclopedic questions as useless and focused on meaningful questions that demonstrate real understanding. A lot of work went into categorizing, filtering, and curating all of this. The webinar is now available. The GitHub repository is AI Engineering Field Guide - asking people to star it and share it on social media. Could create a template for how people can promote this repository[^16][^17].

Apache Flink workshop: ran a workshop on Wednesday about Apache Flink for Data Engineering Zoomcamp. The original content was created by Zac Wilson, who did a Flink stream last year. Updated and reworked the material. The code was already ready, so restructured it step by step in the usual teaching style - explaining things incrementally, showing what order to launch things in, how Flink works, how to configure it. Explained Zac's example and then covered another example about aggregation with watermarks and bolt windows in Flink. About 80-90% of the content is based on Zac's original material, updated to the latest versions - Flink 2.x and Python 3.12/3.8/3.9. A lot of testing was needed to make sure everything worked. Claude Code helped but required a lot of guidance. The workshop went very well on Wednesday. Since this is not a primary area of expertise (not a practicing data engineer), relied fully on Zac's content, which is solid since Zac is a Flink specialist. Could not have answered deep Data Engineering or Flink usage questions, but no such questions came up[^17].

Python for AI Engineering course: started preparing a Python course for the AI Engineering community. Asked Claude Code to analyze all existing courses - ML Zoomcamp, Data Engineering Zoomcamp, MLOps Zoomcamp, LLM Ops Zoomcamp, AI Engineering Buildcamp, and AI Hero course. Did not include AI DevTools Zoomcamp because code there is generated, not written by hand. Used Claude Code instead of doing it manually to avoid missing things and because as an experienced Python developer, some things might seem obvious but are not for beginners. The approach assumes zero Python knowledge. The analysis produced a very good list of required Python topics. Based on this list, came up with a project - the course will use a project-based approach (same methodology as all the Zoomcamps). The project is a podcast aggregator, covering everything from Python basics to advanced topics like database interaction, multithreading, and async. Async is included because AI Engineering Buildcamp uses Pydantic AI which is async-based. The curriculum is not fully finalized yet - no time right now because of Buildcamp. Doing this as background work - switching to it between recording sessions, brainstorming in ChatGPT during breaks. The course name will be "Python for AI Engineering" (tentative). The goal: after completing this course, students can take any Zoomcamp and the AI Engineering course with the right Python foundation. See [Python Primer Course Idea](ideas/python-primer-course-idea.md) for the full concept[^18].

AI Engineering Buildcamp - remaining work: still need to finish a couple of remaining sections for AI Engineering Buildcamp this week[^19].

Exasol in-person meetup preparation: preparing for an in-person meetup on Tuesday about Exasol. Found a large dataset - NHS Prescription Data with over 1 million records - about prescriptions issued to people in the UK. Plan to demonstrate: how to collect and ingest this data, set up a staging environment, build a ready-to-use data warehouse for analytics, create a Grafana dashboard for analytics, and orchestrate everything with Kestra. Working with someone from Exasol on this. Content was prepared about a month ago, now needs polishing and rehearsal. Still need to figure out how to give access to Exasol for attendees who come without their own AWS account - the assumption is people bring their own AWS account to deploy the database, but not everyone will have one. Also handling logistics like food. If you are in Berlin and want to learn about data ingestion and fast analytics, come to the meetup[^19].

## Week of 2026-02-24

Telegram Writing Assistant: added YouTube transcript processing and external audio file support. The bot can now accept audio files recorded outside of Telegram and process them through the same Whisper transcription pipeline. YouTube URL processing also works now. See [What's New in the Telegram Writing Assistant](ready-for-newsletter/telegram-writing-assistant-updates.md) for details[^1][^2].

PNG to SVG conversion: spent time converting a ChatGPT-generated PNG logo into SVG using Claude Code with OpenCV. Went through multiple approaches before finding one that works. See [Recreating a PNG Logo as SVG with Claude Code](svg-logo-recreation.md) for the full story[^3].

Community platform: tested features on the AI Shipping Labs site - set up OAuth tokens for Gmail and GitHub, got Zoom integration working with a one-click meeting creation button, reviewed the admin panel and user dashboard. Created logo with ChatGPT and attempted SVG recreation. All integrations (Gmail, GitHub, Zoom, Slack, Stripe) are now connected. See [Building a Community Platform with Claude Code's Multi-Agent System](work-in-progress/community-platform-implementation.md) for details[^4][^5][^6].

AI Engineer webinar session 2: ran the second "Defining the Role of AI Engineer" session with 200 attendees. Presented data-driven analysis of 895 job descriptions - RAG is the top skill, 93% of roles need more than just GenAI, Python dominates at 82.5%. Answered live Q&A. See [Defining the Role of AI Engineer: Webinar Q&A](ai-engineer-role-definition-qa.md)[^7].

Testing agents: added a workflow for generating tests from usage sessions - record yourself using the agent on video, transcribe with Whisper, feed to ChatGPT to generate test scenarios. Also gave students a homework assignment to test an SQL analytics agent. See [Testing AI Agents with the Judge Pattern](ready-for-newsletter/testing-agents-with-judge-pattern.md)[^8].

SQLiteSearch benchmarking: continued benchmarking, hit scaling issues with vector search on 1 million records. The LSH approach breaks at that scale. Claude suggested HNSW, started implementing it. See [Benchmarking SQLiteSearch](ready-for-newsletter/benchmarking-sqlitesearch.md)[^9].

Course materials: working on the monitoring module for AI Buildcamp. Using Langfuse with Pydantic AI integration. Expanded the monitoring content from the previous cohort. Planning to re-record the DIY self-monitoring part with Grafana. See [Course Material Preparation](ready-for-newsletter/course-material-preparation.md)[^10].

DataTasks: started implementing the task management app using Claude Code (Opus 4.6). Reused an existing repo. Claude Code followed the PROCESS.md workflow - grooming issues first, then implementing in batches of 2 with parallel PM agents. See [Task Management App Idea](ideas/task-management-app-idea.md)[^11].

AI agent project ideas: started collecting project ideas for AI Buildcamp students. Ideas include a GitHub issue creator bot, project idea generator agent, problem discovery framework, job market analytics agent, knowledge management bot, and journaling agent. See [AI Agent Project Ideas](agent-project-ideas.md)[^12].

Community platform features: started a new article for feature ideas for the AI Shipping Labs site. Includes a business case simulator inspired by Karpov.Courses, career help and job search tools, and data collection strategy. See [Community Platform Feature Ideas](community-platform-features.md)[^13].

SQLiteSearch v0.0.3 released: published version 0.0.3 to PyPI with HNSW and IVF implementations. HNSW is the best performer at 6ms query speed on 1M vectors. Recommended for up to 100K items. See [Benchmarking SQLiteSearch](ready-for-newsletter/benchmarking-sqlitesearch.md)[^14].

Production incident: accidentally destroyed the course management platform production database via Terraform destroy. The agent ran terraform destroy with auto-approve, wiping the entire production infrastructure including VPC, RDS, ECS, and load balancers. Backups were deleted along with the database. Upgraded to AWS Business support, got on a call with support at 2 AM. Still waiting for data recovery. Implemented multiple preventive measures: backups outside Terraform state, S3 backups, automated daily Lambda/Step Functions backup pipeline, deletion protection flags, and migrated Terraform state to S3. See [Course Management Production Incident Report](course-management-production-incident.md)[^15].

## Sources

[^1]: [20260226_071301_AlexeyDTC_msg2486_transcript.txt](../inbox/used/20260226_071301_AlexeyDTC_msg2486_transcript.txt)
[^2]: [20260226_071213_AlexeyDTC_msg2484_transcript.txt](../inbox/used/20260226_071213_AlexeyDTC_msg2484_transcript.txt)
[^3]: [20260226_065034_AlexeyDTC_msg2477_transcript.txt](../inbox/used/20260226_065034_AlexeyDTC_msg2477_transcript.txt)
[^4]: [20260225_163430_AlexeyDTC_msg2408_transcript.txt](../inbox/used/20260225_163430_AlexeyDTC_msg2408_transcript.txt)
[^5]: [20260225_201000_AlexeyDTC_msg2445_transcript.txt](../inbox/used/20260225_201000_AlexeyDTC_msg2445_transcript.txt)
[^6]: [20260225_201916_AlexeyDTC_msg2449_transcript.txt](../inbox/used/20260225_201916_AlexeyDTC_msg2449_transcript.txt)
[^7]: [20260224_175508_AlexeyDTC_msg2256_transcript.txt](../inbox/used/20260224_175508_AlexeyDTC_msg2256_transcript.txt)
[^8]: [20260225_200726_AlexeyDTC_msg2441_transcript.txt](../inbox/used/20260225_200726_AlexeyDTC_msg2441_transcript.txt)
[^9]: [20260225_201829_AlexeyDTC_msg2447_transcript.txt](../inbox/used/20260225_201829_AlexeyDTC_msg2447_transcript.txt)
[^10]: [20260225_200842_AlexeyDTC_msg2443_transcript.txt](../inbox/used/20260225_200842_AlexeyDTC_msg2443_transcript.txt)
[^11]: [20260223_192235_AlexeyDTC_msg2226_transcript.txt](../inbox/used/20260223_192235_AlexeyDTC_msg2226_transcript.txt)
[^12]: [20260226_112322_AlexeyDTC_msg2498_transcript.txt](../inbox/used/20260226_112322_AlexeyDTC_msg2498_transcript.txt)
[^13]: [20260226_113315_AlexeyDTC_msg2512_transcript.txt](../inbox/used/20260226_113315_AlexeyDTC_msg2512_transcript.txt)
[^14]: [20260226_134356_AlexeyDTC_msg2534_transcript.txt](../inbox/used/20260226_134356_AlexeyDTC_msg2534_transcript.txt)
[^15]: [20260227_073053_AlexeyDTC_msg2546_transcript.txt](../inbox/used/20260227_073053_AlexeyDTC_msg2546_transcript.txt)
[^16]: [20260305_094927_AlexeyDTC_msg2724_transcript.txt](../inbox/used/20260305_094927_AlexeyDTC_msg2724_transcript.txt)
[^17]: [20260305_095356_AlexeyDTC_msg2726_transcript.txt](../inbox/used/20260305_095356_AlexeyDTC_msg2726_transcript.txt)
[^18]: [20260305_095937_AlexeyDTC_msg2728_transcript.txt](../inbox/used/20260305_095937_AlexeyDTC_msg2728_transcript.txt)
[^19]: [20260305_100309_AlexeyDTC_msg2730_transcript.txt](../inbox/used/20260305_100309_AlexeyDTC_msg2730_transcript.txt)
