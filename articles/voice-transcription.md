---
title: "Voice Transcription with Grok"
created: 2026-01-16
updated: 2026-01-16
tags: [transcription, grok, whisper, voice, telegram]
status: draft
---

# Voice Transcription with Grok

Using Grok's Whisper implementation for fast voice message transcription.

## Transcription Speed

I just added a function for the bot that outputs everything I say into the chat immediately, that is, it outputs the transcript to the chat. Transcription is done using Grok, and I'm surprised at how fast it is. I only finish recording a message and immediately see the transcript.

I just recorded a message a whole minute long, it was processed in 3-4 seconds. I just recorded it and immediately see the transcript. Telegram's built-in transcription works slowly. I'm very impressed at how fast and well the transcript from Whisper works.

## Cost

I'm using Grok for transcription. It's very cool. So far, everything is free, I don't pay anything for it. I don't need to run Whisper locally myself. That would, of course, take longer and not be as cool. I just send a request to Grok, and so far the free plan is sufficient. I don't know, I might eventually exceed the free tier, but for all the voice messages I've recorded so far, they were all transcribed for free.

## File Handling

The .ogg files themselves should not be stored. We should only keep the transcript itself. We received the file, sent it to Whisper, made the transcription, and removed the .ogg file.

## Sources
- [20260116_210806_AlexeyDTC_transcript.txt](../inbox/raw/20260116_210806_AlexeyDTC_transcript.txt)
- [20260116_211410_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211410_AlexeyDTC_transcript.txt)
- [20260116_211501_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211501_AlexeyDTC_transcript.txt)
