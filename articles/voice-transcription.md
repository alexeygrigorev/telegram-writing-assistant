---
title: "Voice Transcription with Grok"
created: 2026-01-16
updated: 2026-01-16
tags: [transcription, grok, whisper, voice]
status: draft
---

# Voice Transcription with Grok

Using Grok for voice message transcription has been surprisingly fast and effective.

## Performance

A one-minute voice message processes in just 3-4 seconds. The transcript appears immediately after finishing recording. This is much faster than Telegram's built-in transcription feature.

## Implementation

The bot sends audio to Grok which uses Whisper for transcription. The free tier has been sufficient so far. No need to run Whisper locally.

## Response Time

The speed is impressive. As soon as a voice message is recorded, the transcription is visible in the chat. This immediate feedback makes the workflow seamless.

## Sources
- [20260116_210806_AlexeyDTC_transcript.txt](../inbox/raw/20260116_210806_AlexeyDTC_transcript.txt)
- [20260116_211410_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211410_AlexeyDTC_transcript.txt)
