# Social Posts Guide — Teaser + Announcement

Every article ships with **two social moments**, each tailored to **three networks**:

- **POST 1 — Teaser**: posted ~2-3 days *before* the article goes live. Job: warm up the audience with a curiosity hook, no spoilers. Drives subscribes/follows.
- **POST 2 — Announcement**: posted *on publish day*. Job: tell people it's live, preview what's inside, link straight to the article.

That's **6 posts total** (2 moments × LinkedIn / X / Threads). No threads — single posts on every network.

Save them as `{slug}-social.md` in the current working directory, separate from the article draft (same `{slug}` as the draft file).

## Voice (same strict bans as the article)

The social posts use the **exact same voice rules** as the article. Read `references/voice.md` if you haven't. The ones that bite hardest on social:

- **No rhetorical questions.** Social tempts you to open with "Ever wondered why...?" Don't. The hook must be a *statement*: a bold claim, a specific scene, a number, a confession. Statements stop the scroll just as well and they fit Vadym's voice.
- **No em dashes.** Commas, periods, line breaks, parentheses.
- **No "not X, but Y" / "more than just X."** State the thing directly.
- **No hype words** (game-changer, unlock, supercharge, delve, leverage).
- **Mix sentence lengths**, use contractions, active voice.

**Statement-hook examples (good):**
- "AI doesn't try harder when you give it more. Usually it gets lost."
- "Anyone can ship a working app this year. That's exactly why most of them will feel forgettable."
- "LinkedIn tells you 93 people viewed your profile. It will never tell you who. That gap is the entire product."

**Question-hooks (avoid these):**
- "Why does adding more context make AI worse?" → rewrite as a statement.
- "Ever notice every SaaS app looks the same?" → rewrite as a statement.

## What to include / leave out

- **Hashtags: yes**, curated per network (see per-platform specs). Tune 1-2 of them to the article's specific topic.
- **Teaser link:** subscribe/follow CTA + `[SUBSCRIBE LINK]`.
- **Announcement link:** the article is published on two homes, so provide **both** placeholders and let Vadym keep whichever he wants per network: `[SUBSTACK LINK]` and `[MEDIUM LINK]`.
- **Emojis: no.** Keep social posts clean text. (The article's own emoji, if any, stay in the article.)
- **Image briefs: no.** Vadym attaches his own visuals.

If Vadym gives his Substack URL, Medium URL, and handles, bake them in instead of placeholders.

---

## Per-platform specs

### LinkedIn

Long-form friendly. The **first 2-3 lines are the hook** (everything after gets hidden behind "see more"), so front-load the strongest line and a line break before the fold.

**Format:**
- Line 1: statement hook.
- Blank line, then short 1-2 sentence paragraphs with whitespace between them. LinkedIn rewards airy formatting.
- For the teaser: tease the tension and the promise, say when it drops, subscribe/follow CTA.
- For the announcement: a light preview of what's inside, one quotable line from the article (the bolded thesis often works), read-now CTA + both links.
- **3-5 hashtags** on their own line at the end. e.g. `#design #UX #productdesign #designthinking` plus one topic-specific tag.
- Length: aim 600-1,300 characters. Long enough to give value, short enough to stay crisp.

### X (Twitter)

Tight. Assume the **280-character limit**. Front-load the hook in the first ~100 chars so it lands in the preview.

**Format:**
- Single post, ≤280 characters. **Include the character count** in the output (e.g. `(247/280)`) so Vadym can confirm it fits. (When you include the link placeholder, count it as ~23 chars, X's t.co length.)
- **1-2 hashtags max.** X punishes hashtag stuffing.
- Teaser: hook + "drops [day]" + subscribe link.
- Announcement: hook + link. No thread, keep it to the single post.

### Threads

Casual and conversational, like talking to peers. Up to **500 characters**. Less hashtag-driven than the others.

**Format:**
- Conversational hook (still a statement, not a question).
- 1-3 short sentences.
- Teaser: casual "new piece drops [day]" energy + subscribe nudge.
- Announcement: casual "it's live" + one line on what's inside + link.
- **1-3 hashtags**, lighter touch.

---

## Teaser strategy (curiosity hook, no spoilers)

An article is a single topic, so you can't hide "the product" the way the newsletter teaser does. Tease the *tension and the promise* without handing over the goods.

- Open on the article's tension or claim, stated boldly.
- Name the territory ("AI and your design system," "why every app feels the same") so the right readers lean in.
- **Withhold the payoff.** Don't list the framework's named parts, the checklist items, the steps, or the final verdict. Those are the reasons to open the article.
- Say when it lands ("this week", "Thursday", "in 3 days").
- Close with a subscribe/follow CTA so new readers don't miss it.

**Hook flavors (pick the strongest per topic, mix across the three networks):**
- **Bold thesis statement.** Lead with the article's core claim, flat and confident. "Functional design was never enough. AI just made that impossible to ignore."
- **Behind-the-scenes / personal.** The "here's what I've been wrestling with" angle. "I've spent two weeks trying to explain why some products feel premium and others feel hollow. Wrote it all down."
- **Provocative stat or claim.** Open on a surprising number or counterintuitive fact, sourced in the article. "Doubling the context you give AI can cut its accuracy by 40%. Most designers are doing the opposite."

## Announcement strategy

- Lead with "it's live" energy, stated not asked.
- Name the article's topic and angle.
- Preview what's inside in a sentence or two (you can reveal the framework or method now).
- Drop **one quotable line** lifted from the finished article. The bolded thesis line is usually the best pull.
- Clear read-now CTA + both links (`[SUBSTACK LINK]` and `[MEDIUM LINK]`), labeled so Vadym keeps whichever he wants per network.

---

## Output file format

Save as `{slug}-social.md`:

```markdown
# Eidos Design — {Article title} Social Posts

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
