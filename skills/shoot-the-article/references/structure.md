# Structure Guide — Article Templates

Open this file once a template is chosen. It covers title and subtitle craft, the shared article anatomy, the template set (five slots, one deprecated) with word norms and annotated scaffolds, code and image conventions, and the final-draft file structure.

---

## Title and subtitle

### Title style

Titles are descriptive and confident. The most common form is `Main idea: a practical promise`:

- *Evaluation-Driven Development: A practical framework for shipping LLM apps*
- *How Vector Search Actually Works: From embeddings to production*
- *RAG Is Not a Search Problem*

Offer **3-5 options, mixing flavors:**

- **Descriptive:** says plainly what the reader gets. *"Building a Production RAG Pipeline: A step-by-step guide."*
- **Thesis / curiosity:** stakes a claim or opens a gap. *"Evaluation Is the New Unit Test."*
- **Tension:** X vs. Y or a provocation with a follow-on. *"Prompts vs. Pipelines: Why your LLM app needs more than good instructions."*
- **Clickbait-leaning (include at least one):** a number, a curiosity gap, a parenthetical promise. *"The One Thing Missing From Your RAG Pipeline (And How to Fix It in 10 Lines)."*

### Subtitle

A **single descriptive sentence** that works as both the Substack subtitle and the Medium deck. It previews the payoff. Offer **3 options**.

Examples:
- *"A step-by-step method for building retrieval pipelines that survive production traffic."*
- *"A practical framework for evaluating LLM applications beyond vibes-based testing."*
- *"From prototype to production: how to ship AI features that don't hallucinate at scale."*

---

## Shared article anatomy

The default shape across most of Alexey's posts, per `articles/_meta/substack-writing-style.md`, is the build log: a concrete personal opener, a roadmap, a chronological progression through dated stages, and a reflective close. Every template below is a variant of this spine, not a replacement for it - read the style doc's "The skeleton" and "The close" sections before drafting, and default to the Build Log template (below) unless the topic clearly fits one of the others.

1. **Title + subtitle** (offered as options in Step 2).
2. **Opener** (1-3 short sentences, first person, past tense). A concrete personal situation, not a general framing - a number or proper noun should land in the first sentence or two. No rhetorical questions as a setup, no "in the age of AI."
3. **Roadmap** (after 2-5 short paragraphs of setup). Announce what the piece covers, either as a bulleted list introduced by "In this post, I'll share:" or the same move in running text. This block is load-bearing - keep it.
4. **Body** — H2 sections (not H3) with plain, short headings, mostly noun phrases ("The workshop problem," "Grooming: the product manager agent"), five to nine of them before any closing apparatus. This is where the template shape lives.
5. **Practical artifact** when it fits — a checklist, framework, code snippet, or step list the reader can lift.
6. **Close** (three to eight short paragraphs, under a plain heading like "Where I use it now" or "What I've Learned"). Restate the arc compactly, extract the principle, look forward. Then the signoff.
7. **Signoff:** `Sincerely,` / `Alexey` (and the Medium community CTA in the platform deltas).

Headings are H2 (`##`), short and plain, mostly noun phrases with no cleverness. Real examples: "A kernel with no core," "The log is the truth," "What people actually say," "The rule I took from it." Reserve H3 for enumerated sub-steps inside an H2 section.

---

## Template 1 — Build Log (default, most common)

*Best for narrating how something was built, fixed, broken, or figured out - the shape most of Alexey's posts actually use. Default to this template unless the topic clearly fits one of the others below.*

**Default length: 1,800-2,400 words.**

### Structure

1. **Opener** — a concrete personal situation, first person, past tense, one to three sentences, before any framing or thesis. A number or proper noun lands in the first sentence or two. Example shape: "I sometimes run offline workshops. These workshops require participants to have access to cloud resources such as AWS."
2. **Roadmap** — after 2-5 short paragraphs of setup, announce the contents, as a bulleted list introduced by "In this post, I'll share:" or the same move in running text.
3. **The chronological build** — narrated forward through time, each stage anchored to a specific month or date ("In October 2025, I built...", "Around December 2025..."). Each stage exists because the previous one broke. Within this:
   - Show the naive first attempt and why it failed, before showing what replaced it: "The obvious choice was X, so I tried that first. It broke almost immediately."
   - State each mistake in one flat clause, no self-flagellation, then extract a one-line rule from it: "It was my fault for not telling Claude that... The rule I took from it: [principle]."
   - Justify choices by self-knowledge rather than benchmarks where that's honest: "I chose Django because I know it well enough to review."
   - Give every claim a number, price, duration, file path, or repo link. Hedge estimates rather than rounding confidently, and deflate your own best numbers where honesty demands it.
