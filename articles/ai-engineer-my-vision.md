---
title: "AI Engineer My Vision"
created: 2026-02-08
updated: 2026-02-16
tags: [ai-engineering, roles, career]
status: draft
---

# AI Engineer My Vision

This article describes my personal vision of the AI engineer role, based on my own experience rather than industry surveys or external data.

## Context

I'm preparing for a "Day of AI Engineer" event and want to share how I see this role. The high interest in previous posts about webinars confirmed there's appetite for this content. Rather than relying on others' data or surveys, I want to describe the role from my direct experience.

As someone teaching AI engineering courses and working with ML and AI for years, I have a clear vision of what the AI Engineer role should be. I'm collecting data to compare my vision with industry reality.

I also have a reference article about data team roles at DataTalks.Club[^4]. It is about 5-6 years old now, but it describes the roles in a data team: Product Managers, Data Analysts, Data Scientists, Data Engineers, ML Engineers, and MLOps Engineers. Things have changed since then, and this event is a good opportunity to revisit these roles in the context of AI engineering[^5].

## Core Responsibility: AI Integration

The main responsibility of the AI Engineer is integrating AI into the product, whatever that means[^6]. In practice, integrating AI into a product typically means interacting with an LLM provider like OpenAI, Anthropic, or others through their API. You know how to call this API, it returns something, and then you integrate these results into whatever product you are working on.

The work involves:
- Calling LLM APIs through providers
- Integrating AI capabilities into existing products
- Building features that leverage LLMs

## Simple Example: Online Classifieds with AI Pre-filling

To illustrate what AI engineers do, consider this example. We have a web interface for an online classifieds website where you can upload anything. Based on what you upload, it classifies the type, extracts the details, and fills everything automatically[^6].

I created this website with Lovable. The prompt was: create an online classifieds platform where people can create and see things to buy and sell. It will be very simplistic - a list page with products, a create page where we create a listing (title, description, categories, and a place to upload a single image). Plus there's a contact button that currently doesn't do anything. The listings come from API (mock it for now) and when we save the event, it also saves into the API. We also pre-fill the details with AI. The posting flow: first they ask the image, you upload, and then you see the form with all pre-filled information from the image. All the API interactions are in a single file[^7].

<figure>
  <img src="../assets/images/ai-engineer-my-vision/lovable-bazaar-marketplace.jpg" alt="Screenshot of Lovable creating the Bazaar marketplace with the prompt visible on the left and the marketplace preview on the right">
  <figcaption>Creating the marketplace with Lovable - first prompt created the initial "Bazaar" version</figcaption>
  <!-- Shows the Lovable interface with the initial prompt on the left and the resulting marketplace with product categories and listings on the right -->
</figure>

With a second prompt, I asked Lovable to rename the website and switch to EUR pricing[^8].

<figure>
  <img src="../assets/images/ai-engineer-my-vision/lovable-trova-rename.jpg" alt="Screenshot of Lovable renaming the marketplace to Trova and switching to euro pricing">
  <figcaption>Second prompt: renamed to "Trova" and switched currency to euros</figcaption>
  <!-- Shows the conversation with Lovable on the left asking to rename and switch currency, and the updated Trova marketplace on the right -->
</figure>

Then I exported this from Lovable and added backend support with Claude Code[^9].

<figure>
  <img src="../assets/images/ai-engineer-my-vision/claude-code-backend-start.jpg" alt="Claude Code v2.1.42 interface showing the prompt to create a FastAPI backend for the marketplace">
  <figcaption>Using Claude Code to create the FastAPI backend for the marketplace</figcaption>
  <!-- Shows Claude Code receiving the instruction to create a FastAPI backend with listing endpoints and AI pre-filling -->
</figure>

I asked Claude Code to create a simple FastAPI backend that takes care of listings and pre-filling with AI. It should return the content, and there would be two endpoints: one for adding a listing and another for pre-filling it with AI[^9].

### What the AI engineer does with this example

This looks pretty straightforward. We upload a picture. Instead of writing the title, the description, the category - it should automatically extract everything we need. All we need to do is define the schema, send the request to OpenAI, describe a prompt, and test locally that things work. That's it, right?[^10]

But not quite. Here is everything that needs to happen:

1. The prompt - how good is this prompt? We need to test it. We need to make sure that the agent is actually doing what we want. We create a test where we send an image and verify the output[^10].

