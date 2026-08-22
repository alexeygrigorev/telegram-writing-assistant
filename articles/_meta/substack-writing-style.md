---
title: "Substack Writing Style"
created: 2026-07-31
updated: 2026-08-22
tags: [reference, writing, style, substack]
status: draft
---

# Substack Writing Style

This is how [alexeyondata.substack.com](https://aishippingblog.com) sounds, distilled from the complete archive of 47 published posts - just over 100,000 words, spanning December 2025 to August 2026. Every rule here comes from something the posts actually do, and the quotes are verbatim.

Use it when drafting a new post, or when checking whether a draft sounds right.

Not every post behaves the same way. Build logs, tutorials, digests, announcements, team-written research pieces and a couple of outliers each have their own habits, and a later section covers the differences. The style also shifted over the nine months of the archive - the "How the style shifted over time" section tracks that drift. Everything before those sections describes the current default, which is the essay-first build log that has dominated since spring 2026.

## Voice and stance

First person singular, past tense, practitioner reporting back. Not a guru, not a peer chatting - someone who did the thing, hit problems, and brought the receipts.

The build logs are told in "I", and "We" shows up in four distinct senses that you shouldn't mix:

- Organisational we, meaning DataTalks.Club: "At DataTalks.Club, we run free courses like ML Zoomcamp"
- Instructional we, meaning author and reader walking through a step together, in tutorials only: "We can now start a fresh session and launch the loop"
- Analytical we, in the data posts: "We collected a dataset of 113 FDE jobs descriptions"
- Team we, in pieces co-written with Valeriia, sometimes with an explicit handoff note: "This article is written by both of us. The next section is from Valeriia... so the 'I' refers to her"

"You" is reserved for guides, and for giving the reader something to do: "In your case, you can select any technology you're comfortable with".

Mistakes are a signature, not a footnote, and they have been from the first month of the newsletter.

The posts state them flat, in one clause, with no self-flagellation and no false modesty:

- "It was my fault for not telling Claude that".
- "One of the agents dropped my production database".
- "Here, I skipped the requirements step, which turned out to be a mistake".
- "Tried installing Linux on an old Samsung phone to run Claude Code (successfully bricked it in the process)".
- "The book I tested has been on Amazon for about five months. So far, it has sold zero copies".
- "I spent more than a month on this project and burned a huge pile of tokens. I rewrote it several times, almost from scratch, but it never became stable".

After stating the failure, the post extracts a rule from it:

> "The rule I took from it: an agent should never have a path to production".

That pairing runs through the whole corpus, with the flat admission coming first and the takeaway second. An entire post, "Six Projects That Didn't Make It", is built from nothing but this move, and it closes on the general principle: "Abandoning some projects along the way is a normal part of the experimentation process".

The posts also admit skill limits without hedging:

> "I am not a designer, and I never liked front-end or design work"

> "I'm not a security expert"

Limits of the process get the same treatment:

> "But this was not 'type a prompt and get a platform'".

Enthusiasm shows up briefly, and only when a concrete fact or another person earns it: "And more than 80 people did, by the way!" and "Thanks again, Zach, for the great workshop material!". In the early months exclamation marks were noticeably more frequent ("And it worked!", "If you want to apply, hurry up!", "Crazy!"); since roughly April 2026 most essay bodies have few or none, and the ones that remain mostly thank people or celebrate community results.

## The opener

The default essay opener drops the reader into the middle of something real: a concrete personal situation, first person, one to three sentences, before any framing or thesis:

> "I sometimes run offline workshops. These workshops require participants to have access to cloud resources such as AWS".

> "My child has very specific interests and information requests".

> "People keep asking me how to get started with coding agents".

> "I published my first Python library in early 2021. Since then, I've released 24 packages on PyPI"

> "I haven't properly updated my personal website since 2012".

This opener was there from the very first real post in December 2025, and it became near-universal for essays by spring 2026.

A few posts vary this. Some open on a general observation the reader will recognise:

> "Your README is the first file people read in your project, and sometimes the only one".

Others open on a data hook or a news hook: "Over the last few days, Andrej Karpathy's autoresearch project has been widely shared and discussed".

The early digest editions sometimes opened with a greeting and housekeeping instead - "Hi everyone," followed by holiday wishes, or "Hey there, I got two to share with you" - a habit that disappeared by March 2026. Don't imitate it in new posts.

Something smaller repeats inside all of them. Openers usually put a specific number or a proper noun in the first sentence or two, as in 24 packages, 88,000 people, 2,500+ applications, 195 repositories. Concreteness starts at word one.

## The roadmap

After two to five short paragraphs of setup, the post announces its contents. Nearly every essay from April 2026 onward does this as a literal bulleted list introduced by "In this post, I'll share:" or "walk you through the entire workflow:". Earlier posts make the same move in running text: "In this post, I want to walk through how the project is built: its architecture, scripts, prompts, and automation". About half the full corpus does it one way or the other, and the bulleted form has clearly won.

This block is load-bearing, so keep it, and prefer the bulleted form.

## The skeleton

The default build log follows a recognisable arc, visible in at least a dozen posts:

1. The concrete problem I personally hit, past tense
2. The naive first attempt and why it failed
3. What I built next, step by step, chronologically, with artifacts
4. Where it stands now, including what still doesn't work
5. A short reflective close that extracts a principle

The posts organise chronologically, and each stage exists because the previous one broke:

> "Most parts appeared because the previous version was no longer good enough".

Dates anchor the stages, so the reader can feel time passing:

> "back in June 2022", "In October 2025, I built...", "Around December 2025...", "In January 2026...".

Tutorials swap this for numbered steps: "Step 1: Choose an Assistant" through "Step 6: Use Subagents When Context Gets Too Large". The 2026 course-notes tutorials go further and thread verbatim prompts through the sequence, so the reader can replay the whole session.

## The close

The essay ends with a short reflective section, usually three to eight short paragraphs. Its heading stays plain, like "Where I use it now" or "What I've Learned". Only the data posts use a heading called "Conclusion".

The close restates the arc compactly, extracts the principle, and looks forward:

> "I will write more about this in future articles. If you want to follow along, don't forget to subscribe".

The forward teaser plus subscribe nudge is a constant across the whole corpus, from December 2025 ("I'll describe the architecture of this project in more detail in an upcoming newsletter. Subscribe for the full breakdown.") to June 2026 ("I plan to write more about DataMailer in one of my future newsletters. Subscribe to stay updated!").

After the essay, most posts have the newsletter apparatus in a fixed order:

1. "What I've Been Working On Recently", with numbered or bulleted sub-items
2. Workshop and event recaps, each with a registration or recording link
3. "Tools", as bulleted capsule reviews with the resource name in bold
4. A resources block, sometimes
5. "Edited by Valeriia Kuka"

That apparatus is format, not voice. The early editions carried more of it - reader Q&A answers, GitHub sponsors thanks, course announcement blocks repeated verbatim week after week - and the essay portion has steadily grown at its expense.

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

Expect five to nine H2 sections before the apparatus. The archive uses H3s for enumerated sub-steps, and the occasional question heading, but stylint rejects both in new drafts - see "Where the linter is stricter than the archive" below. For new posts, keep everything at H2 and put the step number in the heading text.

## Sentences and paragraphs

Sentences run 8 to 20 words, subject-verb-object, declarative. They build through parallel escalation and then land a short punch. The clearest example shows all three moves in sequence:

"A weak agent that misunderstands us writes fifty lines of broken code. A strong agent that misunderstands us creates eight files, wires them together, and adds tests that pass. The code works, but it isn't what we needed".

Fragments and short sentences are used sparingly, as verdicts: "What could go wrong? / Plenty". and "No interface. No web app". and "ChatGPT alone didn't work". and "You need a development process".

Paragraphs run one to three sentences almost everywhere. Single-sentence paragraphs are common and do the work that bold would otherwise do. Nothing runs past about five sentences.

Contractions are natural throughout, so you get "it's", "don't", "I'll" and "wasn't" without the writing going slangy. The expanded forms appear in more formal instructional passages.

The posts have consistent punctuation habits:

- The spaced hyphen is the connector of choice: "There's a 'deployment gap' - the gap between a prototype and a working customer system". A spaced em dash slips through occasionally in the earliest posts, but the spaced hyphen is the rule.
- Colons do heavy lifting, introducing lists, definitions and code blocks.
- Bulleted lists appear in nearly every section, both plain and numbered.
- In current essay prose, bold and italic are essentially absent, and emphasis comes from sentence position and paragraph isolation. This was not always true: through about February 2026, bold list leads like "Refer 3 friends" and "Story generation (GPT-4o):" were common in body text. They faded out of the essays by March and never came back. Bold survives only in the Tools apparatus, where resource names are bolded.
- Semicolons are rare. Emoji never appear in prose; the only exceptions are decorative calendar glyphs in a few event listings ("📅 Tue, Feb 24" style) and a star on CTA buttons ("⭐ Star the course repo"). Text emoticons appear two or three times in nine months, always as a light aside: "Fun detail: Gemini now recommends it ;-)" and "But no worries, I've resolved the issue... :)". Recent essays have none.

Sections pass the reader on, because the last sentence of a section often sets up the next heading:

> "That is what led to the next stage: building a RAG-powered Slack bot that could answer questions automatically".

You can also open a paragraph with "So" or "But" or "And". The same goes for "That's why", "Eventually" and "At that point".

One thing to keep in mind: the writing is plain rather than polished, and a few non-native constructions and plain typos survive editing across the whole corpus ("rarly access", "Clause" for Claude, "hist CORS errors", "speciation" for specification). Don't manufacture those, but don't sand the text into idiomatic perfection either, because direct and slightly plain beats elegant variation.

## Concreteness

Nothing else in the corpus does as much work as this, and it is the one habit that has never wavered from the first post to the latest.

The posts are dense with counts and metrics:

- "4,894 descriptions"
- "the number of FDE-related postings increased from 28 in January to 108 in July"
- "retrieval reached a 94% hit rate and 90% mean reciprocal rank"
- "41 of 46 tasks were done"
- "Total conversations: 2,808" and "The download was 775 MB! Yes, I talk to ChatGPT a lot."

Money and time get the same treatment:

- "cost roughly $4 using Gemini 3 Pro"
- "€20/month"
- "It produced 21 chapters, took about 45 minutes of wall-clock time"
- "I usually spend around 10 minutes on this step"
- "the full recovery took about 24 hours"

Paths and configs appear literally, whether that means file trees, `.claude/skills/<skill-name>/SKILL.md`, or full `pyproject.toml` snippets. Repos get named inline: "Project: github.com/alexeygrigorev/merm".

Estimates are hedged honestly rather than rounded confidently, as in "around 40, maybe even 50, people" and "It takes about 20 to 30 minutes". The best numbers even get deflated voluntarily where honesty demands it:

> "The CI workflow as a whole only got about 1.5-2x faster overall because most of the CI time is spent on container setup... Most of the 20x build win is hidden behind CI overhead".

That self-correction of a headline number is a signature honesty move, and it appears early too: "Even though only 50% of suggested images were good, it saved a lot of time".

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

Tables are essentially absent, because lists do that job. From mid-2026 onward, simple architecture diagrams (often Mermaid-rendered, with data-bearing captions) increasingly do the job that a third screenshot used to do.

## The signature moves

These are the moves that make a post recognisable:

1. Roadmap bullets after the opener.
2. Failure stated flat, then a rule extracted from it: "I learned the hard way that you shouldn't give your agents access to production".
3. The naive attempt shown first: "The obvious choice for a GitHub-hosted site was Jekyll, so I tried that first. It broke almost immediately". Also "I first tried generating the book directly with ChatGPT... ChatGPT alone didn't work".
4. Choices justified by self-knowledge rather than benchmarks: "I choose Django because I know it well enough to review". And "I decided to migrate the platform to Django because I have known it since 2010 and wanted a stack I could step into myself if something went wrong".
5. The trade-off couplet, where a benefit is followed by "But", the downside, and then acceptance: "...the generator is specific to this project... But the scope is narrow, so in practice, that has been manageable".
6. The shrug that accepts either outcome: "If it ends up replacing MailChimp, great. If not, that's fine, and we keep MailChimp. But that's the direction".
7. De-escalation of his own advice: "In many cases, you don't need this complexity. Often, a simple prompt or loop is enough". Also "Don't overthink it" and "Don't spend too much time comparing them".
8. Continuity with past posts, treated as running lore. The dropped production database is invoked in at least six later posts, and nearly every essay from February 2026 onward links back to one or two earlier newsletters by name.
9. Jargon defined inline at first use, in apposition: "the harness: the system around an agent, such as Claude Code or Codex". And "tmux (Terminal Multiplexer), a tool that manages multiple terminal sessions and keeps processes running in the background".
10. People credited by full name, with explicit thanks where earned, and often a LinkedIn or GitHub link. Community showcase posts are built entirely from this move.
11. A rhetorical question as a pivot: "What could go wrong?" and "But why?" and "So I started my Substack today. Now what?". This move is real in the archive but stylint now flags questions in prose, so new drafts make the statement instead ("Plenty could go wrong").
12. Personal life as scaffolding - school runs, gym rest periods, tram stops, his son's book requests - matter-of-fact and specific, never sentimental, always in service of the engineering problem. Present from the first month (the kids horror stories pipeline) to the latest posts.
13. One-line distilled verdicts: "An AI application without evaluation is only a demo". And "Structure beats search". And "When the assistant gives a bad answer, it's not because of the tech stack, but because of the data".
14. "It works like this:" or "Here's how it works:" followed by a sequence. This appears in over half the posts.
15. A direct request for reader response: "Let me know in the comments", "Reply to this email", "Ping me in the comments if you want to get slides". Heavier in the early months (one edition even ran a reader poll), but still present in current posts as a single question near the close.

## Things that never appear

Hype is entirely absent from the corpus, so words like `Revolutionary` and `game-changing` never appear, and neither do `delve`, `supercharge` or `unlock`. The posts call out that register outright:

> "Phrases such as 'AI-powered platform,' 'innovative solution,' and 'intelligent system' add little unless you explain what the system actually does".

Bold and italic do not appear in current essay prose (see the punctuation section for the early-2026 exception), and horizontal rules never appear anywhere in the corpus.

No throat-clearing opener in the essays, and no dictionary definitions. Abstract framing, where it exists at all, comes after the concrete personal case. The only greetings and housekeeping openers live in the December-February digest editions, and they died out.

No result without its limitation attached. Even launch posts have a caveat: "This is a brand-new platform, so some automations might not work perfectly yet".

The posts never claim certainty about the future:

> "Gemini Flash has not been tested yet for this workflow, so it isn't clear how much quality or cost would change".

Nobody gets moralised at, and second-person accusation never appears. The posts list common mistakes clinically, as in "A wall of text". and "A stale README"., rather than as "you're doing it wrong".

Paragraphs never run long, clauses never nest deeply, and elegant variation never happens. The same term repeats, so it stays the agent, the index and the workshop instead of rotating through synonyms.

Metaphor is almost entirely absent. The rare ones are homely and cashed out immediately: "grading its own homework", "flying blind", a README as "your landing page", "blast radius". Anything more literary reads as wrong.

## Vocabulary

These terms recur across the posts, and you should use them as-is:

- `coding agent` and `coding assistant` (also `AI assistant` for the chat tools), never "AI tool"
- `harness`, `orchestrator`, `subagent`, `session`
- `grooming`, `acceptance criteria`, `definition of done`, `backlog`
- `pipeline`, `workflow`, `human in the loop`, `spec-driven development`
- `sandbox`, `blast radius`, `skip-permissions`, `YOLO mode`
- `brain dump`, `dictation mode`, `voice notes` - the capture workflow is itself recurring subject matter
- `throw-away tools`, `dead weight`, `MVP`, `Zoomcamp`, `cohort`, `freestyle workshop`
- `tokens` as a consumable, as in "burned a huge pile of tokens" and "tokenmaxing"

These verbs come up again and again:

- `build`, `ship`, `run`, `dump`
- `wire`, `point at`, `hand`
- `iterate`, `polish`, `drift`, `land`

The register is technical-casual, and tool names, versions and prices are given exactly. Concepts get explained from zero at first use, on the assumption that readers are smart but may not know this particular corner. Any humour you find is dry and rare.

## Differences between post types

Build logs are the default voice and the dominant form since spring 2026. They rely on "I" and run chronologically through dated stages. Each failure comes paired with a rule, the repos get linked, and the piece ends on a reflective close.

Tutorials use instructional "we" plus imperative "you", numbered steps, verbatim prompts as code blocks, and de-escalations in the "don't overthink it" register. They end with a pointer to the next instalment or to resources. The July-August 2026 course-notes series adds a fixed head matter: a part list ("Part 1... Part 5: TBA") and "Subscribe to receive the next article in the series".

Digest editions, the dominant form from December 2025 to February 2026, bundle one shortish main topic with many recurring sections: work-in-progress notes, workshop recaps, course announcements (often repeated verbatim from the previous week), tools, and occasionally reader Q&A. The main topic follows build-log rules in miniature; the rest is apparatus.

Announcements run shorter and use "we" more often, at 1,650 to 2,000 words. They give bulleted benefits with explicit calls to action. They stay concrete regardless, with numbers like "81 members" and "27 participants", and they stay caveated. They only create urgency when it's real:

> "Registration is still open, and it closes on April 13".

The data-analysis posts use analytical "we" and put a percentage on every bullet, as in "Direct client engagement (90% of postings)". They state their own bias caveat ("But our data is probably biased because in our scrapes we focus on AI Engineering roles"), and they have the corpus's only "Conclusion" headings. They're the least personal pieces. A few of these are team-written digests of longer articles on aishippinglabs.com: they end with a "Read the full article" button rather than a reflective close, sometimes skip the apparatus entirely, and one even refers to Alexey in the third person ("Over the past months, Alexey has been researching market data"). Don't mix that team voice into a build log.

The third-party explainers (MemPalace, Karpathy's autoresearch) drop personal narrative almost entirely. They open on the news hook, give dense mechanism description with exact parameters read from the actual source, then close on an evaluative note or an idea to try:

> "There's nothing magical here - it's solid engineering with a few clever ideas".

Community showcase posts (demo days, graduate projects) run one short section per person or project: name, link, what they built, the stack, one interesting engineering challenge. Flat, generous, no ranking.

## How the style shifted over time

The corpus spans nine months, and the voice is stable but the format drifted. If you're matching current style, write like the posts from April 2026 onward.

December 2025 to February 2026, the digest era. Weekly multi-topic newsletters with greetings ("Hi everyone,"), holiday wishes, reader Q&A, sponsor thanks, repeated announcement blocks, bold list leads in body text, more exclamation marks, and the corpus's only emoticons. The main-topic essays inside them already had the signature voice: concrete openers, flat failure admissions, numbers everywhere.

February to March 2026, the research series era. The AI-engineer role research produced the analytical "we" posts, the team-written digests pointing to aishippinglabs.com, and the event-promotion blocks with calendar emoji. This is also when the biggest lore event happened (the dropped production database) and when self-referencing across posts became constant.

April 2026 onward, the essay era and the current default. One long essay-first build log per post, a bulleted roadmap after the opener, no bold in prose, few exclamation marks, no greetings, mermaid-style diagrams with data-bearing captions, and a compact apparatus. The reflective close plus principle plus forward teaser became standard.

July to August 2026, the series era layered on top. Course-notes tutorials with part lists and verbatim prompts joined the rotation, alternating with the build logs.

What never changed: first-person practitioner stance, concreteness in the first sentence, honest failure plus extracted rule, hedged estimates and deflated headline numbers, links to his own repos, personal life as scaffolding, "Edited by Valeriia Kuka" at the end.

## Where the linter is stricter than the archive

New drafts are gated by `stylint`, and the raw archive would not pass it clean. Some of that is scraping noise (smart quotes, image-embed URLs rendered as bare links). But some habits are real in the published posts and still banned going forward, so match the archive's voice while obeying the linter on these points:

- Sentence budget. The archive occasionally runs 26-48 word sentences with 4-5 commas; stylint caps sentences at 25 words and 3 commas. Split once at a clause boundary rather than chopping into fragments.
- Headings. The archive uses H3 and H4 sub-steps and the occasional question heading ("Why Do AI Agents Need Memory?"); new drafts use H2 only, no question headings, and carry step numbers in the heading text.
- Questions in prose. The archive pivots on "What could go wrong?"; stylint flags questions, so write the statement form.
- Word slips. "itself", "worth testing/packaging/saving", "source of truth", "at once", "very", and "signal" as a metaphor all appear a handful of times across nine months of posts, and all are banned now.
- Quote punctuation. Periods and commas go after the closing quotation mark in new drafts.
- Bare URLs. A few early posts drop a raw link in prose ("The source code is here: https://..."); new drafts always use `[name](url)`.
- Code fences. Always tag the language (```bash, ```python, ```text) and keep a connective sentence between blocks, which the archive already does.

Everything else in this document and the linter agree: short plain sentences, 1-3 sentence paragraphs, bulleted lists with colon lead-ins, no bold or italic in prose, no horizontal rules, no tables, contractions, concrete numbers.

## The checklist

Run a draft against this before publishing it. It targets the current (post-April-2026) default.

1. Open with the concrete problem you hit, first person past tense, a number or proper noun in the first sentence, two or three sentences before any framing. No greeting, no housekeeping.
2. Add "In this post, I'll share:" and four to six bullets.
3. Narrate chronologically: naive attempt, why it broke, what you built, what still doesn't work. Anchor the stages to months and years.
4. Give every claim a number, price, duration, file path or repo link. Hedge estimates. Deflate your own best numbers where honesty demands it.
5. Keep paragraphs to one to three sentences. Spaced hyphens, colons into lists and code, no bold or italic in prose. Verbatim agent prompts as code blocks, with a connective sentence before and after.
6. State each mistake in one flat clause, then extract a one-line rule from it.
7. For every choice, give the personal reason and the accepted downside.
8. Link back to the earlier newsletters this builds on, by name, and credit people by full name.
9. Close with a short reflective section that compresses the arc into a principle, points forward to a future post, and nudges the reader to subscribe.
10. Delete anything that sounds like marketing, any bold emphasis, any metaphor you wouldn't say out loud, and any claim with no evidence attached.
