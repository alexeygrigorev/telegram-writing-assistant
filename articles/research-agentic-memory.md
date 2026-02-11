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

### GitHub Blog: Building an Agentic Memory System for GitHub Copilot

Source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/

Overview: GitHub's production approach to cross-agent memory that enables Copilot agents (coding agent, CLI, code review) to share learnings across the entire development workflow without explicit user instructions.

Key Ideas:
- Cross-agent memory allows agents to remember and learn from experiences across development workflows, creating a cumulative knowledge base that grows with every use
- The core challenge is not information retrieval but ensuring stored knowledge remains valid as code evolves across branches and time
- Instead of offline memory curation, GitHub uses just-in-time verification with citations to validate memories before use
- Memories are scoped to repositories and only created by users with write permissions, used by users with read permissions
- Memory is available in public preview for Copilot coding agent, CLI, and code review

Key Insights:
- Information retrieval is asymmetrical: hard to solve but easy to verify - this is the key insight that makes the citation system viable
- The citation-based verification avoids significant LLM costs and engineering complexity of offline curation while preventing outdated information
- Memory sharing creates a flywheel effect where each agent contributes to and benefits from shared knowledge
- The system automatically transfers knowledge from experienced team members to newer ones through code review feedback
- Abandoned branches and conflicting observations are handled naturally through verification rather than complex branch tracking

Actionable Patterns:
- Store memories with citations: references to specific code locations that support each fact
- Implement memory creation as a tool call that agents invoke when discovering actionable patterns
- At retrieval time, verify citations by checking the cited code locations still exist and support the memory
- If code contradicts memory, store a corrected version; if citations check out, refresh the memory timestamp
- Use the most recent memories for a repository as context inclusion in prompts

Technical Details:
- Memory structure stored as JSON objects:
```json
{
  "subject": "API version synchronization",
  "fact": "API version must match between client SDK, server routes, and documentation.",
  "citations": ["src/client/sdk/constants.ts:12", "server/routes/api.go:8", "docs/api-reference.md:37"],
  "reason": "If the API version is not kept properly synchronized, the integration can fail..."
}
```
- Retrieval fetches recent memories for target repository at session start
- Verification is a small number of read operations adding no significant latency
- Adversarial memory testing showed agents consistently verified citations and self-healed the memory pool
- A/B testing on Copilot code review showed 3% increase in precision and 4% increase in recall with memory

Quotes:
- "Cross-agent memory allows agents to remember and learn from experiences across your development workflow, without relying on explicit user instructions"
- "Information retrieval is an asymmetrical problem: It's hard to solve, but easy to verify"
- "If an inexperienced developer opens a pull request that updates only one of these locations, Copilot code review will flag the omission and suggest the missing updates, automatically transferring knowledge from a more experienced team member to a newer one"

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

1. Storage: Keep memories as structured text with metadata (BM25 or embeddings, or GitHub's citation-based approach)
2. Indexing: Either BM25 (keyword-based), embeddings (semantic), or citation references
3. Retrieval: Query-based ranking to fetch relevant memories
4. Verification: GitHub's key insight - verify citations at read-time rather than complex offline curation
5. Consolidation: Summarize or prune older memories to manage storage

GitHub's citation-based verification approach is particularly interesting because it solves the staleness problem differently than vector-based systems. Instead of trying to detect when code changes and update memories proactively, it simply validates that citations are still accurate at retrieval time. This turns a complex distributed consistency problem into a simple read-time verification step.

For a Telegram-controlled bot, the key challenge is maintaining context across command sessions while keeping the retrieval fast and relevant. The GitHub approach suggests that storing references to source material (citations) and verifying them at use-time could be more robust than trying to keep memory perfectly synchronized.

## Sources

[^1]: [20260209_221323_AlexeyDTC_msg1259.md](../inbox/raw/20260209_221323_AlexeyDTC_msg1259.md)
[^2]: [20260209_221536_AlexeyDTC_msg1260.md](../inbox/raw/20260209_221536_AlexeyDTC_msg1260.md)
[^3]: [20260210_075929_AlexeyDTC_msg1261_transcript.txt](../inbox/raw/20260210_075929_AlexeyDTC_msg1261_transcript.txt)
[^4]: [https://eric-tramel.github.io/llm/2024/11/14/memory.html](https://eric-tramel.github.io/llm/2024/11/14/memory.html)
[^5]: [https://towardsdatascience.com/how-to-build-your-own-custom-llm-memory-layer-from-scratch/](https://towardsdatascience.com/how-to-build-your-own-custom-llm-memory-layer-from-scratch/) (Note: Original URL building-custom-llm-memory-layers-5f12a877881d returns 404)
[^6]: [https://github.com/The-Vibe-Company/companion](https://github.com/The-Vibe-Company/companion)
[^7]: [20260210_082618_AlexeyDTC_msg1262_photo.md](../inbox/raw/20260210_082618_AlexeyDTC_msg1262_photo.md)
[^8]: [https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)
