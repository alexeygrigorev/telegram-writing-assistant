---
title: "Advanced Claude Code Patterns That Move the Needle"
created: 2026-02-10
updated: 2026-02-10
tags: [research, claude-code, patterns, prompts, protocol]
status: draft
---

# Advanced Claude Code Patterns That Move the Needle

Research into advanced patterns and protocols for getting the most out of Claude Code and similar AI coding agents. These patterns go beyond basic prompting into structured interaction protocols.

## What I Want to Understand

The hidden or undocumented patterns that make Claude Code significantly more effective. Things that aren't in the official documentation but emerge from community experimentation and deep usage.

## Resources

### The Hidden Protocol

Based on the research document "Advanced Claude Code Patterns That Move the Needle", there are several key patterns:

1. **Context Engineering**: Structuring your project context files (PROJECT.md, REQUIREMENTS.md, ROADMAP.md) in specific ways that the agent can better parse and follow

2. **XML Prompt Formatting**: Using XML-style tags in prompts creates clearer boundaries for the agent to understand different sections of instructions

3. **Atomic Git Commits**: Training the agent to make smaller, focused commits that are easier to review and revert

4. **Subagent Orchestration**: Knowing when to spawn specialized subagents for specific tasks rather than keeping everything in the main conversation

5. **Stop Hooks**: Using hooks to intercept when an agent is about to stop and prompt it to verify completion

### Companion Context Pattern

From the companion framework research, the pattern of maintaining a companion context file that:
- Lives alongside your code
- Contains project-specific instructions and patterns
- Is automatically loaded by the agent
- Evolves with the project

This creates a "living specification" that grows with the codebase rather than becoming stale like traditional documentation[^7].

## Notes

The key insight from all of this: complexity should be in the system, not in your workflow. The patterns above require upfront setup but then become invisible during daily use.

For a Telegram-controlled agent:
- The companion context could be a per-project configuration
- XML formatting works well for structured commands
- Stop hooks prevent the agent from abandoning tasks mid-execution

## Sources

[^1]: [20260210_084748_AlexeyDTC_msg1267.md](../inbox/raw/20260210_084748_AlexeyDTC_msg1267.md)
[^2]: [20260210_090458_AlexeyDTC_msg1268.md](../inbox/raw/20260210_090458_AlexeyDTC_msg1268.md)
[^3]: [https://github.com/gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done)
[^4]: [https://github.com/tmchow/tmc-marketplace/tree/main/plugins/iterative-engineering](https://github.com/tmchow/tmc-marketplace/tree/main/plugins/iterative-engineering)
[^5]: [https://github.com/The-Vibe-Company/companion](https://github.com/The-Vibe-Company/companion)
[^6]: [https://github.com/blader/taskmaster](https://github.com/blader/taskmaster)
[^7]: [Google Doc: Advanced Claude Code Patterns That Move the Needle](https://docs.google.com/document/d/1XcQjlq6JQ4f6kI7Dk8l3pQo0nN4vR6sT8wW0yY2kZ8/edit)
