---
title: "13 Real-Life AI Projects from AI Engineering Buildcamp Cohort 3"
created: 2026-09-03
updated: 2026-09-04
tags: [ai-buildcamp, projects, demo-day, newsletter]
status: draft
---

# 13 AI Projects from AI Engineering Buildcamp Cohort 3

The third cohort of my AI Engineering course wrapped this summer, and in this post I want to share what we built.

The projects are real-life and include an exam questions generator, a chess coach, a RAG pipeline, job tools, and research assistants.

This is not the first post about the projects that AI Buildcamp graduates. I wrote about the previous two cohorts earlier:

- First cohorst: [5 ideas for AI agents](https://aishippingblog.com/p/5-ideas-for-ai-agents-and-openais)
- Second cohort: [9 Real-Life AI Projects from AI Engineering Buildcamp Graduates](https://aishippingblog.com/p/9-real-life-ai-projects-from-ai-engineering)

In this post I want to describe some of these projects.

Some of the course participants presented their projects live on [Demo Day](https://youtu.be/kKUDZwdyuP4), so we'll start with them.

Let's start!

## 1) Exam Questions Generator by Salma Bouzid

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/exam-questions-generator/quizgen-landing-page.png" alt="Quizgen landing page inviting professors to generate exam questions from their own lecture slides">
  <figcaption>Quizgen generates exam questions from a professor's own lecture slides</figcaption>
</figure>

Salma is a data analyst who took the course to get better at building an AI app. She's leaving her job to work as a founder. Her project helps university professors generate exams from their own slide decks.

You upload a course PDF and pick how many questions you want. You also choose a mix of case studies, theory, and applied-concept questions. A professor can approve, edit, or reject each question, then export the exam. In the live demo she asked the model to tailor an HR-management exam to a business student in Berlin.

- The frontend is Next.js
- Supabase stores user actions plus API cost, PDF size, and regeneration prompts
- She started with Claude and later moved to OpenAI
- An LLM judge checks that a question is grounded in the course and not answerable without it


[Salma's LinkedIn](https://www.linkedin.com/in/salma-bouzid-45634762/)


## 2) ATS Gap Analyser by Amar Agrawal

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/ats-gap-analyser/01-example-result.png" alt="ATS Gap Analyser example result showing a 75 out of 100 moderate match, missing keywords, and improvement suggestions">
  <figcaption>ATS Gap Analyser's example result with a 75/100 match, missing keywords, and improvement suggestions</figcaption>
</figure>

Amar's [ATS Gap Analyser](https://github.com/Amar-Ag/ats-gap-analyser) is for people who apply to jobs and never find out what went wrong.

You paste a job URL and your CV. The app returns a match score out of 100, missing keywords, improvement suggestions, and a three-paragraph cover letter.

The app is live on [Streamlit](https://ats-gap-analyser.streamlit.app/). It doesn't store the CV or the job description, not even in the logs.

The agent has four tools.

- Extract job requirements
- Score the CV
- Suggest improvements
- Generate the cover letter

Suggestions retrieve from 50 ATS best-practice documents with minsearch.

- Eval used 50 manually written cases.
- Version 1 had 60% recall and 30% accuracy, and version 6 reached 88% recall.
- Amar kept accuracy lower on purpose: he would rather flag a missing skill than miss it.

[Amar's LinkedIn](https://www.linkedin.com/in/amar-agrawal-/)

## 3) Chess Coach Agent by Leo Cabibihan

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/chess-coach-agent/chess-coach-agent-practice.png" alt="Chess Coach practice screen showing a chess position, an engine-approved move, and the next scheduled review date">
  <figcaption>Chess Coach practice screen with a Stockfish-backed move recommendation and a scheduled retry</figcaption>
</figure>

Leo's first project was a chess-coach chat, but it wasn't useful. [Chess Coach Agent](https://github.com/leo-cabibihan/chess-coach-agent) starts from your real games instead. You import Lichess, Chess.com, or a PGN file. The app finds weak moments, explains them, and drills those positions.

Leo imported about 2,700 of his own Lichess games for the demo.

The stack includes FastAPI, React, Postgres with pgvector, and PydanticAI. It also uses Stockfish, BM25 lessons, Logfire, and it's [deployed on Render](https://chess-coach-agent.onrender.com/).

Practice uses spaced repetition at 1, 3, and 7 days, doubling up to 30. If there's no API key, deterministic templates still run. CI uses a TestModel so tests stay offline.

[Leo's LinkedIn](https://www.linkedin.com/in/leo-cabibihan/)


## 4) Document Preparation Agent by Paulien Out and Alena Fojtik

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/rag-dataprep-agent/document-preparation-pipeline.png" alt="ArXiv papers, manuals, and EU documents feed an LLM for parsing, classification, metadata extraction, and chunking before becoming JSON manifests">
  <figcaption>ArXiv papers, manuals, and EU documents feed the same preparation pipeline before becoming RAG-ready manifests</figcaption>
</figure>

Paulien and Alena build on-premise AI systems. They created [Document Preparation Agent](https://github.com/PaulienOut/rag-dataprep-agent), which is RAG with extra metadata. This metadata is needed for filtering: their clients often want to add query qualifiers like "only the latest documents" or "only files written by person X".

Because the customer data is private, the demo they used public arXiv papers, manuals, and EU documents. For v1 they focused only on PDFs only. There's also no UI, only CLI.

Each manifest has author and document type, plus a summary, keywords, and numbered chunks.


[Paulien's LinkedIn](https://www.linkedin.com/in/paulien-out-023a708/) and [Alena's LinkedIn](https://www.linkedin.com/in/alena-fojtik-ab439999/)

## 5) Research Radar by Hana Ben Ali

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/research-radar/research-radar-ratings.png" alt="Research Radar dashboard showing paper rating distribution and papers saved for later">
  <figcaption>Research Radar dashboard showing star-rating distribution and papers saved for later</figcaption>
</figure>

Hana is a structural engineer and a PhD student. She needs to stay of top of new research, but it's very difficult: there are 100–300 new papers per day on arXiv. Scanning all the titles and abstracts manually takes hours, and relevant work is easy to miss.

Her [Research Radar](https://github.com/55382/Research_Radar_agent_phd_assistant) solves this problem. It fetches the new papers every morning, ranks them against her interests, and emails her the best matches.

The app also builds her interest profile based on the papers she already read, and the new recommendations are based on it.

It works in two stages:

1. Semantic search with cosine similarity and an author boost, keep top 15.
2. Re-rank with an LLM ranker to get top 5.

The top 5 go out by email through Resend.

Stars from the email write back to `ground_truth_papers.csv`, which is both the knowledge base and the eval set.

She started from 26 papers she had rated herself. After tuning a 0.6 semantic / 0.4 LLM blend, NDCG@5 went from 0.871 to 0.923. A Streamlit dashboard shows timestamps, average score, and ratings over time. The hardest part was making the ranker get better each morning.

[Hana's LinkedIn](https://www.linkedin.com/in/hana-ben-ali-357b1a18b)


The other submissions weren't presented live. Here they are.

## 6) AI Diet Coach by Thet Su Win

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/ai-diet-coach/ai-diet-coach-weekly-plan.png" alt="AI Diet Coach weekly meal plan showing Southeast Asian dishes, meal tracking, and nutrition totals">
  <figcaption>AI Diet Coach weekly plan with Southeast Asian meals, tracking state, and nutrition totals</figcaption>
</figure>

[AI Diet Coach](https://github.com/thetsuwin66/ai-diet-coach-agent) is a meal planner for Southeast Asian users. Most Western diet apps ignore this group, that's why Thet decided to create an app.

You set goals, restrictions, cuisines, and location. The agent builds a 7-day plan from 256 recipes: 201 from TheMealDB and 55 Asian dishes added by the author. It tracks meals and weight, swaps meals, and builds a shopping list.

It also looks up USDA nutrition data and suggests nearby restaurants through Google Maps. The app is live on [Streamlit](https://ai-diet-coach-agent-htbjcoo2pylrfhdyv2cjbm.streamlit.app/).

A judge went through four versions on 88 labeled answers, and accuracy moved from 46.6% to 73.9%.

[Thet Su Win's LinkedIn](https://sg.linkedin.com/in/thet-su-win-169221172)

## 7) AI Learning OS by Wesley Tan

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/ai-learning-os/queue.png" alt="AI Learning OS queue showing staged learning resources and knowledge-base progress counts">
  <figcaption>AI Learning OS queue of staged resources, with knowledge-base and progress counts in the sidebar</figcaption>
</figure>

Wesley wanted to solve the watch-later graveyard problem. Self-learners save dozens of videos and articles across YouTube playlists, browser bookmarks, and note-taking apps, but most of this material is never used.

They do finish some content, but it rarely becomes structured knowledge that's possible to use later.

To solve that, Wesley created [AI Learning OS](https://github.com/wesleytanjiale/ai-learning-os).

It separates saved content from learned content. You queue YouTube videos, articles, markdown, and images. After a learning walkthrough, the system writes only what you actually studied into a knowledge base. Chat search cites that base and reports progress.

The agent has six tools

- Add to queue
- Browse queue
- Load for learning
- Consolidate to the knowledge base
- Search
- Get progress

Retrieval is hybrid BM25 plus dense vectors with reciprocal rank fusion. A 400-word chunk size with 5 results scored 15/15 on the tuning set. 600-word chunks with 7 results scored 12/15. An empty-knowledge-base test checks that the agent doesn't invent content.

[Wesley's LinkedIn](https://sg.linkedin.com/in/wesley-tan-jia-le-b31871219)

## 8) Applied ML Teaching Copilot by Marco Teran

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/applied-ml-teaching-copilot/01-grounded-answer.png" alt="Applied ML Teaching Copilot answer citing course material aml-001 and showing the tool-call panel">
  <figcaption>Applied ML Teaching Copilot answer grounded in course material aml-001, with the tool-call panel below</figcaption>
</figure>

Marco's [Applied ML Teaching Copilot](https://github.com/marcoteran/applied-ml-teaching-copilot) answers questions based on the Applied ML course materials. You can search, fetch a record by id, and get citations.

The stack is Streamlit, OpenAI, minsearch, PydanticAI, and Logfire. There's a [Streamlit demo](https://applied-ml-teaching-copilot.streamlit.app/).

The first judge scored 0.727 accuracy. The calibrated judge reached 1.0 on 33 labeled cases.

[Marco's LinkedIn](https://www.linkedin.com/in/marcoteran)

## 9) Datawarehouse Agent by Lars van Asseldonk

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/datawarehouse-agent/datawarehouse-agent-answer.png" alt="Datawarehouse Agent answer showing an incident count, success flags, and the read-only SQL query used">
  <figcaption>Datawarehouse Agent answer with success flags and the read-only SQL used for the incident count</figcaption>
</figure>

Lars's [Datawarehouse Agent](https://github.com/larsvasseldonk/datawarehouse_agent) is a natural-language-to-SQL assistant over Dutch Railways (NS) station-safety incidents. Non-technical staff ask a question and get a plain-language answer plus the SQL.

Lars used PydanticAI, OpenAI, DuckDB, and Streamlit. He also used Logfire, minsearch, and Plotly, and he recorded a [demo video](https://github.com/user-attachments/assets/9534b98f-0aab-442b-97e7-491813ba3e81).

## 10) WorkerChronicle by Miki Foster

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/work-chronicle/work-chronicle-overview.png" alt="WorkerChronicle project overview describing its worker's experience library and cover-letter generator">
  <figcaption>WorkerChronicle's experience library and cover-letter generator</figcaption>
</figure>

When applying for jobs, people often struggle to remember concrete examples from their past work and adapt them to each role. Miki built [WorkerChronicle](https://github.com/MikiYamFos/work-chronicle) to help with this.

You use can use it when applying for jobs:

- Before applying, you import your resume, previous cover letters, and raw notes to build a library of projects and accomplishments.
- When you find a job, you give it the job description. The app finds relevant examples from your library, shows where evidence is missing, and creates an editable cover-letter outline.
- Before an interview, it uses the same material to prepare likely questions and remind you which examples to discuss.

[Miki's LinkedIn](https://www.linkedin.com/in/mikifoster)

## 11) Multi-Agent Software Development Platform by Nitesh Mishra

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/multi-agent-dev-platform/01-pm-agent-user-stories.png" alt="Multi-Agent Software Builder showing PM agent user stories, acceptance criteria, and a review step">
  <figcaption>Multi-Agent Software Builder after the PM stage, with user stories and acceptance criteria awaiting review</figcaption>
</figure>

Nitesh's [Multi-Agent Software Development Platform](https://github.com/mishranitesh/AI_Engineering_Buildcamp_From_RAG_to_Agents/tree/main/capstone/multi-agent-dev-platform) turns a plain-English requirement into user stories, architecture, and backend code.

It also writes tests, reviews the generated code, and packages the result. Optionally, it can create a JIRA epic with stories and tasks, or open a draft GitHub pull request.

Each requirement goes through the same steps:

- PM agent creates user stories and acceptance criteria.
- Human confirmation approves the plan before code generation.
- Architect agent designs the system and creates a Mermaid diagram.
- Developer agent uses RAG to generate the backend code.
- QA agent writes the tests.
- Review agent uses RAG to find problems in the code.
- Artifact generation packages the code, tests, architecture, and README into a ZIP file.

[Nitesh's LinkedIn](https://www.linkedin.com/in/mishra-nitesh)

## 12) LearnMate AI by Dianne Bronola

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/learnmate-ai/review.png" alt="LearnMate active review session showing a question, a student answer, and evaluated feedback">
  <figcaption>LearnMate active review session with a generated question, student answer, and evaluated feedback</figcaption>
</figure>

Dianne's [LearnMate AI](https://github.com/dinobronx/learnmate-ai) turns a YouTube lesson into spaced-repetition review. Ingest builds a concept map, and a review agent quizzes you. Separate judges grade answers and code, and mastery decays so fading concepts come back.

Dianne put the due-concept logic, question order, mastery math, and session caps in code. The agent handles the review conversation. She designed it for `gpt-4o-mini`. A cosine match threshold of 0.65 scored 8/8 on an 8-query sweep. Judge calibration on 35-row CSVs came out at 85.7% for answers, 85.7% for code, and 74.3% for session conduct.

## 13) GapFinder by Katja Weber

<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/gapfinder/02-gap-report.png" alt="GapFinder report separating understood concepts from missed concepts and listing video timestamps to revisit">
  <figcaption>GapFinder report separating understood concepts from missed concepts and listing timestamps to revisit</figcaption>
</figure>

Katja's [GapFinder](https://github.com/katjaweb/gapfinder) is a study tool for long YouTube tutorials. It fetches the transcript, chunks it, and asks diagnostic questions.

Then it grades your answers against the video and report:

- what you understood vs what you missed
- which sections you should rewatch

The stack is PydanticAI, OpenAI, Streamlit, Logfire, and minsearch.

[Katja's LinkedIn](https://www.linkedin.com/in/katjaweber/)


## New Cohort

I'm happy to see these projects. At the same time, I want more participants to make it to the finish line and graduate with a completed project.

This is one of my main priorities for the next cohort. I'm actively researching what helps learners stay on track and finish ambitious projects, and I'll apply what I learn to the course. You'll see the results in the upcoming cohort.

The next cohort of the [AI Engineering Bootcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) starts on September 21.

If you want to build a system like these, join us. Use code "SUBSTACK" to get 20% off.
