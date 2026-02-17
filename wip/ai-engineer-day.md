---
title: "Day of AI Engineer"
created: 2026-02-16
updated: 2026-02-16
tags: [ai-engineering, roles, career, ml-engineering, data-science, methodology, crisp-dm, processes]
status: draft
---

# Day of AI Engineer

This article describes my personal vision of the AI engineer role, compares it with traditional data team roles, and shows how the CRISP-DM methodology applies to AI projects.

## Context

I'm preparing for a "Day of AI Engineer" event and want to share how I see this role. The high interest in previous posts about webinars confirmed there's appetite for this content. Rather than relying on others' data or surveys, I want to describe the role from my direct experience.

As someone teaching AI engineering courses and working with ML and AI for years, I have a clear vision of what the AI Engineer role should be. I'm collecting data to compare my vision with industry reality.

I also have a reference article about data team roles at DataTalks.Club. It is about 5-6 years old now, but it describes the roles in a data team: Product Managers, Data Analysts, Data Scientists, Data Engineers, ML Engineers, and MLOps Engineers. Things have changed since then, and this event is a good opportunity to revisit these roles in the context of AI engineering.

## Core Responsibility: AI Integration

The main responsibility of the AI Engineer is integrating AI into the product, whatever that means. In practice, integrating AI into a product typically means interacting with an LLM provider like OpenAI, Anthropic, or others through their API. You know how to call this API, it returns something, and then you integrate these results into whatever product you are working on.

The work involves:
- Calling LLM APIs through providers
- Integrating AI capabilities into existing products
- Building features that leverage LLMs

## Simple Example: Online Classifieds with AI Pre-filling

To illustrate what AI engineers do, consider this example. We have a web interface for an online classifieds website where you can upload anything. Based on what you upload, it classifies the type, extracts the details, and fills everything automatically.

I created this website with Lovable. The prompt was: create an online classifieds platform where people can create and see things to buy and sell. It will be very simplistic - a list page with products, a create page where we create a listing (title, description, categories, and a place to upload a single image). Plus there's a contact button that currently doesn't do anything. The listings come from API (mock it for now) and when we save the event, it also saves into the API. We also pre-fill the details with AI. The posting flow: first they ask the image, you upload, and then you see the form with all pre-filled information from the image. All the API interactions are in a single file.

<figure>
  <img src="../assets/images/ai-engineer-my-vision/lovable-bazaar-marketplace.jpg" alt="Screenshot of Lovable creating the Bazaar marketplace with the prompt visible on the left and the marketplace preview on the right">
  <figcaption>Creating the marketplace with Lovable - first prompt created the initial "Bazaar" version</figcaption>
  <!-- Shows the Lovable interface with the initial prompt on the left and the resulting marketplace with product categories and listings on the right -->
</figure>

With a second prompt, I asked Lovable to rename the website and switch to EUR pricing.

<figure>
  <img src="../assets/images/ai-engineer-my-vision/lovable-trova-rename.jpg" alt="Screenshot of Lovable renaming the marketplace to Trova and switching to euro pricing">
  <figcaption>Second prompt: renamed to "Trova" and switched currency to euros</figcaption>
  <!-- Shows the conversation with Lovable on the left asking to rename and switch currency, and the updated Trova marketplace on the right -->
</figure>

Then I exported this from Lovable and added backend support with Claude Code.

<figure>
  <img src="../assets/images/ai-engineer-my-vision/claude-code-backend-start.jpg" alt="Claude Code v2.1.42 interface showing the prompt to create a FastAPI backend for the marketplace">
  <figcaption>Using Claude Code to create the FastAPI backend for the marketplace</figcaption>
  <!-- Shows Claude Code receiving the instruction to create a FastAPI backend with listing endpoints and AI pre-filling -->
</figure>

I asked Claude Code to create a simple FastAPI backend that takes care of listings and pre-filling with AI. It should return the content, and there would be two endpoints: one for adding a listing and another for pre-filling it with AI.

### What the AI engineer does with this example

This looks pretty straightforward. We upload a picture. Instead of writing the title, the description, the category - it should automatically extract everything we need. All we need to do is define the schema, send the request to OpenAI, describe a prompt, and test locally that things work. That's it, right?

But not quite. Here is everything that needs to happen:

1. The prompt - how good is this prompt? We need to test it. We need to make sure that the agent is actually doing what we want. We create a test where we send an image and verify the output.