2. Evaluation dataset - we can have a few tests, but we can also have an evaluation set where we have a bunch of images. We run this extraction process and verify that every time we run with the current prompt, we get what we want. This becomes our evaluation dataset. Tests must always pass. The evaluation dataset gives us a metric of how good our model is doing. Sometimes the model describes something incorrectly - it is not the end of the world. Sometimes it is really important. We define all that[^10].

3. Iterating on the prompt - we change something in the prompt, we run the evaluation set, we see that the model is not degrading. It is very important to have all these things[^10].

4. Rolling out to users - if everything works, we can roll it out. But how? We need to make sure there are no regressions so user experience stays good. We split this to do an A/B test - roll out to a small portion of people first[^10].

5. Production monitoring - we observe that there are no errors. It is very important to have proper production monitoring. In how many cases does our endpoint not return anything? It breaks. We need a dashboard for that[^10].

6. Collecting logs and inspecting results - we also need to know in how many cases this does not work. We need to be able to inspect the results, inspect the input, inspect the output, and see if things are misaligned[^10].

7. Human annotators - we can add humans here, human annotators that regularly sample data from this monitoring system and verify things work. When humans evaluate and we roll it out to some users, they can see some problematic cases. We can actually add these to our evaluation set[^10].

8. Model updates - we deploy the system, everything works, we rolled out to all users, we have monitoring, we have evaluation set, we have testing. Then OpenAI releases a new model. We need to update to the new model. We run it on the evaluation set and we see that things don't work so well as before. But because we have evaluations, we can actually determine this[^10].

9. Prompt versioning - when we iterate on the prompt, we need version control for prompts. How do we control the version of the prompt? We need a proper experimentation system in place. Could be MLflow, could be just keeping things in Git, but it is something important. When we evaluate something, we need to know what we changed. Did we change the prompt? Maybe if we are working on an agent, we changed some tools, maybe we changed the model. We need to know what exactly we changed. We need to properly set the experiment - this is the change and this is the result[^10].

10. Feedback from users - we also need to collect feedback. Feedback could be explicit - if we add a thumbs up or thumbs down button and the user clicks on that, that is explicit feedback. But also implicit - maybe the user corrects the output. We need to think about all these things[^10].

Even for this simplest example, there are so many things that need to happen. It is not enough to just define a Pydantic class, send it to OpenAI, and call it a day. There is a lot of things that need to happen to properly integrate this into the product[^11].

We did not even talk about UI changes. There also need to be UI changes. Typically front-end engineers do this, but in some cases, if you work at a startup, AI engineers might also do that. With AI assistance like Claude Code, it doesn't really matter if your TypeScript knowledge is not the best. AI engineers or any engineer can make these changes, they can integrate this into the product. But typically in bigger companies, it would be a front-end engineer[^11].

<!-- TODO: Add screenshot of the completed backend tests here -->
<!-- TODO: Add screenshot of the evaluation framework in action -->
<!-- TODO: Add screenshot of the monitoring dashboard -->

<figure>
  <img src="../assets/images/ai-engineer-my-vision/claude-code-backend-progress.jpg" alt="Claude Code todo list showing backend implementation progress with completed tasks">
  <figcaption>Claude Code working on the example project - backend structure, API endpoints, AI service, and tests</figcaption>
  <!-- Shows the Claude Code task list with completed items: restructure into monorepo, initialize backend, implement database layer, API endpoints, AI image analysis service, update frontend, and currently writing backend tests -->
</figure>

In this example, we have tests, we have CI/CD, you can see everything that is implemented. These are placeholders throughout the article where we can illustrate these things, to show what AI engineers do[^12][^13].

### Also CI/CD

When we talk about testing and deployment, CI/CD is important. When we run tests, we want to be able to run these tests on push to Git. When we deploy, we want to be able to deploy to a staging environment. When our tests on the staging environment pass, we want to roll out to production. Setting this up, of course, the AI engineer would not be doing this alone. Typically there could be some platform engineers that help. But if it is a startup, knowing how to do these things will certainly help[^14].

## Complex Scenarios: RAG and Agents

That was just a very simple thing. But imagine we go from this simple thing to RAG. We make our process more complex. Now we have a search engine that we need to use, something like Elasticsearch. We need to ingest the data. We need to know how to build data pipelines, and how to build data pipelines reliably, because the data is coming from somewhere. We need to put it into our search engine. This could be a vector search engine or a text search engine. We need to be able to do that. Sometimes, oftentimes, we need to be able to provision the infrastructure for that[^14].

