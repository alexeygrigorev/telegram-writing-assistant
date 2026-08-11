---
title: "Plan: Nicole Newman"
created: 2026-08-11
updated: 2026-08-11
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Nicole Newman

Internal working document. Share only the `Summary` and `Plan` sections with the member. Everything from `Internal Context` onward stays inside AI Shipping Labs.

## Summary

- Current situation: Technology Strategy consultant at Accenture, based in New Jersey. Builds with Claude Code, GPT APIs, N8N, Lovable and Python notebooks, and has an early wedding-planning prototype built locally but not deployed.
- Goal for the next 6 to 8 weeks: get more technical - understand what happens under the applications she builds - and take one idea past a first prototype, so she has both the technical foundation and the portfolio work for interviews starting in November or December.
- Main gap to close: she uses AI tools but does not yet write the full-stack part herself - project structure, Docker, back end, LLM integration, and the reasoning behind the technical design decisions.
- Weekly time commitment: about 5 hours per week, strongest on weeknights and weekends, with weeks varying because of client work.
- Why this plan is the right next step: the fastest way into the technical side for her target roles is through the coding tools, not through AI engineering theory. AI Dev Tools Zoomcamp gives her that directly, and AI Hero run in parallel tells her how deep into AI engineering she actually wants to go.

## Plan

The goal for the next six weeks is that Nicole becomes more technical - "Build stronger AI engineering skills" is her stated path, and the question is which direction inside that gives her the most for the roles she is targeting.

Two things run in parallel.

The first and main one: move to Codex or Claude Code as the way she builds, and take AI Dev Tools Zoomcamp for the coding side. Out of the things she needs, this will be the more useful one. She already uses Claude Code - the recommendation is to do much more of it. Those are also the tools for taking what she has in Lovable and n8n and moving it to something real.

The second, running alongside: take the AI Hero course. The point is not to complete it as a formal goal but to understand how much AI engineering she actually needs, or whether what she really needs is the AI development tools side.

If it turns out after AI Hero that AI engineering is something she wants to go further into, the next step after that is LLM Zoomcamp, which covers it in more detail. That is a conversation to have once she has touched AI Hero, not a decision to make now.

## Focus

- Main focus: AI Dev Tools Zoomcamp, and building with Codex or Claude Code as the default way of working.
- Supporting focus: AI Hero, in parallel, as a way to find out whether AI engineering is the direction she wants.
- Supporting focus: settle which project she takes forward - the wedding and event planning product or business process mapping - and take that one past the first prototype.

## Timeline

Week 1:

- Start AI Dev Tools Zoomcamp. Work through the first module.
- Pick the coding assistant and set it up properly - Codex or Claude Code. She already has Claude Code, so the step here is to start using it for everything rather than occasionally.
- Start AI Hero in parallel. First modules only, at whatever pace the 5 hours allow.
- Settle the project decision with Alexey (wedding and event planning versus business process mapping) so the build work in weeks 2 to 6 has one target.

Week 2:

- Continue AI Dev Tools Zoomcamp with the next module.
- Continue AI Hero.
- Take the chosen project and write down what exists today and what the target version looks like. The current wedding-planning prototype produces a downloadable PDF and is not interactive, so the target state should be concrete about what changes.

Week 3:

- Continue AI Dev Tools Zoomcamp.
- Continue AI Hero. By the end of this week she should have a first read on whether AI engineering is interesting to her or whether the tools side is what she actually needs.
- Start building the chosen project with the coding assistant, using the workflow from the Zoomcamp rather than the tools she used for the first prototype.

Week 4:

- Continue AI Dev Tools Zoomcamp.
- Keep building. This is where project structure and Docker come in - the two things she named as what "becoming more technical" means in practice.
- Post progress in the sprint channel.

Week 5:

- Continue AI Dev Tools Zoomcamp.
- Keep building toward a working end-to-end version rather than a polished one. Finishing and polishing is the thing that stalls her projects, so the target is something that runs, not something that is finished.

Week 6:

