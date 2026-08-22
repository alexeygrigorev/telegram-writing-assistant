# Comparison notes: dsh vs Claude Code, Codex CLI, opencode

Reference material for the comparison section. Every claim below is tied to a doc page or repo file I actually fetched. Anything I could not confirm is marked `[VERIFY: ...]`.

One correction up front: opencode's repo is no longer at `sst/opencode`. That path redirects to https://github.com/anomalyco/opencode (MIT, TypeScript). The docs site is still https://opencode.ai.

## dsh (DeepSeek Harness)

The bet: no privileged core. From `docs/architecture.md` - "Every part of the product is a plugin, including the model adapter, the tool registry, the session log, and the agent loop itself, so every part is replaceable from configuration. There is no privileged core to patch." The session log is an append-only `SessionEvent` stream, and `deriveMessages()` projects model history from it under the invariant "model-visible means logged." Persistence is itself a seam: `ctx.sessionPersistence` has JSONL and SQLite backends that "persist the same SessionEvent vocabulary."

Pros:
- Compaction, forking, resume, transcripts, telemetry and replay all come out of one mechanism instead of five, because they are all projections of the same stream.
- Adding a new model-visible input is forced through a new session event, so nothing can reach the model off the record. That is an auditability property, not a convenience one.
- Swapping one provider changes the whole product. Filesystem and subprocess providers share one execution world, so repointing them at a remote sandbox moves Bash, PTY and LSP with them.

Cons:
- Adding a capability means designing three roles (service definition, provider, consumer). Real ceremony for a small feature.
- The event vocabulary is a versioned contract, shipped at version zero with no compatibility promise. The flexibility is theoretical for anyone who needs stable session files.
- Only one loop implementation exists. `docs/capability-seams.md` lists `ctx.agentLoop` as "The one concrete loop plugin." `[VERIFY: no third-party alternative loop plugin found]`

Sources: https://github.com/deepseek-ai/deepseek-harness/blob/main/docs/architecture.md , /docs/subsystems/core.md , /docs/capability-seams.md

## Claude Code

The bet: one vendor owns the whole vertical, and you get polish and safety defaults in exchange. There is no published implementation source - `anthropics/claude-code` contains docs, plugins, examples and a changelog, not the CLI's code. Sessions are conventional: transcripts are stored "locally in plaintext under `~/.claude/projects/` for 30 days by default to enable session resumption," tunable with `cleanupPeriodDays`. Models are Claude only; the deployment choices (Anthropic API, Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, a self-hosted gateway via `ANTHROPIC_BASE_URL`) change where inference runs, not which model family answers.

Pros:
- The richest documented extension surface of the four. Around 30 named hook events, including `PreToolUse` (can block, can rewrite tool input via `updatedInput`, can decide permission), `PostToolBatch` (can block before the next model call), `PreCompact`, `Stop`, `SubagentStart`/`SubagentStop`.
- Sandboxing is built in: macOS Seatbelt, Linux and WSL2 via two packages. No native Windows support.
- The permission model has a second layer - auto mode routes actions to "a separate classifier model" instead of to you, while your explicit ask and deny rules still apply.

Cons:
- Single model family. If your reason for using an open harness is running Qwen on a 3090, none of this applies.
- Every extension point is additive. A plugin ships `skills/`, `commands/`, `agents/`, `hooks/hooks.json`, `.mcp.json`, `.lsp.json`, `monitors/`, `bin/`, `settings.json`. None of those replace a component.
- You cannot debug what you cannot read. dsh's public postmortems cite event sequence numbers from a log on your disk; the Claude Code equivalent is a `/feedback` upload.

Sources: https://code.claude.com/docs/en/hooks , /docs/en/plugins , /docs/en/security , /docs/en/sandboxing , /docs/en/data-usage , /docs/en/third-party-integrations , https://github.com/anthropics/claude-code

## Codex CLI

The bet: an open, readable core with a stable protocol boundary, so any UI can drive it. `codex-rs/docs/protocol_v1.md` defines Codex as an engine talking to a UI over a Submission Queue and an Event Queue, and states plainly that "Codex is intended to be operated by arbitrary UI implementations" over "any transport that supports bi-directional streaming." Apache-2.0, Rust.