4. **Where it stands now** — including what still doesn't work. No result ships without its limitation attached.
5. **Close** — a short reflective section, three to eight short paragraphs, under a plain heading like "Where I use it now" or "What I've Learned." Restate the arc compactly, extract the principle, look forward. Then the signoff.

### Notes

- This is the template the deepseek-harness / durable-agents style third-party-analysis pieces should still borrow the arc from, even though they drop personal narrative for the middle sections (see Template 5).
- Read `articles/_meta/substack-writing-style.md` section "The skeleton" and "The signature moves" before drafting this template - the failure-then-rule pairing and the naive-attempt-first move are what make it read as a story instead of a spec sheet.

---

## Template 2 — Practical Workflow / Method

*Best for a repeatable method, a named framework, or a set of steps the reader can copy into their own project. Grounded in "My PyPI Release Pipeline for Python Libraries," "How to Set Up Your Coding Agent," "Getting an AI Engineering Job," "Choosing a Portfolio Project," and "How to Write a Good README."*

**Default length: 1,800-2,400 words.**

### Structure

1. **Opener** — a concrete personal situation or a plainly stated problem, one to three sentences, before any framing. No stat-led hook. Real openers: "I published my first Python library in early 2021. Since then, I've released 24 packages on PyPI" and "Your README is the first file people read in your project, and sometimes the only one."
2. **Roadmap** — the method stated once, as a short bulleted or numbered list, right after the opener, per the shared anatomy.
3. **Name the method, if it has a name** — some pieces brand it early: "The Project-Selection Framework" (Choosing a Portfolio Project) or "The Job Search Algorithm" (Getting an AI Engineering Job). Others go straight into the steps without naming them.
4. **Walk the steps in order, one H2 per step, and number the heading itself** — real headings carry the step number: "1. Start with an Idea" through "6. Automate Publishing with Skills" (PyPI pipeline), "Step 1: Choose an Assistant" through "Step 6: Use Subagents When Context Gets Too Large" (coding agent setup), "Part 1: What is this project?" through "Part 4: How was it built?" (good README). Each section says what to do, why, and shows the real command, prompt, or config for it, in flowing prose - not a fixed "what / why / example / trap" sub-pattern.
5. **Failed or weaker approaches folded into the walk-through, not a separate contrast section** — when an approach is worse than the recommended one, say so inside the step where it belongs. "Choosing a Portfolio Project" contrasts a naive "Spray-and-Pray Strategy" with the recommended domain-based approach as two H3s inside one step, rather than as a dedicated before/after section.
6. **The practical artifact, embedded where it's used** — a prompt template, a named skill or tool, or a config snippet, placed inside the step it belongs to rather than collected at the end. The PyPI post's artifacts are the actual named Claude Code skills (`init-library`, `setup-pypi-ci`, `release`), each introduced at the point in the pipeline where it gets used.
7. **A short practical wrap-up before the close** — "Other Tips," "Where to go from here," or a plain "Common mistakes" list, as in "How to Write a Good README." This carries the caveats and honest limitations. It is not a "good signs / warning signs" pair.
8. **Close** — the same short reflective landing as the shared anatomy, sometimes just one short paragraph before the signoff and apparatus.

### Notes

- No dedicated "why it matters" stat-stacking section, no before/after or wrong-way/right-way contrast as its own beat, no "good signs / warning signs" list, and no strategic zoom-out to teams or orgs. None of the real posts checked do any of these.
- Headings do exist in these posts and carry real structure. The `reference/substack/*.md` archive files lost all markdown heading syntax during scraping - confirmed by fetching the live pages directly, which show rich, numbered H2/H3 structure the local files don't preserve. Don't take a flat, heading-free archive file as evidence that a post itself has no headings; check the live URL if in doubt.
- This is the same real scaffold as Template 3 (a numbered sequence, one H2 per item, the number in the heading). The difference is content, not structure: use this template when the numbered items are actions the reader takes, and Template 3 when they are claims, benefits, or dimensions the reader is meant to weigh rather than execute.

---

## Template 3 — Argument Essay (Numbered Claims)

*Best for an essay that argues toward a set of claims, benefits, or dimensions, stated as a bare numbered list and unpacked afterward in prose. Grounded in "Benefits of Learning in Public and Why It Works," "What AI Forward-Deployed Engineers Do," and "How CRISP-DM Still Applies to AI Engineering." The elaborate headed "framework" with per-item sub-labels does not exist anywhere in the corpus - dropped in favor of what these posts actually do.*

**Default length: 1,800-2,400 words.**

### Structure

