---
title: "Plan: Daniel Sa Earp"
created: 2026-05-06
updated: 2026-05-06
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

### Focus

- Main focus: build one end-to-end data-ingestion project with Python, the GitHub API, Docker, and Elasticsearch. By the end of week 6, fetching new and updated issues from a real GitHub repo and storing them in Elasticsearch on a schedule.
- Supporting focus: get unblocked on Python software-engineering shape - classes, project structure, environments, packaging - using the project as the carrier. Stop using AI as a black box; understand what it produces.
- Supporting focus (light): if there is room after the project is solid, start AI Hero with the first day or two on search. Skip the agent material - that lands in LLM Zoomcamp.

### Timeline

Week 1:

- Pick the data source. GitHub issues from one well-known public project is the recommended choice (Kubernetes, Pandas, Airflow - any large repo with active issues and comments). Decide which repo and why.
- Set up the Python project from scratch by hand. uv-based project, virtual environment, a `pyproject.toml`, a folder structure that makes sense to you. Write the first script that uses `requests` to fetch the latest issues from the GitHub API. The point is to write this *yourself*, using AI for explanations of concepts you have not seen before, not as a code generator.
- Run Elasticsearch locally in Docker via docker-compose. Confirm it is up and you can write a single document to an index using the Python client.

Week 2:

- Build the ingestion pipeline: fetch issues from the API, transform them into the shape you want indexed, write them into Elasticsearch. Index titles, bodies, labels, and metadata. Do not touch comments yet.
- Add a simple CLI - one command to ingest a repo from scratch, one to confirm what is in the index. This is the first place where Python project structure (modules, functions, a `main.py` or a small CLI library) becomes real rather than theoretical.

Week 3:

- Add update detection. On a re-run, detect issues that have changed since last ingest and update them in Elasticsearch instead of re-inserting. The bookkeeping (last-seen timestamp, ETag, or whatever you choose) is the engineering bit; this is where SQL/dbt instinct translates well - you are doing incremental loads, just into Elasticsearch instead of a warehouse.
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

### Project approach

- Analytics-engineering skills transfer. You already know how to model data (SQL/dbt) and run incremental loads. The GitHub-issues project is the same shape - source of truth → transform → load → make queryable - just with a different stack. Lean on the parts that are familiar; the new bits are Python project structure, Docker, and the API client.
- Stop using AI as a black box. Daniel flagged this himself: Claude does the project structure, Docker, etc., but he wants to actually understand it. Concrete rule for the sprint: when AI generates code, read it line by line, ask it to explain anything unfamiliar, and rewrite at least one part by hand to confirm you can. The point is comprehension, not output.
- Elasticsearch first, deployment later. Elasticsearch is great for personal projects locally but expensive to deploy. For this sprint, run it locally in Docker - that is enough. If a deployment exercise becomes useful later, pick a project that does not need Elasticsearch (or use a cheaper alternative like sqlite-vec) for that piece.
- Out-of-scope is recorded, not abandoned. The career decision (analytics engineer vs data/AI engineer), the side project, and "AI in my day job" are explicitly parked behind the LLM Zoomcamp prep for this sprint. They reappear after week 6.
- Skip CI/CD this time. It is genuinely useful but not the right gap to close before LLM Zoomcamp; revisit later.

### Resources

