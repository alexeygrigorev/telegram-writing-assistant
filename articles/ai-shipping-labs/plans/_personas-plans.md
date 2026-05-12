---
title: "AI Shipping Labs - Persona Plans"
created: 2026-05-12
updated: 2026-05-12
tags: [ai-shipping-labs, plans, personas, synthesis]
status: draft
---

# AI Shipping Labs - Persona Plans

This document distils, for each of the four AI Shipping Labs personas, what a typical starting point looks like, a realistic 6-month arc, and a 6-week sprint template. It is grounded in the real plans, intake docs, interviews, and 1:1 zoom calls collected up to 2026-05-12 - not invented from a generic AI Engineering syllabus.

Inputs used: 18 personal plans in [plans/](.) (the `YYYYMMDD_*.md` files), 19 interview files in [interviews/](../interviews/), and 12 1:1 zoom-call summaries plus 1 discussion summary from `~/git/zoom-calls/`. The full list lives at the bottom of this file.

## How to use this

These are templates, not contracts. When a new member arrives, pick the persona that fits them, use the starting-point checklist to confirm, and then adapt the 6-week template. The structural decisions (week 1 picks a project, week 4 builds the eval set, week 6 demos) repeat across plans for a reason - they work. The content per week is what gets tailored. Each persona section also includes a "Why this plan fits" subsection with one or two worked examples from real members, showing how the template lands on a specific intake.

When in doubt, ground the conversation in the canonical persona definitions in [personas.md](../personas.md) - especially the engineering-skills / AI-knowledge / main-gap table.

## Persona overview

The canonical starting-point table from [personas.md](../personas.md):

| Persona | Engineering skills | AI/ML knowledge | Main gap |
|---------|-------------------|-----------------|----------|
| Alex | Strong | Low | AI-specific knowledge |
| Priya | Strong | Medium | Depth and production patterns |
| Taylor | Weak-to-medium | Strong | Software engineering, deployment, production |
| Sam | Weak (scripts, not systems) | Low | Both engineering and AI fundamentals |

Distribution across the existing personal plans (with provisional / confirmed persona assignments from the Internal Context section of each plan):

- Alex - 8 plans: Daiyaan Shaik, Aashiesh Siwach, Manjunath Yelipeta, Vishnu, Motasem Salem, Kushal Kulshreshtha, Grace, Dianne Bronola
- Priya - 2 plans: Juan Perez Prim, Nirajan Acharya
- Sam - 6 plans: Daniel Sa Earp, Valeriia Kuka, Sai Kumar G, Carlos Pumar, Jakob Zischka, Koray Can Canut (Diogo Valente Polónia is provisionally Sam)
- Taylor - 2 plans: Luca, Edu Gonzalo Almorox
- Undetermined - 1 plan: Vancesca Dinh (closest to Alex)

Distribution across interviews where a persona is tagged: Alex (Aashiesh, Daiyaan, Vancesca, Brad Smith, Leonor, anonymous-buildcamp-participant), Priya (Chandra, Luciano Pecile, anonymous-participant-april), Sam (Jakob, Koray). The remaining interviews are tagged Undetermined because the intake stayed too brief to map.

The 1:1 zoom calls in `~/git/zoom-calls/1x1/` provide additional unfiltered starting-point detail for many of the same people plus some who never made it into a plan (Giang Do, Nikolai, Kirill, Sergey Sedler, Ivan Brigida, Ivan Dubograi, Bradley Smith, Chandra, Shrikant K., Luciano Pecile).

Alex is the most common persona in the current data, Priya and Taylor are the rarest, Sam is the second most common but also the most varied.

## Alex - The Engineer Transitioning to AI

### Starting point

Across the eight Alex-tagged plans plus the zoom calls and interviews, the typical Alex arrives looking like this:

- Has shipped software professionally for several years. The exact stack varies - Daiyaan is a data lead on Databricks and a Data Engineering Zoomcamp + MLOps Zoomcamp graduate ([20260509_daiyaan-shaik.md](20260509_daiyaan-shaik.md)); Manjunath is a traditional ML engineer with FastAPI and Docker familiarity ([20260506_manjunath-yelipeta.md](20260506_manjunath-yelipeta.md)); Grace is a 7-year iOS engineer in Stockholm ([20260420_grace.md](20260420_grace.md)); Dianne is an iOS / platform engineer ([20260502_dianne-bronola.md](20260502_dianne-bronola.md)); Motasem is an ML engineer with a software engineering background who already deploys models to production ([20260427_motasem-salem.md](20260427_motasem-salem.md)). The common thread is "I can build and ship software", not a specific stack.
- Has dabbled in AI on the side - usually one or two prototypes - but has not built and shipped one LLM application end to end at the depth they want. Daiyaan built a Karpathy-style "second brain" in Obsidian with NotebookLM flashcards but acknowledges "none of this uses the core AI fundamentals - it uses existing tools and their orchestration" ([20260509_daiyaan-shaik.md](20260509_daiyaan-shaik.md)). Aashiesh has shipped a hybrid search + reranking pipeline and a climate misinformation RAG during a university internship ([20260508_aashiesh-siwach.md](20260508_aashiesh-siwach.md)). Vishnu already has V1 of a 5-agent Medicare plan recommender nearly done ([20260429_vishnu.md](20260429_vishnu.md)). Vancesca finished one Buildcamp project and wants a second ([20260420_vancesca-dinh.md](20260420_vancesca-dinh.md)). The depth varies from "first time" (Manjunath) to "second project, more rigorous this time" (Vancesca, Vishnu).
- Day job constrains them to evenings and weekends. Typical time budgets sit in a 5-15 hr/week band: Daiyaan 5-8 ([20260509_daiyaan-shaik.md](20260509_daiyaan-shaik.md)), Vishnu 6-10 ([20260429_vishnu.md](20260429_vishnu.md)), Manjunath 8-10 ([20260506_manjunath-yelipeta.md](20260506_manjunath-yelipeta.md)), Grace ~10 with weekend swelling ([20260420_grace.md](20260420_grace.md)), Dianne 10-15 ([20260502_dianne-bronola.md](20260502_dianne-bronola.md)), Motasem 10-15 ([20260427_motasem-salem.md](20260427_motasem-salem.md)), Vancesca 20 with job-search time ([20260420_vancesca-dinh.md](20260420_vancesca-dinh.md)). Nirajan's 30-40 hr/week is the outlier.
- Heavy or growing user of coding agents. Daiyaan uses Cursor and Claude Code daily ([20260509_daiyaan-shaik.md](20260509_daiyaan-shaik.md)); Motasem wants to learn the spec-driven agent-team workflow ([20260427_motasem-salem.md](20260427_motasem-salem.md)); Ivan Dubograi (zoom call 2026-04-27) is already running a manager + dev + tester sub-agent pattern with Spec-Driven Development. The Alex picks-a-coding-assistant step in week 1 is real - free tiers do not survive a 6-week sprint.
- The "where do I start" feeling is not about content; it is about choosing one project and committing. Alex usually has more ideas than time. The anonymous Buildcamp participant interview ([../interviews/anonymous-buildcamp-participant.md](../interviews/anonymous-buildcamp-participant.md)) sums it up: "content is not the problem - the problem is accountability".

### 6-month plan

