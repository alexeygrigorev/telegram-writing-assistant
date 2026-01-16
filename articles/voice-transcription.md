---
title: "Voice Transcription with Grok"
created: 2026-01-16
updated: 2026-01-16
tags: [transcription, grok, whisper, voice]
status: draft
---

# Voice Transcription with Grok

Using Grok's Whisper implementation for fast voice message transcription.

## Performance

A one-minute voice message processes in 3-4 seconds. The transcription appears immediately after recording finishes. This is much faster than Telegram's built-in transcription feature.

## Implementation

Voice messages are sent to Grok API for transcription. The service uses Whisper for speech-to-text conversion. Currently using the free tier, which has been sufficient for all voice notes recorded so far.

## Benefits

No need to run Whisper locally. The API approach is faster and more convenient. No costs incurred yet on the free plan. May eventually need to upgrade to a paid tier as usage grows.

## Cleanup

Original .ogg audio files are deleted after transcription. Only the text transcript is kept to save storage space.

## Sources

- [20260116_210806_AlexeyDTC_transcript.txt](../inbox/raw/20260116_210806_AlexeyDTC_transcript.txt)
- [20260116_211410_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211410_AlexeyDTC_transcript.txt)
- [20260116_211501_AlexeyDTC_transcript.txt](../inbox/raw/20260116_211501_AlexeyDTC_transcript.txt)
