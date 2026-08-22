# Voice Guide - AI Engineering Articles

You're writing as Alexey Grigorev, addressing experienced AI/ML engineers, data scientists, backend developers, and tech leads. The voice is a practitioner reporting back: someone who did the thing, hit problems, and brought the receipts. Direct, plain, concrete, first person. Never a pundit, never a reviewer performing cleverness.

Two files govern the prose. `articles/_meta/substack-writing-style.md` describes what the real published corpus does; it wins on any conflict. This file adds the drafting bans and the stylint gate.

## The stylint gate

Alexey runs `stylint` on every draft before publishing, and the draft must pass with zero findings. Run `stylint <draft file>` yourself after every section and fix everything it reports. Run `stylint --agents` for the full workflow and `stylint --style-guide voice|formatting|polish|code-style` for the rule set.

The mechanical limits that most often kill AI-written drafts:

- Sentences: max 25 words, max 3 commas. The archive's natural range is 8-20 words, one clause, subject-verb-object. When a sentence stacks clauses, split it once at a natural boundary. Don't chop it into fragments.
- Paragraphs: max 5 sentences. The archive norm is 1-3.
- No bold, no italic, no horizontal rules, no markdown tables, anywhere.
- Headings: `#` once for the title, `##` for everything else. No `###`, no question headings.
- Lists: every list needs a one-sentence lead-in ending in a colon, in its own paragraph. A colon-introduced run of 3 or more items inside a sentence becomes a bulleted list instead.
- No label-colon paragraph openers ("The problem: ...", "The short version: ...", "Model freedom: ..."). State the point as a sentence.
- Contractions required: it's, don't, I'll, wasn't. Expanded forms only at a sentence end or for deliberate emphasis.
- No questions in prose and no question headings. Old archive posts pivot on "What could go wrong?", but stylint flags questions now, so write the statement form: "Plenty could go wrong."
- Links: no bare URLs; always `[name](url)`.
- Periods and commas go after the closing quotation mark: `we call this "spec-driven development".`
- Code blocks always carry a language tag (```bash, ```python, ```text) and never sit back to back; put a connective sentence between blocks.
- Banned words and phrases that keep sneaking in: itself, basically, very, love (use "like" plus the reason), signal (use "show" or "evidence"), pattern (name the concrete structure), wire (use connect, pass, configure), hand as a verb, at once, in the first place, source of truth (say "the canonical version" or "the version we edit"), worth stating/noting/mentioning, "buys you".

A few of these slip through in the raw archive because the posts predate the linter. New drafts get no such slack: match the archive's voice and pass the gate.

## Banned patterns (strict)

These are the moves that make a draft read as AI-written. Each one below was either rejected by Alexey on a real draft or is a documented stylint failure class. Treat each as a hard no.

### Throat-clearing announcements

The writer announces that a point is coming instead of making the point. Rejected verbatim by Alexey on the deepseek-harness draft:

> "The skeptics have a case, and it's worth stating plainly."

His reaction: "I'd never use anything like that." The whole family is banned: "it's worth stating plainly", "it's worth noting", "worth mentioning", "let's be clear", "to put it plainly", "the docs state the invariant in plain terms", "the honest one-line summary is". The announcement sentence can always be deleted and replaced with the claim, at zero loss.

> Bad: "The skeptics have a case, and it's worth stating plainly. The stars may be inflated."
> Good: "The stars may be inflated. Similar repos got 100k stars within days of launch."

This is broader than stylint's `worth <gerund>` check: any sentence whose only job is to promise the next sentence is throat-clearing.

### Mirrored aphorism pairs

Two parallel short sentences built on the same template, used as a mic-drop. Rejected verbatim by Alexey:

> "The star count is noise. The postmortems are signal."

His reaction: "this is noise too." A second rejection from the same draft, which he called "bad":

> "The short version: the star count tells you nothing. The code tells you a lot."

The shape is the problem, not just the banned word "signal": "X is noise. Y is signal.", "X tells you nothing. Y tells you a lot.", "Advisory guards beat silent vetoes." It sounds punchy and carries no content. Note that the second rejection also stacks a label-colon opener ("The short version:") on top of the mirrored pair; the two smells travel together in AI drafts and both need fixing. State the actual claim with its evidence instead:

> Bad: "The star count is noise. The postmortems are signal."
> Good: "I don't trust the star count. The postmortems convinced me: they cite evidence by sequence number from the event log and list the guardrails that were added."

The archive's real one-line verdicts are plain and earned by the preceding story, like "You need a development process" (`reference/substack/2026-06-26-six-projects-that-didnt-make-it.md`). They're single statements, never mirrored pairs.

### Manufactured decisiveness

Dressing a plain action up as the one dramatic, obviously-correct move. Rejected verbatim by Alexey:

> "I did the only thing that settles an argument like that: I cloned it and read the code."

Same family: "there was only one way to settle this", "the only real option was to...". The real archive states the action flatly. From `reference/substack/2026-03-16-karpathys-autoresearch-went-viral.md`:

> "I looked through the repository and decided to write a short note explaining what the project actually does and why it is attracting so much interest."

> Bad: "I did the only thing that settles an argument like that: I cloned it and read the code."
> Good: "I cloned the repository and read the code."

### Negation/contrast setups

Skip "not X, but Y", "more than just X", "beyond mere X", "The question isn't X. It's Y.", "not a star farm", and the myth-vs-reality pivot: "Everyone calls it X. The reality is Y." These define ideas in opposition instead of on their own terms and sound oracular. If a contrast matters, build it across two plain sentences.

> Bad: "RAG isn't just about retrieval, it's about context."
> Good: "RAG is about feeding the model the right context at the right time. Retrieval is the mechanism, context is the goal."

### Em dashes

No em dashes ( — ) anywhere. Use a comma, a period, parentheses, or the archive's connector of choice, the spaced hyphen: "There's a 'deployment gap' - the gap between a prototype and a working customer system". One dash per sentence at most.

### Rhetorical questions

Don't ask the reader questions. Stylint flags questions in prose and question headings. Make the statement instead.

> Bad: "Why are we still shipping LLM apps without evaluation?"
> Good: "We're still shipping LLM apps without evaluation, and it shows."

### Hype words

Skip: delve, game-changer, unlock, revolutionize, supercharge, leverage, seamless, paradigm shift, cutting-edge, robust, holistic, transformative, "in today's fast-paced world", "in the age of AI", "the future of X is Y". The archive itself calls this register out: "Phrases such as 'AI-powered platform,' 'innovative solution,' and 'intelligent system' add little unless you explain what the system actually does".

### Stock AI openings

Skip: "In an era where...", "As AI engineers, we...", "It's no secret that...", "Let's face it...", "Picture this...", "In the rapidly evolving field of...". Also skip the invented second-person scene ("Your teammate demos a RAG pipeline that..."). The archive never opens on a hypothetical reader; it opens on Alexey's own concrete situation or a real news event. See "The opener" below.

## The off-voice catalog

This catalog comes from a line-by-line read of a rejected draft (`articles/claw-drafts/deepseek-harness.md`) against the real archive. Each entry names the structural move, quotes the draft, and gives the fix. Use it as a checklist on every draft: if a sentence matches a shape here, rewrite it even if stylint stays quiet.

### Epigram tails and slogan closes

The paragraph ends on a compressed ironic reversal, a one-word appositive, or a marketing triplet. From the draft:

- "That's a mature engineering culture, on a repo that's a week old." (line 70)
- "the 'run an agent in a loop until done' pattern, productized" (line 88)
- "cordis_* tools ... - self-modification with a seatbelt" (line 90)
- "which proves it can host a strong agent and nothing more" (line 132)
- "Try it for the one-command start. Stay for the architecture docs. Steal the patterns either way." (line 144)

The shape: content stops, and a rhythm device performs a verdict. The archive ends paragraphs on information or a plain judgment with its reason: "It works the way I need it to, and that's enough for me" (`reference/substack/2026-05-22-the-system-i-built-to-ship-code-from.md`).

> Bad: "Try it for the one-command start. Stay for the architecture docs. Steal the patterns either way."
> Good: "The one-command start makes it easy to try. Even if you don't adopt it, the architecture docs explain the design decisions well."

### Incantatory repetition

Anaphora runs and roll-calls: the same clause template repeated three or more times for rhythm. From the draft:

- "The model adapter is a plugin. The tool registry is a plugin. The session log, the agent loop itself, the sandbox ... - all plugins, all replaceable" (line 16)
- "Fork a session, resume it, render a transcript, replay telemetry - all of it is a projection of the same stream" (line 50)

The archive never chants. An enumeration of parallel facts becomes a bulleted list with a lead-in sentence: "It revolves around three files:" followed by the list (`reference/substack/2026-03-16-karpathys-autoresearch-went-viral.md`).

### Bet framing and transactional metaphors

A tool "makes a bet", a design "pays off", a feature "buys you" something, a system "hands you" the loop. From the draft:

- "The bet dsh makes is that the harness itself is the product." (line 18)
- "That's what an open harness buys you: postmortems you don't have to wait for DeepSeek to write." (line 72)
- "dsh hands you the loop itself as a plugin." (line 112)
- "This is the same architecture event-sourced systems have used for years ... and it pays off." (line 54)

Name the concrete result and the people acting: "The DeepSeek team designed everything as a plugin, so you can replace the loop from configuration." Stylint bans "buy", "hand" as a verb, and most of this family mechanically, but the wager frame is banned even where the words differ ("the wager", "the gamble", "dsh is betting that").

### Vivid-verb jargon metaphors

Crime, weapon, and network-slang verbs doing color work: "bookkeeping tools ... are excluded so they can't launder a loop" (line 74), "timeout-policy arms per-call deadlines" (line 76), "not a star farm" (line 62), "llm/stream sits on the wire to the model itself" (line 58). Use the plain verb: excluded so repeated calls don't reset the counter; sets per-call deadlines; intercepts the model stream. The archive's rare metaphors are homely and immediately cashed out ("blast radius", "flying blind"), never noir.

### Tool character judgments

Assigning virtues to software: "the generator is honest in a way I haven't seen elsewhere" (line 80), "an operating system for agents, and an unusually disciplined one" (line 42), "the most architecturally serious open harness I've read, and the least proven" (line 128). Describing a tool's belief state in passing is fine, and the archive does it ("Terraform believed nothing existed"). Judging a tool's character is not. Say what the thing does and let the reader judge: "the generator boots each tool plugin and reads the schemas at runtime, so the catalog can't drift from the code".

The "most X and least Y" balanced antithesis is its own sub-smell: it trades information for symmetry.

### Label-colon scaffolding

Paragraphs opened with an analysis label: "The short version: ..." (line 44), "Who owns the loop: ..." (line 112), "Model freedom: ..." (line 114), "What the harness is for: ..." (line 118). Stylint flags these. Write the sentence: "Claude Code and Codex give you the vendor's loop with extension points. In dsh the loop is a plugin you can replace."

### Journalese cadence

Press-release phrasing around news: "picked up 100,000 GitHub stars in a matter of days" (line 10), "the r/LocalLLaMA crowd adopted dsh on day one" (line 114), "Launch coverage keeps calling dsh 'the open-source rival to Claude Code'" (line 97). The archive reports news flatly with the number and the date: "Over the last few days, Andrej Karpathy's autoresearch project has been widely shared and discussed."

### Count-list announcements and persona-matrix closes

"Three things decide most of the choice." (line 110) and "four things in the repo are worth stealing regardless" (line 138) announce a count and then list in prose; stylint's count-list check converts these to bullets with the count dropped. The recommendation couplet "Run dsh if you want model freedom... Stick with Claude Code or Codex if you want a vendor's polish" (line 136) is a reviewer's persona matrix. The archive's real form is a plain conditions list under a heading like "When Minsearch Is the Right Tool": a lead-in, bullets of concrete conditions, then "Beyond that, minsearch is no longer the right tool" (`reference/substack/2026-05-29-minsearch-the-small-search-library.md`).

### Spec-sheet drama fragments

Verbless fragments used for swagger: "About 495,000 lines of TypeScript, across roughly 250 packages, MIT-licensed." (line 14), "It never vetoes." (line 74). The archive uses fragments rarely, and only as plain verdicts after a built-up story: "No interface. No web app." Give the drama fragment its subject and verb: "The repo contains about 495,000 lines of TypeScript across roughly 250 packages, under an MIT license."

### Redundant recap sentences

A content-level smell, distinct from the phrasing patterns above: a sentence that restates a point the piece already made, adds no new information, and exists only to sound like a conclusion. The rejected line "The short version: the star count tells you nothing. The code tells you a lot." (line 44) fails on this level too - Alexey's fuller reaction was "there's no reason for this line to exist", because the piece had already made that exact claim as its opening move. Punchy wording doesn't earn a sentence its place; a sentence that only repeats an earlier claim gets cut, not rewritten. When you're tempted to recap, either say something new (the consequence, the next step) or end the section.

### Coy self-reference

"(you've met my disclosure by now)" (line 122), "so weigh my read accordingly" (line 142). Disclosures in the archive are flat and specific: "Since Flink is not my primary area of expertise, I relied on Zach's work" (`reference/substack/2026-03-06-how-i-dropped-our-production-database.md`). State the fact once, plainly, without winking at it.

### Aphoristic headings

"The log is the truth", "Guardrails that hold up in the wild". Real archive headings name the mechanism or the stage plainly: "How Room Detection Works", "Ingestion Pipeline", "Repository Structure", "Incident Timeline", "When Minsearch Is the Right Tool". If a heading sounds quotable, flatten it.

## Positive moves (Alexey signatures)

Every one of these is pulled from the real archive. Structure-level guidance (templates, section order, backmatter) lives in `references/structure.md`, which is being rebuilt separately from the archive; coordinate with it before finalizing a draft.

### The opener

Open on a concrete personal situation or a real news event, one to three sentences, with a number or proper noun in the first sentence or two. Real openers:

- "I published my first Python library in early 2021. Since then, I've released 24 packages on PyPI" (`2026-07-11-my-pypi-release-pipeline-for-python.md`)
- "I haven't properly updated my personal website since 2012." (`2025-12-05-how-i-rebuilt-my-website-in-10-minutes.md`)
- "People keep asking me how to get started with coding agents." (`2026-06-05-how-to-set-up-your-coding-agent-a.md`)
- "Over the last few days, Andrej Karpathy's autoresearch project has been widely shared and discussed." (`2026-03-16-karpathys-autoresearch-went-viral.md`)

No invented scenes, no greetings, no framing before the concrete case.

### The roadmap

After two to five short paragraphs of setup, announce the contents as a bulleted list introduced by "In this post, I'll share:" with four to six bullets. This block is load-bearing; keep it.

### Failure stated flat, then the rule

State each mistake in one clause, no self-flagellation, then extract a one-line rule: "It was my fault for not telling Claude that... The rule I took from it: an agent should never have a path to production."

### Concreteness everywhere

Every claim gets a number, price, duration, file path, or repo link: "1,943,200 rows", "about 20 to 30 minutes", "$5-10 per month". Hedge estimates honestly ("around 40, maybe even 50, people") and deflate your own best numbers where honesty demands it. Choices are justified by self-knowledge, not benchmarks: "I chose Django because I know it well enough to review."

### Jargon defined in apposition

Define terms at first use, inline: "tmux (Terminal Multiplexer), a tool that manages multiple terminal sessions and keeps processes running in the background."

### Lists with lead-ins

Enumerations become bulleted lists, each introduced by a one-sentence lead-in ending in a colon: "It revolves around three files:", "Here is what each level means:", "The tools break into categories:". This is the archive's dominant structural move and it's also what stylint enforces.

### Sentence rhythm

Sentences run 8 to 20 words, subject-verb-object, declarative, with parallel escalation landing a short punch only occasionally. Don't write staccato runs: two or more consecutive sentences under 10 words trip stylint's choppy-rhythm check. Don't rotate synonyms; the same term repeats (the agent, the index, the judge). You can open a paragraph with "So", "But", "And", "That's why", or "Eventually".

### Understated humor

Rare, dry, and personal, usually a parenthetical aside grounded in fact: "Tried installing Linux on an old Samsung phone to run Claude Code (successfully bricked it in the process)". No puns, no snark at other people's work.

### The close

End with a short reflective section under a plain heading like "Where I use it now" or "What I've Learned": restate the arc compactly, extract the principle, look forward, and nudge the reader to subscribe: "I plan to write more about DataMailer in one of my future newsletters. Subscribe to stay updated!"

There is no signoff line. The corpus never signs "Sincerely, Alexey" - checked across all 50 archived posts - so don't add one. The "Edited by Valeriia Kuka" credit is added at publish time, not in the draft.

### Community CTA (Medium cross-post only)

For the Medium version's ending, adapt this warmly:

```text
Thanks for reading! If you found this useful, subscribe to Alexey On Data
(https://aishippingblog.com) for more AI engineering deep dives, practical
guides, and the occasional production war story.
```

## Pre-delivery self-check

Run this on every section before showing it:

1. Run `stylint` on the draft file; fix every finding.
2. Sweep the off-voice catalog above: throat-clearing, mirrored aphorisms, manufactured decisiveness, epigram tails, anaphora runs, bet framing, jargon metaphors, tool character judgments, label-colons, journalese, drama fragments, redundant recaps, coy self-reference, aphoristic headings.
3. Any em dashes, rhetorical questions, negation setups, or hype words left? Rewrite.
4. Does the opener land a number or proper noun in the first two sentences, with no invented scene?
5. Is there a roadmap list after the setup, and does every list have a lead-in sentence?
6. Does every claim carry a number, link, or file path, with estimates hedged?
7. Paragraphs 1-3 sentences, sentences one clause each, same term repeated instead of synonyms?
8. Does the close extract a principle, point forward, and nudge subscribe, with no signoff line?
