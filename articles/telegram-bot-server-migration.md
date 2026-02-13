---
title: "Telegram Bot Server Migration"
created: 2026-02-13
updated: 2026-02-13
tags: [telegram-bot, infrastructure, deployment]
status: draft
---

# Telegram Bot Server Migration

Plans to move the Telegram writing assistant bot from a local computer to a dedicated server.

## The problem

The Telegram bot currently requires the computer to be always on. This is not very convenient. I want to be able to turn off the computer without worrying about the bot stopping[^2].

## The plan

We set up an n8n server some time ago but never really used it. Now instead of n8n, I want to repurpose that server to run the Telegram bot. I also want to run other things on it, including OpenCode[^1].

## Sources

[^1]: [20260213_171420_AlexeyDTC_msg1637_transcript.txt](../inbox/used/20260213_171420_AlexeyDTC_msg1637_transcript.txt)
[^2]: [20260213_171440_AlexeyDTC_msg1639_transcript.txt](../inbox/used/20260213_171440_AlexeyDTC_msg1639_transcript.txt)
