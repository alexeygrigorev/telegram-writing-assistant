---
title: "Wikidata MCP Workshop"
created: 2026-01-23
updated: 2026-01-23
tags: [workshop, wikidata, mcp, fact-checking, llm, teaching]
status: draft
---

# Wikidata MCP Workshop

A workshop demonstrating Wikidata MCP (Model Context Protocol) for fact-checking with language models.

## The Problem

Language models have knowledge cutoffs and may hallucinate when asked about current events. For example, asking "who is the current president" might produce outdated or incorrect information[^1].

## The Solution: MCP + Wikidata

By connecting to Wikidata through MCP (Model Context Protocol), the agent can retrieve accurate, up-to-date information to use as a reference point for verification[^2].

## Workshop Content

The workshop covered:

- Using open language models for fact-checking
- Retrieving facts from Wikidata as a priori truths
- Checking how well a claim matches known facts
- Using one model for reranking to select relevant facts from Wikidata
- Using a second model to verify truthfulness of the claim

## Terminology

In English terminology:
- The claim is what is being verified
- Facts are what is extracted from Wikidata (considered a priori true)[^3]

## Related Courses

This workshop content is based on materials from:
- AI Bootcamp: https://maven.com/alexey-grigorev/from-rag-to-agents
- LLM Zoomcamp: https://github.com/DataTalksClub/llm-zoomcamp

## Sources

- [20260121_114016_AlexeyDTC_msg355_transcript.txt](../inbox/raw/20260121_114016_AlexeyDTC_msg355_transcript.txt)
- [20260123_080056_valeriia_kuka_msg416_photo.md](../inbox/raw/20260123_080056_valeriia_kuka_msg416_photo.md)

[^1]: [20260121_114016_AlexeyDTC_msg355_transcript.txt](../inbox/raw/20260121_114016_AlexeyDTC_msg355_transcript.txt)
[^2]: [20260121_114016_AlexeyDTC_msg355_transcript.txt](../inbox/raw/20260121_114016_AlexeyDTC_msg355_transcript.txt)
[^3]: [20260121_114016_AlexeyDTC_msg355_transcript.txt](../inbox/raw/20260121_114016_AlexeyDTC_msg355_transcript.txt)
