---
title: "From Google Docs to an Automated FAQ System for DataTalks.Club Courses"
date: 2026-04-24
url: https://aishippingblog.com/p/from-google-docs-to-an-automated
---

At DataTalks.Club, we run [free courses](https://datatalks.club/blog/guide-to-free-online-courses-at-datatalks-club.html) like ML Zoomcamp, Data Engineering Zoomcamp, MLOps Zoomcamp, and LLM Zoomcamp. Since 2021, we’ve been launching new cohorts every year, and with each new cohort, the same questions kept coming up.

[![DataTalks.Club courses overview diagram](https://substackcdn.com/image/fetch/$s_!uOb6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa523f37d-16ab-4584-b077-9ecda988c680_1743x1457.png)](https://substackcdn.com/image/fetch/$s_!uOb6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa523f37d-16ab-4584-b077-9ecda988c680_1743x1457.png)

Overview of free DataTalks.Club courses

To deal with that, we created an FAQ.

The first version was a shared Google Docs FAQ. It worked well at first, but as the content grew, its limitations became clearer, so we eventually moved to a [proper FAQ website](https://datatalks.club/faq/) (here’s [its source repo](https://github.com/DataTalksClub/faq)).

[![Image 2](https://substackcdn.com/image/fetch/$s_!RDBF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bd430ca-c2e9-4185-8689-a8784deb3f96_2048x1394.png)](https://substackcdn.com/image/fetch/$s_!RDBF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bd430ca-c2e9-4185-8689-a8784deb3f96_2048x1394.png)

DataTalks.Club FAQ on a separate website

In this post, I’ll show how that system evolved:

* How we started with shared Google Docs
* How Alex Litvinov built a RAG-powered Slack bot to answer questions automatically
* How I migrated the FAQ to a Git-based static website using a parsing and cleanup pipeline
* How Fred Pearce built a GitHub Actions workflow for community contributions
* How the agent decides whether a proposal is a new entry, an update, or a duplicate
* How I use Claude Code to review and fix the pull requests created by the bot

This project also gives a broader view of retrieval-augmented generation (RAG). It is often framed as a way to answer questions over documents, but the same pattern is useful anywhere you need to search a large body of information and act on what you find. So the same pattern is useful for workflows like routing support tickets, finding similar products or articles, generating study materials, or maintaining an FAQ like this one.

## How We Started with Shared Google Docs

At our free DataTalks.Club courses, every year, each new cohort brings anywhere from 5,000 to 25,000 students, depending on the course.

Most of the course communication happens in Slack. And every time a new cohort starts, the same questions come up again:

* Can I still join?
* How do I set this up on Windows?
* Where do I submit homework?
* What should I do if something breaks?

Answering these questions over and over on Slack isn’t an efficient way to support a large learning community.

[![Image 3](https://substackcdn.com/image/fetch/$s_!ZG7s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb203654f-835e-4c1f-8034-354f0a08fbbc_2048x993.png)](https://substackcdn.com/image/fetch/$s_!ZG7s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb203654f-835e-4c1f-8034-354f0a08fbbc_2048x993.png)

Active discussions and peer support in our dedicated Slack community channel

So our first solution was simple: a shared Google Docs FAQ for each course. It was just a regular document with a defined structure, nothing fancy, but students could check whether their question had already been answered and add new entries themselves. That made contributions very easy and helped the FAQ grow over time.

[![Image 4](https://substackcdn.com/image/fetch/$s_!4J_W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49646dd8-b1e8-43ec-9ffe-06b0ee97b640_1280x725.png)](https://substackcdn.com/image/fetch/$s_!4J_W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49646dd8-b1e8-43ec-9ffe-06b0ee97b640_1280x725.png)

The old FAQ format in Google Docs, editable by anyone

To encourage people to contribute, we also added a small gamification element. Our courses already have leaderboards, where students earn points for homework and other activities. At some point, we added one extra point per homework for contributing something useful to the FAQ. Many students contributed without that incentive, but the extra point helped keep the FAQ fresh.

[![Image 5](https://substackcdn.com/image/fetch/$s_!N0GI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76fddad1-b32b-4ea8-a025-5487c69289cd_2048x1099.png)](https://substackcdn.com/image/fetch/$s_!N0GI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76fddad1-b32b-4ea8-a025-5487c69289cd_2048x1099.png)

The old version of the course leaderboard displaying student progress and achievements

[![Image 6](https://substackcdn.com/image/fetch/$s_!KRma!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F099583b0-0c8c-4f84-b14e-f593fd89ec77_922x1020.jpeg)](https://substackcdn.com/image/fetch/$s_!KRma!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F099583b0-0c8c-4f84-b14e-f593fd89ec77_922x1020.jpeg)

The current version of the course leaderboard with Alexander Daniel Rios’s individual profile

This setup was easy and frictionless, but over time, its limitations became obvious. Open Google Docs meant no real moderation, and vandalism happened more than once.

The FAQ also became too large to work well as a simple shared document. Across all Zoomcamps, it eventually grew to around 1,300 entries, with the Data Engineering Zoomcamp FAQ alone reaching roughly 500. Students asked questions at very different levels: about the course overall, specific modules, and homework within each module. At that scale, expecting people to read the whole document before asking in Slack was no longer realistic.

That is what led to the next stage: building a RAG-powered Slack bot that could answer questions automatically.

## Alex Litvinov’s Slack Bot

One of our community members, [Alex Litvinov](https://www.linkedin.com/in/aaalexlit/), built a [Slack bot](http://github.com/aaalexlit/faq-slack-bot) to make the FAQ more usable in practice.

At that point, the main problem was helping students find the right one when they needed it, without expecting them to manually search through hundreds of FAQ entries.

The bot solved that by bringing the FAQ directly into Slack. Instead of opening a large Google Doc and scrolling through it, students could ask a question in the course channel and receive an automatic answer.

[![Image 7](https://substackcdn.com/image/fetch/$s_!ZfgZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f8240c2-b593-45c0-a4cb-d919f4256568_1917x575.png)](https://substackcdn.com/image/fetch/$s_!ZfgZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f8240c2-b593-45c0-a4cb-d919f4256568_1917x575.png)

Example of a ZoomcampQABot answering a question from a Data Engineering Zoomcamp course participant

The bot is still running today, and it pulls data from several sources:

* FAQ documents: question-answer pairs from each course FAQ
* Slack history: past questions and answers from course channels
* GitHub repositories: course notebooks, code, and other materials
* YouTube subtitles: transcripts from course lectures

Each source is chunked according to its structure:

* FAQ content is split into question-answer pairs.
* Slack threads are treated as a single document consisting of the original question and the discussion.
* GitHub content is organized by file.

This produces more semantically complete chunks, which improves retrieval quality.

[![Image 8](https://substackcdn.com/image/fetch/$s_!vsX9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd824cee1-2eba-4fea-91d5-cd011f33fb5f_1438x917.png)](https://substackcdn.com/image/fetch/$s_!vsX9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd824cee1-2eba-4fea-91d5-cd011f33fb5f_1438x917.png)

Image from [Alex Litvinov’s GitHub repository](https://github.com/aaalexlit#llm-powered-question-answering-slack-bot)

The ingestion pipeline is scheduled to run daily with Prefect and runs inside Docker. Slack and Google Docs are pulled in through custom readers, then passed through LlamaIndex, which handles chunking and embedding. For embeddings, the bot uses BAAI/bge-base-en-v1.5, and the processed documents are stored in Zilliz Cloud.

The rest of the stack includes:

* LlamaIndex for the RAG pipeline
* Milvus locally and Zilliz Cloud in production for vector storage
* Cohere Rerank for reranking
* GPT-4o-mini for answer generation
* Slack Bolt with Socket Mode for Slack integration
* Upstash Redis for caching embeddings, which gives roughly a 5x speedup during ingestion
* LangSmith for observability
* Fly.io for hosting

The bot maintains separate query engines for each course, and routes each question to the appropriate engine based on the Slack channel ID. For each query, it retrieves 20 candidate documents, applies time weighting to prefer more recent Slack answers, and then reranks the results to the top 4 before passing them to the LLM. That time-weighting matters because some answers depend on deadlines, cohort-specific logistics, or temporary course instructions.

> You can see the full code [here](http://github.com/aaalexlit/faq-slack-bot).

This was a big improvement over the original Google Docs workflow. The Slack bot made the FAQ much easier to use. At the same time, the setup still depended on Google Docs as the source of truth, which still had maintenance problems: moderation, structure, and the fragility of an open document that anyone could edit.

At some point, the Google Docs FAQ was vandalized again, and Alex’s bot started having parsing issues. Those problems pushed me to make time to move the FAQ out of Google Docs and into a [dedicated website](https://datatalks.club/faq/) with proper moderation and a better reading experience.

[![Image 9](https://substackcdn.com/image/fetch/$s_!MNBG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0750683b-6609-40c8-99a4-f259542c2e85_2048x1394.png)](https://substackcdn.com/image/fetch/$s_!MNBG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0750683b-6609-40c8-99a4-f259542c2e85_2048x1394.png)

## How I Migrated the FAQ to a Static Website

### 1) Parsing the Google Docs

I already had code for parsing Google Docs into JSON. I originally wrote it for LLM Zoomcamp, where RAG is one of the course topics, and the FAQ made a useful dataset for experimentation.

[![Image 10](https://substackcdn.com/image/fetch/$s_!D8lv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0373613e-e6c0-4416-bbac-e0c1d02fbafa_2048x1131.png)](https://substackcdn.com/image/fetch/$s_!D8lv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0373613e-e6c0-4416-bbac-e0c1d02fbafa_2048x1131.png)

The parsing pipeline looks like this:

* Download the Google Doc as a DOCX file
* Use Python’s docx module to extract the content
* Use document headers to detect where questions end and answers begin
* Output JSON records with fields like text, section, and question

[![JSON documents format from parsed FAQs](https://substackcdn.com/image/fetch/$s_!GSlQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4c73172-21ed-4ff1-8177-d8432212917a_1280x770.jpeg)](https://substackcdn.com/image/fetch/$s_!GSlQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4c73172-21ed-4ff1-8177-d8432212917a_1280x770.jpeg)

The JSON format used for parsing, where each entry includes fields like text, section, and question

> You can find the notebook [here](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2024/05-orchestration/parse-faq-llm.ipynb). The code is not polished because it was written as a one-off notebook rather than a reusable production pipeline, but it was sufficient to extract the data.

### 2) Clining Up the Content with GPT-4o

Getting the text out was only half of the work. The extracted content still needed a lot of cleanup because formatting was inconsistent:

* Some answers had grammar issues.
* In some places, code appeared as screenshots instead of actual code blocks.

Cleaning all of that by hand would have taken too long, so I wrote a small script that sent the extracted entries to GPT-4o with instructions to standardize formatting, fix grammar, and turn code screenshots into proper code blocks. After a few evenings of running and checking the process, I had a much cleaner dataset ready to be turned into website content.

[![Image 12](https://substackcdn.com/image/fetch/$s_!m9US!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0e5a36d-4b57-49f9-b13e-b133cc5283ca_2048x1044.png)](https://substackcdn.com/image/fetch/$s_!m9US!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0e5a36d-4b57-49f9-b13e-b133cc5283ca_2048x1044.png)

Screenshot from a [cleanup notebook](https://github.com/DataTalksClub/faq/blob/main/notebooks/process-questions.ipynb)

### 3) Structuring the Content

Once the content was cleaned up, I reorganized it into a more structured format.

Instead of one large document per course, the new repository is organized like this:

* course
* module
* individual question

[![FAQ repository directory structure](https://substackcdn.com/image/fetch/$s_!z60K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb227f809-7975-4773-8b02-695218865ce9_964x494.jpeg)](https://substackcdn.com/image/fetch/$s_!z60K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb227f809-7975-4773-8b02-695218865ce9_964x494.jpeg)

The FAQ repository structure. Content is organized by course, then by section such as `general` or `module-1`, with a `_metadata.yaml` file for course-level configuration and Jinja2 templates in \_layouts for generating the site pages.

Each FAQ entry became its own Markdown file with frontmatter metadata. That metadata includes things like the FAQ ID, the question text, and the sort order, while the file body contains the answer itself.

[![Individual FAQ file format](https://substackcdn.com/image/fetch/$s_!yPCp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F152afec2-676e-490e-92e0-1bfb57e0800b_746x450.jpeg)](https://substackcdn.com/image/fetch/$s_!yPCp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F152afec2-676e-490e-92e0-1bfb57e0800b_746x450.jpeg)

An individual FAQ entry stored as a Markdown file with frontmatter metadata, including the entry ID, question text, and sort order, followed by the answer content.

This structure made the FAQ much easier to maintain. Questions could now be reviewed, updated, moved, or reordered independently. It also made the content much more suitable for version control, automated processing, and static site generation.

> You can find the full cleanup notebook [here](https://github.com/DataTalksClub/faq/blob/main/notebooks/process-questions.ipynb).

### 4) Building the Website

Once the content was in structured Markdown, the next step was turning it into a website.

The obvious choice for a [GitHub-hosted site](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) was [Jekyll](https://jekyllrb.com/), so I tried that first. It broke almost immediately.

The Data Engineering Zoomcamp includes an [Analytics Engineering module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/04-analytics-engineering) that uses dbt, and dbt models are written in [Jinja](https://jinja.palletsprojects.com/en/stable/). That becomes a problem inside Jekyll, because Jekyll uses [Liquid](https://github.com/shopify/liquid) as its own template engine and tries to interpret the same `{{ ... }}`, double-curly-brace syntax.

For example, a dbt snippet like this caused Jekyll to treat `{{ ref(’stg_trips’) }}` as a template expression and fail:

```
select *

from {{ ref(’stg_trips’) }}

where date >= ‘{{ var(”start_date”) }}’
```

I spent an evening trying different escaping tricks, but I couldn’t get it to handle these cases reliably.

So instead of fighting Jekyll, I wrote a custom static site generator.

That sounds heavier than it really was. By then, coding assistants already existed, so I used GitHub Copilot to help write the first version, and then adjusted it for the structure of the FAQ repository.

The generator is a Python script that reads the Markdown files from \_questions, parses their YAML frontmatter, converts the Markdown into HTML, and renders the final pages with Jinja2 templates.

[![Image 15](https://substackcdn.com/image/fetch/$s_!TbAg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa82cf3c4-3af6-4a33-b6d6-731e4e4d41e5_2048x779.png)](https://substackcdn.com/image/fetch/$s_!TbAg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa82cf3c4-3af6-4a33-b6d6-731e4e4d41e5_2048x779.png)

The generator also handles some project-specific details. It copies CSS assets and images into the output directory, renders one page per course plus an index page, and passes metadata such as course names, section structure, and generation time into the templates.

[![Image 16](https://substackcdn.com/image/fetch/$s_!svd-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbce35b16-cc31-4099-b05c-99d760ad3b45_1758x800.png)](https://substackcdn.com/image/fetch/$s_!svd-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbce35b16-cc31-4099-b05c-99d760ad3b45_1758x800.png)

This gave me a setup that matched the FAQ structure much better:

* Markdown files as the source of truth
* frontmatter for metadata such as question ID and sort order
* Jinja2 templates in `_layouts`
* static HTML pages generated into `_site`

> You can find the generator code [here](https://github.com/DataTalksClub/faq/blob/main/website/generate_website.py).

The downside is that the generator is specific to this project. It’s not a general-purpose tool that I can easily reuse elsewhere, and I still have to maintain it myself. But the scope is narrow, so in practice, that has been manageable.

This approach also works well with GitHub Pages as it exists today. GitHub Pages no longer has to be a Jekyll-only workflow. As long as GitHub Actions produces static HTML in the right place, a custom generator works fine. A few years ago, that would have been much less practical.

### JSON Export

One useful side effect of writing my own generator is that I could make it export JSON too, not just HTML. That became important later, because the FAQ was no longer only a website for humans to read. It also became something other tools could consume programmatically.

The generator produces a `courses.json` index file that lists all available courses, and a separate JSON file for each course. Each FAQ entry includes the same core fields used in the site itself:

* `id`
* `course`
* `section`
* `question`
* `answer`

This made the FAQ much easier to reuse. Instead of treating the website as the only interface, I could expose the same content as a structured dataset that other tools could index directly.

For example, you can fetch the JSON files and load them into minsearch in just a few lines:

```
import requests
from minsearch import Index

base_faq_url = ‘https://datatalks.club/faq’
courses_index_url = f’{base_faq_url}/json/courses.json’
courses_index = requests.get(courses_index_url).json()

documents = []

for course in courses_index:
   course_url = f”{base_faq_url}/{course[’path’]}”
   documents.extend(requests.get(course_url).json())

index = Index(
   text_fields=[’section’, ‘question’, ‘answer’],
   keyword_fields=[’course’]
)
index.fit(documents)
```

That was useful for more than convenience. By exporting JSON, the FAQ stayed close to its internal structure as a collection of records that could be indexed, searched, and reused in other systems.

[![Generated FAQ website](https://substackcdn.com/image/fetch/$s_!12AZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2150d2e0-6e0b-45c1-bf5d-b0c0882d361a_1280x756.jpeg)](https://substackcdn.com/image/fetch/$s_!12AZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2150d2e0-6e0b-45c1-bf5d-b0c0882d361a_1280x756.jpeg)

The [generated FAQ website for LLM Zoomcamp](http://datatalks.club/faq/llm-zoomcamp.html), with section navigation at the top and individual FAQ entries rendered below.

At that point, the FAQ had become much more robust than the original Google Docs version. It had proper structure, lived in Git, rendered as a static website, and could also be consumed programmatically.

## The FAQ Automation Bot

Moving to a website solved the moderation problem, but introduced a new problem: while reading the FAQ became better, contributing to it became much harder. With Google Docs, anyone could open the file and start typing. But contributing to a GitHub repo means you need to fork, edit markdown, open a pull request – that creates a lot of friction for a student who just want to add a contribution.

I wanted to keep the ease of contribution we had with Google Docs while still using the repository as the source of truth. That is how the [FAQ Automation Bot](https://github.com/DataTalksClub/faq/blob/main/faq_automation/rag_agent.py) came to be.

The idea behind the bot is like that: a student opens a GitHub issue with the `faq-proposal` label and fills in three things:

* course
* question
* answer

From there, the automation takes over. GitHub Actions triggers the FAQ automation workflow based on the FAQ Automation Bot:

* It loads the existing FAQ entries for that course
* It searches for similar entries in the current FAQ
* It sends the proposal, the retrieved results, and the course section metadata to the LLM
* the LLM returns a structured decision
* Based on that decision, the workflow either creates a new FAQ file, updates an existing one, or closes the issue as a duplicate
* If a file change is needed, the bot opens a pull request
* A human reviews and merges it

[![Image 18](https://substackcdn.com/image/fetch/$s_!jOHN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67529a21-78ee-4c59-b704-5e1bfb8ea650_1296x1442.png)](https://substackcdn.com/image/fetch/$s_!jOHN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67529a21-78ee-4c59-b704-5e1bfb8ea650_1296x1442.png)

So the student interacts with a simple issue form, while the system handles the repetitive repository work in the background.

### How the Agent Works

The core behind the FAQ Automation Bot is RAG agent.

Here’s how it works:

It starts by loading the current FAQ entries and course metadata from the repository.

Then it builds a search index with `minsearch`, using `section`, `question`, and `answer` as text fields, and course and `section_id` as keyword fields.

When a new proposal comes in, the agent does not send it to the model in isolation. It first searches the existing FAQ for similar entries, keeps the relevant matches, and then builds a prompt from three pieces:

* The new proposal
* The top matching FAQ entries
* The section metadata for that course

That prompt is then sent to the model together with instructions about how the repository should be maintained.

[![Image 19](https://substackcdn.com/image/fetch/$s_!fvhe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F963591a5-21ac-4dfb-be48-b711d3178aec_2036x1210.png)](https://substackcdn.com/image/fetch/$s_!fvhe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F963591a5-21ac-4dfb-be48-b711d3178aec_2036x1210.png)

### The Decision Model

The model returns a structured Pydantic object, `FAQDecision`, rather than free-form text. That object includes:

* `action`: `NEW, UPDATE`, or `DUPLICATE`
* `rationale`: short explanation of the decision
* `document_id`: the FAQ entry to act on
* `section_id`: where the content belongs
* `section_rationale`: why that section was chosen
* `order`: where the entry should appear inside the section
* `question`: the final normalized question text
* `proposed_content`: the answer text for a new or updated entry
* `filename_slug`: filename for new entries
* `warnings`: optional notes about possible problems

> You can find the code for the RAG agent [here](https://github.com/DataTalksClub/faq/blob/main/faq_automation/rag_agent.py).

### Broader View on RAG

What I find interesting here is that retrieval is doing more than helping answer questions. It is also helping maintain the knowledge base itself.

The same retrieval step can be used to:

* Find the most relevant existing entries
* Detect when a proposal is already covered
* Merge new information into an older answer
* Place content into the right section
* Keep the FAQ structure consistent as it grows

The agent uses a lightweight model by default, gpt-5-nano, so this kind of triage stays cheap enough to run routinely. But the system is still human-in-the-loop. Nothing gets merged automatically without review.

### Building the Bot

I wrote the first version as a notebook. It was enough to prove that the decision logic worked, but it was still a prototype, not something you would want to run on every GitHub issue.

The project became much more practical during Hacktoberfest, when [Fred Pearce](https://github.com/frederick-douglas-pearce) picked it up and built the [GitHub Actions orchestration around it](https://github.com/DataTalksClub/faq/blob/main/faq_automation/github_actions.py). That is what turned the idea into a usable workflow for the community: issue events could trigger the automation, and the result could be turned into a pull request automatically.

[![Image 20](https://substackcdn.com/image/fetch/$s_!u2Yt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7f74fe4-5800-4d6d-a857-f24a941ee91e_2048x1329.png)](https://substackcdn.com/image/fetch/$s_!u2Yt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7f74fe4-5800-4d6d-a857-f24a941ee91e_2048x1329.png)

The repository got a proper automation layer around the agent:

* a GitHub Actions workflow to react to FAQ proposal issues
* a structured GitHub issue template for course, question, and answer
* Python helpers for passing outputs between workflow steps
* a CLI for running the automation logic
* tests and documentation so the system was easier to maintain

So from the student’s side, the process stayed simple: fill out the FAQ proposal form with the course, question, and answer. From the repository side, that issue now becomes the input to an automated workflow that retrieves similar FAQ entries, runs the triage agent, and either prepares a pull request or closes the issue with feedback.

> The contribution guides are in the [repository’s CONTRIBUTING.md](https://github.com/DataTalksClub/faq/blob/main/CONTRIBUTING.md) file.

[Leave a comment](https://aishippingblog.com/p/from-google-docs-to-an-automated/comments)

## Reviewing Pull Requests with Claude Code

The bot makes mistakes, which is not very surprising. A typical one is putting a question about Kestra, which belongs in the workflow orchestration module, into the general section. Another is merging a proposal into the wrong FAQ because the retrieved match looked similar on the surface, but was actually about a different problem.

[![FAQ bot suggesting category change](https://substackcdn.com/image/fetch/$s_!uKHy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b12fe0e-b3ec-4b1b-8967-563a28f7bcc1_1280x758.jpeg)](https://substackcdn.com/image/fetch/$s_!uKHy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b12fe0e-b3ec-4b1b-8967-563a28f7bcc1_1280x758.jpeg)

The FAQ bot sometimes misclassifies entries. In this case, the fix is to move the question from `general` to `module-2`, where workflow orchestration topics belong.

Fixing these mistakes manually was tedious. For each pull request, I had to check out the branch, edit the Markdown, push the change, and repeat the process for the next one. That is a lot of overhead for small corrections. I made some fixes here and there, but it wasn’t sustainable for managing the queue.

So I started batching them instead. I let the pull requests pile up for a bit, then open a Claude Code session and go through them one by one.

The workflow looks like this:

* List the open pull requests with gh pr list
* Pick the next one and show Claude what changed
* Explain the correction, for example: move this to module-2 or merge it into the existing FAQ about X
* Claude checks out the branch, makes the edit, and pushes it
* I review the result, merge the pull request, delete the branch, and move on

What I like about this workflow is that it keeps the review process focused. I only look at one pull request at a time, instead of trying to keep the whole queue in my head. And once Claude has seen a few similar corrections in the same session, it often starts suggesting the same kind of fix on later pull requests without needing as much guidance.

### Why Keep a Human in the Loop

I could try to encode more of these corrections directly into the bot, but that would add complexity to the GitHub Actions workflow and make the agent logic more elaborate.

Using Claude Code for review is a simpler trade-off:

* Nothing gets merged without human review
* Fixing mistakes is faster than redesigning the automation around every edge case
* I can clean up other repository issues at the same time, such as duplicates or stale entries
* The bot itself stays cheap to run, because it uses a smaller model for triage and I only use a stronger model during review

### Feeding the Mistakes Back

The next step is to use those review sessions as training material for the workflow itself.

Each correction is a small example of where the bot went wrong: the wrong section, the wrong merge target, a duplicate not recognized, and so on. Those cases can be fed back into the agent prompt as examples, so the next round of decisions is a bit better.

That is the feedback loop I want from this system. Review catches what the bot missed, and the bot gradually improves from the patterns in those corrections.

## Starting Simple

What I like about this system is that each stage solved a real constraint from the previous one.

* Google Docs made contributions easy
* The Slack bot made the content usable at scale
* The website made the content maintainable
* The automation bot made contributions practical again
* Human review with Claude Code kept the whole thing under control

I also like that this system stayed fairly pragmatic throughout. I didn’t start with a huge architecture. Most parts appeared because the previous version was no longer good enough.

## What I’ve Been Working On Recently

### 1. First AI Shipping Labs Workshop

[![User Uploaded Image](https://substackcdn.com/image/fetch/$s_!oucK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F415f74d3-d6a3-47c6-ad5b-ca756323e379_1600x832.png)](https://substackcdn.com/image/fetch/$s_!oucK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F415f74d3-d6a3-47c6-ad5b-ca756323e379_1600x832.png)

I ran the first workshop inside AI Shipping Labs: “[Deploy Your AI Agent Project to Production with FastAPI and a Vector DB”](https://luma.com/j1zzd47e).

In the session, we took an existing [Telegram bot agent](https://alexeyondata.substack.com/p/telegram-assistant), built a frontend for it, packaged it as a Docker image, and deployed it on Render.

The format was more freestyle than usual. I prepared some parts in advance, but a lot of it was improvised because I wanted it to feel closer to real project work.

It ran for about two hours, longer than usual, but the feedback was good. Based on that, I want to do [more sessions like this in AI Shipping Labs](https://luma.com/home).

The recording and code are already available in the [AI Shipping Labs](https://aishippinglabs.com/?utm_source=alexey_on_data&utm_medium=email&utm_campaign=ai_shipping_labs&utm_content=2026_04_24) Slack community, and I’m now turning the workshop into a step-by-step written tutorial for members.

If you’d like access to the materials, you can [join AI Shipping Labs](https://aishippinglabs.com/#tiers?utm_source=alexey_on_data&utm_medium=email&utm_campaign=ai_shipping_labs&utm_content=2026_04_24). Slack is included in the Main and Premium tiers.

[Join AI Shipping Labs](https://aishippinglabs.com/#tiers?utm_source=alexey_on_data&utm_medium=email&utm_campaign=ai_shipping_labs&utm_content=2026_04_24)

### 2. PyConDE in Darmstadt

[![Alexey and others at PyConDE Darmstadt 2026](https://substackcdn.com/image/fetch/$s_!Khls!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F730ba2bc-8769-45a7-97c5-fa6c16520626_1920x1280.jpeg)](https://substackcdn.com/image/fetch/$s_!Khls!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F730ba2bc-8769-45a7-97c5-fa6c16520626_1920x1280.jpeg)

I was in Darmstadt for [PyConDE](https://2026.pycon.de/), the Python and PyData conference, where I recorded a series of interviews.

I spoke with community leaders, educators, developer advocates, and Python tooling builders. A few themes kept coming up across the conversations: how Python is changing in the age of AI, how conferences help sustain technical communities, and why human connection, mentorship, and strong fundamentals still matter.

Among the people I spoke with were Jessica Greene, Cheuk Ting Ho, Sebastian Raschka, Kyle Into, Valerio Maggio, Tereza Iofciu, and Irina Saribekova.

Listen to the full recording here:

## Tools

![Image 24](https://substackcdn.com/image/fetch/$s_!an7h!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27279798-94be-4731-8e78-fd30b0de2622_903x702.png)![Image 25](https://substackcdn.com/image/fetch/$s_!G9n9!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8dc3b095-23c5-4ec0-8c9b-af503b0aebc4_947x696.png)![Image 26](https://substackcdn.com/image/fetch/$s_!o96h!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b7d86c1-c30d-4494-8bef-4d14977a8d18_864x764.png)

Three screens from DeathByClawd’s “SaaSpocalypse Survival Scanner” show DataTalks.Club rated 12/100 SAFE, with the conclusion that community is a stronger moat than product surface area.

* [DeathByClawd](https://deathbyclawd.com/) is a joke tool, but it makes a real point. It tries to answer a simple question: if Claude got a bit more packaging, would this product still matter? Running it on DataTalks.Club produced a 12/100 SAFE score and a surprisingly accurate roast. The result is funny, but the underlying point is serious: communities are much harder to replace than interfaces.
* [Claude Memory Compiler](https://github.com/coleam00/claude-memory-compiler) is a practical implementation of Andrej Karpathy’s idea of an LLM knowledge base for personal work. It takes Claude Code conversations, extracts the useful parts, and organizes them into a searchable set of Markdown notes. What makes it interesting is that retrieval does not rely on vector search or a full RAG stack. Instead, it uses a structured index, based on the idea that at a personal scale, clean organization can work better than heavier infrastructure.

## Resource

[![Image 27](https://substackcdn.com/image/fetch/$s_!PITp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66bcb43c-9a8a-4ddd-afb1-dcf49735fdce_1160x976.png)](https://substackcdn.com/image/fetch/$s_!PITp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66bcb43c-9a8a-4ddd-afb1-dcf49735fdce_1160x976.png)

[LennysData.com hackathon winners](https://www.linkedin.com/posts/lennyrachitsky_announcing-the-winners-of-the-lennysdatacom-share-7450274416166608896-ayJf) is a useful reference if you are looking for ideas for a personal project built on open content. The winning entries came from a hackathon based on [Lenny Rachitsky](https://open.substack.com/users/1849774-lenny-rachitsky?utm_source=mentions)’s podcast transcripts and [Lenny's Newsletter](https://open.substack.com/pub/lenny) archive, and included projects like Lenny’s Greatest Hits, Lenny’s Comics, and Lenny’s Dots of Wisdom. A good reminder that once content is available in a structured form, it can become raw material for many small products and experiments.

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