The session model is closer to dsh than most people assume. `codex-rs/rollout` writes append-only JSONL `RolloutLine` records with a timestamp and ordinal, and `RolloutItem` is a typed enum: `SessionMeta`, `ResponseItem`, `InterAgentCommunication`, `Compacted`, `TurnContext`, `WorldState`, `SecurityRiskScore`, `EventMsg`. A comment in `rollout/src/lib.rs` says "resume and projection use the same item decoder."

The difference is direction. Codex logs the wire items rather than deriving them. `policy.rs` filters which items get persisted at all, and `CompactedItem` carries a `replacement_history` field, so compaction swaps history out instead of re-deriving it from the log. dsh's invariant runs the other way.

Pros:
- Multi-provider through `model_providers.<id>` with built-ins for `openai`, `ollama` and `lmstudio`, so local models work.
- The most serious sandbox of the four: `codex-rs/sandboxing` ships Seatbelt `.sbpl` policies, Landlock, bubblewrap and a Windows path, with `sandbox_mode` values `read-only`, `workspace-write`, `danger-full-access` and an `approval_policy` of `untrusted`, `on-request`, `never`, or a granular object.
- You can read the whole thing, which puts it ahead of Claude Code for anyone diagnosing behaviour.

Cons:
- Reading is not replacing. See the next section.
- Compaction that replaces history means the pre-compaction state is recoverable only from the raw rollout file, not from the running history structure.
- The protocol doc warns "the code might not completely match this spec," and submission payloads are "primarily in-process Rust types rather than a stable serde wire contract."

Sources: https://github.com/openai/codex/blob/main/codex-rs/docs/protocol_v1.md , /codex-rs/rollout/src/lib.rs , /codex-rs/rollout/src/policy.rs , /codex-rs/history/src/lib.rs , /codex-rs/sandboxing/src/ , https://learn.chatgpt.com/docs/config-file/config-reference

## opencode

The bet: model-agnostic, client-server. `opencode serve` runs a headless HTTP server with an OpenAPI 3.1 spec at `/doc` on port 4096, and the TUI is just one client talking to it. Model support is 75+ providers through the AI SDK and Models.dev.

Its context model is the most underrated thing in this comparison. `CONTEXT.md` defines Session History as "the projected chronological conversation selected for a provider turn after applying the active compaction and Context Epoch cutoffs," plus a Context Epoch (an immutable rendered system-context baseline that acts as the provider-cache prefix), a Context Snapshot, and Mid-Conversation System Messages for changed context sources. Messages live in a SQLite table with a `seq` column, and `session/history.ts` builds model history by selecting rows from the latest compaction `seq` forward. So opencode derives history too, but the durable rows are messages, not arbitrary typed events.

Pros:
- Provider breadth backed by a real catalog rather than a hand-maintained list.
- Non-destructive compaction with an explicit cache-prefix concept. Prior mid-conversation system messages "remain durable audit history but leave projected model history."
- Plugins change behaviour, not just observe it: `tool.execute.before`/`after`, `shell.env`, `experimental.session.compacting` (which can replace the compaction prompt outright), and a plugin tool takes precedence over a built-in with the same name.

Cons:
- No sandboxing. Permissions are `allow`/`ask`/`deny` pattern rules with last-match-wins and per-agent overrides, but nothing isolates execution.
- The session model is message-shaped, so anything that is not a message needs its own mechanism. The Context Epoch machinery is exactly the complexity dsh avoids by making everything an event.
- The repo moved owners recently, which matters for anyone pinning a source. `[VERIFY: no plugin hook found that replaces the session runner or turn loop; hooks attach at edges only]`

Sources: https://opencode.ai/docs/plugins/ , /docs/providers/ , /docs/permissions/ , /docs/server/ , https://github.com/anomalyco/opencode/blob/dev/CONTEXT.md , /packages/core/src/session/history.ts

## Who owns the loop

This is the point the draft currently reduces to one line, and it deserves the space. The distinction is not how much you can configure. All four are configurable. The distinction is whether the loop's own decision logic is addressable - can you point at it and put something else there - or whether you can only observe and constrain it from outside.