1. **Opener** — the same concrete-situation or plain-claim opener as the shared anatomy, not an invented vivid scene. "Benefits of Learning in Public" opens on the DataTalks.Club context; "What AI Forward-Deployed Engineers Do" opens on a dated stat.
2. **State the list once, bare, no sub-labels** — a numbered list of the claims or dimensions the piece will cover, under its own H2 (as in "Benefits of Learning in Public," which states eight one-line benefits under a "Benefits of Learning in Public" heading immediately before unpacking them).
3. **Unpack each item, one H2 per item, and number the heading itself** — real headings carry the number: "1. Visibility and Career Opportunities" through "8. Beyond Jobs: Unexpected Opportunities" (Learning in Public); "1. Business Understanding" through "6. Deployment" (CRISP-DM, mapping an existing outside framework onto AI work, phase by phase). One to three short paragraphs per item. Evidence is a named practitioner's quote, a linked tool, or a stat woven into the paragraph, never a repeated "why it matters / practical applications / trap to avoid" formula.
4. **A caveat, stated plainly where it belongs, not saved for the end** — the data-backed variant states its own bias inline, where the claim needs it: "But our data is probably biased because in our scrapes we focus on AI Engineering roles" (What AI Forward-Deployed Engineers Do).
5. **Close** — short and plain. The personal essay ends on a compact maxim plus the standard forward teaser and subscribe nudge. The data-backed variant sometimes closes under a plain "Conclusion" heading instead, per the style doc's note that only the data posts use that heading.

### Notes

- There is no numbered, headed "framework" with per-item sub-labels (why it matters / practical applications / trap to avoid) anywhere in the corpus. The closest real pattern is a bare numbered list of claims or dimensions, stated once, then unpacked afterward in ordinary prose, one H2 per item, with the number in the heading itself.
- Don't force a metaphor-driven "build the argument" section before the list. The real posts move from the opener straight to the list.
- Headings do exist and carry the item number (see the heading note under Template 2 - the local archive files lost heading markup during scraping, but the live posts show it clearly).
- This is the same real scaffold as Template 2 (a numbered sequence, one H2 per item). The difference is content, not structure: use this template when the items are claims, benefits, or dimensions to weigh, and Template 2 when they are actions to take.
- Even this essay form opens on the concrete personal or organizational case before any abstract framing, per the style doc: "Abstract framing, where it exists at all, comes after the concrete personal case."

---

## Template 4 — Concepts / Architecture Explainer (deprecated)

*This template does not hold up against the real archive. It is kept here, marked deprecated, only so the numbering in this file matches `SKILL.md`. Do not offer it at kickoff - use Template 1 or Template 3 instead, per the notes below.*

### What we checked

Three archived posts about Alexey's own libraries plausibly fit "decode how a system works": [Minsearch: The Small Search Library Behind My RAG Workshops and Courses](https://aishippingblog.com/p/minsearch-the-small-search-library), [How I Built SQLiteSearch: A Lightweight Python Library for Local Text and Vector Search](https://aishippingblog.com/p/how-i-built-sqlitesearch-a-lightweight), and [How I Built a Tool to Search and Visualize My Entire ChatGPT History](https://aishippingblog.com/p/chatgpt-data-viewer).

All three are chronological build logs, confirmed against the live pages, not concept-by-concept explainers. Minsearch's real H2s run "Why Elasticsearch Was Too Much," "The First Version," "From a File to a Package," "Where I Use It," "Implementing Inverted Index and Vector Search," "Making minsearch Faster with Claude Code," "When Minsearch Is the Right Tool" - a build history, not one H2 per mechanism. SQLiteSearch's real H2s run "Background," "My Requirements," "Research Phase," "Implementation," "Final Solution," "Release Workflow for the Publication to PyPI."

Both close by pivoting into "What I've Been Working on Recently" and other newsletter apparatus, not a recap list of concepts covered. No other post in the 47-post archive reads as a pure concept explainer either. `articles/_meta/substack-writing-style.md`'s "Differences between post types" section documents build logs, tutorials, digest editions, announcements, the data-analysis posts, third-party explainers, and community showcase posts, and none of those is "decode a concept with no build narrative and no third-party subject."

### What to use instead

- Explaining your own system, library, or pipeline: use **Template 1 (Build Log)**. That's what minsearch, SQLiteSearch, and the ChatGPT data viewer actually are.
- Explaining a general concept or an outside framework structurally, one phase or dimension per H2, without a build narrative: use **Template 3**, whose CRISP-DM example is exactly this shape.
- Explaining someone else's tool: use **Template 5**.

---

## Template 5 — Tool / Library Teardown (third-party explainer)

*Best for a deep read of one tool, library, or framework through an engineer's lens - someone else's project, not Alexey's own build. This is the one template where the style doc says personal narrative mostly drops out, so don't force the build-log arc's "I hit this problem" opener here. Use this for pieces like the deepseek-harness draft.*

