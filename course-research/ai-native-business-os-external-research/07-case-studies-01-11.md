# Case studies C01–C11

Part of the external-source research pack for the AI-Native Business Operating System course.

This file contains **11** implementation cases. Metrics are reported as described by the source and should not be treated as independently audited unless the evidence note explicitly says so.

[Back to the research index](README.md)

## C01 — Basis: Employee onboarding

- **Evidence rating:** A
- **Evidence note:** Customer-reported in a primary OpenAI article

**Before / operational problem.** First-day onboarding depended on repeated HR explanation and setup work.

**AI or system role.** A reusable onboarding skill guides employees through company concepts and integration setup using a clear trigger, known steps, tools, and a definition of done.

**Human control / boundary.** HR handles exceptions and complex questions; the skill is updated when recurring gaps appear.

**Reported outcome.** First-day onboarding reportedly fell from 2 hours to 30 minutes.

**Primary teaching lesson.** Demonstrate a stable process once, convert it into a reusable skill, and learn from exceptions.

**Source:** [https://openai.com/index/ai-native-company-workflows/](https://openai.com/index/ai-native-company-workflows/)

## C02 — Clay: Account-management prioritization

- **Evidence rating:** A
- **Evidence note:** Customer-reported in a primary OpenAI article

**Before / operational problem.** Deal context was scattered across CRM, email, Slack, calls, decks, texts, and internal conversations.

**AI or system role.** A persistent workspace and subagent per account refresh source material overnight; a coordinating agent produces daily priority moves with evidence.

**Human control / boundary.** Sellers inspect primary evidence and decide what action to take; existing account permissions apply.

**Reported outcome.** Clay reports roughly 1 hour of nightly inbox triage saved for the featured GTM engineer.

**Primary teaching lesson.** Persistent context, refresh cadence, evidence proximity, and human judgment at action time.

**Source:** [https://openai.com/index/ai-native-company-workflows/](https://openai.com/index/ai-native-company-workflows/)

## C03 — Exa Labs: Developer-integration opportunity to tested artifact

- **Evidence rating:** A
- **Evidence note:** Customer-reported in a primary OpenAI article

**Before / operational problem.** Teams manually monitored repositories and the ecosystem, researched integration opportunities, coordinated engineering, and prepared communications.

**AI or system role.** The agent monitors opportunities, gathers context, creates pull requests, runs tests, and drafts weekly updates or announcements.

**Human control / boundary.** Humans choose priorities and commitments; tests and review are required before shipping.

**Reported outcome.** Qualitative reduction in cross-functional handoffs; no independently audited time metric published.

**Primary teaching lesson.** Let the agent carry work farther, but preserve tests, permissions, evidence, and decision rights.

**Source:** [https://openai.com/index/ai-native-company-workflows/](https://openai.com/index/ai-native-company-workflows/)

## C04 — Fastweb + Vodafone (Swisscom Group): Customer support and consultant assistance

- **Evidence rating:** B
- **Evidence note:** Detailed vendor case pack; customer-reported architecture and metrics

**Before / operational problem.** The existing chatbot handled straightforward requests, but complex cases required customer context, multiple systems, procedural troubleshooting, and frequent transfers; consultants also searched across disconnected knowledge sources.

**AI or system role.** Super TOBi uses a supervisor to apply guardrails, clarify intent, route to specialized agents, call bounded APIs, and complete selected transactions. Super Agent follows structured procedures and combines a knowledge graph with vector retrieval for source-backed guidance.

**Human control / boundary.** The supervisor can hand off to human operators; business specialists define procedures; consultants retain the customer relationship; daily automated evaluations are reviewed by business stakeholders and technical teams.

**Reported outcome.** The case reports Super TOBi serving nearly 9.5 million customers with 90% correctness, 82% resolution, and a 5.2/7 Customer Effort Score; Super Agent reports one-call resolution above 86%.

**Primary teaching lesson.** Encode domain procedures in inspectable structures, limit each specialist to defined APIs, make handoff a first-class path, and use daily trace-based evaluation to improve the operating system.

**Source:** [https://www.langchain.com/blog/customer-experience-cx-agents-in-production-lessons-from-lyft-vodafone-and-latam-airlines](https://www.langchain.com/blog/customer-experience-cx-agents-in-production-lessons-from-lyft-vodafone-and-latam-airlines)

## C05 — OpenAI Symphony: Always-on coding-agent dispatch from an issue tracker

- **Evidence rating:** A
- **Evidence note:** Primary company implementation with internal, non-audited metric

**Before / operational problem.** Engineers manually supervised several interactive agent sessions at once, creating a context-switching and attention bottleneck even when the agents themselves were fast.

**AI or system role.** Symphony treats the project board as a state machine and control plane. Each active task receives a dedicated workspace and agent; dependencies control when work starts; stalled agents are restarted; agents can create follow-up tasks.

**Human control / boundary.** Humans define and prioritize tickets, review plans and outputs, and decide what lands. Automated tests, repository rules, guardrails, and task status constrain the agents.

**Reported outcome.** OpenAI reports a 500% increase in landed pull requests on some teams.

**Primary teaching lesson.** Manage agents through durable deliverables and explicit state rather than chat sessions. Scale depends on task contracts, isolated workspaces, restart behavior, dependency handling, tests, and review gates.

**Source:** [https://openai.com/index/open-source-codex-orchestration-symphony/](https://openai.com/index/open-source-codex-orchestration-symphony/)

## C06 — Every Consulting / Natalia Quintero: Client project management with Claudie

- **Evidence rating:** B
- **Evidence note:** Practitioner media; self-reported results

**Before / operational problem.** Project management consumed about 15 hours per week across onboarding, data checks, client status, and weekly updates.

**AI or system role.** An AI project manager works from a detailed job description and uses Google Workspace tools to carry out recurring coordination.

**Human control / boundary.** Natalia reviews work, supplies context, and rebuilt the architecture several times before it was reliable.

**Reported outcome.** Every reports workload reduced from 15 hours per week to 1 hour.

**Primary teaching lesson.** A nontechnical operator can build operating leverage, but only through granular job design, iteration, and contextual access.

**Source:** [https://every.to/podcast/everys-head-of-consulting-just-automated-her-job](https://every.to/podcast/everys-head-of-consulting-just-automated-her-job)

## C07 — Every client in private equity: Investment-memo first draft

- **Evidence rating:** B
- **Evidence note:** Practitioner media; client-reported result

**Before / operational problem.** An investment team manually sifted through a decade of thesis materials and applied a current strategy to new opportunities.

**AI or system role.** Proprietary sources are connected to ChatGPT and processed through custom prompts to generate a memo draft.

**Human control / boundary.** An internal champion with both domain and AI understanding mapped the job and guides use; investors retain judgment.

**Reported outcome.** Every reports a solid first draft in about 30 minutes versus a prior three-week process.

**Primary teaching lesson.** High leverage comes from task mapping plus proprietary context; distinguish draft acceleration from final investment judgment.

**Source:** [https://every.to/podcast/everys-head-of-consulting-just-automated-her-job](https://every.to/podcast/everys-head-of-consulting-just-automated-her-job)

## C08 — System AI / The Srama Group: WhatsApp-to-CRM and property tracker

- **Evidence rating:** B
- **Evidence note:** Vendor/customer case study; self-reported

**Before / operational problem.** Virtual assistants copied voice/text requests from WhatsApp into Zoho CRM and Google Sheets; each task took 4–5 minutes.

**AI or system role.** The workflow detects voice or text, transcribes/translates, classifies intent, updates CRM or Sheets, returns confirmation links, and logs executions.

**Human control / boundary.** Verification links make review easy; modular subflows, logging, and existing-tool interfaces support debugging and control.

**Reported outcome.** Vendor case reports 10–20 seconds per task, about one day saved per week, and onboarding-to-sale reduced from 62 to 44 days.

**Primary teaching lesson.** A highly teachable deterministic shell around bounded AI interpretation, with verifiable outputs in existing systems.

**Source:** [https://n8n.io/case-studies/system-ai/](https://n8n.io/case-studies/system-ai/)

## C09 — Healthie: Sales and customer-success call coaching

- **Evidence rating:** B
- **Evidence note:** Vendor/customer case study; self-reported

**Before / operational problem.** Managers could not review every call; reps manually logged notes and drafted follow-ups.

**AI or system role.** Per-rep agents analyze Zoom recordings using a SPICED framework, post coaching and summaries to Slack, create Salesforce records, and draft follow-up email.

**Human control / boundary.** Reps send the final email; managers and teams act on coaching and churn/expansion insights.

**Reported outcome.** Zapier reports more than 60 hours saved per week across roughly 20 reps and CSMs.

**Primary teaching lesson.** Show a clean trigger → analysis → system update → draft → human action workflow with a measurable baseline.

**Source:** [https://zapier.com/blog/healthie-saves-60-hours-per-week-with-ai-agents/](https://zapier.com/blog/healthie-saves-60-hours-per-week-with-ai-agents/)

## C10 — Morgan Stanley Wealth Management: Advisor knowledge and meeting debrief

- **Evidence rating:** A
- **Evidence note:** Primary customer case; customer-reported metrics

**Before / operational problem.** Advisors searched large document collections and manually turned meetings into notes and follow-ups.

**AI or system role.** Assistant retrieves approved knowledge; Debrief converts consented Zoom recordings into CRM notes, draft follow-ups, and action items.

**Human control / boundary.** Advisors review and edit outputs; domain experts grade evals; daily regression tests and compliance controls run.

**Reported outcome.** OpenAI reports more than 98% advisor-team adoption; follow-ups moved from days to hours; document access rose from 20% to 80%.

**Primary teaching lesson.** The strongest Prove case: expert evals, representative datasets, regression suites, consent, and mandatory human review.

**Source:** [https://openai.com/index/morgan-stanley/](https://openai.com/index/morgan-stanley/)

## C11 — OpenAI accounting team: Month-end close preparation

- **Evidence rating:** A
- **Evidence note:** Primary company implementation description

**Before / operational problem.** Journal entries, reconciliations, variance analysis, workpapers, and control totals required repetitive assembly and coordination.

**AI or system role.** A shared agent prepares key parts of close, follows policies, and generates underlying inputs and control totals for review.

**Human control / boundary.** Accounting retains review and sign-off; permissions can be required before sensitive actions.

**Reported outcome.** OpenAI states the agent completes key preparation work in minutes; no audited end-to-end close metric published.

**Primary teaching lesson.** AI should assemble and reconcile; humans remain accountable for financial judgment and control sign-off.

**Source:** [https://openai.com/index/introducing-workspace-agents-in-chatgpt/](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)