Claude Code sits at one end. Its extension points are numerous and genuinely powerful: `PreToolUse` can rewrite a tool's arguments and return a permission decision, `PostToolBatch` can stop the run before the next model request, `PreCompact` can block compaction, `Stop` can refuse to let the turn end. Every one of those attaches to a named moment in a loop whose internals stay closed. How the model's context gets assembled each step, what compaction actually does to the transcript, when the turn is considered finished - that is Anthropic's code, shipped as an installed binary with no published source. The Agent SDK confirms the shape rather than changing it: it "gives you the same tools, agent loop, and context management that power Claude Code," and the documented alternative is dropping to the Client SDK, where "you implement the tool loop yourself." There is no middle rung where you keep the harness and change the loop.

Codex CLI is open-core, and it is worth being precise about what that buys. You can read every line of the loop. There are two extension seams, and neither is the loop. The user-facing one is the plugin manifest, which declares `skills`, `mcp_servers`, `apps` and `hooks` - the same additive shape as Claude Code's. The deeper one, `codex-rs/ext/extension-api`, is a Rust trait registry: `ContextContributor`, `ToolContributor`, `TurnInputContributor`, `TurnLifecycleContributor`, `ToolLifecycleContributor` and so on, assembled by an `ExtensionRegistryBuilder`. That is a real seam, and the in-tree features (memories, skills, goal, guardian, web search, connectors) are built on it. But it is compiled in. The host constructs the registry at startup from crates linked into the binary; there is no runtime path for mounting your own contributor, and contributing to the turn is not the same as replacing the turn. Your options are configure it, hook it, or fork it and recompile. `[VERIFY: no dynamic/out-of-tree contributor loading found in codex-rs/ext/extension-api]`

dsh is the case where the loop is genuinely a row in the tree. `core/agent` owns the `Agent` interface, the live registry and the `agent/*` events on `ctx.agents`. `core/agent-loop` is separately described as "the default driver implementing that interface" on `ctx.agentLoop`. The separation is enforced, not incidental: "Extension plugins depend on `agent` - including when they need the initiating Agent - and never on `agent-loop` directly, so the loop stays swappable." Agent creation goes through a factory seam - "Agent creation is provided by whichever plugin implements the AgentFactory (`@deepseek-ai/dsh-agent-loop`), registered via `setFactory`" - so a replacement driver with different turn, retry or compaction semantics registers the same way, and a config patch targeting that row swaps it. Nothing in the Cordis kernel privileges the shipped loop.

The honest caveat: dsh currently ships exactly one loop. `capability-seams.md` calls `ctx.agentLoop` "the one concrete loop plugin," and the only listed consumer is an example package, `agent-spine-demo`. So the correct claim is that dsh's architecture makes the loop addressable and its dependency rules keep it that way, not that a plugin ecosystem of alternative loops exists. The practical payoff today is narrower and still real: because extensions bind to the `agent` contract and not to the loop package, the shipped loop can be rewritten without breaking them, and a fork does not have to be a fork of everything.

The cost cuts the other way too. A closed loop is a loop one team can profile, tune and regression-test end to end - which is a defensible reason Claude Code's compaction and turn behaviour feel more finished than anything in the open field.

## What actually decides the choice

Three axes, all grounded in the above.

Whether you need to change turn semantics or only constrain them. If your requirement is "block this command," "inject this context," "run a linter after every edit," all four handle it, and Claude Code handles it with the most named events. If your requirement is "retry differently," "compact by a different rule," "end the turn on a different condition," Claude Code and Codex require a fork or a recompile, and dsh is the only one where that is a config row.

Whether the session log is the source of truth or a byproduct. Codex's rollout files and opencode's SQLite message table are both durable, ordered and derivable, which is more than a plain transcript array. But Codex filters what it persists in `policy.rs` and replaces history on compaction, and opencode's rows are messages, so non-message state needs the parallel Context Epoch and Context Snapshot machinery. dsh's invariant closes that gap by construction, at the price of a versioned event vocabulary that is currently unstable. Choose on whether you need to reconstruct exactly what the model saw, or only roughly.

Whether isolation is your problem or your platform's. Codex ships the broadest sandbox (Seatbelt, Landlock, bubblewrap, Windows) with three explicit sandbox modes. Claude Code ships Seatbelt and a Linux path with no native Windows. opencode ships permission rules and no sandbox at all. dsh ships a Landlock launcher and an E2B proof of concept. If you are running an agent unattended on a machine you care about, this axis outranks the other two.
