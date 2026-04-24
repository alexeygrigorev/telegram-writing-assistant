---
title: "AI Engineering Buildcamp Cohort 2 - Demo Day"
created: 2026-04-24
updated: 2026-04-24
tags: [ai-buildcamp, demo-day, capstone-projects, community]
status: draft
---

# AI Engineering Buildcamp Cohort 2 - Demo Day

Demo day for the second cohort of the AI Engineering Buildcamp (from RAG to Agents). Five participants presented their capstone projects live, two via recording. Other cohort members submitted projects through the course platform but did not present at the demo.

Recording: [Demo day on YouTube](https://www.youtube.com/watch?v=4k_3vOINbgM)[^1]

All submitted projects are listed on the [course management platform](https://courses.datatalks.club/ai-buildcamp-2/projects)[^2]. The course uses pseudonyms for graded submissions, so projects are matched to authors by GitHub repo owner.

## Projects Presented at Demo Day

### Bikepacking Recommender Agent (Edu Gonzalo Almorox)

Repo: https://github.com/edugonzaloalmorox/baikpacking-agent[^3]

A recommender for bike packing events. Bike packing is long-distance cycling where logistics matter as much as physical condition - riders need to know exactly what gear and bags to bring for a specific race. Setup advice is scattered across articles, rider interviews, and equipment lists, with no single place to ask "what should I bring to Transpyr?" and get a grounded answer.

The project scrapes setups from a website that tracks bikepacking events, loads them into PostgreSQL with pgvector, and serves recommendations through a chat UI and REST API. About 200 events are indexed.

Tech stack: Python 3.12, FastAPI, Reflex (UI), PostgreSQL + pgvector, Ollama (embeddings), pydantic-ai, Pydantic, Logfire, Streamlit, Playwright + BeautifulSoup (scraping), Docker Compose, uv, pytest.

Key features:

- Event-aware retrieval with three grounding tiers (exact_event, similar_event, unknown_global) and matching writer policies (strict_grounded, pattern_based, generic_fallback) to limit hallucination
- KB pipeline (scrape, clean, load, embed) over rider chunks with vector similarity search
- Deterministic offline evaluation from manual_scenarios.yaml, a Streamlit eval dashboard, a human review loop that feeds reviewer hints back into the prompt, and an LLM judge over live runs
- Logfire + pydantic-ai instrumentation capturing agent runs, tool-call traces, and per-request live-eval rows
- Full Docker Compose stack (Postgres+pgvector, Ollama, FastAPI, Reflex UI) with a Makefile bootstrap

Edu noted that the hardest part was getting good recommendations rather than just any recommendation. Two things helped: enforcing structured output and not letting the model do too much - delegating only the final wording to the LLM while everything else (event resolution, retrieval planning, evidence summarization, policy selection) runs through deterministic stages. Deployment was the next challenge - the combination of Postgres connections, pgvector indexes, and Ollama in Docker did not come together in the available time, so the project remains local for now.

This project was presented at the demo but was not submitted through the course platform.

### Meal-Map (Pablo)

Repo: https://github.com/elgrassa/CapstoneMealMapSimplified[^2]

A family meal-planning agent. The project is designed for personal use - tracking calorie and nutrient consumption for every family member and suggesting meals that respect allergies, medical constraints, age gaps, weight, and breastfeeding status. Generic AI chatbots either do not cite sources, give unsafe medical claims, or are not allergen-aware. Recipe apps skip the nutrition side.

Pablo demoed adding a family member with preferences and allergies, then generating a weekly meal plan with highlighted nutritional gaps versus recommendations. The system flags deficiencies (fiber, calcium) and suggests recipes from the indexed corpus.

Tech stack: Python 3.13, PydanticAI, OpenAI gpt-4.1-mini, minsearch (BM25), sentence-transformers (RRF hybrid), Streamlit, SQLite, Docker/docker-compose, uv, Makefile, GitHub Actions CI, pytest, mutmut.

Key features:

- RAG agent with 9 documented tools, BM25 retrieval over a baked 4-source / 28-chunk corpus with SHA256 provenance manifest
- Three-tier response strategy: built-in LLM invoke, RAG with curated nutrition data, and a fallback when neither has enough data (so the system says "not enough data, retry later" instead of inventing an answer)
- Authority-weighted evidence gate that classifies responses as supported / fallback / refused, with deterministic fallback path when no API key is set
- Input guardrails: intent classification (meal/nutrition only), prompt-injection blocking, curative-claim refusal with clinician-referral disclaimer
- Personalization against a household profile (adults, children, allergens, cuisine preferences, cook time)
- LLM-as-Judge evaluation (6 criteria), 20-case hand-crafted ground truth, chunk-strategy x top_k tuning sweep
- Monitoring: JSONL logs, SQLite feedback DB (thumbs up/down), Streamlit dashboard, logs-to-ground-truth pipeline
- Cost guardrails: 20 LLM calls/session/hour and a $0.50 per UTC day cap with auto-downgrade to deterministic path

Pablo also covered the deployment side - an external system was pushing directly to main, so he had to disable his commit history and PR checks temporarily. His takeaway: sometimes you need to bypass your CI/CD on purpose. Hybrid search added latency without helping much for this corpus, so he is rethinking that part. Around 40 recipes are indexed so far, and he plans to add more before the submission deadline.

### Engineering Decision Memory Agent (Camila)

Capstone repo: https://github.com/vccat/2026_ai_engineering_capstone[^2]

An agent that indexes architectural decision records (ADRs/ATRs), RFCs, design documents, and postmortems so that engineers can ask questions about past decisions and get structured answers. Engineering teams make hundreds of technical decisions over time. Those decisions live across many documents that nobody has time to read, and the engineers who made them often leave the team. New engineers have no way to understand why the system is the way it is.

Camila demoed two queries against 21 indexed documents: "why did we move from monolithic to microservices?" and "why was Kafka chosen over SQS?". Each answer comes back with the decision, the alternatives that were considered, the tradeoffs, the context and constraints, and the source documents with relevance scores. If the knowledge base does not have the answer, the agent says so - no hallucination.

Pipeline:

1. Documents loaded and split into overlapping chunks
2. Chunks embedded with a HuggingFace model and stored in ChromaDB
3. Question comes in, most relevant chunks retrieved
4. Chunks passed to Claude with a JSON schema that maps directly to UI cards
5. Response rendered with structured fields (decision, alternatives, tradeoffs, context, sources)

Tech stack: Python, ChromaDB, HuggingFace embeddings, Claude (anthropic), Streamlit, custom monitoring dashboard.

Key features:

- Structured responses with explicit "I don't have the information" path
- Monitoring dashboard with queries per day, answer-found vs not-found, latency distribution, token usage per query
- Interaction history with feedback (thumbs up), chunk count, token count, latency

Next step Camila mentioned: rebuilding the same agent with Spec Kit, using Claude with explicit requirements and constraints to compare the developer experience.

Note: the linked capstone repo currently contains an earlier Kids Science Chatbot version (a different agent built on Pydantic AI with Qdrant over SciShow Kids transcripts). The Engineering Decision Memory Agent is the version Camila demoed live.

The discussion after the demo highlighted how teams often have all the documentation they need (Jira, Coda, Confluence) but lose track of where decisions live once they are made. Indexing only the "paper trail" (ADRs/RFCs) rather than all of Confluence avoids overload, and a tool like this could save hours of ADR review for principal engineers.

### VoiceIssue Agent (Ladden)

Repo: https://github.com/lomodev-mmaric/voice_issue_code[^2]

A Telegram bot that lets you file structured GitHub issues by voice across multiple repositories. The motivation came directly from a problem Alexey shared with Ladden: I have many GitHub repos, sometimes I get an idea on the go (e.g. while shopping), and to capture it I need to open GitHub, find the right repo, create an issue, and type or dictate the description. A bot where you send a voice message and it figures out the right repo and files a structured issue would be much better.

Ladden demoed sending a voice message saying "we have Albanian hackers attacking our front end and there's denial of service, please report it to security team". The bot first evaluated whether this was on-topic, decided it was a legal/security issue rather than a bug, and refused. After a follow-up message providing more technical detail (JavaScript code structure, possible SQL injection), the bot drafted a structured front-end bug report, asked for human approval, and only then created the GitHub issue.

Tech stack: Python 3.10+, pydantic-ai, OpenAI (transcription + LLM), python-telegram-bot, GitHub REST API, PostgreSQL, Streamlit, Grafana, Docker Compose, uv, pytest.

Key features:

- Voice-to-issue pipeline: Telegram voice message, transcription, PII scrubbing, repo routing, structured markdown issue draft
- Human-in-the-loop approval via Telegram inline keyboard before any GitHub issue is created
- Multi-repo routing: bot picks the correct target repo from a comma-separated GITHUB_REPOS allow-list (uses minsearch / RAG over repos to identify the right project)
- LLM-as-a-Judge container that asynchronously scores each session 1 to 5 for quality, so off-topic or low-quality requests do not get filed
- Two Streamlit UIs (password-protected): an Orchestrator that streams Docker logs and overrides secrets, plus a Sessions dashboard over Postgres
- Grafana analytics for aggregate LLM costs, total issues created, and P50 interaction latencies
- Local CLI mode via Makefile (make cli/bot/admin/dashboard/online-judge/test-all) so components run without Docker

Six-container microservice stack orchestrated by docker-compose: bot, judge, orchestrator (Streamlit, port 8501), session dashboard (Streamlit, port 8502), Postgres, and Grafana (port 3000). Deployed on Google Cloud - Ladden noted you need at least a medium VM (4 GB RAM, 50 GB storage, dual core); smaller instances choke. The $10/month developer credit covers it.

In the discussion, Ladden mentioned not having tried Logfire - he is using HTTP/OTel into Grafana directly, which works fine. Telegram was chosen over WhatsApp for ease of bot creation: in Telegram you ask BotFather for a token and you have a bot in minutes.

### Offline Medical SOAP Notes (Spiros)

A local-first dictation app for medical practitioners. The motivation came from a conversation with friends in the medical field (doctors, a psychotherapist) in Canada. They all said: "AI is great, but I would never put my medical documents online." Canadian data laws around US data centers (the data can be subject to US legal access if it leaves Canada) make any cloud tool a non-starter for many practitioners.

The biggest pain point is dictation. Doctors spend up to four to five hours after seeing patients writing up notes. Some now charge for services that require additional dictation. Spiros built a vibe-coded prototype that:

1. Transcribes the meeting using a local Whisper model
2. Diarizes (loosely) by classifying the two roles with a local model
3. Summarizes the transcript into a SOAP note (Subjective, Objective, Assessment, Plan)

The pitch is: doctor disconnects their computer from the internet, runs the model locally, gets their notes, no escape to the cloud. Spiros tested with a 3-minute recording of a student talking to a patient; processing took up to 10 minutes on his hardware, so performance still needs work.

Existing tools (e.g. Mentalyc) are online, which is exactly what these doctors do not want. Even the option of running on-device models (Gemma 3, Apple's on-device AI, Google's edge models) was discussed during Q&A as a future path. The medical and nuclear sectors are very wary of any data center, so an air-gapped tool has a real use case.

Spiros is continuing the project and may apply for a green initiative / waste reduction grant to switch from his nine-to-five to working on it full time.

This project was not submitted through the course platform.

## Submitted but Not Presented at the Demo

These projects were submitted to the course management platform but were not presented live at the demo.

### Cyber Sachet (Nirajan Acharya)

Repo: https://github.com/nirajanacharya/Cyber-Agent[^2]

A bilingual (English/Nepali) AI assistant for cyber security awareness and Nepal cyber law (IT Act 2063, Digital Security Act 2024). Nepali users face fragmented cyber safety guidance and confusing legal references, with English-only technical advice creating a language gap.

Tech stack: Python 3.13, OpenAI (gpt-4o-mini), text-embedding-3-small, ChromaDB, Streamlit, Logfire, uv, pytest.

Key features:

- Multi-tool agent with intent-based tool selection (semantic_search, search_laws, search_awareness, check_penalty)
- Bilingual response generation in English and Nepali with source citations
- Monitoring via Logfire spans with token/cost estimation and user feedback hooks
- Full evaluation pipeline: scenario dataset, batch runs, manual labeling app, LLM judge with accuracy/precision/recall reports
- Live cloud deployment on Streamlit Cloud (https://nepalicyberagent.streamlit.app/)

Modular layout separates the core agent, knowledge documents, Streamlit UI, observability wrappers, and a notebook-first evaluation pipeline. The agent follows a 5-step workflow (intent detection, tool selection, grounded context build, answer generation with citations, metadata return for tracing) backed by a ChromaDB vector store over three Nepal-specific cyber law and awareness documents. Submission scored 32 on the platform.

### AMR Awareness Platform (Juan Prim)

Repo: https://github.com/juanpprim/amr_ai[^2]

An AI-powered educational RAG platform for Antimicrobial Resistance (AMR). AMR is a global health threat with authoritative information scattered across WHO, CDC, FAO, scientific literature, and government reports - hard for the public, students, and clinicians to access reliably.

Tech stack: Python 3.13, uv, PydanticAI, Anthropic Claude (claude-sonnet-4-6), ChromaDB, BioBERT embeddings, BM25, Reciprocal Rank Fusion, Scrapy, Docling, Gradio 5, pytest.

Key features:

- Multi-source ingestion pipeline covering 15 AMR sources (PubMed, WHO GLASS, CARD, NCBI NDARO, CDC, FAO, World Bank, UN) via API, HTML scraping, and PDF conversion with Docling
- Hybrid retrieval combining BioBERT semantic embeddings with BM25 keyword search, fused via Reciprocal Rank Fusion for biomedical relevance
- PydanticAI agent backed by Claude that produces grounded, source-cited answers through a Gradio chat UI

A `pipeline/` layer (sources registry, scraper, Docling converter, downloader orchestrator) handles ingest from raw HTML/PDFs to markdown; a `rag/` layer chunks markdown, ingests into a persistent ChromaDB collection with BioBERT embeddings, and serves hybrid retrieval. Submission scored 26 on the platform.

### AI Regulation Research Assistant (LEMTideman)

Repo: https://github.com/LEMTideman/MyAgent[^2]

A pydantic-ai agent that answers practical AI compliance questions across jurisdictions (EU, US, NL) and sector-specific frameworks (e.g. automotive). It maps legal obligations to compliance controls and evidence artifacts so practitioners get a single grounded research interface.

Tech stack: Python 3.11+, pydantic-ai, OpenAI gpt-4o-mini, MCP (Streamable HTTP), Qdrant, Brave Search, Jina Reader, Docling, DeepEval, pytest/pytest-asyncio, uv, youtube-transcript-api, yt-dlp.

Key features:

- Scope guard that filters out off-topic prompts before invoking the LLM
- Local RAG over a curated corpus (PDFs, arXiv, Substack, YouTube transcripts) via Qdrant
- Web search + clean-page extraction pipeline (Brave + Jina Reader) with deduplication and truncation
- Filtered MCP toolsets for EU AI Act, US regulations, Dutch law, and automotive compliance (Ansvar AI servers)
- Integration tests verifying the agent routes questions to the correct tools
- LLM-as-a-judge evaluation (DeepEval) scoring answers against structured legal/compliance criteria

Built on the pydantic-ai Agent abstraction with a single gpt-4o-mini model, two local Python tools (RAG, web search), and four remote MCP toolsets exposed via MCPServerStreamableHTTP, each filtered to a curated subset of tools and namespace-prefixed (eu/us/nl/automotive). Shared runtime state (RAG client, Brave session) is injected through a typed Deps object via build_deps(), and an out-of-scope guard short-circuits irrelevant queries before model calls.

## Sources

[^1]: [Demo day video on YouTube](https://www.youtube.com/watch?v=4k_3vOINbgM) and [20260424_183801_AlexeyDTC_msg3641.md](../inbox/used/20260424_183801_AlexeyDTC_msg3641.md), [20260424_183909_AlexeyDTC_msg3643_transcript.txt](../inbox/used/20260424_183909_AlexeyDTC_msg3643_transcript.txt)
[^2]: [Course management projects page](https://courses.datatalks.club/ai-buildcamp-2/projects)
[^3]: Project link shared in [20260424_183801_AlexeyDTC_msg3641.md](../inbox/used/20260424_183801_AlexeyDTC_msg3641.md) (not submitted via the course platform)
