---
title: "Zoland Talk"
created: 2026-03-14
updated: 2026-03-14
tags: [talk, zoland, claude-code, slides, telegram-assistant]
status: draft
---

# Zoland Talk

A talk at the Zoland meetup about the Telegram writing assistant and code agents - skills and subagents. The full talk content is in a separate article: [Building Blocks of Modern Code Agents](talks/code-agents-building-blocks.md).

## What the Talk Was About

The talk covered the building blocks of modern code agents: reusable skills and role-based subagents. The Telegram writing assistant was used as the running example throughout. The talk was about 20 minutes with a 10-minute Q&A[^1].

The key topics:

- Overview of coding assistant categories (chat-based, IDE, CLI, project bootstrappers)
- Skills and commands as reusable workflows
- Subagents for isolating context-heavy work
- The Telegram writing assistant as a practical demonstration
- How to create and iterate on skills through real usage

## Preparing for the Talk

To prepare for this talk, the Telegram assistant itself was used. The process was[^1]:

1. Dictated ideas into the Telegram assistant as voice messages
2. Opened an interactive Claude Code session and told it what to work with from those ideas
3. Told Claude to make slides. It created slides using reveal.js
4. Reviewed the slides and gave feedback, iterating until they were right

This was the first time using Claude Code to create slides, and the process worked well enough to become the standard approach[^1].

## Slides Workflow for All Workshops

After the Zoland talk, this approach is now used for all workshops, including the AI Engineering workshops. The time spent on slides keeps decreasing with each iteration. The first time took a long time, but now it takes less and less because there are previous examples to reference. The workflow is: tell Claude what should be on the slides, it creates them, iterate on feedback until the result is right[^1].

Things like organizing content, deciding layout, and figuring out where to place elements - all of that is now handled by Claude. Just describe what you want to see, and iterate. Each time there are more examples to point to and say "do it like last time"[^1].

## Existing Content

The detailed talk content with all slides, code examples, and speaker notes is documented in [Building Blocks of Modern Code Agents](talks/code-agents-building-blocks.md). That article includes[^2]:

- The talk prep process (about an hour total)
- Screenshots of the slides
- Photos from the meetup
- The full content about skills and subagents

The slides were shared previously but are not currently in this repository. If they need to be found, check Telegram history or the reveal.js output from the Claude Code session[^1].

## The Telegram Writing Assistant

The talk featured the Telegram writing assistant as the main example. The bot handles everything except video download. It processes text, voice messages, photos, URLs, and YouTube transcripts[^1].

Illustrations from the talk slides could be used in the [Telegram Writing Assistant Updates](ready-for-newsletter/telegram-writing-assistant-updates.md) article. If suggestions are needed for where to add illustrations, the slides from this talk are a good source[^1].

## Sources

[^1]: [20260314_065251_AlexeyDTC_msg2906_transcript.txt](../inbox/used/20260314_065251_AlexeyDTC_msg2906_transcript.txt)
[^2]: [20260314_065332_AlexeyDTC_msg2908_transcript.txt](../inbox/used/20260314_065332_AlexeyDTC_msg2908_transcript.txt)
