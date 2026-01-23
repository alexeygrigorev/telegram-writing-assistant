---
title: "Course Management Agent"
created: 2026-01-23
updated: 2026-01-23
tags: [agents, automation, course-management, claude-skills]
status: draft
---

# Course Management Agent

Automating course administration tasks using Claude Skills to create assignments and course plans through an agent that sends POST requests to a course management platform.

## The Problem

Creating course content involves significant manual work in the administration interface. For a Data Engineering course, creating all homework assignments with deadlines takes 20-30 minutes of clicking. This is repetitive manual work that could be automated[^1].

Previously, I delegated some of this to Grace, but it still takes time and is not immediate.

## The Solution: An Agent with Skills

I created a Cloud Agent that uses skills describing how to interact with the course management platform API. The workflow:

1. First, I used code to create an API endpoint on the course management platform that accepts POST requests with all necessary information
2. Created a Claude agent with skills describing the API and how to use it
3. Now I can describe what I want in text format - which homework assignments to create, what deadlines they should have
4. The agent makes the POST requests and sends me a URL to review

## Time Investment

I spent about 1.5-2 hours setting this up initially. Now for each course, I save significant time on every homework assignment. The automation pays for itself quickly[^2].

## Application to Individual Assignments

The same approach works for creating individual homework assignments. My previous workflow:
1. Write homework in a Markdown document
2. Push to repository
3. Open the platform admin interface
4. Manually enter questions and answers (5-10 minutes)

Now I can tell the agent: "Here's a markdown document with homework, please create the homework form." Done[^3].

## Terminal-Based vs IDE-Based AI Assistants

I see Claude Code as an assistant that can execute bash commands in the terminal. This is not necessarily about coding - Claude Code handles this well, but for more thoughtful coding work, I prefer Cursor or other IDE-based assistants.

With Cursor, I see all changes the agent makes. I can accept or reject each change. I have more control over what happens. When working from the terminal, I see what the agent is doing and can stop it, but it's more of a "wipe-coding" experience than AI-assisted coding[^4].

For tasks like "send a POST request" or "make this pull request" where I can review the plan first, the terminal workflow works great. I can ask to see the plan first, approve it, and then the agent creates everything[^5].

## Source

https://github.com/alexeygrigorev/course-management-agent

## Sources

- [20260123_120902_valeriia_kuka_msg422.md](../inbox/raw/20260123_120902_valeriia_kuka_msg422.md)
- [20260123_120918_valeriia_kuka_msg424_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg424_transcript.txt)
- [20260123_120918_valeriia_kuka_msg425_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg425_transcript.txt)
- [20260123_120918_valeriia_kuka_msg426_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg426_transcript.txt)
- [20260123_120918_valeriia_kuka_msg427_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg427_transcript.txt)
- [20260123_120918_valeriia_kuka_msg428_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg428_transcript.txt)
- [20260123_120918_valeriia_kuka_msg429_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg429_transcript.txt)
- [20260123_120956_valeriia_kuka_msg436.md](../inbox/raw/20260123_120956_valeriia_kuka_msg436.md)

[^1]: [20260123_120918_valeriia_kuka_msg424_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg424_transcript.txt)
[^2]: [20260123_120918_valeriia_kuka_msg424_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg424_transcript.txt)
[^3]: [20260123_120918_valeriia_kuka_msg425_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg425_transcript.txt)
[^4]: [20260123_120918_valeriia_kuka_msg426_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg426_transcript.txt)
[^5]: [20260123_120918_valeriia_kuka_msg428_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg428_transcript.txt)
