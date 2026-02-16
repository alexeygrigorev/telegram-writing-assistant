---
title: "CRISP-DM for AI"
created: 2026-02-08
updated: 2026-02-16
tags: [ai-engineering, methodology, crisp-dm, processes]
status: draft
---

# CRISP-DM for AI

CRISP-DM (Cross-Industry Standard Process for Data Mining) is a methodology from 1996 that organized how data mining and ML teams work. What's remarkable is that this framework, originally designed for data mining, remains highly relevant for AI projects today[^1].

## Why CRISP-DM Still Matters

All the processes that data teams have used since the 1990s remain applicable to AI projects. The steps we take in AI projects map directly to the CRISP-DM framework.

I wrote about CRISP-DM in my book, and the concepts described there apply equally to modern AI engineering[^2].

<figure>
  <img src="../assets/images/crisp-dm-for-ai/crisp-dm-cycle.jpg" alt="CRISP-DM cycle diagram showing six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment">
  <figcaption>The CRISP-DM cycle: six phases that form an iterative process for data-driven projects</figcaption>
  <!-- This diagram illustrates the cyclical nature of AI projects, where each phase informs the others -->
</figure>

## Running Example: Online Classifieds with AI

To illustrate how CRISP-DM applies to AI, we use the same example as in the AI Engineer vision article: an online classifieds platform. In machine learning, we would have a classification problem. In the AI case, we upload an image and from this image we want to reliably extract the information we need[^10].

## Mapping CRISP-DM to AI Projects

### Business Understanding

We don't just solve problems for the sake of solving problems. Not "hey, we have AI, how about we use it" and then start thinking of different use cases. No - it should come from a real user problem. Maybe we already know about this problem. We already tried to solve it differently, but now we think we want to try to solve it with AI[^10].

We need to have this business understanding. What is the problem? Why do we want to do this? Not just because we want a cool new feature, but because there is a real problem that users have with our product that we will solve. This is usual work that product managers do, user experience researchers do. There should be a real problem or a hypothesis that this problem exists and we want to verify this hypothesis[^10].

We need to understand: how many people does this affect? At this point, we think more about the problem, not the solution. How can we measure it? What could be the metric for solving this problem?[^10]

For the classifieds example: users complain that it takes so much time to fill the form. There is some existing user research that confirms this. Otherwise we need to conduct this research to find out this is actually a problem worth solving. Maybe users don't really complain about this. If we solve a problem that doesn't exist, nobody will care and we waste money and time[^10].

Then our goal becomes clear. Right now it takes five minutes to fill the form, and we think we can reduce this time to one minute. We can also have secondary metrics - like users who started filling the form and didn't finish because it was too complex. Right now that is 15%, but we want to drop it to 5%. The important part is we need to have this research, we need to understand there is a problem, and we need to understand this is a way to solve it[^10].

For integrating AI into products, this is very important. We don't want to spend time on solving a problem that doesn't exist[^10].

The AI engineer's role here is to work with product managers to understand: do we actually need AI here, or is there something simpler we can do? Previously for machine learning, building a model was more expensive and took more time. Sometimes you could solve the problem by using rules. In case of AI, testing a hypothesis is cheaper in terms of time, but we still need to understand if it is worth solving with AI or if we can use something else[^11].

### Data Understanding

At this point, we want to understand if there is data we can rely on to build our model. In case of machine learning, we need to determine if we have training data. In case of AI, we need to understand what data we have available[^12].

We need to send something to AI. Do we have everything we need for that? We want to understand how difficult it would be to integrate what we need. In our example, when we send data to AI, we need to make sure the front end can send all the data we need. That is one thing[^13].

But let's say we are talking about integrating AI into something else - it could be something not user-facing, running on the backend. You can use AI to optimize some processes. There it is very important that you have some data for AI to act on, because it needs to get in some data[^13].

In our case, the input will be a picture. Of course, in our case it is easy - we already have the picture[^13].

For RAG cases, we also need to think about data understanding and data preparation. Do we have all the data we need? Do we have the integrations we need? Some services are not easy to integrate to or access. This is something we also need to keep in mind[^16].

<!-- TODO: Brainstorm what other projects would look like for data understanding and data preparation steps -->

### Data Preparation

In case of machine learning, we just need to fetch the data from different sources. We need to prepare it in the right format. For this particular case, it is less important. But if we want to use AI for recommendations or search or things like that, of course we need to have data available[^14].

In some cases, where we want to integrate into products like search and recommendation, we need to be able to access this data[^14].

We are talking about data preparation steps. We need to prepare data in such a way that we can put this into the model. In our case, it is an image, it is text. This is fairly simple. We just fetch whatever image was sent to us from the front end. We send it to OpenAI, we process, we get data, and we send it back. There is not much data pre-processing[^15].

For agents that need to access things, we need to think about whether we have all the data we need and whether we have the integrations we need. Some services are not easy to integrate to or access[^16].

### Modeling

There is not much of a traditional modeling step, but I would change it a little[^15].

In case of ML, here we do the actual training. We train the actual model. We also evaluate the model - cross validation, all sorts of things. In the AI case: we have the prompt, we have our output class (the Pydantic model), we have input. Then we set up the validation framework, we set up the tests for our AI system[^15].

We need to collect evaluation data, we need to evaluate our model. This is a process very similar to what we would do with machine learning, except we don't train the model. We have other criteria, other things we are optimizing. The important thing is that we have a metric - not necessarily a business metric, but more like a technical metric for how many images we are able to extract correctly. Then we change our prompt, we tune our prompt, we do other things[^15].

