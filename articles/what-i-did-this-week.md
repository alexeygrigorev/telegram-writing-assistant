---
title: "What I Did This Week"
created: 2026-02-11
updated: 2026-02-13
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

Thursday, February 13, 2026

### Course Recording

Main focus this week is still course recording and video production[^3].

### Nobook: Python-Based Jupyter Notebooks

In parallel with course recording, I ran an experiment I had been wanting to do for a long time. I built Nobook - a tool that uses plain `.py` files as Jupyter notebooks instead of `.ipynb` JSON files. Claude Code with the latest Opus wrote all the code in one evening while I spent about an hour checking and correcting. See the separate article on [Nobook](nobook.md) for details[^3][^4].

### Claude Code: Testing New Models

I experimented with the new Sonnet 4.6 and Opus 4.6 models in Claude Code. The improvements seem to come more from software updates (better planning, context compaction) than from the models themselves. See [Claude Code Experiments](claude-code-experiments.md) for details[^5].

### OpenCode Experiments with GLM-5

I tried OpenCode - an open-source AI coding assistant - with the new GLM-5 model. Built two things in background mode while doing course recording. The desktop mode is nice - it is built on VS Code. See [OpenCode Experiments](opencode-experiments.md), [Microphone Booster App](microphone-booster-app.md), and [AI Engineer RPG Game](ai-engineer-rpg-game.md) for details[^6][^7].

### Paid Community: Accountability Circles

New idea for the paid community: accountability circles / mastermind groups where members meet regularly to share progress and help each other with blockers. Running them in sprints rather than continuously to maintain interest and enable promotion. Plan to redirect mentoring requests to this structure[^8].

## Sources

[^1]: [20260211_094131_AlexeyDTC_msg1377_transcript.txt](../inbox/raw/20260211_094131_AlexeyDTC_msg1377_transcript.txt)
[^2]: [20260211_094212_AlexeyDTC_msg1378_transcript.txt](../inbox/raw/20260211_094212_AlexeyDTC_msg1378_transcript.txt)
[^3]: [20260213_070408_AlexeyDTC_msg1574_transcript.txt](../inbox/used/20260213_070408_AlexeyDTC_msg1574_transcript.txt)
[^4]: [20260213_070414_AlexeyDTC_msg1575_transcript.txt](../inbox/used/20260213_070414_AlexeyDTC_msg1575_transcript.txt)
[^5]: [20260213_065936_AlexeyDTC_msg1573_transcript.txt](../inbox/used/20260213_065936_AlexeyDTC_msg1573_transcript.txt)
[^6]: [20260213_145200_AlexeyDTC_msg1607_transcript.txt](../inbox/used/20260213_145200_AlexeyDTC_msg1607_transcript.txt)
[^7]: [20260213_145555_AlexeyDTC_msg1608_transcript.txt](../inbox/used/20260213_145555_AlexeyDTC_msg1608_transcript.txt)
[^8]: [20260213_152027_AlexeyDTC_msg1610_transcript.txt](../inbox/used/20260213_152027_AlexeyDTC_msg1610_transcript.txt)
