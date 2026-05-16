---
title: "Plan: Vancesca Dinh"
created: 2026-04-20
updated: 2026-04-27
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Vancesca Dinh

Internal working document. Share only the `Summary` and `Plan` sections with the member.

## Summary

- Current situation: job-searching, already completed one AI Buildcamp project, and wants a second portfolio project that ideally also helps DataTalks.Club.
- Goal for the next 6 weeks: ship one more end-to-end project that proves she can build API endpoints, host on AWS, and potentially add a scheduling/cron component.
- Main gap to close: scoping and finishing. Once the end result is clear, Vancesca tends to execute well.
- Weekly time commitment: about 20 hours.
- Why this plan is the right next step: the fastest route is to choose an already-defined problem from the DataTalks.Club issue list and turn it into a portfolio-ready AWS project.

## Plan

## Focus

- Main focus: pick one concrete DataTalks.Club project and commit to it.
- Supporting focus: build it locally in Python first, then deploy it to AWS Lambda.
- Supporting focus: if useful, add one extra engineering signal such as evaluation or a scheduled/cron job.

## Timeline

Week 1:

- Review the shortlist of candidate projects and pick one.
- Define the end result in concrete terms: user flow, success criteria, and what the first version must include.

Week 2:

- Build the local prototype with clear schemas and a clean development workflow.
- Push to GitHub regularly so progress stays visible and incremental.

Week 3:

- Add the API endpoint or entry point the project needs.
- Tighten the local version so the main workflow is already usable.

Week 4:

- Deploy the first working version to AWS Lambda.
- Fix the biggest issues discovered during deployment.

Week 5:

- Add one extra layer that strengthens the portfolio signal: evaluation, cron/scheduling, or another lightweight operations feature.
- Tighten the project so it is usable without a lot of manual hand-holding.

Week 6:

- Write the README, clarify the architecture, polish the demo, and share the project in the community.
- Decide whether the next step is maintenance, iteration, or a second project.

## Resources

