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

- Current situation: Sai has a thorough conceptual design for the News Event Reminder Telegram bot - three flows (flagging, freshness check, day-of reminder), a four-table schema, a folder layout - but no code yet. Repo: [github.com/saig217/future-event-remainder](https://github.com/saig217/future-event-remainder).
- Goal for the next 6 weeks: a working version of the bot demoable on week 6, built in sync with the AI Engineering Buildcamp progression.
- Main gap to close: moving from conceptual plan to implementation. The conceptual step is essentially done. What is missing is a step-by-step build plan and the agent-building skills to execute it.
- Weekly time commitment: 15 hours per week, more on weekends - a strong fit for a 6-week build.
- Why this plan is the right next step: Sai is already a cloud data engineer with a thorough plan. He does not need more design. He needs to start shipping, ideally writing the agent and its tools himself rather than handing it to a coding agent, because the goal is to learn how agents work.

## Plan

## Focus

- Main focus: ship a working first version of the News Event Reminder bot in 6 weeks, in sync with the AI Engineering Buildcamp progression (concept → tools → tests → monitoring → evolution).
- Supporting focus: build the agent yourself rather than letting a coding assistant build it for you. The point is to learn how agents work end to end.
- Supporting focus: implement the underlying tools (event extraction, scheduler, freshness check) as plain Python functions first, then wire them into an agent that calls them.

## Timeline

Week 1:

- The conceptual work is already done - keep the three flows and four tables as the working design. Treat the architecture as a starting point, not a contract: small projects are easy to refactor as you go, so do not over-invest in getting the architecture perfect now.
- Pick one coding assistant for the supporting work (Claude Code, Codex, or similar). Avoid free tiers - hitting limits mid-session breaks momentum.
- Decide what gets built by hand and what gets delegated to the assistant. Default: write the agent loop, tool definitions, and prompt logic by hand. Let the assistant help with boilerplate (database models, Dockerfile, CI, fetcher cleanup).
- Start the Telegram bot skeleton: bot connects, accepts a forwarded message, replies with a placeholder. This is the smallest possible end-to-end loop.

Week 2:

- Implement the core extraction step as a plain function (no agent yet): given a URL, fetch the article, run an LLM call with a Pydantic schema, return the list of events with confidence labels. Cover the failure paths (invalid URL, fetch fail, LLM fail).
- Save extracted events to the database (`watched_stories` and `events` tables). Confirm the bot can flag an article end to end and reply with the list of events it will track.

Week 3:

- Add the scheduler. Wire APScheduler (or equivalent) so the day-of reminder fires at the right local time. At this point the system can flag, store, and remind - still without an agent in the loop.
- Add the day-of reminder Telegram message. Confirm the full Flow C path works.

Week 4:

- Now introduce the agent. Wrap the freshness-check logic into a single agent with two tools (`web_search`, `fetch_page`). Define the tools as plain Python functions with clear input/output schemas. Let the agent decide when to call them.
- Connect the freshness-check agent to Flow B (sanity check at flagging, weekly cron for events 7-60 days out, daily cron at 06:00 for events 1-2 days out). Log every tool call to the `agent_runs` table.
- This is the Buildcamp "tools" milestone for this project.

Week 5:

- Add tests. Pick the most important scenarios (article with one clear event, article with no future-dated events, article whose event gets postponed, article that becomes uncertain) and write end-to-end tests for them. The point is to lock down behaviour before adding more features.
- Add monitoring. The `agent_runs` table is already the foundation. Add a small dashboard or daily summary that surfaces failures, retries, and cost.
- This is the Buildcamp "tests" and "monitoring" milestones.

Week 6:

- Iterate on whatever the previous weeks surfaced - usually extraction quality, freshness-check confidence calibration, or reminder timing.
- Cut a tagged release on GitHub, update the README to show the architecture and how to run it locally, and prepare a short demo (screen recording or live walkthrough at the sprint demo).
- This is the Buildcamp "evolution" milestone.

## Project approach

Additional principles for taking a clean conceptual plan to a shipped first version:

- Build the agent yourself if the goal is to learn agents. It is fine to use a coding assistant for boilerplate, but the agent loop, tool definitions, and prompt logic are the parts where the learning lives. Letting Claude Code build the whole thing skips the lesson.
- Implement tools as plain functions first, then wrap them in an agent. If you can call `extract_events(url)` and `check_freshness(event)` directly and get the right answers, the agent's job becomes orchestration rather than first-pass logic. Debugging is far easier this way.
- Treat the architecture as adjustable, not fixed. Three flows and four tables is a reasonable starting point - if a flow turns out to be unnecessary or a table needs to split, change it. Do not freeze the design.
- Sync the build to the Buildcamp arc. Buildcamp goes concept → tools → tests → monitoring → evolution. The weekly plan above maps the bot onto that same arc, so the course content reinforces what you are building each week.
- Ship one project. The bot is the project for this sprint. Do not start a second one until V1 ships.

## Resources

- AI Engineering Buildcamp - already enrolled. The course modules are the primary reference. No extra courses needed.
- AI Hero - free, useful for filling in agent fundamentals if any module feels too dense. Cover whichever pieces (tool calling, agent loops, evaluation) feel weakest.
- [github.com/alexeygrigorev/telegram-writing-assistant](https://github.com/alexeygrigorev/telegram-writing-assistant) - reference repo for the shape of a Telegram-bot-plus-agent system. Skim for patterns (how messages are received, how the bot triggers downstream processing, how external tools are called) rather than copying code.
- Coding assistant of choice (Claude Code, Codex, or similar). Pick one and commit to a paid plan that fits 15 hours per week.

## Deliverables

- Telegram bot skeleton with end-to-end flag-and-reply path - by end of week 2.
- Day-of reminder firing reliably from the scheduler - by end of week 3.
- Freshness-check agent with two tools, logging to `agent_runs` - by end of week 4.
- End-to-end tests and a small monitoring view - by end of week 5.
- Tagged release, README, and demo ready - by end of week 6.

## Accountability

- Weekly check-in: what shipped, what is blocked, what is the goal for the next week. Sai named "weekly check-ins and fixed deliverables" as the format that works for him. The weekly goals above match that.
- 15 hours per week, more on weekends. The plan is sized to that budget. If a week slips, drop a stretch goal rather than extending the week.
- One project until it ships. The News Event Reminder bot is the only project until the demo.
- Share progress in the AI Shipping Labs Slack so other members can ask questions and learn from the agent-building decisions.

## Interview prep

Sai also asked for an interview prep plan. The shortest realistic answer: a shipped, well-evaluated project IS the interview prep.

Once V1 is running:

- Write a short README that explains the architecture, the trade-offs (why three flows, why four tables, why no agent in Flow A), and what you would change next. This is the answer to most "tell me about a project" interview questions.
- The community session ideas Sai already raised (recent AI Engineering interview questions, mock interviews, strategy for getting interview calls) are tracked in [community-session-ideas.md](../../community-session-ideas.md#ai-engineer-job-hunt-topics-sai-kumar-g) and will be planned as community-wide sessions rather than as part of the personal sprint.

## Next Steps

- [ ] [Sai] Pick a coding assistant (Claude Code or Codex) and confirm a paid plan that fits 15 hours per week.
- [ ] [Sai] Get the Telegram bot skeleton accepting forwarded messages by end of week 1.
- [ ] [Sai] Implement the extraction step as a plain function and store events in the database by end of week 2.
- [ ] [Sai] Share weekly progress in the AI Shipping Labs Slack.
- [ ] [Alexey] Send the written plan and confirm the AI Hero entry point for agent fundamentals if Sai wants the extra reading.
- [ ] [Valeriia] Confirm Sai is on the AI Shipping Labs Slack channel and added to the May sprint roster.

## Internal Context

## Persona

Sam - The Technical Professional Moving to AI (preliminary, to confirm). Sai has 2+ years as an Azure cloud data engineer and a clear project idea, but has not started building it yet. He is the classic data-engineer-moving-into-AI profile that fits Sam.

See [personas.md](../personas.md) for full persona definitions.

## Background

Sai Kumar G is a member of Alexey's AI Engineering cohort on Maven. He is a Cloud Data Engineer with two-plus years of experience in Azure data engineering. His goal for the AI Shipping Labs community is to stay updated with the latest AI tech without being overwhelmed by the noise on social platforms[^2].

LinkedIn: Sai Kumar G

GitHub (project repo, just started): [github.com/saig217/future-event-remainder](https://github.com/saig217/future-event-remainder)

He previously responded to Valeriia's outreach with topics he wanted the community to cover - recent AI Engineering interview questions, mock interviews and strategy for getting interview calls, and building personal projects - and framed his goal as: "I need the plan to build AI project and get the AI Engineer role". Captured in [community-session-ideas.md](../../community-session-ideas.md#ai-engineer-job-hunt-topics-sai-kumar-g).

## Intake

## Initial Input

I do have a two plus years of experience in Azure data engineering and my goals for this community is to stay updated with the latest AI tech without overwhelming updates from the social platforms[^2].

About the project: A Telegram bot that solves the problem of forgetting future-dated events buried inside news articles - court verdicts, product launches, earnings calls, sports rosters, movie releases - by extracting those events when a user forwards an article, scheduling reminders, and re-verifying each event 1-2 days before it fires to catch postponements or cancellations. The intended user is a heavy news consumer (initially himself) who follows AI, tech, markets, and sports across many sources and cannot manually track every "this will happen on date X" mention. The system uses the Telegram Bot API for input, a web fetcher and an LLM with structured output (Pydantic) for event extraction, a relational database for storage, a scheduler for reminders, and a freshness-check agent with web search and page-fetch tools. Output is Telegram messages: confirmation on flagging, proactive alerts when a date shifts, and the final reminder on the event day with a summary and source link[^2].

## Questions and Answers

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

- Flow A - Flagging (synchronous, user-triggered, ~5-15 seconds end-to-end). User forwards article, bot validates, fetcher cleans the article, dedup check by canonical_url, extraction LLM call returns ExtractionResult, events with confidence high or medium are saved with status=scheduled, low-confidence events are saved with status=pending_review and shown to the user for confirmation, bot replies with the list of events it will track. Failure paths: invalid URL means a friendly error reply. Fetch fails means asking the user to paste text. LLM call fails means retry once with exponential backoff and then surface the error. No events found means tell the user honestly without fabrication.
- Flow B - Freshness check (async, scheduled, runs at three cadences). Triggers: at flagging time for any event more than 7 days out (sanity check). Weekly cron for events 7-60 days out (catch early postponements). Daily cron at user 06:00 for events 1-2 days out (final verification before reminder). The agent uses two tools (web_search and fetch_page) and returns one of: unchanged, date_changed, cancelled, completed_early, uncertain. Each tool call is logged to agent_runs with cost and latency. Decision policy: unchanged means no action. Date_changed means update plus alert. Cancelled or completed_early means archive plus alert. Uncertain means schedule a re-run if the event is more than 2 days out, otherwise escalate to the user with explicit keep/cancel/recheck choice.
- Flow C - Day-of reminder (async, scheduled, runs daily at user 08:00). For events firing today: compose reminder, send Telegram message with summary plus source link plus inline buttons (Mark done / Snooze 1 day), update events.status=fired. Failures retry 3 times with backoff, then alert admin.

Schema (four tables): watched_stories is one row per flagged article. Events is one row per future-dated event extracted from a story (an article can have multiple). Event_history logs every change detected (postponement, cancellation, completion). Agent_runs is the observability table - every LLM call writes one row with decision, tool calls, cost, and latency. The agent_runs table is intended to make monitoring straightforward.

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

## Meeting Notes

No intake call yet - input collected via the Google Doc[^2].

## Internal Recommendations

Alexey's recommendations after reviewing Sai's intake[^3]:

1. The Telegram bot idea is great. The conceptual work is already strong - Sai has thought through the three flows, four tables, and even the folder layout. The first step (concept) is essentially done. It is time to implement.

2. Don't overthink the architecture. It looks reasonable at first pass. The project is small enough that the architecture can change as you go - if a flow turns out unnecessary or a table needs to split, fix it then. The principle: if it works, the architecture is right.

3. 6 weeks is realistic for a working version, and 15 hours per week is a strong fit. There is no need to recommend additional courses on top of Buildcamp - Sai is already enrolled, and Buildcamp covers everything needed for the build.

4. Sync the bot's build to the Buildcamp progression: concept → tools → tests → monitoring → evolution. Each Buildcamp milestone maps onto a milestone for the bot, so the course content directly supports the project.

5. On framework choice: better to start without a coding agent doing the agent work for you, if the goal is to learn how agents work. Writing the agent loop, defining the tools (ScheduleReminder, VerifyFreshness, etc.), and wiring them together is where the learning lives. Using an AI assistant for boilerplate is fine.

6. For agent fundamentals, AI Hero is a good entry point if any Buildcamp module feels too dense.

7. The [telegram-writing-assistant repo](https://github.com/alexeygrigorev/telegram-writing-assistant) is a useful reference for the shape of a Telegram-bot-plus-agent system - skim for patterns rather than copy code. It is optional, not required.

8. Build pattern: implement the underlying logic (event extraction, freshness check) as plain Python functions first - call them directly from the bot before introducing an agent. Once the functions work, wrap them in an agent that decides when to call which one. This is far easier to debug than starting with an agent.

9. Interview prep is best treated as a side effect of the shipped project rather than a parallel track. A working, well-evaluated bot plus a clear README that explains the trade-offs is the strongest answer to most interview questions. The community already has Sai's broader interview-prep requests (recent AI Engineering interview questions, mock interviews, strategy for getting interview calls) captured in [community-session-ideas.md](../../community-session-ideas.md#ai-engineer-job-hunt-topics-sai-kumar-g) and those will be planned as community-wide sessions.

## Internal Action Items

- [ ] [Alexey] Send Sai the written plan.
- [ ] [Alexey] Confirm the AI Hero entry point for agent fundamentals if Sai wants the extra reading.
- [ ] [Valeriia] Confirm Sai is on the AI Shipping Labs Slack channel and added to the May sprint roster.

## Sources

[^1]: [20260430_162055_AlexeyDTC_msg3794.md](../../../inbox/used/20260430_162055_AlexeyDTC_msg3794.md) - shared as plan number 11.
[^2]: [Sai Kumar G's intake (Google Doc)](https://docs.google.com/document/d/1417RoEHm0VH52R8iFjXTBDlMpRGTRgjJVEz3LDEityU/edit?usp=sharing)
[^3]: [20260502_174950_AlexeyDTC_msg3825_transcript.txt](../../../inbox/used/20260502_174950_AlexeyDTC_msg3825_transcript.txt)