The personal plans in this folder cover only the first 6 weeks. The 6-month arc below is a synthesis of the "next sprint" sketches at the end of each Alex plan, the longer-arc notes (Dianne's 3 / 12-month framing, Manjunath's platform pivot, Daiyaan's analysis-paralysis-to-shipping arc), and the 1:1 patterns. The arc is one shipped project per sprint, deepened in the right direction.

Month 1 - Foundation and first shipped artefact.

- AI Hero as the foundation course for anyone without LLM/agent experience (Daiyaan, Aashiesh, Manjunath, Kushal, Grace, Jakob all start there). The shape is 7 days of agent fundamentals: chunking, search, agent with tools, evaluation, deployment. Plan to actually take 2-3 calendar weeks at evenings-and-weekends pace, not the marketing "7 days".
- Pick one project using the brainstorming gist ([alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1](https://gist.github.com/alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1)). Bias the pick toward something Alex would actually use - the four-criterion scoring (interest, usefulness, data availability, feasibility) is in [20260508_aashiesh-siwach.md](20260508_aashiesh-siwach.md).
- Ship the simplest end-to-end version - input, processing, output - on the chosen project by end of month 1. Deployed or at least runnable as a CLI / Streamlit page used daily.

Month 2 - Eval, monitoring, polish, first portfolio piece.

- Build an eval set of 20-50 representative questions or inputs ([20260509_daiyaan-shaik.md](20260509_daiyaan-shaik.md), [20260508_juan-perez-prim.md](20260508_juan-perez-prim.md), [20260506_manjunath-yelipeta.md](20260506_manjunath-yelipeta.md) all do this).
- Add monitoring (Logfire or equivalent) so failures and slow tool calls are visible.
- Deploy properly. Live URL, CI eval gating on every push, README that explains problem / architecture / eval results / run instructions. This is where the month-1 prototype becomes a portfolio piece.
- Demo to the community via Slack.

Month 3 - Direction-specific second project.

- The direction shifts based on what Alex discovered in months 1-2. Three common branches:
  - AI Engineering depth - second project with agentic patterns, RAG over a different shape of data, cost/latency optimisation (this is Manjunath's post-week-6 sketch in [20260506_manjunath-yelipeta.md](20260506_manjunath-yelipeta.md), and Daiyaan's "fintech-adjacent next project" arc).
  - AI Platform / MLOps - start abstracting the deployment, monitoring, and eval scaffolding into a reusable platform v0.0.1 (the v1 plan for Manjunath, kept as the next-sprint arc).
  - AI-assisted full-stack development - spec-driven development with a team of agents, frontend + backend + e2e tests (Motasem's track in [20260427_motasem-salem.md](20260427_motasem-salem.md)).
- LLM Zoomcamp re-recording starts in June 2026 and can be folded in here for anyone who wants more structured retrieval / search material.

Month 4 - Second shipped project, deeper agentic work.

- Second project shipped with the same arc compressed - week 1 pick, weeks 2-3 build, week 4 eval, week 5 monitor + deploy, week 6 polish.
- The eval and monitoring patterns from month 2 transfer; the build is faster because the scaffolding is already in muscle memory.
- This is the sprint where Alex first feels the platform-shaped question: "what is shared between project 1 and project 2?" That answer seeds month 5.

Month 5 - Direction-specific deepening.

- For the AI Engineering branch: a third project that pushes one specific area (fine-tuning experiment, multi-agent orchestration where it genuinely helps, deeper eval with LLM-as-judge and rubrics, cost optimisation pass with measured before / after numbers).
- For the AI Platform branch: write the unified deployment script that takes either of the two projects as input and produces a live URL, then iterate it toward a small platform skeleton with a config format and a CLI ([20260506_manjunath-yelipeta.md](20260506_manjunath-yelipeta.md) v1 plan, weeks 4-5).
- For the full-stack branch: tighten the spec-driven workflow, expand test coverage, add a third real feature delivered through the agent-team pattern.

Month 6 - Public portfolio and the next sprint.

- LinkedIn / Substack write-up of the strongest project. Eugene Yan is the reference for the cadence (Chandra zoom call 2026-04-28).
- Job applications start running in parallel for anyone targeting a role move - the Ivan Dubograi pattern of "apply early to surface what interviewers actually ask, even before the portfolio feels ready" (Ivan Dubograi zoom call 2026-04-27).
- Plan the next 6-month arc based on what real usage and interviews surfaced. The arc above is one possible path; some Alexes will pivot to Priya territory once their projects are shipping and the new gap is depth rather than first-time experience.

### 6-week sprint plan

The Alex template draws from the patterns in [20260509_daiyaan-shaik.md](20260509_daiyaan-shaik.md), [20260508_aashiesh-siwach.md](20260508_aashiesh-siwach.md), [20260506_manjunath-yelipeta.md](20260506_manjunath-yelipeta.md), [20260427_motasem-salem.md](20260427_motasem-salem.md), [20260427_kushal-kulshreshtha.md](20260427_kushal-kulshreshtha.md), [20260420_grace.md](20260420_grace.md), [20260502_dianne-bronola.md](20260502_dianne-bronola.md).

Week 1:

- Start AI Hero from day 1. Treat the agent-building modules as the foundation for the project work, not a side track. Plan to spend 2 weeks on AI Hero, not the marketed 7 days.
- Run the project-idea brainstorming prompt and surface 5-10 candidates biased toward Alex's domain or daily friction. Pick a coding assistant + paid plan in parallel.
- Optional but common: a small piece of role / market research - pull 10 job descriptions in the target role, summarise responsibilities, watch the AI Engineering Field Guide webinars ([20260506_manjunath-yelipeta.md](20260506_manjunath-yelipeta.md), [20260427_kushal-kulshreshtha.md](20260427_kushal-kulshreshtha.md), Ivan Dubograi zoom call 2026-04-27).

Week 2:

- Finish AI Hero. Treat day 7's deployed RAG on the course default data as the foundation pattern - not the portfolio piece.
- Run the fit-check prompt on the top 1-2 candidate projects and pick one. Write a one-paragraph project card (user / input / output / what "useful" looks like).
- Secure the corpus or dataset the project needs.

Week 3:

- Build the simplest working end-to-end version on Alex's own corpus. Functions first as plain Python, agent loop on top. Deploy or run as a CLI / Streamlit page that Alex uses daily during the rest of the sprint.

Week 4:

- Build an eval set of 20-50 representative inputs with a notion of what "correct" looks like. LLM-as-judge for the open-ended cases, assertion-style checks for the deterministic ones.
- Use the eval set to compare two or three retrieval / chunking / prompt variants. Stop tuning when the differences are small.

Week 5:

- Add monitoring (Logfire or equivalent). Confirm an end-to-end trace from user input to final answer is readable.
- Deploy - small VM, Render, Fly.io, Hugging Face Space, AWS Lambda - whichever fits. Wire up GitHub Actions so the eval set runs on every push and blocks regressions.

Week 6:

- Polish: README that covers problem, architecture, eval results, run instructions. Short walkthrough or recording if energy allows.
- Demo in the AI Shipping Labs Slack `#plan-sprints` channel.
- Decide the next sprint: deepen this project, second project, or pivot direction.

### Why this plan fits - worked examples

Daiyaan Shaik ([20260509_daiyaan-shaik.md](20260509_daiyaan-shaik.md)) - data lead at a fintech startup, 5-8 hr/week, ADHD, alternating theory-then-build cadence requested.

- AI Hero in weeks 1-2 mirrors the Zoomcamp shape he explicitly asked for. He named the alternating "short focused theory block, then build that exact concept" cadence as what worked for him in DE Zoomcamp and MLOps Zoomcamp; AI Hero's day-by-day modules give each week a concept then a build on that concept.
- Forcing the project pick in week 1 directly targets his stated analysis-paralysis trigger ("wanting to understand too much before building", "comparing too many tools", "no hard deadlines makes it worse"). The brainstorming gist plus the four-criterion fit-check turns the pick into a 1-week deliverable rather than an open-ended browse.
- One project across the full sprint suits his already-shipped LLM "second brain" history. He has a Karpathy-style Obsidian + Claude + NotebookLM workflow running and could easily start a parallel build; the plan's explicit "one project, not three" rule names that exact failure mode and removes it.
- The week-4 eval set is where his stated fundamentals goal (embeddings, RAG internals, evaluation, agents/tool calling) gets applied rather than studied. He asked to close the gap from "I followed the tutorial" to "I built my own version that I understand end to end"; eval-on-your-own-corpus is the week where that gap closes.
- Fixed weekly check-ins and Slack updates match the ADHD-driven preference he flagged ("fixed cadence is better than flexible") and the demo-based milestone format he asked for in intake.

Manjunath Yelipeta ([20260506_manjunath-yelipeta.md](20260506_manjunath-yelipeta.md)) - traditional ML engineer pivoting to AI Engineer, 8-10 hr/week, jobless and sole bread-earner.

- The week-1 role-research block (10 AI Engineer job descriptions plus the AI Engineering Field Guide webinars) addresses his stated dilemma between AI-first roles and AI-support / Platform roles. He had a difficult prior role with no eval culture and was wary of repeating it; pulling real job descriptions is the cheapest way to test whether the current AI Engineer market actually looks like the one that burned him.
- Building one project end to end - rather than the v1 plan's two projects plus a platform skeleton - reflects the feedback he sent on 2026-05-12 after doing his own role research and shifting toward AI Engineering for the immediate market. One deployed project at 8-10 hr/week is honest for someone job-searching as the sole bread-earner.
- Week 4's eval set with a failure-mode breakdown maps directly to the strength he asked the plan to make visible ("Evaluation and failure mode analysis" from his ML work). The bridge from his old skills to LLM systems runs through the part he is already strong at.
- Week 5 carves out a cost-and-latency optimization pass because Manjunath flagged it explicitly in his feedback and AI Hero does not cover it. The logging from week 4 supplies the measurement data, so the optimization week is real numbers rather than guesswork.
- Docker, Kubernetes and DevOps self-study sit in parallel outside the 8-10 hour budget. This preserves the AI Platform direction he names as his long-term end goal without compromising the AI Engineering sprint deliverable that the job search actually needs first.

### Plans that exemplify this persona

- [Daiyaan Shaik](20260509_daiyaan-shaik.md) - data lead at a fintech startup, MLOps Zoomcamp graduate, 5-8 hr/week, alternating theory-then-build cadence requested.
- [Aashiesh Siwach](20260508_aashiesh-siwach.md) - UK-based ML engineer with shipped retrieval pipelines, hard end-of-summer 2026 deadline for a full-time AI/ML role.
- [Manjunath Yelipeta](20260506_manjunath-yelipeta.md) - traditional ML engineer pivoting to AI Engineer (immediate market) with AI Platform as the long-term goal, 8-10 hr/week, jobless and sole bread-earner.
- [Vishnu](20260429_vishnu.md) - 5-agent Medicare plan recommender with V1 nearly done, 6-10 hr/week, needs structure + a quick win in week 2 to carry momentum.
- [Motasem Salem](20260427_motasem-salem.md) - ML engineer who wants AI-assisted full-stack development via spec-driven agent teams, 10-15 hr/week.
- [Kushal Kulshreshtha](20260427_kushal-kulshreshtha.md) - engineer transitioning to AI engineering, targeting Europe / relocation / remote roles - filter companies first, pick a domain, mine tech blogs for 10 typical problems.
- [Grace](20260420_grace.md) - Stockholm iOS engineer with 7 years experience, ~10 hr/week, wants clarity through one shipped end-to-end project.
- [Dianne Bronola](20260502_dianne-bronola.md) - iOS / platform engineer, 10-15 hr/week, Learning Companion Agent capstone, "manual workflow first, agent second" build pattern.

## Priya - The Improver

Only two plans are tagged Priya in the current data: [Juan Perez Prim](20260508_juan-perez-prim.md) and [Nirajan Acharya](20260420_nirajan-acharya.md). The interviews add three more Priya signals (Chandra, Luciano Pecile, anonymous-participant-april). The template below is therefore the lightest-sourced of the four - treat it as provisional and refine as more Priya plans land.

### Starting point

- Already has at least one shipped AI project, often with a non-trivial stack. Juan has [amr_ai](https://github.com/juanpprim/amr_ai), a PydanticAI + ChromaDB + BioBERT hybrid-retrieval RAG over WHO/CDC/FAO/PubMed sources, scored 26 on the Maven Buildcamp submission ([20260508_juan-perez-prim.md](20260508_juan-perez-prim.md)). Nirajan topped the Buildcamp Cohort 2 leaderboard and has a deployed AI project ([20260420_nirajan-acharya.md](20260420_nirajan-acharya.md)). Chandra has "gotten good at Kiro and is picking up speed with Claude Code" and is asking about inference optimisation ([../interviews/chandra.md](../interviews/chandra.md)). The build skill is there; the gap is elsewhere.
- The gap is production / depth, not first-time AI experience. Juan asked specifically for help with system design, Dockerisation, scalability, security, GitHub Actions ([20260508_juan-perez-prim.md](20260508_juan-perez-prim.md)). Nirajan wants "production-level standards: system optimization, handling edge cases, advanced evaluation, team-based development environments" ([20260420_nirajan-acharya.md](20260420_nirajan-acharya.md)). Luciano Pecile is asking about reliable copilots, eval frameworks, integration into existing products ([../interviews/luciano-pecile.md](../interviews/luciano-pecile.md)).
- Time budget is typically moderate-to-light, around what a Priya can carve out from a full-time AI / ML / DS lead role. Juan 5-10 hr/week ([20260508_juan-perez-prim.md](20260508_juan-perez-prim.md)). Nirajan's 30-40 hr/week is exceptional and tied to his scholarship-supported job-search push.
- Tendency to under-specify the target state. Nirajan's intake was full of phrases like "production-ready AI agents" and "industry workflows" without a concrete build plan; the core internal recommendation was "describe current state, describe target state, work the gap" ([20260420_nirajan-acharya.md](20260420_nirajan-acharya.md)). Priya often needs help defining what "better" actually means before the sprint can be sized.
- Already a community contributor in some form. Juan met Alexey through Maven and joined to share tips and collaborate ([20260508_juan-perez-prim.md](20260508_juan-perez-prim.md)). Nirajan teaches as well and gets reused course material permission ([../1x1/2026-04-27-nirajan-acharya-summary.md](~/git/zoom-calls/1x1/2026-04-27-nirajan-acharya-summary.md)). Chandra wants to lead community sessions on MCP ([../1x1/2026-04-28-chandra-yarlagadda-summary.md](~/git/zoom-calls/1x1/2026-04-28-chandra-yarlagadda-summary.md)).

### 6-month plan

Month 1 - Define the target state, ship the production layer on the existing project.

- Write down the project's current state and target state in concrete terms. This is the recommendation that ran through both Priya plans - Juan's plan starts from "you have the project, the missing piece is deployment + monitoring + eval"; Nirajan's plan starts from "describe both states before doing anything".
- Dockerise the existing project, pick a deployment target (private Hugging Face Space, small VM, AWS Lambda), get a live URL with HTTPS and basic auth so it can be shared with 5-10 trusted users ([20260508_juan-perez-prim.md](20260508_juan-perez-prim.md)).

Month 2 - Eval + monitoring on the existing project.

- Replicate a known pattern (Juan's plan points at the Buildcamp monitoring + evaluation workshop) on the existing project. 20-50 representative questions wired into CI, monitoring with Logfire or equivalent, regression gating on every push.
- Iterate on retrieval / reranker / prompt variants using the eval set as the scoreboard.
- Polish the README, architecture diagram, and "how this was built" page. The portfolio piece is now real.

Month 3 - Real users.

- Open the project to a small group (Juan's "five colleagues", Nirajan's first community pilot of the cybersecurity chatbot in [../1x1/2026-04-27-nirajan-acharya-summary.md](~/git/zoom-calls/1x1/2026-04-27-nirajan-acharya-summary.md)). Real usage surfaces the next backlog much faster than synthetic eval ever does.
- Capture feedback into the eval set so it tightens with real signal.

Month 4 - Depth on the production-engineering side.

- Pick one production-engineering area that the existing project genuinely needs and deepen it. Common candidates: cost / latency optimisation (Manjunath flagged this, applies the same to Priya), durable execution, observability beyond logs, auth and multi-tenant data isolation, more aggressive caching.
- For Priyas leaning toward AI Platform - sketch what is shared between two of their projects and start writing a unified deployment script ([20260506_manjunath-yelipeta.md](20260506_manjunath-yelipeta.md) v1 plan is a Priya-shaped arc once Manjunath has more LLM mileage).

Month 5 - Second project or vertical extension.

- Either a second project that uses the same scaffolding (faster build, same eval / monitoring discipline), or a vertical extension of project 1 (a multi-agent split where it now genuinely helps, generalisation to a different topic - Juan's stated long-term goal is generalising `amr_ai` to other learning topics).
- Community contribution starts paying off here: peer review, seminar presentations, leading a topic session ([../interviews/chandra.md](../interviews/chandra.md) MCP session arc).

Month 6 - Public artefacts and direction call.

- Substack / LinkedIn write-ups of the strongest project ([../1x1/2026-04-28-chandra-yarlagadda-summary.md](~/git/zoom-calls/1x1/2026-04-28-chandra-yarlagadda-summary.md) for the cadence pattern: one post per week, collected posts roll up into one long-form article).
- Decide the longer arc: stay applied (more projects), go deeper into a platform direction, or pivot toward a senior IC / consulting / side-product play. Chandra's call is the clearest version of this fork.

### 6-week sprint plan

Drawn from [20260508_juan-perez-prim.md](20260508_juan-perez-prim.md) and [20260420_nirajan-acharya.md](20260420_nirajan-acharya.md).

Week 1:

- Write the current-state vs target-state document. List exactly what the project does today, what it should do by week 6, and what is in scope vs explicitly out of scope. For Priya, this is the highest-leverage exercise of the sprint.
- Dockerise the existing project so another machine can `docker compose up` and reproduce the local experience.
- Pick the deployment host and lock down secrets in env vars or a secret store.

Week 2:

- Ship the first deployed version. URL accessible over HTTPS, basic access control so the link is not openly indexable.
- Decide what the eval set should look like - the rubric, the question shape, the labels.

Week 3:

- Build the eval set: 20-50 representative inputs with expected answer characteristics. Replicate the Buildcamp / known pattern rather than designing from scratch.

Week 4:

- Wire the eval set into GitHub Actions on every push. Failing scores block deploy. The goal is regression visibility, not a high absolute number.
- Add monitoring on the deployed site. End-to-end trace from user input to model answer must be readable.

Week 5:

- Iterate using the eval set as the scoreboard. One or two principled experiments (different embedding model, reranker tweak, chunking change, prompt variant).
- Polish the README, architecture diagram, "how this was built" page.

Week 6:

- Open the deployed site to a small trusted group. Capture feedback back into the eval set.
- Demo in `#plan-sprints`.
- Decide the next sprint: deepen, generalise, or start a second project.

### Why this plan fits - worked examples

Juan Perez Prim ([20260508_juan-perez-prim.md](20260508_juan-perez-prim.md)) - Madrid data science lead with `amr_ai` already built, 5-10 hr/week.

- Week 1's Docker step (one `docker compose up` reproduces the chat locally) responds directly to his intake ask: "Dockerization, scalability, security, and workflows for deploying code updates via GitHub Actions". The sprint reads his question back to him as a sequence rather than a list.
- Weeks 3-4 replay the Buildcamp monitoring + evaluation workshop on `amr_ai` instead of designing eval from scratch. He attended that workshop already; the sprint turns it from a watched recording into a CI-gated eval set on his own corpus. This matches the "concept → tools → tests → monitoring → evolution" Buildcamp arc that he has not yet finished for his own project.
- Week 6's "share with five colleagues" is exactly the success criterion he named in intake. The sprint does not invent a portfolio goal; it operationalises the one he already articulated.
- The "no rebuilding the frontend, no gamification, no generalisation" guardrail addresses the long idea list he brought to the intake call (diagrams, images, videos in chat, points for flashcards, generalising to other topics). At 5-10 hr/week with a full-time DS lead role and family responsibilities, those would each cost the deployment milestone.
- Pairing with Manjunath is suggested because Manjunath is building a deployment platform that takes a project as input and produces a live URL - the exact capability Juan needs for `amr_ai`. The pair is two sides of the same problem rather than a generic accountability buddy.

### Plans that exemplify this persona

- [Juan Perez Prim](20260508_juan-perez-prim.md) - Madrid-based data science lead, `amr_ai` already built, sprint is about adding the production layer (deployment, monitoring, eval) rather than building.
- [Nirajan Acharya](20260420_nirajan-acharya.md) - Buildcamp Cohort 2 leaderboard top, 30-40 hr/week, deployed AI project already, needs sharper focus and a clearer target state.

## Sam - The Technical Professional Moving to AI

### Starting point

Sam is the most varied persona in the current data. Six plans plus several zoom calls show several distinct sub-shapes - data analyst, analytics engineer, non-programmer marketing / community team member, cloud data engineer, domain expert with a side-project itch. The common thread is the gap between "I can write scripts that do data work" and "I can build and ship software systems".

- Can write code for data work but not for systems. Daniel Sa Earp is "fine with functions, data analysis libraries like pandas, numpy" but struggles with "classes, project structure, environments, APIs, deployment" ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md)). Jakob has basic Python and describes most of his code as "vibe coded" with AI assistance, finding the Buildcamp "way too technical" ([20260420_jakob-zischka.md](20260420_jakob-zischka.md), [../1x1/2026-04-23-jakob-zischka-summary.md](~/git/zoom-calls/1x1/2026-04-23-jakob-zischka-summary.md)). Valeriia is explicitly a non-programmer working in content marketing ([20260506_valeriia-kuka.md](20260506_valeriia-kuka.md)). Sergey Sedler (zoom call 2026-04-24) is a procurement / foreign-trade professional with zero developer background who has built a 1,500-line RAG over pineapple specs using Ollama and ChatGPT-5 copy-paste.
- Time budget tends to fragment around a day job and life. Valeriia 3-4 hr/week ([20260506_valeriia-kuka.md](20260506_valeriia-kuka.md)). Koray 20 hr in week 1 and 2 hr/week after the freelance gig starts on May 4 ([20260430_koray-can-canut.md](20260430_koray-can-canut.md)). Daniel 10-15 hr/week as a worst case ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md)). Sai 15 hr/week with more on weekends ([20260502_sai-kumar-g.md](20260502_sai-kumar-g.md)). Carlos and Diogo around 5-10 hr/week. The range is wider than any other persona.
- Often arrives with a concrete project idea but no engineering shape around it. Sai has a thorough conceptual design for a News Event Reminder Telegram bot (three flows, four tables, folder layout) but no code yet ([20260502_sai-kumar-g.md](20260502_sai-kumar-g.md)). Carlos has a personal-agent-for-SMEs idea with a clear two-tool split ([20260420_carlos-pumar.md](20260420_carlos-pumar.md)). Koray has a working deployed Telegram nutrition bot on Cloud Run + BigQuery ([20260430_koray-can-canut.md](20260430_koray-can-canut.md)). Daniel has a longer-term side project (corpus-grounded agent + website + login + subscription for his wife's audiovisual education business) that he is deferring until after the sprint ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md)).
- Uses AI heavily as a coding assistant - sometimes too heavily. Daniel flagged this himself: "Claude does the project structure, Docker, etc., but I would like to be able to do it myself, or at least have a good understanding of what AI is doing and why. I don't want to just use AI like a black box" ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md)). Koray's gap is similar - "Python still needs improvement, LLM does all the coding, I just try to understand what it's doing" ([20260430_koray-can-canut.md](20260430_koray-can-canut.md)).
- Wants "structure, accountability, and fun" - Dianne's phrasing for the DE Zoomcamp experience she wants to recreate ([20260502_dianne-bronola.md](20260502_dianne-bronola.md), but Dianne is Alex; the framing fits Sam too). Jakob's main blocker is "lack of a clear path of what will be achieved when" ([20260420_jakob-zischka.md](20260420_jakob-zischka.md)).

Sam is the persona where the standard AI Engineering arc takes longest because the engineering scaffolding has to be built alongside. The honest framing from [personas.md](../personas.md): "the fastest path for Sam is to build coding comfort first, then the AI content becomes much more valuable".

### 6-month plan

Month 1 - Engineering shape, not AI depth.

- Pick a project where Sam can carry a familiar skill (data work for the analyst sub-shape, a daily annoyance for the non-programmer sub-shape) and use it as the carrier for the missing engineering pieces - Python project structure, virtual environments, Docker, an API client, an entry point. The Daniel plan ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md)) is the clearest example: GitHub-issues ingestion to Elasticsearch as the engineering-shape build, with LLM Zoomcamp in June as the AI track that follows.
- For non-programmer Sams (Valeriia), AI Hero is the entire scope of month 1 - one module per week, with a coding assistant as the on-call tutor ([20260506_valeriia-kuka.md](20260506_valeriia-kuka.md)).
- Foundational courses run in parallel where they help. Alexey's Python course for Jakob ([20260420_jakob-zischka.md](20260420_jakob-zischka.md)). The first module of Data Engineering Zoomcamp as a Docker reference for Daniel.

