---
title: "Mini-Course Proposal: LLM Wikis as Agent Memory"
created: 2026-07-31
updated: 2026-07-31
tags: [llm-wiki, agent-memory, mini-course, agents, knowledge-management]
status: draft
---

# Mini-Course Proposal: LLM Wikis as Agent Memory

## Short proposal for Paul

Let us turn the existing AI Research OS workshop into a broader, vendor-neutral mini-course called **LLM Wikis as Agent Memory**. The course will teach the pattern rather than a particular Obsidian setup: how an agent compiles heterogeneous raw sources into a persistent, inspectable set of linked markdown pages; how it retrieves context through progressive disclosure; and how ingest, query and lint operations let that memory improve over time. Paul's open-source research skill remains the main implementation, but we present it as one concrete implementation of a more general architecture that works with Claude Code, Codex or another agent harness.

Roughly 25% of the session will establish the mental model and boundaries. An LLM wiki is primarily persistent semantic or project memory, not the agent's working memory and not automatically a replacement for conversational, transactional or large-scale retrieval systems. The practical part will build a wiki from mixed sources, inspect the generated index, concepts, comparisons and citations, then ask a new question that creates a durable derivative page. A second demo will use the wiki as context for an agent doing real work, so the audience sees the difference between collecting knowledge and using it.

The final section will cover the cases where the pattern is genuinely useful and where it is not. The course should leave participants with a reusable skill, a small wiki built from their own sources, and a decision framework for choosing among plain files, search/RAG, databases and knowledge graphs. All source material, code and exercises will remain free, and the two written parts can be published across our Substacks.

## Learning outcome

By the end, participants should be able to:

- Explain how an LLM wiki differs from a document dump, long context, RAG and a knowledge graph.
- Identify the kind of agent memory the wiki provides.
- Create a scoped wiki from several source types with provenance back to immutable raw material.
- Use its index and links for progressive disclosure instead of loading everything into context.
- Query it, file useful outputs back into it and lint it for stale or contradictory claims.
- Decide when this architecture is too small, too slow or too risky for the problem.

## Proposed 90-minute format

### 1. Theory and decision model — 20 minutes

- The problem: agents repeatedly rediscover the same project knowledge.
- The core artifact: raw sources → compiled wiki → agent work.
- The three layers: immutable raw sources, LLM-maintained wiki and maintenance schema.
- The three operations: ingest, query and lint.
- Indexes, links, provenance, progressive disclosure and version history.
- Agent-memory taxonomy:
  - Working memory lives in the current context window.
  - Episodic memory records events and prior runs.
  - Semantic memory records durable facts, concepts and relationships.
  - Procedural memory records instructions and workflows.
  - An LLM wiki mainly provides scoped semantic memory, with optional episodic logs and procedural rules.
- Why this compounds in a way that one-shot RAG does not—and why that does not make RAG obsolete.

### 2. Build the wiki with a reusable skill — 20 minutes

Use a deliberately generic input set: one article, one video transcript, one repository and one short personal note.

Show:

- Source capture and normalization.
- The generated source catalog/index.
- Entity, concept and comparison pages.
- Citations and links back to raw material.
- The maintenance log and schema.
- How the same skill can be adapted to different sources or agent harnesses.

### 3. Demo one: research that compounds — 15 minutes

Build a small wiki around one bounded topic. Ask a question that was not part of the ingestion prompt, inspect how the agent navigates from index to wiki pages to raw sources, and save the useful answer as a new page. Then add one conflicting source and show how the wiki records or resolves the contradiction.

Output to show:

- `raw/` source snapshot.
- `index.yaml` or `index.md`.
- Source summaries.
- Concept and comparison pages.
- A query-created note.
- Provenance and a lint report.

### 4. Demo two: wiki as agent memory — 15 minutes

