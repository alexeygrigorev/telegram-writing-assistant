# Social Posts Guide — Teaser + Announcement

Every article ships with **two social moments**, each tailored to **three networks**:

- **POST 1 — Teaser**: posted ~2-3 days *before* the article goes live. Job: warm up the audience with a curiosity hook, no spoilers. Drives subscribes/follows.
- **POST 2 — Announcement**: posted *on publish day*. Job: tell people it's live, preview what's inside, link straight to the article.

That's **6 posts total** (2 moments × LinkedIn / X / Threads). No threads — single posts on every network.

Save them as `{slug}-social.md` in the current working directory, separate from the article draft (same `{slug}` as the draft file).

## Voice (same strict bans as the article)

The social posts use the **exact same voice rules** as the article. Read `references/voice.md` if you haven't. The ones that bite hardest on social:

- **No rhetorical questions.** The hook must be a *statement*: a bold claim, a specific scene, a number, a confession.
- **No em dashes.** Commas, periods, line breaks, parentheses.
- **No "not X, but Y" / "more than just X."** State the thing directly.
- **No hype words** (game-changer, unlock, supercharge, delve, leverage).
- **Mix sentence lengths**, use contractions, active voice.

**Statement-hook examples (good):**
- "Your RAG pipeline works in testing and breaks in production. The gap is almost always retrieval quality."
- "Most LLM eval suites test the model. The right ones test the pipeline."
- "I've seen the same RAG failure pattern in three companies this month. Wrote it all down."

**Question-hooks (avoid these):**
- "Why does your RAG pipeline fail in production?" → rewrite as a statement.
- "Ever wonder why LLM apps are hard to evaluate?" → rewrite as a statement.

## What to include / leave out

- **Hashtags: yes**, curated per network (see per-platform specs). Tune 1-2 of them to the article's specific topic.
- **Teaser link:** subscribe/follow CTA + `[SUBSCRIBE LINK]` (default: https://alexeyondata.substack.com).
- **Announcement link:** provide **both** placeholders: `[SUBSTACK LINK]` and `[MEDIUM LINK]`.
- **Emojis: no.** Keep social posts clean text.
- **Image briefs: no.** Alexey attaches his own visuals.

---

## Per-platform specs

### LinkedIn

Long-form friendly. The **first 2-3 lines are the hook** (everything after gets hidden behind "see more"), so front-load the strongest line and a line break before the fold.

**Format:**
- Line 1: statement hook.
- Blank line, then short 1-2 sentence paragraphs with whitespace between them.
- For the teaser: tease the tension and the promise, say when it drops, subscribe/follow CTA.
- For the announcement: a light preview of what's inside, one quotable line from the article, read-now CTA + both links.
- **3-5 hashtags** on their own line at the end. e.g. `#AI #LLM #MachineLearning #RAG` plus one topic-specific tag.
- Length: aim 600-1,300 characters.

### X (Twitter)

Tight. Assume the **280-character limit**. Front-load the hook in the first ~100 chars so it lands in the preview.

**Format:**
- Single post, ≤280 characters. **Include the character count** in the output (e.g. `(247/280)`). Count link placeholders as ~23 chars.
- **1-2 hashtags max.**
- Teaser: hook + "drops [day]" + subscribe link.
- Announcement: hook + link. No thread.

### Threads

Casual and conversational, like talking to peers. Up to **500 characters**.

**Format:**
- Conversational hook (still a statement, not a question).
- 1-3 short sentences.
- Teaser: casual "new piece drops [day]" energy + subscribe nudge.
- Announcement: casual "it's live" + one line on what's inside + link.
- **1-3 hashtags**, lighter touch.

---

## Teaser strategy (curiosity hook, no spoilers)

Tease the *tension and the promise* without handing over the goods.

- Open on the article's tension or claim, stated boldly.
- Name the territory ("RAG and retrieval quality," "LLM evaluation," "building AI agents") so the right readers lean in.
- **Withhold the payoff.** Don't list the framework's named parts, the code snippets, the steps, or the final verdict.
- Say when it lands ("this week", "Thursday", "in 3 days").
- Close with a subscribe/follow CTA.

**Hook flavors (pick the strongest per topic, mix across networks):**
- **Bold thesis statement.** "Evaluation is the bottleneck of every LLM project. Most teams don't even know theirs is broken."
- **Behind-the-scenes / personal.** "I've spent two weeks debugging a RAG pipeline that passed every test and failed every real query. Here's what I found."
- **Provocative stat or claim.** "Doubling your vector DB size can cut retrieval precision by 30%. Most teams are scaling the wrong thing."

## Announcement strategy

- Lead with "it's live" energy, stated not asked.
- Name the article's topic and angle.
- Preview what's inside in a sentence or two.
- Drop **one quotable line** lifted from the finished article. The bolded thesis line is usually the best pull.
- Clear read-now CTA + both links.

---

## Output file format

Save as `{slug}-social.md`:

```markdown
# {Article title} — Social Posts

> Article: {final title}
> Teaser: post ~2-3 days before publishing. Announcement: post on publish day.
> Announcement links: keep whichever you want per network.

---

## POST 1 — TEASER (post ~2-3 days before)

### LinkedIn
{copy, ending with [SUBSCRIBE LINK]}

{hashtags}

### X
{copy with [SUBSCRIBE LINK]}
({n}/280)

### Threads
{copy with [SUBSCRIBE LINK]}

{hashtags}

---

## POST 2 — ANNOUNCEMENT (publish day)

### LinkedIn
{copy}

Read it on Substack: [SUBSTACK LINK]
Or on Medium: [MEDIUM LINK]

{hashtags}

### X
{copy}
Substack: [SUBSTACK LINK] · Medium: [MEDIUM LINK]
({n}/280)

### Threads
{copy}

Substack: [SUBSTACK LINK] · Medium: [MEDIUM LINK]

{hashtags}
```
