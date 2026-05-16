---
title: "Plan: Koray Can Canut"
created: 2026-04-30
updated: 2026-05-02
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Koray Can Canut

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: Koray has a working Telegram nutrition bot ([@koraycan_bot](https://t.me/koraycan_bot), repo: [compileandrun/nutrient_bot](https://github.com/compileandrun/nutrient_bot)) that logs meals from photos or text via OpenAI vision, stores logs in BigQuery, runs serverless on Google Cloud Run, and recommends foods to fill daily nutrient gaps. Estimation accuracy is the weak spot, recommendations feel raw, and there is no systematic way to measure prompt or model changes.
- Goal for the next 6 weeks: build a real evaluation pipeline for the bot, add a small set of agentic decisions and end-to-end tests, and ship a measurably better version of the bot that can be shared as a portfolio piece.
- Main gap to close: a systematic way to measure quality. Right now changes to prompts, models, or temperature land without a quality signal. Once an evaluation loop is in place, every other improvement (agentic behaviour, fuzzy nutrient lookup, recommendations) can be validated.
- Weekly time commitment: 20 hours in week 1 (before the freelance gig starts on May 4), then 2 hours per week through the rest of the sprint.
- Why this plan is the right next step: he already has a deployed end-to-end product. The use now is concept and structure (evaluation, agentic scenarios planned ahead, tests) rather than building more features. The plan front-loads the conceptual work into the high-time week so the 2-hour weeks have unambiguous tasks - and when 2 hours isn't enough, a coding agent can do most of the implementation as long as the plan is concrete.

## Plan

## Focus

- Main focus: build an offline evaluation pipeline for nutrient_bot - representative scenarios, manual labels, and an LLM judge aligned with those labels.
- Supporting focus: add a few targeted end-to-end tests in test-driven-development style for specific scenarios (blurry photo handling, accidental duplicate, non-food image).
- Supporting focus: pre-design the agentic decisions on paper or with ChatGPT before implementing them (clarify on unclear photo, skip recommendation when daily targets are met, duplicate detection).

## Timeline

Week 1 (~20 hours):

- The most important task this week is to maximally understand the plan. Read every step until each weekly task is concrete enough that you (or a coding agent) can pick it up cold and execute it. The 2-hour weeks depend on this preparation - the better the plan is understood now, the less thinking is needed when time is short later.
- Use the high-time window to plan everything the rest of the sprint will execute. When the 2-hour weeks start, every step should already be decided.
- Define what "good" means for the bot. Be explicit and write it down: when is an estimation acceptable, when is a recommendation acceptable, when does the bot need to ask for clarification. This becomes the rubric for both manual labelling and the LLM judge.
- Draft 15-20 evaluation scenarios using equivalence partitioning (see Resources). Cover the meal types the bot should handle (single dish, mixed plate, drinks, snacks), wrong terminology, blurry or partial photos, multi-meal photos, non-food photos, edge cases like small or large portions, and cases where today's targets are already met.
- Plan the agentic decisions on paper or with ChatGPT (using voice/dictation while commuting works well for this kind of conceptual work). For each decision, write down: when does it trigger, what does the bot do, and how would you test it. Don't implement yet.
- Decide which features are in scope for this 6-week sprint and which to defer. Reasonable scope: evaluation pipeline + 1-2 agentic decisions + a couple of TDD-style tests. Out of scope: full RAG, multi-agent rewrite, new platforms.

Week 2 (~2 hours):

- Run the 15-20 scenarios manually through the current bot and record the outputs (input, output, cost). A simple script that loops over a CSV of scenarios and saves results to JSON is enough.
- Label each result good or bad against the rubric from week 1. Note the failure type for the bad ones (hallucinated nutrient values, wrong portion estimate, missed clarification, etc.). This is the gold standard dataset.

Week 3 (~2 hours):

- Build an LLM judge: a prompt that takes the question, the bot's response, and outputs a label plus reasoning (reasoning before label, so it has to think first).
- Run the judge over the labelled scenarios and compare with the human labels - count agreements and disagreements.
- Tweak the judge prompt to address the patterns where it disagrees, without overfitting to specific scenarios.

Week 4 (~2 hours):

- Add a couple of TDD-style integration tests for the most important scenarios (e.g. blurry photo → bot asks for a clearer image, non-food photo → bot returns a parse error, accidental duplicate within a few seconds → handled correctly). These are different from the eval set: they should always pass and protect against regressions.

Week 5 (~2 hours):

- Implement one or two of the agentic decisions designed in week 1. Good first targets: "if image confidence is low, ask for a clearer photo before logging" and "if today's nutrient gaps are small, skip the recommendation rather than fabricate one".
- Re-run the eval pipeline and the integration tests. Confirm the changes improved the judge score and didn't break anything.

Week 6 (~2 hours):

- Tighten what is left. Update the README to describe the eval pipeline and the agentic behaviour. Add a short note about the Cloud Run + BigQuery deployment - other AI Shipping Labs members have asked about this and a small write-up would be valuable both for them and for Koray's own portfolio.
- Decide the next iteration: deeper evaluation, a lightweight nutrient-table search (see Resources), or a portfolio write-up post.

## When 2 hours isn't enough

Two hours is tight. The plan is sized for it, but a given week might not fit.

The fallback:

- Hand the week's task to a coding agent. The week-1 plan is detailed enough that the agent has a concrete spec to implement. Run the agent, check what it produced, correct the parts that drift from the plan, and ship.
- Use commute and walking time for the conceptual work. Voice/dictation conversations with ChatGPT or Claude are fine for thinking through scenarios, agentic decisions, and prompt tweaks. Save the desk time for execution.
- The week-1 deep read of the plan is what makes both fallbacks work. If the plan is fuzzy, the agent will produce something fuzzy and the commute thinking will go in circles. If the plan is concrete, both fallbacks are productive.

## Project approach

Additional principles for taking nutrient_bot to a measurably better state. Koray is already doing several of these. Treat this as a checklist, not a rebuild.

- One project at a time. nutrient_bot is the project for this sprint. Don't start a second one until V1 of the eval-and-agentic upgrades is shipped.
- Frame the work as current state to target state. Current state: working bot, no quality signal, raw recommendations. Target state: working bot with a measured quality signal, a few agentic decisions, and tests that protect against regressions. The weekly plan is the delta.
- Concept first, implementation second. The conceptual work (defining "good", scenario design, agentic decision design) is the part Koray needs to own. LLMs can implement most of the code, but understanding evaluation as a concept is a skill that transfers across every project from here on.
- Use commute and walking time for conceptual work. Voice/dictation conversations with ChatGPT or Claude are fine for designing scenarios and agentic decisions. Save the desk time for implementation.
- Keep the gym. Energy comes from training and simple food, not from skipping them to study more. Two hours in the gym beats two hours of forced learning.
- Ship one thing end-to-end before adding new layers. Eval pipeline first, then agentic behaviour, then maybe lightweight search - not all in parallel.

## Resources

- Coding assistant of choice (Claude Code or Codex). Both are fine. Pick one and commit. Avoid free tiers - hitting limits mid-session breaks 2-hour weeks. The same agent is also the fallback for weeks where 2 hours isn't enough to do the work by hand.
- AI Engineering Buildcamp evaluation module (week 6). The core idea to take from it: equivalence partitioning - divide the input space (here: meal photos and text descriptions) into groups where you'd expect similar bot behaviour, then cover each group with at least 2-3 scenarios. Add edge cases (out-of-scope, deliberately confusing inputs) on top. Result: 15-20 scenarios that give a real signal, not 1000 cherry-picked examples.
- Eugene Yan on LLM evaluation and on AlignEval - good external reading for the eval mindset (label some data, align an LLM judge against it, then trust the judge for the next runs).
- minsearch ([github.com/alexeygrigorev/minsearch](https://github.com/alexeygrigorev/minsearch)) - a lightweight search engine that fits the use case far better than full RAG. If a fuzzy nutrient-table lookup or recommendation lookup is added later, minsearch is a sensible starting point - cheap, simple, easy to host alongside the existing Cloud Run setup.
- LLM Zoomcamp (free) - for the broader RAG/agent context if the project later grows in that direction. Not needed for this sprint.

## Deliverables

- A documented evaluation rubric and a set of 15-20 scenarios with manual labels - by end of week 2.
- An LLM judge aligned against the manual labels, with reported agreement metrics - by end of week 3.
- A side-by-side experiment comparing at least two configurations (model, temperature, or prompt variant) using the judge - by end of week 4.
- One or two agentic decisions implemented and validated through the eval pipeline - by end of week 5.
- An updated README covering the eval pipeline, the new agentic behaviour, and a short note on the Cloud Run + BigQuery setup - by end of week 6.

## Accountability

- Weekly check-in: what shipped, what is blocked, what is the goal for the next week. Koray named milestones plus deadlines and peer discussion as the formats that work for him.
- 20 hours in week 1, then 2 hours per week. The plan is sized for those 2-hour weeks - if a week slips, drop a stretch goal or hand the implementation to a coding agent rather than extending the week.
- One project. Nutrient_bot only until the sprint demoes. Don't start a second project mid-sprint.
- Share progress in the AI Shipping Labs Slack rather than only one-on-one. Other members have asked about Cloud Run deployments and would benefit from seeing how Koray's bot is set up.

## Career direction note

Koray asked whether the data analyst → junior data engineer or junior AI engineer move is realistic. The honest answer: yes, but the strongest evidence is a shipped, evaluated AI product. nutrient_bot already has the deployment story (Cloud Run, BigQuery, serverless, multi-user). Adding evaluation, agentic decisions, and tests turns it into a portfolio piece that demonstrates the engineering discipline employers screen for. Once the sprint wraps, a short write-up of the eval-and-agentic upgrade and a LinkedIn post about the Cloud Run setup are both natural follow-ups.

## Next Steps

- [ ] [Koray] Pick a coding assistant (Claude Code or Codex) and commit to a paid plan that fits the 2-hour weeks (and serves as the fallback when 2 hours isn't enough).
- [ ] [Koray] Use week 1 (20 hours) to read the plan deeply, write the evaluation rubric, draft the 15-20 scenarios, and design the agentic decisions on paper.
- [ ] [Koray] Share progress in the AI Shipping Labs Slack at the weekly check-in cadence.
- [ ] [Alexey] Send the written plan and point Koray at the Buildcamp evaluation module location.
- [ ] [Valeriia] Confirm Koray is on the AI Shipping Labs Slack channel and added to the May sprint roster.

## Internal Context

## Persona

Sam - The Technical Professional Moving to AI. Koray is a data analyst / analytics engineer (5-6 years) who has built an end-to-end AI product but self-describes the gap as "Python still needs improvement, LLM does all the coding, I just try to understand what it's doing." That's the classic Sam scripts-to-systems gap, even though the deployed bot is more sophisticated than the typical Sam baseline.

See [personas.md](../personas.md) for full persona definitions.

## Background

Koray is a former student of Alexey's Data Engineering Zoomcamp (2024 cohort). He met Alexey in person in Berlin and trusts him, which is why he is trying AI Shipping Labs. He has been job-hunting, has a five-month full-time freelance gig starting May 4, 2026 (running through October 15, 2026), and signed up to AI Shipping Labs partly as a small token of appreciation for what he got from the free Zoomcamp[^1].

His personal project, nutrient_bot, accepts meal photos or text descriptions, analyses macros and micronutrients with OpenAI vision, stores logs in BigQuery, and runs on Google Cloud Run. The bot has /start, /today, /recommend commands, supports multi-user use, has WHO/FDA-based daily limits, tracks token costs, and includes hard caps to prevent runaway API spend. The repo includes a one-shot deploy.sh that handles Docker build, registry push, Cloud Run deploy, and Telegram webhook registration[^repo].

His freelance gig starts May 4, 2026, so the 20-hour first week is the gap before that, and the 2-hour weeks run alongside the freelance load.

The plan number in the inbox marks this as the 10th personalised plan in the current batch[^1].

## Intake

The intake is the Google Doc with Koray's input collected ahead of this plan[^1]. The meeting notes from the call with Valeriia are in a separate Google Doc[^1]. The same content is captured in [interviews/koray-can-canut.md](../interviews/koray-can-canut.md).

Highlights from the answers:

- One-week trial framing initially, but he is open to staying if the value is there.
- Concrete week-1 outcome (his framing): test the bot's estimation, then improve it while keeping costs under a threshold.
- 6-8 week framing (his framing): a plan for what to learn about AI engineering and cloud tools to test/deploy/monitor.
- Self-described main blockers: time, learning curve not steep enough, want a strict mentor.
- Wanted help: weekly roadmap of things to learn or build, distinction between "core skills (without LLM help)" and "things to do with LLM", peer discussion or group learning, milestones and deadlines.
- Career questions: realistic chance at junior AI engineer / junior data engineer roles, portfolio strategy, LinkedIn visibility strategy.

## Internal Recommendations

Alexey's recommendations after reviewing Koray's input and his bot's repo[^2]:

1. The project is genuinely good and the deployment story (Cloud Run + BigQuery) is rare enough in the community that it is worth surfacing. Koray should share the project on Slack, not just one-on-one with Alexey - other members are interested in Cloud Run patterns and would learn from it. The same channel gives him peer review back.

2. The "improve estimation" goal maps almost exactly to evaluation. The right next step is not to chase better prompts blindly - it's to build an eval pipeline first, so prompt/model/temperature changes can be measured. The Buildcamp evaluation module (homework on equivalence partitioning) is the conceptual reference. The principle to extract is "divide the input space into groups, cover each group with a few scenarios, then label and align an LLM judge against the manual labels."

3. Agentic behaviour is mostly a planning problem. Koray's instinct is right: clarify on unclear photos, skip recommendations when daily targets are met. The work to do upfront is to enumerate the scenarios on paper or with ChatGPT before implementing ("продумать все сценарии до того, как ты имплементируешь агента") so the implementation phase is mechanical.

4. Rule-based deduplication is a natural fit for an LLM check. He can keep the rule-based logic and add a light LLM check on top for the cases the rule misses. Cost/latency vs precision trade-off is something to measure once eval is in place.

5. RAG is overkill for the current bot. minsearch is the recommended drop-in if a lightweight food-table lookup or a recommendation lookup is needed - it's simple, hostable on the existing Cloud Run setup, and avoids the embedding/vector-db tax. Worth a look once eval and agentic behaviour are in place.

6. Tests in addition to evaluation. A few TDD-style integration tests for the highest-stakes scenarios (blurry photo, non-food, duplicate within seconds) protect against regressions in a way the eval set does not. Be careful with agent-written tests - they will mock things they shouldn't. Review what gets mocked.

7. Time strategy: use the 20-hour week to plan thoroughly and to read the resulting plan deeply. The conceptual decisions (eval rubric, scenarios, agentic decisions) made in week 1 should be detailed enough that the 2-hour weeks are implementation-only. When 2 hours isn't enough, the same plan is concrete enough to hand to a coding agent and then check + correct the output. Concept-heavy work (designing scenarios, talking through edge cases) can also be done while commuting via voice/dictation with ChatGPT.

8. Don't drop the gym. Energy comes from training and simple food. Two hours in the gym beats two hours of grinding code with no energy left over.

9. Focus on one project. Don't start a second project mid-sprint. After the freelance gig ends in October he can decide whether to take on a second.

10. AI Hero is good if there are gaps - check it for areas (RAG, agents, testing, monitoring, evaluation) where Koray feels weakest. Buildcamp's RAG/agents/testing/monitoring/evaluation modules cover the same ground in more depth.

11. LinkedIn visibility plan is a good idea - the Cloud Run write-up alone would be a strong post once the eval-and-agentic upgrade ships.

Adjustments to the plan after the first pass[^4]:

- The weekly time commitment is 2 hours per week alongside the freelance gig, not 4. Update every reference accordingly.
- Drop the "pre-sprint" framing on week 1 - it confuses people. Week 1 is just week 1, and the 20-hour budget is what makes it different.
- Be concrete with Koray about what to do when 2 hours isn't enough: hand the week's task to a coding agent (the plan should be detailed enough by then to use as the spec), check what the agent produced, and correct the parts that drift. Don't extend the week.
- The most important task in week 1 is to understand the plan deeply enough that the 2-hour weeks (and the agent fallback) work. Make this explicit so the planning week doesn't get spent only on rubric/scenario/agentic-decision drafts.
- Conceptual work can be done during free time - while commuting, walking, or otherwise away from the desk - via voice/dictation with ChatGPT or Claude.

## Internal Action Items

- [ ] [Alexey] Send Koray the written plan and point him at the Buildcamp v2 evaluation module (location to confirm once it's on the AI Shipping Labs platform).
- [ ] [Alexey] Mention Koray's Cloud Run + BigQuery setup in the Slack as a reference for other members asking about that deployment pattern.
- [ ] [Valeriia] Confirm Koray is on the AI Shipping Labs Slack channel and the May sprint roster.
- [ ] [Valeriia] Ask Alexey about the policy for removing dropped members from the Slack channel and notify Koray (open question from the call[^3]).

## Sources

[^1]: [20260429_155342_AlexeyDTC_msg3761.md](../../../inbox/used/20260429_155342_AlexeyDTC_msg3761.md), [Koray's Answers (Google Doc)](https://docs.google.com/document/d/1UItdFnW6F5TNpMzYdI3MhfnV1-dRD1wv4lA8RdTVEpk/edit?usp=sharing), [Meeting Notes (Google Doc)](https://docs.google.com/document/d/1sqqWHwPP01b-q_66vv9yOiWup9mB-zzuf8WQY605SRw/edit?usp=sharing)
[^2]: [20260430_085223_AlexeyDTC_msg3767_transcript.txt](../../../inbox/used/20260430_085223_AlexeyDTC_msg3767_transcript.txt)
[^3]: [Meeting Notes (Google Doc)](https://docs.google.com/document/d/1sqqWHwPP01b-q_66vv9yOiWup9mB-zzuf8WQY605SRw/edit?usp=sharing)
[^4]: [20260502_180319_AlexeyDTC_msg3834_transcript.txt](../../../inbox/used/20260502_180319_AlexeyDTC_msg3834_transcript.txt)
[^repo]: [github.com/compileandrun/nutrient_bot](https://github.com/compileandrun/nutrient_bot), [@koraycan_bot](https://t.me/koraycan_bot)
