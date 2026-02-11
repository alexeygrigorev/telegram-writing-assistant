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

Source: https://github.com/gsd-build/get-shit-done

Overview: GSD is a lightweight meta-prompting and context engineering system for Claude Code, OpenCode, and Gemini CLI that specifically solves context rot, which is the quality degradation that happens as Claude fills its context window. The tool provides a complete spec-driven development workflow through simple slash commands while hiding complex orchestration behind the scenes.

Key Ideas:
- GSD targets solo developers who want AI to write code without pretending to run a 50-person engineering organization with sprint ceremonies, story points, and Jira workflows
- Context rot is the core problem: as Claude's context window fills, response quality degrades, so GSD uses fresh context windows for each task via subagent orchestration
- The system creates structured documentation artifacts (PROJECT.md, REQUIREMENTS.md, ROADMAP.md, STATE.md, CONTEXT.md) that keep project state and decisions accessible
- Installation is a single npx command with options for runtime (Claude Code, OpenCode, Gemini) and scope (global or local project)
- The recommended workflow skips permissions mode with `claude --dangerously-skip-permissions` since stopping to approve basic commands defeats the purpose of AI automation

Key Insights:
- The complexity lives in the system, not the user workflow: behind the scenes there's context engineering, XML prompt formatting, subagent orchestration, and state management, but the user only sees simple commands
- Existing codebases should first be mapped with `/gsd:map-codebase` which spawns parallel agents to analyze stack, architecture, conventions, and concerns before planning new work
- GSD uses a thin orchestrator pattern: the main context stays light (30-40%) while heavy work happens in fresh subagent contexts, keeping the session responsive
- Atomic commits per task enable git bisect to find exact failing commits, make each task independently revertable, and provide clear history for future AI sessions
- For brownfield projects, the mapping phase is critical because it lets the system understand existing patterns so new work follows established conventions

Actionable Patterns:
- The discuss phase before planning: `/gsd:discuss-phase` captures implementation preferences (visual layouts, API response formats, content structure) so research and planning are guided by actual user decisions rather than assumptions
- Phase-based execution loop: discuss (capture decisions), plan (research + verify plans), execute (parallel waves with fresh context), verify (user acceptance testing) - repeat until milestone complete
- Quick mode for ad-hoc tasks: `/gsd:quick` provides GSD guarantees (atomic commits, state tracking) without full planning overhead, ideal for bug fixes and small features
- The XML task structure specifies files, actions, verification steps, and done conditions in a format optimized for Claude to understand without ambiguity

Technical Details:
- Install with `npx get-shit-done-cc@latest` and verify with `/gsd:help` inside the chosen runtime
- Core workflow commands: `/gsd:new-project`, `/gsd:discuss-phase [N]`, `/gsd:plan-phase [N]`, `/gsd:execute-phase <N>`, `/gsd:verify-work [N]`
- Configuration lives in `.planning/config.json` with settings for mode (yolo/interactive), depth (quick/standard/comprehensive), and model profiles (quality/balanced/budget)
- Model profiles control which Claude model each agent uses: quality profile uses Opus for planning and execution, balanced uses Opus for planning and Sonnet for execution, budget uses Sonnet throughout
- XML task format includes type, name, files, action instructions, verification commands, and done conditions for each atomic task
- The system creates structured artifacts: PROJECT.md (vision), REQUIREMENTS.md (v1/v2 scope), ROADMAP.md (phases), STATE.md (decisions and blockers), CONTEXT.md (implementation preferences), PLAN.md (atomic tasks), SUMMARY.md (what changed)
- Git branching strategies include none (commits to current branch), phase (branch per phase), and milestone (one branch for entire milestone)
- Workflow agents can be toggled: research (domain investigation before planning), plan_check (verifies plans achieve goals), verifier (confirms delivery after execution)

Quotes:
- "If you know clearly what you want, this WILL build it for you. No bs."
- "The complexity is in the system, not in your workflow. Behind the scenes: context engineering, XML prompt formatting, subagent orchestration, state management. What you see: a few commands that just work."
- "Each task gets its own commit immediately after completion" - enabling git bisect to find exact failing tasks and independent reversion of any piece of work

### tmc-marketplace iterative-engineering

Source: https://github.com/tmchow/tmc-marketplace/tree/main/plugins/iterative-engineering

Overview: A comprehensive plugin for Claude Code and Codex that implements a full iterative development workflow with brainstorming, technical planning, multi-agent reviews, TDD implementation, and PR management. It provides opinionated defaults while keeping user choice at the center of every decision point.

