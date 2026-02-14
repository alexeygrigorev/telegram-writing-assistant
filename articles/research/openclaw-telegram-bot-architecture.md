---
title: "OpenClaw: Building a Persistent AI Assistant from a Telegram Bot"
created: 2026-02-14
updated: 2026-02-14
tags: [research, telegram-bot, anthropic, claude, ai-assistant, architecture, openclaw]
status: draft
---

# OpenClaw: Building a Persistent AI Assistant from a Telegram Bot

Research into a tutorial by Nader Dabit that walks through building a persistent AI assistant from first principles, starting with a basic Telegram bot and iterating toward a full multi-channel, multi-agent system. The goal is to understand architectural patterns for Telegram bots powered by the Anthropic API and compare them to our own approach[^1][^2].

## What I Want to Understand

How to architect a Telegram bot backed by the Anthropic API so that it goes beyond stateless request-response and becomes a persistent, tool-using, multi-channel assistant. What patterns emerge when you build incrementally, and which of those patterns are worth adopting.

## Resources

### GitHub Gist: You Could've Invented OpenClaw

Source: [https://gist.github.com/dabit3/bc60d3bea0b02927995cd9bf53c3db32](https://gist.github.com/dabit3/bc60d3bea0b02927995cd9bf53c3db32)

The gist is a long-form tutorial (approximately 1400 lines) that starts with the simplest possible Telegram bot using the Anthropic API and builds up to a "mini OpenClaw" - a ~400-line Python script that includes sessions, personality, tools, permissions, context compaction, long-term memory, command queuing, scheduled tasks (heartbeats), and multi-agent routing. The final script runs as a REPL but the same architecture applies to Telegram deployment.

OpenClaw itself is a larger open-source project for building persistent AI assistants across multiple messaging platforms. The tutorial reverse-engineers its architecture by deriving each component from a practical problem.

## Architecture Overview

The tutorial follows an incremental build approach. Each iteration solves a specific limitation of the previous one:

### Version 0: Stateless Bot

A minimal Telegram bot using `python-telegram-bot` and the Anthropic Python SDK. Each message is independent - no memory, no tools, no personality. The entire bot is about 15 lines of code.

The key elements: `Application.builder().token()` for Telegram setup, `client.messages.create()` for the Anthropic API call, `MessageHandler(filters.TEXT, handle_message)` for routing, and `app.run_polling()` for the event loop.

### Version 1: Persistent Sessions via JSONL

Conversation history is stored as JSONL files (one file per user, one JSON object per line). On each message, the full history is loaded, the new message is appended, the entire history is sent to the Anthropic API, and the response is appended back.

The JSONL format is chosen for crash safety: append-only writes mean at most one line is lost on process crash. Session files live in a directory keyed by user ID.

### Version 2: Personality via System Prompt (SOUL.md)

A markdown string defining the agent's identity, behavioral rules, and boundaries is injected as the `system` parameter on every API call. This transforms a generic assistant into a specific persona.

The tutorial calls this pattern "SOUL.md" - a file that gives the agent a name, personality traits, and behavioral constraints. The more specific the SOUL, the more consistent the agent's behavior.

### Version 3: Tool Use with Agent Loop

Tools are defined as JSON schemas following the Anthropic tool use format. The tutorial implements four tools: `run_command` (shell execution), `read_file`, `write_file`, and `web_search`.

The agent loop is the core pattern: call the API with tools defined, check if `stop_reason` is `tool_use`, execute the requested tools, append tool results as a user message with `tool_result` content blocks, and call the API again. Repeat until `stop_reason` is `end_turn`.

A `serialize_content` helper converts Anthropic response objects into JSON-serializable dicts for session storage.

### Version 4: Permission Controls

A safety layer for tool execution. Commands are classified as safe (allowlisted base commands like `ls`, `cat`, `git`), previously approved (stored in `exec-approvals.json`), or needing approval. Dangerous patterns like `rm`, `sudo`, and piped `curl | sh` are flagged.

Approvals are persisted to a JSON file, so each command only needs approval once. OpenClaw extends this with glob patterns (approve `git *` once) and three tiers: ask (prompt user), record (log but allow), and ignore (auto-allow).

### Version 5: Gateway Pattern (Multi-Channel)

The key architectural insight: the agent loop function (`run_agent_turn`) is channel-agnostic. It takes messages and returns text. To add a second channel, you add a Flask HTTP endpoint that calls the same function with the same session store.

This means a user can send a message via Telegram, then query via HTTP using the same user ID, and get continuity. Same sessions, same memory, same agent. The tutorial calls this the "gateway pattern" and notes that OpenClaw extends it to Telegram, Discord, WhatsApp, Slack, Signal, and iMessage through a plugin adapter system.

### Version 6: Context Compaction

When conversation history exceeds a token threshold (estimated at ~4 chars per token), the older half of messages is summarized by a separate API call. The summary replaces the old messages as a single "conversation summary" user message, followed by the recent messages.

This prevents hitting context window limits during long conversations while preserving key facts, decisions, and open tasks.

### Version 7: Long-Term Memory

Two tools are added: `save_memory` (writes a markdown file keyed by a label like "user-preferences") and `memory_search` (keyword search across memory files). Memory files live in a separate directory from sessions, so they survive session resets.

The SOUL is updated to instruct the agent to use these tools proactively. OpenClaw's production version uses vector search with embeddings for semantic matching.

### Version 8: Command Queue (Per-Session Locking)

A `defaultdict(threading.Lock)` provides per-session mutexes. Each session key gets its own lock, so concurrent messages from the same user are serialized while different users can proceed in parallel.

This prevents data corruption when two messages arrive simultaneously for the same session (e.g., one from Telegram and one from HTTP).

### Version 9: Scheduled Tasks (Heartbeats)

Using the `schedule` library, recurring tasks fire the agent on a timer. Each heartbeat uses its own session key (e.g., `cron:morning-briefing`) to avoid polluting the main conversation history. Heartbeats call the same `run_agent_turn` function - they are just timer-triggered messages.

OpenClaw extends this with full cron expressions and routes heartbeats through a separate queue lane so they never block real-time conversations.

### Version 10: Multi-Agent Routing

Multiple agent configurations, each with its own SOUL and session prefix, are routed based on message content. The tutorial uses prefix commands (`/research` routes to a "Scout" agent). Agents share the memory directory, so one agent can save findings and another can search for them later.

## Key Technical Patterns

### Pattern 1: JSONL for Session Persistence

One file per session, one JSON object per line, append-only writes. Crash-safe and simple. The file path encodes the session key (user ID, agent prefix, or cron job name). This avoids the complexity of a database for session storage.

### Pattern 2: The Agent Loop

The while-true loop that handles tool use is the fundamental building block. Call the API, check stop_reason, execute tools, feed results back, repeat. Every feature in the system (multi-agent, heartbeats, gateway) is built on top of this same loop.

### Pattern 3: Channel-Agnostic Agent Logic

By keeping the agent loop free of any channel-specific code, adding new interfaces becomes trivial. The agent function takes a session key, user text, and agent config. It returns response text. Whether that text came from Telegram, HTTP, Discord, or a cron job is irrelevant to the agent.

### Pattern 4: Session Key as Identity

The session key determines what conversation the agent sees. Using `user_id` gives per-user sessions. Using `cron:task-name` gives isolated scheduled sessions. Using `agent:researcher:user_id` gives per-agent-per-user sessions. This single abstraction handles all scoping needs.

### Pattern 5: Memory as Files, Not Database

Long-term memory is stored as markdown files in a dedicated directory. The key is the filename, the content is the knowledge. Search is keyword-based (checking if query words appear in file content). This is simple enough to build in minutes and sufficient for many use cases.

### Pattern 6: Content Serialization for Persistence

Anthropic API responses contain Python objects (TextBlock, ToolUseBlock) that are not directly JSON-serializable. A `serialize_content` helper converts them to plain dicts before storing. This is a practical detail that trips up many implementations.

## Comparison to Building a Telegram Bot with Anthropic API

### What This Approach Does Well

1. Incremental complexity. Starting from 15 lines and adding one feature at a time makes each architectural decision clear. You understand why each component exists because you felt its absence.

2. Session persistence from the start. Many Telegram bot tutorials use in-memory dicts for conversation history, which is lost on restart. The JSONL approach is production-ready from version 1.

3. Clean separation of concerns. The agent loop, session management, tool execution, and channel handling are all independent. You can swap any layer without touching the others.

4. Tool use done right. The agent loop pattern (call, check, execute, feed back, repeat) is the correct way to implement Anthropic tool use. The serialization helper handles the common gotcha of non-serializable response objects.

5. Safety as a first-class concern. Adding permission controls for shell execution before deploying is critical. The persistent approval list is a practical pattern that avoids repeated prompting.

### What Is Missing or Could Be Improved

1. No streaming. All API calls use synchronous `messages.create()`. For a Telegram bot, this means the user sees nothing until the entire response is generated. Streaming with `messages.stream()` would provide a better user experience, especially for long responses.

2. Token counting is approximate. The `len(json.dumps(m)) // 4` estimation works but can be inaccurate. The Anthropic API returns `usage.input_tokens` and `usage.output_tokens` on each response, which could be used for precise tracking.

3. No error handling for API calls. The tutorial omits retry logic, rate limiting, and error handling for Anthropic API failures. A production bot needs exponential backoff and graceful degradation.

4. Memory search is keyword-only. Semantic search (e.g., "dinner plans" matching "restaurant reservations") requires embeddings. The tutorial acknowledges this and notes that OpenClaw uses vector search in production.

5. No image or voice handling. The tutorial focuses on text messages only. A real Telegram bot often needs to handle photos, voice messages, documents, and stickers. Anthropic's vision capability could process images sent to the bot.

6. Single-process architecture. Everything runs in one Python process. For production, you would want the agent loop in a separate worker process, with a message queue (Redis, RabbitMQ) between the Telegram handler and the agent.

7. No conversation branching. The linear message history does not support editing or regenerating previous messages. Once a message is appended, it stays.

### Patterns Worth Adopting

1. The JSONL session format is worth considering for its simplicity and crash safety.

2. The gateway pattern (channel-agnostic agent logic) is the right way to structure a bot that might expand to other platforms.

3. The session key abstraction (single string that encodes user, agent, and scope) is elegant and flexible.

4. Context compaction via summarization is a practical solution for long-running conversations without managing complex sliding windows.

5. The persistent approval list for shell commands is a good balance between safety and usability.

6. The heartbeat pattern (scheduled agent runs on isolated sessions) is straightforward to implement and useful for proactive assistant features like daily briefings.

## Tech Stack

- Language: Python
- Telegram library: python-telegram-bot (using `Application`, `MessageHandler`, `filters`)
- LLM: Anthropic Claude (claude-sonnet-4-5-20250929 via the `anthropic` Python SDK)
- API pattern: `client.messages.create()` with tool use
- Session storage: JSONL files on local filesystem
- Memory storage: Markdown files on local filesystem
- Scheduling: `schedule` library with background thread
- HTTP API: Flask (for the gateway pattern demo)
- Concurrency: `threading.Lock` per session, `threading.Thread` for background tasks

## Actionable Takeaways

1. Start with the agent loop. Get the while-true tool-use cycle working first. Everything else (sessions, memory, multi-agent) builds on top of it.

2. Persist sessions to disk from day one. In-memory session storage is a trap that forces a rewrite later.

3. Keep the agent function channel-agnostic. Even if you only have Telegram today, structuring the code this way costs nothing and pays off when you add more interfaces.

4. Add memory tools before you need them. Once the agent can save and search its own memory, you can instruct it (via the SOUL/system prompt) to proactively remember important information.

5. Use per-session locks if your bot handles concurrent messages. The cost is one defaultdict and one `with` statement. The alternative is corrupted session files.

6. Plan for context limits. Compaction is simple to implement and prevents the hard failure that happens when conversation history exceeds the model's context window.

## Sources

[^1]: [20260214_103313_AlexeyDTC_msg1673.md](../../inbox/used/20260214_103313_AlexeyDTC_msg1673.md)
[^2]: [20260214_103407_AlexeyDTC_msg1675_transcript.txt](../../inbox/used/20260214_103407_AlexeyDTC_msg1675_transcript.txt)
