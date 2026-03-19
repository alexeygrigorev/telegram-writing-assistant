---
title: "Useful Utilities I Built with Claude Code"
created: 2026-03-19
updated: 2026-03-19
tags: [claude-code, tools, python, utilities]
status: draft
---

# Useful Utilities I Built with Claude Code

A collection of utilities I created with AI coding assistants, mostly Claude Code. These are tools I use daily - practical things that solve real problems in my workflow.

## dirdotenv: Cross-Platform Environment Variable Management

GitHub: https://github.com/alexeygrigorev/dirdotenv

When working in a terminal, you need a way to automatically load environment variables when entering a directory. This is convenient for storing secrets like API keys for OpenAI and other providers.

The existing solution, direnv, is a shell extension that loads environment variables when you cd into a directory. But it only worked with its own `.envrc` format, while more and more projects use the simpler `.env` format - Docker Compose uses it, Visual Studio Code uses it, UV uses it.

I created dirdotenv - a Python-based alternative that works with both `.env` and `.envrc` formats and is cross-platform (Windows, Linux, macOS). It can be installed with uv and works anywhere Python is available.

I have multiple Windows computers, one of them a tablet with ARM64 architecture. With binaries, everything is very difficult on ARM64. But Python code is cross-platform - it runs everywhere. That is why I wrote dirdotenv in Python. All shells work well: bash, zsh, fish, and PowerShell.

It can also be used via uvx without any installation at all. I usually do `uv tool install dirdotenv` and that is it. I have already switched from direnv to dirdotenv on all my computers because it is more convenient. I can always customize it to my needs, unlike direnv.

dirdotenv was one of my very first experiments with Claude Code. I made it in December and wanted to understand what Claude Code can do. It was an interesting experience because I had never worked with bash hooks before. With Claude Code, I can try many things I never dealt with before - I can try things, look at them, and at least roughly understand how they work.

I have been actively using dirdotenv since December.

## SSH Auto Forward: Automatic Port Forwarding

GitHub: https://github.com/alexeygrigorev/ssh-auto-forward

I built an automatic SSH port forwarding tool with Claude Code. The tool connects to a remote machine via SSH, detects open ports, and automatically forwards them to localhost.

The need came from my remote development setup on Hetzner. I do everything on the remote server via VS Code Remote SSH. But when I need to access a web service running on the remote machine from my local browser, the firewall blocks all ports except SSH. VS Code handles this with automatic port forwarding, but I wanted the same thing in the terminal without VS Code.

I told Claude Code what I needed: connect via SSH, detect open ports, forward them to localhost. The implementation went through multiple iterations. I specified additional requirements as I used it - for example, forwarding to the same local port number if free, showing what process is running on each port, and displaying process names in the terminal tab.

The tool is published on PyPI. You just type `uvx ssh-auto-forward hetzner` and everything that is open on the remote machine becomes available in your local browser. It has an interactive TUI dashboard with port list, process names, and log panel. It auto-discovers listening ports, handles port conflicts by incrementing, and also supports CLI mode for non-interactive use.

The whole story of building it is longer - it all started because I needed to copy course documentation from my remote server to the Maven course platform. A long chain of requirements led to needing reliable port forwarding.

## Nobook: Plain Python Files as Jupyter Notebooks

GitHub: https://github.com/alexeygrigorev/nobook

I wanted Jupyter notebooks that use plain `.py` files instead of `.ipynb` JSON. The standard `.ipynb` format is a huge JSON file that is hard to read, hard to diff, and inconvenient for both humans and AI assistants.

The motivation: I want code in my documentation to come from Python files so I can cover them with tests. I need to be sure the code in course documentation always executes correctly, has no syntax errors, and produces output. When I update a library version, I want to catch breaking changes. I also want to run these notebooks interactively in Jupyter for my own experiments and easily include results in documentation.

Since I work with AI assistants, it is much more efficient for them to read and write plain Python files than JSON notebooks. With `.ipynb` files there is token overhead for reading and writing JSON.