Month 2 - First AI integration on top.

- Add one LLM API call to the project. Smallest possible end-to-end flow: input -> API -> useful output ([20260420_jakob-zischka.md](20260420_jakob-zischka.md) week 4 pattern).
- For Sams who already shipped something (Koray, Sai once the build is rolling): start the eval pipeline rather than chasing more features.

Month 3 - Eval and observability, treated as conceptual work.

- The eval pattern is the same shape as Alex's month 2, but Sam's bottleneck is rarely the implementation - it is owning the conceptual work (defining "good", scenario design, rubric writing). Koray's plan front-loads this into his high-time week 1 so the 2-hour weeks can be implementation-only with a coding agent as fallback ([20260430_koray-can-canut.md](20260430_koray-can-canut.md)).
- "Stop using AI as a black box" becomes an explicit project rule: when AI generates code, read it line by line, ask for explanations, rewrite at least one part by hand ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md)).

Month 4 - LLM Zoomcamp / structured AI track.

- LLM Zoomcamp (re-recorded version starting June 2026, with five workshops mapped to modules) is the natural carrier here for Sams who came up through the engineering-shape sprint. The 6-week sprint project can grow into the Zoomcamp project rather than competing with it ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md), [20260508_aashiesh-siwach.md](20260508_aashiesh-siwach.md)).
- Office hours specifically for community members doing LLM Zoomcamp is the small-cohort substitute for trying to support all public Zoomcamp participants directly ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md) meeting notes).