- Finish the Zoomcamp material.
- Get the project to a demoable state and deploy it, so it stops being local-only.
- Decide with Alexey what comes next based on how AI Hero landed. If AI engineering is the direction, LLM Zoomcamp is the next course.

## Resources

- [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) - the main course for this sprint, covering the coding tools and how to build with them.
- [AI Hero](https://aishippinglabs.com/courses/aihero) - run in parallel, to find out how much AI engineering she wants.
- [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) - the next step after AI Hero if AI engineering turns out to be the direction. Covers it in more detail.

## Deliverables

- One chosen project, taken past the first prototype and deployed by the end of week 6.
- AI Dev Tools Zoomcamp completed.
- Enough of AI Hero to answer the question of whether to go deeper into AI engineering.

## Accountability

- Weekly check-ins and async Slack feedback, which are the two formats she asked for.
- Progress posted in the sprint channel each week.

## Next Steps

- [ ] [Nicole] Set up Codex or Claude Code as the default way of building and start AI Dev Tools Zoomcamp.
- [ ] [Nicole] Start AI Hero in parallel.
- [ ] [Alexey] Give Nicole a read on the project direction (wedding and event planning versus business process mapping) for the roles she is targeting.
- [ ] [Alexey] Revisit the plan after AI Hero to decide whether LLM Zoomcamp comes next.

## Internal Context

## Persona

Sam (The Technical Professional moving to AI) - assigned by the onboarding questionnaire (`onboarding-sam`). Analyst and consultant who builds with no-code and AI tools, uses Python for notebooks and data analysis, and wants to understand the layer underneath.

She is a distinctive Sam: she does not want to become an AI engineer. She wants enough technical depth to hold architecture conversations in Solutions Architect and technical Product interviews. That is why the plan leans toward the dev tools side rather than the AI engineering side, with AI Hero as the probe.

See [personas.md](../personas.md) for full persona definitions.

## Background

Nicole J Newman, based in New Jersey near New York. Works in Technology Strategy at Accenture, which she describes as similar to Big 4. Joined AI Shipping Labs on 2026-07-07, premium tier, CRM record 37.

She is preparing for a career transition later this year. Target roles: Solutions Architect or technical Product Management, and also partnership lead or strategy and operations, at an AI company, AI research company, or a later-stage startup. She expects to start interviewing in the November to December window.

Tools she has used: Claude Code, GPT APIs, N8N, Lovable, Python notebooks, and data analysis. Python comfort level: notebooks and data analysis scripts.

No interview file exists for Nicole yet.

## Intake

Three inputs: the onboarding questionnaire submitted 2026-08-01, the onboarding call with Valeriia on 2026-08-10, and Nicole's follow-up email sent 2026-08-11.

## Initial Input

Nicole's follow-up email to Valeriia and Alexey, 2026-08-11:

She wants to become more technically fluent in AI while preparing for a potential career transition later this year. She currently works in Technology Strategy at Accenture and is most interested in Solutions Architect or technical Product Management roles within an AI company or later-stage startup. She expects to begin interviewing in December, so her goal over the next 6 to 8 weeks is to strengthen both her technical foundation and the portfolio of work she can use in those conversations.

The four areas she asked for support on:

- Technical depth: a stronger understanding of full-stack AI products, including architecture, APIs, LLM selection, integrations, agentic workflows, and the reasoning behind technical design decisions. She has experience with Claude Code, GPT APIs, N8N, Lovable, Python notebooks and data analysis, but wants to understand more of what is happening underneath the applications she builds.
- Project direction: she has an early wedding-planning prototype built with Lovable and N8N. She is deciding whether to develop it into a broader event-planning product or pivot to a more enterprise-oriented use case, such as using AI to accelerate business process mapping. She asked for Alexey's perspective on which direction would be the strongest demonstration of product thinking, technical fluency, and strategic problem solving for the roles she is targeting.
- Build experience: take one idea beyond a first prototype and work through scoping, architecture, development, and refinement of a more complete AI application.
- Interview readiness: understand the technical concepts and architecture discussions she should be prepared to navigate for Solutions Architect and technical Product roles, without trying to become an AI engineer.

She can commit roughly five hours per week, with more flexibility during evenings and weekends. Her preference is to establish the technical foundations first and then apply them through a hands-on project.

## Questions and Answers

From the onboarding questionnaire (`onboarding-sam`, submitted 2026-08-01), kept close to verbatim:

- What would you like to have achieved 6 to 8 weeks from now: "I would like to build an AI product 8 weeks from now. I created a prototype using Lovable & n8n, and would like to further refine my idea. This prototype is what I will leverage in applying for strategy & ops roles." On the call she added solutions architect and product manager roles to that list, the November/December interview timing as the bigger goal, and that she is currently deciding whether to continue with the wedding planning AI product or explore business process mapping.
- Which path best fits that goal: "Build stronger AI engineering skills." On the call she said interview preparation would have been her second choice if it had been an option. Asked to define what building stronger AI engineering skills means, she said: learning how to implement full-stack AI products and understanding the underlying technology and how it works - writing front-end and back-end code, connecting LLMs, skills, MCPs. She agreed with the framing "becoming more technical than you are currently".
- How many hours per week can you realistically commit: 3 in the questionnaire, revised to 5 on the call to be realistic.
- What should we know about your availability: "I am a consultant, so my weeks vary based on client needs." On the call: mornings are hard, nights and weekends are best.
- What tends to slow you down or make projects stall: finishing and polishing, limited time, not enough feedback or accountability.
- What kind of accountability would help you make progress: weekly check-ins, async Slack feedback.
- Do you already have a project, idea, or direction in mind: "Yes, I have my project here: cufnszn.com, but it doesn't have to remain within the wedding planning space. I would like to go deeper in fleshing out a project that offers a true paradigm shift."
- What stage is your project or idea at: built locally but not deployed.
- What would you like us to help with while preparing your plan: scoping, architecture, career positioning.
- Anything else we should know before preparing your plan: "I often have more time on weekends, or select weeknights."
- When you say you want to become more technical, what would be useful in practice: project structure, Docker, building small apps.
- How comfortable are you with Python for building software: "I mostly use notebooks or data analysis scripts."
- Which AI tools have you used, and what did you use them for: "Claude Code, GPT APIs, and N8N."
- Which pace feels right for you: phased - foundations, then build. On the call she explained why: if she is interviewing with companies, they will want to know the underlying architecture, the integrations, and the strategy behind choosing one LLM over another.
- How much do you want to understand what is happening behind the AI tools: "I want deeper technical understanding."

## Meeting Notes

Onboarding call with Valeriia Kuka, 2026-08-10, about 23 minutes.

On the role search: she is a technology strategy consultant looking for a new role, but not in AI engineering. Technical product manager, solutions architect, partnership lead, or strategy and operations, at an AI research company or a late-stage startup. She noted that the product field is not doing too well right now, which is why she widened the list. She wants to understand how AI works from a technical perspective, prepare for interviews, and build prototypes.

On the project decision, which is the main open question she brought to the call:

- The wedding planning site was built with N8N plus some APIs about four or five months ago. It is not built on skills, and right now the output is a downloadable PDF rather than an interactive site. She and her partner showed it at a few places including an expo and got positive feedback, but she considers it a first pass.
- She interviewed newlyweds about a year ago and heard that they wanted budgeting and tools. That has shifted: in the US, weddings are being done more cheaply, so budgeting is less of a need, and what people now want is to see and envision what the wedding could look like - plugging things in and seeing a sketch come to life. The original goal was to connect people with lower-cost or unique options (an arcade, a vintage church).
- An entrepreneur mentor suggested widening from wedding planning into event planning generally - baby showers, sweet sixteens - or alternatively continuing with the same site but using different skills to keep people on it.
- The alternative direction is business process mapping. She learned at work that business process mapping in ERP tools like SAP is very difficult and can take up to two years with full-time staff. Her question is whether picking a use case with a pressing need like that would be more compelling to hiring managers than expanding the wedding product and trying to make it premium.
- She cannot do both, so she needs to pick one.

Her other question on the call: for technical product or solutions architect interviews she knows she does not need to be as well-versed as an AI engineer, so what does interview preparation look like for her specifically.

Valeriia explained the AI Shipping Labs onboarding: a personalized six-week plan built from the questionnaire, with a weekly milestone and accountability through the sprint channel on Slack.

Two process issues surfaced on the call. Nicole had submitted the questionnaire but Valeriia did not initially see it, and Nicole could not find where her answers or the plan appear in her profile - Valeriia had to log in and share her screen to show her the "review your onboarding answers" button. The onboarding response is still in `review_state: awaiting`, and the CRM record has empty persona, summary, and next steps fields even though the questionnaire assigned the Sam persona.

## Internal Recommendations

Alexey's framing from the voice notes:

Her main goal is "Build stronger AI engineering skills". Given that, there are two things worth doing, and which one matters more depends on what she wants to focus on.

The recommendation is that she moves to Codex or Claude Code. For that, she can use the AI Dev Tools Zoomcamp coding course - out of the things she needs, this will be more useful. She already uses Claude Code, but he would recommend doing much more of it.

Those tools are also what she needs to take what she has in Lovable and n8n and move it to something real - the Zoomcamp gives her the tools for that.

In parallel she can take AI Hero, simply to understand how much she needs to go deeper into AI engineering, or whether what she needs is more to look at the AI tools for development. So those two courses together: AI Dev Tools Zoomcamp for the tools, AI Hero to test the AI engineering direction.

After reading her follow-up email, Alexey confirmed the same read: her email supports going into dev tools now, and in parallel just touching AI Hero to see how much her heart is in AI engineering and whether she wants to keep going in that direction. If she does, then - and this is something to discuss further with her - after AI Hero she can take LLM Zoomcamp, which covers it in more detail.

Open point: Nicole explicitly asked for Alexey's perspective on the project direction - continue the wedding and event planning product or pivot to business process mapping. The voice notes cover the courses and the tooling direction but do not answer the project question, so it stays open.

## Internal Action Items

- [ ] [Alexey] Answer the project-direction question: wedding and event planning versus business process mapping, judged by what best demonstrates product thinking and technical fluency for Solutions Architect and technical Product roles.
- [ ] [Alexey] Work out what interview preparation looks like for a technical Product / Solutions Architect track rather than an AI engineer track - she asked this on the call and it is not covered yet.
- [ ] [Valeriia] Mark the onboarding response as reviewed and fill in the CRM record persona, summary, and next steps - all three are empty.
- [ ] [Valeriia] Check the profile navigation - Nicole could not find where her onboarding answers and plan appear without a screen share.

## Sources

[^1]: [20260811_155946_AlexeyDTC_msg4861.md](../../../inbox/used/20260811_155946_AlexeyDTC_msg4861.md) - Alexey shared Nicole's onboarding-call doc link
[^2]: [Google Doc - AI Shipping Labs: Valeriia's Appointment Schedule (Nicole Newman)](https://docs.google.com/document/d/1ZmhewWJMYNF6pQ-OqN7QD5sTc3Zrd1zRtgpt6ck1B-o/edit) - Gemini notes and full transcript of the 2026-08-10 onboarding call with Valeriia
[^3]: [20260811_160050_AlexeyDTC_msg4864.md](../../../inbox/used/20260811_160050_AlexeyDTC_msg4864.md) - Nicole's follow-up email
[^4]: [20260811_161119_AlexeyDTC_msg4866_transcript.txt](../../../inbox/used/20260811_161119_AlexeyDTC_msg4866_transcript.txt) - Alexey's voice-note recommendation: Codex or Claude Code plus AI Dev Tools Zoomcamp as the main direction, AI Hero in parallel to test the AI engineering direction
[^5]: [20260811_161248_AlexeyDTC_msg4868_transcript.txt](../../../inbox/used/20260811_161248_AlexeyDTC_msg4868_transcript.txt) - Alexey's follow-up after reading the email: confirms dev tools now, AI Hero in parallel, LLM Zoomcamp after AI Hero if AI engineering is the direction
[^6]: AI Shipping Labs onboarding questionnaire (`onboarding-sam`), submitted 2026-08-01, retrieved through the AI Shipping Labs API
