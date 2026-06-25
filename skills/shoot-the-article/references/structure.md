# Structure Guide — Article Templates

Open this file once a template is chosen. It covers title and subtitle craft, the shared article anatomy, the four templates with word norms and annotated scaffolds, image conventions, and the final-draft file structure.

---

## Title and subtitle

### Title style

Eidos / Medium titles are descriptive and confident. The most common form is `Main idea: a practical promise`:

- *Context engineering: A repeatable AI workflow for product designers*
- *How LinkedIn (and Other Products) Play With Our Minds: The Psychology Behind The Nudges*
- *Feelings Are The New Features*

Offer **3-5 options, mixing flavors:**

- **Descriptive:** says plainly what the reader gets. *"Context engineering: A repeatable AI workflow for product designers."*
- **Thesis / curiosity:** stakes a claim or opens a gap. *"Feelings Are The New Features."*
- **Tension:** X vs. Y or a provocation with a follow-on. *"Love vs. Infatuation: why the best products know when to let you go."*
- **Clickbait-leaning (include at least one):** a number, a curiosity gap, a parenthetical promise. *"The One Thing AI Can't Fake (And Why It'll Define Design)."*

### Subtitle

A **single descriptive sentence** that works as both the Substack subtitle and the Medium deck. It previews the payoff. Offer **3 options**.

Examples from the real pieces:
- *"A step-by-step method to feed AI the right inputs in the right order, without prompt gymnastics."*
- *"A strategic framework for emotional design when function is free."*
- *"The Science of Attention: A Playbook for Engagement."*

---

## Shared article anatomy

Whatever the template, every article has this spine:

1. **Title + subtitle** (offered as options in Step 2).
2. **Hook** (1-2 short paragraphs). A concrete scene, a counterintuitive linked stat, or a specific moment. No rhetorical questions, no "in an era where."
3. **Framing** (1-2 paragraphs). Pivot from the hook to what the piece argues or teaches. State the thesis in plain language.
4. **Body** — H3 sections with evocative, scannable headings. This is where the template shape lives.
5. **Practical artifact** when it fits — a checklist, framework, comparison, or step list the reader can lift.
6. **Close** (1-2 short paragraphs). A personal landing, often "Here's what I believe:", that ties back to the spine and leaves a takeaway. Then the signoff.
7. **Signoff:** `Sincerely,` / `Vadym Grin` (and the Medium community CTA in the platform deltas).

Headings are H3 (`###`) and named with personality, not generic labels. Real examples: "A chorus of echoes," "The psychology of feeling something," "Why context matters more than commands," "The Curiosity Gap: Guess Who?"

---

## Template 1 — Practical Workflow / Method

*Reference piece: Context engineering. Best for a repeatable method, system, or workflow.*

**Default length: 1,800-2,400 words.**

### Structure

