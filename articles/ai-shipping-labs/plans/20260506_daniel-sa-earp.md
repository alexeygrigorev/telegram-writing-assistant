---
title: "Plan: Daniel Sa Earp"
created: 2026-05-06
updated: 2026-05-07
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Daniel Sa Earp

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: Brazilian analytics engineer with a full-time job, working primarily in SQL and dbt. Comfortable with Python for data analysis (pandas, numpy) but not with software engineering shape (classes, project structure, environments, APIs, deployment). Has signed up for LLM Zoomcamp starting in June and the workshops beforehand. Has a side project requiring AI knowledge that he wants to discuss on a call.
- Goal for the next 6 weeks: arrive at LLM Zoomcamp in June well-prepared. Concretely: build one end-to-end data-ingestion project that combines analytics-engineering muscle with the engineering shape needed for the course (API ingestion → Docker → Elasticsearch).
- Main gap to close: turning analytics-engineering skills (SQL/dbt) into engineering shape - APIs, Docker, project structure, deployment - so that when the LLM Zoomcamp starts in June, the AI content is the only new thing he is learning, not also "what is Docker" and "how does a Python project work".
- Weekly time commitment: 10-15 hours per week worst case (2 hours per workday, 3-4 hours per non-workday), likely more.
- Why this plan is the right next step: AI Shipping Labs adds structure, accountability, and project feedback while LLM Zoomcamp does the AI teaching. Without preparation, the course's pace plus learning Python/Docker/APIs at the same time would be overwhelming. With preparation, the course becomes the deeper-end of the same shape he already practised.

## Plan

## Focus

- Main focus: build one end-to-end data-ingestion project with Python, the GitHub API, Docker, and Elasticsearch. By the end of week 6, fetching new and updated issues from a real GitHub repo and storing them in Elasticsearch on a schedule.
- Supporting focus: get unblocked on Python software-engineering shape - classes, project structure, environments, packaging - using the project as the carrier. Stop using AI as a black box. Understand what it produces.
- Supporting focus (light): if there is room after the project is solid, start AI Hero with the first day or two on search. Skip the agent material - that lands in LLM Zoomcamp.

## Timeline

Week 1:

- Pick the data source. GitHub issues from one well-known public project is the recommended choice (Kubernetes, Pandas, Airflow - any large repo with active issues and comments). Decide which repo and why.
- Set up the Python project from scratch by hand. uv-based project, virtual environment, a `pyproject.toml`, a folder structure that makes sense to you. Write the first script that uses `requests` to fetch the latest issues from the GitHub API. The point is to write this yourself, using AI for explanations of concepts you have not seen before, not as a code generator.
- Run Elasticsearch locally in Docker via docker-compose. Confirm it is up and you can write a single document to an index using the Python client.

Week 2:

- Build the ingestion pipeline: fetch issues from the API, transform them into the shape you want indexed, write them into Elasticsearch. Index titles, bodies, labels, and metadata. Do not touch comments yet.
- Add a simple CLI - one command to ingest a repo from scratch, one to confirm what is in the index. This is the first place where Python project structure (modules, functions, a `main.py` or a small CLI library) becomes real rather than theoretical.

Week 3:

- Add update detection. On a re-run, detect issues that have changed since last ingest and update them in Elasticsearch instead of re-inserting. The bookkeeping (last-seen timestamp, ETag, or whatever you choose) is the engineering bit. This is where SQL/dbt instinct translates well - you are doing incremental loads, just into Elasticsearch instead of a warehouse.
- Add comments ingestion. For each issue, fetch its comments and store them so they are searchable alongside the issue.

Week 4:

- Run the pipeline regularly (cron, GitHub Actions, or a tiny scheduler) so the index stays current. Iterate on whatever broke when you ran it the second time on a different repo - this is where edge cases show up.
- Write a small Streamlit page or a CLI search tool that queries the Elasticsearch index with text search. Not a full product - just enough that you can demo "search the project's issues" end to end.

Week 5:

- Light AI Hero start: first day or two, on search. The point is to understand the search side of RAG before LLM Zoomcamp covers retrieval-augmented generation. Skip the agent material.
- Tighten the project: README that explains the architecture, the schema, how to run it, and what each part does. Pretend a future LLM Zoomcamp peer needs to clone and run it.

Week 6:

- Wrap to a state you would happily show in the LLM Zoomcamp Slack as your starter project. Tag a release.
- Walk through what you understand now that you did not understand six weeks ago. This is the meta-deliverable: the increase in Python/engineering confidence is the actual sprint outcome, with the GitHub-issues project as the visible artefact.
- Decide whether the side project mentioned during intake is the right next sprint, or whether to use LLM Zoomcamp's homework projects instead.

