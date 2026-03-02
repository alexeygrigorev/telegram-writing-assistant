---
title: "Personal Project Ideas"
created: 2026-03-02
updated: 2026-03-02
tags: [ideas, projects, personal]
status: draft
---

# Personal Project Ideas

A collection of personal project ideas I want to implement. These are my own ideas for tools and systems I want to build, not student project ideas or course assignments.

## Voice-Based Document Editing

I have articles already written in Google Docs. I want to edit them using voice input. The idea: I dictate notes via Telegram or record them on a computer, and the system applies all my comments as comments to a Google Doc or DOCX document. So instead of sitting down and manually editing, I record voice notes with my feedback and corrections, and they get applied to the document automatically[^1].

## Notebook Server for Claude Code

Currently when Claude Code needs to experiment with code, it either writes a script and runs it, or writes code in a notebook but has to run the entire notebook from scratch. This is inconvenient. I want to build an interface like Jupyter but through the CLI - I do not like Jupyter's interface, I would rather do it through CLI[^2].

The goal is for Claude Code to maintain a Python session where it can run code and see outputs, similar to how ChatGPT does with its Python code interpreter. In ChatGPT, when you ask it to write Python code, it writes and runs code in an interactive session, you can ask follow-up questions, and the code state persists between messages. This would accelerate the iteration cycle when developing course materials and examples.

Some options being considered: MCP (Model Context Protocol) for Jupyter notebooks, understanding how ChatGPT's code analysis feature works with IPython kernels, creating a tool that synchronizes Claude's code session with notebook sessions.

See also: [From Vague Ideas to Concrete Results with ChatGPT](work-in-progress/idea-to-concrete-iteration.md) where this idea was first recorded[^3].

## Voice-Controlled Development Bot

A general-purpose Telegram bot that executes development tasks from voice commands. Record a voice message in Telegram, the bot reacts and does something - create issues in repositories, change its own code, execute commands. Like saying "I want this feature" and it goes and implements it. Should run in a Docker sandbox for security.

This is still an idea, but after finishing the course, all the tools and skills are in place: AI-assisted development experience, a server where it can run, and experience with multi-agent orchestration.

See: [Voice-Controlled Development Bot](ideas/voice-controlled-dev-bot.md) for full details[^4].

## DataTasks - Task Management App

A unified task management system that combines Trello-like project templates with spreadsheet-like task lists. Built for community management workflows where tasks come from multiple sources (spreadsheets, Trello, Telegram, email). The architecture is serverless: AWS Lambda with JavaScript, DynamoDB, vanilla JS frontend. Main goal: maximally cheap, no hosting costs.

Implementation has started using Claude Code. The project is at [github.com/alexeygrigorev/datatasks](https://github.com/alexeygrigorev/datatasks).

See: [Task Management App Idea](ideas/task-management-app-idea.md) for full details[^5].

## Content Reuse System

A system that helps achieve different content formats by reusing existing content. The goal is to understand where content lives and what can be pulled from it for different purposes - turning the same source material into newsletters, social posts, course materials, and community updates[^6].

## Sources

[^1]: [20260302_074708_AlexeyDTC_msg2658_transcript.txt](../inbox/used/20260302_074708_AlexeyDTC_msg2658_transcript.txt)
[^2]: [20260302_074814_AlexeyDTC_msg2660_transcript.txt](../inbox/used/20260302_074814_AlexeyDTC_msg2660_transcript.txt)
[^3]: [20260201_114115_AlexeyDTC_msg816_transcript.txt](../inbox/used/20260201_114115_AlexeyDTC_msg816_transcript.txt)
[^4]: [20260220_135246_AlexeyDTC_msg2144_transcript.txt](../inbox/used/20260220_135246_AlexeyDTC_msg2144_transcript.txt)
[^5]: [20260211_043339_AlexeyDTC_msg1351_transcript.txt](../inbox/used/20260211_043339_AlexeyDTC_msg1351_transcript.txt)
[^6]: [20260214_111721_AlexeyDTC_msg1687.md](../inbox/used/20260214_111721_AlexeyDTC_msg1687.md)
