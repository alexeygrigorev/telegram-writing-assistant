---
title: "In-Person Agents Workshop in Berlin at NOW-GMBH"
created: 2026-01-19
updated: 2026-01-23
tags: [workshop, agents, teaching, ai-bootcamp, groq, anthropic, mcp]
status: draft
---

# In-Person Agents Workshop in Berlin at NOW-GMBH

A two-day workshop on AI agents, based on materials from the AI Bootcamp course. This workshop was created for a company in Berlin (NOW-GMBH) and covers foundations of AI agents and building custom coding agents.

Source: https://github.com/alexeygrigorev/now-workshop-agents

## Workshop Format

This is a two-day workshop from 9:00 to 16:00 with breaks:
- 10:30 - 10:45: Coffee break
- 12:00 - 13:00: Lunch break
- 15:00 - 15:15: Coffee break

## Day 1: Foundations of AI Agents

Learning objectives:
- Learn Large Language Models and Retrieval-Augmented Generation
- Build conversational agents using the OpenAI SDK
- Create data-processing pipelines
- Add agentic behavior with function calling
- Use PydanticAI as the agents orchestrator framework
- Expose tools via MCP

### Part 1: Accessing LLMs with OpenAI API

OpenAI client setup and basic requests. Understanding system prompts, conversation history, and the stateless nature of LLMs. Structured output with Pydantic models for type-safe responses.

### Part 2: Alternatives to OpenAI

Groq API for free access to open-source models. Anthropic (Claude) API with structured output support for Sonnet and Opus models. Accessing Claude via AWS Bedrock and z.ai. Google Gemini API with structured output via response_mime_type.

### Part 3: RAG (Retrieval-Augmented Generation)

RAG combines retrieval and generation to let LLMs answer questions using your specific data. We use minsearch for text search and sentence-transformers for vector search, then combine both for hybrid search.

### Part 4: Agents

Agents let the LLM decide which tools to call and in what order. We cover the agentic RAG pattern where the LLM decides whether and what to search. The tool-calling loop continues until no more tool calls are needed. ToyAIKit framework is used to illustrate how agents work.

## Day 2: Building a Custom Coding Agent

Learning objectives:
- Set up a Django project template
- Implement tools for file access and manipulation
- Design and develop a coding agent
- Coordinate multiple agents
- Add monitoring and guardrails with Pydantic Logfire

### Part 1: Django Project Template

Setting up a Django template project with uv for environment management, SQLite database, and TailwindCSS for styling. The template serves as the foundation for the coding agent to work with.

### Part 2: Agent Tools

Creating an AgentTools class with methods for:
- read_file: View existing code
- write_file: Create or modify files
- execute_bash_command: Run commands
- see_file_tree: Navigate the project
- search_in_files: Find specific code

### Part 3: Coding Agent

Building a coding agent using ToyAIKit and then switching to PydanticAI for production-ready features. The agent explores the project structure, thinks about the sequence of changes, and makes modifications step by step.

### Part 4: Multi-Agent Systems

The planner-executor pattern where a planning agent creates structured plans and an executor agent implements each step. Specialized agents for research and writing. A coordinator agent pattern where the LLM decides which agents to call.

### Part 5: Monitoring with Pydantic Logfire

Instrumenting agent calls with Logfire for observability. Tool callbacks to monitor individual tool calls in real-time.

### Part 6: Guardrails

Input validation with Pydantic to block dangerous commands. Output sanitization to check generated code for harmful patterns. Cost limits with RunLimits for maximum steps and tokens.

## Teaching Experience

The workshop went well. Participants were engaged and the material flowed naturally from one topic to the next. The progression from basic API usage to full agent implementations worked well for building understanding.

<figure>
  <img src="../assets/images/agents-workshop/workshop-group-session.jpg" alt="Group workshop session with participants working on laptops">
  <figcaption>Participants working through the exercises during the in-person workshop session</figcaption>
  <!-- This shows the collaborative learning environment -->
</figure>

## Related Courses

This workshop content is based on materials from:
- AI Bootcamp: https://maven.com/alexey-grigorev/from-rag-to-agents
- LLM Zoomcamp: https://github.com/DataTalksClub/llm-zoomcamp

## Sources
- [20260119_154030_AlexeyDTC_msg308_transcript.txt](../inbox/raw/20260119_154030_AlexeyDTC_msg308_transcript.txt)
- [20260119_154248_AlexeyDTC_msg309.jpg](../assets/images/agents-workshop/workshop-group-session.jpg)
- [20260120_135731_AlexeyDTC_msg333_transcript.txt](../inbox/raw/20260120_135731_AlexeyDTC_msg333_transcript.txt)
- [20260120_135931_AlexeyDTC_msg341_transcript.txt](../inbox/raw/20260120_135931_AlexeyDTC_msg341_transcript.txt)
- [20260120_140020_AlexeyDTC_msg345_transcript.txt](../inbox/raw/20260120_140020_AlexeyDTC_msg345_transcript.txt)
- [now-workshop-agents](https://github.com/alexeygrigorev/now-workshop-agents)
- [20260123_080056_valeriia_kuka_msg415_photo.md](../inbox/raw/20260123_080056_valeriia_kuka_msg415_photo.md) - Feedback to make title more specific and separate workshops
