---
title: "What's New in the Telegram Writing Assistant"
created: 2026-02-19
updated: 2026-02-25
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

## Claude Code Subagents

Claude Code supports creating subagents for specialized tasks. This is useful when a single agent's context window becomes overloaded with processing multiple articles or resources.

## When to Use Subagents

When processing multiple URLs or large amounts of content, a single agent reading everything can exceed its context window. This forces context compaction, which loses information and slows down processing.

The solution is to create specialized subagents that handle specific types of work independently. This keeps the main agent's context focused on its primary task.

## Creating Subagents

Creating a subagent in Claude Code is straightforward:

1. Run the `/agents` slash command
2. Select "Create new agent"
3. Describe what the agent should do
4. The agent is created and available immediately

The documentation claims no restart is needed, but a restart may be required for the subagent to work properly.

## Example Use Cases

For research workflows, two subagents can be created:

- Research agent - Summarizes research articles for research topics
- Resource agent - Summarizes interesting resources for the resources newsletter

Both agents use Jina Reader to fetch web content, then process it independently. The main agent remains focused on its primary task (processing voice messages) while subagents handle external content[^2].

## Verification Subagent

A verification subagent was created to address the issue of summarizing voice message content despite instructions not to. Even though the instructions explicitly say not to summarize, the bot sometimes still does it.

The verification subagent runs at the end of processing and:

1. Checks the text that was written
2. Compares it against the original source messages
3. Adds missing content if anything was omitted

This two-step process ensures complete preservation of voice message content[^1].

## Benefits

- Main agent context stays clean and focused
- No context window overflow from processing external content
- Specialized agents can be iterated on independently
- Parallel processing of multiple URLs speeds up workflow

## Audio File Processing

Currently when Telegram receives files (not voice notes), the bot does not do anything with them. We want it to handle audio files too - when it receives audio that is not a voice note, it most likely contains speech, so it should transcribe it the same way and process it as a regular voice note. This is a task that needs to be implemented.[^2]

Code was added to handle custom audio files (mp4, m4a), but the first test did not work. Need to check the logs to see what happened.[^3][^4]

## Video Download Support

I taught the bot to download YouTube videos. When running on my local computer, regular requests work fine. But since all the bots moved to Hetzner, it is a data center, not a regular computer, so standard downloads do not work. I had to add proxy support to the regular script. It was not particularly difficult since I had done it before, but I had to re-implement it for the new setup.[^5]

## Sources

[^1]: [20260219_081802_AlexeyDTC_msg2017_transcript.txt](../inbox/used/20260219_081802_AlexeyDTC_msg2017_transcript.txt)
[^2]: [20260219_144023_AlexeyDTC_msg2079_transcript.txt](../inbox/used/20260219_144023_AlexeyDTC_msg2079_transcript.txt)
[^3]: [20260220_070425_AlexeyDTC_msg2103_transcript.txt](../inbox/used/20260220_070425_AlexeyDTC_msg2103_transcript.txt)
[^4]: [20260220_070616_AlexeyDTC_msg2106_transcript.txt](../inbox/used/20260220_070616_AlexeyDTC_msg2106_transcript.txt)
[^5]: [20260225_210831_AlexeyDTC_msg2463_transcript.txt](../../inbox/used/20260225_210831_AlexeyDTC_msg2463_transcript.txt)