<!-- TODO: Add diagram showing RAG pipeline architecture -->

For agents, we need to know tool calling and things like that. When we have tools, we need to make sure agents can use these tools reliably. We need to be able to write tests for tools and for the agent behavior. With tools, everything becomes more complex. We need to write our tests and update our evaluation framework, evaluation criteria - in this scenario, these tools must be used, things like that[^15].

In the simple case, it is already a lot of work. In more complex cases with RAG and agents, the complexity is maybe 10 times more than before. All these things are solved by AI engineers[^15].

## The Role is Similar to ML Engineering

It is very similar to data science. If you think about data science - what data scientists need to do, what ML engineers need to do - they need to integrate machine learning into the product. Here everything is similar. The roles of ML engineer and AI engineer are very similar[^14].

## Solving Real Problems with AI

The AI engineer's approach involves:

1. Understanding the problem - What exactly are we trying to solve? What would success look like?

2. Prompt engineering - Crafting effective prompts to get the desired behavior from AI models

3. Experimentation - This is critical. AI engineering requires continuous experimentation through A/B testing. We show a new feature to a portion of traffic, measure how users respond, and iterate based on results

## Key Skills

What AI engineers need to know[^10]:
- How to interact with API
- How to create web services
- How to create tests
- Evaluation strategy
- Production monitoring (endpoint monitoring, web service monitoring, AI monitoring)
- Collecting logs
- Adding humans in the loop for evaluation
- Setting up processes for collecting user feedback (explicit and implicit)

## What AI Engineers Don't Focus On

Unlike traditional ML engineers, AI engineers typically don't:
- Fine-tune models from scratch
- Build custom model architectures
- Focus heavily on feature engineering in the traditional ML sense

Instead, they focus on:
- Engineering best practices for AI systems
- Effective prompt design and versioning
- Integration of AI capabilities into products

This vision guides both my teaching and my research into how the industry actually defines and hires for AI Engineer roles.

## Sources

[^1]: [20260208_114623_AlexeyDTC_msg1188_transcript.txt](../inbox/used/20260208_114623_AlexeyDTC_msg1188_transcript.txt)
[^2]: [20260204_102339_AlexeyDTC_msg900_transcript.txt](../inbox/used/20260204_102339_AlexeyDTC_msg900_transcript.txt)
[^3]: [20260204_102429_AlexeyDTC_msg902_transcript.txt](../inbox/used/20260204_102429_AlexeyDTC_msg902_transcript.txt)
[^4]: [Data Team Roles Explained](https://datatalks.club/blog/data-roles.html)
[^5]: [20260216_125341_AlexeyDTC_msg1721_transcript.txt](../inbox/used/20260216_125341_AlexeyDTC_msg1721_transcript.txt)
[^6]: [20260216_125634_AlexeyDTC_msg1727_transcript.txt](../inbox/used/20260216_125634_AlexeyDTC_msg1727_transcript.txt)
[^7]: [20260216_130544_AlexeyDTC_msg1729_photo.md](../inbox/used/20260216_130544_AlexeyDTC_msg1729_photo.md)
[^8]: [20260216_130631_AlexeyDTC_msg1731_photo.md](../inbox/used/20260216_130631_AlexeyDTC_msg1731_photo.md)
[^9]: [20260216_130937_AlexeyDTC_msg1735_photo.md](../inbox/used/20260216_130937_AlexeyDTC_msg1735_photo.md)
[^10]: [20260216_131724_AlexeyDTC_msg1737_transcript.txt](../inbox/used/20260216_131724_AlexeyDTC_msg1737_transcript.txt)
[^11]: [20260216_131833_AlexeyDTC_msg1739_transcript.txt](../inbox/used/20260216_131833_AlexeyDTC_msg1739_transcript.txt)
[^12]: [20260216_140036_AlexeyDTC_msg1777_photo.md](../inbox/used/20260216_140036_AlexeyDTC_msg1777_photo.md)
[^13]: [20260216_140204_AlexeyDTC_msg1779_transcript.txt](../inbox/used/20260216_140204_AlexeyDTC_msg1779_transcript.txt)
[^14]: [20260216_132048_AlexeyDTC_msg1741_transcript.txt](../inbox/used/20260216_132048_AlexeyDTC_msg1741_transcript.txt)
[^15]: [20260216_132214_AlexeyDTC_msg1743_transcript.txt](../inbox/used/20260216_132214_AlexeyDTC_msg1743_transcript.txt)
