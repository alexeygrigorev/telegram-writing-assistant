---
title: "Opik Customer Story: Evaluating and Improving the DataTalks.Club FAQ Assistant"
created: 2026-07-31
updated: 2026-07-31
tags: [opik, comet, faq, agents, evals, observability, article-idea]
status: draft
---

# Opik Customer Story: Evaluating and Improving the DataTalks.Club FAQ Assistant

## Short proposal for Paul and Comet

I maintain the FAQ assistant used in the DataTalks.Club Slack community. It is a real system built around two AI workflows: one agent turns community proposals into new or updated FAQ entries, and another retrieves from roughly 3,300 FAQ, documentation and course-repository chunks to answer questions in Slack. The system already has useful evaluation material: 61 decision cases for the FAQ agent, a retrieval benchmark built from 130 real Slack questions, a small set of production answer failures, and integration tests for grounding, fallbacks and citations. What it does not yet have is a proper observability and evaluation layer. The code and the full architecture are open source.

For the collaboration, I would instrument both workflows with Opik and show how traces expose the complete path from input through retrieval and generation to the final action or answer. I would then turn the existing cases—and selected failures from production traces—into Opik test suites with assertions for correct routing, grounded answers, valid citations, appropriate fallbacks and concise responses. Finally, I would use Opik Agent Optimizer on one bounded component, most likely the FAQ decision prompt or answer-generation prompt, and compare the optimized version with the current baseline on a held-out set. The result would be an honest “I tried Opik on a working FAQ agent” customer story: what was easy to integrate, what the traces revealed, whether optimization improved the measured result, and where human review is still necessary.

This gives Comet a concrete demonstration of the full loop around a mature proof of concept: observe real behavior, convert failures into regression tests, optimize against an explicit quality bar, and verify the change before deployment. I can demonstrate the application, its existing evaluations and the Opik project by screen sharing. The accompanying Substack article can go deeper into the implementation and publish reproducible code and results.

## Project links

- Published article: [(Re)Building a FAQ System for DataTalks.Club](https://aishippingblog.com/p/rebuilding-a-faq-system-for-datatalksclub)
- FAQ content, website and proposal-triage agent: [DataTalksClub/faq](https://github.com/DataTalksClub/faq)
- Retrieval, generation and evaluation service: [DataTalksClub/faq-assistant](https://github.com/DataTalksClub/faq-assistant)
- Slack integration: [DataTalksClub/au-tomator-lambda](https://github.com/DataTalksClub/au-tomator-lambda)
- Previous FAQ article: [From Google Docs to an Automated FAQ System for DataTalks.Club Courses](https://aishippingblog.com/p/from-google-docs-to-an-automated)
- Previous Au-Tomator article: [Building and Maintaining a Slack Moderation Bot for an 88k-Member Community](https://aishippingblog.com/p/building-and-maintaining-a-slack)

## Proposed proof of concept

1. Add traces around FAQ proposal classification, query rewriting, retrieval and answer generation.
2. Log the inputs, retrieved source ids, outputs, model, token usage, cost and latency without sending Slack credentials or private channel history.
3. Import a representative subset of the existing evaluation cases into separate Opik test suites:
   - FAQ triage: new, update, duplicate, wrong course and false-positive protection.
   - Answering: groundedness, relevance, citation validity, correct fallback and scope.
   - Production gaps: questions the bot could not answer or answered incorrectly.
4. Add repeated execution for non-deterministic assertions and keep a held-out set that the optimizer never sees.
5. Optimize one prompt, compare it with the current production baseline, inspect regressions by slice, and only adopt it if it improves the target metric without damaging the failure modes that matter most.
6. Show how a newly observed failure becomes a permanent regression test.

## Success criteria

- A trace makes it possible to explain why a bad answer or action happened.
- Existing cases run as named, repeatable Opik test suites.
- The baseline and optimized prompt are compared on the same held-out cases, cost and latency.
- The write-up reports regressions and limitations as well as improvements.
- No private Slack content, credentials or personal data are published.

## Future Substack article placeholder

Working title: **I Added Evals and Observability to Our Production FAQ Agent—Here Is What Changed**

The article should begin with the current FAQ architecture rather than an Opik tutorial. The central question is whether adding an evaluation platform changes how quickly and safely I can improve an agent that already has tests and real users.

Suggested structure:

1. The system before Opik: two agents, three repositories and the existing hand-built evaluations.
2. What was missing: end-to-end traces, comparable experiment history and a short path from production failure to regression test.
3. Instrumenting the proposal agent and the Slack answering path.
4. Translating the existing evaluation sets into Opik test suites.
5. One real failure followed from trace to diagnosis to permanent test.
6. Optimizing one prompt and comparing baseline versus candidate on held-out data.
7. What Opik helped with, what remained easier in code, and what I would keep in production.
8. Reproducible setup, project links, costs and measured results.

Do not decide the conclusion in advance. The useful story is the measured outcome, including a result where the optimizer produces no safe improvement.

## Opik references

- [Building Test Suites](https://www.comet.com/docs/opik/evaluation/advanced/building-test-suites)
- [Opik Agent Optimizer](https://www.comet.com/docs/opik/development/optimization-runs/overview)

