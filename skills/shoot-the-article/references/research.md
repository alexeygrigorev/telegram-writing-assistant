# Research Guide — Finding the Article's Angle

The goal of research is to find **3-5 article angles** worth pitching. A strong angle gives a single article one arguable thesis, a timely hook, a practical payoff, and real sources to cite.

## Source playbook

### Primary social signal: x.ai Grok (use this first)

The fastest way to find what AI engineers are debating right now is **Grok's live search** across X/Twitter, Reddit, and the web. It has real-time access to both platforms (which block conventional scraping) and returns citations.

**Tool:** `~/git/ai-engineering-field-guide/interview/_internal/xai_search.py`
**API key:** `XAI_API_KEY` in `~/git/ai-engineering-field-guide/.env`
**Model:** `grok-4-1-fast-reasoning`
**Cost:** ~$0.06 per query (8 server-side tool calls)

**Usage:**
```bash
cd ~/git/ai-engineering-field-guide && python3 interview/_internal/xai_search.py \
  '<research prompt>' \
  --tools web_search,x_search \
  --label 'descriptive-name'
```

**Writing good Grok prompts:**
1. State what you're researching (context)
2. Define exactly what you want (debates, opinions, data, links)
3. Specify where to look (Reddit r/LocalLLaMA, X/Twitter, HN, blogs)
4. Scope it (time period, exclude what you don't want)
5. Request structured output (for each result: source link, who said it, what they argued)

**Best for:** trending debates, contrarian takes, production war stories, tool comparisons, what practitioners are arguing about on X and Reddit. This is the **primary trend discovery tool** — start here before anything else.

**Example query that works well:**
```
I'm researching trending topics in AI engineering for article ideas.
Find me the hottest discussions from the past 2 weeks on Reddit
(r/LocalLLaMA, r/MachineLearning), X/Twitter, and Hacker News about:
LLM agents in production, model routing, evaluation challenges, open-weight
vs closed models, context engineering, AI cost optimization. For each trend,
give me: what the debate is about, key voices/links, and why it matters
to practitioners building LLM applications.
```

### Daily aggregators (quick pulse check)

These aggregate Twitter/X, Reddit, blogs, and papers into one daily read:

- [TLDR AI](https://tldr.tech/ai) — daily AI digest, 1.1M subscribers. Model launches, research, tools, funding. Scrapeable at `tldr.tech/ai/YYYY-MM-DD`
- [Latent Space](https://www.latent.space/) — Swyx & Alessio, podcast + newsletter, captures Twitter signal
- [The Rundown AI](https://www.therundown.ai/) — daily, more practical/applied

### Hacker News (fully accessible via Algolia API)

- Front page: `https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30`
- By topic: `https://hn.algolia.com/api/v1/search?query=LLM&tags=story&numericFilters=points>30,created_at_i>{week_ago}`
- Sort by points to find what's trending
- Comments are often more valuable than the post itself
- Python example:
```python
import json, urllib.request, time
week_ago = int(time.time()) - 7*86400
url = f'https://hn.algolia.com/api/v1/search?query=LLM&tags=story&hitsPerPage=20&numericFilters=points>30,created_at_i>{week_ago}'
data = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=10).read())
for h in sorted(data['hits'], key=lambda x: x['points'], reverse=True)[:15]:
    print(f"[{h['points']}pts {h['num_comments']}c] {h['title']}")
    if h.get('url'): print(f"  {h['url']}")
```

### AI/ML engineering newsletters and blogs (deep dives)

Read the last 2-3 weeks for what's being discussed and argued:

- [The Batch](https://www.deeplearning.ai/the-batch/) — Andrew Ng / DeepLearning.AI
- [Ahead of AI](https://magazine.sebastianraschka.com/) — Sebastian Raschka (ML internals, fine-tuning, quantization)
- [Latent Space](https://www.latent.space/) — Swyx & Alessio (AI eng podcast + newsletter)
- [Simon Willison's Weblog](https://simonwillison.net/) — LLM tools, agents, prompt injection, practical experiments
- [Hugging Face Blog](https://huggingface.co/blog) — model releases, inference, open-source ecosystem
- [Eugene Yan's blog](https://eugeneyan.com/) — ML systems, evaluation, production patterns
- [Chip Huyen's blog](https://huyenchip.com/blog/) — ML infrastructure, LLM ops
- [Hamel Husain's blog](https://hamel.dev/blog/) — LLM evaluation, LLMOps, "your evals are broken"
- [Lilian Weng's blog](https://lilianweng.github.io/) — deep technical surveys on agents, RL, diffusion
- [Jason Liu's blog](https://jxnl.co/blog/) — Instructor, structured outputs, function calling
- [Daniel Feldman's blog](https://daniel-feldman.space/) — open-source models, on-device inference
- [Sway All Ways (Shreya Rajyalakshmi)](https://swayallways.com/) — LLM systems, data pipelines
- [The Sequence](https://thesequence.substack.com/) — ML/DL research summaries
- [AI Tinkerers](https://aitinkerers.org/) — community of AI builders
- [AK's Substack / YouTube](https://www.youtube.com/@AK_/) — paper walkthroughs
- [Zach Mueller's blog](https://zachmueller.dev/) — fast.ai, Hugging Face, open-source practical guides

### Framework and infra blogs

- [LangChain Blog](https://blog.langchain.dev/) — agents, LangGraph, LangSmith
- [LlamaIndex Blog](https://www.llamaindex.ai/blog) — RAG, data agents
- [OpenAI Cookbook / Blog](https://openai.com/blog) — new features, best practices
- [Anthropic Blog / Engineering](https://www.anthropic.com/news) — Claude, context engineering, safety
- [Google AI Blog / Research](https://research.google/blog/) — Gemini, research papers
- [vLLM Blog](https://blog.vllm.ai/) — serving, PagedAttention, throughput
- [Modal Blog](https://modal.com/blog) — serverless GPU, AI infra patterns
- [Replicate Blog](https://replicate.com/blog) — model serving, Cog, deployment
- [Together AI Blog](https://www.together.ai/blog) — open-source models, inference
- [Fireworks AI Blog](https://fireworks.ai/blog) — fast inference, fine-tuning
- [Anyscale Blog](https://www.anyscale.com/blog) — Ray, distributed AI
- [Pinecone Blog](https://www.pinecone.io/learn/) — vector search, RAG
- [Weaviate Blog](https://weaviate.io/blog) — vector DB, retrieval
- [Qdrant Blog](https://qdrant.tech/articles/) — vector search, filtering, performance
- [Chroma Blog](https://www.trychroma.com/blog) — embeddings, developer DX
- [Unstructured Blog](https://unstructured.io/blog) — document parsing, ingestion
- [Cursor Blog](https://cursor.com/blog) — coding agents, agent economics

### X/Twitter thought leaders

Search via Grok `--tools x_search` for recent posts by: Andrew Ng, Yann LeCun, Andrej Karpathy, Sebastian Raschka, Harrison Chase (LangChain), Jerry Liu (LlamaIndex), Swyx, Clem Delangue (Hugging Face), Greg Brockman, Simon Willison, Eugene Yan, Chip Huyen, Hamel Husain, Jason Liu (Instructor), Lilian Weng, Pieter Abbeel, Jeremy Howard (fast.ai), Zach Mueller, @_avichawla (model routing), @nikesharora (evals/orchestration), @orvi_onethread (agent costs).

Look for: posts with high engagement, original frameworks, candid takes on AI engineering, tooling debates, production failures, benchmarks. Andrew Ng's provocations and Karpathy's hot takes are good foils to argue with.

### Reddit communities (via Grok or direct)

- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) — open-weight models, inference, quantization
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/) — research papers, industry news
- [r/dataengineering](https://www.reddit.com/r/dataengineering/) — pipelines, infra
- [r/MLQuestions](https://www.reddit.com/r/MLQuestions/) — practical problems
- Direct JSON API (`reddit.com/r/{sub}.json`) often 403s — use Grok instead

### Course platforms and communities (Alexey's ecosystem)

- [DataTalksClub](https://datatalks.club/) — Alexey's community
- [AI Shipping Labs](https://aishippinglabs.com/) — Alexey's courses
- [AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) — Alexey's Maven course
- [MLOps Community](https://mlops.community/) — Slack, podcast, articles
- [AI Engineer SF](https://www.youtube.com/@AIEngineerSF) — talks and panels

### Publications and where to cross-post

- [Medium AI/ML tags](https://medium.com/tag/artificial-intelligence) — scan trending
- [Towards Data Science](https://towardsdatascience.com/) (Medium)
- [Towards AI](https://pub.towardsai.net/)
- [Papers with Code](https://paperswithcode.com/)
- [arXiv (cs.CL, cs.LG, cs.AI)](https://arxiv.org/list/cs.CL/recent)

### Model and tool radar

- [Hugging Face trending models](https://huggingface.co/models?o=trending)
- [OpenAI model releases](https://openai.com/blog)
- [Anthropic releases](https://www.anthropic.com/news)
- [Google AI / Gemini releases](https://blog.google/technology/ai/)
- [Meta AI / Llama releases](https://ai.meta.com/blog/)
- [Mistral AI releases](https://mistral.ai/news/)
- [vLLM releases](https://github.com/vllm-project/vllm/releases)
- [Ollama releases](https://github.com/ollama/ollama/releases)
- [SGLang](https://github.com/sgl-project/sglang) — fast serving
- AI infrastructure: Modal, Replicate, Together AI, Anyscale, Fireworks AI, Groq
- Vector DBs: Pinecone, Weaviate, Chroma, Qdrant, Milvus, pgvector, Redis
- Frameworks: LangChain, LlamaIndex, Instructor, DSPy, Haystack, Semantic Kernel, Pydantic AI
- Evaluation: Ragas, DeepEval, Promptfoo, Braintrust, LangSmith, Arize Phoenix

### Research papers worth tracking

- [arXiv cs.CL latest](https://arxiv.org/list/cs.CL/recent) — NLP and CL
- [arXiv cs.LG latest](https://arxiv.org/list/cs.LG/recent) — machine learning
- [Papers with Code trending](https://paperswithcode.com/)
- Key conferences: NeurIPS, ICML, ACL, EMNLP, ICLR, COLM
- [AK's paper summaries on YouTube](https://www.youtube.com/@AK_/)

### Podcasts and video

- [Latent Space Podcast](https://www.latent.space/podcast)
- [Practical AI](https://changelog.com/practicalai)
- [The TWIML AI Podcast](https://twimlai.com/podcast/)
- [Lex Fridman Podcast](https://lexfridman.com/podcast/) (for big-picture interviews)
- [AI Engineer SF YouTube](https://www.youtube.com/@AIEngineerSF)
- [Andrej Karpathy YouTube](https://www.youtube.com/@AndrejKarpathy)
- [3Blue1Brown](https://www.youtube.com/@3blue1brown) (for neural network deep dives)
- [Yannic Kilcher](https://www.youtube.com/@YannicKilcher) — paper explanations

## Topic-quality heuristics

An angle is strong when it passes all four:

1. **It has one arguable thesis.** You can state it in a sentence and a thoughtful engineer could disagree.
2. **It's timely.** Something concrete in the last 30-60 days makes the conversation feel urgent (a model release, a viral post, fresh benchmark, a production failure story, a new paper).
3. **It has a practical payoff.** You can hand the reader a method, framework, code pattern, checklist, or set of architecture decisions.
4. **It's citable.** Real sources exist for the stats and claims. If the angle relies on numbers you can't source, it's weak.

An angle is weak when:

- It's a trend roundup with no argument.
- It's evergreen with no current hook.
- The payoff is vague ("use AI responsibly").
- The claims can't be sourced.

## Angle-presentation format

Bring 3-5 angles back to Alexey, each like this:

```markdown
### Angle {N}: {Working title}

**Thesis (1 sentence):** {The argument the article makes.}

**Best template:** {Build Log / Practical Workflow / Argument Essay / Tool Teardown}

**Why it's hot:** {The concrete recent event/post/research/model release that makes it timely, phrased as the *debate* it triggered. Link 1-2 sources.}

**Where it's being discussed:** {Specific venues and voices — X handles, subreddits, HN threads, blog posts — with links. If it's only being discussed in one place, say so; that's a weaker signal.}

**Practical payoff:** {The checklist, framework, code pattern, or architecture decision the reader walks away with.}

**Risk / tradeoff:** {What's hard about writing it, or what nuance might get lost.}
```

Then present the angles to Alexey and ask him to pick one (or adjust). Once he picks, research that angle deeper, capturing every URL you'll cite, before moving to the outline.

**Presentation rules for topic pitches:**
- **Always pitch in English.** The articles are written in English, so working titles, theses, and angle descriptions are in English even if the conversation with Alexey is in Russian.
- **Every pitch must state why it's hot and where it's discussed** — specific venues, voices, and links, not "it's trending." Alexey uses this to judge whether the wave is worth riding.
- **Generate fresh topics from live research, not from existing drafts/backlog.** Don't scan the drafts folder or work-in-progress files when brainstorming topics unless Alexey explicitly asks for them. Fresh angles come from the Grok/HN/blog scan, not from the archive.

## Research workflow (how to actually do it)

**⚠️ Know the current date.** Before researching, check the actual current date (via `session_status` or the runtime timestamp in the inbound context). Always scope your Grok queries with the correct year and month. AI search tools often return results from 6-12 months ago if you don't explicitly anchor to the current date. Use phrases like "August 2026", "this week August 2026", or "past 2 weeks" in your queries.

1. **Start with Grok** — query X/Twitter + Reddit for trending AI engineering debates from the past 2 weeks. This is the fastest way to find what practitioners are arguing about right now. Include the current month/year explicitly in the query.
2. **Check HN front page** via Algolia API. Note anything AI/LLM/agent related with >100 points. Query by keyword for the past week.
3. **Scan TLDR AI** (today + yesterday). Note model launches, funding, big stories.
4. **Read 3-4 key blogs** (Simon Willison, Latent Space, Sebastian Raschka, Hamel Husain). What are they arguing about?
5. **Check LangChain / LlamaIndex / HF / Cursor blogs** — what did they ship this week?
6. **Synthesize**: What themes appear across 3+ sources (Grok + HN + blogs + TLDR)? What's getting argued about? What's the contrarian take?
7. **Pitch 3-5 angles** in the angle format below.

The goal is **pattern-matching across sources**, not summarizing one post. A trend that appears on Grok + HN + TLDR + a blog simultaneously is a much stronger angle than a single viral post.

## A note on citations

Citation density is a signature of these articles. Almost every stat, tool, person, event, benchmark, and technical claim gets an inline link. Capture URLs *as you research*, never reconstruct them later. If you can't find a real source for a claim during drafting, drop the claim or flag it `[VERIFY: needs source]`. Never invent a link or a statistic.
