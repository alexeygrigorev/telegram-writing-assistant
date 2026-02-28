---
title: "YouTube Shorts Automation"
created: 2026-02-28
updated: 2026-02-28
tags: [research, youtube, automation, shorts, video]
status: draft
---

# YouTube Shorts Automation

Research into how automated YouTube Shorts posting works, specifically looking at [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) as a reference implementation.

## What I Want to Understand

How to automate posting YouTube Shorts - what tools and APIs are involved, what are the technical approaches.

## MoneyPrinterV2 Overview

MoneyPrinterV2 (13k+ stars) is a Python application that automates YouTube Shorts creation and uploading. It has four main features: YouTube Shorts automation, a Twitter bot, affiliate marketing (Amazon + Twitter), and local business outreach. The Shorts feature is the most prominent - it generates short-form videos from scratch and uploads them to YouTube, with optional scheduling for recurring uploads.[^1]

## How It Generates Shorts

The video generation pipeline follows these steps:

1. Topic generation - uses g4f (GPT4Free, a free wrapper around various LLMs) to generate a topic from the channel's niche
2. Script generation - generates a short script (configurable sentence count, default 4 sentences) via LLM
3. Metadata generation - generates a title (under 100 chars, with hashtags) and description via LLM
4. Image prompt generation - generates AI image prompts from the script
5. Image generation - creates images using either G4F's SDXL Turbo (max 25 images) or a user-deployed Cloudflare Worker endpoint (both free-tier options)
6. Text-to-speech - converts the script to audio using CoquiTTS with the `tts_models/en/ljspeech/tacotron2-DDC_ph` model and univnet vocoder. Note: the TTS is English-only despite the configurable language setting, so non-English scripts produce poor results
7. Subtitle generation - uses AssemblyAI (requires paid API key) to transcribe the TTS audio back to SRT subtitles, equalized to max 10 characters per segment. Subtitles are rendered in yellow (#FFFF00) with black stroke, 100pt font
8. Video assembly - uses MoviePy to combine images (cropped to 1080x1920 portrait), TTS audio, background music (randomly chosen from downloaded songs, mixed at 10% volume), and burned-in subtitles into a final MP4

## How It Posts Shorts

The uploading mechanism is entirely browser automation via Selenium with Firefox. There is no YouTube Data API usage.

### Authentication

The user provides a path to a Firefox profile that is already logged into their YouTube account. Selenium launches Firefox using that profile, inheriting the existing YouTube session cookies. No OAuth tokens, API keys, or YouTube Data API credentials are needed.

### Upload Flow

1. Navigate to YouTube Studio and extract the channel ID from the redirected URL
2. Go to the upload page at youtube.com/upload
3. Find the custom `<ytcp-uploads-file-picker>` element, drill into its nested `<input>` tag, and inject the MP4 file path via `send_keys()`
4. Set the title by finding textbox elements and typing the AI-generated title
5. Set the description in the second textbox element
6. Set the "Made for Kids" radio button based on config
7. Click "Next" three times to navigate through the upload wizard (details, video elements, checks, visibility)
8. Set visibility by clicking the third radio button (Unlisted - hardcoded)
9. Click "Done" to publish
10. Navigate to the Shorts tab in YouTube Studio to retrieve the video URL from the most recent upload
11. Cache the result (title, description, URL, timestamp) to a local JSON file

### Scheduling

Uses the Python `schedule` library (not system cron). Options: once daily, or twice daily (10:00 and 16:00). A "thrice daily" option appears in the menu but is not actually implemented for YouTube (only works for Twitter). Each scheduled execution spawns a new Python subprocess, launches a new Firefox browser instance, generates a video from scratch, and uploads it. The main process must keep running for scheduled jobs to fire - it is not a true cron job.

## Key Observations

No official API usage - the project completely bypasses the YouTube Data API. This avoids quota limits and OAuth setup, but is fragile since it depends on YouTube Studio's DOM structure. Any UI change by YouTube could break the upload flow.

Firefox profile-based auth - rather than handling login programmatically (which would need 2FA, captchas, etc.), it requires the user to pre-authenticate in a Firefox profile. A pragmatic workaround.

Videos are always uploaded as Unlisted (hardcoded). The user would need to manually change visibility to Public or modify the source code.

A video qualifies as a YouTube Short by convention, not by API flag - it is rendered at 1080x1920 (9:16 portrait aspect ratio) and is short in duration. YouTube automatically categorizes portrait videos under 60 seconds as Shorts.

Timing-dependent automation - the upload flow uses hardcoded `time.sleep()` calls (2s, 5s, 10s) rather than explicit waits for elements. Susceptible to failures on slow connections.

g4f (GPT4Free) is used as the LLM backbone, making the project zero-cost to run (aside from AssemblyAI for subtitles).

The entire `upload_video()` method is wrapped in a bare `try/except` that catches all exceptions and returns `False`. If anything goes wrong during upload, the browser is quit and the method silently fails. There is no retry logic or error logging.

The background music is downloaded on first run from a ZIP file URL (default: a filebin.net link). The default URL is likely dead based on open issues, and the Songs.zip file may be corrupted.

## Practical Concerns

The project has significant dependency issues making it hard to set up today. Open GitHub issues report moviepy version incompatibilities, numpy conflicts, Firefox binary path loading failures, and empty AssemblyAI transcripts. YouTube accounts are stored in `.mp/youtube.json` as JSON with UUID-based account IDs, Firefox profile paths, niche/language settings, and upload history.

## Sources

[^1]: [20260228_163913_AlexeyDTC_msg2606.md](../../inbox/used/20260228_163913_AlexeyDTC_msg2606.md)
