---
title: "Plan: Sai Kumar G"
created: 2026-05-02
updated: 2026-05-02
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Sai Kumar G

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

Pending Alexey's review of Sai's intake.

## Plan

Pending. Once Alexey records his recommendations, fill the Focus, Timeline, Resources, Deliverables, Accountability, and Next Steps sections following the [plan template](_plan.md).

## Internal Context

### Persona

Sam - The Technical Professional Moving to AI (preliminary, to confirm). Sai has 2+ years as an Azure cloud data engineer and a clear project idea, but has not started building it yet. He is the classic data-engineer-moving-into-AI profile that fits Sam.

See [personas.md](../personas.md) for full persona definitions.

### Background

Sai Kumar G is a member of Alexey's AI Engineering cohort on Maven. He is a Cloud Data Engineer with two-plus years of experience in Azure data engineering. His goal for the AI Shipping Labs community is to stay updated with the latest AI tech without being overwhelmed by the noise on social platforms[^2].

LinkedIn: Sai Kumar G

GitHub (project repo, just started): [github.com/saig217/future-event-remainder](https://github.com/saig217/future-event-remainder)

He previously responded to Valeriia's outreach with topics he wanted the community to cover - recent AI Engineering interview questions, mock interviews and strategy for getting interview calls, and building personal projects - and framed his goal as: "I need the plan to build AI project and get the AI Engineer role". Captured in [community-session-ideas.md](../../community-session-ideas.md#ai-engineer-job-hunt-topics-sai-kumar-g).

### Intake

#### Initial Input

I do have a two plus years of experience in Azure data engineering and my goals for this community is to stay updated with the latest AI tech without overwhelming updates from the social platforms[^2].

About the project: A Telegram bot that solves the problem of forgetting future-dated events buried inside news articles - court verdicts, product launches, earnings calls, sports rosters, movie releases - by extracting those events when a user forwards an article, scheduling reminders, and re-verifying each event 1-2 days before it fires to catch postponements or cancellations. The intended user is a heavy news consumer (initially himself) who follows AI, tech, markets, and sports across many sources and cannot manually track every "this will happen on date X" mention. The system uses the Telegram Bot API for input, a web fetcher and an LLM with structured output (Pydantic) for event extraction, a relational database for storage, a scheduler for reminders, and a freshness-check agent with web search and page-fetch tools. Output is Telegram messages: confirmation on flagging, proactive alerts when a date shifts, and the final reminder on the event day with a summary and source link[^2].

#### Questions and Answers

1. What do you hope to achieve with this plan in the next 6 to 8 weeks?

A working project for a strong portfolio that he can explain in interviews, plus an interview prep plan if possible[^2].

2. If you had to choose one concrete outcome for the next 6 weeks, what should it be?

To be able to complete the project successfully in sync with his weekly learnings from Buildcamp[^2].

3. How much time can you realistically commit each week over the next 6 to 8 weeks?

Around 15 hours a week for the project. More time on weekends[^2].

4. What is the current state of the News Event Reminder Bot?

The project is just planned. No code work has started[^2].

5. What have you already built or tested?

Project not started[^2].

6. What part of the project feels most important to build first?

Telegram bot working[^2].

7. What new skills do you want to develop through this project?

Agents with tool calling, evaluation, and product thinking[^2].

8. What is blocking you most right now from moving forward?

Unclear architecture and weekly artifacts he should complete[^2].

9. What kind of AI updates would be useful for you?

A small weekly reading list and practical tools[^2].

10. What type of accountability would be most effective for you?

Weekly check-ins and fixed deliverables[^2].

11. What would make you feel that, at the end of the next 6 to 8 weeks, the plan was worthwhile?

Having a strong portfolio project[^2].

12. Is there anything else Alexey should know before preparing the plan?

He has a planned architecture and would like input on whether it is correct[^2]. The proposal:

The three flows:

- Flow A - Flagging (synchronous, user-triggered, ~5-15 seconds end-to-end). User forwards article, bot validates, fetcher cleans the article, dedup check by canonical_url, extraction LLM call returns ExtractionResult, events with confidence high or medium are saved with status=scheduled, low-confidence events are saved with status=pending_review and shown to the user for confirmation, bot replies with the list of events it will track. Failure paths: invalid URL means a friendly error reply; fetch fails means asking the user to paste text; LLM call fails means retry once with exponential backoff and then surface the error; no events found means tell the user honestly without fabrication.
- Flow B - Freshness check (async, scheduled, runs at three cadences). Triggers: at flagging time for any event more than 7 days out (sanity check); weekly cron for events 7-60 days out (catch early postponements); daily cron at user 06:00 for events 1-2 days out (final verification before reminder). The agent uses two tools (web_search and fetch_page) and returns one of: unchanged, date_changed, cancelled, completed_early, uncertain. Each tool call is logged to agent_runs with cost and latency. Decision policy: unchanged means no action; date_changed means update plus alert; cancelled or completed_early means archive plus alert; uncertain means schedule a re-run if the event is more than 2 days out, otherwise escalate to the user with explicit keep/cancel/recheck choice.
- Flow C - Day-of reminder (async, scheduled, runs daily at user 08:00). For events firing today: compose reminder, send Telegram message with summary plus source link plus inline buttons (Mark done / Snooze 1 day), update events.status=fired. Failures retry 3 times with backoff, then alert admin.

Schema (four tables): watched_stories is one row per flagged article; events is one row per future-dated event extracted from a story (an article can have multiple); event_history logs every change detected (postponement, cancellation, completion); agent_runs is the observability table - every LLM call writes one row with decision, tool calls, cost, and latency. The agent_runs table is intended to make monitoring straightforward.

File / folder layout:

```
news-event-tracker/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── pyproject.toml
├── .env.example
├── src/
│   ├── bot/              # Telegram handlers, message composition
│   ├── ingestion/        # Fetcher, cleaner, deduplication
│   ├── extraction/       # LLM extraction, Pydantic schemas
│   ├── agent/            # Freshness-check agent + tools
│   ├── scheduler/        # APScheduler setup, cron jobs
│   ├── storage/          # SQLAlchemy models, migrations
│   ├── monitoring/       # Streamlit dashboard, log shippers
│   └── config.py
├── tests/
│   ├── unit/
│   ├── fixtures/
│   └── judge/
└── evals/
    ├── ground_truth.jsonl
    └── run.py
```

### Meeting Notes

No intake call yet - input collected via the Google Doc[^2].

### Internal Recommendations

Pending. Items Alexey will likely want to weigh in on once he reviews the doc:

- Whether the proposed architecture (three flows, four tables) is right for a 6-week build, or whether the first version should ship with a smaller scope.
- Where to start: Telegram bot skeleton, then extraction, then scheduler, then freshness check.
- Whether interview prep should be a parallel weekly thread or sequenced after the project ships.
- The community already has the Sai-Kumar-G request for interview questions / mock interviews / strategy for interview calls captured in [community-session-ideas.md](../../community-session-ideas.md#ai-engineer-job-hunt-topics-sai-kumar-g) - decide whether any of that can be folded into the plan.

### Internal Action Items

- [ ] [Alexey] Review the intake doc and the proposed architecture; record voice notes with recommendations.
- [ ] [Alexey] Decide whether to use the proposed three-flow / four-table architecture as-is, simplify it, or recommend a different first-version scope.
- [ ] [Valeriia] Confirm Sai is on the AI Shipping Labs Slack channel and added to the May sprint roster.

### Sources

[^1]: [20260430_162055_AlexeyDTC_msg3794.md](../../../inbox/used/20260430_162055_AlexeyDTC_msg3794.md) - shared as plan number 11.
[^2]: [Sai Kumar G's intake (Google Doc)](https://docs.google.com/document/d/1417RoEHm0VH52R8iFjXTBDlMpRGTRgjJVEz3LDEityU/edit?usp=sharing)
