---
title: "Minsearch Benchmarking and Optimization"
created: 2026-02-09
updated: 2026-02-09
tags: [minsearch, benchmarking, optimization, python, performance, llm]
status: draft
---

# Minsearch Benchmarking and Optimization

Optimizing the minsearch appendable index through iterative benchmarking with AI assistance.

## Context

While preparing the agents section of a course, I needed to demonstrate how an agent can add documents to an existing search index. The minsearch library has two index types:

- Simple index: documents are indexed once, nothing can be added
- Appendable index: documents can be added dynamically after creation

The appendable index was needed for the agent demonstration, but it had performance problems.

## Initial Benchmark

I set up a benchmark comparing the two index types using Claude's assistance. We chose Simple Wikipedia as the test dataset because:
- It's written in simple English (A1-A2 level)
- It's not too large for quick benchmarking
- It's suitable for testing purposes[^1]

The initial implementation was extremely slow: the appendable index was 100 times slower than the simple index. The simple index uses scikit-learn internally with efficient operations, while the appendable index was adding each document one at a time.

## Optimization Process

I asked Claude to improve the appendable index performance with a specific workflow:

1. Run benchmark and save baseline results
2. Make improvements to the code
3. After each improvement, verify results still match the original
4. Compare performance[^2]

This approach ensured correctness wasn't sacrificed for speed. Claude implemented optimizations and the final appendable index actually became faster than the original simple index for search operations.

## Final Results

On a c6a.2xlarge AWS instance (8 vCPUs) with 150,000 Simple Wikipedia documents:

- Search: appendable index is faster than the simple index
- Index creation: appendable index is about 1.5x slower than simple index

The slower index creation is expected because each document is added individually rather than batch processed. However, the search performance improvement makes this trade-off worthwhile for use cases where you need to add documents dynamically.

## Workflow

What made this optimization efficient was the parallel workflow:
- I provided direction (use Simple Wikipedia, benchmark, iterate)
- Claude implemented and ran benchmarks
- I checked results about once per hour
- The entire process ran while I worked on course materials[^3]

This demonstrates how AI coding assistants can handle iterative optimization work with minimal supervision, as long as the human provides clear direction and validation criteria.

## Sources

[^1]: [20260209_143545_AlexeyDTC_msg1234_transcript.txt](../inbox/used/20260209_143545_AlexeyDTC_msg1234_transcript.txt)
[^2]: [20260209_143545_AlexeyDTC_msg1234_transcript.txt](../inbox/used/20260209_143545_AlexeyDTC_msg1234_transcript.txt)
[^3]: [20260209_143545_AlexeyDTC_msg1234_transcript.txt](../inbox/used/20260209_143545_AlexeyDTC_msg1234_transcript.txt)
