---
title: "Plan: Eva Mareckova"
created: 2026-05-19
updated: 2026-05-19
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Eva Mareckova

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: already operating at a very high level - orchestrates Claude Code daily at production scale across a multi-app enterprise engagement and a personal stack of 5+ apps, has shipped a multi-tenant SaaS to Hetzner production, and already has a concrete Phase 01-05 launch plan for her own product.
- Goal for the next 6 weeks: ship Tier 1 MVP of the Compound Practice Kit by Tuesday June 30, 2026 with 10-20 paying buyers and a working install loop in each buyer's vault.
- Main gap to close: distribution + packaging mechanics for non-developer buyers - shipping Python as a self-installable product across Windows/macOS/Linux without engineering hand-holding.
- Weekly time commitment: 5 to 10 hours per week.
- Why this plan is the right next step: Eva already has the build skill and the spec discipline. The sprint's value is structure, weekly accountability, and a community of testers to pressure-test the install flow before launch day.

## Plan

## Focus

- Main focus: protect the 5 to 10 hour weekly slot against the client engagement so the Phase 01-05 cadence holds all the way to June 30.
- Supporting focus: close the distribution gap - figure out the cleanest path from Gumroad/Stripe checkout to a working capture loop in the buyer's vault in under 15 minutes.
- Supporting focus: use the community as a cross-platform tester pool ahead of launch.

## Timeline

Eva already has Phase 01-05 milestones with hard dates. The weeks below align to those dates instead of overwriting them. Each week ends with a community-visible checkpoint (Slack update, live meeting, or demo) so the cadence holds the calendar slot.

Week 1 (May 19 to May 23):

- Ship Phase 01: BUG_LEDGER template, capture.py, select.py. First Saturday wave build.
- Phase 01 demoable artifact on May 23 - capture entry + selector surfacing high-signal entry, end to end.
- Slack intro in the cohort - share who you are, the project, and the June 30 launch date so the sprint group sees the arc.

Week 2 (May 24 to May 30):

- Phase 02 polish: tighten the templates, smooth the install copy, write the README for non-developer buyers.
- Phase 02 demoable artifact on May 30.
- Decision point: stay on pure Python distribution or seriously consider compiling a small native binary (see Resources). The earlier the call, the less rework.

Week 3 (May 31 to June 6):

- Distribution deep dive: pick the Gumroad or Stripe flow, work out file delivery + license + install email + first-session walkthrough.
- Document the "buyer runs it on Windows / macOS / Linux and it must Just Work" path end to end, including the failure-mode email when something breaks.
- Weekly Slack update on which platform showed friction first - this is where community testers can help next week.

Week 4 (June 7 to June 13):

- Phase 03 build: post-purchase delivery automation working end to end on at least two of three platforms.
- Mid-sprint demo on June 13 - the buyer flow, not just the scripts. Walk through "I just bought it, what happens next."
- Hand a free copy to two or three cohort members for a real install test (cross-platform: at least one Windows and one macOS).

Week 5 (June 14 to June 20):

- Phase 04 build: worked examples shipped alongside the Kit, plus the landing page and launch-week communication draft.
- Phase 04 demoable artifact on June 20 - polished install walkthrough plus the public-facing landing page.
- Incorporate the cross-platform feedback from week 4 testers. Fix the worst friction point first.

Week 6 (June 21 to June 27):

- Phase 05 pre-launch demo on June 27 - the full buyer journey from landing page to working capture loop, end to end.
- Final pre-launch verification pass. Lock scope - no new features past this point.
- Soft-launch communication ready to send Tuesday June 30.

Launch (June 28 to June 30):

- Tuesday June 30 launch at the early-bird price.
- Sprint demo doubles as the launch recap once the first buyers come through.

## Resources