- LLM Zoomcamp - the main learning track for AI starting in June. AI Shipping Labs is the structure-and-accountability layer around it.
- AI Hero - free, light reference for the search side of RAG. Day 1-2 only during this sprint.
- Pre-Zoomcamp workshops - attend even if not everything lands. The goal is exposure, not full comprehension. Several past members have said the workshops became more useful in retrospect once the course covered the same material.
- [Elasticsearch's Python client docs](https://elasticsearch-py.readthedocs.io/) - read the relevant sections of the official docs rather than relying on AI summaries. This is part of the "stop using AI as a black box" rule.
- A coding assistant of choice (Claude Code, Codex, or similar). Use it for explanation as much as for code generation.

### Deliverables

- Project skeleton + working "fetch and print one issue" script - by end of week 1.
- Issues-only ingestion pipeline writing to Elasticsearch (in Docker) - by end of week 2.
- Updates and comments ingestion working - by end of week 3.
- Pipeline running on a schedule, basic search UI/CLI - by end of week 4.
- Tightened project, README, AI Hero search material started - by end of week 5.
- Tagged release ready to show in LLM Zoomcamp - by end of week 6.

### Accountability

- Study schedule (Daniel's preference) - block the 2 hr/workday + 3-4 hr/non-workday in the calendar at the start of the week.
- Weekly or biweekly check-in. The biweekly cadence is fine if a week feels short - the goal is consistent progress, not reporting volume.
- Feedback on work: post the week's commit (or a snippet of code you are unsure about) in the AI Shipping Labs Slack and ask for a read. The community is the substitute for a lone analytics engineer not having peers to bounce engineering questions off.

### Longer arc

- 6-week sprint: end-to-end ingestion project, ready for LLM Zoomcamp.
- 3-4 month: complete LLM Zoomcamp with a final project that builds on this ingestion pipeline (e.g., RAG over GitHub issues).
- 12-month: clearer call on analytics engineer vs data/AI engineer, informed by what the LLM Zoomcamp project surfaces. Side project resumes once Python and AI confidence are higher.

### Next Steps

- [ ] [Daniel] Pick the GitHub repo to ingest and write the one-page concept doc by end of week 1.
- [ ] [Daniel] Confirm a coding-assistant choice and a schedule of weekly time blocks.
- [ ] [Daniel] Share weekly progress in the AI Shipping Labs Slack.
- [ ] [Alexey] Send the written plan; agree on the call date to discuss the side project, the career question, and the medium-term plan.
- [ ] [Valeriia] Confirm Daniel is on the AI Shipping Labs Slack channel, on the LLM Zoomcamp roster for June, and added to the May sprint.

## Internal Context

### Persona

Sam - The Technical Professional Moving to AI (preliminary). Daniel works mainly with SQL/dbt and uses Python for data analysis but not for building systems. He himself describes his level as "neither technical nor completely non-technical", and the engineering-shape gaps he names (classes, project structure, environments, APIs, deployment) match Sam's profile precisely.

See [personas.md](../personas.md) for full persona definitions.

### Background

Daniel is a Brazilian analytics engineer based in Brazil with a full-time job. He uses SQL and dbt as his main stack, with Databricks at work and Airflow as a "light user" (he can build and debug DAGs but did not set the platform up). He has been trying for the last few months to learn more about AI for both daily life and work, but feels overwhelmed by the volume of AI content online. He is considering whether to stay an analytics engineer or move to a more technical role (data engineer or AI engineer)[^1].

He plans to join LLM Zoomcamp in June and attend the pre-Zoomcamp workshops. He has signed up to AI Shipping Labs at the premium tier specifically to take courses, finish his side project, become more technical, and stay current through a curated lens. He flagged that he prefers a quick chat to discuss a few of the questions in more depth, particularly the side project and how to combine analytics engineering with AI[^1].

### Intake

#### Initial Input

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

#### Questions and Answers

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

Daniel's closing comment: he is aware his goals are big for 6-8 weeks; he plans to stay in the community for the long haul and would value a longer-term plan in addition to the short one.

### Meeting Notes

Call planned but not yet held. Topics for the call: side project, career direction, accountability cadence, longer-term plan.

### Internal Recommendations

Alexey's recommendations after reviewing Daniel's intake[^2]:

1. Analytics engineer is technical work close to data engineering - he can move toward it without starting from zero. RAG is the right first AI focus.

2. There is no AI Shipping Labs course content yet for what he wants - the team is focused on the May sprint and will roll out a course in parallel. So for this sprint, AI Shipping Labs adds structure and feedback while LLM Zoomcamp (in June) is the main learning track. Daniel's own framing is correct.

3. Recommend he attend the pre-Zoomcamp workshops even if not everything lands - prior cohort feedback says exposure is genuinely useful, even when comprehension lags by a few weeks. The "I half-understood it then but it clicked later" effect is common.

4. The right preparation project: an end-to-end data-ingestion pipeline using Python and an API. Concretely - take GitHub issues from a large public project, fetch via requests, store them in Elasticsearch in Docker, handle updates and comments. This sits at the crossover of data engineering (ingestion, incremental loads, schema design) and AI engineering (Elasticsearch as a search backend). Six weeks of build is enough to make him max-prepared for LLM Zoomcamp, and the project doubles as a strong starter for the LLM Zoomcamp final project.

5. Why Elasticsearch specifically: companies often use it; getting hands-on with it now pays off later. The constraint to be honest about: it is expensive to deploy for personal projects, so the production-deployment exercise belongs to a different project (not Elasticsearch). For this sprint, local Docker is enough.

6. He flagged using AI as a black box - this is the most important thing to address. The plan should explicitly say "stop outsourcing comprehension". The project gives him a setting where he has to write Python project structure, Docker, and an API client himself, with AI as an explainer rather than a code generator.

7. CI/CD is genuinely useful but is not the right gap to close before LLM Zoomcamp. Park it. Same for full deployment.

8. AI Hero first day or two, on search, only if there is time after the project is solid. Skip the agent material - that lands in LLM Zoomcamp.

9. Out-of-scope items (career direction, side project, AI in his day job, broader Python proficiency) get recorded for future plans. The intake call is the natural place to cover the side project and start sketching the longer-term arc Daniel asked for.

### Internal Action Items

- [ ] [Alexey] Send Daniel the written plan and propose call slots.
- [ ] [Alexey] On the intake call, cover the side project, the career direction, and the medium-term plan.
- [ ] [Valeriia] Confirm Daniel is on the AI Shipping Labs Slack channel, the LLM Zoomcamp June roster, and the May sprint.

### Sources

[^1]: [Daniel Sa Earp's intake (Google Doc)](https://docs.google.com/document/d/1QtkLtuYae5f9i9JbElRgRxiBs9IKnGqwhZJktwWxImA/edit?usp=sharing), shared via [20260506_174247_AlexeyDTC_msg3873.md](../../../inbox/used/20260506_174247_AlexeyDTC_msg3873.md).
[^2]: [20260506_200424_AlexeyDTC_msg3880_transcript.txt](../../../inbox/used/20260506_200424_AlexeyDTC_msg3880_transcript.txt) - Alexey's recommendations after reading the Q&A.