Key Ideas:
- Planning pays dividends - the workflow enforces planning before coding to avoid slower rush-to-code approaches
- Each skill works standalone - you can run `/code-review` independently or `/iterative:brainstorming` mid-implementation
- PRD is a living document - tech planning and implementation update it when they encounter new constraints
- Dependency-aware batching - subtasks run concurrently within batches, but batches execute sequentially to respect ordering
- Severity-based fix acceptance - users pick which severity levels to address, not all-or-nothing review feedback
- Agent teams with cross-validation - specialized reviewers can push back on each other (e.g., YAGNI reviewer challenging completeness suggestions)

Key Insights:
- Stage boundaries are explicit: brainstorming produces PRDs with high-level technical direction but NOT implementation details; tech planning describes what and where but NOT how (no pre-written method bodies); implementing produces code and PRs
- Requirements are prioritized (Core / Must-Have / Nice-to-Have / Out) rather than flat, driving implementation scope decisions
- Open questions from PRDs are classified by resolution method: research questions get parallel investigation, experiential questions get spiked via throwaway prototypes
- Large plan sections (6+ subtasks) get automatic incremental reviews between batches to catch issues before later code builds on flawed foundations
- External model CLIs (Gemini, Codex, Claude) can provide independent perspectives in full review mode, with the orchestrator self-identifying and skipping its own model family

Actionable Patterns:
- PRD structure: requirements grouped by priority, scope splits (In Scope vs Boundaries), open questions tagged by what they affect
- Tech plan structure: architecture decisions, query strategies, file paths, concrete test scenarios with specific inputs and expected outputs
- Spike pattern: build in isolated worktrees, build-present-feedback loop, decisions persist in PRD but code is throwaway
- Git worktree isolation for spikes and implementation branches
- Branch safety gate before first commit prevents accidental commits to default branch

Technical Details:
- Installation: `/plugin marketplace add tmchow/tmc-marketplace` then `/plugin install iterative-engineering@tmc-marketplace`
- Core workflow skills use `iterative:` prefix to avoid naming collisions
- Plan reviewers: clarity, completeness, specificity, YAGNI (4 agents)
- Code reviewers: correctness, security, performance, simplicity, testing (5 agents)
- Task workers run as isolated subagents, each with its own context window containing just its subtask
- Docs committed at every checkpoint - PRDs, plans, and spike docs are never left as uncommitted changes

Quotes:
- "Planning pays off - Rushing to code is often slower than planning first"
- "Tech plan describes what, not how - Plans capture architecture, query strategies, and test scenarios. They don't pre-write method bodies - that's brittle and gets followed blindly"
- "Iteration improves quality - A review after a review can still find improvements"

### FullStack-Agent Research

Source: https://x.com/omarsar0/status/2020891961511809456

Overview: FullStack-Agent is a multi-agent system designed for end-to-end full-stack web development, addressing the gap between generating simple frontends and shipping complete working applications with functional backends, databases, and APIs. The paper introduces two key innovations: Development-Oriented Testing and Repository Back-Translation.

Key Ideas:
- Most AI coding agents default to mock data, fake endpoints, and frontend-only implementations, but real-world web development requires all three layers (frontend, backend, database) working together
- The bottleneck in AI-assisted web development is not frontend generation but building functional backends and databases that integrate properly
- FullStack-Agent uses three specialized agents: a Planning Agent for structured JSON designs, a Backend Coding Agent with HTTP debugging tools, and a Frontend Coding Agent that builds against real APIs
- The system achieved 64.7% frontend accuracy, 77.8% backend accuracy, and 77.9% database accuracy on FullStack-Bench (647 frontend, 604 backend, 389 database test cases)
- This represents improvements of 8.7%, 38.2%, and 15.9% respectively over the strongest baseline

Key Insights:
- Development-Oriented Testing validates code during generation rather than after, providing real-time execution feedback that catches integration failures as they happen
- Repository Back-Translation solves the training data problem by having an information-gathering agent read real open-source repositories and extract development patterns
- A trajectory agent reproduces repositories from scratch given only extracted plans, generating high-quality training examples grounded in real codebases
- After training a Qwen3-Coder-30B model on 2K crawled and 8K augmented trajectories, frontend accuracy improved by 9.7% and backend accuracy by 9.5% in just two rounds
- The multi-agent architecture allows each agent to specialize while maintaining integration through shared planning and testing infrastructure

Actionable Patterns:
- Separate planning from implementation with a dedicated Planning Agent that generates structured designs
- Validate during generation, not after - integrate testing tools directly into coding agents
- Use real-world repositories as training data by extracting plans and reproducing them from scratch
- Give frontend agents tools to monitor terminal and browser console errors dynamically
- Give backend agents HTTP request tools to validate API responses during development

