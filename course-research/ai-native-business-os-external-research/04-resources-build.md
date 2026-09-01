# Resources: Build

Part of the external-source research pack for the AI-Native Business Operating System course.

This file contains **14** of the **53** annotated public resources. Entries preserve every field from the research workbook. Resources are assigned to a file by the first phase named in the original `Phase` field; multi-phase labels are retained in full.

[Back to the research index](README.md)

## R03 — Building Effective AI Agents

- **Phase:** Build
- **Priority:** Core
- **Format:** Technical-practical article
- **Publisher / speaker:** Anthropic
- **Published / updated:** 2024-12-19
- **Evidence type:** Primary engineering guide

**Why it is relevant.** Clear taxonomy of prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, and autonomous agents; strongly argues for the simplest adequate design.

**Best classroom use.** Use to choose the right architecture after the workflow is specified. Have learners classify their workflow as deterministic, workflow-based, or genuinely agentic.

**Source:** [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)

## R04 — A practical guide to building agents

- **Phase:** Build / Run
- **Priority:** Core
- **Format:** Practical guide
- **Publisher / speaker:** OpenAI
- **Published / updated:** 2025
- **Evidence type:** Primary engineering guide

**Why it is relevant.** Covers use-case fit, models, tools, instructions, orchestration, guardrails, handoffs, exit conditions, and human intervention.

**Best classroom use.** Use as a design checklist for the smallest useful build. Particularly useful for converting SOPs and policies into explicit agent routines.

