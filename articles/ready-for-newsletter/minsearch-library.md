---
title: "Minsearch: Simple Search for Small Datasets"
created: 2026-01-23
updated: 2026-05-28
tags: [search, python, library, minsearch, elasticsearch-alternative]
status: draft
---

# Minsearch: Simple Search for Small Datasets

Minsearch is a lightweight search library for small to medium datasets, for when you don't need the complexity of Elasticsearch. The source is at [github.com/alexeygrigorev/minsearch](https://github.com/alexeygrigorev/minsearch).

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

## How It Started

The library came out before the first run of LLM Zoomcamp. When I was planning the course, I wanted it to focus mostly on RAG, and search - retrieval - is one of the most important parts of RAG. So I needed a simple search library I could use both for the course and for the workshops I was running alongside it to promote it[^origin1].

I knew Elasticsearch well at the time, so I started with that. But in parallel with the course I was running workshops on Google Colab, and this was even before the first run of the course itself. The reason the workshops needed Colab is that one module was about open source LLMs, where the models had to be open source only. Running those requires a GPU, and for that you need Colab. On Colab you simply cannot run Elasticsearch: there is no way to run Docker there, and running Elasticsearch without Docker is very hard, especially on Colab[^origin2].

So I needed a maximally lightweight search that would run right in Python, with no Docker. I went looking for something existing with similar functionality, but found nothing. I have been doing text processing and search for a long time, so building a small in-process search library myself was not hard - even back then, when coding agents were not as good as they are now[^origin1].

## Building the First Version

I already had the picture in my head, and the implementation itself is simple. The idea is a bag of words with TF-IDF: you take a TF-IDF vectorizer and apply it to all the documents you have, then apply the same vectorizer to the query, multiply the matrices, sort the results, and that's it[^origin2].

I described what I wanted to a chat assistant, got code back, asked for a few fixes, and that became the first version of the library. At first it was just a single Python file[^origin2].