## Project approach

- Analytics-engineering skills transfer. You already know how to model data (SQL/dbt) and run incremental loads. The GitHub-issues project is the same shape - source of truth → transform → load → make queryable - just with a different stack. Lean on the parts that are familiar. The new bits are Python project structure, Docker, and the API client.
- Stop using AI as a black box. Daniel flagged this himself: Claude does the project structure, Docker, etc., but he wants to understand it. Concrete rule for the sprint: when AI generates code, read it line by line, ask it to explain anything unfamiliar, and rewrite at least one part by hand to confirm you can. The point is comprehension, not output.
- Elasticsearch first, deployment later. Elasticsearch is great for personal projects locally but expensive to deploy. For this sprint, run it locally in Docker - that is enough. If a deployment exercise becomes useful later, pick a project that does not need Elasticsearch (or use a cheaper alternative like sqlite-vec) for that piece.
- Out-of-scope is recorded, not abandoned. The career decision (analytics engineer vs data/AI engineer), the side project, and "AI in my day job" are explicitly parked behind the LLM Zoomcamp prep for this sprint. They reappear after week 6.
- Skip CI/CD this time. It is genuinely useful but not the right gap to close before LLM Zoomcamp. Revisit later.

## Resources

- LLM Zoomcamp - the main learning track for AI starting in June. AI Shipping Labs is the structure-and-accountability layer around it.
- AI Hero - free, light reference for the search side of RAG. Day 1-2 only during this sprint.
- Pre-Zoomcamp workshops - attend even if not everything lands. The goal is exposure, not full comprehension. Several past members have said the workshops became more useful in retrospect once the course covered the same material.
- [Elasticsearch's Python client docs](https://elasticsearch-py.readthedocs.io/) - read the relevant sections of the official docs rather than relying on AI summaries. This is part of the "stop using AI as a black box" rule.
- A coding assistant of choice (Claude Code, Codex, or similar). Use it for explanation as much as for code generation.

## Deliverables

- Project skeleton + working "fetch and print one issue" script - by end of week 1.
- Issues-only ingestion pipeline writing to Elasticsearch (in Docker) - by end of week 2.
- Updates and comments ingestion working - by end of week 3.
- Pipeline running on a schedule, basic search UI/CLI - by end of week 4.
- Tightened project, README, AI Hero search material started - by end of week 5.
- Tagged release ready to show in LLM Zoomcamp - by end of week 6.

## Accountability

- Study schedule (Daniel's preference) - block the 2 hr/workday + 3-4 hr/non-workday in the calendar at the start of the week.
- Weekly or biweekly check-in. The biweekly cadence is fine if a week feels short - the goal is consistent progress, not reporting volume.
- Feedback on work: post the week's commit (or a snippet of code you are unsure about) in the AI Shipping Labs Slack and ask for a read. The community is the substitute for a lone analytics engineer not having peers to bounce engineering questions off.

## Longer arc

- 6-week sprint: end-to-end ingestion project, ready for LLM Zoomcamp.
- 3-4 month: complete LLM Zoomcamp with a final project that builds on this ingestion pipeline (e.g., RAG over GitHub issues).
- 12-month: clearer call on analytics engineer vs data/AI engineer, informed by what the LLM Zoomcamp project surfaces. Side project resumes once Python and AI confidence are higher.

## Next Steps

- [ ] [Daniel] Pick the GitHub repo to ingest and write the one-page concept doc by end of week 1.
- [ ] [Daniel] Confirm a coding-assistant choice and a schedule of weekly time blocks.
- [ ] [Daniel] Share weekly progress in the AI Shipping Labs Slack.
- [ ] [Alexey] Send the written plan. Agree on the call date to discuss the side project, the career question, and the medium-term plan.
- [ ] [Valeriia] Confirm Daniel is on the AI Shipping Labs Slack channel, on the LLM Zoomcamp roster for June, and added to the May sprint.

## Internal Context

## Persona

Sam - The Technical Professional Moving to AI (preliminary). Daniel works mainly with SQL/dbt and uses Python for data analysis but not for building systems. He himself describes his level as "neither technical nor completely non-technical", and the engineering-shape gaps he names (classes, project structure, environments, APIs, deployment) match Sam's profile precisely.

See [personas.md](../personas.md) for full persona definitions.

## Background

Daniel is a Brazilian analytics engineer based in Brazil with a full-time job. He uses SQL and dbt as his main stack, with Databricks at work and Airflow as a "light user" (he can build and debug DAGs but did not set the platform up). He has been trying for the last few months to learn more about AI for both daily life and work, but feels overwhelmed by the volume of AI content online. He is considering whether to stay an analytics engineer or move to a more technical role (data engineer or AI engineer)[^1].

He plans to join LLM Zoomcamp in June and attend the pre-Zoomcamp workshops. He has signed up to AI Shipping Labs at the premium tier specifically to take courses, finish his side project, become more technical, and stay current through a curated lens. He flagged that he prefers a quick chat to discuss a few of the questions in more depth, particularly the side project and how to combine analytics engineering with AI[^1].

## Intake

## Initial Input

Daniel's free-form input from the intake document[^1]:

> Hello!
>
> I'm a Brazilian living in Brazil and an analytics engineer with a full time job. Recently (in the last few months) I've been trying to learn more about AI and how I can use it both in my daily life and in my work/personal projects.
>
> Unfortunately I feel overwhelmed by the sheer amount of online information and am unsure how to proceed.
>
> By joining your paid services, I aim to:
> - Learn more about AI and AI tools, take courses etc (This is why I chose "premium" and not "main".)
> - Finish a side project that requires AI knowledge (I can explain more later)
> - Figure out how to use AI in my day to day job so I can distinguish myself
> - Stay current with the latest trends through your curated lens, instead of being bombarded by information on the internet
> - Decide whether to remain an analytics engineer or migrate to a more technical role (data or AI engineer)
>
> If I had to describe myself, I would say I'm neither technical nor completely non-technical. I work mainly with data modeling and SQL/DBT and have some past experience with Python, primarily using libraries for data analysis and cleansing when I was a data analyst. Therefore, I'd say I'm familiar with Python but I'm not proficient in it. I struggle a bit with the more technical data engineering tools as well.
>
> Overall, I want to become more technical while learning more about AI, if that makes sense.

He asked three follow-up questions[^1]:

- Is it worth joining the LLM Zoomcamp pre-workshops on top of AI Shipping Labs?
- Can the plan include a track to become more technical with general tools (like Python)?
- Is focusing on both data engineering and AI simultaneously too much?

## Questions and Answers

1. What should this plan help you achieve in the next 6 to 8 weeks? - "For the next 6 to 8 weeks I believe that learning and getting deeper into AI will be just fine! I assume that will already make me a bit more technical as well." (He reframed the long list as a long-run goal, not a 6-week one.)

2. What is the side project you want to finish? - "I would prefer to talk about this on our chat, I believe it will be easier."

3. How much time can you realistically commit each week? - "I can, worst case scenario, commit to 2 hours each workday, and 3-4 hours each non workday (holidays and weekends). I'd rather commit to that worst case scenario, but most likely I'll be able to do more."

4. What does "becoming more technical" mean to you? - "Doing all that. You literally described what I meant!" (Python more confidently, building small applications, working with APIs, Docker, cloud, data pipelines, deploying.)

5. What is your current Python level? - "I do fine with functions, data analysis libraries like pandas, numpy, etc. I struggle a bit with classes, project structure, environments, APIs, deployment, etc. (...) Ironically, AI has been a detriment to this, I find I rely too much on it. Claude helps me with project structure, docker, etc, but I would like to be able to do it myself, or at least have a good understanding of what AI is doing and why. I don't want to just use AI like a black box in this scenario."

6. Which technical data engineering skills feel like the biggest gap? - Spark, Docker, data pipelines, orchestration. Also CI/CD and infrastructure but he had to prioritise. Uses Airflow as a light user (the data engineering team set it up).

7. How would you like to combine analytics engineering and AI? - Wants to discuss on the call.

8. What AI topics should we prioritize first? - "Prompting, RAG and agents would be ok for now I think."

10. How should LLM Zoomcamp fit into your plan? - "Yes, I believe the zoomcamp and the workshops will be challenging enough for me, so I don't know if more tasks would be a good idea at the moment (unless you disagree), so maybe this plan should 'use LLM Zoomcamp as the main learning track while AI Shipping Labs adds structure, accountability, and project feedback.'"

11. What usually causes information overload for you? - "Unclear learning path, feeling behind and not knowing what matters for my role."

12. What kind of accountability would help you stay consistent? - "Study schedule, some form of check-in (weekly or bi weekly) and feedback on my work."

13. What would make the next 6 to 8 weeks worthwhile? - "Clearer AI learning path and readiness for the LLM Zoomcamp, better python confidence would be a plus."

(The intake document numbering jumps from 8 to 10 - question 9 is missing from the source.)

Daniel's closing comment: he is aware his goals are big for 6-8 weeks. He plans to stay in the community for the long haul and would value a longer-term plan in addition to the short one.

## Meeting Notes

Daniel and Valeriia held a 30-minute call on 2026-05-07. Alexey was not on this call - the original intake call with Alexey is still pending and is the place to cover the side project and the longer-term plan in depth[^3][^4].

Key points from the 2026-05-07 call[^3][^4]:

- Sprint plan reception: Daniel finds the proposed 6-week plan doable and says it gives him much-needed structure - exactly what he was missing as someone new to AI engineering. He acknowledged he is starting a day late (May 7 instead of May 1) but said he will start week 1 the same evening and notify the team if he needs more time.
- Python course: Daniel will not take the Python course Alexey is preparing during this sprint - he believes the existing plan is already a lot of work. He still wants to see the summary and plans to do the full course later, possibly alongside LLM Zoomcamp. Valeriia agreed to ask Alexey to share the Python course draft.
- Coding approach: Daniel wants to use ChatGPT/Codex to understand concepts and see examples, then write code by hand, then ask ChatGPT for feedback, and finally post weekly progress on Slack for community feedback. Valeriia confirmed this aligns with Alexey's recommendations - "use AI for explanation as much as for code generation" rather than copy-paste.
- Existing course content as reference: Valeriia walked Daniel through how LLM Zoomcamp, AI Hero, and the pre-Zoomcamp workshops all have hands-on code examples he can follow. The pre-Zoomcamp workshops will be cut into the LLM Zoomcamp module videos, so attending them gives him the same content earlier. Valeriia agreed to share the Luma link for the Data Talks Club workshops series.
- Office hours support: Valeriia explained that Alexey plans to host weekly office hours specifically for AI Shipping Labs members doing LLM Zoomcamp - the small-cohort substitute for trying to support all 10,000+ public Zoomcamp participants directly.
- AI Hero access: Daniel can sign in to the new AI Shipping Labs platform with Google or Slack and access AI Hero there. Valeriia mentioned the platform was published the previous night and not yet announced - some members are still flagged as free plan, but access works. Daniel confirmed he will look at AI Hero in week 5 as planned, focusing on the Python and Docker foundations first.
- Docker resource: Valeriia recommended the first module of Data Engineering Zoomcamp as a Docker reference Daniel can refer to during the sprint.
- Long-term guidance: Daniel asked whether he can keep getting some guidance after the 6-week sprint and the LLM Zoomcamp, even if the community grows and per-member attention decreases. Valeriia said it depends on how the community grows and Alexey's availability, but they hope to provide at least some guidance for ongoing members.
- Tooling tip: Valeriia suggested Daniel use ChatGPT's microphone input for brain-dumping his side project idea before writing it down - the same flow Alexey uses.
- Future course topics: Daniel suggested the community could eventually offer courses on LLM/AI subjects that LLM Zoomcamp does not cover, and recommended querying the public to find preferred topics. Valeriia acknowledged the suggestion and noted that direct asks like this call help more than broad polls, since people often stay silent when surveyed.

Action items added by this call:

- [ ] [Valeriia] Send these meeting notes to Alexey.
- [ ] [Valeriia] Ask Alexey to share the Python course draft with Daniel.
- [ ] [Valeriia] Send Daniel the Luma link for the Data Talks Club workshops series.
- [ ] [Valeriia] Check Alexey's calendar availability for a 30-minute call on Daniel's side project.
- [ ] [Daniel] Sign in to the new AI Shipping Labs platform via Google or Slack and access AI Hero there.
- [ ] [Daniel] Document the side project main idea in this plan document (recorded below in Side Project Idea, recorded by Daniel during the call to follow up on this).

## Side Project Idea (recorded during the 2026-05-07 call)

Daniel intends to start this only after the 6-week sprint - he wants the Python, Docker, APIs, and Elasticsearch foundation in place first. The information is captured here so it does not get lost. The sprint plan does not change[^3][^4].

The project is a chatbot platform for a proprietary educational method in the audiovisual industry. Daniel's wife runs the business and owns the underlying material - documents, PDFs, videos, and lessons that teach this method to other people. She currently uses a custom GPT she built in the ChatGPT web interface, trained on these documents. She wants to sell access to this knowledge as a service to other people in the audiovisual industry.

What needs to be built:

- An AI agent grounded in the proprietary corpus (documents, PDFs, videos, lessons).
- A website that embeds the agent and lets users interact with it.
- Login, accounts, and a subscription plan so paying customers can use the chatbot.
- Rate limiting per user, so an unbounded API bill is not possible if a user asks an unlimited number of questions.

Valeriia's read on the call: the project is "absolutely doable", in the same shape as similar projects from Alexey's courses (corpus-grounded chatbot with citations - the Data Talks Club podcast chatbot idea is one example). The build needs to be staged - the agent first, then the website and integrations, then payments. Daniel asked whether he should write this in the plan document or send it to Alexey directly on Slack, and said he would prefer a 30-minute call with Alexey to discuss it in more depth if that is possible.

## Internal Recommendations

Alexey's recommendations after reviewing Daniel's intake[^2]:

1. Analytics engineer is technical work close to data engineering - he can move toward it without starting from zero. RAG is the right first AI focus.

2. There is no AI Shipping Labs course content yet for what he wants - the team is focused on the May sprint and will roll out a course in parallel. So for this sprint, AI Shipping Labs adds structure and feedback while LLM Zoomcamp (in June) is the main learning track. Daniel's own framing is correct.

3. Recommend he attend the pre-Zoomcamp workshops even if not everything lands - prior cohort feedback says exposure is genuinely useful, even when comprehension lags by a few weeks. The "I half-understood it then but it clicked later" effect is common.

4. The right preparation project: an end-to-end data-ingestion pipeline using Python and an API. Concretely - take GitHub issues from a large public project, fetch via requests, store them in Elasticsearch in Docker, handle updates and comments. This sits at the crossover of data engineering (ingestion, incremental loads, schema design) and AI engineering (Elasticsearch as a search backend). Six weeks of build is enough to make him max-prepared for LLM Zoomcamp, and the project doubles as a strong starter for the LLM Zoomcamp final project.

5. Why Elasticsearch specifically: companies often use it. Getting hands-on with it now pays off later. The constraint to be honest about: it is expensive to deploy for personal projects, so the production-deployment exercise belongs to a different project (not Elasticsearch). For this sprint, local Docker is enough.

6. He flagged using AI as a black box - this is the most important thing to address. The plan should explicitly say "stop outsourcing comprehension". The project gives him a setting where he has to write Python project structure, Docker, and an API client himself, with AI as an explainer rather than a code generator.

7. CI/CD is genuinely useful but is not the right gap to close before LLM Zoomcamp. Park it. Same for full deployment.

8. AI Hero first day or two, on search, only if there is time after the project is solid. Skip the agent material - that lands in LLM Zoomcamp.

9. Out-of-scope items (career direction, side project, AI in his day job, broader Python proficiency) get recorded for future plans. The intake call is the natural place to cover the side project and start sketching the longer-term arc Daniel asked for.

## Internal Action Items

- [ ] [Alexey] Send Daniel the written plan and propose call slots.
- [ ] [Alexey] On the intake call, cover the side project, the career direction, and the medium-term plan.
- [ ] [Valeriia] Confirm Daniel is on the AI Shipping Labs Slack channel, the LLM Zoomcamp June roster, and the May sprint.
- [ ] [Valeriia] Follow through on the action items from the 2026-05-07 call (listed under Meeting Notes).

## Sources

[^1]: [Daniel Sa Earp's intake (Google Doc)](https://docs.google.com/document/d/1QtkLtuYae5f9i9JbElRgRxiBs9IKnGqwhZJktwWxImA/edit?usp=sharing), shared via [20260506_174247_AlexeyDTC_msg3873.md](../../../inbox/used/20260506_174247_AlexeyDTC_msg3873.md).
[^2]: [20260506_200424_AlexeyDTC_msg3880_transcript.txt](../../../inbox/used/20260506_200424_AlexeyDTC_msg3880_transcript.txt) - Alexey's recommendations after reading the Q&A.
[^3]: [Meeting notes from Daniel and Valeriia's call, 2026-05-07 (Google Doc)](https://docs.google.com/document/d/1F3rD7jBbjL5p3AK-6XuQiSf1dFhTHz3BebS_9hWJxlw/edit?usp=sharing), shared via [20260507_135305_AlexeyDTC_msg3940.md](../../../inbox/used/20260507_135305_AlexeyDTC_msg3940.md).
[^4]: [20260507_135305_AlexeyDTC_msg3941_transcript.txt](../../../inbox/used/20260507_135305_AlexeyDTC_msg3941_transcript.txt) - Valeriia's voice summary of the same call, with Alexey's instruction to record this information without changing the plan in [20260507_135934_AlexeyDTC_msg3944_transcript.txt](../../../inbox/used/20260507_135934_AlexeyDTC_msg3944_transcript.txt).
