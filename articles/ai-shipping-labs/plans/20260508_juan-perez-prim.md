---
title: "Plan: Juan Perez Prim"
created: 2026-05-08
updated: 2026-05-09
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Juan Perez Prim

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: Madrid-based data science lead, met Alexey through the Maven AI Engineering Buildcamp. Already shipped [amr_ai](https://github.com/juanpprim/amr_ai), an AMR (Antibiotic Resistance) learning agent: Streamlit chat that produces overviews, quizzes, and flashcards from a hybrid-retrieval RAG over WHO/CDC/FAO/PubMed sources, built with PydanticAI + Claude + ChromaDB + BioBERT[^2]. The build itself is solid. The project has not been deployed yet[^1].
- Goal for the next 6 weeks: take the existing `amr_ai` Streamlit app from "runs locally" to "deployed and reachable on a secure independent website", with monitoring and evaluation added on top so other people can use it for feedback.
- Main gap to close: deployment + monitoring + evaluation. The build skill is already there - what is missing is the production wrapping (Dockerization, scalability, secure hosting, GitHub Actions pipeline) plus the production-side evaluation Juan has not done before.
- Weekly time commitment: 5 to 10 hours per week, around a full-time data science lead role and family responsibilities[^1].
- Why this plan is the right next step: Juan already has the project the Buildcamp arc would normally have him build. The natural next step in the Buildcamp arc - concept → tools → tests → monitoring → evolution - is the part he has not done yet. Doing exactly that for `amr_ai` doubles as a portfolio piece and a base for the long-term goal of generalising the platform to other topics.

## Plan

This is the shareable part of the document.

## Focus

- Main focus: deploy `amr_ai` to a secure independent website. Dockerise the Streamlit app, set up a small Docker-Compose-style stack (app + Chroma store + a reverse proxy for HTTPS), pick a host that does not bankrupt a side project, and wire up GitHub Actions so a push to main updates the live site.
- Supporting focus: add real evaluation on top of the existing RAG. The Buildcamp workshop walked through this end to end - replicate that pattern on `amr_ai` and use it to compare retrieval/reranker variants and answer-grounding quality.
- Supporting focus: add monitoring once the site is live. Logfire (or equivalent) for traces and request-level visibility, plus a small dashboard so usage from the five colleagues you share it with is observable rather than guessed at.

## Timeline

Week 1:

- Stand up a Docker setup that runs the existing Streamlit app + Chroma collection together. The acceptance bar is "another machine can `docker compose up` and get the same chat experience".
- Decide the host (Hugging Face Space - private to start - vs. a small VM vs. a managed Streamlit deploy). Private HF Space is the lightest path for the "share with five colleagues" goal Juan named in intake[^1]. A small VM is the right call if the eventual platform direction needs it.
- Lock down secrets (API keys, DB paths) in env vars / a secret store, not in the repo.

Week 2:

- Deploy the first version. Get a URL you can send to one colleague and ask them to break.
- Add HTTPS / a custom domain if the host does not give one for free. Add basic auth or signed links so the URL is not openly indexable.
- Replay one or two of the colleague's sessions from the logs to confirm what they saw.

Week 3:

- Replay the Buildcamp workshop on monitoring + evaluation against `amr_ai`. Take the workshop's pattern (instrumentation around the RAG step + an evaluation harness over a small held-out set of AMR questions) and wire it in as written, not as a clean-sheet redesign. Goal: reproduce the workshop pattern in your project.
- Build the eval set: 20-50 AMR questions you would want a clinician/student to be able to ask, with a notion of what a correct grounded answer looks like. The set is the project's quality bar from this point on.

Week 4:

- Add a CI step in GitHub Actions that runs the eval set on every push. Failing eval scores block deploy. The point is not to chase a high score - it is to make regressions visible.
- Add monitoring on the deployed site (Logfire or equivalent) so live errors and slow retrievals are visible. Confirm an end-to-end trace from "user types question" to "Chroma returns chunks" to "Claude returns answer" is readable.

Week 5:

- Iterate on retrieval/reranker variants using the eval set as the scoreboard. The hybrid (BioBERT + BM25 + RRF) stack you already have is a solid baseline. One or two principled experiments (e.g., a different embedding model, a reranker tweak, a chunking change) is enough.
- Polish the README, the architecture diagram, and the "how this was built" page so the public-facing version of the site has a writeup behind it.

Week 6:

- Open the site to the five colleagues you mentioned in intake[^1]. Capture their feedback in the eval set so it tightens with real usage.
- Decide whether the next sprint is: (a) generalising the platform to other topics (your stated long-term goal), (b) moving to a more capable host now that you have real usage, or (c) starting on the second project from your idea list.

## Project approach

- The build is not the bottleneck. `amr_ai` already has a richer stack than most sprint projects start with - PydanticAI agent, hybrid retrieval, BioBERT, Reciprocal Rank Fusion, Docling for PDFs[^3]. The sprint is about adding the production layer around what you have built, not rebuilding it.
- Streamlit is fine for week-1 deployment. It got you to a working chat. Replacing it with a custom React frontend is a different project. If it ever happens, do it after the sprint, not during it.
- Replicate the Buildcamp pattern, do not reinvent it. The workshop on monitoring + evaluation is the reference for what to add and in what order. Build the same shape on `amr_ai`, then improve from there.
- Pair where it accelerates. Manjunath Yelipeta is sprinting on a v0.0.1 deployment platform that takes an AI project as input and produces a live URL ([his plan](20260506_manjunath-yelipeta.md)). His project and your project are on opposite sides of the same problem - there is real value in talking weekly about what each side learns. Pairing is optional but encouraged. Treat it as an open conversation, not a dependency.
- Keep secondary feature work parked. Adding diagrams, images, videos, gamified flashcards, generalising the platform - all good, all out of scope for this sprint. Note them in a follow-up doc so they are not lost. Do not let them displace deployment.

## Resources

- Buildcamp workshop on monitoring + evaluation - the reference pattern for week 3-4. Use the same structure on `amr_ai` rather than designing from scratch.
- AI Shipping Labs first workshop on Telepot agents and deployment to Render (week of 2026-04-20) - useful as a deployment-walkthrough reference if you want to see one path end to end. Available to community members. Ask Valeriia for the link.
- Streamlit + Docker deployment docs for whichever host you pick.
- Logfire (or your monitoring tool of choice) for the production-side traces.
- [The amr_ai repo](https://github.com/juanpprim/amr_ai) .

## Deliverables

- `amr_ai` Dockerised and running locally via `docker compose up` - by end of week 1.
- First deployed URL accessible over HTTPS with basic access control - by end of week 2.
- Eval set of 20-50 AMR questions wired into a CI eval step - by end of week 3-4.
- Live monitoring with end-to-end traces visible - by end of week 4.
- Public README + architecture writeup, eval-driven retrieval iteration - by end of week 5.
- Site shared with the five colleagues, feedback captured back into the eval set - by end of week 6.

## Accountability

- Weekly async update on what shipped, what is blocked, and the goal for next week - the "structured deadlines and motivation through feedback" Juan asked for in intake[^1].
- Pair check-in with Manjunath (optional but encouraged) once a week or once a fortnight - 20 minutes is enough.
- Post the live URL in `#plan-sprints` once it exists. The community is the first set of users.

## Next Steps

- [ ] [Juan] Watch the recording of the first sprint session he missed.
- [ ] [Juan] Email Valeriia the project GitHub link ([amr_ai](https://github.com/juanpprim/amr_ai)).
- [ ] [Juan] Decide on the deployment host by end of week 1 (private HF Space is the recommended starting point).
- [ ] [Juan] Start a short "deferred features" doc so secondary work (diagrams, gamification, generalisation) does not pull the sprint off course.
- [ ] [Alexey] Send the written plan and confirm the Buildcamp monitoring + evaluation workshop link.
- [ ] [Valeriia] Connect Juan with Manjunath for a weekly pair check-in if both are open to it.

## Internal Context

Everything below is for internal use only.

## Persona

Priya - The Improver. Juan already has a working AI project (`amr_ai`, demoed at Buildcamp Cohort 2[^3]) and a stable senior data role. He is not transitioning from zero - he is improving an existing build to production grade and learning the production-engineering side he has not done before. The "no transition deadline, no industry preference" framing reinforces this: the sprint is about depth on what already exists, not breadth into a new stack.

See [personas.md](../personas.md) for full persona definitions.

## Background

Juan is based in Madrid and has a full-time data science lead role with some touchpoints with LLM/GenAI work, but not as much as he would like. His background is data science (not pure computer science) with prior industry experience in retail, pharma, and engineering. He met Alexey through the Maven AI Engineering Buildcamp and joined AI Shipping Labs to learn, share tips, and possibly collaborate on community projects. He is open to transitioning toward an AI engineering role but has no strict deadline or industry preference.

His public project is [amr_ai](https://github.com/juanpprim/amr_ai) - a learning agent focused on Antibiotic Resistance (AMR), built during the Maven boot camp. The current Streamlit app generates overviews, quizzes, and flashcards over public AMR content. He wants to evolve it during the sprint, with deployment as the primary priority.

He had a complicated month leading up to the intake call - his wife was sick and he was juggling care for a small child[^1].

Cross-reference the matching interview at [../interviews/juan-perez-prim.md](../interviews/juan-perez-prim.md).

## Intake

## Initial Input

The Google Doc is a Gemini-generated transcript and summary from Juan and Valeriia's intake call on 2026-05-07[^1]. There was no separate free-form written input. Juan opened the call by giving context on how he joined and what he wants from the community:

> So, I joined - I mean, I know Alexey, I met him through one of the platforms, Maven. So one of the courses, it was the AI Engineering Buildcamp. My background is in data science. So I'm not a computer science by study. So I'm more on the engineering side that moved forward to the data side... And then my situation is - I use a little bit of the tools of AI, but I want to know - since I have not done much, it's easier to do it with someone or a community, you can push yourself a little bit higher than if you're more alone. So one of the things in the community that I think is interesting is sharing tips, getting some profiles, maybe even collaborate on projects with other people or for Alexey... I have a project I did for the bootcamp, the Maven one - I wanted to evolve it, keep it evolving a little bit. So that's going to be my goal. And what I want to do is, one is learning purposes, and second is - I'm open to looking for jobs. I have a full-time job but maybe would like to transition to another role.

## Questions and Answers

Questions are paraphrased from Valeriia's prompts during the call. Answers are condensed from Juan's responses[^1]. Timestamps reference the transcript.

1. What are your goals for joining the community? - "Learning, including collaborating on projects, sharing tips, and potentially contributing to Alexey's work. I have a full-time job but I'm open to looking for roles, and I would like to evolve a project I completed during the boot camp."

2. Do you have a specific deadline or target role for the transition? - "No, I don't have a deadline. It's just a desire of being more close to the technology on the AI side, but I don't have a pure deadline for myself. I have a full-time job, so I don't have the rush or the need to do it. It's just a desire of moving in that direction. The role would be more on the AI engineering side - my role at the moment is more on the data science part in the lead. I still have through work a little bit of touch with LLM and agentic AI, but not as much as I would like."

3. What industry are you targeting? - "I don't have any in mind. I have worked mainly in retail, pharma, and engineering, but I don't have a close idea industry-wise."

4. Can you describe the project you completed during the bootcamp? - "It's a learning agent focused on AMR (Antibiotic Resistance). The current Streamlit app generates overviews of the AMR issue, quizzes (e.g., 'give me a quiz about risk of AMR'), and flashcards that you can flip and have evaluated. I built the basics during the bootcamp but still have a lot of room to improve. I have many ideas - adding diagrams, images, videos inside the chat, gamified features like earning points with flashcards, and eventually generalising the platform to any topic (finance, etc.). But step by step."

5. Do you plan to work on this project during the sprint? - "Yes, that's my idea. I will work on it during this sprint or maybe the next one. I couldn't join the first sprint meeting yesterday but I will watch the recording."

6. What is your priority for the six-week sprint? - "Deployment. I want to figure out how to move the existing Streamlit app to a secure, independent website where people can interact with it. I need help with system design - Dockerization, scalability, security, and workflows for deploying code updates via GitHub Actions. Adding new features (better quiz logic, graphs) would be secondary, in later parts of the plan."

7. What would success look like at the end of six weeks? - "Having a basic website deployed that I can share with five or so colleagues for feedback. Potentially using a private Hugging Face Space initially."

8. How much time can you dedicate per week? - "5 to 10 hours per week."

9. What kind of accountability would help you keep momentum? - "Structured deadlines from the community and motivation through feedback and ideas - especially given my limited working time."

10. Are you open to being paired with other community members? - "Yes, that would be more fun and collaborative."

11. Are there other tools or topics you want to explore in the community? - "Long-running agents - I'd like to try OpenClaw, and there's another one I think called GilLoad, and another that runs as a service through Telegram. I haven't gone deeper yet but it's on my to-do list. I'm also curious about coding assistants like Cursor and other AI tools, and would be interested in community group learning activities or standups where people research and share knowledge on specific topics."

## Meeting Notes

No intake call yet between Alexey and Juan - the input above was collected on 2026-05-07 via Valeriia's intake call (recorded as a Google Doc with Gemini-generated summary, next steps, and transcript)[^1].

## Internal Recommendations

Alexey's recommendations after reviewing the intake doc[^4]:

1. He already has the project. `amr_ai` is the AMR learning agent he built during the Maven Buildcamp - PydanticAI agent, hybrid retrieval (BioBERT + BM25 + RRF), Streamlit chat over WHO/CDC/FAO/PubMed sources[^3]. He scored 26 on the Buildcamp submission. The build is solid. Deployment is the missing piece.

2. The sprint goal is straightforward: deploy what exists. Streamlit is fine as the first deployed shape - he should not rebuild the frontend during this sprint. After the deploy works, the Buildcamp arc continues with monitoring and evaluation, in that order.

3. The Buildcamp monitoring + evaluation workshop is the reference. He attended a workshop with us where we walked through how to add monitoring and proper evaluation to a project - this is the pattern to replicate on `amr_ai`. That removes the "design-from-scratch" overhead and turns this into a known recipe applied to his project.

4. Pair him with Manjunath. Manjunath's plan is a v0.0.1 deployment platform that takes any AI project and produces a live URL ([his plan](20260506_manjunath-yelipeta.md)). Juan needs exactly that capability for `amr_ai`. They are on opposite sides of the same problem and can compare notes weekly. This pairing is more useful than the Edu pairing flagged earlier - same shape of problem, complementary perspectives.

5. Read on Juan's request: he asked for help with system design (Dockerization, scalability, security, GitHub Actions). All of those land in the deployment-and-monitoring sequence. The plan covers them in week 1-2 (Docker, secrets, hosting), week 4 (CI/CD with eval gating), and week 4 (live monitoring). No need to break those out as separate workstreams.

6. Out of scope this sprint: gamification, diagrams in chat, video embeds, generalising to other topics. All worth doing, none belong in a 6-week deployment-focused sprint. Capture them in a "deferred features" doc so they are not lost.

## Internal Action Items

- [x] [Alexey] Record recommendations on Juan's intake (Persona assignment, plan focus, project framing for the AMR learning agent deployment) - done 2026-05-09[^4].
- [ ] [Alexey] Send the written plan and confirm the link to the Buildcamp monitoring + evaluation workshop recording.
- [ ] [Valeriia] Confirm Juan is on the AI Shipping Labs Slack channel and added to the May sprint roster.
- [ ] [Valeriia] Drop the Edu pairing follow-up unless Juan specifically wants it - Manjunath is the higher-priority pairing now (same problem space, opposite sides). Edu can still join the wider conversation, just not as the primary pair.
- [ ] [Valeriia] Set up the Juan ↔ Manjunath pairing if both are open to a weekly check-in.
- [ ] [Valeriia] Mention OpenClaw / long-running agent topic in the community channel for group learning, per Juan's interest.

## Sources

[^1]: [Juan Perez Prim's intake (Google Doc)](https://docs.google.com/document/d/1j-vldwylQfbFkqOBNmtwHj8of2rq36VGakkP6DX2ev0/edit?usp=sharing), shared via [20260508_084825_AlexeyDTC_msg3955.md](../../../inbox/used/20260508_084825_AlexeyDTC_msg3955.md), and re-confirmed in [20260509_113436_AlexeyDTC_msg3986.md](../../../inbox/used/20260509_113436_AlexeyDTC_msg3986.md).
[^2]: `amr_ai` GitHub repository: [github.com/juanpprim/amr_ai](https://github.com/juanpprim/amr_ai).
[^3]: [AI Engineering Buildcamp Cohort 2 - Demo Day](../../demo-day-cohort-2.md) - "AMR Awareness Platform (Juan Prim)" entry, including stack and feature breakdown.
[^4]: [20260509_113453_AlexeyDTC_msg3988_transcript.txt](../../../inbox/used/20260509_113453_AlexeyDTC_msg3988_transcript.txt) - Alexey's recommendations after reviewing Juan's intake doc.
