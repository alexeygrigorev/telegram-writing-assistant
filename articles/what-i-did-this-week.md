---
title: "What I Did This Week"
created: 2026-02-11
updated: 2026-02-11
tags: [weekly, updates]
status: draft
---

# What I Did This Week

Weekly updates on work in progress. This article serves as a working draft - content is removed when published elsewhere.

## 2026-W06 (February 6-12, 2026)

**Message date: 2026-02-11**

### Course Video Recording

Focused this week on recording course videos. As of Wednesday (the current recording date), I have completed most of the content but haven't reached frameworks yet.

The main change in approach is covering agents in much more detail. Previously, I mentioned agents briefly and pointed to implementations in libraries like Toyaikit. Now I provide detailed explanations because:

- Many people use LangChain and other frameworks without understanding what's happening inside
- I've seen positive feedback on Twitter from people who say they didn't understand how LangChain worked until they wrote their own agentic tool call loop
- This deeper understanding is important

I created a simple agent class that demonstrates the core concepts - a mini framework that shows what's happening inside larger frameworks. It's not flexible enough for production but serves as an educational tool.

The progression in the course:
1. Pure OpenAI API requests (lowest level)
2. Toyaikit - a lightweight library I wrote based on workshops and courses
3. Toyaikit is for education, debugging, and prototyping only - not for production
4. Production frameworks like OpenAI's SDK and others

### Topics Covered So Far

- Basic RAC (Retrieval Augmented Generation)
- Agentic RAC - the agent chooses which queries to make
- Agentic Search - the agent sees snippets and titles, decides which full pages to fetch, moving beyond traditional RAG

Currently recording the lecture on OpenAI's SDK. Still to record:
- Using other providers (Anthropic, etc.)
- Tool calling with different providers
- Other frameworks like LangChain, LangGraph, OpenAI Agents SDK

### Background Work: Content Preparation

While doing other activities (breaks from recording, travel), I use the Telegram bot to capture thoughts about the upcoming Monday event on AI engineer roles. This braindump approach helps me:
- Capture ideas as they come
- Let the system structure them
- Build a transcript that serves as the foundation for the talk

This is how I prepare content - scattered thoughts throughout the week get structured and become the basis for presentations.

## Sources

[^1]: [20260211_093351_AlexeyDTC_msg1375_transcript.txt](../inbox/raw/20260211_093351_AlexeyDTC_msg1375_transcript.txt)
[^2]: [20260211_093515_AlexeyDTC_msg1376_transcript.txt](../inbox/raw/20260211_093515_AlexeyDTC_msg1376_transcript.txt)
[^3]: [20260211_094131_AlexeyDTC_msg1377_transcript.txt](../inbox/raw/20260211_094131_AlexeyDTC_msg1377_transcript.txt)
[^4]: [20260211_094212_AlexeyDTC_msg1378_transcript.txt](../inbox/raw/20260211_094212_AlexeyDTC_msg1378_transcript.txt)