**Default length: 1,200-2,000 words.**

### Structure

Six beats, confirmed against real drafting: what it is, how to configure and run it, first impressions, how it works under the hood, comparison with other tools, recommendations. Use these as the actual H2 headings (reworded for the specific tool, not left generic).

1. **What it is** — the concrete news hook: what happened, when, with numbers (a release, a star count, a launch thread, a controversy). Ground it in real, dated events and real links before any analysis starts. Fold in a flat, first-person statement of the work behind the piece ("I did the only thing that settles such arguments: I cloned it and read the code"), the scale (lines of code, packages, license), and the one-line bet the tool makes.
2. **How to configure and run it** — the practical setup path: the actual command, what it launches, the actual config/composition mechanism if one exists. This is the concrete, reproducible part - real commands in fenced code blocks, each with a sentence of explanation before and after.
3. **First impressions** — a short, personal reaction after actually running or reading it, before the deep mechanism dive. This is where a stray community comparison (someone else's take on X) can be cited and agreed or disagreed with in one sentence, plus the one-line verdict-so-far.
4. **How it works under the hood** — the guided walkthrough, as H3s nested under this H2, each with a plain heading naming the mechanism, not a generic label ("A kernel with no core" and "The log is the truth," not "Architecture"). Walk 3-5 mechanisms relevant to this specific tool - don't force a fixed dimension checklist (architecture/DX/performance/ecosystem/tradeoffs) if the tool doesn't warrant each one. Cite the actual source (docs, code, commits, postmortems) inline for every claim, and fold in real community reaction (fans and skeptics both) at the point in the mechanism it's actually evidence for, rather than saving it all for a separate reception section at the end.
5. **Comparison with other harnesses/tools** — where this sits next to comparable tools, ideally as a comparison table plus 2-3 axes that actually decide the choice.
6. **Recommendations** — an honest, evaluative close in the same dry, hedged register as the rest of the piece: who should run this and why, who should skip it and why, the honest caveats (what's unproven, what has no independent benchmark), and what's worth stealing regardless of the tool's own fate, folded into the same paragraphs rather than a separate bulleted "what to steal" section. Then the signoff.

### Notes

- Review from real use or deep reading, never on vibes. Specific observations beat adjectives ("cold start is 8 seconds on an A10G" beats "slow startup").
- Link the tool on first mention, and any other libraries or people referenced.
- Do not add a standalone "What people actually say" or "What to steal" section - both read as generic bolt-on listicles when separated from the piece. Weave reactions into the mechanism they support, and weave the stealable patterns into the closing recommendation paragraphs.

---

## Code snippets

Use fenced code blocks with the correct language tag. Keep snippets:

- **Short** — show the essential logic, not a full codebase.
- **Runnable when possible** — or at least structurally accurate.
- **Explained** — always say what the code does before or after.
- **Annotated** — use inline comments for non-obvious lines.

```python
# Cross-encoder reranking: slower but more accurate than bi-encoder retrieval
from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
scores = reranker.predict([(query, doc) for doc in retrieved_docs])
top_k = sorted(zip(retrieved_docs, scores), key=lambda x: x[1], reverse=True)[:5]
```

---

## Images and diagrams

Leave a clearly-marked placeholder at the spot the visual belongs. Write captions plainly, naming the components shown:

```
[IMAGE: Architecture diagram of a RAG pipeline with reranking]
Caption: 1. Document ingestion and chunking. 2. Embedding and vector storage. 3. Bi-encoder retrieval. 4. Cross-encoder reranking. 5. LLM generation.
```

Don't embed real images. One lead diagram near the top plus 2-4 inline visuals is typical for a deep dive.

---

## Final draft file structure

After all sections are approved, save as `{slug}-draft.md` with this layout:

```markdown
# {Working title}

> Subtitle: {chosen subtitle}

[Lead image placeholder]

{Hook through close, in full publish-ready markdown, ending with the Sincerely / Alexey signoff}

---

## Platform Deltas

**Substack (Alexey On Data):**
- URL: https://aishippingblog.com
- Subtitle: {chosen subtitle}
- Paywall: place `[PAYWALL BREAK - free preview ends here]` after {section}.
- Ends on the Sincerely / Alexey signoff.

**Medium:**
- 5 topic tags: {e.g. Artificial Intelligence, Machine Learning, LLM, NLP, MLOps}
- Member-only: yes/no.
- Ends on the community CTA: "Thanks for reading! If you found this useful, subscribe for more AI engineering deep dives..."

---

## SEO Keywords

- 8-12 keywords/phrases mixing head terms (e.g. "LLM evaluation," "RAG pipeline") and long-tail phrases tied to the article's specific topic.

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
