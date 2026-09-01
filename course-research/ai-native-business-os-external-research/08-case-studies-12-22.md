# Case studies C12–C22

Part of the external-source research pack for the AI-Native Business Operating System course.

This file contains **11** implementation cases. Metrics are reported as described by the source and should not be treated as independently audited unless the evidence note explicitly says so.

[Back to the research index](README.md)

## C12 — OpenAI sales team / Rippling: Lead qualification and opportunity briefs

- **Evidence rating:** B
- **Evidence note:** Primary product article; customer-reported metric

**Before / operational problem.** Reps manually combined call notes, account research, qualification criteria, and follow-up drafting.

**AI or system role.** Agents research accounts, summarize calls, score against a rubric, draft follow-ups, update CRM, and post deal briefs.

**Human control / boundary.** Reps decide whether and how to engage; sensitive actions can require approval.

**Reported outcome.** Rippling reports 5–6 hours per week saved per rep for its Sales Opportunity agent.

**Primary teaching lesson.** A reusable pattern for agencies and professional services: evidence-rich preparation followed by human relationship judgment.

**Source:** [https://openai.com/index/introducing-workspace-agents-in-chatgpt/](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)

## C13 — Zendesk: Natural-language service procedures

- **Evidence rating:** A
- **Evidence note:** Primary customer case; vendor/customer-reported

**Before / operational problem.** Traditional service bots followed rigid dialogue trees and struggled with changing customer intent and multi-step resolution.

**AI or system role.** A procedure-compilation agent converts business rules into a structured flow; an execution agent calls APIs and updates systems inside that logic.

**Human control / boundary.** Business teams define procedures; previews, benchmarks, audit records, quality metrics, and escalation constrain execution.

**Reported outcome.** Zendesk reports setup reduced from days to minutes; broader automation metrics were still in pilot at publication.

**Primary teaching lesson.** Excellent Specify → Build pattern: compile natural-language rules into a visible procedure before an agent executes them.

**Source:** [https://openai.com/index/zendesk/](https://openai.com/index/zendesk/)

## C14 — BBVA Mexico Legal Services: Corporate signatory-authority questions

- **Evidence rating:** A
- **Evidence note:** Primary report; customer-reported metrics

**Before / operational problem.** Specialist legal staff answered repetitive branch questions before transactions could proceed, creating bottlenecks.

**AI or system role.** A legal chatbot gives instant access to standardized, pre-validated legal FAQs and guidance.

**Human control / boundary.** Legal Services develops and reviews the content; complex matters remain with specialists.

**Reported outcome.** OpenAI reports more than 9,000 queries automated annually, 3 FTE-equivalents redeployed, and 26% of the division's annual savings KPI delivered.

**Primary teaching lesson.** A bounded high-value knowledge workflow can free scarce expert capacity without delegating final legal judgment.

**Source:** [https://openai.com/business/guides-and-resources/the-state-of-enterprise-ai-2025-report/](https://openai.com/business/guides-and-resources/the-state-of-enterprise-ai-2025-report/)

## C15 — Huel: Enterprise-wide workflow building and AI champions

- **Evidence rating:** B
- **Evidence note:** Vendor/customer case study; self-reported

**Before / operational problem.** AI experiments risked remaining with a small technical group while teams depended on fragmented, expensive SaaS tools.

**AI or system role.** A central three-person AI/automation team governs complex builds while departmental AI Champions create workflows; recurring trainings and showcases spread patterns.

**Human control / boundary.** Central monitoring, approval gates, API-based oversight, InfoSec alerts, and project roles govern distributed building.

**Reported outcome.** n8n reports nearly 200 workflows, about 1,000 hours saved in nine months, and more than £100,000 in annual software-license savings.

**Primary teaching lesson.** A strong operating-model case: central platform and governance plus embedded champions, learning rituals, and visible examples.

**Source:** [https://n8n.io/case-studies/huel/](https://n8n.io/case-studies/huel/)

## C16 — Fullscript: Citizen workflow development with production gates

- **Evidence rating:** B
- **Evidence note:** Vendor/customer case study; self-reported

**Before / operational problem.** The AI/ML team could not be the bottleneck for every internal workflow in a regulated healthcare organization.

**AI or system role.** Employees build in a staging environment; engineering controls production. Training and a hackathon generated many workflow ideas.

**Human control / boundary.** Separate staging/production, audit outputs, regulated-data controls, and production ownership limit risk.

**Reported outcome.** n8n reports 200+ employee users, 130 workflows created at a hackathon, and a security-investigation workflow reducing time from weeks to roughly 30 minutes.

**Primary teaching lesson.** Democratize discovery and prototyping, but maintain a clear gate between experimentation and production.

**Source:** [https://n8n.io/case-studies/fullscript/](https://n8n.io/case-studies/fullscript/)

## C17 — Zapier: Organization-wide AI adoption

- **Evidence rating:** B
- **Evidence note:** Primary company account; self-reported

**Before / operational problem.** Tool access alone did not guarantee durable use across all functions.

**AI or system role.** Leadership urgency, structured experimentation, hackathons, shared groups, internal examples, measurement, and workflow redesign became ongoing operating practices.

**Human control / boundary.** Compliance and safety structures run behind the scenes; adoption and usage are tracked; teams own real workflows.

**Reported outcome.** Zapier reports 97% adoption; Support Sidekick cut average handle time roughly in half.

**Primary teaching lesson.** Adoption is a managed operating system: repeated signals, safe experimentation, champions, examples, and measurement.

**Source:** [https://zapier.com/blog/how-zapier-rolled-out-ai/](https://zapier.com/blog/how-zapier-rolled-out-ai/)

## C18 — Trendyol: Decentralized workflow platform at enterprise scale

- **Evidence rating:** B
- **Evidence note:** Vendor/customer case study; self-reported

**Before / operational problem.** Technical and nontechnical teams had long backlogs for small utilities, support, legal, search, and operational automations.

**AI or system role.** A self-hosted platform supports seller chat, legal assistance, search-relevancy checks, code review, and hundreds of team-built workflows.

**Human control / boundary.** About 200 isolated projects scope credentials and visibility; SSO, logging, vaults, a central maintainer team, and local ownership are required.

**Reported outcome.** n8n reports 1,000+ active users, 700 active workflows, and about 500,000 executions per quarter in under a year.

**Primary teaching lesson.** Scale requires tenant isolation, credentials governance, logging, local ownership, and a community—not just more agents.

**Source:** [https://n8n.io/case-studies/trendyol/](https://n8n.io/case-studies/trendyol/)

## C19 — Moderna: Federated GPT creation and clinical/product workflows

- **Evidence rating:** B
- **Evidence note:** Primary customer case; customer-reported

**Before / operational problem.** AI value needed to spread beyond a central team while preserving domain review in science, legal, compliance, and communications.

**AI or system role.** Employees create reusable GPTs; examples include dose-analysis support, contracts, policies, investor communication, and target-product-profile drafting.

**Human control / boundary.** Clinical and legal experts retain decision authority; outputs reference sources and support rather than replace judgment.

**Reported outcome.** OpenAI reports 750 GPTs in two months, 40% of weekly active users creating GPTs, and some analytical steps reduced from weeks to hours.

**Primary teaching lesson.** A federated-building case: empower domain experts, but keep high-stakes interpretation and decisions human-led.

**Source:** [https://openai.com/index/moderna/](https://openai.com/index/moderna/)

## C20 — Klarna: Customer-service automation and later hybrid correction

- **Evidence rating:** A/Caution
- **Evidence note:** Primary launch metrics plus independent Reuters follow-up

**Before / operational problem.** High-volume support created pressure to automate refunds, returns, payments, disputes, and multilingual questions.

**AI or system role.** An AI assistant handled routine conversations and transactions at global scale.

**Human control / boundary.** Live agents remained available; by late 2025 Klarna emphasized that complex issues and customer preference still require humans.

**Reported outcome.** Klarna's 2024 launch reported 2.3 million conversations, two-thirds of chats, 25% fewer repeat inquiries, and under 2 minutes versus 11 minutes. Reuters later reported a deliberate hybrid model.

**Primary teaching lesson.** Use as a caution: impressive launch metrics do not determine the durable autonomy boundary; service quality and customer preference can shift the design.

**Sources:** [Klarna launch announcement](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) · [Reuters follow-up](https://www.reuters.com/business/business-leaders-agree-ai-is-future-they-just-wish-it-worked-right-now-2025-12-16/)

## C21 — Leading European bank (BCG client): Retail lending

- **Evidence rating:** B
- **Evidence note:** Consulting client case; self-reported

**Before / operational problem.** Loan origination required document classification, data synchronization, extraction, correction, fraud checks, signatures, and contract validation.

**AI or system role.** An agentic operating process handles unstructured data and coordinates the full lending workflow.

**Human control / boundary.** The case stresses defined governance, controls, accountability, exception handling, and a process owner.

**Reported outcome.** BCG reports more than 90% end-to-end automation for consumer loans, more than 70% for mortgages, and productivity gains above 50%.

**Primary teaching lesson.** A zero-based process redesign can outperform adding an AI assistant to isolated lending tasks.

**Source:** [https://www.bcg.com/publications/2026/reinventing-the-operating-system-of-work-with-ai](https://www.bcg.com/publications/2026/reinventing-the-operating-system-of-work-with-ai)

## C22 — Every: Small-team product delivery with coding agents

- **Evidence rating:** C
- **Evidence note:** Practitioner media; self-reported

**Before / operational problem.** A very small engineering team wanted to increase delivery capacity without scaling headcount proportionally.

**AI or system role.** Engineers coordinate AI coding agents across implementation, bug fixes, infrastructure, and testing.

**Human control / boundary.** Humans specify, inspect changes, run tests, and decide what ships.

**Reported outcome.** Every reports two engineers shipped work comparable to a much larger team during the featured period.

**Primary teaching lesson.** Useful adjacent analogy: autonomy is credible only when specifications, tests, and review make agent output inspectable.

**Source:** [https://every.to/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents-7bc186bd-b5ea-40cd-9690-963845203f80](https://every.to/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents-7bc186bd-b5ea-40cd-9690-963845203f80)
