---
title: "AI Bootcamp Course"
created: 2026-01-22
updated: 2026-01-22
tags: [course, ai-bootcamp, curriculum, agents, rag]
status: draft
---

# AI Bootcamp Course

The AI Bootcamp "From RAG to Agents" course is now called "AI Engineering BuildCamp" - a comprehensive 9-week program that takes students from core concepts to production-grade AI systems. The first iteration had 49 participants, and their feedback was incorporated into an updated syllabus[^1].

## Course Renaming

The course is being renamed from "AI Bootcamp" to "AI Engineering BuildCamp". There are many bootcamps in the space (iBootCamp, etc.) and it's hard to stand out. Since the course focus is on Learning by Doing and Building, with many projects as output, "BuildCamp" is a fitting name that emphasizes the building aspect[^2].

The course outline is being redesigned to be more focused. The material remains the same but is now better organized. Posts about the renaming should be made on social media explaining the change, with a Substack article covering the details[^3].

<figure>
  <img src="../assets/images/ai-bootcamp-course/course-folder-structure.jpg" alt="AI Engineering BuildCamp course folder structure">
  <figcaption>Course folder structure showing the organized curriculum layout from v2 materials</figcaption>
  <!-- This illustrates how the course materials are structured and organized -->
</figure>

## Course Structure

The course is redesigned with 90% of materials re-recorded based on prior cohort feedback. It's longer but less dense, and more focused.

### Week 1: LLMs and RAG Foundations

- Course overview and logistics
- Environment preparation with GitHub Codespaces
- AI-assisted development tools (ChatGPT, GitHub Copilot, Codex, Antigravity)
- OpenAI API basics and responses
- RAG (Retrieval-Augmented Generation) introduction
- Building a document assistant with RAG
- Structured output and vector search
- Alternatives to OpenAI (Groq, Anthropic, Gemini, Z.ai)
- Advanced chunking techniques

### Week 2: Buffer Week

This is a buffer week for environment setup, with optional content on other use cases and external databases.

### Week 3: Agents

- Introduction to agents and agentic RAG
- Agent tool-call loop foundation
- Pydantic AI framework
- Multi-agent systems (linear execution, agents as tools)
- Model-Context Protocol (MCP) for tool integration

Several frameworks have been added as optional materials based on numerous student requests:
- LangChain and LangGraph (popular, but PydanticAI remains the primary focus)
- Google ADK (Agent Development Kit)
- CrewAI
- OpenAI Agents SDK

While many students ask for LangChain and LangGraph, and they are among the first frameworks used for RAG and agents, the course focuses primarily on PydanticAI. Other frameworks are included as optional content to accommodate different preferences and backgrounds[^4].

### Week 4: Testing for Agents

- Converting Jupyter notebooks to Python projects
- Writing agent tests
- Tracking usage and costs
- Testing with structured output
- LLM judges for agent testing

### Week 5: Monitoring

- Pydantic Logfire for observability
- OpenTelemetry and Jaeger
- DIY logging and monitoring with Postgres and Streamlit
- Grafana dashboards
- Other observability platforms (Evidently, LangWatch)

### Week 6: Evaluation

- Manual log evaluation
- Synthetic data generation
- Retrieval evaluation
- LLM judges for evaluation
- Prompt optimization with evaluator pattern
- Selecting chunking approaches with evals

### Weeks 7-9: Bonus and Use Cases

- Guardrails (input/output validation with OpenAI Agents SDK and Pydantic AI)
- Deployment (Streamlit, Render, AWS)
- Building a coding agent from scratch
- Deep research agent
- Other use cases (FAQ assistant, code explainer, book writer)
- Project work and demos

## Student Projects

Students create multiple projects throughout the course including FAQ assistants, YouTube Q&A systems, documentation agents, coding agents, and deep research agents. All projects can be viewed on the course website.

## Framework Approach

The course focuses on PydanticAI as the primary framework. Other frameworks (LangChain, LangGraph, Google ADK, CrewAI, OpenAI Agents SDK) are included as optional materials based on student demand, but the main teaching and examples use PydanticAI.

## Wikidata MCP Workshop

A recent workshop demonstrated Wikidata MCP in action for fact-checking. The example showed how LLMs have knowledge cutoffs and may hallucinate when asked about current events (like "who is the current president"). By connecting to Wikidata through MCP, the agent can retrieve accurate, up-to-date information[^5].

The workshop covered:
- Using open language models for fact-checking
- Retrieving facts from Wikidata as a priori truths
- Checking how well a claim matches known facts
- Using one model for reranking to select relevant facts
- Using a second model to verify truthfulness

In English terminology, the claim is what we're checking, and facts are what we extract from Wikidata (considered a priori true)[^6].

## NOW GmbH Workshop

Xia He-Bleinagel from NOW GmbH hosted a two-day AI agents training session. The workshop covered text search, semantic search, LLM agents, agent tools, and MCP. Participants found that understanding these foundations gives a completely different perspective on what's possible with AI tools. Day 2 focused on building a custom AI agent tool[^7].

## Sources

- [20260120_135731_AlexeyDTC_msg333_transcript.txt](../inbox/raw/20260120_135731_AlexeyDTC_msg333_transcript.txt)
- [20260120_135733_AlexeyDTC_msg334.md](../inbox/raw/20260120_135733_AlexeyDTC_msg334.md)
- [20260120_135830_AlexeyDTC_msg337.md](../inbox/raw/20260120_135830_AlexeyDTC_msg337.md)
- [20260120_135830_AlexeyDTC_msg338.md](../inbox/raw/20260120_135830_AlexeyDTC_msg338.md)
- [20260121_091318_AlexeyDTC_msg353_transcript.txt](../inbox/raw/20260121_091318_AlexeyDTC_msg353_transcript.txt)
- [20260121_125000_AlexeyDTC_msg359_transcript.txt](../inbox/raw/20260121_125000_AlexeyDTC_msg359_transcript.txt)
- [20260121_114016_AlexeyDTC_msg355_transcript.txt](../inbox/raw/20260121_114016_AlexeyDTC_msg355_transcript.txt)
- [20260120_174345_AlexeyDTC_msg351.md](../inbox/raw/20260120_174345_AlexeyDTC_msg351.md)
- [20260122_155148_AlexeyDTC_msg395.md](../inbox/raw/20260122_155148_AlexeyDTC_msg395.md)
- [20260121_123704_AlexeyDTC_msg357_photo.md](../inbox/used/20260121_123704_AlexeyDTC_msg357_photo.md)

[^1]: [AI Bootcamp: From RAG to Agents](https://maven.com/alexey-grigorev/from-rag-to-agents)
[^2]: [20260121_091318_AlexeyDTC_msg353_transcript.txt](../inbox/raw/20260121_091318_AlexeyDTC_msg353_transcript.txt)
[^3]: [20260121_091318_AlexeyDTC_msg353_transcript.txt](../inbox/raw/20260121_091318_AlexeyDTC_msg353_transcript.txt)
[^4]: [20260121_125000_AlexeyDTC_msg359_transcript.txt](../inbox/raw/20260121_125000_AlexeyDTC_msg359_transcript.txt)
[^5]: [20260121_114016_AlexeyDTC_msg355_transcript.txt](../inbox/raw/20260121_114016_AlexeyDTC_msg355_transcript.txt)
[^6]: [20260121_114016_AlexeyDTC_msg355_transcript.txt](../inbox/raw/20260121_114016_AlexeyDTC_msg355_transcript.txt)
[^7]: [20260120_174345_AlexeyDTC_msg351.md](../inbox/raw/20260120_174345_AlexeyDTC_msg351.md)
