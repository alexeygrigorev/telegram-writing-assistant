---
title: "Inside ZCode: Taking a Coding Agent Harness Apart"
created: 2026-09-18
updated: 2026-09-18
tags: [research, agents, zcode, reverse-engineering, codex, glm]
status: draft
---

# Inside ZCode: Taking a Coding Agent Harness Apart

Z.ai gives away 300 million GLM tokens on weekend promotions, and you have to spend them through their ZCode desktop app. The app is GUI-only - no TUI, no public API. I connected it to Codex instead (my codex-zcode fork), and that meant taking the app apart to see what I was actually plugging into.

I expected a thin GUI wrapper over an API. Instead, the app ships a full agent harness in a separate Node bundle. The harness has its own tool set, subagents, MCP support, and skills. Its goal system never trusts the model's own completion claims.

I look at four things below:

- where the real agent lives in the Electron app, and how I extracted readable sources
- how the UI talks to that bundle over a small NDJSON protocol
- what the harness does inside - tools, subagents, MCP, skills, and the goal system
- which pieces I want to copy into the codex-zcode fork

Every claim below comes from reading the de-minified code, and the commands to re-check it are at the end.

## Taking the app apart

The installed app sits in /opt/ZCode as a 206 MB Electron binary. `npx asar extract` unpacks the GUI code (a React 19 renderer, the Electron main process, a host, and a cron scheduler). None of these contain the agent.

The app ships the agent as a separate file next to the GUI: `resources/glm/zcode.cjs`. It's a single 12.6 MB esbuild bundle, version 0.16.5 of their CLI. This one file talks to the model and runs every tool.

Prettier turns minified JavaScript back into something greppable:

```bash
npx asar extract /opt/ZCode/resources/app.asar /tmp/asar
npx prettier --parser babel --print-width 100 \
  /tmp/asar/out/host/index.js > /tmp/host.pretty.js

for f in /opt/ZCode/resources/glm/m*.js; do
  npx prettier --parser babel --print-width 100 "$f" > "/tmp/$(basename "$f").pretty.js"
done
```

The core ships as chunk files named m0000.js and m0123.js. After formatting, the protocol schemas live in m0000 and the agent runtime in m0123, which comes to about 369k readable lines. The minifier destroyed whitespace but kept most names, so `ToolScheduler`, `subagentPort`, and `sessionStore.setTarget` all survive.

## Four processes per conversation

<!-- illustration: process topology of the ZCode desktop app -->

The desktop splits the work across four processes:

- Electron main owns windows and forks the other processes
- the host owns every conversation with the agent core
- the React renderer draws the UI and never touches stdio
- the zcode.cjs bundle is the core, one process per workspace

Main connects the sides with a MessageChannelMain and then steps out of the way. Port 1 goes to the renderer on the `zcode:service-port` channel. Port 2 goes to the host, and agent traffic flows between renderer and host without passing through main.

The host spawns the core with ELECTRON_RUN_AS_NODE=1, so the Electron binary runs it as a plain Node process with the workspace as the working directory.

```text
┌──────────────────────────────────────────────────────────────┐
│ Electron main                                                │
│   forks the host and the cron scheduler                      │
│   MessageChannelMain: port2 to the host, port1 to the UI     │
└───────────────┬───────────────────────────────┬──────────────┘
                │ port2                         │ port1
                ▼                               ▼
┌────────────────────────────┐   ┌─────────────────────────────┐
│ host                       │   │ renderer (React 19)         │
│ one client per workspace,  │◄──│ receives the port on the    │
│ event bus, permission      │   │ "zcode:service-port" channel│
│ mirroring to the UI        │   └─────────────────────────────┘
└────────────┬───────────────┘
             │ stdio, NDJSON, "ZCode Protocol" v1
             ▼
┌──────────────────────────────────────────────────────────────┐
│ zcode.cjs - "app-server --stdio", ELECTRON_RUN_AS_NODE=1     │
│ one process per workspace, cwd set to the workspace          │
└──────────────────────────────────────────────────────────────┘
```

## The stdio protocol

The host and the core speak "ZCode Protocol" version 1 over stdio. It's JSON-RPC with the jsonrpc field shaved off - NDJSON frames with incrementing request ids. The surface covers about 60 methods across sessions, events, plugins, and MCP.