Technical Details:
- Planning Agent outputs structured JSON designs for both frontend and backend
- Backend Coding Agent has a dedicated debugging tool that sends HTTP requests and validates responses
- Frontend Coding Agent includes a tool that monitors terminal and browser console errors dynamically
- FullStack-Bench provides comprehensive test coverage across three layers
- Training approach: 2K crawled trajectories + 8K augmented trajectories from Repository Back-Translation

Quotes:
- "The gap between generating a landing page and shipping a working app with a functional backend, database, and API layer remains wide."
- "Development-Oriented Testing validates code during generation, not after."
- "The bottleneck in AI-assisted web development isn't frontend generation. It's building functional backends and databases that actually work together."

Paper: https://arxiv.org/abs/2602.03798[^6]

### Compound Engineering

Source: https://every.to/guides/compound-engineering

Overview: Compound Engineering is an AI-native engineering philosophy from Every where each unit of work makes subsequent units easier. Instead of codebases accumulating complexity over time, features teach the system new capabilities, bug fixes eliminate entire categories of future bugs, and codified patterns become tools for future work.

Key Ideas:
- The core philosophy flips traditional development on its head: instead of features adding complexity, they teach the system new capabilities that compound over time
- A four-step loop forms the basis: Plan (transforms ideas to blueprints), Work (agent implements while developer monitors), Review (catches issues and captures learnings), Compound (makes gains permanent)
- The "compound" step is what separates this from traditional AI-assisted development - it produces a system that builds features better each time, not just a single feature
- Planning and review should comprise 80% of engineering time, with work and compound taking the other 20%
- Every runs five products (Cora, Monologue, Sparkle, Spiral, Every.to) with primarily single-person engineering teams using this system

Key Insights:
- Traditional development stops at review but compound engineering uses the fourth step to capture what worked, make it findable with YAML frontmatter, update CLAUDE.md, and verify the learning would be caught automatically next time
- The plugin ships with 26 specialized agents, 23 workflow commands, and 13 skills that provide domain expertise on tap
- CLAUDE.md is the most important file - the agent reads it every session for preferences, patterns, and project context
- docs/solutions/ builds institutional knowledge because each solved problem becomes searchable documentation that future sessions find automatically
- First attempts have a 95% garbage rate, second attempts 50% - expecting perfection on attempt one is like expecting a junior developer to nail a complex feature without context

Actionable Patterns:
- The 50/50 rule: allocate 50% of engineering time to building features and 50% to improving the system (creating review agents, documenting patterns, building test generators)
- Extract taste into systems: write preferences in CLAUDE.md or AGENTS.md, build specialized agents for reviewing/testing/deployting, add slash commands that encode preferred approaches
- Parallelization is the new bottleneck: run multiple agents and features simultaneously, perform review/testing/documentation all at once
- Plans are the new code: having a plan captures decisions before they become bugs - fixing ideas on paper is cheaper than fixing code later
- Trust the process by building safety nets: tests, automatic review, monitoring flag issues so you don't have to watch every step

Technical Details:
- Plugin installation: `claude /plugin marketplace add https://github.com/EveryInc/every-marketplace` then `claude /plugin install compound-engineering`
- Core commands: `/workflows:brainstorm` (when requirements are fuzzy), `/workflows:plan` (three parallel research agents), `/workflows:work` (agent writes code), `/workflows:review` (14 specialized agents), `/workflows:compound` (documents solved problems)
- `/lfg` chains the full pipeline: plan to deepen-plan to work to review to resolve findings to browser tests to feature video to compound - spawns 50+ agents
- Project structure: CLAUDE.md (agent instructions), docs/brainstorms/ (output), docs/solutions/ (categorized), docs/plans/ (output), todos/ (priority tracking)
- Review agents include security-sentinel, performance-oracle, architecture-strategist, data-integrity-guardian, code-simplicity-reviewer, and framework-specific reviewers

Quotes:
- "The core philosophy of compound engineering is that each unit of engineering work should make subsequent units easier - not harder."
- "Most codebases get harder to work with over time because each feature you add injects more complexity. Compound engineering flips this on its head."
- "First attempts have a 95 percent garbage rate. Second attempts are still 50 percent. This isn't failure - it's the process."
- "An hour spent creating a review agent saves 10 hours of review over the next year."

### Taskmaster

Source: https://github.com/blader/taskmaster

Overview: Taskmaster is a stop hook for Claude Code that prevents the agent from stopping prematurely. It intercepts stop attempts and forces the agent to verify that all work is truly complete before allowing termination[^11].

Key Ideas:
- Uses a Stop hook in Claude Code to intercept agent termination attempts
- Scans the last 50 lines of the session transcript for incomplete signals (pending tasks, in-progress items, tool errors)
- Implements a session-scoped counter to prevent infinite continuation loops
- Respects user intent changes - if user withdraws a request or says to skip something, that item is treated as resolved
- Requires jq for JSON processing and bash for execution