Month 5 - Second project or deeper agent.

- Layer agentic behaviour onto the existing project, or pick a second project that uses the same scaffolding. Sai's News Event Reminder bot starts with plain functions and introduces the freshness-check agent only in week 4 of the sprint ([20260502_sai-kumar-g.md](20260502_sai-kumar-g.md)); month 5 of the longer arc is where Sams who started with no agent now layer one in.
- The deferred long-term side project (Daniel's audiovisual chatbot platform, Carlos's SME agent extension, Diogo's other two candidate projects) becomes realistic here, not before.

Month 6 - Decision point.

- Sam often arrives with a career-direction question that the sprint deliberately parked. Daniel wants to decide between analytics engineer and data / AI engineer; Koray asked about a junior-AI-engineer move; Sai wants AI Engineer interview prep. By month 6, with one or two shipped projects and demonstrated engineering muscle, the question becomes answerable from evidence rather than speculation ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md), [20260430_koray-can-canut.md](20260430_koray-can-canut.md), [20260502_sai-kumar-g.md](20260502_sai-kumar-g.md)).
- For non-programmer Sams who finished AI Hero: the capstone is the demo, and the next sprint picks one DataTalks.Club-style automation idea with the engineering basics in place ([20260506_valeriia-kuka.md](20260506_valeriia-kuka.md)).

