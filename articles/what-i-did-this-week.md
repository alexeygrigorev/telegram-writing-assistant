---
title: "What I Did This Week"
created: 2026-02-11
updated: 2026-02-11
tags: [weekly, updates]
status: draft
---

# What I Did This Week

Weekly updates on work in progress. This article serves as a working draft - I remove content when I publish it elsewhere.

## 2026-W06 (February 6-12, 2026)

Wednesday, February 11, 2026

### Course Recording: AI Engineering Buildcamp

I am fully focused on recording course videos this week. As of Wednesday, I have completed the main part but haven't reached the frameworks section yet.

Teaching Approach: Agents in Detail

The main change in my approach is covering agents in much more detail. Previously I would go through this topic superficially and point to implementations in the Toyaikit library. Now I describe this in great detail because I think it's important.

Many people use LangChain and other frameworks without understanding what's happening inside. I saw positive feedback on Twitter from people who said they didn't understand how LangChain worked until they wrote their own agentic tool call loop.

I combined many agentic frameworks into one class called "agent." A mini framework turned out this way. It's not very flexible, but as an illustration of what's happening inside these frameworks, it works well.

Course Progression

The course follows this progression:

1. Pure OpenAI API requests - the lowest level
2. Toyaikit - a lightweight library I wrote based on past workshops and courses
3. Toyaikit is for education, debugging, and prototyping only - not for production
4. Production frameworks like OpenAI SDK and others

Topics Covered

Regular RAG versus agentic approaches:

- Regular RAG just retrieves information
- Agentic RAG lets the agent choose what queries to make
- Agentic search goes further - the agent sees a snippet and title, decides what to look at, then requests the full page

I finished recording the agentic search section.

Still To Record

- OpenAI SDK lecture (in progress)
- Other providers like Anthropic
- Tool calling with different providers
- Other frameworks: LangChain, LangGraph, OpenAI Agents SDK

### Background Work: Monday Event Preparation

I am preparing material for Monday's event about AI engineer roles and how I see them.

How I prepare material:

1. I throw all thoughts into Telegram as a brain dump
2. The system structures the information
3. I use the structured information as a transcript for the talk

This works well during breaks from recording. When I'm going somewhere or have thoughts about the project, I dictate a voice message. The system structures everything and I use it to prepare for the event.

## Sources

[^1]: [20260211_094131_AlexeyDTC_msg1377_transcript.txt](../inbox/raw/20260211_094131_AlexeyDTC_msg1377_transcript.txt)
[^2]: [20260211_094212_AlexeyDTC_msg1378_transcript.txt](../inbox/raw/20260211_094212_AlexeyDTC_msg1378_transcript.txt)
