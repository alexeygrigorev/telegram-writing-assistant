---
title: "Multi-Agent Patterns for the Course"
created: 2026-02-21
updated: 2026-02-21
tags: [ai-buildcamp, agents, multi-agent, course-content]
status: draft
---

# Multi-Agent Patterns for the Course

I have a module about multi-agents now. I gave Claude the task to work on it and prepare content, but I do not like what it came up with. I want to base it on my own experience and say what sections I want there[^1].

## Pattern 1: Evaluation

The first pattern is evaluation. We have a loop: one agent does something, a second one checks whether there are errors or not. The second agent can run things depending on the situation. They iterate until the result is good[^3].

For example, we can take the YouTube example. We had an example where we generated video timestamps. We can have an agent that checks whether the timestamps are correct or not. It iterates until the timestamps are absolutely correct. The YouTube example works better than other examples for this[^3].

For each pattern, I want to include examples of how it is used in other applications, not just our specific example. For evaluation, this is how I use it: at the end of a task there is a QA loop. For example, I have a task to write code, I have a coding agent, and I want the code to be verified and working. I create a separate agent whose main focus is specifically verification[^3].

## Pattern 2: Subagent (Agents as Tools)

The first and most basic pattern is the subagent. We have a main agent and it has various tools it can use to do things. It also has another agent that it uses for certain tasks. This subagent may or may not have the same tools as the main agent - it depends on the situation[^1].

The main idea: the problem the subagent solves is that all agents have a context window. The problem is that this context window gets full and the agent can no longer perform its task properly. For context-heavy tasks, we can launch a subagent. For example, an exploration task - we need to explore something. We can launch a subagent to do that[^1].

The subagents take on these heavy contextual tasks so that the main agent's context does not get bloated. This is the first pattern[^1].

"Agents as Tools" fits in this first section. We define agents as tools - an agent is just another tool that we can launch. This is how we build multi-agent systems[^4].

In Claude Code, there is a subagent that does exploration - this is a real-world example of this pattern[^3].

## Pattern 3: Planner-Executor

The second pattern is planner-executor. The idea is to split things into two steps: planning and execution. The execution can happen in multiple steps, so the tasks are more granular for the agent. Because of the context window, the agent cannot just do a big task with 10 steps all at once. If you first plan, decompose it into 10 small steps, and then run each step separately, the agent handles it much better. This is the planner-executor pattern[^2].

In Claude Code, there is also planning - you give it a task, it writes a plan, then passes it to a regular agent. This is not exactly the same decomposition by tasks, but it is close[^3].

I need to think about what example works well for all these patterns. The subagent example does not fit documentation very well - need to think of a good example that people will understand[^2].

## Pattern 4: Orchestration

When we have two agents running, the main agent gets output from one agent and the second agent and decides who to run at what moment. This is the orchestration pattern[^4].

## Patterns Not Included

"Agents as Tools" as a standalone pattern is not needed - it is included in the subagent section. "Orchestration" as a standalone section was initially considered unnecessary, but it fits as the pattern where a main agent coordinates multiple agents[^3][^4].

## Proposed Order

1. Evaluation (loop pattern)
2. Subagent / decomposition (includes Agents as Tools)
3. Planner-Executor
4. Orchestration[^3]

I will iterate further with Claude Code on how to best decompose this into units[^4].

## Sources

[^1]: [20260221_193111_AlexeyDTC_msg2190_transcript.txt](../inbox/used/20260221_193111_AlexeyDTC_msg2190_transcript.txt)
[^2]: [20260221_193257_AlexeyDTC_msg2192_transcript.txt](../inbox/used/20260221_193257_AlexeyDTC_msg2192_transcript.txt)
[^3]: [20260221_193907_AlexeyDTC_msg2194_transcript.txt](../inbox/used/20260221_193907_AlexeyDTC_msg2194_transcript.txt)
[^4]: [20260221_194006_AlexeyDTC_msg2196_transcript.txt](../inbox/used/20260221_194006_AlexeyDTC_msg2196_transcript.txt)
