# Prompt Engineering Is Dead. Long Live Context Engineering.

> Subtitle: With 1M-token windows, the skill that matters isn't asking the right question. It's curating what the model knows in the moment.

[IMAGE: Diagram showing the four layers of context engineering: Selection, Ordering, Compression, Eviction]

Your teammate pastes a 200-page PDF into Claude and asks it to "summarize the key risks." Claude produces a clean, confident summary. Two of the three risks are real. The third is plausible, specific, and completely fabricated. It cited a section that exists,引用了 a paragraph that doesn't.

You've seen this before. The model had plenty of context. The problem is that it had *too much* context, arranged badly, with no mechanism to separate signal from noise.

For years, we called the solution "prompt engineering." Write better instructions, add a few-shot example, chain-of-thought, system prompt with persona. That worked when models had 4K tokens and you had to choose every word carefully. It doesn't work the same way when the window holds a million.

[Anthropic published "Effective Context Engineering for AI Agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) last year, and it named something a lot of practitioners were already doing without a word for it. The post landed on [Hacker News with huge engagement](https://news.ycombinator.com/item?id=45418251), and the phrase "context engineering" started showing up everywhere. [Phil Schmid's follow-up](https://news.ycombinator.com/item?id=44427757) put it bluntly: the new skill in AI is not prompting, it's context engineering.

Some people pushed back. "It's just rebranded prompt engineering," the HN comments said. "The work matters more than the name."

They're half right. The work overlaps. But the framing changes what you optimize for, and that changes outcomes.

### The shift: from wording to curation

[Avi Chawla's framework](https://x.com/_avichawla/status/2072980277870383366) breaks it into layers:

**Prompt engineering** is about wording a single call. What you say, how you say it, which examples you include.

**Context engineering** is about everything in the window beyond the prompt itself: retrieved documents, conversation history, tool outputs, memory, and the structure that connects them. Which of those things belong? In what order? What gets compressed, summarized, or dropped?

**Harness engineering** is the outer layer: which tools the agent has, how loops and verifiers work, when to stop.

This article focuses on the middle layer. That's where most production LLM applications live or die.

Here's why. When you give a model 4K tokens, every token matters, and careful prompt wording dominates. When you give it 1M tokens, the wording matters less. What matters is *what's in those tokens*. The model is good at finding the answer if the answer is in the window. [The problem is that "in the window" and "findable by the model" are not the same thing](https://news.ycombinator.com/item?id=44564248). Long contexts have a "dumb zone" in the middle where models lose accuracy, a pattern [Gergely Orosz and Dex Horthy discussed in detail](https://x.com/GergelyOrosz/status/2077434907274428914).

**The bottleneck in production LLM systems has moved from the prompt to the context window. The skill that matters now is deciding what information reaches the model, in what order, and what gets left out.**

### Four layers of context engineering

### 1. Selection: what goes in

This is the most consequential decision. A common mistake is to dump everything: full codebase, entire chat history, all retrieved chunks. More context sounds safe. In practice, it degrades performance.

[Anthropic's own engineering team](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) describes a hybrid approach: static files loaded upfront (like CLAUDE.md for project rules) combined with dynamic, just-in-time retrieval using tools (glob, grep, search) instead of loading entire files into the window.

[Cursor takes a similar approach](https://medium.com/@ai-labs/cursors-new-context-discovery-principles-can-transform-how-you-use-any-ai-coding-tool-d379191d4f25): minimal relevant context over maximal inclusion. Their dynamic context discovery surfaces only what's needed for the current task, not everything that might be relevant.

The selection principle: **load what you need, when you need it, not before.**

A practical pattern from [practitioner threads](https://x.com/Av1dlive/status/2073394238554009933):

- **Static context** (always loaded): project rules, persona, guardrails, coding standards. Small, stable, high-signal.
- **Dynamic context** (loaded on demand): retrieved chunks, tool results, live data, file contents. Large, variable, needs filtering.

### 2. Ordering: where things go

Models don't read context uniformly. The "lost in the middle" effect is real: information placed in the middle of a long context window gets retrieved with lower accuracy than information at the beginning or end.

[Avi Chawla's thread](https://x.com/_avichawla/status/2072980277870383366) recommends reranking retrieved chunks for relevance and placing key facts outside the middle zone. If you have a critical instruction or a key document, put it first or last.

This sounds trivial. It isn't. I've seen RAG pipelines where the most important retrieved chunk was buried at position 15 out of 20, and moving it to position 1 improved answer accuracy measurably. The retrieval pipeline found the right document. The context ordering hid it.

### 3. Compression: keeping the window manageable

Context grows. Every tool call adds tokens. Every retrieval adds chunks. Every conversation turn adds history. Without compression, you hit the window ceiling and either truncate blindly (losing information) or error out.

[Anthropic describes several compression techniques](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents):

- **History summarization:** periodically summarize older conversation turns into a compact representation.
- **Tool-result clearing:** remove the raw output of completed tool calls, keeping only the extracted insight.
- **Compaction:** collapse verbose retrieved text into key points before injecting into context.

[Martin Fowler's deep dive on coding agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) adds another pattern: push large blobs to external files and reference them by path, rather than inlining the full content. Instead of loading a 50K-token log file into the context, write it to disk and tell the agent "the logs are at `/tmp/logs/2026-07-24.log`, use `grep` to search them."

The compression principle: **be intentional about what gets compacted.** Don't let the model decide by running out of window. Design your compaction strategy explicitly.

### 4. Eviction: what to remove

The hardest decision. When the context is full and compression isn't enough, what do you drop?

Most systems do this implicitly and badly. They truncate from the top (oldest messages) or from the middle (random chunks). A better approach:

- Evict tool outputs first (they're regenerable).
- Evict retrieved chunks that haven't been referenced in the last N turns.
- Never evict system instructions, guardrails, or the current task description.
- Keep a compact summary of evicted content so the model knows what it used to know.

This maps to how [Claude Code manages its own context](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): static rules stay, dynamic content gets summarized and cleared, and the agent uses tools to re-fetch what it needs rather than holding everything in window.

### What this looks like in production

Here's a pattern I've seen work across RAG systems, agent pipelines, and coding assistants:

```
Context Budget (per turn):
├── Static (always loaded)
│   ├── System prompt + persona        ~500 tokens
│   ├── Project rules / guardrails     ~1,000 tokens
│   └── Current task description       ~300 tokens
├── Dynamic (loaded per turn)
│   ├── Retrieved chunks (reranked)    ~4,000 tokens
│   ├── Tool results (filtered)        ~2,000 tokens
│   └── Recent conversation history    ~2,000 tokens
├── Reserved for model output
│   └── Generation + reasoning         ~2,000 tokens
└── Total                              ~12,000 tokens
```

This is deliberately smaller than the window. You don't want to operate at the ceiling. Models degrade near the top of their context window, and you need headroom for the response.

The point is not the exact numbers. The point is that someone designed this budget. Someone decided what goes in, how much space it gets, and what happens when it overflows. That design work is context engineering.

### Is this just rebranded prompt engineering?

Let's address the skeptics directly. A [highly debated HN thread](https://news.ycombinator.com/item?id=44427757) pushed back on the term, and they have a point. Prompt engineering and context engineering share DNA. Both are about giving the model what it needs to succeed.

But the optimization target is different. Prompt engineering optimizes *wording*. Context engineering optimizes *information architecture*. When your window was 4K tokens, wording was the bottleneck. When it's 1M tokens, information architecture is the bottleneck.

[Some X posts frame context engineering as an evolution](https://x.com/tonsofpetefun/status/2080670439307981074), others call it commodity shift. The practical difference: you can write a perfect prompt and still get garbage if your context is bloated, unordered, and uncompressed. You can write a mediocre prompt and get great results if your context is clean, well-ordered, and focused.

### What to do on Monday

1. **Audit your current context.** Take a real production request. Print everything in the context window. How much of it is actually useful for this specific call? Most teams have never done this.

2. **Design a context budget.** Decide how much space each category gets (static, retrieved, history, tool output, generation). When you overflow, which category shrinks first?

3. **Rerank before injecting.** Don't just retrieve top-K chunks. Retrieve 3K, rerank with a cross-encoder, inject the top 10.

4. **Compress aggressively.** Summarize old turns. Clear stale tool outputs. Push large blobs to external files. Don't wait for the window to fill.

5. **Move key information out of the middle.** First and last positions get the most attention. Put your critical instructions there.

6. **Build observability for context.** Log what's in the window for every call. You can't optimize what you can't see. Tools like [LangSmith](https://www.langchain.com/langsmith), [Braintrust](https://www.braintrust.dev/), and [Arize Phoenix](https://phoenix.arize.com/) can help, but even raw logging works.

### Here's what I believe

The models are good enough now. GPT-5.5, Claude Opus, Gemini 3.6, Kimi K3, the open-weight frontier. They can reason, retrieve, use tools, and write code. The bottleneck is not the model. It's the pipeline around it, and specifically the part where we decide what the model knows in the moment it generates a response.

That decision used to be an afterthought. You wrote a prompt, threw in some context, and hoped. Now it's the whole game. Context engineering is the skill that separates teams shipping reliable LLM applications from teams debugging hallucinations at 2am.

If you're building AI systems and not thinking about context architecture explicitly yet, this is your sign to start. I teach this and other production AI engineering patterns in [AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) and write about them at [Alexey On Data](https://alexeyondata.substack.com). Come join.

Sincerely,
Alexey

---

## Platform Deltas

**Substack (Alexey On Data):**
- URL: https://alexeyondata.substack.com
- Subtitle: With 1M-token windows, the skill that matters isn't asking the right question. It's curating what the model knows in the moment.
- Paywall: place `[PAYWALL BREAK — free preview ends here]` after "### What this looks like in production".
- Ends on the Sincerely / Alexey signoff.

**Medium:**
- 5 topic tags: Artificial Intelligence, Machine Learning, LLM, NLP, MLOps
- Member-only: yes
- Ends on the community CTA: "Thanks for reading! If you found this useful, subscribe to [Alexey On Data](https://alexeyondata.substack.com) for more AI engineering deep dives, practical guides, and the occasional production war story. Or just share it with someone who's debugging their context window at 2am."

---

## SEO Keywords

- context engineering
- prompt engineering vs context engineering
- LLM context window management
- context engineering for AI agents
- RAG context optimization
- context compression LLM
- lost in the middle LLM
- context ordering language models
- production LLM applications
- AI agent context management

---

## Title & Subtitle Shortlist

### Titles
1. Prompt Engineering Is Dead. Long Live Context Engineering.
2. Context Engineering: The skill that separates good LLM apps from great ones
3. Why your LLM has a million tokens and still hallucinates
4. The four layers of context engineering (and why your prompt doesn't matter anymore)
5. Stop prompt engineering. Start context engineering.

### Subtitles
1. With 1M-token windows, the skill that matters isn't asking the right question. It's curating what the model knows in the moment.
2. A practical framework for managing what your LLM sees, orders, compresses, and forgets.
3. From prompt wording to information architecture: how production AI systems actually manage context.
