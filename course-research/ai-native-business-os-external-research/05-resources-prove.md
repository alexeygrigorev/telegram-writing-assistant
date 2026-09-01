# Resources: Prove

Part of the external-source research pack for the AI-Native Business Operating System course.

This file contains **9** of the **53** annotated public resources. Entries preserve every field from the research workbook. Resources are assigned to a file by the first phase named in the original `Phase` field; multi-phase labels are retained in full.

[Back to the research index](README.md)

## R31 — How evals drive the next chapter in AI for businesses

- **Phase:** Prove
- **Priority:** Core
- **Format:** Business primer
- **Publisher / speaker:** OpenAI
- **Published / updated:** 2025-11-19
- **Evidence type:** Primary business guide

**Why it is relevant.** A business-friendly Specify → Measure → Improve loop using real examples, golden sets, error taxonomies, edge cases, expert review, and production-like tests.

**Best classroom use.** Use as the main Prove reading. Have each learner create a 20–50 case golden set and a failure taxonomy.

**Source:** [https://openai.com/index/evals-drive-next-chapter-of-ai/](https://openai.com/index/evals-drive-next-chapter-of-ai/)

## R32 — Demystifying evals for AI agents

- **Phase:** Prove
- **Priority:** Core
- **Format:** Engineering guide
- **Publisher / speaker:** Anthropic
- **Published / updated:** 2025
- **Evidence type:** Primary engineering guide

**Why it is relevant.** Defines an eval as inputs plus grading logic; stresses clear task definitions, reference solutions, positive and negative tests, and human review.

**Best classroom use.** Use to make the learner's definition of done executable and to test when the system should refuse or escalate.

**Source:** [https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## R33 — From vibe checks to continuous evaluation: Engineering reliable AI agents

- **Phase:** Prove / Run
- **Priority:** Core
- **Format:** Engineering article
- **Publisher / speaker:** Google Cloud
- **Published / updated:** 2025
- **Evidence type:** Primary engineering guide

**Why it is relevant.** Connects pre-release testing to production monitoring, LLM judges, human feedback, and continuous quality improvement.

**Best classroom use.** Use to design the live review loop after the first workflow is deployed.

**Source:** [https://cloud.google.com/blog/topics/developers-practitioners/from-vibe-checks-to-continuous-evaluation-engineering-reliable-ai-agents](https://cloud.google.com/blog/topics/developers-practitioners/from-vibe-checks-to-continuous-evaluation-engineering-reliable-ai-agents)

## R34 — Eval-Driven System Design: From Prototype to Production — Receipt Inspection

- **Phase:** Prove
- **Priority:** Strong
- **Format:** Hands-on cookbook
- **Publisher / speaker:** OpenAI Cookbook
- **Published / updated:** 2025
- **Evidence type:** Primary technical tutorial

**Why it is relevant.** A concrete workflow case where imperfect real-world inputs, criteria, and evaluation shape a production system.

**Best classroom use.** Use for learners who need to see eval-driven design applied to a document-heavy business process.

**Source:** [https://developers.openai.com/cookbook/examples/partners/eval_driven_system_design/receipt_inspection](https://developers.openai.com/cookbook/examples/partners/eval_driven_system_design/receipt_inspection)

## R35 — Production monitoring and feedback loops for generative AI

- **Phase:** Prove / Run
- **Priority:** Strong
- **Format:** Operational guidance
- **Publisher / speaker:** AWS Prescriptive Guidance
- **Published / updated:** 2025
- **Evidence type:** Primary official guidance

**Why it is relevant.** Covers production feedback, structured review, and human oversight for unfamiliar, high-risk, or low-confidence cases.

**Best classroom use.** Use to define sampling, reviewer assignment, feedback capture, and escalation after go-live.

**Source:** [https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-feedback.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-feedback.html)

## R36 — A scorecard for the AI age

- **Phase:** Prove / Scale
- **Priority:** Core
- **Format:** Business scorecard
- **Publisher / speaker:** OpenAI
- **Published / updated:** 2026
- **Evidence type:** Primary business guide

**Why it is relevant.** Pushes teams to measure useful work, full cost per successful task, dependability, review burden, retries, and rework—not raw output volume.

**Best classroom use.** Use to create the business KPI dashboard for the workflow and to expose hidden human-review costs.

**Source:** [https://openai.com/index/a-scorecard-for-the-ai-age/](https://openai.com/index/a-scorecard-for-the-ai-age/)

## R37 — How companies evaluate LLM systems: 7 examples from Asana, GitHub, DoorDash, and more

- **Phase:** Prove
- **Priority:** Strong
- **Format:** Examples article
- **Publisher / speaker:** Evidently AI
- **Published / updated:** 2025
- **Evidence type:** Secondary synthesis with primary links

**Why it is relevant.** Shows production evaluation practices, including quality dimensions, LLM judges, monitoring, and human calibration.

**Best classroom use.** Use as an examples bank when learners struggle to invent quality rubrics for their own workflows.

**Source:** [https://www.evidentlyai.com/blog/llm-evaluation-examples](https://www.evidentlyai.com/blog/llm-evaluation-examples)

## R38 — You don't know what your agent will do until it's in production

- **Phase:** Prove / Run
- **Priority:** Core
- **Format:** Conceptual guide
- **Publisher / speaker:** LangChain
- **Published / updated:** 2026-02-26
- **Evidence type:** Primary practitioner guidance

**Why it is relevant.** Explains why agent monitoring must capture prompts, responses, multi-turn context, retrieval, tool calls, and full trajectories—not only latency and errors—and connect bad traces back to datasets and experiments.

**Best classroom use.** Use to design the live review loop: what gets traced, sampled, scored, labeled, escalated, and converted into a regression test.

**Source:** [https://www.langchain.com/blog/production-monitoring](https://www.langchain.com/blog/production-monitoring)

## R39 — Evaluate a RAG application

- **Phase:** Prove
- **Priority:** Strong
- **Format:** Hands-on evaluation tutorial
- **Publisher / speaker:** LangSmith / LangChain
- **Published / updated:** Living documentation
- **Evidence type:** Primary technical tutorial

**Why it is relevant.** Shows how to create a test dataset and separately measure answer correctness, answer relevance, groundedness, and retrieval relevance for a knowledge workflow.

**Best classroom use.** Use as technical reinforcement for learners whose workflow depends on retrieval. Require them to distinguish retrieval failures from generation failures.

**Source:** [https://docs.langchain.com/langsmith/evaluate-rag-tutorial](https://docs.langchain.com/langsmith/evaluate-rag-tutorial)
