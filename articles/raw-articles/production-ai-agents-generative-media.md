---
title: "A Free Course on Production AI Agents for Generative Media Starts Monday"
created: 2026-11-13
updated: 2026-11-13
tags: [courses, generative-media, agents, nebius, datatalksclub, substack]
status: draft
---

# A Free Course on Production Generative Media Starts Monday

<figure>
  <img src="../../assets/images/production-ai-agents-generative-media/course-cover.png" alt="Production AI Agents for Generative Media: a free, open source, project-based course with DataTalks.Club and Nebius. An agent plans, writes and checks image, voice and video assets on serverless GPUs, from 1 to 1,000+ records, with a cost per asset">
</figure>

On Monday we're starting Production AI Agents for Generative Media. It's our new free course that we run at DataTalks.Club together with Nebius. 

In the course we learn how to build a media generation pipeline and we learn to use open-source models and tools for that. Running these models require access to GPUs, which course participants will receive though the Nebius Buider (?) program. 

Generating one image is simple. Doing it for 1,000 records is where the trouble starts. GPU jobs fail halfway, files are large, and you pay for every GPU hour.

You build an agent that plans and checks image, voice, and video assets. Then you run it on GPUs for 1,000+ records. You don't need your own GPU or a cluster. We run the models as Jobs and Endpoints on Nebius Serverless AI.

Here's what's in this post:

- The four modules and the capstone
- The stack and what you should know before joining
- How to apply, how the GPU credits work, and the dates

You can start from these links:

