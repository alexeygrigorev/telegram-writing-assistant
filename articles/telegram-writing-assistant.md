---
title: "Telegram Writing Assistant"
created: 2026-01-16
updated: 2026-01-16
tags: [telegram, bot, writing, knowledge-management]
status: draft
---

# Telegram Writing Assistant

A personal knowledge management system where thoughts sent to Telegram are organized into articles.

## Overview

The core idea is to have a bot that helps organize voice notes and other materials. You send text, voice messages, or images to Telegram. The bot saves everything locally. Then a command processes these materials to update existing articles or create new ones.

## Workflow

1. Send thoughts to Telegram (text, voice, images)
2. Bot saves everything to inbox/raw/
3. Voice messages are transcribed
4. Command triggers processing:
   - Analyze accumulated materials
   - Update existing articles or create new ones
   - Commit to GitHub
   - Send commit link back to chat

## Voice Notes and Language

Voice notes are recorded in Russian for convenience. The system handles this automatically. Materials are translated to English before being added to articles. The target language for all articles is English.

The agent can understand messages in any language. It figures out which article each voice note relates to. Then it adds the material to that existing article.

## Sources
- [20260116_210119_AlexeyDTC_transcript.txt](../inbox/raw/20260116_210119_AlexeyDTC_transcript.txt)
- [20260116_210336_AlexeyDTC_transcript.txt](../inbox/raw/20260116_210336_AlexeyDTC_transcript.txt)
- [20260116_205911_AlexeyDTC_photo.md](../inbox/raw/20260116_205911_AlexeyDTC_photo.md)