Important thing in CRISP-DM: the evaluation we do with cross-validation and metrics like accuracy is not the "evaluation" step in CRISP-DM. That belongs to the modeling step[^15].

### Evaluation

At the evaluation step, we actually see how it affects the product and how it affects the users. We take what we developed and we roll it out to users. We run some sort of A/B tests[^17].

We remember at the business understanding step we defined the metric. Here we see if this metric is good. We also collect feedback from people - this implicit feedback. We see how often people change the output, how good it is. But the important thing is if users were able to do this faster than before[^17].

Here we can introduce extra metrics to measure the performance of our model, but the main metric was defined in business understanding. Here we can see if this is good or not[^17].

CRISP-DM is a fairly old model. Before, evaluation and deployment were kind of separate, but now they are almost the same. You deploy to a part of users and then if everything works, you say okay, it is good. We can roll this to everyone[^17].

If during the evaluation we see something is off, we either refine our business understanding, or we can say: with what we have right now, it doesn't seem valuable to continue with this project, so we are parking it for now. This could be an outcome too - saying that we cannot achieve what we wanted. And this is an outcome too. Between the initial idea and this outcome, ideally you want to spend as little time as possible[^17].

This would be the first iteration, but on the second iteration, you would spend more time. The goal is to iterate. This process is very iterative - you iterate as many times as possible[^17].

### Deployment

Deployment remains similar: putting the system into production. The entire process is iterative - we cycle through these steps until performance is satisfactory[^8].

## Who is Involved at Each Step

The roles involved at each CRISP-DM step[^18]:

- Business understanding - product managers, AI engineers. AI engineers help PMs understand if it is something AI can solve
- Data understanding - data analysts, product managers, AI engineers, backend engineers. Together with analysts, AI engineers try to understand the data. Could involve people from other teams if you need data from there
- Data preparation - data engineers and AI engineers. If you don't have a data engineer in the team, AI engineer will need to do this
- Modeling - strictly AI engineers
- Evaluation - AI engineers, analysts, product managers. Analysts help set up the A/B test. PMs need to be involved to double-check that we track the right metrics. We need to set up the experiment properly
- Deployment - AI engineers, platform engineers

AI engineers are involved in pretty much every step[^18].

## The Iterative Nature

CRISP-DM emphasizes that projects are iterative. We never truly "finish" - we iterate until we achieve satisfactory results, then continue improving. This iterative approach is essential for AI projects where:
- User behavior may be unpredictable
- Prompts need refinement
- Evaluation metrics may need adjustment

This is a valid framework for AI projects. You don't necessarily have to follow each step, but it gives a good mental model to understand how you can approach not only machine learning projects, but also AI projects[^17].

## Historical Context

The fact that a framework from 1996 remains relevant tells us something important: while the tools change (from training models to API calls), the fundamental process of building data-driven products remains constant.

The processes data scientists have always used - evaluation, versioning, experimentation - are exactly what AI engineers need today. This is why data scientists often make excellent AI engineers with some additional coding practice[^9].

## Sources

[^1]: [20260208_114819_AlexeyDTC_msg1192_transcript.txt](../inbox/used/20260208_114819_AlexeyDTC_msg1192_transcript.txt)
[^2]: [CRISP-DM Article at ML Bookcamp](https://mlbookcamp.com/article/crisp-dm) - Original article explaining the CRISP-DM methodology
[^3]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/used/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^4]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/used/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^5]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/used/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^6]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/used/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^7]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/used/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^8]: [20260208_115250_AlexeyDTC_msg1198_transcript.txt](../inbox/used/20260208_115250_AlexeyDTC_msg1198_transcript.txt)
[^9]: [20260208_114623_AlexeyDTC_msg1188_transcript.txt](../inbox/used/20260208_114623_AlexeyDTC_msg1188_transcript.txt)
[^10]: [20260216_133539_AlexeyDTC_msg1757_transcript.txt](../inbox/used/20260216_133539_AlexeyDTC_msg1757_transcript.txt)
[^11]: [20260216_133631_AlexeyDTC_msg1759_transcript.txt](../inbox/used/20260216_133631_AlexeyDTC_msg1759_transcript.txt)
[^12]: [20260216_133802_AlexeyDTC_msg1761_transcript.txt](../inbox/used/20260216_133802_AlexeyDTC_msg1761_transcript.txt)
[^13]: [20260216_134020_AlexeyDTC_msg1763_transcript.txt](../inbox/used/20260216_134020_AlexeyDTC_msg1763_transcript.txt)
[^14]: [20260216_134346_AlexeyDTC_msg1765_transcript.txt](../inbox/used/20260216_134346_AlexeyDTC_msg1765_transcript.txt)
[^15]: [20260216_134601_AlexeyDTC_msg1767_transcript.txt](../inbox/used/20260216_134601_AlexeyDTC_msg1767_transcript.txt)
[^16]: [20260216_134943_AlexeyDTC_msg1771_transcript.txt](../inbox/used/20260216_134943_AlexeyDTC_msg1771_transcript.txt)
[^17]: [20260216_134855_AlexeyDTC_msg1769_transcript.txt](../inbox/used/20260216_134855_AlexeyDTC_msg1769_transcript.txt)
[^18]: [20260216_135139_AlexeyDTC_msg1773_transcript.txt](../inbox/used/20260216_135139_AlexeyDTC_msg1773_transcript.txt)
