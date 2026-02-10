---
title: "Spec-Driven Development and Task Management for AI Agents"
created: 2026-02-10
updated: 2026-02-10
tags: [research, claude-code, agents, task-management, spec-driven-development]
status: draft
---

# Spec-Driven Development and Task Management for AI Agents

Research into spec-driven development systems and task management patterns for AI coding agents like Claude Code. This article collects resources and patterns for keeping agents working until tasks are truly complete.

## What I Want to Understand

How context engineering and spec-driven development really work for agents and Claude. The goal is to build a bot I can control via Telegram with tighter integration to code, allowing me to give commands and correct behavior during active sessions[^1].

## Resources

### Get Shit Done (GSD)

[Get Shit Done](https://github.com/gsd-build/get-shit-done) is a lightweight meta-prompting and context engineering system for Claude Code, OpenCode, and Gemini CLI. It solves context rot through XML prompt formatting, subagent orchestration, and atomic git commits.

Key features:
- `/gsd:new-project` - Full initialization with questions, research, requirements, and roadmap
- `/gsd:plan-phase` - Research and planning with XML-structured task plans
- `/gsd:execute-phase` - Parallel execution with fresh context per task
- Context engineering via structured files (PROJECT.md, REQUIREMENTS.md, ROADMAP.md, STATE.md)

Philosophy: complexity is in the system, not in your workflow. Behind the scenes: context engineering, XML prompt formatting, subagent orchestration. What you see: a few commands that just work[^4].

### tmc-marketplace iterative-engineering

[iterative-engineering](https://github.com/tmchow/tmc-marketplace/tree/main/plugins/iterative-engineering) is a plugin for Claude Code with brainstorming, tech planning, multi-agent reviews, TDD implementation, and PR management.

The workflow:
1. Brainstorming - PRD creation with iterative review
2. Research - Parallel investigation of open questions
3. Tech Planning - Dependency-ordered subtasks with file paths and test scenarios
4. Implementing - Dependency-aware batch execution with code reviews
5. Wrapup - Test verification and PR creation

Each stage produces an artifact, offers iterative review, and hands off when ready[^5].

### FullStack-Agent Research

[Omar Sar's tweet](https://x.com/omarsar0/status/2020891961511809456) discusses FullStack-Agent, a multi-agent system for end-to-end full-stack web development with two key innovations: Development-Oriented Testing and Repository Back-Translation.

The system uses three specialized agents:
- Planning Agent - Generates structured frontend and backend designs in JSON
- Backend Coding Agent - Implements server logic with dedicated debugging tools
- Frontend Coding Agent - Builds UI against real backend APIs

Development-Oriented Testing validates code during generation, not after. Each agent gets real-time execution feedback, catching integration failures as they happen[^6].

### Taskmaster

[Taskmaster](https://github.com/blader/taskmaster) is a stop hook for Claude Code that prevents the agent from stopping prematurely. When the agent finishes a response and is about to stop, Taskmaster intercepts and prompts it to re-examine whether all work is truly done[^7].

The hook:
1. Scans recent transcript for incomplete tasks or errors
2. Prompts the agent to verify: original requests addressed, plan steps completed, tasks resolved, errors fixed
3. If work remains, the agent continues. If truly done, allows the stop

## Notes

Previously worked with stop hooks in the Ralph project, but it was quite useless - just "continue" and that's it. The goal is to make this more intelligent:

1. The system should look at messages from Claude and respond based on them
2. Instead of a simple task list like "continue improving", there should be something concrete
3. When an agent finishes one piece, it should take on the next, until everything is complete

This is the essence of proper task decomposition: tasks broken into pieces, where the agent completes one fragment then moves to the next, until all are done.

## Sources

[^1]: [20260209_220800_AlexeyDTC_msg1256.md](../inbox/raw/20260209_220800_AlexeyDTC_msg1256.md)
[^2]: [20260209_220915_AlexeyDTC_msg1257.md](../inbox/raw/20260209_220915_AlexeyDTC_msg1257.md)
[^3]: [20260209_221149_AlexeyDTC_msg1258.md](../inbox/raw/20260209_221149_AlexeyDTC_msg1258.md)
[^4]: [https://github.com/gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done)
[^5]: [https://github.com/tmchow/tmc-marketplace/tree/main/plugins/iterative-engineering](https://github.com/tmchow/tmc-marketplace/tree/main/plugins/iterative-engineering)
[^6]: [https://x.com/omarsar0/status/2020891961511809456](https://x.com/omarsar0/status/2020891961511809456)
[^7]: [20260210_082645_AlexeyDTC_msg1263.md](../inbox/raw/20260210_082645_AlexeyDTC_msg1263.md)
[^8]: [20260210_082759_AlexeyDTC_msg1264_transcript.txt](../inbox/raw/20260210_082759_AlexeyDTC_msg1264_transcript.txt)
[^9]: [20260210_082911_AlexeyDTC_msg1265.md](../inbox/raw/20260210_082911_AlexeyDTC_msg1265.md)
[^10]: [20260210_083048_AlexeyDTC_msg1266.md](../inbox/raw/20260210_083048_AlexeyDTC_msg1266.md)
[^11]: [https://github.com/blader/taskmaster](https://github.com/blader/taskmaster)