2. Evaluation dataset - we can have a few tests, but we can also have an evaluation set where we have a bunch of images. We run this extraction process and verify that every time we run with the current prompt, we get what we want. This becomes our evaluation dataset. Tests must always pass. The evaluation dataset gives us a metric of how good our model is doing. Sometimes the model describes something incorrectly - it is not the end of the world. Sometimes it is really important. We define all that.

3. Iterating on the prompt - we change something in the prompt, we run the evaluation set, we see that the model is not degrading. It is very important to have all these things.

4. Rolling out to users - if everything works, we can roll it out. But how? We need to make sure there are no regressions so user experience stays good. We split this to do an A/B test - roll out to a small portion of people first.

5. Production monitoring - we observe that there are no errors. It is very important to have proper production monitoring. In how many cases does our endpoint not return anything? It breaks. We need a dashboard for that.

6. Collecting logs and inspecting results - we also need to know in how many cases this does not work. We need to be able to inspect the results, inspect the input, inspect the output, and see if things are misaligned.

7. Human annotators - we can add humans here, human annotators that regularly sample data from this monitoring system and verify things work. When humans evaluate and we roll it out to some users, they can see some problematic cases. We can actually add these to our evaluation set.

8. Model updates - we deploy the system, everything works, we rolled out to all users, we have monitoring, we have evaluation set, we have testing. Then OpenAI releases a new model. We need to update to the new model. We run it on the evaluation set and we see that things don't work so well as before. But because we have evaluations, we can actually determine this.

9. Prompt versioning - when we iterate on the prompt, we need version control for prompts. How do we control the version of the prompt? We need a proper experimentation system in place. Could be MLflow, could be just keeping things in Git, but it is something important. When we evaluate something, we need to know what we changed. Did we change the prompt? Maybe if we are working on an agent, we changed some tools, maybe we changed the model. We need to know what exactly we changed. We need to properly set the experiment - this is the change and this is the result.

10. Feedback from users - we also need to collect feedback. Feedback could be explicit - if we add a thumbs up or thumbs down button and the user clicks on that, that is explicit feedback. But also implicit - maybe the user corrects the output. We need to think about all these things.

Even for this simplest example, there are so many things that need to happen. It is not enough to just define a Pydantic class, send it to OpenAI, and call it a day. There is a lot of things that need to happen to properly integrate this into the product.

We did not even talk about UI changes. There also need to be UI changes. Typically front-end engineers do this, but in some cases, if you work at a startup, AI engineers might also do that. With AI assistance like Claude Code, it doesn't really matter if your TypeScript knowledge is not the best. AI engineers or any engineer can make these changes, they can integrate this into the product. But typically in bigger companies, it would be a front-end engineer.

<!-- TODO: Add screenshot of the completed backend tests here -->
<!-- TODO: Add screenshot of the evaluation framework in action -->
<!-- TODO: Add screenshot of the monitoring dashboard -->

<figure>
  <img src="../assets/images/ai-engineer-my-vision/claude-code-backend-progress.jpg" alt="Claude Code todo list showing backend implementation progress with completed tasks">
  <figcaption>Claude Code working on the example project - backend structure, API endpoints, AI service, and tests</figcaption>
  <!-- Shows the Claude Code task list with completed items: restructure into monorepo, initialize backend, implement database layer, API endpoints, AI image analysis service, update frontend, and currently writing backend tests -->
</figure>

In this example, we have tests, we have CI/CD, you can see everything that is implemented. These are placeholders throughout the article where we can illustrate these things, to show what AI engineers do.

### Also CI/CD

When we talk about testing and deployment, CI/CD is important. When we run tests, we want to be able to run these tests on push to Git. When we deploy, we want to be able to deploy to a staging environment. When our tests on the staging environment pass, we want to roll out to production. Setting this up, of course, the AI engineer would not be doing this alone. Typically there could be some platform engineers that help. But if it is a startup, knowing how to do these things will certainly help.

## Complex Scenarios: RAG and Agents

That was just a very simple thing. But imagine we go from this simple thing to RAG. We make our process more complex. Now we have a search engine that we need to use, something like Elasticsearch. We need to ingest the data. We need to know how to build data pipelines, and how to build data pipelines reliably, because the data is coming from somewhere. We need to put it into our search engine. This could be a vector search engine or a text search engine. We need to be able to do that. Sometimes, oftentimes, we need to be able to provision the infrastructure for that.

<!-- TODO: Add diagram showing RAG pipeline architecture -->

For agents, we need to know tool calling and things like that. When we have tools, we need to make sure agents can use these tools reliably. We need to be able to write tests for tools and for the agent behavior. With tools, everything becomes more complex. We need to write our tests and update our evaluation framework, evaluation criteria - in this scenario, these tools must be used, things like that.

