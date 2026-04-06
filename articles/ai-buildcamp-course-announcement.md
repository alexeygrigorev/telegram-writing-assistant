---
title: "AI Engineering Buildcamp Course Announcement"
created: 2026-04-06
updated: 2026-04-06
tags: [ai-buildcamp, course, announcement]
status: draft
---

# AI Engineering Buildcamp Course Announcement

Course page: [AI Engineering Buildcamp: From RAG to Agents](https://maven.com/alexey-grigorev/from-rag-to-agents)

This is a hands-on course where students spend most of their time building[^1]. By the end, they have a collection of projects for their portfolio. The course runs for about 9 weeks, and every week students work on their capstone project, adding new capabilities as they learn them. Each homework assignment is also a separate project, so students build many different agents throughout the course[^3].

## Course Syllabus

The course takes students from core AI concepts to production-grade AI systems[^2].

### Week 1: LLMs and RAG

Foundation module covering Large Language Models and Retrieval-Augmented Generation. Students build a Documentation Agent that can search technical documentation and answer questions about a project. The module covers the OpenAI API, the RAG pattern, document chunking, and indexing with minsearch. There is also a section on OpenAI alternatives: Groq, Anthropic, AWS Bedrock, Gemini, and Ollama.

### Week 2: RAG Use Cases and Technologies

This week covers practical RAG applications through several projects:

- FAQ Assistant - a chatbot for course FAQ data using RAG with boosting and filtering
- YouTube Transcripts - extracting summaries with timecoded chapters and building RAG systems for chatting with video content
- Structured Extraction from PDFs - extracting data from books by converting PDF pages to images and using LLMs with structured output
- Text Search with Elasticsearch
- Vector Search with Qdrant

### Week 3: AI Agents

Students learn why agents are needed beyond RAG. The module covers tool calling, agent frameworks (PydanticAI, OpenAI Agents SDK, LangChain, Google ADK), web research agents, and Model Context Protocol (MCP). Key components covered: the LLM as the brain, instructions, tools, and memory.

### Week 4: Testing and Multi-Agent Systems

Two big topics. First, testing for agents: writing tests, testing tool calls, using LLM judges to evaluate agent quality, and coming up with test cases. Second, multi-agent systems: routing patterns, pipeline patterns, feedback loops, parallelization, orchestrator-workers, and multi-agent collaboration.

### Week 5: Monitoring and Observability

Adding observability to AI applications using Pydantic Logfire, OpenTelemetry, Jaeger, and Grafana. Students also build DIY logging and monitoring with SQLite and Streamlit dashboards. Other platforms covered: Evidently and LangWatch.

### Week 6: Evaluation and Improvement

Offline evaluation for agents, collecting evaluation data, running agents on scenarios, evaluating AI responses, judge alignment, and synthetic evaluation data generation. Students learn to measure quality systematically and improve their agents based on data.

### Weeks 7-8: Project Work and Advanced Use Cases

Students polish their capstone projects. Advanced project examples include building a coding agent from scratch (scaffolding Django apps), a code analysis agent, and a deep research agent with multi-stage search and fact-checking. Bonus use cases: scary stories generator, code explainer, and book writer. Deployment options covered: Streamlit, Render, and AWS.

### Week 9+: Demo and Hackathon

Project demo presentations, peer review, and an optional hackathon for collaborative work on real-world problems.

## Projects

The course has a strong focus on building. Students work on many projects throughout the course[^1][^3].

### Projects Built During Lectures

These are the main projects built step by step during the course materials:

- Documentation Agent - RAG system for searching and answering questions about technical documentation. This is the running example that evolves throughout the first weeks.
- FAQ Assistant - chatbot for DataTalks.Club course FAQs using real data from multiple courses
- YouTube Transcript Summarizer - extracting summaries and chapters from YouTube videos with structured output
- PDF Book Processor - structured extraction from PDF books, handling illustrations, formulas, and complex structures
- Web and YouTube Researcher - agents that search the web and YouTube for information
- Coding Agent - a fully functional coding agent that scaffolds Django apps, essentially building a clone of Lovable.dev but with Django
- Code Analysis Agent - agents that analyze and understand codebases
- Deep Research Agent - multi-stage research with initial broad search, expansion into follow-up queries, deep dives, fact-checking, and article generation

### Bonus Use Cases

- Scary Stories Generator - creating stories from pictures
- Code Explainer - explaining code functionality
- Book Writer - generating structured written content

### Homework Projects

Each homework assignment is a separate project where students build a new agent[^3]:

- Week 1: Document Processing with AI - download books, extract PDF text, chunk documents, build a full RAG pipeline
- Week 3: Wikipedia Agent - implement search and page fetching tools, build an agent using any framework
- Week 4: DuckDB SQL Agent - build an SQL agent querying NYC taxi data, write pytest tests, add LLM judges, track costs
- Week 5: Trivia Quizmaster Agent - build an interactive trivia agent using the Open Trivia Database API, instrument with Logfire
- Week 6: Recipe Assistant Evaluation - design 20+ evaluation scenarios, run batch tests, detect hallucinations

### Capstone Project

Students work on one capstone project throughout the entire course. Each week they add new capabilities based on what they learned[^3]:

1. Week 1 - project ideation and problem definition
2. Week 2 - add RAG with external data
3. Week 3 - add agent tools and capabilities
4. Week 4 - add testing and evaluation
5. Week 5 - add monitoring and observability
6. Week 6 - systematic evaluation
7. Final weeks - polish and deploy

By the end, students have a complete, production-grade AI application with RAG, agent capabilities, testing, monitoring, and evaluation. There are also 50+ project ideas provided for inspiration - from multilingual RAG chatbots to financial portfolio trackers to developer tools.

## Course Details

- Price: $1,799
- Next cohort: April 13 - June 14, 2026
- Live sessions: Mondays 3:00-4:00 PM UTC (8 sessions total)
- Async content and homework: 3-10 hours per week
- 193 lessons total with lifetime access
- Slack community for peer support
- Certificate of completion

## Sources

[^1]: [20260406_072044_AlexeyDTC_msg3217_transcript.txt](../inbox/used/20260406_072044_AlexeyDTC_msg3217_transcript.txt)
[^2]: [20260406_072804_AlexeyDTC_msg3219.md](../inbox/used/20260406_072804_AlexeyDTC_msg3219.md)
[^3]: [20260406_073529_AlexeyDTC_msg3221_transcript.txt](../inbox/used/20260406_073529_AlexeyDTC_msg3221_transcript.txt)
