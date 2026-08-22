---
title: "How CRISP-DM Still Applies to AI Engineering"
date: 2026-03-11
url: https://aishippingblog.com/p/how-crisp-dm-still-applies-to-ai
---

If you come from machine learning or data science backgrounds, there’s a high chance you already know CRISP-DM, a framework developed in the 1990s for structuring data projects and later actively adopted by the DS and ML community.

At first glance, AI engineering can look like a completely different discipline. Today’s teams work with LLM APIs, retrieval pipelines, agents, prompts, evaluation tooling, and production observability. The stack has changed significantly.

But if you step back from the tools, the underlying development process is less new than it seems. Many of the stages of the work still map reasonably well to the CRISP-DM lifecycle.

[![Image 1](https://substackcdn.com/image/fetch/$s_!mszO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc34a135f-bcc3-458a-acdc-e25682da90c7_1924x1252.png)](https://substackcdn.com/image/fetch/$s_!mszO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc34a135f-bcc3-458a-acdc-e25682da90c7_1924x1252.png)

In this post, we use CRISP-DM as a reference point to look at AI engineering work phase by phase. We show where the structure still holds and how it can help when planning or analyzing modern AI systems.

## The Six CRISP-DM Phases, in AI Terms

[![Image 2](https://substackcdn.com/image/fetch/$s_!EB03!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F689a54fc-b683-47a5-8bff-6434c3fa4f72_1280x1282.png)](https://substackcdn.com/image/fetch/$s_!EB03!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F689a54fc-b683-47a5-8bff-6434c3fa4f72_1280x1282.png)

CRISP-DM breaks projects into six phases:

* Business Understanding
* Data Understanding
* Data Preparation
* Modeling
* Evaluation
* Deployment

## Example

To illustrate how CRISP-DM can be applied to AI engineering, let’s take an example of an online classifieds platform where users can sell their items. To create a new listing, they fill out the form with the item’s title, description, category, and price.

[![Create Listing form with AI-prefilled fields after uploading a photo of headphones: title, description, price, and category](https://substackcdn.com/image/fetch/$s_!yWik!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb1a6895-1eda-4850-aa50-f9d3bbdc00aa_844x789.png)](https://substackcdn.com/image/fetch/$s_!yWik!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb1a6895-1eda-4850-aa50-f9d3bbdc00aa_844x789.png)

Instead of asking a user to fill in every field manually, we may want to create an AI feature that automatically suggests fields based on a user-uploaded photo.

With that example in mind, we can walk through the CRISP-DM phases.

[![Image 4](https://substackcdn.com/image/fetch/$s_!JLlT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F571620ca-ec97-4660-99fd-5ae36b46bd47_1924x1496.png)](https://substackcdn.com/image/fetch/$s_!JLlT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F571620ca-ec97-4660-99fd-5ae36b46bd47_1924x1496.png)

## 1. Business Understanding

The first phase focuses on defining the problem and the criteria for success.

In the classifieds example, the problem may be that creating a listing takes too long, causing users to drop off. This can lead to measurable objectives such as reducing listing creation time from 5 minutes to 1 minute and lowering the abandonment rate from 15% to 5%.

At this stage, the AI engineer often helps determine whether an AI system is appropriate or whether a simpler solution could address the problem.

## 2. Data Understanding

Once the objective is defined, the next step is to examine the data that could support the solution.

For the classifieds feature, the team would analyze the image data that users upload when creating listings. Questions at this stage might include:

* How are images stored and accessed?
* What formats and resolutions are common?
* How often do listings include images?
* Are images frequently blurry, rotated, or incomplete?

The team may also explore related data such as existing listing titles, descriptions, and categories. These fields can provide additional context that helps the AI system generate structured outputs.

## 3. Data Preparation

After understanding the available inputs, the team prepares them for use by the system.

For the classifieds feature, this might involve:

* Validating uploaded image formats
* Normalizing image size or orientation
* Preparing category metadata
* Defining the structured output format for generated attributes

In other AI systems, preparation may involve tasks like document chunking, embedding generation, or building retrieval indices for RAG pipelines.

## 4. Modeling

The modeling phase focuses on designing and testing the system that will produce the desired output.

In traditional machine learning projects, this stage usually involves training and tuning models on prepared datasets.

In AI systems built around foundation models, the work often shifts from model training to system design around the model.

For the classifieds example, this may include:

* Designing the prompt that describes the extraction task
* Defining the expected output schema (for example, using a structured format such as a Pydantic model)
* Implementing validation logic for the generated attributes
* Building tests to measure how reliably the system extracts information from images

The team then runs experiments and refines the prompt or configuration based on the results.

## 5. Evaluation

After building the system, the team evaluates whether it solves the problem defined in the first phase.

For the classifieds feature, the team may run an A/B test comparing the current listing workflow with the AI-assisted version.

They would then measure the results against the original goals:

* Did listing creation time decrease?
* Did the abandonment rate drop?

If the system improves those metrics, it may proceed to broader deployment. If not, the team may return to earlier phases and refine the approach.

## 6. Deployment

Once the system meets the evaluation criteria, it can be integrated into the production environment.

For the classifieds example, deployment means connecting the AI system to the listing workflow so that when a user uploads an image, the system automatically generates the listing details.

This stage includes:

* Integrating the AI service with backend systems
* Handling errors and unexpected inputs
* Monitoring system performance over time

After deployment, the team continues to track key product metrics to ensure the feature delivers value.

## The Iterative Nature of the Process

Although CRISP-DM describes deployment as the final phase, the process is inherently iterative.

Once a system is running in production, teams often discover new edge cases, unexpected inputs, or weaknesses in evaluation criteria. These insights frequently lead back to earlier phases like data preparation, modeling, or evaluation.

## Read the Full Article

To explore this in more detail, read the full article.

We go deeper into each phase, walk through the example AI feature step by step, and show what the AI engineer does at each stage and which roles they typically work with along the way.

[Read the full article](https://aishippinglabs.com/blog/crisp-dm-for-ai)