In the simple case, it is already a lot of work. In more complex cases with RAG and agents, the complexity is maybe 10 times more than before. All these things are solved by AI engineers.

## The Role is Similar to ML Engineering

It is very similar to data science. If you think about data science - what data scientists need to do, what ML engineers need to do - they need to integrate machine learning into the product. Here everything is similar. The roles of ML engineer and AI engineer are very similar.

## Solving Real Problems with AI

The AI engineer's approach involves:

1. Understanding the problem - What exactly are we trying to solve? What would success look like?

2. Prompt engineering - Crafting effective prompts to get the desired behavior from AI models

3. Experimentation - This is critical. AI engineering requires continuous experimentation through A/B testing. We show a new feature to a portion of traffic, measure how users respond, and iterate based on results

## Key Skills

What AI engineers need to know:
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

## AI Engineers vs ML Engineers

The task of an ML engineer is to integrate machine learning into the product. The task of AI engineers is to integrate AI into the product. What is the difference?

Typically, if we talk about LLM providers, the difference is that you already have an LLM, you just call the web service, versus actually having the weights and owning the model. In some cases, yes, we have open source LLMs. There are cases where you need to serve the LLM yourself. Then this becomes your responsibility as AI engineer too. In traditional ML, it is always the responsibility of the ML engineer to actually serve the model.

### LLM Serving

There are many tools for serving LLMs, like vLLM, but the tools are secondary - just knowing that you need to do this matters. LLMs require special hardware. You also need to know how to provision infrastructure for this hardware. Typically this is also on the AI engineer. For an ML engineer, it could be similar - if you need to serve a neural network model, the difference is that LLMs require a lot more power, bigger GPUs. This is the main difference with ML engineers.

## AI Engineers vs Data Scientists

Data scientists focus on training models, experimenting with models, conducting experiments, translating requirements from product to machine learning terms. They work on creating data and so on.

When it comes to AI (using LLMs), the model is already there. People from OpenAI trained the model, so they went through the process. We don't need this. In cases when we do something simple, when we don't need to fine-tune, when we don't need to do anything else - we don't really need data scientists. It depends on the size of the organization, but if we talk about a small AI team, we don't really need data scientists here.

## Bigger Organizations: Traditional ML + AI

In bigger organizations where we have also classical machine learning, the setup is: data scientists work on a model, on translating requirements into machine learning terms, and ML engineers work together with data scientists to productionize it. The engineer focuses more on serving the model, CI/CD, tests, best engineering practices, infrastructure. Data scientists focus more on modeling, testing, experimenting.

Now let's say there is already a team that has been doing machine learning for quite some time, but now they have an AI use case. In this setup, both data scientists and ML engineers would work on it. Data scientists would focus more on interacting with the model, understanding how to call it, how to tune the prompt, how to set up the validation framework - how to make sure that the model, the agent is behaving the way it should behave. The ML engineer would focus more on the engineering aspects. This would be the setup in teams where there is not necessarily an AI engineer yet. They would split the responsibilities of AI engineer into both roles. And frankly, if we talk about a bigger project, bigger company, they will both have so much work.

The company might decide to hire an AI engineer who will work together with data scientists on these things. But the data scientists will also have responsibilities of taking care of traditional machine learning, maybe some legacy systems, but also some systems that they need now - because LLM is not the answer to all the questions. AI now is very good at solving a subset of some problems, but there are so many problems that don't need LLMs. We still need data scientists, we still need machine learning engineers. They still need to work on what they have been working on. But some problems are of course simpler now - NLP is simpler, many things are simpler now with LLMs.

## What Changed

### The Disappearing Data Scientist

The traditional Data Scientist role is becoming less relevant in AI teams. Why? Because we're no longer training models from scratch. Instead, we make API calls to providers like OpenAI.

The focus has shifted from:
- Model training and fine-tuning
- Feature engineering for traditional ML
- Building custom model architectures

To:
- Engineering practices - how to properly integrate AI into systems
- Evaluation - measuring AI system performance
- Prompt versioning - managing prompt evolution
- Experimentation - A/B testing AI features

### Data Scientists Become AI Engineers

Data Scientists are well-positioned to transition to AI engineering. The skills that transfer:

- Evaluation - Data scientists have always measured model performance
- Versioning - They understand the importance of tracking experiments
- Experimental mindset - A/B testing and iterative improvement

What they need to add:
- Stronger coding skills
- Understanding of AI APIs and prompt engineering
- Production engineering practices

### ML Engineers Become AI Engineers

