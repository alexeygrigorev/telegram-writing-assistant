---
title: "Plan: Kirill Krotov - LLM Zoomcamp July Sprint"
created: 2026-06-30
updated: 2026-06-30
tags: [ai-shipping-labs, plan, community, llm-zoomcamp-2026]
status: draft
---

# Plan: Kirill Krotov - LLM Zoomcamp July Sprint

Internal working document. Share only the `Summary` and plan sections with the member.

## Summary

- Current situation: Kirill is a project engineer in offshore oil and gas who also drives digitalization work in the Norwegian office. His previous sprint plan focused on a pipe-history / risk-lookup RAG for offshore engineering data. In the May sprint, he marked the first two conceptual-scope checkpoints done, but the implementation work still needs a tighter course-aligned path. He has now requested a plan around taking LLM Zoomcamp and already has the `llm-zoomcamp-2026` tag.
- Goal for the next 6 weeks: stay aligned with LLM Zoomcamp while turning the course work into a practical offshore-document assistant: a small, demoable RAG / extraction workflow over synthetic or anonymized pipe-project documents that can answer risk/similarity questions and expose what data would be needed for a real company version.
- Main gap to close: moving from conceptual scenarios to an implemented, evaluated LLM workflow. The important bridge is not Graph-RAG yet; it is a plain, reliable pipeline with clear data assumptions, retrieval, answer generation, evaluation, monitoring, and a demo that uses safe data.
- Weekly time commitment: protect the LLM Zoomcamp cadence first; shrink the project slice when work/travel reduces capacity.
- Why this plan is the right next step: Kirill learns best by doing and wants practical skills he can apply to internal AI-adoption work. LLM Zoomcamp gives the course structure; the pipe-history / document-audit use case gives the domain-specific project that makes the course useful instead of abstract.

## Focus

- Main focus: use LLM Zoomcamp as the weekly learning track, and apply each module to a small offshore-document RAG / extraction project.
- Supporting focus: keep the project scoped to synthetic or anonymized data, with a clear path from "new pipe project -> similar past cases + risks" to a demoable assistant.
- Supporting focus: document the assumptions, data model, failure modes, and SharePoint / scale constraints so the output can later become an internal proposal or next-sprint project.

## Timeline

Week 1:

- Catch up and align with the LLM Zoomcamp cohort: review the Agentic RAG and Vector Search modules, note anything missing from earlier homework, and get ready for the Orchestration work.
- Re-scope the May sprint idea into one project card: user, input, data sources, output, success metric, and what will be synthetic/anonymized for the community demo.
- Pick the exact demo slice: either pipe-history risk lookup, structured extraction from legacy documents, or document audit against internal standards. Default to pipe-history risk lookup unless another slice is clearly easier with available safe data.
- Create 8-12 synthetic example records that represent past pipe projects: properties, source snippet, outcome, and risk notes. Keep the schema simple enough to use in the course homework.

Week 2:

- Apply the LLM Zoomcamp Orchestration module to the project: define the main flow from user question to retrieval/extraction to final answer.
- Build the first minimal end-to-end version on synthetic data: load records, index chunks, retrieve relevant cases, and produce a grounded answer with cited source snippets.
- Write 10 realistic test questions that match Kirill's actual work scenarios, including "new pipe project with properties X/Y/Z" and document-audit style questions.
- Post a short #plan-sprints update with the chosen project card and one example query/answer.

Week 3:

- Apply the LLM Zoomcamp Evaluation module: turn the 10 questions into a small evaluation set with expected answer traits, not just generic correctness.
- Run a baseline eval and record where the system fails: wrong retrieval, vague answer, missing citation, bad extraction, or unsafe overclaim.
- Improve one thing based on the eval results. Choose the highest-impact fix only: chunking, metadata filters, prompt structure, or answer schema.
- Keep a short failure-mode note that could later support an internal pitch: what the system can do, what it cannot do yet, and what data quality it depends on.

Week 4:

- Apply the monitoring/logging part of LLM Zoomcamp: capture queries, retrieved chunks, answer schema, latency, and obvious failure labels.
- Add a lightweight structured output format for the answer: similar cases, risk flags, source snippets, confidence/limitations, and suggested next checks.
- Test the workflow with a second synthetic document type, such as a scanned-report summary, inspection note, or standard/checklist excerpt.
- Write down the SharePoint and data-storage constraints separately from the prototype so they do not block the demo but remain visible for a real implementation.

Week 5:

- Polish the demo path: 3-5 prepared questions, stable answers, visible citations, and a short explanation of the data schema.
- Tighten the README: problem, data assumptions, architecture, run instructions, evaluation results, and limitations.
- Decide what should be shown publicly and what should stay private. Use only synthetic or anonymized examples in Slack, GitHub, or any live demo.
- Ask one or two LLM Zoomcamp / AI Shipping Labs peers for feedback on the demo flow and the evaluation criteria.

