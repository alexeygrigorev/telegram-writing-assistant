---
title: "Minsearch: Simple Search for Small Datasets"
created: 2026-01-23
updated: 2026-05-28
tags: [search, python, library, minsearch, elasticsearch-alternative]
status: draft
---

# Minsearch: Simple Search for Small Datasets

Minsearch is a lightweight search library for small to medium datasets, for when you don't need the complexity of Elasticsearch.

If you want to see how it works from the inside, I turned it into a workshop: Build Your Own Search Engine [aishippinglabs.com/workshops/2026-05-14-build-your-own-search-engine](https://aishippinglabs.com/workshops/2026-05-14-build-your-own-search-engine) [^build]. The first version came out two years ago and was originally a talk at DataTalks.Club. I updated it with newer versions of the libraries, but it is essentially the same workshop as before, now split into units. If you are curious about how minsearch is built, that is the place to look[^build].

## How It Started

The library came out of the very first run of LLM Zoomcamp, two years ago in the summer. The course covered RAG, and search - retrieval - is one of the most important parts of RAG. So I wanted to explain search[^origin1].

When I started explaining RAG, I realized that if I wanted to teach it with a simple example, I didn't have many options. I needed a search engine, and the one I knew well at the time was Elasticsearch. So I was explaining RAG on top of Elasticsearch. The problem was the setup: Elasticsearch plus Colab plus Docker, "let's take this dataset and quickly build a RAG". I couldn't find anything suitable for that. I went looking for something ready-made, but found nothing[^origin1].

I have been doing text processing and search for a long time, so building a small in-process search library on my own was not hard. This was a while ago, back when coding agents were not as good as they are now. Even so, I was already using a chat assistant to help[^origin1].

## Building the First Version

I already had the picture in my head, and the implementation itself is not complicated. You take a TF-IDF vectorizer, apply it to all the documents you have, then apply the same vectorizer to the query, multiply the matrices, sort the results, and that's it[^origin2].

I described exactly what I wanted to a chat assistant - I think it was ChatGPT, maybe Claude, I don't remember which. I explained everything I wanted to build and got code back. The code didn't please me right away, so I asked for a few fixes, copied it over, and that became the first version of the library. At first it was just a single Python file[^origin2].

## Why Colab Made It Necessary

Then I thought: this is a very useful thing, and it is especially important for RAG, which was exactly what the course was teaching at the time. So why not turn it into a workshop, as preparation for the course? It would be interesting for a lot of people[^origin2].

The reason it mattered that this run on Colab is that I had a module about open source LLMs, where the models had to be open source only. Running those requires a GPU, and for that you need Google Colab. On Colab you simply cannot run Elasticsearch: there is no way to run Docker there, and running Elasticsearch without Docker is very hard, especially on Colab. That is the main reason I wanted to build minsearch[^origin2].

I used it on the workshops first, and then on the course itself. My original idea had been to use Elasticsearch, but I realized minsearch was a much better fit, much simpler. You don't need to prepare any complex infrastructure for it, no Docker, nothing. In the beginning people just downloaded the single file[^origin2].

## From a Single File to a PyPI Package

Over time I realized I needed to make changes to the library. For example, I added vector search, which I had been doing on one of the workshops. I needed a way to ship these changes so that everyone taking the course could pick them up easily[^evolution1].

That is when it became convenient to publish it properly. I looked into how to package and publish a library on PyPI. I already had some experience releasing Python libraries, so I refreshed my memory, set it up, and published the first version, 0.0.1. That turned out to be very convenient, and I gradually started adding new functionality[^evolution1].

## How the Library Evolved

Here is roughly how minsearch developed over time, based on its commit history[^commits]:

- 2024-05 (0.0.1): Initial release. A single-file library implementing minimalistic TF-IDF and cosine-similarity text search, with keyword filtering and field boosting.
- 2024-09 (0.0.2): Made pip-installable with proper packaging.
- 2025-05/06 (0.0.3): Added the appendable index, an incrementally updatable index where documents can be added after creation.
- 2025-07 (0.0.4): Added vector search, plus CI and a move to uv.
- 2025-09 (0.0.5): Made keyword fields optional across all index classes.
- 2025-10 (0.0.6 / 0.0.7): Bug fixes around None handling.
- 2025-11: Added append support to vector search for incremental vector indexing; fixed TF-IDF normalization in the appendable index to match scikit-learn.
- 2026-02 (0.0.8): Added numeric and date range filters, and refactored filtering into its own module.
- 2026-02 (0.0.9): Major appendable-index performance optimizations, a highlighter for search results, and a tokenizer module with stemming support.
- 2026-02 (0.0.10): Added save and load methods to all index classes for persistence.
- 2026-05 (0.0.11): Fixed appendable-index scoring.
- 2026-05 (0.1.0): Switched to CI-based publishing on tag push. This is the current version.

The performance work behind 0.0.9 has its own story in [Minsearch Benchmarking and Optimization](minsearch-benchmarking-optimization.md).

## Where It Fits

Minsearch is designed for situations where:

- You have a small to medium-sized dataset
- You need search functionality
- Everything lives within a single process
- You don't need heavy infrastructure like Elasticsearch[^usecases]

The most convenient use is indexing small sites or datasets up to a few thousand documents, somewhere in the 5,000 to 10,000 range. A few thousand documents index extremely fast, and the search is fast too. This works best when you don't need vector search, because vector search is more involved: computing the embeddings takes time. When you have enough plain text to search over, minsearch is the most convenient option[^scale].

Beyond around 10,000 documents it stops being the right tool, and at that point it is better to use SQLiteSearch instead[^scale].

## Where It's Used

I use this library on practically all of my workshops. You can find the list of workshops at [aishippinglabs.com/workshops](https://aishippinglabs.com/workshops) - not every one of them uses minsearch, but many do[^workshops]. It is also used across all of my courses: LLM Zoomcamp, AI Hero, and AI Engineering Buildcamp[^workshops].

Beyond teaching, I use it in many applied projects. One example is the FAQ assistant for DataTalks.Club at [github.com/DataTalksClub/faq](https://github.com/DataTalksClub/faq) [^workshops]. Its automation module reads GitHub issues and creates FAQ entries, and minsearch is used there to check whether a question already exists before adding it. I wrote about that system on Substack: [From Google Docs to an Automated FAQ System for DataTalks.Club Courses](https://alexeyondata.substack.com/p/from-google-docs-to-an-automated) [^workshops].

I also use it for a lot of personal projects. It is very convenient precisely because you don't have to drag along anything heavy: for simple projects you can index the data very quickly, with no complex processing, as long as everything lives in a single process[^applied].

## Sources

[^build]: [20260528_122208_AlexeyDTC_msg4329_transcript.txt](../../inbox/used/20260528_122208_AlexeyDTC_msg4329_transcript.txt), [20260528_122122_AlexeyDTC_msg4325.md](../../inbox/used/20260528_122122_AlexeyDTC_msg4325.md), [20260528_122137_AlexeyDTC_msg4327.md](../../inbox/used/20260528_122137_AlexeyDTC_msg4327.md), [20260528_122049_AlexeyDTC_msg4323_transcript.txt](../../inbox/used/20260528_122049_AlexeyDTC_msg4323_transcript.txt)
[^origin1]: [20260528_105720_AlexeyDTC_msg4308_transcript.txt](../../inbox/used/20260528_105720_AlexeyDTC_msg4308_transcript.txt)
[^origin2]: [20260528_110401_AlexeyDTC_msg4309_transcript.txt](../../inbox/used/20260528_110401_AlexeyDTC_msg4309_transcript.txt)
[^evolution1]: [20260528_110619_AlexeyDTC_msg4311_transcript.txt](../../inbox/used/20260528_110619_AlexeyDTC_msg4311_transcript.txt)
[^commits]: [20260528_110612_AlexeyDTC_msg4310.md](../../inbox/used/20260528_110612_AlexeyDTC_msg4310.md), [20260528_110626_AlexeyDTC_msg4312_transcript.txt](../../inbox/used/20260528_110626_AlexeyDTC_msg4312_transcript.txt), [github.com/alexeygrigorev/minsearch](https://github.com/alexeygrigorev/minsearch/commits/main/)
[^usecases]: [20260123_121456_valeriia_kuka_msg458_transcript.txt](../../inbox/used/20260123_121456_valeriia_kuka_msg458_transcript.txt)
[^scale]: [20260528_110735_AlexeyDTC_msg4313_transcript.txt](../../inbox/used/20260528_110735_AlexeyDTC_msg4313_transcript.txt)
[^workshops]: [20260528_122004_AlexeyDTC_msg4321_transcript.txt](../../inbox/used/20260528_122004_AlexeyDTC_msg4321_transcript.txt)
[^applied]: [20260528_122004_AlexeyDTC_msg4321_transcript.txt](../../inbox/used/20260528_122004_AlexeyDTC_msg4321_transcript.txt)
