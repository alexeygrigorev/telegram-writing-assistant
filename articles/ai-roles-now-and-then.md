---
title: "AI Roles Now and Then"
created: 2026-02-08
updated: 2026-02-16
tags: [ai-engineering, roles, career, ml-engineering, data-science]
status: draft
---

# AI Roles Now and Then

This article compares traditional data team roles with the emerging AI engineer role, examining how responsibilities have shifted with the rise of API-based AI.

## The Evolution of Data Roles

I previously wrote an article describing roles in data teams: Product Managers, Data Analysts, Data Scientists, Data Engineers, ML Engineers, and MLOps Engineers[^1]. That article is 5-6 years old now, and things have changed.

We will definitely refer to this article as a reference throughout the discussion of AI engineering roles[^9].

## AI Engineers vs ML Engineers

The task of an ML engineer is to integrate machine learning into the product. The task of AI engineers is to integrate AI into the product. What is the difference?[^5]

Typically, if we talk about LLM providers, the difference is that you already have an LLM, you just call the web service, versus actually having the weights and owning the model. In some cases, yes, we have open source LLMs. There are cases where you need to serve the LLM yourself. Then this becomes your responsibility as AI engineer too. In traditional ML, it is always the responsibility of the ML engineer to actually serve the model[^5].

### LLM Serving

There are many tools for serving LLMs, like vLLM, but the tools are secondary - just knowing that you need to do this matters. LLMs require special hardware. You also need to know how to provision infrastructure for this hardware. Typically this is also on the AI engineer. For an ML engineer, it could be similar - if you need to serve a neural network model, the difference is that LLMs require a lot more power, bigger GPUs. This is the main difference with ML engineers[^6].

## AI Engineers vs Data Scientists

Data scientists focus on training models, experimenting with models, conducting experiments, translating requirements from product to machine learning terms. They work on creating data and so on[^7].

When it comes to AI (using LLMs), the model is already there. People from OpenAI trained the model, so they went through the process. We don't need this. In cases when we do something simple, when we don't need to fine-tune, when we don't need to do anything else - we don't really need data scientists. It depends on the size of the organization, but if we talk about a small AI team, we don't really need data scientists here[^7].

## Bigger Organizations: Traditional ML + AI

In bigger organizations where we have also classical machine learning, the setup is: data scientists work on a model, on translating requirements into machine learning terms, and ML engineers work together with data scientists to productionize it. The engineer focuses more on serving the model, CI/CD, tests, best engineering practices, infrastructure. Data scientists focus more on modeling, testing, experimenting[^8].

Now let's say there is already a team that has been doing machine learning for quite some time, but now they have an AI use case. In this setup, both data scientists and ML engineers would work on it. Data scientists would focus more on interacting with the model, understanding how to call it, how to tune the prompt, how to set up the validation framework - how to make sure that the model, the agent is behaving the way it should behave. The ML engineer would focus more on the engineering aspects. This would be the setup in teams where there is not necessarily an AI engineer yet. They would split the responsibilities of AI engineer into both roles. And frankly, if we talk about a bigger project, bigger company, they will both have so much work[^8].

The company might decide to hire an AI engineer who will work together with data scientists on these things. But the data scientists will also have responsibilities of taking care of traditional machine learning, maybe some legacy systems, but also some systems that they need now - because LLM is not the answer to all the questions. AI now is very good at solving a subset of some problems, but there are so many problems that don't need LLMs. We still need data scientists, we still need machine learning engineers. They still need to work on what they have been working on. But some problems are of course simpler now - NLP is simpler, many things are simpler now with LLMs[^10].

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

The path from ML Engineer or Data Scientist to AI Engineer is straightforward because the foundational knowledge already exists[^2].

## Other Data Team Roles

The roles of data analysts, data scientists, and data engineers are described in the original article. We will refer to this article when going through the event[^9].

## Teams Without "AI" in the Name

Many companies don't have dedicated AI engineer roles. Instead, existing team members take on AI responsibilities:

- Data Scientists focus on designing experiments and evaluation
- ML Engineers focus more on monitoring and deployment

The job titles may be old, but the tasks are new. Instead of training models from scratch, they use OpenAI or similar APIs. Everything else remains the same[^3].

In teams where we don't have AI engineers, the responsibilities would be split between data scientists and ML engineers[^11].

## Career Paths

For Data Scientists and ML Engineers, the transition to AI Engineer is natural:
- The base skills are already there
- The focus shifts from model training to prompt engineering
- Evaluation and experimentation remain core competencies

What we teach in AI Engineering Buildcamp covers exactly what's needed for this transition[^4].

## Sources

[^1]: [Data Team Roles Explained](https://datatalks.club/blog/data-roles.html) - Original article on data team roles
[^2]: [20260208_114623_AlexeyDTC_msg1188_transcript.txt](../inbox/used/20260208_114623_AlexeyDTC_msg1188_transcript.txt)
[^3]: [20260208_114707_AlexeyDTC_msg1190_transcript.txt](../inbox/used/20260208_114707_AlexeyDTC_msg1190_transcript.txt)
[^4]: [20260208_115417_AlexeyDTC_msg1200_transcript.txt](../inbox/used/20260208_115417_AlexeyDTC_msg1200_transcript.txt)
[^5]: [20260216_132515_AlexeyDTC_msg1745_transcript.txt](../inbox/used/20260216_132515_AlexeyDTC_msg1745_transcript.txt)
[^6]: [20260216_132630_AlexeyDTC_msg1747_transcript.txt](../inbox/used/20260216_132630_AlexeyDTC_msg1747_transcript.txt)
[^7]: [20260216_132750_AlexeyDTC_msg1749_transcript.txt](../inbox/used/20260216_132750_AlexeyDTC_msg1749_transcript.txt)
[^8]: [20260216_132934_AlexeyDTC_msg1751_transcript.txt](../inbox/used/20260216_132934_AlexeyDTC_msg1751_transcript.txt)
[^9]: [20260216_133101_AlexeyDTC_msg1755_transcript.txt](../inbox/used/20260216_133101_AlexeyDTC_msg1755_transcript.txt)
[^10]: [20260216_133028_AlexeyDTC_msg1753_transcript.txt](../inbox/used/20260216_133028_AlexeyDTC_msg1753_transcript.txt)
[^11]: [20260216_135139_AlexeyDTC_msg1773_transcript.txt](../inbox/used/20260216_135139_AlexeyDTC_msg1773_transcript.txt)
