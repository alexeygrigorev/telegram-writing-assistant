# Structure Guide — Article Templates

Open this file once a template is chosen. It covers title and subtitle craft, the shared article anatomy, the four templates with word norms and annotated scaffolds, code and image conventions, and the final-draft file structure.

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

Whatever the template, every article has this spine:

1. **Title + subtitle** (offered as options in Step 2).
2. **Hook** (1-2 short paragraphs). A concrete scene, a counterintuitive linked stat, or a specific failure. No rhetorical questions, no "in the age of AI."
3. **Framing** (1-2 paragraphs). Pivot from the hook to what the piece argues or teaches. State the thesis in plain language.
4. **Body** — H3 sections with scannable headings. This is where the template shape lives.
5. **Practical artifact** when it fits — a checklist, framework, code snippet, or step list the reader can lift.
6. **Close** (1-2 short paragraphs). A personal landing, often "Here's what I believe:", that ties back to the spine and leaves a takeaway. Then the signoff.
7. **Signoff:** `Sincerely,` / `Alexey` (and the Medium community CTA in the platform deltas).

Headings are H3 (`###`) and named with personality, not generic labels. Real examples: "The retrieval problem nobody owns," "Why your eval suite is lying to you," "Chunking: the unglamorous bottleneck," "The latency tax of thinking step-by-step."

---

## Template 1 — Practical Workflow / Method

*Best for a repeatable method, system, or pipeline.*

**Default length: 1,800-2,400 words.**

### Structure

1. **Hook** — a counterintuitive claim with a linked stat that reframes a common habit.
2. **Why it matters** — 2-4 short paragraphs establishing the problem with evidence. Stack a few linked stats here; this template is the most data-forward.
3. **The method, broken into named parts** — numbered layers, steps, or stages, each an H3. Each part: what it is, what it's for, a concrete example with code or config, ideally a linked source.
4. **A before/after or wrong-way/right-way contrast** — show the naive approach vs. the robust approach side by side.
5. **The practical artifact** — a checklist or copy-pasteable code template. This template almost always carries one.
6. **"How to know it's working"** — a "good signs / warning signs" pair of lists.
7. **Strategic implications** — zoom out to what this means for individual engineers, teams, and orgs.
8. **Close** — the reassuring landing (you already have these skills, here's the new way to apply them) + signoff.

### The artifact for this template

A checklist, config template, or code snippet the reader can copy:

```python
# Minimal evaluation harness skeleton
from typing import List, Dict

def evaluate_pipeline(
    queries: List[str],
    expected: List[str],
    retrieve_fn,
    generate_fn,
) -> Dict[str, float]:
    results = []
    for q, exp in zip(queries, expected):
        context = retrieve_fn(q)
        answer = generate_fn(q, context)
        results.append(score(answer, exp))
    return aggregate(results)
```

Or a grouped checklist ("Data preparation: ...", "Embedding strategy: ...", "Retrieval tuning: ...") of yes/no questions.

---

## Template 2 — Strategic Essay + Framework

*Best for an argument that resolves into a named, reusable framework.*

**Default length: 1,800-2,400 words.**

### Structure

1. **Scene hook** — a vivid, specific moment that sets up the tension.
2. **Reframe the problem** — an H3 that names the real question and answers it plainly. Cite a practitioner, paper, or benchmark if one anchors it.
3. **Build the argument** — 2-3 H3 sections moving through evidence and one **extended metaphor**. Drop the **bolded thesis line** here.
4. **The framework** — a numbered set of named dimensions. For each item, follow this exact sub-pattern:

```markdown
### N. {Dimension}: {short evocative tagline}

[1-2 sentences defining it.]

**Why it matters:** [2-3 sentences on the technical or business reason. Link research/benchmarks if you have it.]

**Practical applications:**
- **[Lead-in phrase].** [Concrete example naming a real tool/library, linked.]
- **[Lead-in phrase].** [Another concrete example.]

**The trap to avoid:** [The failure mode, 1-2 sentences.]
```

5. **Close** — a personal "Here's what I believe:" landing that states the stakes, plus signoff.

### Notes

- The framework is the artifact. Keep the items parallel in shape so the reader can scan and reuse them.
- Each dimension needs at least one named, linked tool or example.

---

## Template 3 — Concepts / Architecture Explainer

*Best for decoding how a system or pattern works. Often runs shorter (800-1,500 words).*

### Structure

1. **Relatable hook** — a specific, common experience, stated (not asked). "Most of us have watched an LLM confidently cite a document that doesn't exist."
2. **Set up the explainer** — one short paragraph promising to break it down.
3. **One concept per H3, each with a clear subhead** — the heading names the concept; the body explains the mechanism with a concrete example.

```markdown
### Embedding sharding: splitting to scale

When your corpus hits millions of documents, a single vector index becomes a bottleneck. *Embedding sharding* splits the index across multiple nodes. Each shard handles a subset of vectors, and a coordinator routes queries to the relevant shards. [Faiss](link) and [Milvus](link) support this natively.
```

4. **"How others do it" roundup** — a list applying the same concept across tools:

```markdown
🔬 **Faiss:** in-memory, GPU-accelerated, great for research and medium-scale prod.
📦 **Pinecone:** managed, auto-scaling, good for teams that don't want to own infra.
🐘 **pgvector:** if you're already on Postgres, it's the path of least resistance.
```

5. **Recap list** — a short list of the concepts covered, ideally each linked.
6. **Community CTA** — close on the "subscribe for more..." CTA.

### Notes

- Personal parenthetical asides shine in this template.
- Name the formal technique every time and link it. The credibility is in the citations.

---

## Template 4 — Tool / Library Teardown

*Best for a deep read of one tool, library, or framework through an engineer's lens.*

**Default length: 1,200-2,000 words.**

### Structure

1. **Framing** — why this tool, why now, what engineers can learn from it.
2. **Guided walkthrough by dimension.** Walk 4-6 named dimensions:
   - **Architecture:** how it works under the hood, key design decisions.
   - **DX (developer experience):** setup, docs, ergonomics, time-to-first-result.
   - **Performance:** latency, throughput, resource usage, with real numbers where possible.
   - **Ecosystem:** integrations, community, maturity, who's using it in production.
   - **Tradeoffs:** what it optimizes for and what it sacrifices.
   - **Observability:** logging, tracing, metrics, debuggability.
3. **"What engineers can steal"** — the practical artifact: 3-5 transferable patterns or techniques.
4. **Verdict** — an honest landing on where it shines and where it falls short, plus signoff.

### Notes

- Review from real use or deep reading, never on vibes. Specific observations beat adjectives ("cold start is 8 seconds on an A10G" beats "slow startup").
- Link the tool on first mention, and any other libraries or people referenced.

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
- Paywall: place `[PAYWALL BREAK — free preview ends here]` after {section}.
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