The file format is simple - a plain `.py` file with `# @block=name` markers to split code into cells. Each block becomes a Jupyter cell. The architecture uses stock Jupyter - both the UI and the IPython kernel are unmodified. A custom `NobookContentsManager` intercepts file I/O, parsing block markers on read and converting back on save.

You can run blocks from the command line with `uv run nobook run example.py`. Output goes to `.out.py` with results inlined as comments. Since output and errors are plain comments, `.out.py` files are valid Python.

Users do not need to install anything - just run `uvx nobook` and Jupyter opens. Right-click a `.py` file and select "Open as Nobook." It includes a JupyterLab extension with a launcher card, context menu, and editable block name labels.

I built this in one evening using Claude Code with the latest Opus model. I spent about 1 hour checking, correcting, and giving feedback while working on other things in parallel.

## Microphone Booster: Windows Microphone Amplification

GitHub: https://github.com/alexeygrigorev/microboost

A Windows microphone booster built with OpenCode and GLM-5 using Tauri + Rust. It solves the problem of quiet USB-C microphones that the built-in Windows booster does not support.

At home I use regular headphones and the sound is okay. The built-in Windows microphone booster works with headphones plugged into the audio jack port, but does not boost as much as I would like. And it does not work at all with USB-C devices. When recording away from home with Apple earbuds (USB-C), the audio comes out too quiet.

I asked OpenCode with GLM-5 to implement it. I did not care about the technology, so it chose Rust with Tauri 2.0 and Svelte for the UI. It took three attempts to get it right. The first attempt produced a heavy app with a browser engine that completely forgot about the booster requirement. On the third attempt, it rewrote everything from scratch and it worked.

The app uses native Windows APIs. The best outcome is that I now know the Tauri + Rust technology stack and can use it to build GUI applications for Windows. These apps are self-contained - no libraries, no .NET, nothing else needed.

## Bot Master: Process Manager for Telegram Bots

GitHub: https://github.com/alexeygrigorev/bot-master

I built Bot Master to solve a simple problem: I have a bunch of Telegram bots running on my computer, and when one crashes, I do not notice. Bot Master monitors all the bots and automatically restarts any that go down.

It is a process manager with a Textual TUI. It runs as a background daemon that survives reboots via systemd. The daemon manages bot subprocesses, auto-restarts on crash with exponential backoff, and buffers logs in memory while writing to disk. The TUI client connects to the daemon to view live status, stream logs, and send start/stop/restart commands. If the TUI crashes, the bots keep running.

## Common Themes

All these utilities share several things in common:

- They solve real daily workflow problems, not hypothetical ones
- They were built with AI coding assistants (mostly Claude Code, one with OpenCode/GLM-5)
- They are published on GitHub and most are on PyPI
- They are written in Python (except the Microphone Booster which uses Rust/Tauri)
- The development time was minimal - usually an evening or a few sessions of checking in and giving feedback
- I learned new technologies in the process (bash hooks, SSH tunneling, Jupyter internals, Tauri/Rust, systemd daemons)

The pattern is consistent: I describe what I want, the AI builds it, I check and correct, and after a few iterations I have a working tool that I use daily. The key insight is that AI-assisted development lets me build tools in domains I have never worked in before - system programming, shell hooks, native Windows APIs - because the AI handles the implementation details while I focus on what I need the tool to do.

## Sources

[^1]: [20260319_184030_AlexeyDTC_msg3016_transcript.txt](../inbox/used/20260319_184030_AlexeyDTC_msg3016_transcript.txt)
[^2]: [dirdotenv article](ready-for-newsletter/dirdotenv.md)
[^3]: [SSH Auto Forward article](ready-for-newsletter/ssh-auto-forward.md)
[^4]: [Nobook article](ready-for-newsletter/nobook.md)
[^5]: [Microphone Booster article](ready-for-newsletter/microphone-booster-app.md)
[^6]: [Bot Master article](bot-master.md)
