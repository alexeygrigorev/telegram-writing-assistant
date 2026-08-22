---
title: "9 Real-Life AI Projects from AI Engineering Buildcamp Graduates"
date: 2026-05-02
url: https://aishippingblog.com/p/9-real-life-ai-projects-from-ai-engineering
---

The second cohort of my AI Engineering course finished a few weeks ago, and in this post I want to share with you what we built. The projects are real-life and include personal assistants, professional tooling, and health-case assistants.

Some of us presented the projects live a few weeks ago on the demo day, so we’ll start with them.

### 1) bAIpacking Agent by Eduardo Gonzalo Almorox

[![alt text](https://substackcdn.com/image/fetch/$s_!H-xY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F162b3879-74ec-44e4-b004-99c9f744a68c_1428x959.png)](https://substackcdn.com/image/fetch/$s_!H-xY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F162b3879-74ec-44e4-b004-99c9f744a68c_1428x959.png)

Edu’s [bAIpacking Agent](https://github.com/edugonzaloalmorox/baikpacking-agent) helps long‑distance cyclists decide which tires, drivetrain, and bags to use for specific races. The agent scrapes event reports from [DotWatcher](https://dotwatcher.cc/) (a platform for bike races), stores them in PostgreSQL, and builds a RAG pipeline.

On the backend side, FastAPI resolves the event name, finds similar events, retrieves rider setups, and summarizes evidence. Then the results are presented via a Reflex UI.

Evaluation runs offline: each recommendation call is logged and later scored by a judge script.

### 2) Meal‑Map by Pavlo Skorodziievskyi

[![215FD3BC-D69B-421E-B74E-4B318712F5D3](https://substackcdn.com/image/fetch/$s_!V-d1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59d966c5-4281-4294-936d-3b61296d3dca_2882x2692.png)](https://substackcdn.com/image/fetch/$s_!V-d1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59d966c5-4281-4294-936d-3b61296d3dca_2882x2692.png)

Pavlo’s [Meal‑Map](https://github.com/elgrassa/CapstoneMealMapSimplified) is a meal planner for an entire family. It takes into account dietary preferences, goals and allergies. The output is a list for grocery shopping as well as a list of recipes.

The knowledge base consists of 4 public‑domain nutrition sources chunked into 28 documents. The agent interacts with the knowledge base using 9 tools such as nutrition lookup, recipe search, and meal‑plan generation.

Evaluation uses a hand‑crafted ground-truth set, an LLM judge, and a search parameter sweep to tune retrieval. The agent limits calls to 20 LLM requests per session and $0.50 of cost per day; once exceeded, it downgrades to deterministic logic.

### 3) Engineering Decision Memory Agent by Camila Gaitan Mosquera

[![Image 3](https://substackcdn.com/image/fetch/$s_!p4nq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff245de07-fadc-4b83-846f-bf5154e73016_1678x937.png)](https://substackcdn.com/image/fetch/$s_!p4nq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff245de07-fadc-4b83-846f-bf5154e73016_1678x937.png)

Engineering Decision Memory Agent helps engineering teams recover context from past technical decisions. It indexes ADRs (architecture decision records), RFCs (request for comments), and postmortems so engineers can ask questions like “Why did we move from a monolith to microservices?” or “Why was Kafka chosen over SQS?”

The flow for the demo:

* Camila indexed around 21 documents.
* The system split them into overlapping chunks, embeded them with a Hugging Face model, stored them in ChromaDB.
* On user query, the system retrieves the most relevant chunks for a question, and passes them to Claude as context.
* Claude returns a structured JSON response that maps directly to UI cards: decision, alternatives considered, tradeoffs, context and constraints, and source documents.

Camila also built a monitoring dashboard with queries per day, answers found vs. not found, latency distribution, token usage, interaction history, and basic thumbs-up feedback. Her next step is to rebuild the same agent with [spec-kit](https://github.com/github/spec-kit) to define clearer requirements, constraints, and implementation details.

### 4) VoiceIssue Agent by Mladen Maric

[![Image 4](https://substackcdn.com/image/fetch/$s_!qmIC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75b8355e-b055-4e94-936f-6da39c96e319_1496x1051.png)](https://substackcdn.com/image/fetch/$s_!qmIC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75b8355e-b055-4e94-936f-6da39c96e319_1496x1051.png)

The [VoiceIssue Agent](https://github.com/lomodev-mmaric/voice_issue_code) lets users create GitHub issues via voice through Telegram.

When you have a lot of projects, keeping track of ideas is difficult, especially when you’re away from your computer. The agent simplifies this process by letting you use voice notes: you simply dictate your idea, and the bot assigns it to appropriate project. Before making any actions, the bot asks for a confirmation.

Everything is deployed via Docker Compose. Additionally, services include an interface for managing secrets, a session dashboard connected to the PostgreSQL log database, and a Grafana dashboard for analyzing cost and latency. There’s also an LLM‑as‑judge container that scores each session to filter out low-quality requests.

### 5) Medical Transcription App by Spyros Koumarianos

[![Image 5](https://substackcdn.com/image/fetch/$s_!2CFN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1b1ff55-add1-438e-a0c6-34b3754f6e43_974x289.png)](https://substackcdn.com/image/fetch/$s_!2CFN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1b1ff55-add1-438e-a0c6-34b3754f6e43_974x289.png)

Spyros developed an app for clinicians to turn doctor-patient sessions into actionable [SOAP notes](https://www.ncbi.nlm.nih.gov/books/NBK482263/). This is information is sensitive, so it’s important to do everything locally. The app transcribes with a local Whisper model, performs basic diarisation (speaker disambiguation), and summarizes the discussion into a SOAP note using a local Llama model.

Operating entirely offline, doctors can disconnect their computers from the internet and create notes without transmitting audio to any server. Processing a three-minute recording takes around ten minutes on regular hardware without any GPUs.

Some of the projects weren’t presented live on the Demo day. I’ll describe them here too.

### 6) Cyber Sachet by Nirajan Acharya

[![Image 6](https://substackcdn.com/image/fetch/$s_!mFSN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7546ef35-dea8-4c12-a799-2f7264488d10_2094x1116.png)](https://substackcdn.com/image/fetch/$s_!mFSN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7546ef35-dea8-4c12-a799-2f7264488d10_2094x1116.png)

[Cyber Sachet](https://github.com/nirajanacharya/Cyber-Agent) is a bilingual AI assistant for cybersecurity awareness. The agent targets Nepali users who need guidance on phishing, social engineering, and legal penalties. In Nepal, this information is scattered and often available only in English.

It uses a local knowledge base and selects tools based on the user’s intent, such as semantic search, law search, or penalty check. Responses are provided in both English and Nepali and include citations.

It uses Logfire for monitoring, and includes an LLM judge to measure accuracy, precision, and recall. The app is deployed on Streamlit Cloud for evaluation.

### 7) SnapSplit by James Watkins

SnapSplit is an AI‑powered receipt‑splitting app.

The target users are people who go to restaurants often, and often with the same group of friends. You upload a picture of a restaurant bill, and a vision model extracts the line items. Then the system understands who each dish belongs to and then splits the bill.

If any mismatches are detected, it re-runs OCR with specific hints and escalates to human review if needed.

### 8) AMR Awareness Platform by Juan Perez Prim

[![Image 7](https://substackcdn.com/image/fetch/$s_!36-D!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88698511-7d27-47c0-90f5-60b4e0454f7a_1784x694.png)](https://substackcdn.com/image/fetch/$s_!36-D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88698511-7d27-47c0-90f5-60b4e0454f7a_1784x694.png)

Juan’s [Antimicrobial Resistance (AMR) Awareness Platform](https://github.com/juanpprim/amr_ai) educates users about the causes, risks, and prevention of AMR.

A pipeline ingests data from 15 sources, including WHO, CDC, FAO, PubMed, and Our World in Data, and converts HTML and PDF documents into Markdown. The text is chunked and embedded with BioBERT. Retrieval combines BM25 keyword search with BioBERT semantic search via reciprocal rank fusion.

A PydanticAI agent, backed by Claude, answers questions with citations via a Gradio interface.

### 9) AI Regulation Research Assistant by Léonore Tideman

[![Image 8](https://substackcdn.com/image/fetch/$s_!FO3C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3afcbd82-ab7a-4e9e-890d-17dc11e11144_1770x826.png)](https://substackcdn.com/image/fetch/$s_!FO3C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3afcbd82-ab7a-4e9e-890d-17dc11e11144_1770x826.png)

[AI Regulation Research Assistant](https://github.com/LEMTideman/MyAgent) helps practitioners navigate AI compliance across European, US, and Dutch jurisdictions.

The pipeline:

* A scope guard filters out off-topic prompts.
* The agent uses a local retrieval system over a curated corpus before performing a web search.
* The web search utilizes Brave Search combined with Jina Reader to fetch and clean page content.
* The agent connects to [Ansvar](https://ansvar.eu/)’s external legal data services (EU, US, Dutch, and automotive regulations) and uses them to answer legal questions.

Integration tests ensure the agent routes questions correctly, and an LLM judge scores answers against structured compliance criteria.

I’m really happy to see these projects! We’ve already started Cohort 3 (now we’re finishing week 3). I’m very excited to see what we will build this time!

If you’re planning to enroll in the next edition of the course, join the mailing list. I don’t know when exactly I’ll run it, but you’ll be the first to know about it.

[Join Mailing List](https://maven.com/alexey-grigorev/from-rag-to-agents)

## What I’ve Been Working On Recently

### 1. Updated “Create Your Own Coding Agent” workshop

I went to MLCon Amsterdam last week to give a workshop about building your own coding agent.

Things change quickly, that’s why I decided to update [my old workshop](https://dev.aishippinglabs.com/workshops/building-coding-agent-python-django) and equip the agent from there [with skills](https://dev.aishippinglabs.com/workshops/coding-agent-skills-commands). The result is [the “Coding Agent v2” workshop](https://github.com/alexeygrigorev/workshops/tree/main/coding-agent-v2) that I presented in Amsterdam.

If you want to see more content like that and learn from me, join AI Shipping Labs - we host similar workshops regularly.

### 2. AI Shipping Labs: New Website + Accountability Sprint

[![Image 9](https://substackcdn.com/image/fetch/$s_!cKfJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf899920-44c3-4291-bcd1-7a7ac2ccf884_2580x1478.png)](https://substackcdn.com/image/fetch/$s_!cKfJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf899920-44c3-4291-bcd1-7a7ac2ccf884_2580x1478.png)

I continue working on the Django website for AI Shipping Labs. Right now, I am taking all my AI-related workshops, updating them and posting them there. For now, you can see them on [the dev version](https://dev.aishippinglabs.com/workshops) of the website, but soon [aishippinglabs.com](http://aishippinglabs.com) will serve this new content too.

Also, AI Shipping Labs already has 81 members.

Next week, we start a 6-week accountability sprint. [I wrote about the idea earlier](https://alexeyondata.substack.com/p/tired-of-learning-ai-alone-were-launching) and now we’re ready! It will include weekly check-ins to report progress and blockers. By the end, everyone will finish with a project.

For early joiners, we develop a personalized plan based on your goals and background and lay out the exact steps for the sprint. Valeriia and I already created more than 20 plans, and we’re very excited to see how it goes.

You can still join us as the sprint just starts.

[Join AI Shipping Labs](https://aishippinglabs.com/#tiers?utm_source=alexey_on_data&utm_medium=email&utm_campaign=ai_shipping_labs&utm_content=2026_04_24)

### 3. Third DataTalks.Club Meetup

[![Attendees gather in a modern venue, listening to speakers discussing agentic search and workflows, with presentation visuals displayed behind them.](https://substackcdn.com/image/fetch/$s_!nBwO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3709e60f-90ef-49e0-bca7-41eb56e5aa28_1200x675.png)](https://substackcdn.com/image/fetch/$s_!nBwO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3709e60f-90ef-49e0-bca7-41eb56e5aa28_1200x675.png)

On April 28, we hosted our third offline DataTalks.Club meetup of 2026.

Thanks to everyone who joined and stayed to discuss. Also, I’d like to thank Ivan Potapov for organizing the meetup, Zalando for hosting us, and Hopsworks and Elastic for sponsoring the pizza.

We’ll continue doing more offline meetups this year!

## Tools

[![Image 11](https://substackcdn.com/image/fetch/$s_!rDUP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c7b95e0-71c5-4925-ae16-18a02e0281ec_1462x410.png)](https://substackcdn.com/image/fetch/$s_!rDUP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c7b95e0-71c5-4925-ae16-18a02e0281ec_1462x410.png)

* [DeepTutor](https://github.com/HKUDS/DeepTutor) is an open-source AI tutoring assistant that turns your documents into an interactive learning environment. It combines RAG-powered knowledge bases with multiple learning modes - chat, guided learning journeys, quiz generation, deep research, and an AI co-writer - all sharing the same conversation context. It also supports persistent “TutorBots” that remember your learning history and evolve over time.
* [Tech Debt Audit](https://github.com/ksimback/tech-debt-skill) is a Claude Code skill that produces a thorough, file-cited tech debt audit of an entire codebase rather than a generic best-practices checklist. It runs a three-phase protocol - orient, audit across nine dimensions, deliver - with required file:line citations on every finding and a "looks bad but is actually fine" section that catches shallow analysis. The output is a persistent TECH\_DEBT\_AUDIT.md artifact you can commit and re-run, with resolved findings tracked over time.

## Resource

[![Banner](https://substackcdn.com/image/fetch/$s_!IN44!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba00638f-b057-48f7-a74c-4a62fd449aab_1200x488.png)](https://substackcdn.com/image/fetch/$s_!IN44!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba00638f-b057-48f7-a74c-4a62fd449aab_1200x488.png)

[Awesome AI Apps](https://github.com/Arindam200/awesome-ai-apps) is a collection of 70+ practical examples for building LLM-powered applications, covering everything from simple chatbots to advanced multi-agent systems. The projects span starter agents, RAG applications, MCP integrations, memory-enhanced agents, and production-ready workflows using frameworks like Agno, CrewAI, LangChain, PydanticAI, and AWS Strands. It is a great source of inspiration for AI project ideas with working code you can study and extend.