**Source:** [https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

## R22 — AI workflows: How to combine automation and AI

- **Phase:** Build
- **Priority:** Strong
- **Format:** Practical article
- **Publisher / speaker:** Zapier
- **Published / updated:** 2025
- **Evidence type:** Primary vendor guide

**Why it is relevant.** Good low-code framing for mixing deterministic trigger/action steps with AI judgment only where interpretation is required.

**Best classroom use.** Use to sketch the first build as a deterministic shell around one bounded AI step.

**Source:** [https://zapier.com/blog/ai-workflows/](https://zapier.com/blog/ai-workflows/)

## R23 — AI for business automation

- **Phase:** Build
- **Priority:** Strong
- **Format:** Practical article
- **Publisher / speaker:** Zapier
- **Published / updated:** 2025
- **Evidence type:** Primary vendor guide

**Why it is relevant.** Explains how AI can be layered into existing business automations without turning the whole process into an autonomous agent.

**Best classroom use.** Use for learners working in email, forms, spreadsheets, CRMs, and document workflows.

**Source:** [https://zapier.com/blog/ai-for-business-automation/](https://zapier.com/blog/ai-for-business-automation/)

## R24 — Agentic orchestration explained

- **Phase:** Build / Run
- **Priority:** Core
- **Format:** Concept guide
- **Publisher / speaker:** Camunda
- **Published / updated:** 2026
- **Evidence type:** Primary vendor methodology

**Why it is relevant.** Strong deterministic-first explanation: coordinate agents, people, and systems in one process; use agent judgment only for genuine ambiguity; preserve auditability.

**Best classroom use.** Use to teach the automation spectrum and the rule: as much determinism as possible, as little autonomy as necessary.

**Source:** [https://camunda.com/what-is-agentic-orchestration/](https://camunda.com/what-is-agentic-orchestration/)

## R25 — Move your AI agents from proof of concept to production with Amazon Bedrock AgentCore

- **Phase:** Build / Prove / Run
- **Priority:** Core
- **Format:** Hands-on production tutorial
- **Publisher / speaker:** AWS
- **Published / updated:** 2025-09-19
- **Evidence type:** Primary technical tutorial

**Why it is relevant.** Follows a customer-support agent from a local prototype to persistent memory, secure tool sharing, authentication, scalable runtime, end-to-end observability, and a customer-facing interface.

**Best classroom use.** Use as the end-to-end build case. Ask learners to separate demo functionality from the capabilities needed for safe, maintainable production operation.

**Source:** [https://aws.amazon.com/blogs/machine-learning/move-your-ai-agents-from-proof-of-concept-to-production-with-amazon-bedrock-agentcore/](https://aws.amazon.com/blogs/machine-learning/move-your-ai-agents-from-proof-of-concept-to-production-with-amazon-bedrock-agentcore/)

## R26 — An open-source spec for Codex orchestration: Symphony

- **Phase:** Build / Run
- **Priority:** Core
- **Format:** Implementation case + open specification
- **Publisher / speaker:** OpenAI
- **Published / updated:** 2026-04-27
- **Evidence type:** Primary company implementation; internal metric

**Why it is relevant.** Turns an issue tracker into a control plane: every active task gets an isolated agent workspace, blocked dependencies govern execution, stalled work is restarted, and humans review results.

**Best classroom use.** Use as a full dispatch-system case. Map the queue, task contract, state machine, workspace isolation, retries, tests, review gates, and evidence required for closure.

**Source:** [https://openai.com/index/open-source-codex-orchestration-symphony/](https://openai.com/index/open-source-codex-orchestration-symphony/)

## R27 — Choose a design pattern for your agentic AI system

- **Phase:** Build / Run
- **Priority:** Core
- **Format:** Architecture guide
- **Publisher / speaker:** Google Cloud Architecture Center
- **Published / updated:** 2026-05-28
- **Evidence type:** Primary official architecture guidance

**Why it is relevant.** The human-in-the-loop pattern makes intervention a structural workflow checkpoint: execution pauses, state is preserved, and a person can approve, correct, reject, or provide missing input.

**Best classroom use.** Use to build an autonomy ladder and approval matrix. Require learners to identify exactly which actions can proceed, pause, or never be delegated.

**Source:** [https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)

## R28 — Build a custom RAG agent with LangGraph

- **Phase:** Build
- **Priority:** Strong
- **Format:** Hands-on tutorial
- **Publisher / speaker:** LangChain
- **Published / updated:** Living documentation
- **Evidence type:** Primary technical tutorial

**Why it is relevant.** Builds a bounded knowledge workflow that preprocesses and indexes documents, exposes retrieval as a tool, grades retrieved material, rewrites weak queries, and assembles the control graph.

**Best classroom use.** Use as a technical lab for a knowledge assistant. Compare a retrieval-only workflow with a system that is allowed to take external actions.

**Source:** [https://docs.langchain.com/oss/python/langgraph/agentic-rag](https://docs.langchain.com/oss/python/langgraph/agentic-rag)

## R29 — Function calling

- **Phase:** Build
- **Priority:** Strong
- **Format:** Technical guide
- **Publisher / speaker:** OpenAI API documentation
- **Published / updated:** Living documentation
- **Evidence type:** Primary official documentation

**Why it is relevant.** Explains the explicit tool contract and call–execute–return loop: the model requests a structured action, the application executes it, and the result is returned for the next decision.

**Best classroom use.** Use to define each workflow tool's schema, permissions, failure behavior, and authorization boundary. Emphasize that the model proposes actions; the surrounding system controls execution.

**Source:** [https://developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling)

## R30 — Beyond pilots: A proven framework for scaling AI to production

- **Phase:** Build / Run / Scale
- **Priority:** Strong
- **Format:** Implementation framework
- **Publisher / speaker:** AWS
- **Published / updated:** 2025-10-24
- **Evidence type:** Primary implementation framework; customer-reported examples

**Why it is relevant.** Uses the Five V's—Value, Visualize, Validate, Verify, and Venture—to connect business outcomes, baselines, real-world testing, production readiness, ownership, adoption, and total cost.

**Best classroom use.** Use before the build sprint and again in the Run module. Have learners identify what their pilot still lacks before it can become an owned operating capability.

**Source:** [https://aws.amazon.com/blogs/machine-learning/beyond-pilots-a-proven-framework-for-scaling-ai-to-production/](https://aws.amazon.com/blogs/machine-learning/beyond-pilots-a-proven-framework-for-scaling-ai-to-production/)

## R49 — How Two Engineers Ship Like a Team of 15 With AI Agents

- **Phase:** Build / Scale
- **Priority:** Strong
- **Format:** Podcast + article
- **Publisher / speaker:** Every
- **Published / updated:** 2025
- **Evidence type:** Practitioner media; self-reported results

**Why it is relevant.** A practitioner account of coordinating coding agents to deliver many changes with a very small team.

**Best classroom use.** Use as an adjacent example of capacity amplification, while asking what evidence, tests, and review gates make the claim credible.

**Source:** [https://every.to/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents-7bc186bd-b5ea-40cd-9690-963845203f80](https://every.to/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents-7bc186bd-b5ea-40cd-9690-963845203f80)

## R51 — Agents @ Work: Lindy.ai

- **Phase:** Build / Run
- **Priority:** Strong
- **Format:** Podcast
- **Publisher / speaker:** Latent Space
- **Published / updated:** 2025
- **Evidence type:** Practitioner interview

**Why it is relevant.** A candid discussion of why agents need rails, where autonomous systems behave unexpectedly, and how product teams constrain them.

**Best classroom use.** Use as a cautionary architecture case after showing polished agent demos.

**Source:** [https://www.latent.space/p/lindy](https://www.latent.space/p/lindy)

## R53 — Introducing workspace agents in ChatGPT

- **Phase:** Build / Run
- **Priority:** Strong
- **Format:** Product + implementation examples
- **Publisher / speaker:** OpenAI
- **Published / updated:** 2026-04-22
- **Evidence type:** Primary company article; product examples

**Why it is relevant.** Includes concrete internal workflows for lead outreach, product-feedback routing, software review, metrics reporting, third-party risk, and accounting close, with approvals and admin controls.

**Best classroom use.** Use as a library of small workflow briefs that learners can reverse-engineer into maps and specifications.

**Source:** [https://openai.com/index/introducing-workspace-agents-in-chatgpt/](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)