Give an execution agent a real task that depends on several sources—for example, plan an article, compare several codebases or propose a feature for an existing project. Run it first with only the immediate prompt, then with the scoped wiki available. Compare factual coverage, source use, context size and the amount of repeated research.

The important output is not an attractive Obsidian graph. It is evidence that the agent finds and uses the right project knowledge, and that the result becomes easier to inspect and reproduce.

### 5. Where it works and where it does not — 10 minutes

Good fits:

- Project research that will be queried repeatedly.
- Literature reviews and competitive analysis.
- Codebase architecture and engineering decision memory.
- Course, article and video production from overlapping sources.
- Team knowledge assembled from documents, meetings and support conversations.
- Bounded due diligence where provenance and inspectability matter.

Poor fits:

- A one-off question that search or a single prompt answers.
- Exact transactional state such as balances, inventory or permissions.
- Rapidly changing facts that require authoritative real-time lookup.
- Huge corpora where a hand-maintained file index no longer retrieves reliably.
- Strict row-level access control, regulated personal data or sources that must not be mixed.
- Fully autonomous editing of a human-authored source of truth.
- Personalization based on individual conversation history unless identity, consent, deletion and isolation are designed explicitly.

Escalation rule:

- Start with plain linked files for a bounded project.
- Add full-text or semantic search when the index stops being sufficient.
- Add structured storage for exact facts and filters.
- Add a graph database only when relationship traversal is itself a core query.

### 6. Exercise, recap and Q&A — 10 minutes

Participants choose three sources, define the scope and schema, build a wiki, ask one synthesis question, file the answer and run a lint pass. The take-home extension is to connect one additional source type or use the wiki in an agent task.

## Division between Alexey and Paul

Paul:

- Introduce the original Research OS journey and the reusable wiki/research skill.
- Lead the ingestion and compounding-research demo.
- Explain the practical lessons from using the system across projects.

Alexey:

- Establish the agent-memory taxonomy and the boundary with RAG and databases.
- Lead the “wiki as working project context” comparison demo.
- Present the fit/non-fit decision framework and the evaluation checklist.

Together:

- Show failure modes rather than only the happy path.
- Review participant adaptations and publish the resulting examples.

## Quality checklist

A useful LLM wiki should be evaluated as a memory system, not by the number of generated pages:

- **Retrieval:** does the agent find the relevant page for representative questions?
- **Grounding:** can important claims be traced to a source?
- **Coverage:** are the questions the project actually needs answerable?
- **Freshness:** are changed or conflicting claims detected?
- **Separation:** are raw sources protected from generated derivatives?
- **Efficiency:** does progressive disclosure save context compared with rereading raw sources?
- **Utility:** does the wiki improve the downstream task, not merely produce more notes?

## Two-part publishing plan

### Part 1: What LLM Wikis Are and When They Beat One-Shot RAG

Publish on one Substack. Cover the theory, architecture, agent-memory taxonomy, progressive disclosure and decision framework. End with the small mixed-source demo.

### Part 2: Building and Using an LLM Wiki as Agent Memory

Publish on the other Substack. Walk through the reusable skill, the project-memory demo, outputs, linting, failure modes and take-home exercise. Both posts link to the same free repository and recorded mini-course.

The order can be swapped. The important part is that Part 1 is generic and conceptual, while Part 2 is implementation-led.

## Source material

- [Paul's LLM Wiki article](https://www.decodingai.com/p/llm-wiki-agent-memory)
- [AI Research OS workshop video](https://www.youtube.com/watch?v=ZRM_TfEZcIo)
- [AI Research OS workshop repository](https://github.com/iusztinpaul/ai-research-os-workshop)
- [Alexey and Paul discussing second brains and LLM wikis](https://www.youtube.com/live/TDP3tIKxqlc)
- [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Google's Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
- [Existing research note: LLM Wikis](../../research/llm-wiki.md)
- [Existing research note: Memory Layers for AI Agents](../../research/memory-layer.md)