### 6-week sprint plan

The Sam sprint has the widest variance across plans, because the right week 1 depends heavily on Sam's specific sub-shape. The template below is the modal pattern from [20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md), [20260502_sai-kumar-g.md](20260502_sai-kumar-g.md), [20260430_koray-can-canut.md](20260430_koray-can-canut.md), [20260420_jakob-zischka.md](20260420_jakob-zischka.md), [20260506_valeriia-kuka.md](20260506_valeriia-kuka.md). The most important thing is the explicit anti-pattern: do not start by introducing an agent.

Week 1:

- Conceptual work, not code. For Sams with a project idea: write down what the system should do in plain English - inputs, outputs, data model, success criteria. For Sams without one: brainstorming gist + daily-annoyance notes.
- Pick a coding assistant + paid plan. The free-tier failure mode kills 2-hour weeks faster than any other ([20260430_koray-can-canut.md](20260430_koray-can-canut.md)).
- For the analyst sub-shape: set up the Python project from scratch by hand (uv, virtual environment, pyproject.toml, folder structure). For the non-programmer sub-shape: AI Hero day 1.

Week 2:

- Build the data structure and run the workflow manually. The agent does not enter yet. Sai writes the extraction step as a plain function and saves to the database ([20260502_sai-kumar-g.md](20260502_sai-kumar-g.md)). Dianne processes 3-4 real learning sessions manually into her chosen schema ([20260502_dianne-bronola.md](20260502_dianne-bronola.md), Dianne is Alex but the manual-first principle is universally Sam-suitable). Daniel writes the issues-only ingestion pipeline into Elasticsearch in Docker ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md)).
- For Valeriia-shaped Sams: AI Hero module 2.

Week 3:

- Add the second piece. Update detection + comments ingestion for Daniel; scheduler for Sai; first agent capability automating the most-tedious manual step for Dianne. The arc is "make the manual workflow more capable", not "make it more agentic".
- For non-programmer Sams: AI Hero module 3.

Week 4:

- Introduce the agent. Wrap the existing plain-function tools into an agent that decides when to call which one. Sai's freshness-check agent with two tools, logging to `agent_runs` ([20260502_sai-kumar-g.md](20260502_sai-kumar-g.md)). Koray's LLM judge built against manually-labelled scenarios ([20260430_koray-can-canut.md](20260430_koray-can-canut.md)).
- For non-programmer Sams: AI Hero module 4 and the call on whether to keep any stretch goal.

