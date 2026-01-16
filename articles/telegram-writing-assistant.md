---
title: "Telegram Writing Assistant"
created: 2026-01-16
updated: 2026-01-16
tags: [telegram, bot, personal-knowledge, automation]
status: draft
---

# Telegram Writing Assistant

A personal knowledge management system where thoughts are sent to Telegram and automatically organized into articles.

## Core Concept

The system captures ideas through Telegram in multiple formats: voice notes, text, and images. The bot saves everything locally to inbox/raw/. Voice messages get transcribed. A command triggers analysis of accumulated materials to update existing articles or create new ones.

## Workflow

1. Send thoughts to Telegram (text, voice, images)
2. Bot saves everything to inbox/raw/
3. Run /process command
4. Materials are analyzed and organized into articles
5. Processed files move to inbox/used/

## Language Handling

Voice notes and messages can be in any language, but articles are in English. The agent translates content during processing. The user records voice notes in Russian but writes articles in English for Substack.

## Article Management

Each article tracks source materials for easy cleanup. When an article is complete, it can be removed and all its source files deleted. Articles build up gradually from multiple voice notes and messages on the same topic.

## Exception Handling

When exceptions occur during bot processing, the error details are sent to the chat for immediate debugging.

## Sources

- [20260116_210119_AlexeyDTC_transcript.txt](../inbox/raw/20260116_210119_AlexeyDTC_transcript.txt)
- [20260116_210336_AlexeyDTC_transcript.txt](../inbox/raw/20260116_210336_AlexeyDTC_transcript.txt)
- [20260116_211210_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211210_AlexeyDTC_transcript.txt)
- [20260116_213156_AlexeyDTC_transcript.txt](../inbox/raw/20260116_213156_AlexeyDTC_transcript.txt)
- [20260116_213629_AlexeyDTC_transcript.txt](../inbox/raw/20260116_213629_AlexeyDTC_transcript.txt)
- [20260116_205911_AlexeyDTC_photo.md](../inbox/raw/20260116_205911_AlexeyDTC_photo.md)
