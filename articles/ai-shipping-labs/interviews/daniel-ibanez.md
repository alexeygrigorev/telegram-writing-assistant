---
title: "Interview: Daniel Ibáñez"
person: Daniel Ibáñez
persona: Undetermined
created: 2026-04-20
updated: 2026-05-09
tags: [ai-shipping-labs, interview, community]
status: draft
---

# Interview: Daniel Ibáñez

## Persona

Undetermined. Daniel's response so far only describes what he wants from the community (not his background, engineering level, or AI/ML experience) so there is not enough to map him to a persona yet.

See [personas.md](../personas.md) for full persona definitions.

## Response

I believe a roadmap on how to learn the necessary for AI Engineering would be nice to have. What I would like to get from the community is for us to share best practices in AI Engineering and analysis of what works and what doesn't in different scenarios[^1].

## Side project Daniel wants to start after this sprint

Daniel shared a side project he wants to start working on after the current sprint. He is transforming a custom GPT-based knowledge assistant into a scalable paid SaaS product[^2].

Today, there is a working GPT inside ChatGPT that was built using proprietary educational content from his company, focused on the audiovisual / video production market. The GPT is trained with the company's internal methodology, documents, and learning materials, and users can interact with it to ask questions and receive guidance related to this methodology[^2].

The current limitation is that users must log in with their own ChatGPT accounts to access the assistant, which creates friction and is not ideal for a commercial product experience[^2].

The goal is to turn this into an independent platform where:

- Users can create accounts and log in directly on the website
- Access is restricted to paying subscribers
- The AI assistant is embedded into the platform experience
- Payments / subscriptions are integrated
- Usage and costs can be controlled sustainably[^2]

One of the main challenges Daniel is trying to solve is designing a pricing and access-control strategy that keeps the business financially sustainable.

Since AI usage costs are paid by his company through API consumption, he needs to think carefully about[^2]:

- Subscription models
- Rate limits
- Usage caps
- Abuse prevention
- Profitability and cost control

At this stage, Daniel is looking for guidance mainly around[^2]:

- Overall architecture decisions
- SaaS / platform design
- Authentication and subscription flows
- AI cost management strategies
- Best practices for scaling this kind of AI-powered product
- Tradeoffs between speed of implementation vs long-term maintainability

## Sources

[^1]: [20260420_085551_valeriia_kuka_msg3459.md](../../../inbox/used/20260420_085551_valeriia_kuka_msg3459.md)
[^2]: [20260509_123930_AlexeyDTC_msg4006.md](../../../inbox/used/20260509_123930_AlexeyDTC_msg4006.md)