Week 5:

- Tests and monitoring on the most-stake scenarios. Sai's end-to-end tests for "blurry photo asks for clearer image", "non-food image returns parse error", "duplicate within seconds is handled" ([20260502_sai-kumar-g.md](20260502_sai-kumar-g.md)). Koray implements one or two agentic decisions designed in week 1 ([20260430_koray-can-canut.md](20260430_koray-can-canut.md)).
- For non-programmer Sams: AI Hero capstone module.

Week 6:

- Wrap to demoable state. README that explains architecture, schema, how to run it, what each part does. Tag a release.
- Demo in `#plan-sprints`. The meta-deliverable for Sam is "the increase in engineering confidence" - the project is the visible artefact, the confidence is the actual outcome ([20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md)).
- For Sams who deferred a side project: decide whether the next sprint is the side project or something else.

### Why this plan fits - worked examples

Diogo Valente Polónia ([20260502_diogo-valente-polonia.md](20260502_diogo-valente-polonia.md)) - industrial / data engineer at the European Environment Agency, ~5-10 hr/week.

- Picking the project for him in week 1 (default: expert-elicitation single agent) is the entire point. His own stated main blocker was time to decide between three candidate ideas - this is choice paralysis named back to him, and the sprint resolves it with a default plus permission to switch only if he strongly prefers one of the other two.
- Dropping the multi-agent framing in favour of one agent matches the "domain expert who manages projects rather than codes day to day" sub-shape. He no longer codes most of the day; a single agent with a clear tool list is something he can build, debug and understand at 5-10 hr/week, whereas multi-agent message passing would silently consume the budget.
- Functions before agent (weeks 2-3 implement data fetchers, expert-perspective prompts and the synthesis step as plain Python, then week 3 wraps them) directly serves his intake goal: "test it himself first to understand the possibilities before he can manage or outsource such projects later". Plain functions are the level at which he can read what is happening.
- "Used at work at least once a week" as the week-6 success bar matches the personal-productivity goal he named (no promotion or job change in scope; he started his current job two months ago). Portfolio polish is deliberately not the metric.
- The discussion-based weekly check-in format ("someone I can ask 'is this feasible'") is exactly what he asked for in the intake call - the sprint's weekly cadence is built around that rather than around demo-day prep.

Sai Kumar G ([20260502_sai-kumar-g.md](20260502_sai-kumar-g.md)) - Azure cloud data engineer with two-plus years' experience, 15 hr/week plus weekends, News Event Reminder Telegram bot already conceptually designed.

- The plan skips concept-week work because Sai already has three flows, four tables and a folder layout written down. Week 1 starts at the Telegram bot skeleton instead of architecture, which respects the conceptual work he has done without rehashing it.
- "Build the agent yourself, do not hand it to Claude Code" is named explicitly because his intake said the new skill he wants is "agents with tool calling, evaluation, and product thinking". Letting a coding assistant write the agent loop would skip the exact lesson he signed up for.
- The week-by-week shape (extraction function in week 2, scheduler in week 3, freshness-check agent introduced only in week 4) is the Buildcamp "concept → tools → tests → monitoring → evolution" arc he is already enrolled in. The bot stays in sync with what the course covers each week, so course content directly reinforces the sprint.
- Week 5's specific test scenarios (article with one clear event, no future-dated events, postponed event, uncertain event) come from the failure paths he himself sketched in the intake. The plan does not invent acceptance criteria - it returns his own design as a test list.
- 15 hr/week with weekend overflow makes the agent-by-hand discipline realistic. The budget is there for him to actually write the agent loop and tool definitions himself rather than delegating them, which is the only configuration in which the plan delivers the skills he named.

### Plans that exemplify this persona

- [Daniel Sa Earp](20260506_daniel-sa-earp.md) - Brazilian analytics engineer, SQL / dbt, the canonical "scripts-to-systems" gap. Sprint is the engineering-shape build before LLM Zoomcamp in June.
- [Valeriia Kuka](20260506_valeriia-kuka.md) - non-programmer in DataTalks.Club content marketing, 3-4 hr/week. AI Hero is the entire scope of the sprint.
- [Sai Kumar G](20260502_sai-kumar-g.md) - Azure cloud data engineer (2+ years), thorough conceptual project plan but no code. Sprint syncs to the Buildcamp arc: concept -> tools -> tests -> monitoring -> evolution.
- [Carlos Pumar](20260420_carlos-pumar.md) - economist at German Savings Banks with a personal-agent-for-SMEs idea. Sprint turns the idea into a scoped build plan and a first prototype.
- [Jakob Zischka](20260420_jakob-zischka.md) - in career transition, Applied AI student, found the Buildcamp "too technical". Python course + AI Hero in parallel, one small AI app at the end of week 6.
- [Koray Can Canut](20260430_koray-can-canut.md) - data analyst / analytics engineer with a deployed Telegram nutrition bot on Cloud Run + BigQuery. Sprint focuses on building the eval pipeline. Tight 2 hr/week budget after week 1 dictates a coding-agent fallback.

[Diogo Valente Polónia](20260502_diogo-valente-polonia.md) is tagged Sam provisionally - he is an industrial / data engineer at the European Environment Agency who manages projects rather than codes day to day. He fits the "domain expert moving deeper into AI" sub-shape rather than the analytics-engineer sub-shape.

## Taylor - The Research-to-Engineering Transitioner

Only two plans are tagged Taylor: [Luca](20260503_luca.md) and [Edu Gonzalo Almorox](20260420_edu-gonzalo-almorox.md). The interview / zoom data is even thinner. The template below is therefore the least-grounded of the four - treat it as provisional. Add more Taylor plans before treating it as canonical.

### Starting point

- Strong AI / ML / research background that does not translate directly to shipped software. Luca has ~22 years in public and private research / education institutes in Italy, is preparing the Google Generative AI Leader (GAIL) certification, and runs his own coding agent (Hermes) on Oracle Cloud A1 + Ollama on a Minisforum with RTX 3090, connected via Tailscale ([20260503_luca.md](20260503_luca.md)). Edu is a senior data scientist in health economics in Madrid who has built RAG and agentic systems at PoC level but has not owned full deployment ([20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md)).
- Articulate about model behaviour but vague about production. Edu names the gap clearly: "I have managed to build a RAG/Agent system that delivers very decent results. However, I have missed the last step - deploy it as a solution that can be accessible to people and that is scalable" ([20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md)). Luca's prioritisation question is about scope control rather than technical feasibility, and his existing two AI Dev Tools Zoomcamp capstones are both unfinished ([20260503_luca.md](20260503_luca.md)).
- Often unemployed or in transition. Luca is unemployed since end of February 2026 and is targeting AI Engineer / technologist / AI systems roles in research institutes. Edu is currently employed but actively searching for positions with a greater AI component.
- Time budget tends to be the largest of any persona because the job hunt and the sprint reinforce each other. Luca 20 hr/week ([20260503_luca.md](20260503_luca.md)). Edu 8-10 hr/week is the lower end ([20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md)).
- The portfolio question matters - hiring committees for AI Engineer / technologist roles in research-adjacent contexts value both rigour and pragmatism, and the publication / theoretical credibility on its own is not enough ([20260503_luca.md](20260503_luca.md)). Lead with "research scientist who ships production-grade AI tooling", not "researcher transitioning to AI engineering".

### 6-month plan

Month 1 - Finish dockerising and deploy what already exists.

