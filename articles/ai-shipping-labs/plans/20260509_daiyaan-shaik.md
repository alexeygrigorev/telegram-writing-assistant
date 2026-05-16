---
title: "Plan: Daiyaan Shaik"
created: 2026-05-09
updated: 2026-05-09
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Daiyaan Shaik

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: Data lead at a small fintech startup, handling the full lifecycle from ingestion to ML deployment on Databricks. Heavy daily user of Cursor and Claude Code. Already shipped a personal LLM "second brain" (Obsidian + Claude workflow + NotebookLM revision flashcards) following Andrej Karpathy's pattern. Data Engineering Zoomcamp and MLOps Zoomcamp graduate. Missed the AI Engineering Buildcamp deadline, which is why he joined AI Shipping Labs[^1][^2].
- Goal for the next 6 weeks: ship one production-style LLM application (likely RAG-based), fintech-adjacent, with proper evaluation and deployment - one project he can point to publicly, on a deeper-than-tutorial level.
- Main gap to close: moving from "I followed the tutorial / wired up existing tools" to "I built my own version of an LLM application that I understand end to end". His own framing - and the right one for the sprint.
- Weekly time commitment: 5-8 hours consistently, mostly weekday evenings and weekends, around the demanding fintech data-lead role[^2].
- Why this plan is the right next step: Daiyaan has the engineering muscle (data engineering + MLOps) and the AI-tooling habit (Cursor, Claude Code, NotebookLM, Obsidian). He has not yet built one LLM application end to end at the level he wants. AI Hero gives him the agent-building foundation in two weeks. The remaining four weeks turn that into one shipped fintech-adjacent project with the alternating theory-then-build cadence he asked for.

Open question to resolve before week 1: by "fundamentals", does he mean (a) how LLMs work under the hood (transformers, attention, tokenisation, training), or (b) how to build production LLM systems (embeddings, RAG internals, evaluation, agents, tool calling)?

If (a): this plan does not fit. Better fits would be Karpathy's "Neural Networks: Zero to Hero" and equivalent material.

If (b): this plan is right - it covers exactly that ground via AI Hero plus a sprint project. Most signals in the intake point at (b), but it is worth confirming before he commits.

## Plan

This is the shareable part of the document.

## Focus

- Main focus: ship one fintech-adjacent LLM application end to end. Most likely a RAG over a corpus you want to query (your own notes, internal docs, meeting transcripts, or a public fintech corpus), with proper evaluation, basic monitoring, and a live URL.
- Supporting focus: complete AI Hero in the first two weeks as the agent-building foundation. Treat it as the theory side of the alternating cadence you asked for - read/build a module, then apply the concept to your project.
- Supporting focus: tighten the AI-assisted coding workflow on this project specifically - better specs, smaller decomposed tasks, deterministic skills/tools that fire when you expect them to, and a habit of reading what Cursor / Claude Code generated rather than running it.

## Timeline

The plan below is dense for a 5-8 hr/week budget. Treat the week boundaries as targets, not contracts. If AI Hero spills into week 3 because evenings get eaten, that is fine - shift everything one week and drop the week 6 polish, not the build/eval/deploy core. The non-negotiable outcome is one shipped, evaluated, deployed project. The calendar is flexible.[^5]

Week 1:

- [Start AI Hero](https://aishippinglabs).com/courses/aihero . Aim for the first half of the modules in week 1. Treat each module as the "theory block" before the build block on the same concept.
- Use the project-idea brainstorming gist to surface 5-10 fintech-adjacent project candidates. Keep the bias toward problems you already feel: things you would use at work (data-science agent team for EDA, internal analytics assistant, model monitoring, data-quality agent, knowledge base over company docs / meeting transcripts) or for yourself.
- Run the fit-check prompt on the top 1-2 candidates and pick one. The picking has to happen this week - if it slides, the analysis paralysis you flagged in the intake is what's pulling it.

Week 2:

- Finish AI Hero. The full course is sized so it can fit inside two weeks of evenings.
- Write a one-paragraph project card for the chosen project: who the user is (often you), what input the system takes, what it produces, what "useful" looks like.
- Find or prepare the corpus the project needs (your Obsidian vault, a fintech public corpus, anonymised work data, scraped public filings - whatever fits).

Week 3:

- Build the simplest working end-to-end version. Plain Python functions for retrieval and answer generation, then wrap them in an agent or chain - functions first, agent on top, not the other way round.
- Ship it as a CLI or Streamlit page that you yourself use at least once a day during the rest of the sprint. If you do not use it, the eval set in week 4 will be hypothetical.

Week 4:

- Build an eval set: 20-50 representative questions / inputs with a notion of what a correct answer looks like. This is where the "embeddings + RAG internals + evaluation" fundamentals from your intake get applied to your project, rather than studied in the abstract.
- Add LLM-as-judge for the open-ended cases and assertion-style checks for the deterministic ones.
- Use the eval set to compare two or three retrieval / chunking variants. Stop tuning when the differences are small enough that the next gain comes from something else.

Week 5:

- Add monitoring: Logfire (or equivalent) for traces and request-level visibility. Confirm an end-to-end trace from user input to answer is readable.
- Deploy: pick a deployment target you are comfortable with (cloud VM, serverless, Hugging Face Spaces, etc.) and ship a live URL, plus GitHub Actions to push on every commit. The eval set runs in CI and can block deploy on regressions.[^5]
- Tighten the AI-assisted coding loop on this project: write specs before letting an agent run, decompose tasks before handing them off, read the diff line by line, and capture the prompts/skills that worked deterministically into a project-local `.cursorrules` / Claude skill so they fire reliably next time.

Week 6:

- Polish: README that covers problem, architecture, eval results, run instructions. Architecture diagram. Short walkthrough video if energy allows.
- Demo to the AI Shipping Labs community via Slack. Capture feedback.
- Decide the next sprint: deeper on this project (fine-tuning experiment, agent extensions), or move to the second project from your candidate list.

## Project approach

- One project, not three. The intake lists several fintech-adjacent project shapes (data-science agents, knowledge base, internal analytics assistant, model monitoring, data-quality agent). Pick one for this sprint. The others are good follow-ups. Trying two in parallel is the fastest way to ship neither.
- Production-quality means useful, not extensive. You said in the intake that you want to ship a tiny product the community or other people can use or learn from - that is the right bar. Tests, logging, evaluation, monitoring, and a clean README are the minimum. Security, cost tracking, CI/CD policies are layers you add only if the project itself needs them.
- Functions before agents. Write the underlying retrieval/answering logic as plain Python functions you can test directly. Wrap them in an agent only after the functions work. This is the cleanest way to get deterministic skills - the agent's nondeterminism is contained because the deterministic parts are in real functions with real tests.
- The Zoomcamp cadence is yours. You said the alternating theory-then-build worked for you in DE Zoomcamp / MLOps Zoomcamp. The week-by-week plan is built around that: each week has a concept (RAG basics, retrieval, evaluation, monitoring, deployment) and the build that uses it.
- Fixed cadence, not flexible. You flagged ADHD and said fixed weekly check-ins work better than flexible ones. Pick a day for the weekly update and treat it as a hard appointment.

## Resources

- [AI Hero](https://aishippinglabs).com/courses/aihero - the agent-building foundation, weeks 1-2.
- [Project-idea brainstorming gist](https://gist).github.com/alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1 - interview prompt for candidate generation, fit-check prompt for validation.
- LLM Zoomcamp re-recording starts in June (workshop on 2026-05-11 is the kickoff). Useful as a parallel track once the sprint project is live.
- Logfire for monitoring once the simple version works.
- Community accountability channel (`#plan-sprints`).

## Deliverables

- AI Hero completed - by end of week 2.
- One-paragraph project card + chosen project + corpus secured - by end of week 2.
- Working end-to-end version (CLI or Streamlit), used daily by you - by end of week 3.
- Eval set + retrieval-variant comparison results - by end of week 4.
- Live monitoring + deployed URL with CI eval gating - by end of week 5.
- Public README + architecture writeup + community demo - by end of week 6.

## Accountability

- Weekly deliverables and demo-based milestones - the format you asked for in intake.
- Fixed weekly check-in day (pick one, stick to it).
- Public progress in `#plan-sprints` Slack: a 3-line update each week (shipped / blocked / next).
- One project. Resist the urge to start a parallel "small experiment" - that is the analysis paralysis you flagged.

## Next Steps

- [ ] [Daiyaan] Confirm what "fundamentals" means to you (LLM internals vs. building LLM systems) so the plan can be tuned or replaced before week 1.
- [ ] [Daiyaan] Run the project-idea brainstorming prompt and produce 5-10 fintech-adjacent candidates by end of week 1.
- [ ] [Daiyaan] Run the fit-check prompt on the top 1-2 candidates and pick one.
- [ ] [Daiyaan] Start AI Hero from day 1.
- [ ] [Alexey] Send the written plan plus the project-idea brainstorming gist link.
- [ ] [Valeriia] Confirm Daiyaan is on the AI Shipping Labs Slack channel and added to the May sprint roster.

## Internal Context

Everything below is for internal use only.

## Persona

Alex - The Engineer Transitioning to AI (with significant Priya overlap). Daiyaan has solid software / data engineering experience (Databricks, full lifecycle, MLOps Zoomcamp graduate) and uses Cursor + Claude Code heavily, but has not built an LLM application end to end at the depth he wants. The "engineer transitioning into LLM/agent work from an existing engineering base" framing is the closest fit. He leans toward Priya in that he has shipped some applied AI/ML work already and is now sharpening it.

See [personas.md](../personas.md) for full persona definitions.

## Background

Daiyaan is a data lead at a small fintech startup, owning the full data lifecycle from ingestion to ML deployment on Databricks. He uses AI tools (Cursor, Claude Code) heavily in his day-to-day workflow and continuously upgrades his MLOps, logging, and ML system practices through articles and crash courses[^2].

He is a graduate of Data Engineering Zoomcamp and MLOps Zoomcamp - those courses turned him "from a casual office worker into a genuinely passionate engineer", and he credits the way concepts were explained for letting him build with confidence rather than treating things as a black box. He missed the AI Engineering Buildcamp deadline, which is why he wanted to try AI Shipping Labs[^1].

Daiyaan has self-disclosed ADHD and explicitly prefers a fixed cadence over flexible scheduling[^2].

A note on the name: the original interview file uses "Daiyaan Ahmed" (the name he introduced himself with in the first message[^1]). The intake document was sent under the name "Daiyaan Shaik"[^3]. Using "Shaik" in this plan to match the most recent message. If "Ahmed" is the canonical name, both files should be reconciled.

Cross-reference the matching interview at [../interviews/daiyaan-ahmed.md](../interviews/daiyaan-ahmed.md).

## Intake

## Initial Input

Daiyaan's free-form input from the intake document[^2]:

> Hey Valeriia and Alexey,
>
> So happy to meet you!
>
> I'm the data lead at a small fintech startup, handling the full lifecycle from ingestion to ML deployment (Databricks). AI tools have significantly sped up my workflow, I use Cursor and Claude Code heavily and I'm constantly looking to improve my workflow by using the latest best practices. I actively improve my MLOps, logging, and ML based systems by reading articles and crash courses.
>
> Personally I don't like building unless I know how the internals work which is why I absolutely loved the data engineering zoomcamp and MLOps zoomcamp. Im grateful for those courses and Alexey's effort.
>
> However, I lack strong fundamentals about how AI works under the hood and haven't had time to consistently build projects based on RAG or fine tuning or it's dozens of use cases. I often get stuck in analysis paralysis and want more structure, accountability, and mentorship.
>
> My goal here is to build and ship consistently, strengthen my fundamentals, and grow a solid GitHub. Similar to how the Zoomcamps helped me learn by deeply understanding concepts and building incrementally.
>
> Happy to jump on a call, I'm available anytime after 7PM ET on weekdays and 10AM to 7PM ET on weekends. Really excited to get started!!!

## Questions and Answers

Verbatim Q&A from the intake document[^2]:

1. What do you hope to achieve with this plan in the next 6 to 8 weeks? - "In order: 1. strengthen fundamentals, 2. ship one solid AI project, 3. grow GitHub, 4. improve AI-assisted workflow."

2. If you had to choose one concrete outcome for the next 6 weeks, what should it be? - "One shipped, production-style LLM app (likely RAG-based) with proper evals - fintech-adjacent."

3. How much time can you realistically commit each week? - "5 to 8 hrs consistently. Mostly weekday evenings + weekends."

4. What kind of project would be most useful for your current work or career direction? - "Fintech or work-adjacent. Strong candidates would be to build a system of data science agents (agent team) to automate the workflow of EDA, building a knowledge base for strict grounded retrieval from company docs and meeting recording transcripts, internal analytics assistant, model monitoring, or data-quality agent."

5. What AI fundamentals do you most want to understand under the hood? - "Embeddings, RAG internals (chunking, retrieval, reranking), evaluation, and agents/tool calling and orchestration. In that order, please correct me if I am wrong."

6. What have you already built or tested with RAG, fine-tuning, or LLM applications? - "Recently built a LLM wiki second brain by following Andrej Karpathy's workflow. I love reading but I find it hard to retain this knowledge so I built a structure on Obsidian and added a lot of templating to reduce my friction to log them. I log every single thing I read or watch on obsidian in a structured template. On the weekends I built a claude workflow which goes through this and updates me on what I learnt, creates a weekend revision and how to proceed on my plan to become a strong AI engineer. I am currently connecting it to NotebookLM to create flashcards and podcasts over what I learnt over the week so that I can remember the important concepts I learnt. None of this uses the core AI fundamentals though, it uses existing tools and its orchestration. Moving from 'I followed the tutorial' to 'I built my own version that I understand end-to-end' is the gap I want this sprint to close."

7. What usually triggers analysis paralysis for you? - "Wanting to understand too much before building and extreme focus on perfectionism, I spend too much time on learning and understanding new things plus comparing too many tools instead of hands on. No hard deadlines makes it worse."

8. What does "production-quality" mean to you for a 6-week AI project? - "Given that I use AI heavily while knowing the architecture, choices and tech under it (not vibe coding it), I would love to ship an actual tiny product which is useful for the community or an idea with real value. Not looking to build my own startup here lol but would love to ship something people would use and benefit from or atleast learn from."

9. How should the plan balance fundamentals and shipping? - "Alternating weekly, short focused theory block, then building that exact concept. Zoomcamp style worked well for me."

10. What kind of mentorship or feedback would be most useful? - (no answer provided)

11. What type of accountability would help you ship consistently? - "Weekly deliverables and demo-based milestones. Public progress and slack checkins help. I have ADHD, so fixed cadence is better than flexible"

12. What AI-assisted coding workflow do you want to improve? - "Writing better specs and decomposing tasks before letting agents run and more importantly knowing how the agents are using the tokens and understanding my prompts and triggering workflows. And I would love to build skills which are kind of deterministic, most of the skills that I build right now hallucinate or don't trigger when I want them to. I want to use Cursor/Claude Code without losing understanding of what's being built."

13. What would make the next 6 to 8 weeks worthwhile? - "One shipped AI project I can point to and genuine confidence in RAG/LLM system design fundamentals."

## Meeting Notes

No intake call yet - input collected via the Google Doc[^2] and the initial outreach message[^1].

## Internal Recommendations

Alexey's recommendations after reviewing the intake[^4]:

1. The detailed answers do most of the work. He has already articulated what he wants in fairly concrete terms - shipping one LLM project, fintech-adjacent, with proper evaluation - so the plan is more about structuring his own picture than redirecting it.

2. Open question on "fundamentals". The intake repeatedly says he wants to "strengthen fundamentals" and "understand how AI works under the hood" but does not specify what that means. If he means transformer internals (attention, tokenisation, training), this plan is the wrong shape - he should look at Karpathy's "Neural Networks: Zero to Hero" or equivalent. If he means LLM application fundamentals (embeddings, RAG internals, evaluation, agents, tool calling) - which is what his Q5 list says - then this plan is correct. Most signals point at the second reading, but confirm before he commits to week 1.

3. If the second reading is correct, the path is the standard one: AI Hero first to give him the agent foundation, then the same project-selection structure used for other members. The brainstorming gist is the picking tool, the four-criterion scoring is the filter, and one chosen project carries the rest of the sprint.

4. Project domain: fintech-adjacent. He works in fintech, his Q4 candidates are all fintech-adjacent, and the brief explicitly says fintech. Let him think through the specific problem himself - the gist exists for that. Do not pre-pick a project for him. The picking exercise is part of the value.

5. Open question on hands-on dev skill. From the intake messages alone it is hard to tell how strong his actual implementation pace is. He says he uses Cursor / Claude Code heavily, but heavy AI-assisted work and shipping a hand-built LLM application end to end are different skills. Treat week 1's project work as the signal and adjust scaffolding (more or less explicit guidance) accordingly.

6. Lean on his Zoomcamp cadence. He explicitly asked for an alternating theory-then-build pattern because that worked for him before. Structure the week-by-week so each week is a concept block followed by a build block on the same concept. AI Hero is the natural carrier for the early weeks. The project's own complexity carries the later ones.

7. The AI-assisted workflow gap is real and worth treating as a sub-deliverable. He flagged that his current skills hallucinate or do not fire deterministically. The sprint project is the right place to practise: write specs first, decompose before delegating, capture the prompts that worked into project-local rules. Do not make it a separate workstream. Make it the way the project gets built.

## Internal Action Items

- [ ] [Alexey] Send Daiyaan the written plan plus the project-idea brainstorming gist link.
- [ ] [Alexey] Confirm with Daiyaan which reading of "fundamentals" applies before he commits to week 1.
- [ ] [Valeriia] Confirm Daiyaan is on the AI Shipping Labs Slack channel and added to the May sprint roster.
- [ ] [Valeriia] Confirm canonical surname (Ahmed vs Shaik) and reconcile the interview file and the plan file.

## Sources

[^1]: [20260504_215616_AlexeyDTC_msg3860.md](../../../inbox/used/20260504_215616_AlexeyDTC_msg3860.md) - Daiyaan's first message in the community (under the name "Daiyaan Ahmed"), source for the existing interview file.
[^2]: [Daiyaan Shaik's intake (Google Doc)](https://docs.google.com/document/d/1G2vCdnx5CmaeT6Y4TqiB40eyd2J9TZ55vAefHbOkHSs/edit?usp=sharing), shared via [20260509_114718_AlexeyDTC_msg3990.md](../../../inbox/used/20260509_114718_AlexeyDTC_msg3990.md).
[^3]: The intake message in the inbox names this person "Daiyaan Shaik": [20260509_114718_AlexeyDTC_msg3990.md](../../../inbox/used/20260509_114718_AlexeyDTC_msg3990.md).
[^4]: [20260509_115045_AlexeyDTC_msg3992_transcript.txt](../../../inbox/used/20260509_115045_AlexeyDTC_msg3992_transcript.txt) - Alexey's recommendations after reviewing the intake.
[^5]: [20260509_123256_AlexeyDTC_msg3998_transcript.txt](../../../inbox/used/feedback/20260509_123256_AlexeyDTC_msg3998_transcript.txt) - Alexey's feedback: AI Hero URL changed (no `dev.` prefix), do not pre-pick deployment platform, check the plan is realistic at 5-8 hr/week.
