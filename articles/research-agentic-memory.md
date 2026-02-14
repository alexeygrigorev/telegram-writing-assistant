---
title: "Agentic Memory Systems for AI Agents"
created: 2026-02-10
updated: 2026-02-14
tags: [research, agents, memory, llm, vector-search, rag]
status: draft
---

# Agentic Memory Systems for AI Agents

Research into memory systems that enable AI agents to remember, retrieve, and synthesize information across long-running sessions and multi-step workflows.

## What I Want to Understand

How to build effective memory layers for agents that can persist context across sessions, enable efficient retrieval of relevant information, and support long-running workflows without context window limitations.

## Resources

### Eric Tramel: Searchable Agent Memory

Status: URL Not Found (404)

The original URL [https://eric-tramel.github.io/llm/2024/11/14/memory.html](https://eric-tramel.github.io/llm/2024/11/14/memory.html) returns a 404 error. The content may have been moved, deleted, or the URL structure changed.

Based on the original reference, this article discussed a lightweight approach to searchable agent memory using BM25 ranking:

Key insights:
- BM25 (Best Matching 25) is a ranking function used in information retrieval
- It's simpler than vector embeddings while still being effective for many use cases
- The approach creates a searchable index of agent interactions and memories
- Memory can be stored as plain text and ranked by relevance at query time

The advantage over vector databases: no embedding computation, simpler infrastructure, and interpretable ranking based on term frequency.

Action needed: Verify correct URL or locate an archived version of this content[^4].

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

### LinkedIn: Why I Stopped Letting LLMs Build My Knowledge Graphs

Source: https://www.linkedin.com/pulse/why-i-stopped-letting-llms-build-my-knowledge-graphs-what-malaraju-ycxbc

Overview: A case study of building an enterprise code migration platform using Fixed Entity Architecture (FEA), a three-layer approach to knowledge graphs that avoids LLMs during graph construction in favor of deterministic, math-based methods.

Key Ideas:
- LLM-based knowledge graph extraction produces noisy, duplicated entities and hallucinated relationships
- Fixed Entity Architecture defines a curated ontology layer built by domain experts, not LLMs
- Three layers: Fixed Entity Ontology (domain concepts), Document Layer (code chunks with embeddings), NLP-Extracted Entities (named entities via spaCy/regex)
- Microsoft GraphRAG requires thousands of LLM calls while FEA uses only math + lightweight NLP
- Adding new data to LLM-built graphs requires reprocessing; FEA connects new data instantly via cosine similarity

Key Insights:
- If you already understand your domain, paying an LLM to rediscover it is both wasteful and less accurate
- The most reliable part of a retrieval system is often the part that uses no AI at all - cosine similarity, dot products, threshold-based edge creation
- Entity duplication (PaymentService vs payment_service vs Payment_Service) is a fundamental problem with LLM extraction that FEA solves by design
- There is an "embedding space gap" between natural language descriptions and code embeddings - direct similarity fails without bridging techniques
- "Super-nodes" are concepts that match too much content (e.g., "Error Handling" appearing in 90% of code) and must be excluded from ontology

Actionable Patterns:
- Define ontology concepts manually with rich textual descriptions and embedding vectors
- Use HyDE (Hypothetical Document Embeddings) to bridge semantic gaps between NL descriptions and code embeddings - generate hypothetical code snippets for each concept, embed those, and use for similarity matching
- Exclude any concept that would match more than 50% of your content to avoid super-node degradation
- Combine three retrieval methods with Reciprocal Rank Fusion: vector search on embeddings, full-text search, concept-guided search through ontology
- Use cosine similarity thresholds (0.35-0.45) to create precise RELATES_TO edges between content and concepts

Technical Details:
- Author's implementation: 15 domain concepts for microservices codebase (9 business logic, 3 communication, 3 infrastructure)
- HyDE improvement: mean cosine similarity jumped from 0.09 (essentially random) to 0.30+ (3x improvement) after bridging to code space
- HyDE is one-time cost: 15 LLM calls for 15 concepts, then pure math for all subsequent connections
- NLP layer uses spaCy and regex for named entity extraction (technology names, organizations, API names)
- Entire FEA layer adds ~2 seconds to ingestion pipeline with zero LLM calls
- Search via Reciprocal Rank Fusion combining three indexes: vector similarity, full-text, concept-guided

Foundational sources referenced:
- Dr. Irina Adamchic's Fixed Entity Architecture series (Accenture Center of Advanced AI)
- Gao et al., "Precise Zero-Shot Dense Retrieval without Relevance Labels" (arXiv:2212.10496, 2022) - HyDE technique

Quotes:
- "If you already understand your domain, why are you paying an LLM to rediscover it poorly?"
- "Cosine similarity, dot products, and threshold-based edge creation are boring. They are also fast, deterministic, reproducible, and free."
- "The quality of your ontology is defined as much by what you exclude as by what you include."
- "No single retrieval method is sufficient. Combine them with RRF and let each method compensate for the others' blind spots."

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

### Reddit: Everyone's Trying Vectors and Graphs for AI Memory. We Went Back to SQL.

Source: https://www.reddit.com/r/AI_Agents/comments/1nkx0bz/everyones_trying_vectors_and_graphs_for_ai_memory/
Referenced in: [20260211_152925_AlexeyDTC_msg1451.md](../inbox/raw/20260211_152925_AlexeyDTC_msg1451.md)

Overview: A Reddit discussion from the AI_Agents community debating different approaches to agentic memory. The OP (Arindam_200 from Gibson) promotes Memori, a SQL-native memory engine, arguing that relational databases are more practical than vector or graph databases for many AI memory use cases. The community response provides nuanced perspectives on when each approach shines.

Key Ideas:
- The core problem: LLMs reason well in the moment but forget everything as conversation moves on
- Common approaches tried: prompt stuffing/fine-tuning (token explosion), vector databases/RAG (noisy retrieval), graph databases (scaling issues), hybrid systems (complexity)
- Gibson's proposal: Use SQL for structured memory - short-term vs long-term tables, entities/rules/preferences as records, promote important facts to permanent memory
- Memori is an open-source "multi-agent memory engine" that gives AI agents SQL-based persistent memory

Key Insights:
- The top-voted comment (caiopizzol, 121 points) argues this solves only part of the problem - different memory types need different storage
- "Semantic recall is noisy" for vector DBs is actually a feature, not a bug - it surfaces connections like "terrified of dogs" to "what pet should I get?" without anticipating every relationship
- Hard facts and rules work great in SQL, but fuzzy semantic matching ("this reminds me of that") requires vectors, and relationship queries ("how does everything connect") require graphs
- Hybrid systems may seem complex but memory itself is complex - the solution should match the problem space
- Some community members noted the marketing angle - Memori was being "spammed across Reddit" which is an interesting growth tactic for open-source projects

Actionable Patterns:
- Use SQL for structured, queryable facts: user preferences, entities, rules, explicit relationships
- Use vector databases for semantic similarity and fuzzy matching across unstructured content
- Use graph databases for complex entity-relationship queries and multi-hop reasoning
- Consider Postgres with pgvector extension to get SQL + vectors in one system, avoiding multi-database complexity
- Implement memory promotion: move important facts from short-term to long-term storage based on relevance/frequency
- The "right tool for the job" depends on memory type, not a single winner-takes-all approach

Technical Details:
- Memori project: https://github.com/MemoriLabs/Memori (12k+ stars)
- Stores memories as structured SQL records with joins and indexes for retrieval
- Supports multiple SQL backends including PostgreSQL, CockroachDB, MySQL, and OceanBase
- Can run in hosted mode with API access or self-hosted with your own database
- The Postgres + pgvector approach emerged as a community favorite: single database for app data, vectors, and structured memory

Quotes:
- "The real story here isn't 'SQL wins.' It's that different types of memory need different storage"
- "Semantic recall is noisy for vector DBs, but that's actually the feature, not the bug"
- "With Postgres, you can layer on extensions like pgvector for semantic search, or graph extensions. Instead of wiring up three different systems, agents could just connect to one database"
- "99% of software solutions can be a relational database with some batch jobs and a web server"

### Reddit: Please Stop Creating "Memory for Your Agent" Frameworks

Source: https://www.reddit.com/r/ClaudeCode/comments/1r4asf6/please_stop_creating_memory_for_your_agent/[^12][^13]

Overview: A provocative post in r/ClaudeCode by u/thurn2 (61 upvotes, 86% upvote ratio) arguing that the proliferation of third-party "agent memory" frameworks and MCP plugins is unnecessary because Claude Code already ships with comprehensive memory capabilities. The post sparked a nuanced community debate about where built-in memory ends and where custom solutions become necessary, revealing a spectrum of opinions from "documentation is all you need" to "memory is the biggest unsolved problem in the agentic world."

### Key Ideas

- Claude Code already provides multiple layers of memory: CLAUDE.md files (project-scoped and directory-scoped), MEMORY.md files, SKILL.md files, README files, a tasks system, a planning system, and an auto-memory system
- The OP's core argument is that writing documentation is the right form of memory for agents - these are files the agent can read and write, scoped to the right level, and they serve double duty as human-readable docs
- Many third-party memory plugins bloat the context window, increase token usage, and can cause hallucinations - the cure is worse than the disease
- A counter-argument emerged from users working at scale (500k+ lines across 6 repos): simple file-based memory breaks down for large codebases where you need semantic search across massive amounts of code context
- Some users pointed out that Claude's auto-memory system, while well-designed in principle, does not trigger reliably enough on its own - it needs periodic system-level reminders (similar to how Anthropic already uses reminders for the TodoWrite tool)

### Key Insights

- File-based memory (markdown docs in the repo) is a surprisingly effective memory system for coding agents because it is version-controlled, human-readable, scoped to directories, and requires zero infrastructure
- The real failure mode of agent memory is not storage or retrieval but context window management - every memory system that injects context must justify its token cost against the degradation in reasoning quality
- Auto-memory features that rely on the agent spontaneously deciding to save or retrieve information are unreliable - they need explicit periodic reminders inserted into the conversation to trigger consistently
- There is a significant gap between small/medium projects (where file-based memory works fine) and large codebases or multi-repo setups (where semantic search, vector embeddings, or structured databases become necessary)
- Commit history itself can serve as a form of memory - it records what changed, when, and why, and is already indexed and searchable
- Context window size is a hard constraint on memory usefulness: beyond approximately 150k tokens, models enter "hallucination and lying territory" regardless of how good the memory system is

### Community Perspectives

The community split roughly into three camps:

1. Minimalists (aligned with OP): File-based memory in CLAUDE.md, MEMORY.md, and documentation is sufficient. The problem is not tooling but discipline - writing good docs and keeping them updated.

2. Pragmatic middle ground: Built-in memory works for most projects, but the auto-memory system needs improvement. u/lucianw pointed out that Anthropic's auto-memory is well-designed but under-triggered, and shared a hook-based reminder system that significantly improved auto-memory usage. u/coloradical5280 noted that MEMORY.md set up as a table of contents linking to other memory files "works wonderfully" and is even followed more reliably by competing agents like Codex.

3. Scale-aware skeptics: Users like u/25th__Baam (500k+ lines of code across 6 repos) and u/Parking-Bet-3798 pushed back hard, arguing that file-based memory simply does not scale. u/skeetd described using Qdrant with HuggingFace text embeddings for semantic search over coding preferences, keeping the CLAUDE.md file lightweight (about 1k tokens) with just references to the vector store.

Quotes:

- "Claude Code already has all the memory features you could ever need. Want to remember something? Write documentation!" - u/thurn2
- "Memory is the biggest problem that needs to be solved still. Anyone who is deep into agentic world knows this. We need as much innovation as we can get." - u/Parking-Bet-3798
- "I almost never see Claude use it [auto-memory], even at times it should. [...] With these reminders, I found myself benefiting from much better Claude-initiated auto-memory updates." - u/lucianw
- "If you've reached compaction, you've already messed up. [...] If you want to maximize intelligence you need to keep things at 100k context window. More than 150k and you're entering hallucinations and lying territory." - u/james__jam

## Notes

The common pattern across these resources:

1. Storage: Keep memories as structured text with metadata (BM25 or embeddings, or GitHub's citation-based approach)
2. Indexing: Either BM25 (keyword-based), embeddings (semantic), or citation references
3. Retrieval: Query-based ranking to fetch relevant memories
4. Verification: GitHub's key insight - verify citations at read-time rather than complex offline curation
5. Consolidation: Summarize or prune older memories to manage storage

GitHub's citation-based verification approach is particularly interesting because it solves the staleness problem differently than vector-based systems. Instead of trying to detect when code changes and update memories proactively, it simply validates that citations are still accurate at retrieval time. This turns a complex distributed consistency problem into a simple read-time verification step.

The LinkedIn article on Fixed Entity Architecture adds an important dimension: when building knowledge graphs for agentic memory, avoid letting LLMs discover your ontology from scratch. The author shows that manually curated domain concepts connected via cosine similarity produce cleaner, more reliable knowledge structures than LLM-extracted entities. The HyDE technique (generating hypothetical code snippets for each concept, then embedding those) solved a critical "embedding space gap" problem - natural language descriptions and code embeddings live in different semantic spaces and need a bridge.

For a Telegram-controlled bot, the key challenge is maintaining context across command sessions while keeping the retrieval fast and relevant. The GitHub approach suggests that storing references to source material (citations) and verifying them at use-time could be more robust than trying to keep memory perfectly synchronized. The FEA approach suggests defining a small, curated ontology of conversation domains rather than letting the LLM extract entities dynamically.

The Reddit discussion on SQL vs vectors vs graphs reinforces that there is no single best storage approach - different memory types require different storage engines. The community consensus favors using the right tool for each memory type: SQL for structured facts (user preferences, explicit rules), vector databases for semantic similarity, and graphs for relationship queries. A practical compromise mentioned multiple times is Postgres with pgvector extension - a single database that handles structured queries and semantic search without multi-system complexity. For a Telegram bot, this suggests starting with SQL for explicit user data and adding pgvector if fuzzy semantic retrieval becomes necessary.

The r/ClaudeCode discussion on "stop creating memory frameworks" adds an important practical dimension: for coding agents specifically, file-based memory (markdown documents in the repo) is a viable and often sufficient memory system. It is version-controlled, human-readable, directory-scoped, and requires zero infrastructure. The key limitation is scale - this approach breaks down for large codebases (500k+ lines, multi-repo) where semantic search becomes necessary. The discussion also highlights a crucial implementation detail: auto-memory features that rely on the agent deciding to save/retrieve on its own are unreliable without explicit periodic reminders. This echoes the broader pattern that even well-designed agent capabilities need prompting infrastructure (hooks, system reminders) to trigger reliably. For context window management, the community consensus is that memory injection must justify its token cost - beyond 150k tokens, reasoning quality degrades regardless of memory quality.

## Sources

[^1]: [20260209_221323_AlexeyDTC_msg1259.md](../inbox/raw/20260209_221323_AlexeyDTC_msg1259.md)
[^2]: [20260209_221536_AlexeyDTC_msg1260.md](../inbox/raw/20260209_221536_AlexeyDTC_msg1260.md)
[^3]: [20260210_075929_AlexeyDTC_msg1261_transcript.txt](../inbox/raw/20260210_075929_AlexeyDTC_msg1261_transcript.txt)
[^4]: [https://eric-tramel.github.io/llm/2024/11/14/memory.html](https://eric-tramel.github.io/llm/2024/11/14/memory.html)
[^5]: [https://towardsdatascience.com/how-to-build-your-own-custom-llm-memory-layer-from-scratch/](https://towardsdatascience.com/how-to-build-your-own-custom-llm-memory-layer-from-scratch/) (Note: Original URL building-custom-llm-memory-layers-5f12a877881d returns 404)
[^6]: [https://github.com/The-Vibe-Company/companion](https://github.com/The-Vibe-Company/companion)
[^7]: [20260210_082618_AlexeyDTC_msg1262_photo.md](../inbox/raw/20260210_082618_AlexeyDTC_msg1262_photo.md)
[^8]: [https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)
[^9]: [20260211_153046_AlexeyDTC_msg1452.md](../inbox/raw/20260211_153046_AlexeyDTC_msg1452.md)
[^10]: [20260211_152925_AlexeyDTC_msg1451.md](../inbox/raw/20260211_152925_AlexeyDTC_msg1451.md)
[^11]: [https://www.reddit.com/r/AI_Agents/comments/1nkx0bz/everyones_trying_vectors_and_graphs_for_ai_memory/](https://www.reddit.com/r/AI_Agents/comments/1nkx0bz/everyones_trying_vectors_and_graphs_for_ai_memory/)
[^12]: [https://www.reddit.com/r/ClaudeCode/comments/1r4asf6/please_stop_creating_memory_for_your_agent/](https://www.reddit.com/r/ClaudeCode/comments/1r4asf6/please_stop_creating_memory_for_your_agent/)
[^13]: [20260214_063525_AlexeyDTC_msg1657.md](../inbox/used/20260214_063525_AlexeyDTC_msg1657.md)