- The opening move for Taylor is to take the existing PoC / capstone / notebook prototype and put it behind an HTTPS URL with basic access control. Edu's plan starts here ([20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md)). Luca's plan does the same shape with Hermes as the runtime in weeks 1-2 ([20260503_luca.md](20260503_luca.md)).
- Lock down secrets. Pick a deployment target that does not bankrupt a personal project (AWS Lambda for Edu, a small VM or private Hugging Face Space otherwise).

Month 2 - Tests, basic monitoring, evaluation harness.

- Add tests covering the main workflow. Edu's week 3 covers this ([20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md)).
- Add basic monitoring so failures are visible.
- Build a lightweight evaluation / improvement loop. The principle Edu names is "include results of the evaluation so the system learns about past errors and gets better" - that is the production-side version of the loop a researcher already understands experimentally.

Month 3 - CI/CD, the standalone reimplementation, the LinkedIn series.

- GitHub Actions runs tests automatically and deploys to a dev environment on every push. Production deploy stays manual to mirror a realistic engineering setup ([20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md)).
- For Taylors with an existing AI-platform-shaped tool in the loop (Luca + Hermes): reimplement as a standalone Python application using an agentic framework of choice (LangChain / LangGraph, LlamaIndex, pydantic-ai, smolagents). The framework's loop replaces the platform's loop. This is the AI Engineering portfolio piece ([20260503_luca.md](20260503_luca.md) phase 3).
- Public LinkedIn series with one short post per week is the brand-building track. Six posts at the end of a sprint give a credible online presence. The cadence matches Chandra's Substack track ([../1x1/2026-04-28-chandra-yarlagadda-summary.md](~/git/zoom-calls/1x1/2026-04-28-chandra-yarlagadda-summary.md)).

Month 4 - Second project or deepening.

- Either a second end-to-end project as an additional portfolio signal (Edu plan), or a deepening of the first project with the same arc compressed.
- This is the month where Taylor starts feeling the platform / depth question: more projects or deeper on one?

Month 5 - Direction-specific deepening.

- For the AI Engineer track: deeper agentic patterns, better eval (LLM-as-judge with rubrics), cost / latency optimisation.
- For the technologist / research-institute track: integration with domain data sources, sharper write-up of the trade-offs and architectural decisions, the rigour-plus-pragmatism story.
- For the MLOps track that Taylor sometimes drifts toward: Terraform, more deployment paths, dev / prod split. Edu's plan flags Terraform as the next layer ([20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md)).

Month 6 - Public artefacts and applications.

