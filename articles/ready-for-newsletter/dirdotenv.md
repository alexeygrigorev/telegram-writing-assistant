---
title: "Cross-Platform Environment Variable Management with dirdotenv"
created: 2026-01-23
updated: 2026-03-13
tags: [python, environment-variables, direnv, uv, tools]
status: draft
---

# Cross-Platform Environment Variable Management with dirdotenv

A Python-based alternative to direnv that works with both .env and .env.rc file formats.

## The Need for Environment Variable Management

When working in a terminal, you need a way to automatically load environment variables when entering a directory. This is convenient for storing secrets like API keys for OpenAI and other providers[^1].

## Existing Solution: direnv

direnv is a shell extension that loads environment variables when you cd into a directory. It requires a special format - variables must be declared in a file called `.env.rc`[^2].

However, more and more projects use a simpler `.env` format for declaring environment variables. Docker Compose uses it, Visual Studio Code uses it, UV uses it. direnv only worked with its own `.envrc` format.

## The dirdotenv Solution

I created a Python-based alternative to direnv that:
- Works with both `.env` and `.env.rc` formats
- Is cross-platform (works on Windows, Linux, macOS)
- Can be installed easily with uv
- Works anywhere Python is available[^3]

## Building with GitHub Copilot

I used GitHub Copilot's "Jumpstart your project" feature to create this project. When creating a new repository on GitHub, there's an option to describe your project in 500 characters, and Copilot generates the initial code[^4].

I went through several iterations:
1. Initial generation via Copilot on GitHub
2. Further development using Copilot and Antigravity
3. Adding tests - I discovered that tox can run tests on Windows via PowerShell, which was new to me
4. Ensuring cross-platform compatibility[^5]

## Cross-Platform Benefits

The main advantage over direnv is that it works everywhere Python runs. This is particularly important for:
- Windows users (direnv can be problematic, especially on ARM)
- Tablets and other non-standard platforms
- Users who prefer simple `uv` installation[^6]

I have multiple Windows computers, one of them a tablet with ARM64 architecture. With binaries, everything is very difficult on ARM64. But Python code is cross-platform - it runs everywhere. That is why I wanted to write dirdotenv in Python[^9].

During development, I tested on both Windows and Linux. All shells work well: bash, zsh, fish, and PowerShell[^7].

It can also be used via uvx without any installation at all. I usually do `pip install` or `uv tool install dirdotenv` and that is it. I have already switched from direnv to dirdotenv on all my computers because it is more convenient. I can always customize it to my needs, unlike direnv. And it does not need to be compiled - the code is in Python, which for me is an advantage[^9].

## Discovery: direnv Added .env Support

After building this project, I discovered that direnv recently added support for `.env` files too. So in some sense, this project wasn't strictly necessary. However, the Python-based implementation has advantages:
- Easy installation via `uv`
- Cross-platform compatibility
- Can run without installation
- Written in a language I'm comfortable with[^8]

## One of My First Claude Code Experiments

dirdotenv was one of my very first experiments with Claude Code. I made it in December and wanted to understand what Claude Code can do and what it cannot. I was impressed[^10].

It was an interesting experience because I had never worked with bash hooks before. With Claude Code, I can try many things I never dealt with before. I can now try things, look at them, and at least roughly understand how they work. Not in depth, but at least get a general idea of what is possible[^10].

I have been actively using dirdotenv since December when I made it. It works as expected[^10].

## Source

https://github.com/alexeygrigorev/dirdotenv

## Sources

- [20260123_121409_valeriia_kuka_msg450.md](../inbox/used/20260123_121409_valeriia_kuka_msg450.md)
- [20260123_121409_valeriia_kuka_msg451.md](../inbox/used/20260123_121409_valeriia_kuka_msg451.md)
- [20260123_121409_valeriia_kuka_msg452_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg452_transcript.txt)
- [20260123_121409_valeriia_kuka_msg453_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg453_transcript.txt)
- [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg454_transcript.txt)
- [20260123_121409_valeriia_kuka_msg455_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg455_transcript.txt)

[^1]: [20260123_121409_valeriia_kuka_msg453_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg453_transcript.txt)
[^2]: [20260123_121409_valeriia_kuka_msg452_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg452_transcript.txt)
[^3]: [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg454_transcript.txt)
[^4]: [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg454_transcript.txt)
[^5]: [20260123_121409_valeriia_kuka_msg455_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg455_transcript.txt)
[^6]: [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg454_transcript.txt)
[^7]: [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg454_transcript.txt)
[^8]: [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/used/20260123_121409_valeriia_kuka_msg454_transcript.txt)
[^9]: [20260313_145539_AlexeyDTC_msg2890_transcript.txt](../inbox/used/20260313_145539_AlexeyDTC_msg2890_transcript.txt)
[^10]: [20260313_150043_AlexeyDTC_msg2892_transcript.txt](../inbox/used/20260313_150043_AlexeyDTC_msg2892_transcript.txt)
