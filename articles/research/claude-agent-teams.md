---
title: "Claude Agent Teams Research"
created: 2026-02-12
updated: 2026-02-12
tags: [claude-code, agent-teams, ai-workflow, research, parallel-agents]
status: draft
---

# Claude Agent Teams Research

Research into Claude Code's agent teams feature, which enables coordinating multiple Claude Code sessions working together as a team with shared tasks, inter-agent messaging, and centralized management.

## What I Want to Understand

How to effectively use agent teams to parallelize complex AI workflows, coordinate multiple specialized agents, and manage inter-agent communication for tasks that benefit from collaborative exploration.

## Resources

### Claude Code Docs: Orchestrate Teams of Claude Code Sessions

Source: https://code.claude.com/docs/en/agent-teams

Overview: Claude Code's agent teams feature allows coordinating multiple Claude Code instances working together as a team, with one orchestrator (team lead) managing multiple specialized agents (teammates) that work independently in their own context windows and communicate directly with each other.

Key Ideas:
- Agent teams are experimental and disabled by default, requiring the CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS environment variable to enable
- One session acts as team lead, coordinating work, assigning tasks, and synthesizing results while teammates work independently
- Unlike subagents which run within a single session and only report back to the main agent, teammates in agent teams can interact directly with each other and the user
- Each teammate is a full, independent Claude Code session with its own context window
- Teams use a shared task list with self-coordination, plus a mailbox messaging system for inter-agent communication
- Two display modes: in-process (all teammates in main terminal) or split panes (each teammate gets own pane via tmux or iTerm2)

Key Insights:
- The core distinction from subagents is inter-agent communication: agent teams enable teammates to message each other directly, collaborate on shared tasks, and challenge each other's findings
- The strongest use cases are parallel code review (multiple reviewers with different focus areas), competing hypotheses debugging, and cross-layer coordination where each teammate owns a different architectural layer
- Single reviewers tend to gravitate toward one type of issue, while splitting review criteria across teammates ensures security, performance, and test coverage all get attention simultaneously
- When debugging with competing hypotheses, the adversarial structure is key: each teammate's job is to investigate their theory AND challenge the others, fighting the anchoring bias that plagues sequential investigation
- Token usage scales linearly with the number of active teammates since each has its own context window, making agent teams more expensive than single sessions
- Teammates don't inherit the lead's conversation history, only project context (CLAUDE.md, MCP servers, skills) plus their spawn prompt

Actionable Patterns:
- Start with explicit team requests: describe the task and team structure in natural language, letting Claude decide teammate count or specifying exactly how many
- Use delegate mode (Shift+Tab to cycle) to restrict the lead to coordination-only tools, preventing it from implementing tasks itself instead of waiting for teammates
- Require plan approval for risky tasks by telling the lead to keep teammates in read-only plan mode until their approach is approved
- For split-pane mode, install tmux (package manager) or iTerm2 with it2 CLI and Python API enabled
- Pre-approve common permissions in settings to reduce friction from teammate permission requests bubbling up to the lead
- Use hooks (TeammateIdle, TaskCompleted) to enforce quality gates that can reject work and send feedback

Technical Details:
- Enable via settings.json: `{"env": {"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"}}`
- Set display mode: `{"teammateMode": "in-process"}` or `"tmux"` or `"auto"` (default)
- Team config stored at: `~/.claude/teams/{team-name}/config.json`
- Task list stored at: `~/.claude/tasks/{team-name}/`
- In-process mode navigation: Shift+Up/Down to select teammates, Enter to view session, Escape to interrupt, Ctrl+T to toggle task list
- Task states: pending, in progress, completed; tasks can depend on other tasks and won't become claimable until dependencies complete
- File locking prevents race conditions when multiple teammates try to claim the same task simultaneously
- Teammate messaging types: `message` (send to specific teammate) and `broadcast` (send to all, use sparingly as costs scale with team size)

Example prompts:
```
# Parallel code review
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.

# Competing hypotheses investigation
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.

# Exploratory research with multiple perspectives
I'm designing a CLI tool that helps developers track TODO comments across
their codebase. Create an agent team to explore this from different angles: one
teammate on UX, one on technical architecture, one playing devil's advocate.

# Parallel refactoring with plan approval
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.

# Specifying teammate count and model
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

Best practices:
- Give teammates enough context: they load CLAUDE.md, MCP, and skills automatically, but include task-specific details in the spawn prompt
- Size tasks appropriately: too small wastes coordination overhead, too large increases wasted effort risk, just right is self-contained units with clear deliverables
- Aim for 5-6 tasks per teammate to keep everyone productive and allow reassignment if someone gets stuck
- Start with research and review tasks that have clear boundaries before moving to parallel implementation
- Avoid file conflicts by breaking work so each teammate owns a different set of files
- Monitor and steer: check in on progress, redirect approaches that aren't working, synthesize findings as they come in

Comparison with subagents:
| Aspect | Subagents | Agent Teams |
|--------|-----------|-------------|
| Context | Own context window; results return to caller | Own context window; fully independent |
| Communication | Report results back to main agent only | Teammates message each other directly |
| Coordination | Main agent manages all work | Shared task list with self-coordination |
| Best for | Focused tasks where only result matters | Complex work requiring discussion and collaboration |
| Token cost | Lower (results summarized) | Higher (each is separate Claude instance) |

Quotes:
- "Coordinate multiple Claude Code instances working together as a team, with shared tasks, inter-agent messaging, and centralized management"
- "Unlike subagents, which run within a single session and can only report back to the main agent, you can also interact with individual teammates directly without going through the lead"
- "Sequential investigation suffers from anchoring: once one theory is explored, subsequent investigation is biased toward it"
- "Agent teams use significantly more tokens than a single session. Each teammate has its own context window, and token usage scales with the number of active teammates"
- "The lead's conversation history does not carry over"

## Notes

The agent teams feature represents a significant evolution beyond subagents. While subagents are useful for quick, focused workers that report back, agent teams enable true multi-agent collaboration where agents can debate, challenge each other, and coordinate autonomously through a shared task list.

The competing hypotheses debugging pattern is particularly powerful. Instead of one agent finding a plausible explanation and stopping (anchoring bias), multiple agents actively try to disprove each other's theories. The theory that survives adversarial challenge is much more likely to be the actual root cause.

For research workflows, agent teams could parallelize article processing with different teammates focusing on different aspects (technical implementation, conceptual framework, actionable patterns). This is more sophisticated than subagents because teammates can discuss findings, identify contradictions, and synthesize a more comprehensive summary.

The token cost consideration is important. Each teammate is a separate Claude session, so costs scale linearly with team size. The docs recommend agent teams for research, review, and new feature work where the extra tokens are worthwhile, but suggest single sessions or subagents for routine tasks.

## Sources

[^1]: [https://code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams)
[^2]: [20260212_092849_AlexeyDTC_msg1484.md](../../inbox/raw/20260212_092849_AlexeyDTC_msg1484.md)
[^3]: [20260212_092906_AlexeyDTC_msg1485.md](../../inbox/raw/20260212_092906_AlexeyDTC_msg1485.md)