- [Apply for the course](https://courses.datatalks.club/register/production-ai-agents-generative-media/). It's free, but seats in the live cohort are limited
- [Course repository](https://github.com/DataTalksClub/production-ai-agents-for-media-generation) with all the materials under the MIT licence
- [Launch stream](https://luma.com/xey7h50c) on Monday, 16 November, at 17:00 CET
- [DataTalks.Club Slack](https://datatalks.club/slack.html) for questions

## Course structure

A welcome session comes first, then four modules over five weeks, and then the capstone. The pre-course Q&A was on 10 November.

<figure>
  <img src="../../assets/images/production-ai-agents-generative-media/diagram-course-roadmap.png" alt="Course structure: Module 0 Welcome, Module 1 Make it work, Module 2 Make it intelligent, Module 3 Make it scale, Module 4 Make it production-ready, then the capstone">
  <figcaption>A welcome session, four modules, and a capstone.</figcaption>
</figure>

## The system

Across the modules we build a media factory. It takes a record from your data and produces a personalized card or ad. An agent plans the asset and writes the text. GPU models make the image and the voice or video.

Before the result goes out, a check looks at it. If the quality isn't good enough, the factory generates it again. We start with one record, scale to more than 1,000, and track the cost of each asset.

<figure>
  <img src="../../assets/images/production-ai-agents-generative-media/diagram-media-factory.png" alt="The Personalized Media Factory: a brief goes to an agent, GPU models generate image, voice or video, a check sends assets that aren't good enough back to revise and regenerate, and the factory scales from 1 to 1,000+ records with a cost per asset">
  <figcaption>The media factory that we build during the course.</figcaption>
</figure>

## Module 1: Consistent Media Generation on Serverless GPUs

We give the first module two weeks, so people who apply after the start can still catch up.

We compare image, video, and audio models. Size, VRAM, and latency are the main criteria, and quality and licence matter too. The comparison shows why video costs so much more than images. After that, you generate a first asset through an Endpoint or in JupyterLab. Then you run the same generation as a batch Job.

For the homework, you build a GPU worker that reports its generation time and the cost of one asset. You work out when self-hosting beats paying per call to an API. You also write a one-page capstone proposal.

## Module 2: Multi-Agent Media Workflows

Here the agent runs on CPU, and the GPU models are its tools. A generation call can take minutes. So the tool submits a job and polls for the result. If something fails, you can resume without paying for the same GPU work twice.

On top of these tools we add a planner, a generator, and a reviewer. A versioned rubric guides the reviewer, and the agent regenerates an asset instead of accepting the first output.

<figure>
  <img src="../../assets/images/production-ai-agents-generative-media/diagram-agent-gpu-tools.png" alt="A CPU agent with planner, generator and reviewer calls GPU models as typed tools: image, voice, video and speech to text. Those tools run on Serverless AI Endpoints and Jobs, and results go to object storage">
  <figcaption>A CPU agent, with GPU models as tools.</figcaption>
</figure>

For the homework, the agent makes a short coffee ad of about 10 seconds. It writes a plan, produces a keyframe, judges it, and only then generates the video. Every step is traced, so the cost of one video can be split by step.

## Module 3: Batch Media Generation at Scale

A batch of 1,000 records needs workers that can fail without losing finished work. We spread the records over parallel Jobs on spot (preemptible) GPUs and checkpoint each item. To test this, we kill a run on purpose and check that it resumes where it stopped.

We also look at what makes an asset cheaper, from cold start to generation time and the choice of GPU. In the homework you compete on a leaderboard, and the cheapest reliable run at acceptable quality wins.

<figure>
  <img src="../../assets/images/production-ai-agents-generative-media/diagram-batch-scale.png" alt="Records fan out to spot GPU workers with a per-item checkpoint. A preempted worker returns its items to the queue. Each result is written once to object storage, with a cost report. A killed run resumes and skips items that are already done">
  <figcaption>Fan-out on spot GPUs, with per-item checkpoints and a cost report.</figcaption>
</figure>

## Module 4: Evaluation, Observability and Production

Cheap deterministic checks come first, and a multimodal judge comes after them. You calibrate the judge on your own labels. A golden set (a fixed set of reference examples) blocks any change that makes the results worse. From one trace you can see why a record cost this much and took this long. An SLO tells you when to react.

In the capstone brief you also write down how you handle auth, quotas, and abuse. Prompt injection, content safety, and licensing go there too.

There's no homework in this module, because you use all of it in the capstone.

<figure>
  <img src="../../assets/images/production-ai-agents-generative-media/diagram-evals-tracing-slo.png" alt="Module 4: evals at the system, agent and media layers, a trace with cost and time per step, and an SLO with a dashboard and an alert">
  <figcaption>Evals, a trace with cost and time per step, and an SLO.</figcaption>
</figure>

## The capstone

For the capstone you build your own agent with at least two GPU media models. You run it on Nebius Serverless AI and share it publicly. We grade the engineering, not how the images look.

Your project has to include:

- An agent with 2 or more tools
- An async GPU workload
- Assets in object storage
- An eval suite
- Tracing
- An SLO
- A cost report
- Proof that a killed run resumes without redoing finished work

<figure>
  <img src="../../assets/images/production-ai-agents-generative-media/capstone-requirements.png" alt="Capstone requirements: an agent with 2 or more tools, an async GPU workload, assets in object storage, an eval suite, tracing, an SLO, a cost report, and proof that a killed run resumes without redoing finished work">
  <figcaption>What the capstone has to include.</figcaption>
</figure>

You bring your own data as a CSV or JSONL file with an id column. Ideas from the repository include a marketing studio, a podcast producer, video localization, or a storybook generator. The proposal is due in the first module and the brief in the last one.

## The stack

We use Nebius Serverless AI together with Nebius Token Factory as the reference platform. The code is MIT-licensed and works with OpenAI-compatible and S3-compatible services, so you can run it somewhere else.

<figure>
  <img src="../../assets/images/production-ai-agents-generative-media/tech-stack.png" alt="The course stack: Hugging Face Diffusers, image models such as Qwen-Image, FLUX-class and Sana, Wan for video, Kokoro, Chatterbox and Whisper for audio, Nebius Token Factory for the LLM, raw tool calling and MCP for agents, Nebius Serverless AI for GPU compute, and S3-compatible object storage with FastAPI">
  <figcaption>The default stack, with alternatives for each layer.</figcaption>
</figure>

These are the defaults:

- Media runtimes: Hugging Face Diffusers, with ComfyUI for prototyping
- Models: Qwen-Image, FLUX-class, and Sana for images, Wan for video, Kokoro or Chatterbox for speech, and Whisper. Any open-weights equivalent works
- LLM: Nebius Token Factory, or self-hosted vLLM, or any OpenAI-compatible API
- Agents and tools: raw tool calling, then MCP. Pydantic AI and LangGraph are alternatives
- GPU compute: Nebius Serverless AI Jobs and Endpoints, or DevLabs with JupyterLab
- Storage and API: S3-compatible object storage and FastAPI, plus Gradio or Streamlit for a simple UI
- Tracking, tracing, and evals: not announced yet. Langfuse and OpenTelemetry are listed as alternatives

Open-weights models come with their own licences, so check each one before you use it commercially.

## Prerequisites

The level is intermediate to advanced.

The course is for people who run open or custom GPU media models:

- AI and ML engineers adding image, video, or audio generation to real systems
- MLOps and platform engineers who own the batch pipeline and its cost
- Technical founders paying for per-call media APIs who want to know when self-hosting wins

You need Python, Docker basics, HTTP APIs, and the command line. Experience with an LLM or MLOps course helps, but it's not required.

We don't cover diffusion maths or training foundation models. CUDA, Kubernetes, RAG, and LLM fundamentals aren't covered either.

## Applying

The course is free, but seats in the live cohort are limited, so it's application only. More than 1,160 people have applied so far, and we review each application, usually within 2 business days.

By "live cohort" I mean shared deadlines and peer-reviewed homework, not mandatory live classes. Lectures are pre-recorded, and there's a weekly live office hour.

Everyone admitted gets GPU compute through the [Nebius AI Builder Program](https://dev.nebius.com/builders), which is free to join. The credits are $25 at the start and another $50 after Homework 2, as we explained in the [pre-course Q&A](https://www.youtube.com/watch?v=iACtrkiXndw&t=736s). Request them after 16 November, not before.

On non-high-end GPUs the price is roughly $2 to $3 per GPU hour. Usage beyond the credits is billed to your account, so the credits may not cover the whole course.

If you don't apply or aren't approved, all the materials stay public. You'll just need your own GPU access to run the code.

## Dates

All times are CET, and modules run Monday to Sunday.

- Monday, 16 November, 17:00 to 18:00: launch stream
- 16 to 29 November: Module 1 (two weeks), Homework 1, and the capstone proposal
- 30 November to 6 December: Module 2, Homework 2 due on 6 December
- 7 to 13 December: Module 3, Homework 3 (leaderboard) due on 13 December
- 14 to 20 December: Module 4 and the capstone brief
- 15 January 2027: capstone, attempt 1
- 22 January 2027: peer review, attempt 1
- 29 January 2027: capstone, attempt 2
- 5 February 2027: final peer review, attempt 2

We may change the materials and dates.

From Nebius, the team is Mikhail Rozhkov, Marouane Khoukh, and Aleksandr Iziumov. Nebius DevRel creates and teaches the course, with content and expert support from Nebius Academy.

If you have questions, ask in the [DataTalks.Club Slack](https://datatalks.club/slack.html) or bring them to the weekly office hour.
