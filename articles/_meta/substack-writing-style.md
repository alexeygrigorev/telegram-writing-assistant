---
title: "Substack Writing Style"
created: 2026-07-31
updated: 2026-07-31
tags: [reference, writing, style, substack]
status: draft
---

TODO some documents are meta. I put them into _meta

# Substack Writing Style

This is how [alexeyondata.substack.com](https://alexeyondata.substack.com) sounds, distilled from the 20 most recent posts - about 56,000 words. Every rule here comes from something the posts actually do, and the quotes are verbatim.

Use it when drafting a new post, or when checking whether a draft sounds right.

Not every post behaves the same way. Build logs, tutorials, announcements and a couple of outliers each have their own habits, and the last section covers the differences. Everything before it describes the default, which is the build log.

## Voice and stance

First person singular, past tense, practitioner reporting back. Not a guru, not a peer chatting - someone who did the thing, hit problems, and brought the receipts.

The build logs are told in "I", and "We" shows up in three distinct senses that you shouldn't mix:

- Organisational we, meaning DataTalks.Club: "At DataTalks.Club, we run free courses like ML Zoomcamp"
- Instructional we, meaning author and reader walking through a step together, in tutorials only: "We can now start a fresh session and launch the loop"
- Analytical we, in the data post: "We collected a dataset of 113 FDE jobs descriptions"

"You" is reserved for guides, and for giving the reader something to do: "In your case, you can select any technology you're comfortable with".

Mistakes are a signature, not a footnote.

The posts state them flat, in one clause, with no self-flagellation and no false modesty:

- "It was my fault for not telling Claude that".
- "One of the agents dropped my production database".
- "Here, I skipped the requirements step, which turned out to be a mistake".
- "The book I tested has been on Amazon for about five months. So far, it has sold zero copies".

After stating the failure, the post extracts a rule from it:

> "The rule I took from it: an agent should never have a path to production".

That pairing runs through the whole corpus, with the flat admission coming first and the takeaway second.

The posts also admit skill limits without hedging:

> "I am not a designer, and I never liked front-end or design work"

> "I'm not a security expert"

Limits of the process get the same treatment:

> "But this was not 'type a prompt and get a platform'".

Enthusiasm shows up only briefly, and only when a concrete fact earns it: "And more than 80 people did, by the way!" Most posts have no exclamation marks in the body at all.

## The opener

Fifteen of the twenty posts open the same way, dropping the reader into the middle of something real.

They give you a concrete personal situation, first person, one to three sentences, before any framing or thesis:

> "I sometimes run offline workshops. These workshops require participants to have access to cloud resources such as AWS".

> "My child has very specific interests and information requests".

> "People keep asking me how to get started with coding agents".

> "I published my first Python library in early 2021. Since then, I've released 24 packages on PyPI"

A few posts vary this. Some open on a general observation the reader will recognise:

> "Your README is the first file people read in your project, and sometimes the only one".

Others open on a data hook or a news hook.

Something smaller repeats inside all of them. Openers usually put a specific number or a proper noun in the first sentence or two, as in 24 packages, three cities, 195 repositories. Concreteness starts at word one.

## The roadmap

After two to five short paragraphs of setup, the post announces its contents. Nine of twenty do this as a literal bulleted list introduced by "In this post, I'll share:" or "walk you through the entire workflow:". Four more make the same move in running text.

This block is load-bearing, so keep it.

## The skeleton

The default build log follows a recognisable arc, visible in at least eight posts:

1. The concrete problem I personally hit, past tense
2. The naive first attempt and why it failed
3. What I built next, step by step, chronologically, with artifacts
4. Where it stands now, including what still doesn't work
5. A short reflective close that extracts a principle

The posts organise chronologically, and each stage exists because the previous one broke:

> "Most parts appeared because the previous version was no longer good enough".

Dates anchor the stages, so the reader can feel time passing:

> "In October 2025, I built...", "Around December 2025...", "In January 2026...".

Tutorials swap this for numbered steps: "Step 1: Choose an Assistant" through "Step 6: Use Subagents When Context Gets Too Large".

## The close

The essay ends with a short reflective section, usually three to eight short paragraphs. Its heading stays plain, like "Where I use it now" or "What I've Learned". Only the data post uses a heading called "Conclusion".

The close restates the arc compactly, extracts the principle, and looks forward:

> "I will write more about this in future articles. If you want to follow along, don't forget to subscribe".

After the essay, most posts have the newsletter apparatus in a fixed order:

1. "What I've Been Working On Recently", with numbered sub-items
2. "Tools", as bulleted capsule reviews
3. A resources block, sometimes
4. "Edited by Valeriia Kuka"

That apparatus is format, not voice.

## Headings

Headings stay short and plain, mostly noun phrases or fragments, with no cleverness:

- "Specs before code"
- "The workshop problem"
- "The First Version"
- "Turning access on from my phone"

Beyond the plain noun phrase, other forms recur:

- The colon heading, giving what and why: "What I built: a credential endpoint I host", "Grooming: the product manager agent"
- Numbered process headings, which include the step count: "1. Start with an Idea"
- Direct questions, occasionally: "Is this role for you?"

Expect five to nine H2 sections before the apparatus, with H3s for enumerated sub-steps.

## Sentences and paragraphs

Sentences run 8 to 20 words, subject-verb-object, declarative. They build through parallel escalation and then land a short punch. The clearest example shows all three moves in sequence:

"A weak agent that misunderstands us writes fifty lines of broken code. A strong agent that misunderstands us creates eight files, wires them together, and adds tests that pass. The code works, but it isn't what we needed".

Fragments and short sentences are used sparingly, as verdicts: "What could go wrong? / Plenty". and "No interface. No web app". and "ChatGPT alone didn't work".

Paragraphs run one to three sentences almost everywhere. Single-sentence paragraphs are common and do the work that bold would otherwise do. Nothing runs past about five sentences.

Contractions are natural throughout, so you get "it's", "don't", "I'll" and "wasn't" without the writing going slangy. The expanded forms appear in more formal instructional passages.

The posts have consistent punctuation habits:

- The spaced hyphen is the connector of choice: "There's a 'deployment gap' - the gap between a prototype and a working customer system". Never the unspaced hyphen-as-dash.
- Colons do heavy lifting, introducing lists, definitions and code blocks.
- Bulleted lists appear in nearly every section, both plain and numbered.
- Bold and italic are essentially absent from body text. Emphasis comes from sentence position and paragraph isolation.
- Semicolons are rare. Emoji never appear, and there's exactly one text emoticon in 56,000 words.

Sections pass the reader on, because the last sentence of a section often sets up the next heading:

> "That is what led to the next stage: building a RAG-powered Slack bot that could answer questions automatically".

You can also open a paragraph with "So" or "But" or "And". The same goes for "That's why", "Eventually" and "At that point".

One thing to keep in mind: the writing is plain rather than polished, and a few non-native constructions survive editing. Don't manufacture those, but don't sand the text into idiomatic perfection either, because direct and slightly plain beats elegant variation.

## Concreteness

Nothing else in the corpus does as much work as this. Almost every claim ships with a number, a name, a date, a price or a link.

The posts are dense with counts and metrics:

- "4,894 descriptions"
- "the number of FDE-related postings increased from 28 in January to 108 in July"
- "retrieval reached a 94% hit rate and 90% mean reciprocal rank"
- "41 of 46 tasks were done"

Money and time get the same treatment:

- "cost roughly $4 using Gemini 3 Pro"
- "€20/month"
- "It produced 21 chapters, took about 45 minutes of wall-clock time"
- "I usually spend around 10 minutes on this step"

Paths and configs appear literally, whether that means file trees, `.claude/skills/<skill-name>/SKILL.md`, or full `pyproject.toml` snippets. Repos get named inline: "Project: github.com/alexeygrigorev/merm".

Estimates are hedged honestly rather than rounded confidently, as in "around 40, maybe even 50, people". The best numbers even get deflated voluntarily where honesty demands it:

> "The CI workflow as a whole only got about 1.5-2x faster overall because most of the CI time is spent on container setup... Most of the 20x build win is hidden behind CI overhead".

That self-correction of a headline number is a signature honesty move.

Code blocks come in three kinds:

- Shell commands
- Config and file layouts
- Verbatim prompts to agents, rendered as code

The text around a block always runs through the same three steps:

1. One line of explanation ending in a colon
2. The block
3. A sentence or two on what happens and why

Blocks never sit back to back without connective text.

Screenshots have descriptive captions that hold data of their own:

> "Codex (gpt-5.5) reporting the backlog goal complete: the shipped fixes, around 9.5M tokens, and 2d 11h 39m elapsed".

Tables are essentially absent, because lists do that job.

## The signature moves

These are the moves that make a post recognisable:

1. Roadmap bullets after the opener.
2. Failure stated flat, then a rule extracted from it: "I learned the hard way that you shouldn't give your agents access to production".
3. The naive attempt shown first: "The obvious choice for a GitHub-hosted site was Jekyll, so I tried that first. It broke almost immediately".
4. Choices justified by self-knowledge rather than benchmarks: "I choose Django because I know it well enough to review".
5. The trade-off couplet, where a benefit is followed by "But", the downside, and then acceptance: "...the generator is specific to this project... But the scope is narrow, so in practice, that has been manageable".
6. The shrug that accepts either outcome: "If it ends up replacing MailChimp, great. If not, that's fine, and we keep MailChimp. But that's the direction".
7. De-escalation of his own advice: "In many cases, you don't need this complexity. Often, a simple prompt or loop is enough". Also "Don't overthink it".
8. Continuity with past posts, treated as running lore. The dropped production database is invoked in at least four separate posts.
9. Jargon defined inline at first use, in apposition: "the harness: the system around an agent, such as Claude Code or Codex".
10. People credited by full name, with explicit thanks where earned.
11. A rhetorical question as a pivot: "What could go wrong?"
12. Personal life as scaffolding - school runs, gym rest periods, his son's book requests - matter-of-fact and specific, never sentimental, always in service of the engineering problem.
13. One-line distilled verdicts: "An AI application without evaluation is only a demo". And "Structure beats search".
14. "It works like this:" or "Here's how it works:" followed by a sequence. This appears in over half the posts.

## Things that never appear

Hype is entirely absent from the corpus, so words like `Revolutionary` and `game-changing` never appear, and neither do `delve`, `supercharge` or `unlock`. The posts call out that register outright:

> "Phrases such as 'AI-powered platform,' 'innovative solution,' and 'intelligent system' add little unless you explain what the system actually does".

Bold and italic never appear in the body text, and neither do horizontal rules.

No throat-clearing opener, and no dictionary definitions. Abstract framing, where it exists at all, comes after the concrete personal case.

No result without its limitation attached. Even launch posts have a caveat: "This is a brand-new platform, so some automations might not work perfectly yet".

The posts never claim certainty about the future:

> "Gemini Flash has not been tested yet for this workflow, so it isn't clear how much quality or cost would change".

Nobody gets moralised at, and second-person accusation never appears. The posts list common mistakes clinically, as in "A wall of text". and "A stale README"., rather than as "you're doing it wrong".

Paragraphs never run long, clauses never nest deeply, and elegant variation never happens. The same term repeats, so it stays the agent, the index and the workshop instead of rotating through synonyms.

Metaphor is almost entirely absent. The rare ones are homely and cashed out immediately: "grading its own homework", "flying blind", a README as "your landing page". Anything more literary reads as wrong.

## Vocabulary

These terms recur across the posts, and you should use them as-is:

- `coding agent` and `coding assistant`, never "AI tool"
- `harness`, `orchestrator`, `subagent`, `session`
- `grooming`, `acceptance criteria`, `definition of done`, `backlog`
- `pipeline`, `workflow`, `human in the loop`, `spec-driven development`
- `sandbox`, `blast radius`, `skip-permissions`
- `throw-away tools`, `dead weight`, `MVP`, `Zoomcamp`
- `tokens` as a consumable, as in "burned a huge pile of tokens"

These verbs come up again and again:

- `build`, `ship`, `run`, `dump`
- `wire`, `point at`, `hand`
- `iterate`, `polish`, `drift`, `land`

The register is technical-casual, and tool names, versions and prices are given exactly. Concepts get explained from zero at first use, on the assumption that readers are smart but may not know this particular corner. Any humour you find is dry and rare.

## Differences between post types

Build logs are the default voice. They rely on "I" and run chronologically through dated stages. Each failure comes paired with a rule, the repos get linked, and the piece ends on a reflective close.

Tutorials use instructional "we" plus imperative "you", numbered steps, verbatim prompts as code blocks, and de-escalations in the "don't overthink it" register. They end with a pointer to the next instalment or to resources.

Announcements run shorter and use "we" more often, at 1,650 to 2,000 words. They give bulleted benefits with explicit calls to action. They stay concrete regardless, with numbers like "81 members" and "27 participants", and they stay caveated. They only create urgency when it's real:

> "Registration is still open, and it closes on April 13".

The data-analysis post uses analytical "we" and puts a percentage on every bullet, as in "Direct client engagement (90% of postings)". It also states its own bias caveat, and it has the only "Conclusion" heading in the corpus. It's the least personal piece.

The third-party explainer drops personal narrative entirely. It gives dense mechanism description with exact parameters, then closes on an evaluative note:

> "There's nothing magical here - it's solid engineering with a few clever ideas".

## The checklist

Run a draft against this before publishing it.

1. Open with the concrete problem you hit, first person past tense, a number or proper noun in the first sentence, two or three sentences before any framing.
2. Add "In this post, I'll share:" and four to six bullets.
3. Narrate chronologically: naive attempt, why it broke, what you built, what still doesn't work. Anchor the stages to months and years.
4. Give every claim a number, price, duration, file path or repo link. Hedge estimates. Deflate your own best numbers where honesty demands it.
5. Keep paragraphs to one to three sentences. Spaced hyphens, colons into lists and code, no bold. Verbatim agent prompts as code blocks, with a connective sentence before and after.
6. State each mistake in one flat clause, then extract a one-line rule from it.
7. For every choice, give the personal reason and the accepted downside.
8. Close with a short reflective section that compresses the arc into a principle and points forward.
9. Delete anything that sounds like marketing, any bold emphasis, any metaphor you wouldn't say out loud, and any claim with no evidence attached.
