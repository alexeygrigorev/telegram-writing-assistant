---
title: "Voice-Controlled Development Bot"
created: 2026-02-20
updated: 2026-02-20
tags: [telegram-bot, automation, idea, claude-code]
status: draft
---

# Voice-Controlled Development Bot

I really like this flow with Telegram - I record a voice message, it reacts and does something. I have been thinking about this for a while: I want a general-purpose bot that does anything I ask. For example, I want to create an issue in some repository - I would dictate the command and the bot would do it[^1].

## The Vision

I know there is OpenClaw or something like that, but I would be interested in building this myself and understanding how it works. I imagine a thing that I simply tell what to do, and it changes its own code and executes different commands. Like I say "I want this feature" and it goes and implements it, changing its own code[^1].

Security is a concern. It should not do anything harmful. If I run it in a Docker sandbox - I want to explore this - it would not be able to access any files outside its container. I could program by voice: record a Telegram message and it executes my commands[^1].

## Why This Matters

Ideas often come on the go, when I am not at a computer. I want to be able to do something with those ideas. With an interactive code session I could direct an agent, and if it does something wrong, I could correct it. With a Telegram bot the interaction is different - it executes, makes a commit, and then I can fix it. But that is fine[^1].

Right now with the website project, the orchestrator creates subagents that I cannot directly control, and it works well. If you set good constraints and control them, they do what is needed[^1].

## What Makes This Possible Now

This is still an idea. But I think after I finish the course, I will be able to build it. I now have everything I need:

- The tools and skills for AI-assisted development
- A server where all of this can run (no need to keep the laptop always on)
- Experience with multi-agent orchestration from the website project[^1]

## Sources

[^1]: [20260220_135246_AlexeyDTC_msg2144_transcript.txt](../inbox/used/20260220_135246_AlexeyDTC_msg2144_transcript.txt)
