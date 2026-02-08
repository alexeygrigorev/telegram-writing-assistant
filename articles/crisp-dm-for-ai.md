---
title: "CRISP-DM for AI"
created: 2026-02-08
updated: 2026-02-08
tags: [ai-engineering, methodology, crisp-dm, processes]
status: draft
---

# CRISP-DM for AI

CRISP-DM (Cross-Industry Standard Process for Data Mining) is a methodology from 1996 that organized how data mining and ML teams work. What's remarkable is that this framework, originally designed for data mining, remains highly relevant for AI projects today[^1].

## Why CRISP-DM Still Matters

All the processes that data teams have used since the 1990s remain applicable to AI projects. The steps we take in AI projects map directly to the CRISP-DM framework.

I wrote about CRISP-DM in my book, and the concepts described there apply equally to modern AI engineering[^2].

<figure>
  <img src="../assets/images/crisp-dm-for-ai/crisp-dm-cycle.jpg" alt="CRISP-DM cycle diagram showing six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment">
  <figcaption>The CRISP-DM cycle: six phases that form an iterative process for data-driven projects</figcaption>
  <!-- This diagram illustrates the cyclical nature of AI projects, where each phase informs the others -->
</figure>

## Mapping CRISP-DM to AI Projects

### Business Understanding

This phase is critical: we must deeply understand the problem we're solving and define upfront how we'll measure success. What makes this project successful or not? We establish these criteria at the beginning[^3].

For AI projects, this means:
- What problem are we solving?
- How will we know if AI is the right solution?
- What metrics define success?

### Data Understanding

We need to understand what data we have available. AI doesn't work in a vacuum. We need to know:
- What data can we send to the AI?
- What can we expect back?
- What data sources exist?

In traditional ML, this phase involves checking for target variables. For AI, it's about understanding what context and inputs we have available[^4].

### Data Preparation

In traditional ML, this means preparing features and target variables for model training. For AI:
- Data needs to be accessible
- It should be stored where it's easily retrievable
- We may need to preprocess or format it for AI consumption

The key difference: we're not preparing data for training, but for retrieval and context injection[^5].

### Modeling

This is where the biggest change occurs. Instead of:
- Fine-tuning models
- Feature engineering
- Traditional model training

We have:
- Prompt engineering - crafting effective prompts
- Experiments - trying different approaches before the model is "ready"
- API-based interaction with models like OpenAI[^6]

### Evaluation

Evaluation follows the same CRISP-DM pattern: we roll out to a portion of users and observe how they react. Classic A/B testing applies to AI projects just as it did for ML[^7].

### Deployment

Deployment remains similar: putting the system into production. The entire process is iterative - we cycle through these steps until performance is satisfactory[^8].

## The Iterative Nature

CRISP-DM emphasizes that projects are iterative. We never truly "finish" - we iterate until we achieve satisfactory results, then continue improving. This iterative approach is essential for AI projects where:
- User behavior may be unpredictable
- Prompts need refinement
- Evaluation metrics may need adjustment

## Historical Context

The fact that a framework from 1996 remains relevant tells us something important: while the tools change (from training models to API calls), the fundamental process of building data-driven products remains constant.

The processes data scientists have always used - evaluation, versioning, experimentation - are exactly what AI engineers need today. This is why data scientists often make excellent AI engineers with some additional coding practice[^9].

## Sources

[^1]: [20260208_114819_AlexeyDTC_msg1192_transcript.txt](../inbox/raw/20260208_114819_AlexeyDTC_msg1192_transcript.txt)
[^2]: [CRISP-DM Article at ML Bookcamp](https://mlbookcamp.com/article/crisp-dm) - Original article explaining the CRISP-DM methodology
[^3]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/raw/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^4]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/raw/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^5]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/raw/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^6]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/raw/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^7]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/raw/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^8]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/raw/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^9]: [20260208_114623_AlexeyDTC_msg1188_transcript.txt](../inbox/raw/20260208_114623_AlexeyDTC_msg1188_transcript.txt)
