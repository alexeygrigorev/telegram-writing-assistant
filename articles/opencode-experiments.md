---
title: "OpenCode Experiments with GLM-5"
created: 2026-02-13
updated: 2026-02-13
tags: [ai-assistants, opencode, glm-5]
status: draft
---

# OpenCode Experiments with GLM-5

Experimenting with OpenCode - an open-source AI coding assistant - using the new GLM-5 model from Z.AI.

## Getting Started with OpenCode

When I installed OpenCode, it just started working. I am not sure how or which API key it used. I asked it to use my Z.AI key - they recently released a new model (GLM-5) and I wanted to try it with OpenCode. I also heard good things about OpenCode - it has more features, so I wanted to try it[^1].

<figure>
  <img src="../assets/images/opencode-experiments/opencode-terminal-setup.jpg" alt="Terminal showing OpenCode setup with Z.AI API key configuration">
  <figcaption>Setting up OpenCode to use the Z.AI API key for GLM-5</figcaption>
  <!-- Screenshot of the initial terminal setup where the user configures OpenCode with the Z.AI key -->
</figure>

## Desktop App vs Terminal

I tried OpenCode first in terminal mode. I am not a fan of the terminal mode, neither in Claude Code nor in OpenCode. The desktop version is more convenient[^2].

The desktop mode in OpenCode is built on Visual Studio Code - it looks like a VS Code fork, adapted for AI coding. It is very convenient - I can open multiple projects and sessions at the same time[^3].

<figure>
  <img src="../assets/images/opencode-experiments/opencode-desktop-new-session.jpg" alt="OpenCode desktop app showing new session with project explorer and GLM-5 model">
  <figcaption>OpenCode desktop app - prefer this over terminal mode</figcaption>
  <!-- Shows the desktop interface with project directory, branch info, and GLM-5 model selector -->
</figure>

<figure>
  <img src="../assets/images/opencode-experiments/opencode-desktop-project-analysis.jpg" alt="OpenCode analyzing project structure by exploring README and configuration files">
  <figcaption>OpenCode analyzing the project - exploring codebase structure through key files</figcaption>
  <!-- Shows the thinking/planning mode where OpenCode explores the codebase before acting -->
</figure>

OpenCode has the usual two modes like other AI assistants - a planning mode and a build mode. I spent about an hour getting familiar with it. I noticed I needed a subagent feature but have not explored that yet[^3].

I was doing all this in the background while my main task was recording course videos. When Claude Code was doing something for the course - for example, updating document descriptions from transcripts for the Maven site - I would switch over and check what OpenCode was doing[^3].

I can also run OpenCode as a web service. My plan is to try this - with Claude Code it would require more effort to set up, but with OpenCode it works without problems[^3].

## Projects Built with OpenCode

I built two projects with OpenCode and GLM-5 to test the tool:

- [Microphone Booster App](microphone-booster-app.md) - a Windows microphone booster using Tauri + Rust
- [AI Engineer RPG Game](ai-engineer-rpg-game.md) - an RPG game for interview practice in Rust

Both were done in the background while I was recording course videos.

## Transferring Skills and Commands from Claude Code

It was very easy to transfer skills and commands from Claude Code to OpenCode. I added my code hooks and skills to the OpenCode configuration with an instruction to automatically sync them. Now all my hooks and skills from Claude Code are automatically duplicated into OpenCode too. They exist in both places. OpenCode does not read commands from Claude Code directly, so this automatic duplication is very convenient[^5][^6].

The commands are automatically added to the shared repository: https://github.com/alexeygrigorev/.claude[^6]

## Overall Impressions

My impression of OpenCode is positive. The desktop mode is great. As for GLM-5, it is decent but I do not really see a big difference from the previous GLM-4. All these agents cut corners and you need to watch them and set up proper processes. Right now I just used plain OpenCode with no custom processes set up. I think I need to set up proper workflows and then the results will be better[^4].

The testing challenge remains unsolved - I have no idea how to test desktop applications in any agent, not just OpenCode. I can extract core functionality into separate testable modules, but testing the UI is something I do not know how to do[^4].

## Sources

[^1]: [20260213_090850_AlexeyDTC_msg1591.md](../inbox/used/20260213_090850_AlexeyDTC_msg1591.md)
[^2]: [20260213_144434_AlexeyDTC_msg1606_transcript.txt](../inbox/used/20260213_144434_AlexeyDTC_msg1606_transcript.txt)
[^3]: [20260213_145200_AlexeyDTC_msg1607_transcript.txt](../inbox/used/20260213_145200_AlexeyDTC_msg1607_transcript.txt)
[^4]: [20260213_145555_AlexeyDTC_msg1608_transcript.txt](../inbox/used/20260213_145555_AlexeyDTC_msg1608_transcript.txt)
[^5]: [20260213_164644_AlexeyDTC_msg1633_transcript.txt](../inbox/used/20260213_164644_AlexeyDTC_msg1633_transcript.txt)
[^6]: [20260213_164714_AlexeyDTC_msg1635.md](../inbox/used/20260213_164714_AlexeyDTC_msg1635.md)