- Tagged release on GitHub, short demo video, README that hiring committees can read.
- Active job applications using the AI Engineering Field Guide ([github.com/alexeygrigorev/ai-engineering-field-guide](https://github.com/alexeygrigorev/ai-engineering-field-guide)) to harvest the responsibilities and language to mirror in CV and LinkedIn ([20260503_luca.md](20260503_luca.md)).

### 6-week sprint plan

Drawn from [20260503_luca.md](20260503_luca.md) and [20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md).

Week 1:

- Concept and data design before any code or configuration. Write a one-page note on what is in the data, the five real questions the system should answer, and how the answer should come back. For Edu: finish dockerising the existing capstone and pick the first deployment target so the hosting decision does not drag ([20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md)). For Luca: configure Hermes (or the operational agent platform) as the runtime with a vault-search tool and a first system prompt ([20260503_luca.md](20260503_luca.md)).
- First LinkedIn post: "why I am building this and how I will work".

Week 2:

- For Edu: deploy the current project to a simple cloud target so it is no longer stuck on the laptop. Capture rough deployment notes and blockers.
- For Luca: finish phase 1 - the working version answers the five real questions end to end as a Hermes use case in daily use.
- Second LinkedIn post.

Week 3:

- Tests and basic monitoring. Fix the highest-friction issues discovered during deployment.
- For Luca: document the working version - what the tool does, what the prompt looks like, what the failure modes are. Pick the agentic framework for phase 3 by end of week ([20260503_luca.md](20260503_luca.md) phase 2).
- Third LinkedIn post.

Week 4:

- Add a lightweight evaluation / improvement loop. Document the architecture trade-offs clearly enough that Taylor can explain the system inside out.
- For Luca: start the standalone framework reimplementation - tools as plain functions, framework wires the agent loop, the Hermes use case stays as a reference.
- Fourth LinkedIn post.

Week 5:

- GitHub Actions runs tests automatically and deploys to a dev environment on push. Production deploy stays manual.
- For Luca: finish phase 3 - framework version on par with the Hermes use case on direct lookups, plus an evaluation script grading both side by side.
- Fifth LinkedIn post.

Week 6:

- Polish the deployed version, close the biggest engineering gaps, sketch the next layer (Terraform for cleaner infra, or a second project brief in a target company / domain).
- Tagged release, README, short demo video. Sixth LinkedIn post.
- Decide the next sprint and the job-application cadence.

### Why this plan fits - worked examples

Luca ([20260503_luca.md](20260503_luca.md)) - Italian researcher (~22 years), unemployed since end of February 2026, preparing GAIL certification, runs Hermes on Oracle Cloud A1 + Ollama on a Minisforum with RTX 3090, 20 hr/week.

- The three-phase shape (Hermes use case in weeks 1-2, document in week 3, framework reimplementation in weeks 4-5) addresses his stated main blocker explicitly: "Prioritisation and scope control". Phase 1 forces an early shipped artefact so Chat with My Notes does not join the two unfinished Zoomcamp capstones he already has on his record.
- Phase 3 is non-negotiable because Luca named the job target as "AI Engineer or technologist role in a research institute" and said he wants to demonstrate building an agent end to end, "not just configuring Hermes well". The sprint deliberately separates the runtime he already has (Hermes) from the code he needs to write himself in a framework (pydantic-ai or smolagents, which he is leaning toward).
- The five-real-questions seed (week 1's concept doc, becoming the golden eval set in week 5) suits his vault situation. His Obsidian vault was created with subfolders but had one test note at intake time; five real questions is the only honest evaluation available before the vault is populated, and it scales as he fills the vault during the sprint.
- The weekly LinkedIn series is positioned as a portfolio artefact, not extra work. He flagged that he wants to "publish progress as a LinkedIn series with Hermes as the common thread" and asked for community feedback before publishing each post. The sprint cadence (one post per week, six total at the end) matches what he proposed.
- "Lead with the combination, not the transition" framing addresses his stated question about positioning toward AI Engineer / technologist roles without losing academic credibility. With ~22 years of research credentials and no AI engineering portfolio, the gap-closing artefact is the shipped agent, not more credentials - the plan names that explicitly.

Edu Gonzalo Almorox ([20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md)) - senior data scientist in health economics, Madrid, 8-10 hr/week.

- Starting with finishing the Buildcamp capstone dockerisation and a chosen deployment target in week 1 reflects his own framing: he said his projects "do not go beyond my laptop and remain local", and his Buildcamp capstone was already in the middle of dockerisation. The sprint picks up where he stopped rather than asking him to start over.
- The evaluation / improvement loop in week 4 (capture results so the system "learns about past errors and gets better") is a near-verbatim restatement of what he said he most wants hands-on practice with - "the end of the pipeline ... how I can improve the app by including results of the evaluation".
- GitHub Actions running tests on push, with production deploy kept manual (week 5), produces the engineering-discipline signal he asked for. He said he wants to move from "this guy has some understanding of how agents work" to "this guy understands how an agent works because the agent he built shows reliable results and it is deployed" - automated test/dev deploy plus a manual production gate is the visible artefact of that distinction.
- Cost containment is built into the deployment choice (AWS Lambda as the simple starting platform). He flagged that he is funding the project out of pocket and wants to "keep an eye at the costs"; a serverless target with a free tier matches the constraint without forcing a platform-engineering detour.
- Terraform sits in week 6 as an optional next layer rather than a required deliverable. At 8-10 hr/week alongside a senior consultancy role, deploy + tests + monitoring + eval already fills the sprint; Terraform is the next-sprint seed, not the current one.

### Plans that exemplify this persona

- [Luca](20260503_luca.md) - Italian researcher (~22 years), unemployed since end of February, preparing GAIL certification, running Hermes on his own infrastructure. Three-phase sprint: configure Hermes as the runtime (weeks 1-2), document and understand (week 3), reimplement as a standalone framework application (weeks 4-5), demo (week 6).
- [Edu Gonzalo Almorox](20260420_edu-gonzalo-almorox.md) - senior data scientist in health economics (Madrid), strong AI side but PoC-level deployments. Sprint focuses on finishing and deploying the Buildcamp capstone with tests, monitoring, CI/CD, and an evaluation loop.

## Cross-persona patterns

These hold across every persona, not just one:

- Every sprint ends in a shipped artefact at week 6 - a demo, a deployed URL, a README, a Slack post. The artefact bar varies by persona but the principle is invariant.
- AI Hero is the foundation for anyone without LLM / agent experience. It is the recommendable free entry point. It is sized as 7 days but realistically takes 2 calendar weeks for most members at evenings-and-weekends pace, and longer for non-programmer Sams.
- Pick one project. Every plan repeats this. Two projects in parallel is the single most reliable way to ship neither.
- Brainstorming gist + fit-check prompt is the standard tool for picking a project ([alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1](https://gist.github.com/alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1)). Voice / dictation mode with ChatGPT or Claude is the recommended brainstorming format.
- Functions first, agent second. Every Sam, Alex, and Taylor plan repeats this in some form. Plain Python functions you can call from a REPL come before the agent loop wraps them.
- Eval week is always there, typically week 4 or 5. 20-50 representative inputs is the standard eval-set size. LLM-as-judge for open-ended cases, assertion-style checks for deterministic ones.
- Coding assistant + paid plan in week 1. Free tiers do not survive a 6-week sprint. Claude Code, Codex, or similar - the framework choice matters far less than committing to one.
- One LinkedIn / Substack post per week is the brand-building cadence for anyone whose sprint includes job-search positioning. Six posts at the end of a sprint roll up into one long-form article.
- Weekly check-in in `#plan-sprints`: what shipped, what is blocked, what is next. The cadence is the accountability.
- Real users beat synthetic eval. Even five trusted colleagues using the deployed project generate a more useful backlog than the most thoughtful synthetic eval set ([20260508_juan-perez-prim.md](20260508_juan-perez-prim.md) week 6, Nirajan's pilot in [../1x1/2026-04-27-nirajan-acharya-summary.md](~/git/zoom-calls/1x1/2026-04-27-nirajan-acharya-summary.md) week 5).

## Sources

Personal plans read for this synthesis:

- [20260509_daiyaan-shaik.md](20260509_daiyaan-shaik.md) (Alex)
- [20260508_juan-perez-prim.md](20260508_juan-perez-prim.md) (Priya)
- [20260508_aashiesh-siwach.md](20260508_aashiesh-siwach.md) (Alex)
- [20260506_daniel-sa-earp.md](20260506_daniel-sa-earp.md) (Sam)
- [20260506_valeriia-kuka.md](20260506_valeriia-kuka.md) (Sam)
- [20260506_manjunath-yelipeta.md](20260506_manjunath-yelipeta.md) (Alex)
- [20260503_luca.md](20260503_luca.md) (Taylor)
- [20260502_sai-kumar-g.md](20260502_sai-kumar-g.md) (Sam)
- [20260502_diogo-valente-polonia.md](20260502_diogo-valente-polonia.md) (provisional Sam)
- [20260502_dianne-bronola.md](20260502_dianne-bronola.md) (Alex)
- [20260430_koray-can-canut.md](20260430_koray-can-canut.md) (Sam)
- [20260429_vishnu.md](20260429_vishnu.md) (Alex)
- [20260427_motasem-salem.md](20260427_motasem-salem.md) (Alex)
- [20260427_kushal-kulshreshtha.md](20260427_kushal-kulshreshtha.md) (Alex)
- [20260420_vancesca-dinh.md](20260420_vancesca-dinh.md) (Undetermined, closest to Alex)
- [20260420_carlos-pumar.md](20260420_carlos-pumar.md) (Sam)
- [20260420_jakob-zischka.md](20260420_jakob-zischka.md) (Sam)
- [20260420_nirajan-acharya.md](20260420_nirajan-acharya.md) (Priya)
- [20260420_edu-gonzalo-almorox.md](20260420_edu-gonzalo-almorox.md) (Taylor)
- [20260420_grace.md](20260420_grace.md) (Alex)

Interview files read:

- [../interviews/aashiesh-siwach.md](../interviews/aashiesh-siwach.md), [../interviews/anonymous-buildcamp-participant.md](../interviews/anonymous-buildcamp-participant.md), [../interviews/anonymous-participant-april.md](../interviews/anonymous-participant-april.md), [../interviews/anonymous-survey-responses.md](../interviews/anonymous-survey-responses.md), [../interviews/archie.md](../interviews/archie.md), [../interviews/brad-smith.md](../interviews/brad-smith.md), [../interviews/chandra.md](../interviews/chandra.md), [../interviews/daiyaan-ahmed.md](../interviews/daiyaan-ahmed.md), [../interviews/daniel-ibanez.md](../interviews/daniel-ibanez.md), [../interviews/jakob-zischka.md](../interviews/jakob-zischka.md), [../interviews/juan-perez-prim.md](../interviews/juan-perez-prim.md), [../interviews/koray-can-canut.md](../interviews/koray-can-canut.md), [../interviews/leonor.md](../interviews/leonor.md), [../interviews/lucia.md](../interviews/lucia.md), [../interviews/luciano-pecile.md](../interviews/luciano-pecile.md), [../interviews/marco-teran.md](../interviews/marco-teran.md), [../interviews/scott-degeest.md](../interviews/scott-degeest.md), [../interviews/vancesca-dinh.md](../interviews/vancesca-dinh.md).

1:1 zoom-call summaries read (in `~/git/zoom-calls/1x1/`):

- 2026-03-04-giang-do-summary.md
- 2026-03-23-nikolai-summary.md
- 2026-04-23-jakob-zischka-summary.md
- 2026-04-24-kirill-summary.md
- 2026-04-24-sergey-sedler-summary.md
- 2026-04-27-ivan-dubograi-summary.md
- 2026-04-27-nirajan-acharya-summary.md
- 2026-04-28-bradley-smith-summary.md
- 2026-04-28-chandra-yarlagadda-summary.md
- 2026-04-29-ivan-brigida-summary.md
- 2026-04-30-shrikant-k-summary.md
- 2026-05-12-luciano-pecile-summary.md

Discussion summary scanned (less directly relevant but reviewed): `~/git/zoom-calls/discussions/2026-03-21-claude-ai-chat-summary.md`.

Canonical definitions and template referenced throughout:

- [../personas.md](../personas.md) - the four personas, their starting-points table, and how-to-serve-each notes.
- [_plan.md](_plan.md) - the canonical plan template (Summary, Plan, Internal Context).
- [how-to-use-plans.md](how-to-use-plans.md) - the shareable note that explains how the plan is built and that it is a flexible guideline rather than a contract.
