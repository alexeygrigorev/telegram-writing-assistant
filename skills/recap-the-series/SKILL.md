---
name: recap-the-series
description: Draft a condensed "recap" or "intro" article that summarizes an existing multi-part article series, reusing the series' real prompts/steps verbatim instead of regenerating them, with a new running example chosen for the target audience. Use when the user wants an overview/teaser article for a series that already has detailed parts written (e.g. "Article 0" for a course series), and wants it grounded in what the series actually says rather than a fresh AI paraphrase of the topic. Triggers - "write a summary article for the series", "condense articles X-Y into one", "intro article for the course", "recap article", "Article 0".
---

# Recap the Series — Condensed Article from Existing Parts

This documents a workflow discovered while drafting "Article 0" for the *AI
Dev Tools Zoomcamp* Substack series (an intro/recap article summarizing
three detailed parts on building, deploying, and operating an app with AI
coding agents). The first attempt at this article was a full independent
19-step tutorial with its own invented prompts. It read as generic and
duplicated the detailed articles instead of pointing to them. The rework
below is what actually worked.

## When to use this

The task is: a series of articles already exists in detail (each with its
own running example, its own prompts, its own voice). You need a shorter
piece that gives readers the shape of the whole arc — enough to be useful
standalone, with pointers to the full parts for depth. This is different
from `shoot-the-article`, which drafts a brand-new standalone piece from
scratch; here the raw material already exists and the job is compression
and re-grounding, not invention.

## The core principle: copy, don't regenerate

The single biggest quality difference in this workflow: **copy the source
articles' actual prompts and steps verbatim, then adjust only what must
change.** Do not ask a model to "summarize article 2's build section" and
accept whatever prose comes back — that produces a flattened paraphrase
that drifts from what the source really said and reads noticeably more
generic/robotic than the original. Instead:

1. Read the source articles directly and extract every literal prompt
   block (the actual ` ```text ` blocks the reader is meant to copy/paste),
   with its section heading and surrounding context.
2. Paste each one into the draft **byte-for-byte**. Do not paraphrase,
   trim, or "clean up" a single word inside a copied block.
3. Drop anything that isn't actually a prompt (file-tree diagrams, raw
   config file contents shown for reference) — keep the list to real
   instructions given to an agent.
4. For each copied prompt, add a short flag noting what — if anything —
   needs to change for the new context: content specific to the old
   example (rename to the new one), or a tool/stack assumption baked into
   the wording (see next section). Most copied prompts need no change at
   all; say so explicitly rather than leaving it ambiguous.

This produces a draft that is honestly *sourced*, not synthesized, and it's
much faster to sanity-check: a human can diff each block against the
original article in seconds.

## Two separate axes of "does this need to change"

Watching for only one of these will let bad prompts through:

- **App-specific**: the prompt names entities from the *old* example (e.g.
  "system design interview application", "canvas component creation").
  These need to be renamed to fit the new running example.
- **Tool/stack-specific**: the prompt hardcodes a particular technology
  (a specific web framework, ORM, cloud provider, IaC tool, CI product,
  container registry, observability vendor) that the source article's
  author simply happened to use, not something the reader is meant to
  copy literally. If the piece's own premise is "these prompts don't
  assume a stack," a hardcoded `AWS CloudFormation` or `GitHub Actions`
  contradicts that premise even though it has nothing to do with the new
  example.

Flag both kinds explicitly and separately — a note that says "generic
as-is" when a prompt actually assumes AWS is worse than no note at all,
because it hides a real inconsistency.

## Filling the tool-choice gap

Source articles are often written by someone who already knew their stack,
so they skip straight to a prompt that assumes a decision was made (e.g.
"Build a FastAPI backend..."). If the recap article's premise is staying
tool-agnostic, insert a new, short "choose the tool" prompt immediately
before each such copied prompt — matching the copied prompts' own terse
style (one to three sentences, not a requirements checklist):

```text
Propose two backend stacks for this application, with the tradeoffs for
each. Recommend one and wait for my approval before writing code.
```

Keep these clearly distinct from copied content (they're new, not sourced)
until the draft is finished, then drop the distinction once it's no longer
needed for review.

## Structure the draft as a skeleton, not prose

Write the condensed draft as a structured outline the whole way through —
resist writing full paragraphs at this stage, even though it's tempting.
For each `##` section and each numbered `###` item inside it:

- **2-4 bullet points** stating what that section needs to say, grounded
  in what the source article actually said (not invented reasoning).
- The prompt block itself (copied, per above).
- A **one-line transition** at the end, connecting to what comes next.

This keeps structural decisions (what to say, in what order) separate from
wording decisions (how to say it), and gives the final prose pass a clean,
checkable skeleton instead of a blank page. It also makes review fast: a
human can read 4 bullets per section far faster than 4 paragraphs, and can
redirect structure before any prose has been written (and thrown away).

Number every `###` item **continuously across the whole file**, not reset
per section — it makes cross-referencing and later reordering easier to
talk about ("move item 14 before item 9").

## Choosing the new running example

Don't reuse the old series' example verbatim, and don't reach for a random
quirky idea either — pick something that resonates with *this* specific
audience. Generate a shortlist grounded in what the audience actually does
(their course, their community, their daily friction), not generic
startup-idea filler. In the source case (a course community that runs
weekly study cohorts), the shortlist included a GPU time-share ledger, a
homework-review swap, and a study-group matching tool — the last one won
because it's something the actual readers have personally tried and
abandoned. A single clear example description (3-4 sentences) goes at the
top of the draft, in the `## Intro` section, and nowhere else needs to
restate it.

## Remove meta-commentary before the final pass

While building the draft it's useful to annotate sources ("[from Article
2, lines 103-110]", "Article 4 says explicitly that..."). Strip every one
of these once traceability is no longer needed — before handing the draft
to a final prose pass. Meta-commentary about where content came from reads
as an internal working note, not something that belongs anywhere near
published prose, and it's easy to forget to remove if left until the end.