The transport code is deliberately boring - sending is JSON.stringify plus a newline. Reading buffers stdout, splits on newlines, and validates every frame against a zod schema for that method. A parse failure closes the transport with a protocol_parse_error reason instead of throwing into the caller.

Two pieces of the protocol matter most if you build on this binary.

Permissions stay outside the core. When the model wants to run something risky, the core sends `interaction/requestPermission` to its client. The host mirrors the request to the UI as an elicitation event, and the user's answer travels back as a response. The core never approves anything without asking.

The host also adds delivery guarantees the core doesn't provide. It backfills sequence numbers for events that arrive with seq 0, and it deduplicates by eventId before any listener fires. Late subscribers can catch up, because session/events replays history. There's also a compat retry: when the core rejects a request because of unknown fields, the host strips the flagged fields and sends it again. The app auto-updates the core binary, so the protocol can shift under any external client with no code change on your side.

## Inside the core

The bundle splits into layers with names that survived minification:

- the model layer speaks the Anthropic Messages API, with `provider.zai` as the default entry (kind anthropic, base URL [api.z.ai/api/anthropic](https://api.z.ai/api/anthropic))
- the session store is a `node:sqlite` database under `~/.zcode/cli/db`, with tables for sessions, todos, usage, and more
- the projection layer rebuilds the timeline, the target, usage, and context size from stored events
- the runtime talks to pluggable ports:
    - `mcpPort` for MCP tool servers
    - `skillPort` for skills
    - `subagentPort` for the Agent tool
    - an `executionPort` for running things, plus a browser session for computer use

Full model input and output also ends up in `rollout/model-io-sess_*.jsonl` files, one per session. If you ever wanted a complete trace of every prompt a coding agent sent, it's already on your disk.

## The agent loop

A turn is a loop, and each step is visible in the bundle:

1. assemble the context from the projection, apply microcompaction, and call the model with the tool list
2. stream the response back out as model.streaming events - text deltas, reasoning deltas, tool input fragments, and complete tool calls
3. run the requested tools through a `ToolScheduler` with maxConcurrency 10 - dependency-aware, parallelizing a known read-only set and serializing everything else
4. append the results to the context and repeat until the model ends a turn without tool calls

Context hygiene runs in two modes. Microcompaction clears stale tool results in place and writes "[Old tool result content cleared]" markers, protecting a list of recent or important entries. Full compaction runs as a separate turn phase that summarizes and rebuilds the context. Checkpoints produce events too, and a rewind restores from a snapshot reference.

## Tools, subagents, and skills

The core registers ten built-in tools:

- Read, Bash, Grep, and Glob
- WebFetch (with SSRF guards for localhost and private addresses) and WebSearch
- Edit, Write, ApplyPatch, and TodoWrite

If you've used Claude Code, the list looks familiar. The code confirms the lineage too - the core ships a Task tool described in-code as a Claude Code-compatible alias.

Subagents go through an Agent tool routed through `subagentPort`, and agent types come from profiles parsed from markdown files. A profile declares the agent's name and color, then sets the permission mode, the model, and the tool allowlist.

Two profiles ship built in: general-purpose and a read-only Explore. The result includes an `agentId`, and `SendMessage` and `TaskOutput` continue or poll a background agent later.

MCP servers merge from user config and plugin manifests into the tool list with the usual `mcp__server__tool` naming. Skills load lazily: a /skill command with a name and a task pulls the skill body into context only at invocation time. Both catalogs are exposed over RPC, which is how the UI renders its pickers.

## Goal verification instead of self-report

The goal system surprised me most - it's more thought-through than what most agent frameworks ship.

A goal is a persisted target on the session with an objective, a status (active or paused), and an optional token budget. One design decision sets it apart from every keep-going-until-done loop I've read: the model never declares the goal done.

After each turn, the runtime runs a separate verification call to the model with `tools: []`. It's a judge pass over the message history plus a verifier prompt. The verdict comes back as passed, a reason, and a nextAction. The runtime errors out if the verifier tries to call tools instead of returning a verdict. If the verifier call fails, the runtime records the result as failed_closed, so the goal stays active rather than completing on a fluke.

```text
turn ends
    │
    ▼
verifier model call (tools: [])
    │
    ├─ passed ───────────────────▶ goal verified, stop
    │
    ├─ failed, nextAction empty ─▶ stop, goal stays open
    │
    └─ failed, nextAction set ───▶ queue a continuation turn
                                   (inputSource "goal-continuation")
                                        │
                                        ▼
                                  back into the agent loop
```

The runtime queues continuation as a command (mode target-continuation) instead of recursing. The command defers while background tasks run, re-checks that the target is still active and unchanged, and skips when there's nothing actionable left. That last rule kills infinite spin: a failed verification with no next action stops the loop instead of burning tokens.

Every verification gets an incrementing goalIteration number, surfaced as timeline markers and rolled up into goalStats:

- timeline markers per attempt: running / pass / notSatisfied / failed
- a stats rollup with iteration count, tokens against the budget, elapsed time, and tool calls

The UI can even show verifying as a phase, because the verifier appears as a first-class work item the user can stop. When the status changes, the runtime injects reminder text into the context at turn-safe points (paused, resumed, cleared). A deferral flag holds the reminder until a safe moment, so the injection never rewrites history mid-stream.

## Using it without the GUI

A persistent core process buys resume, checkpoints, plugins, and automations. My use case is different, because I want the GLM tokens from a terminal.

The codex-zcode fork of Codex CLI drives the same binary through its headless door:

```text
zcode.cjs --prompt <file> --output-format stream-json --mode yolo
```

Each turn spawns one child with this command line:

- the whole Codex transcript flattens into one prompt, written to a 0600 temp file (a long argv hits the Linux 128 KiB argument limit)
- NDJSON events stream back and map onto Codex response events
- the child exits after every turn

The headless surface exposes no goal RPC at all. So the fork runs its own goal system on top, with persistence, token accounting, and idle continuation turns in ext/goal. The model self-reports completion by ending replies with a `[GOAL:COMPLETE]` or `[GOAL:BLOCKED]` marker line. The bridge translates that marker into a goal update.

So the answer to "does the fork use the core's goal system" is no - the marker protocol is where the two worlds meet.

```text
                  zcode-core                 codex-zcode fork
completion judge  separate verifier call    model self-reports via
                  with tools: []             [GOAL:...] markers
continuation      queued command with        idle continuation turns
                  deferral rules
budgets           token budget + goalStats   accounting state with
                                             BudgetLimited
iterations        goalIteration + timeline   implicit turn counting
                  markers
```

## Pieces I want to steal

Reading the goal machine next to my own implementation left a short list:

1. A verifier pass. One extra tool-less model call when the model claims complete - cheap, and it stops the model from grading its own homework. The core also refuses to continue when the verifier fails without a nextAction. I want that rule in my fork too.
2. Pause on cancel. The core pauses the active goal when the user interrupts. My fork leaves it active, so a resumed session can immediately burn a continuation turn on a goal you walked away from.
3. Reminder deferral. Status changes enter the context at turn-safe points instead of rewriting history mid-stream - the same cache-friendly rule my own context code follows.
4. Iteration accounting. A per-attempt counter with timeline markers turns "how far along is this goal" from a guess into a query.

On the bridge side, I noted three smaller items:

- keep one core process warm across turns instead of paying startup cost per turn
- bound the turn with a stall timeout - the desktop gives every RPC a 3-minute default, while my bridge trusts the child until exit
- copy the staged teardown on abort - end stdin, wait through a grace period, then kill the whole process tree (the core spawns shells of its own)

## Reproducing this

I checked every claim against the shipped binaries. You can re-check any of them with two commands: extract the asar, then run prettier over the chunks.

## Sources

I distilled this article from three longer write-ups with verbatim de-minified excerpts (in my private zcode-article repo, not published):

- zcode-anatomy.md - binary layout and the extraction pipeline
- ui-core-interaction.md - the UI-to-core pipeline and the fork bridge comparison
- zcode-core-internals.md - the runtime stack, the agent loop, and the goal machine

For the notes on getting the free GLM tokens and connecting ZCode to Codex, see [free-llm-access](../claw-drafts/free-llm-access.md).
