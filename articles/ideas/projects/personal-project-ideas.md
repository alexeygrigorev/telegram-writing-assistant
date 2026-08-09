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

I have articles already written in Google Docs. I want to edit them using voice input.

I dictate notes via Telegram or record them on a computer. The system then applies all my comments to a Google Doc or DOCX document. Instead of sitting down and manually editing, I record voice notes with feedback and corrections. They get applied to the document automatically[^1].

## Notebook Server for Claude Code

Currently Claude Code has two ways to experiment with code. It either writes a script and runs it, or writes code in a notebook. The notebook path has to run from scratch each time. That is inconvenient.

I want to build an interface like Jupyter but through the CLI. Jupyter's interface is not my thing - I would rather do it through the CLI[^2].

I want Claude Code to maintain a Python session where it can run code and see outputs. Think ChatGPT's Python code interpreter. In ChatGPT, when you ask it to write Python code, it writes and runs code in an interactive session. You can ask follow-up questions and the code state persists between messages. This would accelerate the iteration cycle when developing course materials and examples.

Some options I am considering:

- MCP (Model Context Protocol) for Jupyter notebooks
- Understanding how ChatGPT's code analysis feature works with IPython kernels
- Creating a tool that synchronizes Claude's code session with notebook sessions

More context in [From Vague Ideas to Concrete Results with ChatGPT](work-in-progress/idea-to-concrete-iteration.md), where this idea was first recorded[^3].

## Voice-Controlled Development Bot

A general-purpose Telegram bot that executes development tasks from voice commands. Record a voice message in Telegram, and the bot reacts. It can create issues in repositories, change its own code, or execute commands. Like saying "I want this feature" and having it implement it. Should run in a Docker sandbox for security.

This is still an idea, but after finishing the course, all the tools and skills are in place. I have AI-assisted development experience, a server where it can run, and experience with multi-agent orchestration.

Full details in [Voice-Controlled Development Bot](ideas/voice-controlled-dev-bot.md)[^4].

## DataTasks - Task Management App

A unified task management system that combines Trello-like project templates with spreadsheet-like task lists. Built for community management workflows where tasks come from multiple sources (spreadsheets, Trello, Telegram, email).

The architecture is serverless - AWS Lambda with JavaScript, DynamoDB, and a vanilla JS frontend. It aims to be maximally cheap, with no hosting costs.

Implementation has started using Claude Code. The project is at [github.com/alexeygrigorev/datatasks](https://github.com/alexeygrigorev/datatasks).

Full details in [Task Management App Idea](ideas/task-management-app-idea.md)[^5].

## Content Reuse System

A system that helps achieve different content formats by reusing existing content. It maps where content lives and what can be pulled from it for different purposes. The same source material gets turned into newsletters, social posts, course materials, and community updates[^6].

## Sources

[^1]: [20260302_074708_AlexeyDTC_msg2658_transcript.txt](../inbox/used/20260302_074708_AlexeyDTC_msg2658_transcript.txt)
[^2]: [20260302_074814_AlexeyDTC_msg2660_transcript.txt](../inbox/used/20260302_074814_AlexeyDTC_msg2660_transcript.txt)
[^3]: [20260201_114115_AlexeyDTC_msg816_transcript.txt](../inbox/used/20260201_114115_AlexeyDTC_msg816_transcript.txt)
[^4]: [20260220_135246_AlexeyDTC_msg2144_transcript.txt](../inbox/used/20260220_135246_AlexeyDTC_msg2144_transcript.txt)
[^5]: [20260211_043339_AlexeyDTC_msg1351_transcript.txt](../inbox/used/20260211_043339_AlexeyDTC_msg1351_transcript.txt)
[^6]: [20260214_111721_AlexeyDTC_msg1687.md](../inbox/used/20260214_111721_AlexeyDTC_msg1687.md)