Similarly, ML Engineers can transition to AI engineering. Their foundation in:
- Productionizing models
- Engineering best practices
- Working with other engineering teams

Provides a solid base. What they need:
- Learn the specific patterns of AI Engineering Buildcamp
- Understand prompt engineering and evaluation for AI systems

The path from ML Engineer or Data Scientist to AI Engineer is straightforward because the foundational knowledge already exists.

## Teams Without "AI" in the Name

Many companies don't have dedicated AI engineer roles. Instead, existing team members take on AI responsibilities:

- Data Scientists focus on designing experiments and evaluation
- ML Engineers focus more on monitoring and deployment

The job titles may be old, but the tasks are new. Instead of training models from scratch, they use OpenAI or similar APIs. Everything else remains the same.

In teams where we don't have AI engineers, the responsibilities would be split between data scientists and ML engineers.

## Career Paths

For Data Scientists and ML Engineers, the transition to AI Engineer is natural:
- The base skills are already there
- The focus shifts from model training to prompt engineering
- Evaluation and experimentation remain core competencies

What we teach in AI Engineering Buildcamp covers exactly what's needed for this transition.

## CRISP-DM for AI

CRISP-DM (Cross-Industry Standard Process for Data Mining) is a methodology from 1996 that organized how data mining and ML teams work. What's remarkable is that this framework, originally designed for data mining, remains highly relevant for AI projects today.

### Why CRISP-DM Still Matters

All the processes that data teams have used since the 1990s remain applicable to AI projects. The steps we take in AI projects map directly to the CRISP-DM framework.

I wrote about CRISP-DM in my book, and the concepts described there apply equally to modern AI engineering.

<figure>
  <img src="../assets/images/crisp-dm-for-ai/crisp-dm-cycle.jpg" alt="CRISP-DM cycle diagram showing six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment">
  <figcaption>The CRISP-DM cycle: six phases that form an iterative process for data-driven projects</figcaption>
  <!-- This diagram illustrates the cyclical nature of AI projects, where each phase informs the others -->
</figure>

### Running Example: Online Classifieds with AI

To illustrate how CRISP-DM applies to AI, we use the same example as before: an online classifieds platform. In machine learning, we would have a classification problem. In the AI case, we upload an image and from this image we want to reliably extract the information we need.

### Business Understanding

We don't just solve problems for the sake of solving problems. Not "hey, we have AI, how about we use it" and then start thinking of different use cases. No - it should come from a real user problem. Maybe we already know about this problem. We already tried to solve it differently, but now we think we want to try to solve it with AI.

We need to have this business understanding. What is the problem? Why do we want to do this? Not just because we want a cool new feature, but because there is a real problem that users have with our product that we will solve. This is usual work that product managers do, user experience researchers do. There should be a real problem or a hypothesis that this problem exists and we want to verify this hypothesis.

We need to understand: how many people does this affect? At this point, we think more about the problem, not the solution. How can we measure it? What could be the metric for solving this problem?

For the classifieds example: users complain that it takes so much time to fill the form. There is some existing user research that confirms this. Otherwise we need to conduct this research to find out this is actually a problem worth solving. Maybe users don't really complain about this. If we solve a problem that doesn't exist, nobody will care and we waste money and time.

Then our goal becomes clear. Right now it takes five minutes to fill the form, and we think we can reduce this time to one minute. We can also have secondary metrics - like users who started filling the form and didn't finish because it was too complex. Right now that is 15%, but we want to drop it to 5%. The important part is we need to have this research, we need to understand there is a problem, and we need to understand this is a way to solve it.

For integrating AI into products, this is very important. We don't want to spend time on solving a problem that doesn't exist.

The AI engineer's role here is to work with product managers to understand: do we actually need AI here, or is there something simpler we can do? Previously for machine learning, building a model was more expensive and took more time. Sometimes you could solve the problem by using rules. In case of AI, testing a hypothesis is cheaper in terms of time, but we still need to understand if it is worth solving with AI or if we can use something else.

### Data Understanding

At this point, we want to understand if there is data we can rely on to build our model. In case of machine learning, we need to determine if we have training data. In case of AI, we need to understand what data we have available.

We need to send something to AI. Do we have everything we need for that? We want to understand how difficult it would be to integrate what we need. In our example, when we send data to AI, we need to make sure the front end can send all the data we need. That is one thing.

But let's say we are talking about integrating AI into something else - it could be something not user-facing, running on the backend. You can use AI to optimize some processes. There it is very important that you have some data for AI to act on, because it needs to get in some data.