Since the implementation is simple and there were no libraries like it, I thought it would be interesting to turn into a workshop, both as preparation for the course and as content people would enjoy. That is how the first version of the workshop appeared: Build Your Own Search Engine [aishippinglabs.com/workshops/2026-05-14-build-your-own-search-engine](https://aishippinglabs.com/workshops/2026-05-14-build-your-own-search-engine) [^build]. The first version came out two years ago and was originally a talk at DataTalks.Club. I updated it with newer versions of the libraries, but it is essentially the same workshop as before, now split into units. If you want to understand how minsearch works in more detail, that is the place to look[^build].

## From a Single File to a PyPI Package

At first people just downloaded the single file. Over time I realized I needed to ship changes to the library so that everyone taking the course could pick them up easily. Before this they had to wget the file, which was inconvenient, and pip install is much more convenient[^evolution1].

So I looked into how to package and publish a library on PyPI. I already had some experience releasing Python libraries, so I refreshed my memory, set it up, and published the first version, 0.0.1. That turned out to be very convenient, and I gradually started adding new functionality[^evolution1].

## The Appendable Index

The appendable index came about a year later, when I started working on the second run of the course, which brought in agents. We had started talking about agents on that second launch, and I wanted to show that agents can do more than just search - they can take other actions too. For that I needed a version of the index that you can add documents to after it has been created. That is how the appendable index appeared[^evolution2].

## Vector Search

Vector search came even later. I had been showing vector search on one of the workshops, and I thought it would be nice to make it part of minsearch, since minsearch had come out of that workshop in the first place[^evolution2].

## How the Library Evolved

Here is roughly how minsearch developed over time, based on its commit history[^commits]:

- 2024-05 (0.0.1): Initial release. A single-file library implementing minimalistic TF-IDF and cosine-similarity text search, with keyword filtering and field boosting.
- 2024-09 (0.0.2): Made pip-installable with proper packaging.
- 2025-05/06 (0.0.3): Added the appendable index, an incrementally updatable index where documents can be added after creation.
- 2025-07 (0.0.4): Added vector search, plus CI and a move to uv.
- 2025-09 (0.0.5): Made keyword fields optional across all index classes, because filtering by keyword was not always needed.
- 2025-10 (0.0.6 / 0.0.7): Bug fixes.
- 2025-11: Added append support to vector search for incremental vector indexing; fixed TF-IDF normalization in the appendable index to match scikit-learn.
- 2026-02 (0.0.8): Added numeric and date range filters, and refactored filtering into its own module.
- 2026-02 (0.0.9): Major appendable-index performance optimizations, a highlighter for search results, and a tokenizer module with stemming support.
- 2026-02 (0.0.10): Added save and load methods to all index classes for persistence.
- 2026-05 (0.0.11): Fixed appendable-index scoring.
- 2026-05 (0.1.0): Switched to CI-based publishing on tag push. This is the current version.

The performance work behind 0.0.9 has its own story in [Minsearch Benchmarking and Optimization](minsearch-benchmarking-optimization.md).

## Sources

[^build]: [20260528_122208_AlexeyDTC_msg4329_transcript.txt](../../inbox/used/20260528_122208_AlexeyDTC_msg4329_transcript.txt), [20260528_122122_AlexeyDTC_msg4325.md](../../inbox/used/20260528_122122_AlexeyDTC_msg4325.md), [20260528_122137_AlexeyDTC_msg4327.md](../../inbox/used/20260528_122137_AlexeyDTC_msg4327.md), [20260528_122049_AlexeyDTC_msg4323_transcript.txt](../../inbox/used/20260528_122049_AlexeyDTC_msg4323_transcript.txt)
[^origin1]: [20260528_105720_AlexeyDTC_msg4308_transcript.txt](../../inbox/used/20260528_105720_AlexeyDTC_msg4308_transcript.txt), [20260528_150726_AlexeyDTC_msg4335_transcript.txt](../../inbox/used/20260528_150726_AlexeyDTC_msg4335_transcript.txt)
[^origin2]: [20260528_110401_AlexeyDTC_msg4309_transcript.txt](../../inbox/used/20260528_110401_AlexeyDTC_msg4309_transcript.txt), [20260528_150726_AlexeyDTC_msg4335_transcript.txt](../../inbox/used/20260528_150726_AlexeyDTC_msg4335_transcript.txt)
[^evolution1]: [20260528_110619_AlexeyDTC_msg4311_transcript.txt](../../inbox/used/20260528_110619_AlexeyDTC_msg4311_transcript.txt)
[^evolution2]: [20260528_150726_AlexeyDTC_msg4335_transcript.txt](../../inbox/used/20260528_150726_AlexeyDTC_msg4335_transcript.txt), [20260528_110401_AlexeyDTC_msg4309_transcript.txt](../../inbox/used/20260528_110401_AlexeyDTC_msg4309_transcript.txt)
[^commits]: [20260528_110612_AlexeyDTC_msg4310.md](../../inbox/used/20260528_110612_AlexeyDTC_msg4310.md), [20260528_110626_AlexeyDTC_msg4312_transcript.txt](../../inbox/used/20260528_110626_AlexeyDTC_msg4312_transcript.txt), [github.com/alexeygrigorev/minsearch](https://github.com/alexeygrigorev/minsearch/commits/main/)
[^usecases]: [20260123_121456_valeriia_kuka_msg458_transcript.txt](../../inbox/used/20260123_121456_valeriia_kuka_msg458_transcript.txt)
[^scale]: [20260528_110735_AlexeyDTC_msg4313_transcript.txt](../../inbox/used/20260528_110735_AlexeyDTC_msg4313_transcript.txt)
[^workshops]: [20260528_122004_AlexeyDTC_msg4321_transcript.txt](../../inbox/used/20260528_122004_AlexeyDTC_msg4321_transcript.txt)
[^applied]: [20260528_122004_AlexeyDTC_msg4321_transcript.txt](../../inbox/used/20260528_122004_AlexeyDTC_msg4321_transcript.txt)