- [Stripe Payment Links](https://stripe.com/payments/payment-links) - lower-friction alternative to Gumroad if the buyer flow needs more control.
- [Gumroad seller docs](https://help.gumroad.com/) - faster path to a working purchase + delivery + license email if Stripe feels heavy for v1.
- [PyInstaller](https://pyinstaller.org/) - if pure Python distribution is the right call, this is the standard one-binary path.
- Rust as a fallback for cross-platform distribution: Alexey has shipped projects compiled for Windows, macOS, and Linux in Rust without learning the language deeply. Useful as a backup if the Python install path keeps breaking on non-developer machines. Avoid .NET because it is Windows-only.

## Deliverables

- Phase 01 through Phase 05 demoable artifacts at the dates above.
- Tier 1 MVP shipped Tuesday June 30 with 10 to 20 paying buyers.
- Working "purchase to first capture in under 15 minutes" flow validated on at least two operating systems by community testers.
- Documented install instructions written for an operator who uses Obsidian, not an engineer who reads code.

## Accountability

- Default sprint cadence: weekly Slack update, weekly live meeting, weekly deliverable.
- Stronger commitment: demoable artifact every two weeks (May 23 / May 30 / June 13 / June 20 / June 27) so each Phase has a forcing function.
- Accountability partner pairing: Nirajan Acharya is the closest match in the cohort - already has a deployed AI project with a concrete next-step plan, similar profile of "advanced builder with their own arc." Worth a 30-minute intro call.
- Community testers in week 4 to 5 for real cross-platform installs.

## Next Steps

- [ ] [Eva] Read the plan and flag any week where the date / scope does not match her own Phase plan.
- [ ] [Eva] Decide by end of week 2 whether the distribution path stays pure Python or moves to a native binary.
- [ ] [Alexey] Intro Eva to Nirajan Acharya for an accountability pairing conversation.
- [ ] [Valeriia] Recruit two to three cross-platform testers from the cohort (at least one Windows and one macOS) for week 4.

## Internal Context

## Persona

Undetermined. Eva sits outside the standard archetypes - she is closer to a senior operator-builder using the sprint as external accountability and cohort observation than to anyone in Alex / Priya / Sam / Taylor. The plan reflects that: the value Alexey expects to add is structure and community, not technical instruction.

## Background

Eva Mareckova - Czech operator/builder running a multi-app enterprise engagement and her own AICENTURIA AI-driven business operating system (50+ agents across 5 functional teams). LinkedIn: [evamareckova](https://www.linkedin.com/in/evamareckova/).

Stack: React + TypeScript + Vite + Tailwind + shadcn frontend, FastAPI + Pydantic backend, Docker + Caddy + Cloudflare Tunnel deployment, SQLite + PostgreSQL via SQLAlchemy, GSD spec-driven development discipline. Production deploy on Hetzner LIVE for one client app since April 30 (18+ days uptime). Daily user of Claude Code Terminal, Cowork, Claude in Chrome, Anthropic Skills + custom subagents.

The sprint project (Compound Practice Kit) productizes her own BUG_LEDGER / LESSONS_LEDGER methodology - a structured capture-and-publish loop running in Obsidian, packaged as Python scripts + Markdown templates that operators install in their own vault.

## Intake

## Initial Input

Eva's full intake doc is the Google Doc linked in Sources. Twelve structured questions with detailed answers, including the Phase 01-05 plan, the June 30 launch date, the €99 early-bird / €149 standard pricing, and 10-20 launch-seat target.

## Questions and Answers

Key answers, verbatim where helpful for future cross-referencing:

- Project: Tier 1 MVP of an Obsidian-native "Compound Practice Kit" - Python scripts + Markdown templates operators install in their own vault. Phase 01 = BUG_LEDGER template + capture.py + select.py.
- Hard ship date: Tuesday June 30, 2026 - soft launch at €99 early-bird / €149 standard, targeting 10-20 launch seats.
- Engineering-focus: mid-level, operator-builder hybrid. Wants to move from "operator who orchestrates code generation" to "operator who can read, modify, and ship the code with full understanding."
- Technical baseline: comfortable at orchestration + architecture + discipline layer, not yet a fully independent Python developer for complex modules. Comfortable with the FastAPI + Pydantic + SQLAlchemy stack and production deployment via Docker + Caddy + Cloudflare Tunnel.
- Three areas she wants to learn by building: Python distribution + packaging mechanics for non-developer buyers, Gumroad / Stripe + post-purchase delivery automation, spec-driven development at the distributed-product abstraction layer (versioning, semver, backward compatibility).
- Primary blocker: distribution + packaging mechanics for non-developer buyers. Specifically the cross-platform "must Just Work" problem and the post-purchase flow.
- Secondary blocker: scoping discipline under launch pressure - feature creep risk with a hard June 30 date.
- Time: 5 to 10 hours / week. Sits inside her ~24-32 hours / month Pillar 3 budget alongside ~80% client engagement and AICENTURIA business ops.
- Feedback priorities: project scoping (is Phase 01 v0.1 actually shippable in one Saturday?), distribution mechanics, UX of the Obsidian install flow, documentation register, presentation to potential Tier 1 buyers.
- Accountability format: default sprint cadence + demoable artifact every two weeks. Open to accountability partner pairing.
- Definition of worthwhile: minimum = Tier 1 MVP shipped June 30 with first 10-20 buyers; substantial = all five Phases close on cadence with documented learnings; architectural = sprint cadence holds the Pillar 3 calendar slot against client pull for the full window.

## Meeting Notes

No live intake call yet - working from the Google Doc + Alexey's voice-note feedback. Worth a 30-minute call after she has read the plan, before week 2.

## Internal Recommendations

Alexey's framing in the voice note[^3]: Eva is close in profile to Nirajan Acharya (Nepal-based, Buildcamp Cohort 2 leaderboard top, deployed project, concrete plan). Both already have a clear understanding of what to build and concrete deadlines. The challenge for both is that the usual "give them a roadmap" move does not add much - the value here is accountability and structure, not direction.

Distribution: Alexey's experience with shipping Python to non-technical end users is rough - it usually ends in workarounds. His recommendation, even given the deadline, is to seriously consider Rust as a fallback for the distribution layer if Python keeps failing on non-developer machines. Rust compiles to native binaries for Windows, macOS, and Linux with no runtime dependency, and Alexey has shipped Rust projects without learning the language deeply. .NET is a no - Windows only. The deadline is the open question: she has to assess the rework risk against the launch pressure herself. The Python-only path stays the default until week 2.

Scoping discipline: feature creep is the real risk with a hard external deadline. The June 30 date is the best defense - the plan above hard-locks scope after the Phase 05 pre-launch demo on June 27.

Community use: Eva can lean on the cohort for cross-platform install tests in weeks 4 to 5. AI Shipping Labs members are technical, so giving them a free copy in exchange for honest install feedback is high-leverage. She can also use the cohort as a learning surface for how a community-of-builders runs in practice, which she flagged as a secondary goal.

Accountability partner: pair Eva with Nirajan Acharya. Both are advanced builders running their own clear arc on a hard timeline. Profile match should produce a useful pairing without the usual "junior mentee" friction.

## Internal Action Items

- [ ] [Alexey] Draft the intro message between Eva and Nirajan.
- [ ] [Valeriia] Recruit two to three cross-platform testers (Windows + macOS) from the cohort for week 4.
- [ ] [Eva] Confirm whether the plan dates align with her Phase 01-05 calendar before week 2.

## Sources

[^1]: [Google Doc - Personal Plan Questions for Eva Mareckova](https://docs.google.com/document/d/1RmP3yq_zoWtukZvYZbSkKRwASugyDf06GzqZcEIIJ-I/edit?usp=sharing)
[^2]: [20260519_180847_AlexeyDTC_msg4208.md](../../../inbox/used/20260519_180847_AlexeyDTC_msg4208.md) - Alexey shared Eva's intake doc link
[^3]: [20260519_181952_AlexeyDTC_msg4210_transcript.txt](../../../inbox/used/20260519_181952_AlexeyDTC_msg4210_transcript.txt) - Alexey's voice-note feedback on Eva's profile, Rust as a distribution fallback, scoping discipline, community cross-platform testing, accountability pairing with Nirajan Acharya
