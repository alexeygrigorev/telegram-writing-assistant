---
title: "Bot Master: Process Manager for Telegram Bots"
created: 2026-03-16
updated: 2026-03-16
tags: [tools, telegram, bots, process-management]
status: draft
---

# Bot Master: Process Manager for Telegram Bots

[GitHub: alexeygrigorev/bot-master](https://github.com/alexeygrigorev/bot-master)

I built a new tool called Bot Master. The problem: I have a bunch of bots running on my computer, and when one of them crashes, I do not notice. So I made a tool that monitors all the bots and automatically restarts any that go down[^1].

I launched the Telegram bots through this tool, so now I am checking whether everything works correctly[^1].

Bot Master is a process manager with a Textual TUI. It runs as a background daemon that survives reboots via systemd. The daemon manages bot subprocesses, auto-restarts on crash with exponential backoff, and buffers logs in memory while writing to disk. The TUI client connects to the daemon to view live status, stream logs, and send start/stop/restart commands. If the TUI crashes, bots keep running[^2].

## Sources

[^1]: [20260316_141656_AlexeyDTC_msg2968_transcript.txt](../inbox/used/20260316_141656_AlexeyDTC_msg2968_transcript.txt)
[^2]: [20260316_141908_AlexeyDTC_msg2970.md](../inbox/used/20260316_141908_AlexeyDTC_msg2970.md)
