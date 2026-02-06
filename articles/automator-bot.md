---
title: "Automator Bot"
created: 2026-02-05
updated: 2026-02-05
tags: [slack, automation, bot, community-management]
status: draft
---

# Automator Bot

A Slack bot for community management that automates moderation tasks based on emoji reactions.

GitHub: https://github.com/alexeygrigorev/au-tomator-lambda

## How It Works

I leave emoji reactions on posts to trigger automated actions. For example:

- Promotional posts in General channel - moved or deleted with a warning message
- Course-related posts in General - moved to appropriate channel
- Rule violations - deleted with a DM to the user

## Debugging Incident

Recently, the bot stopped working correctly. Posts weren't being deleted from General, and messages weren't being sent to users. I was preparing for a family trip and didn't have time to debug manually.

I delegated the task to Claude Code, which:

1. Figured out how to retrieve logs from the bot
2. Analyzed the logs to find the error
3. Identified that I had accidentally deleted the API key
4. Guided me to update the key directly in AWS

The entire process happened without opening a browser or manually navigating the AWS console. This demonstrates how Claude Code excels at automation tasks where the focus is on executing actions rather than writing code.

### Claude
Claude Code is particularly useful for troubleshooting production issues when time is limited. I had a situation where the bot was failing for Slack reactions in the general channel. Normally, I would:
1. Go to CloudWatch
2. Check logs there
3. Try to understand what went wrong
4. Fix the issue based on the logs

Instead, I simply asked Claude Code to pull the logs from AWS for the last 2 hours and analyze what was happening. It:
1. Figured out how to retrieve the logs using AWS CLI
2. Found the stacktrace in the logs
3. Identified the error from the stacktrace
4. Fixed the error
5. Made a git commit and push
6. The deployment happened automatically on push

I was preparing for a trip and didn't have time to sit and debug. I just gave Claude Code the task and continued with my preparations while it handled everything. This type of automation - handling urgent maintenance tasks - is where Claude Code excels. Tools like Cursor, Antigravity, and Copilot are better suited for more thoughtful, interactive coding work[^6].


## Future Improvements

There is an unimplemented moderator folder feature for spam handling. When someone starts spamming, the bot would send a message with a button to:

- Delete all messages from that spammer
- Ban the spammer

Currently this requires manual action. The feature was implemented but never tested or deployed.

## Sources

- [20260205_122657_AlexeyDTC_msg937_transcript.txt](../inbox/used/20260205_122657_AlexeyDTC_msg937_transcript.txt)
- [20260205_123340_AlexeyDTC_msg939.md](../inbox/used/20260205_123340_AlexeyDTC_msg939.md) (GitHub link)
- [20260205_123340_AlexeyDTC_msg940_transcript.txt](../inbox/used/20260205_123340_AlexeyDTC_msg940_transcript.txt)
