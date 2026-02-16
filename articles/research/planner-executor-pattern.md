---
title: "Planner-Executor Pattern for AI Agents"
created: 2026-02-16
updated: 2026-02-16
tags: [research, ai-agents, patterns, claude-code]
status: draft
---

# Planner-Executor Pattern for AI Agents

Research on the planner-executor pattern: first you plan thoroughly, then you use code to execute each step separately with a fresh agent context.

## The Idea

The pattern is called planner-executor. First the planner creates a plan, then for each step you launch an agent from scratch, with a clean context. The idea is that each step of the plan fits into the context window[^1][^2].

This is a useful pattern. In the AI Engineering Buildcamp course (my course on Maven), I show students how to build their own coding agent using this setup: first a very good model creates a plan, then a weaker model can already write code. With a good plan, the model that takes longer to execute (and spends more tokens on context) handles it better[^2].

## Ralphex

[Ralphex](https://github.com/umputun/ralphex) is an extended Ralph loop for autonomous AI-driven plan execution with code review. It manages structured implementation plans using this planner-executor pattern[^1].

The idea behind Ralphex is appealing, but the implementation did not work so well in practice - the agent does things but without clear instructions it struggles[^1].

### Three-Phase Workflow

1. Planning phase - create implementation plans through dialogue with Claude. The AI explores the codebase, asks clarifying questions, and generates structured plans

2. Execution phase - Ralphex reads the plan and executes tasks sequentially, one at a time. Each task runs in a fresh Claude session to prevent context degradation. Automatic validation after each task (tests, linters). It marks checkboxes complete and commits changes after each task. Creates a feature branch from the plan name

3. Review phase - launches 5 specialized review agents in parallel via Claude Code's Task tool, covering quality assessment, implementation correctness, testing adequacy, over-engineering detection, and documentation completeness

### Key Architectural Decisions

Fresh session per task is the central design decision. Rather than running a single long Claude Code session, Ralphex launches a new process for each task iteration, each review iteration, and each external review evaluation. This prevents context window degradation and keeps the model sharp. State is communicated through the file system (plan file checkboxes, git commits) rather than through conversational context[^3].

Signal-based communication: Claude communicates its status back to Ralphex through special signal strings embedded in its output (like ALL_TASKS_DONE, TASK_FAILED, REVIEW_DONE). The Go code parses the streaming JSON output and detects these signals, allowing the outer orchestration loop to make decisions about flow control[^3].

Four-phase pipeline with iteration loops: Phase 1 (task execution loop), Phase 2 (first comprehensive code review with 5 parallel agents), Phase 3 (external review via Codex or custom tool), Phase 4 (second focused review with 2 agents). Each phase can iterate multiple times[^3].

Parallel review agents via Claude's Task tool: during code review, a single Claude session uses Claude Code's built-in Task tool to launch 5 sub-agents in parallel covering quality, implementation fidelity, testing, simplification, and documentation[^3].

No-commit detection for review convergence: the review loop captures the git HEAD hash before each Claude session and compares it after. If HEAD hasn't changed, Claude found nothing to fix and the loop terminates[^3].

### Key Advantages

- No context degradation - each task executes in a separate Claude session, maintaining fresh context throughout long feature implementations
- Atomic progress - commits after each completed task, so failed executions don't lose completed work
- Parallel review - multi-agent code review with specialized reviewers happens simultaneously
- Structured planning - unlike simple ralph loops that re-run the same prompt, Ralphex manages explicit structured plans
- Resumable - if interrupted mid-execution, completed tasks remain committed on the feature branch and re-running continues from the first incomplete task

### Technical Details

Written in Go. Uses Claude Code's `--output-format stream-json` for streaming output parsing. Supports Docker isolation for sandboxed execution. Configuration cascades: CLI flags > project-local config > global config > embedded defaults. Template-driven prompts with variable expansion and agent references[^3].

## Connection to Teaching

It is interesting how specifically this is implemented in this project. The pattern maps well to what I teach in AI Engineering Buildcamp - showing students how a good planner plus a weaker executor model can be more effective than one model doing everything[^2].

## Sources

[^1]: [20260216_094456_AlexeyDTC_msg1717.md](../inbox/used/20260216_094456_AlexeyDTC_msg1717.md)
[^2]: [20260216_094806_AlexeyDTC_msg1719_transcript.txt](../inbox/used/20260216_094806_AlexeyDTC_msg1719_transcript.txt)
[^3]: [Ralphex GitHub Repository](https://github.com/umputun/ralphex)