1. **Hook** — a counterintuitive claim with a linked stat that reframes a common habit.
2. **Why it matters** — 2-4 short paragraphs establishing the problem with evidence. Stack a few linked stats here; this template is the most data-forward.
3. **The method, broken into named parts** — numbered layers, steps, or tiers, each an H3. Each part: what it is, what it's for, a concrete example, ideally a linked source.
4. **A before/after or commands-vs-context style contrast** — show the wrong way and the right way side by side.
5. **The practical artifact** — a checklist or copy-pasteable framework (see below). This template almost always carries one.
6. **"How to know it's working"** — a "good signs / warning signs" pair of lists.
7. **Strategic implications** — zoom out to what this means for individual designers, teams, and orgs.
8. **Close** — the reassuring landing (you already have these skills, here's the new way to use them) + signoff.

### The artifact for this template

A checklist or framework template in fenced code blocks the reader can copy:

```
SYSTEM CONTEXT:
[Design tokens and component examples]
BRAND CONSTRAINTS:
[Specific brand rules and boundaries]
TASK:
[The specific design need]
SUCCESS CRITERIA:
[What good output looks like, be specific]
```

Or a grouped checklist ("System Context: …", "Brand Context: …") of yes/no questions.

---

## Template 2 — Strategic Essay + Framework

*Reference piece: Feelings Are The New Features. Best for an argument that resolves into a named, reusable framework.*

**Default length: 1,800-2,400 words.**

### Structure

1. **Scene hook** — a vivid, specific moment that sets up the tension.
2. **Reframe the problem** — an H3 that names the real question and answers it plainly. Cite a thinker or a piece if one anchors it (e.g. Jakob Nielsen, Don Norman).
3. **Build the argument** — 2-3 H3 sections moving through evidence and one **extended metaphor** ("a chorus of echoes"). Drop the **bolded thesis line** here.
4. **The framework** — a numbered set of named dimensions (e.g. *Delight, Trust, Surprise, Nostalgia*). For each item, follow this exact sub-pattern:

```markdown
### N. {Dimension}: {short evocative tagline}

[1-2 sentences defining it.]

**The psychology:** [Why it works on people, 2-3 sentences. Link research if you have it.]

**Practical applications:**
- **[Lead-in phrase].** [Concrete example naming a real product, linked.]
- **[Lead-in phrase].** [Another concrete example.]

**The trap to avoid:** [The failure mode, 1-2 sentences.]
```

5. **Close** — a personal "Here's what I believe:" landing that states the stakes, plus signoff.

### Notes

- The framework is the artifact. Keep the items parallel in shape so the reader can scan and reuse them.
- Each dimension needs at least one named, linked product example.

---

## Template 3 — Psychology / Principles Explainer

*Reference piece: How LinkedIn Plays With Our Minds. Best for decoding why a product or pattern works on us. Often runs shorter (800-1,500 words).*

### Structure

1. **Relatable hook** — a specific, common experience, stated (not asked). "Most of us have gotten that LinkedIn email."
2. **Set up the teardown** — one short paragraph promising to break it down. A little wink is welcome ("And of course we'll break it down").
3. **One principle per H3, each with a witty quoted subhead** — the heading names the principle's effect; the body names the formal principle in *italics*, links a real source for it, and explains the mechanism with the concrete example.

```markdown
### The Curiosity Gap: "Guess Who?"

They tell you how many people viewed your profile, never who. That gap is engineered. It's the *curiosity gap*, described in [The Information Gap Theory of Curiosity](link) by George Loewenstein. Incomplete information itches. You log back in to scratch it.
```

4. **"How other products do it" roundup** — an emoji-bulleted list applying the same lens across products, each tied to a named principle:

```markdown
🖼 **Instagram:** the red notification badge isn't decoration. It's the *von Restorff effect* engineering urgency.
🎥 **YouTube:** autoplay rides the *Law of Continuity* and our tendency to binge.
🛍️ **Amazon & Booking.com:** "Only 2 left!" weaponizes *scarcity* and FOMO.
```

5. **Recap list** — a short list of the principles covered, ideally each linked, so readers can go deeper.
6. **Community CTA** — this template usually closes on the Medium "join the Eidos Design community… spreading the love, folks 🤗" CTA rather than the formal signoff.

### Notes

- Personal parenthetical asides shine in this template (the Zeigarnik / Soviet Union aside).
- Name the formal principle every time and link it. The credibility is in the citations.

---

## Template 4 — Product Teardown

*No single reference article among the samples; borrows the newsletter's Don Norman option. Best for a deep read of one product through a designer's lens.*

**Default length: 1,200-2,000 words.**

### Structure

1. **Framing** — why this product, why now, what designers can learn from it.
2. **Guided walkthrough by dimension.** Two options:
   - **Emotional read:** use **Don Norman's 3 levels** — Visceral (first impressions), Behavioral (usability, performance), Reflective (long-term meaning, identity). Score each X/5 with a one-line italic *emotional signal* quote in the user's voice, then an **Overall: X/5 ⭐**. Disclaimer: *Reminder: evaluated against [Don Norman's 3 levels of design](https://www.interaction-design.org/literature/article/norman-s-three-levels-of-design).*
   - **Heuristic read:** walk 4-6 named dimensions you choose (onboarding, information architecture, microcopy, motion, empty states), each with specific observations.
3. **"What designers can steal"** — the practical artifact: 3-5 transferable patterns the reader can apply to their own work.
4. **Verdict** — an honest landing on where it shines and where it falls short, plus signoff.

### Notes

- Review from real use or deep reading, never on vibes. Specific observations beat adjectives ("the onboarding is 5 screens" beats "smooth onboarding").
- Link the product on first mention, and any other tools or designers referenced.

---

## Images

Leave a clearly-marked placeholder at the spot the visual belongs. Write captions the way the published pieces do: numbered, plain, naming the products shown.

```
[IMAGE: side-by-side loading screens]
Caption: 1. 5 Minute Journal with a generic spinner. 2. Stoic, with a descriptive, reassuring loading screen.
```

Don't embed real images. One lead image near the top plus 2-4 inline visuals is typical for a deep dive.

---

## Final draft file structure

After all sections are approved, save as `{slug}-draft.md` with this layout:

```markdown
# {Working title — Vadym's pick or the top option}

> Subtitle: {chosen subtitle}

[Lead image placeholder]

{Hook through close, in full publish-ready markdown, ending with the Sincerely / Vadym Grin signoff}

---

## Platform Deltas

**Substack (Eidos Design):**
- Subtitle: {chosen subtitle}
- Paywall: place `[PAYWALL BREAK — free preview ends here]` after {section}. (Eidos articles are paid; the free preview usually runs through the hook and first one or two sections.)
- Ends on the Sincerely / Vadym Grin signoff.

**Medium (UX Collective / UX Planet / The Startup):**
- 5 topic tags: {e.g. AI, UX Design, Product Design, Design Systems, Prompt Engineering}
- Member-only: yes/no (Vadym's call).
- Ends on the community CTA: "Thanks for reading! If you found this useful, join the Eidos Design community on Substack… it's about spreading the love, folks 🤗"

---

## SEO Keywords

- 8-12 keywords/phrases mixing head terms (e.g. "emotional design," "AI for designers") and long-tail phrases tied to the article's specific topic.

---

## Title & Subtitle Shortlist (for publish-time selection)

### Titles
1. ...
2. ...
3. ...

### Subtitles
1. ...
2. ...
3. ...
```
