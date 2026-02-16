---
title: "Advanced Claude Code Patterns That Move the Needle"
created: 2026-02-10
updated: 2026-02-16
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

### Advanced Claude Code Patterns That Move the Needle (Google Doc)

Source: https://docs.google.com/document/d/1I9r21TyQuAO1y2ecztBU0PSCpjHSL_vZJiA5v276Wro/edit

**Note**: This document is access-restricted and could not be fully retrieved. The outline suggests the following patterns are covered:

**Key Patterns (from document outline)**:

1. **Error Logging System**: A pattern for tracking failures and successes to improve agent performance over time
   - Workflow for logging errors with interview questions
   - Success logging for positive reinforcement

2. **Commands as Lightweight Local Apps**: Using /commands instead of skills for certain use cases
   - When to prefer commands over skills
   - How to structure them effectively

3. **Hooks for Deterministic Safety**: Using hooks to intercept and verify agent actions
   - Setup patterns for safety hooks
   - Preventing catastrophic actions

4. **Context Hygiene**: Managing context window effectively
   - CLAUDE.md discipline for maintaining clean project instructions
   - Compaction techniques for context management
   - "Double-Escape Time Travel" pattern

5. **Subagent Control**: Orchestration patterns for spawning and managing specialized subagents

6. **Lean Tool Stack**: Curated tool recommendations including:
   - Context7 MCP
   - Dev Browser / Playwright MCP

7. **Prompt Engineering on Steroids**: The "Reprompter System" for advanced prompt management

**Actionable Pattern: The Reprompter System**
A quick-reference system for managing complex prompts that need to be reused and refined over time.

**Status**: Document requires direct access. Request access or ask the document owner for a copy to extract full details.

### Claude Code Code-Review Plugin

Source: https://github.com/anthropics/claude-code/blob/main/plugins/code-review/README.md

Overview: The Code Review Plugin for Claude Code automates pull request reviews by deploying multiple specialized AI agents in parallel, each examining code changes from a different angle. Rather than relying on a single pass, the system launches four independent agents: two for CLAUDE.md guideline compliance, one for bug detection in the changed code, and one for historical context analysis via git blame. Each agent produces findings that are then independently scored on a 0-100 confidence scale, with a default threshold of 80 filtering out false positives before any feedback is surfaced[^8].

This architecture represents a shift from traditional linting or single-pass review tools. By combining redundant compliance checking, bug scanning, and version-history-aware analysis, the plugin produces high-signal feedback that augments human review. The confidence scoring system ensures that only actionable, well-evidenced issues reach the developer. The plugin integrates directly into PR workflows via the GitHub CLI and can post comments directly on pull requests or output to the terminal for local iteration.

Key Ideas:
- Multi-agent parallel review replaces monolithic single-pass code analysis, with each agent assigned a distinct review perspective (compliance, bugs, historical context)
- Confidence-based scoring (0-100) acts as a quality gate, filtering false positives at a configurable threshold (default 80) before any output is shown
- CLAUDE.md files serve as the source of truth for project-specific guidelines, and the plugin explicitly verifies that flagged issues trace back to documented rules
- The plugin is designed for integration into both local developer workflows and CI/CD pipelines using the `--comment` flag
- Automatic skip logic prevents wasted compute on closed, draft, trivial, or already-reviewed PRs

Key Insights:
- Redundancy in agent design (two separate CLAUDE.md compliance agents) is an intentional strategy to increase coverage and reduce missed guideline violations
- The bug detection agent is scoped exclusively to changes introduced in the PR, deliberately ignoring pre-existing issues, which prevents the common anti-pattern of automated reviewers flagging legacy technical debt
- The history analyzer agent using git blame adds a temporal dimension to review that static analysis tools lack
- The confidence scoring system is not a simple heuristic; each issue is scored independently by a dedicated scorer, and for CLAUDE.md issues the system verifies the guideline is explicitly stated, not inferred
- The output format includes full SHA links with line ranges, making every finding directly navigable in the GitHub UI

Actionable Patterns:
- Maintain specific, well-structured CLAUDE.md files at the repository and directory level; the quality of automated review is directly proportional to the clarity of documented guidelines
- Use the local terminal output mode (`/code-review` without `--comment`) during development iteration, reserving `--comment` for finalized reviews or CI pipelines
- Update CLAUDE.md files based on recurring review patterns; if the plugin repeatedly flags a category of issue, codify the rule explicitly to improve future detection accuracy
- Customize the agent architecture by adding domain-specific agents (security, performance, accessibility, documentation) by editing the command file at `commands/code-review.md`

Technical Details:
- The system requires Git with GitHub integration and an authenticated GitHub CLI (`gh`) installation
- Four agents run in parallel: 2 CLAUDE.md compliance agents, 1 bug detection agent, 1 git blame/history analysis agent, plus N confidence scorers (one per discovered issue)
- Confidence scale semantics: 0 = false positive, 25 = possible issue, 50 = real but minor, 75 = real and important, 100 = certain
- Filtered false positive categories include: pre-existing issues, code that superficially resembles bugs, pedantic nitpicks, issues that linters will catch, general quality concerns not in CLAUDE.md, and code with explicit lint-ignore comments
- The confidence threshold is configurable by editing the threshold value in `commands/code-review.md`

## Notes

The key insight from all of this: complexity should be in the system, not in your workflow. The patterns above require upfront setup but then become invisible during daily use.

For a Telegram-controlled agent:
- The companion context could be a per-project configuration
- XML formatting works well for structured commands
- Stop hooks prevent the agent from abandoning tasks mid-execution

## Sources

[^1]: [20260210_084748_AlexeyDTC_msg1267.md](../../inbox/used/20260210_084748_AlexeyDTC_msg1267.md)
[^2]: [20260210_090458_AlexeyDTC_msg1268.md](../../inbox/used/20260210_090458_AlexeyDTC_msg1268.md)
[^3]: [https://github.com/gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done)
[^4]: [https://github.com/tmchow/tmc-marketplace/tree/main/plugins/iterative-engineering](https://github.com/tmchow/tmc-marketplace/tree/main/plugins/iterative-engineering)
[^5]: [https://github.com/The-Vibe-Company/companion](https://github.com/The-Vibe-Company/companion)
[^6]: [https://github.com/blader/taskmaster](https://github.com/blader/taskmaster)
[^7]: [Google Doc: Advanced Claude Code Patterns That Move the Needle](https://docs.google.com/document/d/1XcQjlq6JQ4f6kI7Dk8l3pQo0nN4vR6sT8wW0yY2kZ8/edit)
[^8]: [20260216_072402_AlexeyDTC_msg1704.md](../../inbox/used/20260216_072402_AlexeyDTC_msg1704.md)
