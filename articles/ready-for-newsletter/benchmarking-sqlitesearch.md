---
title: "Benchmarking SQLiteSearch"
created: 2026-02-21
updated: 2026-02-25
tags: [sqlitesearch, benchmarking, performance, python]
status: draft
---

# Benchmarking SQLiteSearch

An article about benchmarking SQLiteSearch came from Friday. One of the comments on the article was asking whether I had benchmarked it. I had not[^1].

## Text Search Benchmarks

I had benchmarks for minsearch - it showed fairly good results. I had taken the English Simple Wikipedia dataset with 250,000 documents. Minsearch handled about half of that normally, but it was already slow, and on Amazon it ran out of memory[^1].

I decided to take the same dataset and test SQLiteSearch. Claude found some issues and fixed them, and now it works. On 250,000 documents it works slowly, so I decided that instead of debugging for such large volumes - the library was not designed for this - I would say that up to 100,000 is fine. After 100,000, benchmarks show degradation. This is not the recommended amount of data for this technology - use something else for larger volumes[^1].

## Vector Search Benchmarks

For vector search, I looked around and found that Milvus (Zilliz) had benchmarks - two benchmarks, one on 1 million vectors and another on 10 million vectors, plus ground truth labels for what should be returned. They prepared this benchmark and tested it on their vector database and on other databases. Naturally their database showed the best results - otherwise why publish the article[^1].

I took their ready-made benchmark and tested it on SQLiteSearch. On 1 million vectors it worked very slowly and recall was mediocre. On 100,000 it was decent. I gave Claude the task to tune it - I do not know what it will or will not do, but at least in terms of performance it behaves fine. On smaller volumes like up to 100,000 it shows itself quite well[^1].

## Publishing the Results

This can be a separate article - benchmarking SQLiteSearch. People asked for it, so I can tell them: you asked for benchmarks, here are benchmarks. At the same time, we tuned the code to make it more performant. Claude did find a couple of things to fix[^2].

## Benchmark Methodology

When I run benchmarks, I tell Claude: "We are benchmarking now, please remember how it works right now. Tune it so that the exact same IDs are returned, so there is no situation where we tuned something and everything broke." I take this into account in the benchmarks - the results must stay the same[^2].

## Scaling Issues and HNSW

I continued benchmarking SQLiteSearch. I first decided to benchmark it, then noticed that on benchmarks it was slow and performed poorly. For text search it works fine, but for vector search the results were bad[^3].

I asked Claude what to do. It said it tested on a dataset of 1 million records. On 100,000 records it works fine, but on 1 million it breaks. The LSH approach in its current form just does not work at that scale. Claude said everyone uses other methods like HNSW. I said go ahead and implement them, and let us see what happens. I do not really understand how they work and have not looked into it, but that is something to explore later[^3].

I implemented the new approach and indexed 1 million records. One of the approaches took over an hour to index - too much. It should take around 10 minutes[^3].

The benchmark dataset has a gold standard, so you can calculate recall and precision. We need to optimize recall - when recall is bad, retrieval is bad and needs to be optimized[^3].

Of course it is not entirely fair to compare my library with Qdrant and others, because those are multithreaded and production-ready. This is just a hobby project. But I like that I can tell Claude "make it better," check twice a day what it is doing, and say "no, make it better"[^3].

## Sources

[^1]: [20260221_184914_AlexeyDTC_msg2186_transcript.txt](../inbox/used/20260221_184914_AlexeyDTC_msg2186_transcript.txt)
[^2]: [20260221_185007_AlexeyDTC_msg2188_transcript.txt](../inbox/used/20260221_185007_AlexeyDTC_msg2188_transcript.txt)
[^3]: [20260225_201829_AlexeyDTC_msg2447_transcript.txt](../inbox/used/20260225_201829_AlexeyDTC_msg2447_transcript.txt)
