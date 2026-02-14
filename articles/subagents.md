---
title: "Claude Code Subagents"
created: 2026-02-11
updated: 2026-02-11
tags: [claude-code, subagents, ai-workflow, research]
status: draft
---

# Claude Code Subagents

Claude Code supports creating subagents for specialized tasks. This is useful when a single agent's context window becomes overloaded with processing multiple articles or resources.

## When to Use Subagents

When processing multiple URLs or large amounts of content, a single agent reading everything can exceed its context window. This forces context compaction, which loses information and slows down processing.

The solution is to create specialized subagents that handle specific types of work independently. This keeps the main agent's context focused on its primary task.

## Creating Subagents

Creating a subagent in Claude Code is straightforward:

1. Run the `/agents` slash command
2. Select "Create new agent"
3. Describe what the agent should do
4. The agent is created and available immediately

The documentation claims no restart is needed, but a restart may be required for the subagent to work properly.

## Example Use Cases

For research workflows, two subagents can be created:

- Research agent - Summarizes research articles for research topics
- Resource agent - Summarizes interesting resources for the resources newsletter

Both agents use Jina Reader to fetch web content, then process it independently. The main agent remains focused on its primary task (processing voice messages) while subagents handle external content[^2].

## Verification Subagent

A verification subagent was created to address the issue of summarizing voice message content despite instructions not to. Even though the instructions explicitly say not to summarize, the bot sometimes still does it.

The verification subagent runs at the end of processing and:

1. Checks the text that was written
2. Compares it against the original source messages
3. Adds missing content if anything was omitted

This two-step process ensures complete preservation of voice message content[^1].

## Benefits

- Main agent context stays clean and focused
- No context window overflow from processing external content
- Specialized agents can be iterated on independently
- Parallel processing of multiple URLs speeds up workflow

## Sources

[^1]: [20260211_103047_AlexeyDTC_msg1427_transcript.txt](../inbox/used/20260211_103047_AlexeyDTC_msg1427_transcript.txt)
[^2]: [20260210_152205_AlexeyDTC_msg1293_transcript.txt](../inbox/used/20260210_152205_AlexeyDTC_msg1293_transcript.txt)
