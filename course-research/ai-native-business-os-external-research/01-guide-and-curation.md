# Guide and curation notes

[Back to the research index](README.md)

## Scope

Curated for the Map → Specify → Build → Prove → Run course. Updated 2026-09-01. Independent public sources only; instructor-owned channels, books, and full-length paid courses excluded.

## What the research pack contains

53 annotated resources, 22 implementation cases, and a five-phase lesson map. The library is intentionally biased toward workflow design, explicit specifications, deterministic controls, human approval, evaluation, ownership, and maintenance. Case metrics are labeled by evidence type; many are customer- or vendor-reported rather than independently audited.

## Recommended first 12 items

### R01 — How AI-native companies turn workflows into operating capability

- **Phase:** Cross-phase
- **Why start here:** Basis, Clay, and Exa show how a recurring workflow becomes a reusable operating capability through triggers, context, tools, evidence, review points, ownership, and metrics.
- **Source:** [https://openai.com/index/ai-native-company-workflows/](https://openai.com/index/ai-native-company-workflows/)

### R05 — Real-World Process Map Examples (+ Expert Tips)

- **Phase:** Map
- **Why start here:** Compares flowcharts, swimlanes, BPMN, value-stream maps, and user flows, including when each is appropriate and what metrics to attach.
- **Source:** [https://miro.com/process-mapping/examples/](https://miro.com/process-mapping/examples/)

### R10 — Business plan for AI agents

- **Phase:** Map
- **Why start here:** Explains when not to use an agent and provides 1–5 scoring across business impact, technical feasibility, and user desirability, plus baselines and go/no-go gates.
- **Source:** [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/business-strategy-plan](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/business-strategy-plan)

### R14 — Effective context engineering for AI agents

- **Phase:** Specify
- **Why start here:** Explains minimal sufficient context, clear instructions, examples, tool contracts, and iterative improvement from observed failures.
- **Source:** [https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### R15 — Equipping agents for the real world with Agent Skills

- **Phase:** Specify / Run
- **Why start here:** Treats reusable instructions, scripts, and resources as an onboarding package for a capable new worker.
- **Source:** [https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### R03 — Building Effective AI Agents

- **Phase:** Build
- **Why start here:** Clear taxonomy of prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, and autonomous agents; strongly argues for the simplest adequate design.
- **Source:** [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)

### R24 — Agentic orchestration explained

- **Phase:** Build / Run
- **Why start here:** Strong deterministic-first explanation: coordinate agents, people, and systems in one process; use agent judgment only for genuine ambiguity; preserve auditability.
- **Source:** [https://camunda.com/what-is-agentic-orchestration/](https://camunda.com/what-is-agentic-orchestration/)

### R31 — How evals drive the next chapter in AI for businesses

- **Phase:** Prove
- **Why start here:** A business-friendly Specify → Measure → Improve loop using real examples, golden sets, error taxonomies, edge cases, expert review, and production-like tests.
- **Source:** [https://openai.com/index/evals-drive-next-chapter-of-ai/](https://openai.com/index/evals-drive-next-chapter-of-ai/)

### R32 — Demystifying evals for AI agents

- **Phase:** Prove
- **Why start here:** Defines an eval as inputs plus grading logic; stresses clear task definitions, reference solutions, positive and negative tests, and human review.
- **Source:** [https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

### R41 — Shared responsibility for AI agents

- **Phase:** Run
- **Why start here:** Organizes responsibilities around data and memory, identity and least privilege, authorization for sensitive actions, oversight, accountability, and acceptable use.
- **Source:** [https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent)

### R25 — Move your AI agents from proof of concept to production with Amazon Bedrock AgentCore

- **Phase:** Build / Prove / Run
- **Why start here:** An end-to-end customer-support build that adds persistent memory, secure tools, authentication, scalable runtime, observability, and a usable interface to a simple prototype.
- **Source:** [https://aws.amazon.com/blogs/machine-learning/move-your-ai-agents-from-proof-of-concept-to-production-with-amazon-bedrock-agentcore/](https://aws.amazon.com/blogs/machine-learning/move-your-ai-agents-from-proof-of-concept-to-production-with-amazon-bedrock-agentcore/)

### R26 — An open-source spec for Codex orchestration: Symphony

- **Phase:** Build / Run
- **Why start here:** A project board becomes the control plane for isolated, continuously running agents, with dependencies, restart behavior, automated tests, and human review.
- **Source:** [https://openai.com/index/open-source-codex-orchestration-symphony/](https://openai.com/index/open-source-codex-orchestration-symphony/)

## Evidence labels used for case studies

- **A:** Primary source with substantial workflow detail. Metrics may still be customer-reported rather than audited.
- **B:** Vendor/customer or practitioner case with a clear workflow and useful implementation detail.
- **C:** Illustrative practitioner account or adjacent analogy; use for discussion, not as causal proof.
- **A/Caution:** Triangulated success and correction/failure evidence; especially useful for teaching boundaries and redesign.

## Suggested curation rule for future additions

Add a resource only when it contributes at least one of the following: a concrete workflow map; an explicit job specification; an architecture decision; a human-control pattern; an evaluation method; a measurable operating result; or a clear failure/correction story. Avoid generic trend pieces, tool roundups, and demonstrations that never show inputs, exceptions, ownership, evidence, or what happens after deployment.
