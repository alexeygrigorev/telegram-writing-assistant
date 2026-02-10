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

**Status: URL Not Found (404)**

The original URL [https://eric-tramel.github.io/llm/2024/11/14/memory.html](https://eric-tramel.github.io/llm/2024/11/14/memory.html) returns a 404 error. The content may have been moved, deleted, or the URL structure changed.

Based on the original reference, this article discussed a lightweight approach to searchable agent memory using BM25 ranking:

Key insights:
- BM25 (Best Matching 25) is a ranking function used in information retrieval
- It's simpler than vector embeddings while still being effective for many use cases
- The approach creates a searchable index of agent interactions and memories
- Memory can be stored as plain text and ranked by relevance at query time

The advantage over vector databases: no embedding computation, simpler infrastructure, and interpretable ranking based on term frequency.

**Action needed**: Verify correct URL or locate an archived version of this content[^4].

### TowardsDataScience: Custom LLM Memory Layers

Source: https://towardsdatascience.com/how-to-build-your-own-custom-llm-memory-layer-from-scratch/

This comprehensive guide builds a memory system from scratch, inspired by the Mem0 architecture. It treats memory as a context engineering problem.

Key Ideas:
- LLMs are stateless by design - every request is a fresh start unless we explicitly provide previous session information
- Memory management requires mastering core context engineering techniques: information extraction, summarization, vector databases, query generation, similarity search, and tool calling
- The system follows a four-component architecture: extract, embed, retrieve, and maintain
- Every memory operation should be optional - the LLM should autonomously decide when to search memory based on context needs

Key Insights:
- Memory is an ever-evolving pool of information, not a simple log. Some memories need deletion when obsolete, others need updating when conditions change
- The Mem0 architecture uses a ReAct (Reasoning and Acting) loop for memory maintenance - the agent decides whether to add, update, delete, or no-op based on conversation turns and contradictions with existing facts
- A "good memory" is defined as a short, self-contained atomic fact that can be embedded and retrieved later with high precision
- User isolation is critical - filtering by user_id in queries guarantees per-user, persistent vector-backed databases

Actionable Patterns:
- Use DSPy Signatures to define memory extraction contracts with structured input/output fields
- Store memories as Pydantic models with metadata (user_id, date, memory_text, embedding)
- Implement hybrid filtering in vector queries - QDrant supports SQL-like where clauses alongside similarity search
- Create separate agent flows for response generation (which may fetch memories) and memory maintenance (which updates them)
- Use ReAct agents with max_iters parameter to control how many memory lookups occur before answering

Technical Details:
- DSPy signature for memory extraction uses docstring as system prompt to customize what information gets extracted
- OpenAI text-embedding-3-small with 64 dimensions balances cost, speed, and quality for short factoids
- QDrant collection setup with DOT distance and user_id payload index for fast filtering
- Memory maintenance tools: add_memory(), update_memory(id, text), delete_memories(ids), no_op()
- The response generator outputs both a response and a save_memory flag for conditional memory updates

Code patterns:
```
# DSPy signature for extraction
class MemoryExtract(dspy.Signature):
    """Extract relevant information from the conversation.
    Memories are atomic independent factoids that we must learn about the user.
    If transcript does not contain any information worth extracting, return empty list.
    """
    transcript: str = dspy.InputField()
    memories: list[str] = dspy.OutputField()

# ReAct agent with tool calling
response_generator = dspy.ReAct(
    ResponseGenerator,
    tools=[fetch_similar_memories],
    max_iters=4
)
```

Quotes:
- "A short, self-contained fact - an atomic unit - that can be embedded and retrieved later with high precision"
- "If your chatbot treats the user as a stranger every time they log in, how can it ever generate personalized responses?"
- "Every step above should be optional. If the LLM agent does not need access to previous memories to answer a question, it should not try to search our vector database at all"

Note: The original URL (building-custom-llm-memory-layers-5f12a877881d) returns 404. This summary is based on the current article "How to Build Your Own Custom LLM Memory Layer from Scratch" which covers the same topic area. Full code repo: https://github.com/avbiswas/mem0-dspy[^5].

### The-Vibe-Company/companion

[companion](https://github.com/The-Vibe-Company/companion) is a web UI for Claude Code built on a reverse-engineered WebSocket protocol.

Overview: Companion unlocks Claude Code from the terminal by providing a browser-based interface with multiple sessions, real-time streaming, and visual tool call approval. It connects to the Claude Code CLI via an undocumented `--sdk-url` WebSocket flag.

Key Ideas:
- Uses NDJSON (newline-delimited JSON) over WebSocket for bidirectional communication between browser and CLI
- Spawns separate Claude Code processes per session, each with independent model and permission settings
- Provides four permission modes from auto-approve everything to manual approval per tool call
- Sessions persist to disk and auto-recover with `--resume` after crashes
- Environment profiles store API keys and config per-project in `~/.companion/envs/`

Key Insights:
- The Claude Code CLI contains a hidden SDK interface that can be exploited for external tooling
- Session isolation at the process level prevents context contamination between parallel agents
- Subagent nesting renders hierarchically, allowing users to follow the full chain of agent spawning
- The full protocol specification (13 control subtypes, permission flow, reconnection logic) is documented in `WEBSOCKET_PROTOCOL_REVERSED.md`

Actionable Patterns:
- For terminal-based AI tools, consider adding a WebSocket server mode for external UI integration
- Use separate processes for session isolation rather than in-memory session management
- Store environment configuration per-project rather than globally to enable multi-tenant workflows
- Implement session persistence with crash recovery for long-running agent workflows

Technical Details:
- Installation: `bunx the-vibe-companion` then open `localhost:3456`
- Tech stack: Bun runtime, Hono server, React 19, Zustand, Tailwind v4, Vite
- Architecture: Browser ←→ Bun/Hono Server ←→ Claude Code CLI
- WebSocket endpoints: `/ws/cli/:session` (CLI connection) and `/ws/browser/:session` (browser connection)
- Session state stored on disk and recovered via `--resume` flag

Quotes:
- "Claude Code is powerful but stuck in a terminal. You can't easily run multiple sessions, there's no visual feedback on tool calls, and if the process dies your context is gone."
- "We reverse-engineered the undocumented WebSocket protocol hidden inside the CLI and built a web UI on top of it. No API key needed, it runs on your existing Claude Code subscription."

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
[^5]: [https://towardsdatascience.com/how-to-build-your-own-custom-llm-memory-layer-from-scratch/](https://towardsdatascience.com/how-to-build-your-own-custom-llm-memory-layer-from-scratch/) (Note: Original URL building-custom-llm-memory-layers-5f12a877881d returns 404)
[^6]: [https://github.com/The-Vibe-Company/companion](https://github.com/The-Vibe-Company/companion)
[^7]: [20260210_082618_AlexeyDTC_msg1262_photo.md](../inbox/raw/20260210_082618_AlexeyDTC_msg1262_photo.md)
