---
title: "What's New in the Telegram Writing Assistant"
created: 2026-02-19
updated: 2026-02-20
tags: [telegram-bot, claude-code, agents, tools]
status: draft
---

# What's New in the Telegram Writing Assistant

Article idea: combine the topic of how subagents are used in Claude Code with the recent improvements to the Telegram Writing Assistant[^1].

## Article Concept

The article would cover two related topics:

1. How I currently use subagents in Claude Code
2. What is new in the Telegram Writing Assistant

These topics overlap because the main improvement to the writing assistant is the addition of subagents[^1].

## Key Features to Cover

- Subagents added to the processing pipeline
- Various things fixed and improved based on ongoing feedback
- The bot self-corrects based on feedback - I just provide feedback and it adjusts its behavior on the next run[^1]
- Research section - a new department for topics being investigated
- Link summary - when I find an interesting article, the bot can create a short summary or do a deep analysis and add it to an existing research topic[^1]
- Quality assurance agent at the end of processing that verifies nothing was forgotten (the main agent sometimes has problems with this)[^1]

## Audio File Processing

Currently when Telegram receives files (not voice notes), the bot does not do anything with them. We want it to handle audio files too - when it receives audio that is not a voice note, it most likely contains speech, so it should transcribe it the same way and process it as a regular voice note. This is a task that needs to be implemented.[^2]

Code was added to handle custom audio files (mp4, m4a), but the first test did not work. Need to check the logs to see what happened.[^3][^4]

## Sources

[^1]: [20260219_081802_AlexeyDTC_msg2017_transcript.txt](../inbox/used/20260219_081802_AlexeyDTC_msg2017_transcript.txt)
[^2]: [20260219_144023_AlexeyDTC_msg2079_transcript.txt](../inbox/used/20260219_144023_AlexeyDTC_msg2079_transcript.txt)
[^3]: [20260220_070425_AlexeyDTC_msg2103_transcript.txt](../inbox/used/20260220_070425_AlexeyDTC_msg2103_transcript.txt)
[^4]: [20260220_070616_AlexeyDTC_msg2106_transcript.txt](../inbox/used/20260220_070616_AlexeyDTC_msg2106_transcript.txt)
