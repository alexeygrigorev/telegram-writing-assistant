---
title: "Cross-Platform Environment Variable Management with dirdotenv"
created: 2026-01-23
updated: 2026-01-23
tags: [python, environment-variables, direnv, uv, tools]
status: draft
---

# Cross-Platform Environment Variable Management with dirdotenv

A Python-based alternative to direnv that works with both .env and .env.rc file formats.

## The Need for Environment Variable Management

When working in a terminal, you need a way to automatically load environment variables when entering a directory. This is convenient for storing secrets like API keys for OpenAI and other providers[^1].

## Existing Solution: direnv

direnv is a shell extension that loads environment variables when you cd into a directory. It requires a special format - variables must be declared in a file called `.env.rc`[^2].

However, many people now use a simpler `.env` format for declaring environment variables. direnv only worked with its own format.

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

During development, I tested on both Windows and Linux. All shells work well: bash, zsh, fish, and PowerShell[^7].

## Discovery: direnv Added .env Support

After building this project, I discovered that direnv recently added support for `.env` files too. So in some sense, this project wasn't strictly necessary. However, the Python-based implementation has advantages:
- Easy installation via `uv`
- Cross-platform compatibility
- Can run without installation
- Written in a language I'm comfortable with[^8]

## Source

https://github.com/alexeygrigorev/dirdotenv

## Sources

- [20260123_121409_valeriia_kuka_msg450.md](../inbox/raw/20260123_121409_valeriia_kuka_msg450.md)
- [20260123_121409_valeriia_kuka_msg451.md](../inbox/raw/20260123_121409_valeriia_kuka_msg451.md)
- [20260123_121409_valeriia_kuka_msg452_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg452_transcript.txt)
- [20260123_121409_valeriia_kuka_msg453_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg453_transcript.txt)
- [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg454_transcript.txt)
- [20260123_121409_valeriia_kuka_msg455_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg455_transcript.txt)

[^1]: [20260123_121409_valeriia_kuka_msg453_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg453_transcript.txt)
[^2]: [20260123_121409_valeriia_kuka_msg452_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg452_transcript.txt)
[^3]: [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg454_transcript.txt)
[^4]: [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg454_transcript.txt)
[^5]: [20260123_121409_valeriia_kuka_msg455_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg455_transcript.txt)
[^6]: [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg454_transcript.txt)
[^7]: [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg454_transcript.txt)
[^8]: [20260123_121409_valeriia_kuka_msg454_transcript.txt](../inbox/raw/20260123_121409_valeriia_kuka_msg454_transcript.txt)
