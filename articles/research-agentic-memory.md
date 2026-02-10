---
title: "Agentic Memory Systems for AI Agents"
created: 2026-02-10
updated: 2026-02-10
tags: [research, agents, memory, llm, vector-search, rag]
status: draft
---

# Agentic Memory Systems for AI Agents

Research into memory systems that enable AI agents to remember, retrieve, and synthesize information across long-running sessions and multi-step workflows.

## What I Want to Understand

How to build effective memory layers for agents that can persist context across sessions, enable efficient retrieval of relevant information, and support long-running workflows without context window limitations.

## Resources

### Eric Tramel: Searchable Agent Memory

[Eric Tramel's blog post](https://eric-tramel.github.io/llm/2024/11/14/memory.html) discusses a lightweight approach to searchable agent memory using BM25 ranking.

Key insights:
- BM25 (Best Matching 25) is a ranking function used in information retrieval
- It's simpler than vector embeddings while still being effective for many use cases
- The approach creates a searchable index of agent interactions and memories
- Memory can be stored as plain text and ranked by relevance at query time

The advantage over vector databases: no embedding computation, simpler infrastructure, and interpretable ranking based on term frequency[^4].

### TowardsDataScience: Custom LLM Memory Layers

[Building Custom LLM Memory Layers](https://towardsdatascience.com/building-custom-llm-memory-layers-5f12a877881d) explores architectures for persistent memory in LLM applications.

The article covers:
- Short-term vs long-term memory patterns
- Vector store integration for semantic search
- Memory consolidation strategies (what to keep, what to discard)
- Hierarchical memory architectures

Key pattern: separate memory stores for different types of information (facts, conversations, procedures) with different retrieval and consolidation strategies[^5].

### The-Vibe-Company/companion

[companion](https://github.com/The-Vibe-Company/companion) is a framework for building AI companions with persistent memory and personality.

Features:
- Long-term memory storage across sessions
- Personality and context persistence
- Multi-session conversation history
- Pluggable memory backends

The codebase shows patterns for:
- Embedding-based semantic search over conversation history
- Selective memory retrieval based on relevance to current context
- Memory summarization to compress older interactions[^6].

## Notes

The common pattern across these resources:

1. Storage: Keep memories as structured text with metadata
2. Indexing: Either BM25 (keyword-based) or embeddings (semantic)
3. Retrieval: Query-based ranking to fetch relevant memories
4. Consolidation: Summarize or prune older memories to manage storage

For a Telegram-controlled bot, the key challenge is maintaining context across command sessions while keeping the retrieval fast and relevant.

## Sources

[^1]: [20260209_221323_AlexeyDTC_msg1259.md](../inbox/raw/20260209_221323_AlexeyDTC_msg1259.md)
[^2]: [20260209_221536_AlexeyDTC_msg1260.md](../inbox/raw/20260209_221536_AlexeyDTC_msg1260.md)
[^3]: [20260210_075929_AlexeyDTC_msg1261_transcript.txt](../inbox/raw/20260210_075929_AlexeyDTC_msg1261_transcript.txt)
[^4]: [https://eric-tramel.github.io/llm/2024/11/14/memory.html](https://eric-tramel.github.io/llm/2024/11/14/memory.html)
[^5]: [https://towardsdatascience.com/building-custom-llm-memory-layers-5f12a877881d](https://towardsdatascience.com/building-custom-llm-memory-layers-5f12a877881d)
[^6]: [https://github.com/The-Vibe-Company/companion](https://github.com/The-Vibe-Company/companion)
[^7]: [20260210_082618_AlexeyDTC_msg1262_photo.md](../inbox/raw/20260210_082618_AlexeyDTC_msg1262_photo.md)