In our case, the input will be a picture. Of course, in our case it is easy - we already have the picture.

For RAG cases, we also need to think about data understanding and data preparation. Do we have all the data we need? Do we have the integrations we need? Some services are not easy to integrate to or access. This is something we also need to keep in mind.

<!-- TODO: Brainstorm what other projects would look like for data understanding and data preparation steps -->

### Data Preparation

In case of machine learning, we just need to fetch the data from different sources. We need to prepare it in the right format. For this particular case, it is less important. But if we want to use AI for recommendations or search or things like that, of course we need to have data available.

In some cases, where we want to integrate into products like search and recommendation, we need to be able to access this data.

We are talking about data preparation steps. We need to prepare data in such a way that we can put this into the model. In our case, it is an image, it is text. This is fairly simple. We just fetch whatever image was sent to us from the front end. We send it to OpenAI, we process, we get data, and we send it back. There is not much data pre-processing.

For agents that need to access things, we need to think about whether we have all the data we need and whether we have the integrations we need. Some services are not easy to integrate to or access.

### Modeling

There is not much of a traditional modeling step, but I would change it a little.

In case of ML, here we do the actual training. We train the actual model. We also evaluate the model - cross validation, all sorts of things. In the AI case: we have the prompt, we have our output class (the Pydantic model), we have input. Then we set up the validation framework, we set up the tests for our AI system.

We need to collect evaluation data, we need to evaluate our model. This is a process very similar to what we would do with machine learning, except we don't train the model. We have other criteria, other things we are optimizing. The important thing is that we have a metric - not necessarily a business metric, but more like a technical metric for how many images we are able to extract correctly. Then we change our prompt, we tune our prompt, we do other things.

Important thing in CRISP-DM: the evaluation we do with cross-validation and metrics like accuracy is not the "evaluation" step in CRISP-DM. That belongs to the modeling step.

### Evaluation

At the evaluation step, we actually see how it affects the product and how it affects the users. We take what we developed and we roll it out to users. We run some sort of A/B tests.

We remember at the business understanding step we defined the metric. Here we see if this metric is good. We also collect feedback from people - this implicit feedback. We see how often people change the output, how good it is. But the important thing is if users were able to do this faster than before.

Here we can introduce extra metrics to measure the performance of our model, but the main metric was defined in business understanding. Here we can see if this is good or not.

CRISP-DM is a fairly old model. Before, evaluation and deployment were kind of separate, but now they are almost the same. You deploy to a part of users and then if everything works, you say okay, it is good. We can roll this to everyone.

If during the evaluation we see something is off, we either refine our business understanding, or we can say: with what we have right now, it doesn't seem valuable to continue with this project, so we are parking it for now. This could be an outcome too - saying that we cannot achieve what we wanted. And this is an outcome too. Between the initial idea and this outcome, ideally you want to spend as little time as possible.

This would be the first iteration, but on the second iteration, you would spend more time. The goal is to iterate. This process is very iterative - you iterate as many times as possible.

### Deployment

Deployment remains similar: putting the system into production. The entire process is iterative - we cycle through these steps until performance is satisfactory.

### Who is Involved at Each Step

The roles involved at each CRISP-DM step:

- Business understanding - product managers, AI engineers. AI engineers help PMs understand if it is something AI can solve
- Data understanding - data analysts, product managers, AI engineers, backend engineers. Together with analysts, AI engineers try to understand the data. Could involve people from other teams if you need data from there
- Data preparation - data engineers and AI engineers. If you don't have a data engineer in the team, AI engineer will need to do this
- Modeling - strictly AI engineers
- Evaluation - AI engineers, analysts, product managers. Analysts help set up the A/B test. PMs need to be involved to double-check that we track the right metrics. We need to set up the experiment properly
- Deployment - AI engineers, platform engineers

AI engineers are involved in pretty much every step.

### The Iterative Nature

CRISP-DM emphasizes that projects are iterative. We never truly "finish" - we iterate until we achieve satisfactory results, then continue improving. This iterative approach is essential for AI projects where:
- User behavior may be unpredictable
- Prompts need refinement
- Evaluation metrics may need adjustment

This is a valid framework for AI projects. You don't necessarily have to follow each step, but it gives a good mental model to understand how you can approach not only machine learning projects, but also AI projects.

### Historical Context

The fact that a framework from 1996 remains relevant tells us something important: while the tools change (from training models to API calls), the fundamental process of building data-driven products remains constant.

The processes data scientists have always used - evaluation, versioning, experimentation - are exactly what AI engineers need today. This is why data scientists often make excellent AI engineers with some additional coding practice.