Week 6:

- Finalize the course-project version: clean repo, reproducible run command, README, small eval report, and demo script.
- Demo in #plan-sprints: one domain scenario, one answer, one failure case, and what changed after evaluation.
- Decide the next step: continue as an LLM Zoomcamp final project, pitch a small internal proof of concept at work, or pivot to the document-audit / structured-extraction variant for the next sprint.
- Write a short next-sprint note: what real data access would be needed, what risks remain, and whether Graph-RAG is justified later or still premature.

## Resources

- [LLM Zoomcamp 2026 GitHub repository](https://github.com/DataTalksClub/llm-zoomcamp) - course modules, homework, and project structure.
- [LLM Zoomcamp 2026 course platform](https://courses.datatalks.club/llm-zoomcamp-2026/) - current cohort deadlines and submissions.
- [AI Shipping Labs AI Hero](https://aishippinglabs.com/courses/aihero) - optional fallback/reference for RAG, agent loop, eval, deployment, and README patterns.
- Previous May plan: AI Shipping Labs plan 60 - pipe-history risk-lookup RAG for offshore engineering data.
- Community accountability channel: `#plan-sprints`.

## Deliverables

- One course-aligned project card for the offshore-document assistant by the end of week 1.
- Synthetic/anonymized dataset with 8-12 pipe/project/document examples by the end of week 1.
- Minimal RAG / extraction workflow with cited answers by the end of week 2.
- Evaluation set and baseline failure-mode note by the end of week 3.
- Monitoring/logging and structured answer format by the end of week 4.
- README, demo script, eval summary, and final #plan-sprints demo by the end of week 6.

## Accountability

Weekly update in #plan-sprints with three lines: what LLM Zoomcamp module/homework moved forward, what changed in the offshore-document project, and what is blocked or uncertain. If time is tight, Kirill should protect the course cadence first and reduce project scope to the next smallest demo slice.

## Next Steps

- Kirill: confirm the exact project slice for the sprint: pipe-history risk lookup, structured extraction, or document audit. Default to pipe-history risk lookup.
- Kirill: collect or write 8-12 safe synthetic examples that mimic the fields and messiness of real pipe/project documents.
- Kirill: catch up with the LLM Zoomcamp Agentic RAG and Vector Search modules, then align the project with the Orchestration homework.
- Kirill: post the project card and first example query/answer in #plan-sprints.
- Alexey: review the project card once posted and steer scope down if the demo starts looking too production-sized.

## Meeting Notes

Source: 2026-04-24 1:1 summary with Alexey Grigorev. Kirill is a project engineer in offshore oil and gas, based in Norway, and runs digitalization work in the Norwegian office. He has built low-code automation and Power BI dashboards, including workflows that aggregate data from spreadsheets and scanned documents. He wants to close the gap between oil-and-gas domain knowledge and AI engineering skills.

The strongest project shape from the 1:1 was pipe-history / risk-lookup RAG: given a new pipe project with properties such as length, weight, material, coating, vessel, field, and installation method, retrieve similar historical cases and identify risks. Alexey recommended starting with plain RAG, not Graph-RAG, and keeping the early work conceptual enough to understand data, questions, and expected answers before coding.

The May plan was created as plan 60 in the May 2026 sprint. Its first two conceptual checkpoints were marked done on 2026-06-17, while most implementation checkpoints remained open. That suggests the July plan should not assume a completed prototype; it should restart from a tighter course-aligned implementation path.

## Internal Recommendations

- Use LLM Zoomcamp as the external cadence and the offshore-document assistant as the applied project. This prevents the course from becoming detached homework.
- Keep the project on synthetic or anonymized data. Real company documents, customer records, and commercial project data should not be used in community demos.
- Do not jump to Graph-RAG in this sprint. The July goal is a reliable plain RAG / extraction workflow with evaluation and monitoring.
- If Kirill falls behind, reduce the project dataset and demo scope, not the weekly course sync. The plan is only useful if it stays connected to the cohort rhythm.

## Sources

- Source file: `/home/alexey/git/zoom-calls/1x1/2026-04-24-kirill-summary.md`.
- Production CRM note 96, created 2026-06-15: Kirill plans to take LLM Zoomcamp and wants to connect with other participants. Source quote recorded in CRM: "yes, I am doing that / Likewise, would be nice to connect with others".
- Production May plan 60: Build a pipe-history risk-lookup RAG for offshore engineering data.
- Public LLM Zoomcamp 2026 course schedule checked on 2026-06-30: Agentic RAG and Vector Search are early modules; Orchestration, Evaluation, and Monitoring follow in July.
