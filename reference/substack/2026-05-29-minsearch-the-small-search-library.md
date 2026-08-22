---
title: "Minsearch: The Small Search Library Behind My RAG Workshops and Courses"
date: 2026-05-29
url: https://aishippingblog.com/p/minsearch-the-small-search-library
---

Two years ago, I was preparing the first run of [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp/tree/main), my free course on building LLM applications. That first run focused mostly on RAG. I was also running workshops on the same topics.

Search, or retrieval, is one of the most important parts of RAG. I needed a way to teach it without asking participants to install Docker or Elasticsearch.

So I built [minsearch](https://github.com/alexeygrigorev/minsearch): a small in-process Python search library. It started as the smallest thing I needed to teach retrieval in a notebook, then grew as the course examples changed.

In this post, I will share:

* Why was Elasticsearch too much for this setup
* How the first version worked
* How it became a PyPI package
* Why I added an appendable index and vector search
* How I used Claude to make it faster
* When minsearch is the right tool

[![Image 1](https://substackcdn.com/image/fetch/$s_!FgN7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F327e7b76-3c70-4765-97a6-144b8d903ff2_1764x1080.png)](https://substackcdn.com/image/fetch/$s_!FgN7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F327e7b76-3c70-4765-97a6-144b8d903ff2_1764x1080.png)

## Why Elasticsearch Was Too Much

In the first run of LLM Zoomcamp, I needed to show participants how to index a small dataset, submit a query, and retrieve relevant documents. Usually, it was a few thousand documents, sometimes fewer. Most of the examples were run in notebooks, sometimes on Google Colab, using open-source LLMs on a GPU. And working with notebooks was my main motivation for creating minsearch as a lightweight alternative to more complex search engines.

For a normal production system, I would probably reach for [Elasticsearch](https://github.com/elastic/elasticsearch). It is powerful, and I knew it well. But for a workshop notebook, it was too much. It requires a server, Docker, configuration, and operational details that weren’t the point of the lesson.

In the course or workshop setup, everything should run within a single notebook. I looked for a small Python library that could do a good-enough lexical search within the same Python process as the notebook, but I didn’t find anything that fit.

At that time, I had been doing text processing and search for quite some time, so building a small in-process search library myself wasn’t hard. Even back then, when coding agents weren’t as good as they are now, I could describe what I wanted to a chat assistant, get code back, and ask for a few fixes.

[![Image 2](https://substackcdn.com/image/fetch/$s_!kyt2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0604a422-a8d0-4562-8f65-05bf3a2be890_2048x904.png)](https://substackcdn.com/image/fetch/$s_!kyt2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0604a422-a8d0-4562-8f65-05bf3a2be890_2048x904.png)

The retrieval module from the first run of LLM Zoomcamp, built around minsearch.

## The First Version

The [first implementation](https://github.com/alexeygrigorev/minsearch/tree/62ddbe9bc4adbc38cfd14114a2128fdf3b8e0110) was a single Python file.

[![Image 3](https://substackcdn.com/image/fetch/$s_!_8HB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fc70f54-aa46-4a85-9206-80192452418e_1968x1100.png)](https://substackcdn.com/image/fetch/$s_!_8HB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fc70f54-aa46-4a85-9206-80192452418e_1968x1100.png)

It had one class, `Index`, and the search was just a bag-of-words with TF-IDF.

It worked like this:

1. Fit a TF-IDF vectorizer for each text field
2. Transform the query with the same vectorizers
3. Multiply the matrices to get document scores
4. Add the scores from all text fields
5. Sort the documents by score

In my teaching, I used examples with FAQs from my free courses, the Zoomcamps. A typical document had a question, an answer, a section, a course name, and some metadata.

This already required a little more than a plain text search. Matches in the question field should count more than matches in the answer field. Sometimes I wanted results only from one course. So the first version also had field boosting and keyword filtering.

That made minsearch useful for teaching. The implementation was small enough that learners could understand it, yet it still included the pieces I needed for real-world course examples: text search, filters, and boosts.

The basic usage looked like this:

```
from minsearch import Index
index = Index(
    text_fields=[”question”, “answer”],
    keyword_fields=[”course”]
)
index.fit(docs)
results = index.search(”can I join the course?”)
```

I also shared how I built it in the workshop titled “[Build Your Own Search Engine](https://github.com/alexeygrigorev/build-your-own-search-engine).” The first version of that workshop came out around two years ago, originally as a DataTalks.Club talk. But I later updated it to include the newer library versions and published it as a [structured tutorial](https://aishippinglabs.com/workshops/2026-05-14-build-your-own-search-engine) in the [AI Shipping Labs workshop library](https://aishippinglabs.com/workshops/).

If you want to understand how minsearch works internally, that workshop is the best place to look.

## From a File to a Package

At first, people downloaded the single Python file, and that worked until I needed to ship changes.

Every time I fixed something or added a feature, course participants had to download the file again. In LLM Zoomcamp, we used to do that with `wget`. It was fine for one notebook, but not for a library I kept changing.

So I packaged it properly, [published it on PyPI](https://pypi.org/project/minsearch/), and now people can install it with `uv` or `pip`:

```
uv add minsearch
```

The first published version was [0.0.1](https://pypi.org/project/minsearch/0.0.1/). At the time of writing, the current version is `0.1.0`.

[![Image 4](https://substackcdn.com/image/fetch/$s_!UGnw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43434ae6-4904-4a30-baa6-eb67c8584deb_2048x1201.png)](https://substackcdn.com/image/fetch/$s_!UGnw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43434ae6-4904-4a30-baa6-eb67c8584deb_2048x1201.png)

[Share](https://aishippingblog.com/p/minsearch-the-small-search-library?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## Where I Use It

I now use minsearch across my courses and workshops:

* [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp)
* [AI Hero](https://aishippinglabs.com/courses/aihero)
* [AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents)

I also use it outside teaching, in personal and DataTalks.Club projects. One example is the [DataTalks.Club FAQ system](https://github.com/DataTalksClub/faq), where the automation reads GitHub issues and creates FAQ entries. Before adding a new question, it uses minsearch to check whether a similar question already exists.

I told you about it in [From Google Docs to an Automated FAQ System for DataTalks.Club Courses](https://alexeyondata.substack.com/p/from-google-docs-to-an-automated):

[From Google Docs to an Automated FAQ System for DataTalks.Club Courses](https://alexeyondata.substack.com/p/from-google-docs-to-an-automated)

The automation loads the FAQ, builds the index, searches it, and continues in one Python process.

That is still the main reason I use minsearch, but the library had to grow once the course examples changed.

## Implementing Inverted Index and Vector Search

The appendable index came later, when I started working on the second run of LLM Zoomcamp and added the module covering agents.

### Implementing Inverted Index

I wanted to show that agents can do more than search existing documents, like adding data back to the index and modifying it. The original index didn’t support that well. It was built for the simple case: create the index, search it, and throw it away when the notebook ends.

To allow the agent to modify the index, I implemented a new index type: `AppendableIndex`. It’s an inverted index that keeps the same `fit` and `search` methods, but it also lets you append documents one at a time.

[![Image 5](https://substackcdn.com/image/fetch/$s_!J7b_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd9be2f0-3ed7-4326-b63f-0c99f066c147_2038x906.png)](https://substackcdn.com/image/fetch/$s_!J7b_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd9be2f0-3ed7-4326-b63f-0c99f066c147_2038x906.png)

### Adding Vector Search

Vector search came later for a similar reason. I had already taught it in Build Your Own Search Engine, but it wasn’t part of the library at first. Eventually, I added it too.

[![Image 6](https://substackcdn.com/image/fetch/$s_!31PQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e88c4a0-9bd3-4538-9d6d-a8b852bbc0b9_2002x992.png)](https://substackcdn.com/image/fetch/$s_!31PQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e88c4a0-9bd3-4538-9d6d-a8b852bbc0b9_2002x992.png)

`VectorSearch` works on pre-computed embeddings and ranks results by cosine similarity. It isn’t trying to replace a full vector database. It is a simple tool for local examples, and my primary use case is to explain search concepts during my courses and workshops.

### Three Index Types and Highlighting

Today the library has three main index types:

* `Index`: The basic TF-IDF index using scikit-learn
* `AppendableIndex`: An inverted index implementation that lets you add documents later
* `VectorSearch`: Cosine similarity search over pre-computed vectors

The same filter model works across all three. You can filter by exact keyword matches, numeric ranges, and date ranges. Keyword fields are optional now, because not every search example needs filtering.

There is also highlighting now. It extracts snippets from search results and marks where the query terms matched. The motivation was that we started to have more and more agents, and I realized that for agents, it is better to mirror how humans see.

The way humans search is that we look at the snippet, for example, in a Google search, and based on what we see, we decide whether we want to check an article. For agents, I think it works better if they can first see highlighted snippets; then, based on those snippets, they can decide whether to check the entire page for details.

I don’t see minsearch as a big infrastructure project. It grew because the examples kept needing more practical features.

## Making minsearch Faster with Claude Code

I used the appendable index more and eventually noticed a problem: it was much slower than the simple index.

At first, I just ignored it. The appendable index was doing more work, and the datasets were small. But at some point, it became too slow even for my use, so I decided to benchmark it.

The first benchmark showed that the appendable index was about 14 times slower to index and 27 times slower to search.

I asked Claude to look at it, and it found out the reason for this inefficiency. The appendable index recomputed tokens and scores during every search, while the simple index relied on scikit-learn’s optimized batch operations.

This was one of the first times I used an AI assistant to benchmark and optimize something like this.

I gave Claude a clear loop:

1. Benchmark against Simple Wikipedia and save a baseline
2. Make changes to the code
3. Check that results still match the baseline
4. Compare the speed

Then I let it run and checked in about once an hour while I worked on course materials. After a few rounds, search in the optimized appendable index was 20 to 76 times faster than the scikit-learn-based index. The gap grew on larger datasets.

The full benchmark writeup is here: [benchmark/BENCHMARK\_WRITEUP.md](https://github.com/alexeygrigorev/minsearch/blob/main/benchmark/BENCHMARK_WRITEUP.md).

## When Minsearch Is the Right Tool

Minsearch is a good fit when:

* You have a small or medium dataset
* You need to search in a notebook, course, prototype, or small automation
* Everything can live in one Python process
* You are indexing up to a few thousand documents

The sweet spot is up to 10,000 documents. At that size, indexing is fast, search is convenient, and you get a useful retrieval layer without setting up extra infrastructure.

It works best when there is enough plain text to search over. That is the case for course FAQs, workshop datasets, documentation pages, and small internal collections.

Beyond that, minsearch is no longer the right tool.

If you have a larger local dataset but still want something lightweight, use [SQLiteSearch](https://github.com/alexeygrigorev/sqlitesearch) instead. I built it for exactly that case, and wrote about it in [How I Built SQLiteSearch](https://alexeyondata.substack.com/p/how-i-built-sqlitesearch-a-lightweight).

[How I Built SQLiteSearch: A Lightweight Python Library for Local Text and Vector Search](https://alexeyondata.substack.com/p/how-i-built-sqlitesearch-a-lightweight)

For bigger systems, use a real search engine or vector database.

## What I’ve Been Working On Recently

### 1. Building pocketshell and testing agent teams

`pocketshell`, the Android app that packages my phone-based development setup, reached a point where I can actually use it while continuing to build it.

It is the next step after the workflow I described in [Working from a Phone](https://alexeyondata.substack.com/p/the-system-i-built-to-ship-code-from). Last week, some parts were still being set up. Now the goal is to put everything into one box, so I can do the development work I need from my phone.

I also ran an experiment with it: coordinating three coding agents, Codex, Claude Code, and OpenCode, as three team managers working on the same repo. The agents had to find each other, divide the work, and collaborate.

[The System I Built to Ship Code From a Phone](https://alexeyondata.substack.com/p/the-system-i-built-to-ship-code-from)

### 2. Scraping more AI engineering jobs

[![Job collection completion log for 2026-05-29: 2,751 scraped, 919 new deduped, 919 HTML downloaded, 919 raw and structured YAML, 0 missing structured IDs](https://substackcdn.com/image/fetch/$s_!r05X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff0a1c88-a961-4bc2-8aef-93be96b83ce5_1080x726.jpeg)](https://substackcdn.com/image/fetch/$s_!r05X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff0a1c88-a961-4bc2-8aef-93be96b83ce5_1080x726.jpeg)

Job collection completion log for 2026-05-29: 2,751 scraped, 919 new deduped, 919 HTML downloaded, 919 raw and structured YAML, 0 missing structured IDs

I ran another scrape for the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide).

The goal is to keep doing this throughout the year, then analyze how the market changes over time. I want to see which requirements appear more often, which tools become more common, and how AI engineering roles evolve.

This run scraped 2,751 listings and added 919 new unique jobs after deduplication. For all 919 new jobs, the pipeline downloaded the HTML and generated both raw and structured YAML.

### 3. Building AI Shipping Labs onboarding

I started building onboarding directly into the [AI Shipping Labs](https://aishippinglabs.com/) platform.

So far, we have manually onboarded around 40, maybe even 50, people. We went through their goals, background, current skill level, and plans by hand.

By now, we have enough material to start making this process easier. Not fully automated, but more structured.

### 4. Running the O’Reilly guardrails workshop

I ran the O’Reilly workshop this week: [Building an Agent with Guardrails](https://aishippinglabs.com/workshops/2026-05-26-agent-with-guardrails).

The workshop focused on how to make an agent less fragile: where to put checks, how to constrain behavior, and how to think about guardrails as part of the system rather than as something added at the end.

### 5. Running LLM Zoomcamp workshops

I also ran two LLM Zoomcamp workshops this week.

The first one was about [agents](https://www.youtube.com/watch?v=RAqLWJsLZb4&pp=0gcJCR4LAYcqIYzv). The second one was about [evaluations](https://www.youtube.com/watch?v=WUGtDveIe7A). Both are part of the work to update the LLM Zoomcamp material with the topics I now use more often in practice.

## Tools

[![Image 8](https://substackcdn.com/image/fetch/$s_!qfP8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fbc10a7-c08f-4841-b8eb-79ad15191461_1752x1094.png)](https://substackcdn.com/image/fetch/$s_!qfP8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fbc10a7-c08f-4841-b8eb-79ad15191461_1752x1094.png)

* [Webwright](https://github.com/microsoft/webwright) is a lightweight, terminal-based browser agent framework from Microsoft that gives an LLM a CLI to spawn browser sessions and complete web tasks. Instead of the step-by-step Playwright MCP loop, it has the model write a re-runnable Python Playwright script end-to-end, so the agent’s browsing history becomes a single code file you can rerun, adapt, and debug. It’s a CLI alternative to Playwright MCP for browser testing and automation, built on just httpx, pydantic, playwright, and typer, with OpenAI, Anthropic, and OpenRouter backends.
* [gstack](https://github.com/garrytan/gstack) is a collection of opinionated Claude Code slash commands that transform a single AI assistant into a team of specialists, such as a CEO, an engineering manager, a release engineer, and a QA engineer. Developed by Y Combinator president Garry Tan, it offers commands like `/plan-ceo-review` for product thinking, `/review` for thorough code review, /ship for one-command PR creation, and `/browse` and `/qa` for automated browser-based testing with screenshots. It serves as a helpful reference for structuring Claude Code custom commands for multi-role development workflows.

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