- DataTalks.Club hackathon issue list - gives Vancesca ready-made problems instead of a blank ideation step.
- [AI Engineering Field Guide](../../ai-engineering-field-guide.md) - useful for checking which kinds of portfolio projects map well to target roles.
- [Project-idea brainstorming prompt](https://gist.github.com/alexeygrigorev/c1c8dc3ece5cba91e1e381eeba2706c1)

## Deliverables

- One deployed AWS-hosted project in Python.
- A project that clearly demonstrates API usage and deployment.
- README/demo materials good enough for portfolio use.
- Optional scheduled or evaluation feature if it strengthens the final result.

## Accountability

- Define the end result early so implementation does not stall in the scoping phase.
- Push to GitHub regularly and use that as the default progress log.
- Use community sync-ups or a peer-learning session to keep the project moving through the final stretch.

## Next Steps

- [ ] [Vancesca] Pick one project from the shortlist and write down what "done" looks like.
- [ ] [Vancesca] Confirm whether the extra feature should be evaluation, scheduling, or both.
- [ ] [Alexey] Help sanity-check the chosen project scope once the first choice is made.

## Internal Context

## Persona

Undetermined - closest to Alex (The Engineer Transitioning to AI), but the intake does not establish the background clearly enough to assign that archetype with confidence.

## Background

Vancesca is looking for an AI role, already has one project from the AI Buildcamp, and wants another end-to-end portfolio project. She would ideally like the project to also support DataTalks.Club. Her interests cluster around AWS deployment, agent evaluation, and clearer problem definition.

## Intake

## Initial Input

Thanks so much for reaching out. My son is home for Easter, so my focus has been a bit scattered these past few weeks. I appreciate your persistence and kindness in letting me know about this program.

This is definitely something I'm interested in being a part of.

As for what I'm working on or hoping to get out of this:

- I'm currently searching for an AI role, and for me, building a strong portfolio. I completed one project as part of the AI Buildcamp. I'd like to add another. I've been feeling stuck about coming up with an idea has been tough lately.
- One thing I want to mention is that I'd like to contribute to the DataTalks community, especially on projects involving LLM/agents. I'd love to hear about potential projects I can work on to support the DTC community.
- I'd like to deploy applications on AWS.
- I'm especially interested in evaluating agents.
- To maintain motivation, I'd like to have a coffee chat with the community where anyone can join and we talk about AI, our projects, things we're working on, etc. - kind of a peer learning thing. I wouldn't mind hosting it if it's something we can build.

## Questions and Answers

If you build one more project now, what do you want it to prove to employers about you?

I want to show that I can set up API endpoints and host on AWS.

Would you want the next project to be mainly for your portfolio, or mainly to support DataTalks.Club, or ideally both?

Ideally both. I want to be exposed to problems and figure out how to solve them. Defining the problem is my bottleneck - once I build the moment by having a clear idea of what the problem is then getting started and doing the work comes easy.

What do you hope to achieve with this plan in the next 6 to 8 weeks?

- Add another end-to-end project to my portfolio
- Experiment with adding a cron job or some sort of scheduling feature

How much time can you realistically commit each week over the next 6 to 8 weeks?

About 20 hours.

From your experience with building previous projects, what have you learned about the most effective ways you work when tackling technical tasks?

- Defining the end result. The how reveals itself once I figure out what result is expected. This also means breaking the larger idea into smaller tasks.
- Building schemas and being organized
- Pushing to GitHub regularly

Where do you typically encounter challenges when working on projects? For instance: scoping, getting started, maintaining momentum, technical obstacles, or finishing tasks.

The start and the end, so coming up with ideas and maintaining the project once it's "finished".

## Meeting Notes

No separate intake call notes are currently attached in this file.

## Internal Recommendations

For Vancesca, Alexey's main recommendation is to anchor the next project in a concrete DataTalks.Club problem so that she does not have to invent the scope from scratch[^3].

Important internal constraints:

- Alexey wants to minimize ongoing dependency on himself, so the project should be able to move forward without constant feedback.
- Community sync-ups should provide enough structure.
- The project should ideally be something she can develop locally, then deploy to AWS Lambda, entirely in Python.

Full DTC hackathon issue list captured in the original notes:

- [#97 Build a Unified Search Interface for Topics, Subtopics & Timestamp Segments](https://github.com/DataTalksClub/datatalksclub.github.io/issues/97)
- [#96 Build a Chatbot That Answers Questions About Any Podcast Episode](https://github.com/DataTalksClub/datatalksclub.github.io/issues/96)
- [#95 Add a List of Mentioned Resources to Each Podcast Page](https://github.com/DataTalksClub/datatalksclub.github.io/issues/95)
- [#94 Assign Topics & Subtopics to Each Podcast Episode (Episode + Timestamp)](https://github.com/DataTalksClub/datatalksclub.github.io/issues/94)
- [#93 Create Dedicated Workshop and Webinar Pages](https://github.com/DataTalksClub/datatalksclub.github.io/issues/93)
- [#92 Build a Full Tools Catalog + Connections Graph](https://github.com/DataTalksClub/datatalksclub.github.io/issues/92)
- [#91 Build a Catalog of Open-Source Demos from YouTube](https://github.com/DataTalksClub/datatalksclub.github.io/issues/91)
- [#90 Automate Slack Discussions to Website FAQ Sync](https://github.com/DataTalksClub/datatalksclub.github.io/issues/90)
- [#87 Podcast: Key Takeaways Section](https://github.com/DataTalksClub/datatalksclub.github.io/issues/87)

Alexey also wants Vancesca involved in the planning itself, with room to react to the proposed scope rather than just receive a fixed prescription.

## Internal Action Items

- [ ] [Vancesca] Pick a project from the DTC issue list and confirm that she likes it.
- [ ] [Alexey] Help sketch the implementation once the project is chosen.
- [ ] [Vancesca] Decide whether the cron/scheduling feature belongs in the first version or as a later enhancement.

## Sources

[^1]: [Google Doc](https://docs.google.com/document/d/1fJT6wQMA_bK9nwYXmfeGuXiA0k8a8fheZB9NyVbCZCQ/edit?usp=sharing)
[^2]: [20260420_083739_AlexeyDTC_msg3443.md](../../../inbox/used/20260420_083739_AlexeyDTC_msg3443.md)
[^3]: [20260420_102138_AlexeyDTC_msg3471_transcript.txt](../../../inbox/used/20260420_102138_AlexeyDTC_msg3471_transcript.txt)
