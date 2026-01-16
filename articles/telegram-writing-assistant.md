---
title: "Telegram Writing Assistant"
created: 2026-01-16
updated: 2026-01-16
tags: [telegram, bot, knowledge-management, automation]
status: draft
---

# Telegram Writing Assistant

A personal knowledge management system where you send thoughts to Telegram (text, voice, images) and a bot saves everything locally, processes it, and organizes it into articles.

## Core Idea

<figure>
  <img src="../assets/images/telegram-writing-assistant/project-summary-workflow.jpg" alt="Project summary workflow">
  <figcaption>A visual summary of the system workflow from sending thoughts to organizing into articles</figcaption>
  <!-- This illustrates the high-level concept of the system -->
</figure>

I usually do brain dumps in the form of voice messages in Telegram. This needs to be organized. The idea is to transcribe these voice messages and add the transcription to some file. As voice messages accumulate, there may be several articles, and from each of these files there will be some article. It will gradually be filled and filled. Then, when the article is finished, we simply remove that article.

## Workflow

1. Send materials to Telegram bot (text, voice, images)
2. Bot saves everything locally to inbox/raw/
3. Run /process command to organize materials
4. Claude analyzes accumulated materials
5. Updates existing articles or creates new ones
6. Commits to GitHub
7. Sends commit link back to Telegram

## Language Handling

The agent can understand any messages regardless of language. When I record a voice message, I want the agent to understand where to add the material from this voice message, into which existing article it relates.

I usually write texts in English, I have a Substack where I write in English. For voice notes, it's sometimes easier for me to speak in Russian. Since we usually communicate in Russian with Valeria, voice messages are also in Russian.

Target language for articles is English. Voice messages can be in any language, but articles should only be in English. When processing, Claude should translate everything to English.

## Article Structure

Each article must include a list of source materials. This is important for cleanup when an article is deleted, so we can easily delete old resources we no longer need, like old transcripts.

## Sources
- [20260116_210119_AlexeyDTC_transcript.txt](../inbox/raw/20260116_210119_AlexeyDTC_transcript.txt)
- [20260116_210336_AlexeyDTC_transcript.txt](../inbox/raw/20260116_210336_AlexeyDTC_transcript.txt)
- [20260116_205911_AlexeyDTC_photo.md](../inbox/used/20260116_205911_AlexeyDTC_photo.md)