Key Insights:
- The core innovation is using the transcript itself as the source of truth for completion state
- The hook uses a two-stage decision process: counter hard cap AND transcript signal analysis
- The stop_hook_active flag is critical - if the hook already fired once AND no incomplete signals exist, it allows stop (agent reviewed and chose to stop again)
- Loop protection is essential - default of 10 continuations prevents runaway behavior
- The system assumes task lists with structured status fields that can be grep-detected

Actionable Patterns:
- Implement stop hooks as bash scripts that receive JSON input with session_id, transcript_path, and stop_hook_active
- Use temporary file-based counters in TMPDIR for session-scoped state
- Scan transcripts for specific patterns like status: pending or is_error: true
- Build a detailed checklist prompt when forcing continuation: original user messages, task list, plan steps, errors, loose ends

Technical Details:
- Installation: copies SKILL.md and hooks to ~/.claude/skills/taskmaster/ and registers Stop hook in ~/.claude/settings.json
- Hook output format: jq -n '{ decision: "block", reason: $reason }' to block stop
- Configuration via TASKMASTER_MAX environment variable (default: 10, 0 for infinite, 1 for minimal review)
- The script uses set -euo pipefail for strict error handling
- Transcript analysis uses tail -50 to check only recent activity

The continuation prompt sent to the agent includes:
1. Re-read original user messages and list every discrete request
2. Check task list for incomplete items
3. Check plan for skipped or partial steps
4. Check for tool/build/test/lint errors
5. Check for TODO comments, placeholder code, missing tests
6. Respect that user's latest instructions always take priority

Quotes:
- "If work remains, the agent continues. If truly done, the agent confirms and the hook allows the stop on the next cycle."
- "IMPORTANT: The user's latest instructions always take priority. If the user said to stop, move on, or skip something, respect that - do not force completion of work the user no longer wants."

## Notes

Previously worked with stop hooks in the Ralph project, but it was quite useless - just "continue" and that's it. The goal is to make this more intelligent:

1. The system should look at messages from Claude and respond based on them
2. Instead of a simple task list like "continue improving", there should be something concrete
3. When an agent finishes one piece, it should take on the next, until everything is complete

This is the essence of proper task decomposition: tasks broken into pieces, where the agent completes one fragment then moves to the next, until all are done.

The FullStack-Agent research reinforces a key insight: testing should happen during generation, not after. Development-Oriented Testing provides real-time execution feedback that catches integration failures as they happen. This aligns with the broader pattern of keeping agents working until tasks are truly complete - the agent should validate its own work continuously rather than requiring separate validation passes.

GSD's approach to context rot directly addresses the Telegram bot goal: by keeping the main orchestrator context light (30-40%) and spawning fresh subagent contexts for each task, the system stays responsive even during long-running work sessions. This is relevant for building a Telegram-controlled bot because the bot needs to maintain state across multiple interactions while keeping each response focused and actionable. The discuss-plan-execute-verify loop maps well to a chat interface: discuss captures requirements, plan creates structured tasks, execute runs them in fresh contexts, and verify confirms completion before moving on.

Taskmaster solves the premature stopping problem that plagued the Ralph project. Instead of a generic "continue" prompt, Taskmaster uses transcript analysis to detect specific incomplete signals (pending tasks, tool errors) and sends a structured checklist that forces the agent to verify each aspect of completion. The two-stage decision process - counter hard cap plus transcript analysis - prevents infinite loops while ensuring thoroughness. This pattern could be adapted for a Telegram bot by analyzing the conversation history for unaddressed requests before marking tasks as complete.

The tmc-marketplace iterative-engineering plugin demonstrates the value of explicit stage boundaries. The brainstorming stage produces PRDs with high-level direction but deliberately avoids implementation details. Tech planning describes what and where but not how - no pre-written method bodies. This separation keeps each stage focused and prevents premature optimization. For a Telegram bot, this suggests structuring commands around stages: a `/brainstorm` command for requirements gathering, a `/plan` command for technical breakdown, and an `/implement` command that executes the plan. The severity-based fix acceptance pattern is also relevant - instead of forcing the user to address all feedback, the bot could present findings grouped by severity and let the user choose what to fix.

Compound Engineering from Every introduces a crucial insight: the compound step is what separates traditional AI-assisted development from a truly compounding system. After shipping a feature, you must capture what worked, make it findable with metadata, update CLAUDE.md, and verify the learning would be caught automatically next time. This maps directly to the Telegram bot goal: after the bot completes a task, it should extract patterns and add them to its knowledge base so future sessions benefit. The 50/50 rule (50% features, 50% system improvement) suggests the bot should invest time in learning from each interaction, not just executing commands.

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
[^12]: [https://every.to/guides/compound-engineering](https://every.to/guides/compound-engineering)