## The final prose pass: hand off to a pinned model, don't write it yourself

Once the skeleton (bullets + prompts + transitions) is solid, use the
`prose-write` skill's subprocess pattern to turn it into flowing article
prose in the series' established voice with a **specific, pinned model
version** the user names (not a family alias):

- Brief the subprocess with: the audience/context, an exhaustive DO-NOT-
  CHANGE list (every prompt block byte-for-byte, every heading text/level/
  order/numbering, the product name), and a voice spec backed by *real
  excerpts* from sibling articles in the series (not adjectives like
  "punchy" or "casual" — actual paragraphs to calibrate against).
- Explicitly instruct it to turn every bullet list into prose paragraphs
  and every transition line into a closing sentence — that's the entire
  job of this pass.
- Tell it to output the finished file to **stdout only**, with no preamble.

**Critical failure mode, learned the hard way**: do not tell the subprocess
to "write the finished result back to `<path>`" anywhere in the brief, even
as an aside. A headless `claude -p` subprocess has full tool access by
default; if the brief mentions a target file path, it may reach for its own
Write tool and overwrite the real file — including with nothing, if it
errors partway through. This wiped the actual article file to 0 bytes
during testing. Always:

```bash
timeout 580 claude --model <pinned-model-id> -p "$(cat prompt.txt)" > rewrite.md 2> err.txt
```

Capture only via shell redirect, verify the output yourself (headings
match, every prompt block is byte-identical to the draft, no stray
meta-commentary survived), and only then copy it over the real file with
your own edit tool. See `prose-write`'s `SKILL.md` for the full subprocess
mechanics, model-ID probing, and the invariant-diff verification script.

## Commit at every checkpoint

This workflow has several distinct stages (thesis outline → verbatim
prompts copied → gaps flagged and filled → bullets/transitions added →
meta-commentary stripped → final prose). Commit after each one, with a
message describing what that specific pass did. The recap article built
this way went through 6+ small commits before the final prose pass — each
one a safe rollback point when a later instruction ("actually, remove
that") turned out to apply to a specific stage rather than the whole
draft.

## What NOT to do

- Don't regenerate a source article's prompts from a summary of what it
  said — copy the literal text, then adjust only flagged spots.
- Don't skip the tool/stack-agnosticism check just because a prompt has no
  app-specific content — "generic as-is" needs to be actually generic.
- Don't write full prose before the bullet/transition skeleton is approved
  — it's much more expensive to redirect a paragraph than a bullet.
- Don't leave source citations or "Article N says..." commentary in past
  the drafting stage — it doesn't belong in the final piece.
- Don't let a subprocess write the final file directly. Capture stdout,
  verify, install yourself.
