# DeepSeek Harness Went Viral. Here's How It Works - publishing notes

Internal publishing notes. Not user-facing prose, so this file is excluded from linting:
run `stylint articles/claw-drafts --exclude '*-meta.md'`.

## Platform deltas

Substack (Alexey On Data, aishippingblog.com):
- Subtitle: What I found reading the source of DeepSeek's open agent runtime
- Paywall: place the break after "One turn through the session log", if paywalled
- Publish-time apparatus added on Substack, not in the draft:
  the "Edited by Valeriia Kuka" credit, plus digest sections if it runs as a regular issue
- Both ```mermaid fences render as images at publish time. Suggested captions:
  1. "The Cordis kernel, the core spine, the capability seams, the policy listeners, and the optional surface bundles."
  2. "One turn: the driver appends events, deriveMessages() projects model history, the invariant re-derives and compares."

Medium:
- Topic tags: Artificial Intelligence, AI Agents, DeepSeek, Open Source, Developer Tools
- Member-only: no
- End CTA: "Thanks for reading! If you found this useful, subscribe to Alexey On Data
  (https://aishippingblog.com) for more AI engineering deep dives, practical guides,
  and the occasional production war story."

## SEO keywords

- DeepSeek Harness
- dsh agent runtime
- DeepSeek Harness architecture
- Cordis plugin kernel
- agent harness plugin architecture
- append-only session event log
- model-visible means logged
- open source alternative to Claude Code
- Codex CLI vs opencode vs dsh
- agent loop as a plugin
- DeepSeek V4-Pro agent runtime
- swappable agent loop harness

## Title and subtitle shortlist

Titles:
1. DeepSeek Harness Went Viral. Here's How It Works (chosen)
2. I Read the Source of DeepSeek Harness
3. How DeepSeek Harness Is Put Together
4. The Agent Runtime Where the Loop Is a Plugin
5. DeepSeek Harness and Its 182,880 Stars

Subtitles:
1. What I found reading the source of DeepSeek's open agent runtime (chosen)
2. The plugin kernel, the session log, and how it compares to Claude Code
3. A read through DeepSeek's open agent runtime, nine days after launch

## Image placeholders

None. Both visuals are real Mermaid diagrams inside the draft, not placeholders.
A Web UI screenshot could be added at publish time after "That launches a browser UI on port 3080."

## Fact corrections applied against the old draft

- E2B is not a `ctx.sandbox` backend. The shipped sandbox provider is `dsh-sandbox-local`
  (bwrap/Landlock/Seatbelt/Windows ACL). `packages/e2b` implements `ctx.fs` and
  `ctx.subprocess`, and no shipped bundle loads it.
- Star count is now timestamped: 182,880 stars and 20,084 forks, read from the GitHub API
  on 2026-08-22. Repo created 2026-08-13. The old "100,000 in days" phrasing is gone.
- LOC framing is now method-explicit: ~247,000 lines of `.ts`/`.tsx` under `packages/` and
  `apps/` excluding tests, 546,000 counting every `.ts` in the tree. The old "495k" is gone.
- opencode's repo is `anomalyco/opencode`, not `sst/opencode`.
- "Built on Cordis" upgraded to the stronger, accurate claim: Cordis is source-vendored into
  `vendor/` under the `@deepseek-ai` scope at 4.0.0-rc.7, commit `56b3d4f`.
- The "model-visible means logged" invariant is enforced code, not documentation:
  `packages/core/agent-loop/src/invariant.ts`.

## Sourcing notes for Alexey

- Every `github.com/deepseek-ai/deepseek-harness/blob/master/...` path in the draft was
  checked with a live HTTP request and returns 200.
- The GitHub API star/fork numbers were read directly on 2026-08-22.
- Two links from the old draft were dropped because they could not be verified:
  - `https://www.reddit.com/r/LocalLLaMA/comments/1vpqum89_deepseek_harnness_why_is_feels_better/`
    is malformed (the post id and slug are fused with no separating slash), so the claims it
    carried (16-hour runs, 20M+ tokens, a 6k system prompt) are not in the draft. If you have
    the real thread, those numbers are worth restoring.
  - `https://myclaw.ai/blog/deepseek-harness-vs-opencode` and the two X aggregator threads
    (`joostvdheijden`, `YoussefHosni951`) were opinion round-ups, replaced by the first-party
    comparison against Claude Code, Codex CLI and opencode docs and source.
- Reddit and X block automated fetching, so the surviving Reddit and X links were only
  checked for well-formedness, not content. Please eyeball them before publishing.
- Length note: the article proper runs about 2,560 words, above the 900-1,700 teardown norm.
  The overage is the two diagram walkthroughs, the four-harness comparison, and the expanded
  "Owning the loop" section. The most cuttable sections if you want it shorter are
  "Running it" and the tool catalog bullets.
