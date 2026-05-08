---
title: "Plan: Juan Perez Prim"
created: 2026-05-08
updated: 2026-05-08
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Juan Perez Prim

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: TBD - pending Alexey's recommendations.
- Goal for the next 6 weeks: TBD - pending Alexey's recommendations.
- Main gap to close: TBD - pending Alexey's recommendations.
- Weekly time commitment: TBD - pending Alexey's recommendations.
- Why this plan is the right next step: TBD - pending Alexey's recommendations.

## Plan

This is the shareable part of the document.

### Focus

- Main focus: TBD - pending Alexey's recommendations.
- Supporting focus: TBD - pending Alexey's recommendations.
- Supporting focus: TBD - pending Alexey's recommendations.

### Timeline

Week 1:

- TBD - pending Alexey's recommendations.

Week 2:

- TBD - pending Alexey's recommendations.

Week 3:

- TBD - pending Alexey's recommendations.

Week 4:

- TBD - pending Alexey's recommendations.

Week 5:

- TBD - pending Alexey's recommendations.

Week 6:

- TBD - pending Alexey's recommendations.

### Resources

- TBD - pending Alexey's recommendations.

### Deliverables

- TBD - pending Alexey's recommendations.

### Accountability

- TBD - pending Alexey's recommendations.

### Next Steps

- [ ] [Member] TBD - pending Alexey's recommendations.
- [ ] [Alexey] TBD - pending Alexey's recommendations.
- [ ] [Valeriia] TBD - pending Alexey's recommendations.

## Internal Context

Everything below is for internal use only.

### Persona

Undetermined. The intake call covers Juan's project, his goal of transitioning toward AI engineering, and his time constraints, but does not give enough engineering-background detail to map cleanly to a persona yet. He has a data science background (not pure computer science) and currently works full-time in a data science lead role with some LLM/GenAI exposure. He is not in a rush to switch jobs - the transition is a desire, not a deadline. Once Alexey records his recommendations, the persona can be revisited.

See [personas.md](../personas.md) for full persona definitions.

### Background

Juan is based in Madrid and has a full-time data science lead role with some touchpoints with LLM/GenAI work, but not as much as he would like. His background is data science (not pure computer science) with prior industry experience in retail, pharma, and engineering. He met Alexey through the Maven AI Engineering Buildcamp and joined AI Shipping Labs to learn, share tips, and possibly collaborate on community projects. He is open to transitioning toward an AI engineering role but has no strict deadline or industry preference.

His public project is [amr_ai](https://github.com/juanpprim/amr_ai) - a learning agent focused on Antibiotic Resistance (AMR), built during the Maven boot camp. The current Streamlit app generates overviews, quizzes, and flashcards over public AMR content. He wants to evolve it during the sprint, with deployment as the primary priority.

He had a complicated month leading up to the intake call - his wife was sick and he was juggling care for a small child[^1].

Cross-reference the matching interview at [../interviews/juan-perez-prim.md](../interviews/juan-perez-prim.md).

### Intake

#### Initial Input

The Google Doc is a Gemini-generated transcript and summary from Juan and Valeriia's intake call on 2026-05-07[^1]. There was no separate free-form written input; Juan opened the call by giving context on how he joined and what he wants from the community:

> So, I joined - I mean, I know Alexey, I met him through one of the platforms, Maven. So one of the courses, it was the AI Engineering Buildcamp. My background is in data science. So I'm not a computer science by study. So I'm more on the engineering side that moved forward to the data side... And then my situation is - I use a little bit of the tools of AI, but I want to know - since I have not done much, it's easier to do it with someone or a community, you can push yourself a little bit higher than if you're more alone. So one of the things in the community that I think is interesting is sharing tips, getting some profiles, maybe even collaborate on projects with other people or for Alexey... I have a project I did for the bootcamp, the Maven one - I wanted to evolve it, keep it evolving a little bit. So that's basically going to be my goal. And what I want to do is, one is learning purposes, and second is - I'm open to looking for jobs. I have a full-time job but maybe would like to transition to another role.

#### Questions and Answers

Questions are paraphrased from Valeriia's prompts during the call; answers are condensed from Juan's responses[^1]. Timestamps reference the transcript.

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

### Meeting Notes

No intake call yet between Alexey and Juan - the input above was collected on 2026-05-07 via Valeriia's intake call (recorded as a Google Doc with Gemini-generated summary, next steps, and transcript)[^1].

### Internal Recommendations

Pending. Alexey has not yet recorded his recommendations on this intake.

### Internal Action Items

- [ ] [Alexey] Record recommendations on Juan's intake (Persona assignment, plan focus, project framing for the AMR learning agent deployment).
- [ ] [Alexey] Once recommendations are in, fill out the Summary, Plan, and Next Steps sections and send the written plan to Juan.
- [ ] [Valeriia] Confirm Juan is on the AI Shipping Labs Slack channel and added to the May sprint roster.
- [ ] [Valeriia] Follow up with Edu Gonzalo Almorox about pairing with Juan (both data scientists, both in Madrid, both from Alexey's course; Edu works in health economics which overlaps with Juan's AMR project domain).
- [ ] [Valeriia] Mention OpenClaw / long-running agent topic in the community channel for group learning, per Juan's interest.
- [ ] [Juan] Watch the recording of the first sprint session he missed.
- [ ] [Juan] Email Valeriia the project GitHub link ([amr_ai](https://github.com/juanpprim/amr_ai)).

### Sources

[^1]: [Juan Perez Prim's intake (Google Doc)](https://docs.google.com/document/d/1j-vldwylQfbFkqOBNmtwHj8of2rq36VGakkP6DX2ev0/edit?usp=sharing), shared via [20260508_084825_AlexeyDTC_msg3955.md](../../../inbox/used/20260508_084825_AlexeyDTC_msg3955.md).
