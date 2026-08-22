---
title: "Last Call for AI Engineering Buildcamp"
date: 2026-04-07
url: https://aishippingblog.com/p/last-call-for-ai-engineering-buildcamp
---

Next Monday (April 13), I start another iteration of [the AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents), a course that teaches AI engineering by building.

After it concludes, I do not plan to run another cohort in the nearest future. I want to take a break from the course and focus on [AI Shipping Labs](https://aishippinglabs.com/) for a while.

So, if you’ve been thinking about joining, this cohort might be the right time. You can sign up using the SUBSTACK promo code for 20% off for newsletter subscribers.

[Join the course now with 20% off](https://maven.com/alexey-grigorev/from-rag-to-agents)

In this post, I’ll go over the course content, the projects you can work on, and how to join this cohort. I’ll also explain how you can get special discounts or explore financing options for your participation.

## What AI Engineering Buildcamp is

The main idea of AI Engineering Buildcamp is that you learn AI engineering by building one system step by step.

Over the course of the program, you work on several kinds of projects in parallel:

* A running example project that evolves throughout the course
* Optional example projects that show how the same ideas apply to other RAG and agent use cases
* Homework projects that help you practice each week on your own
* Your capstone project, where you apply everything to a use case you choose yourself

This structure gives you both guidance and independence. You follow a concrete example, see multiple variations of the same patterns, practice them in homework, and gradually build your own project into a more complete AI application.

### 1. A Running Example Project

The running example throughout the course is the Documentation Agent. We index the Evidently documentation and build an AI agent on top of it.

[![Image 1](https://substackcdn.com/image/fetch/$s_!1pbF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36fee947-800b-436e-a0c0-d3fb715ff109_1280x853.jpeg)](https://substackcdn.com/image/fetch/$s_!1pbF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36fee947-800b-436e-a0c0-d3fb715ff109_1280x853.jpeg)

This project stays with you through the course and grows as new concepts are introduced:

* Week 1 lays the foundation, covering topics like LLMs, the OpenAI API, RAG, and search. We index the documentation and build our first RAG application to answer questions about it. From the first week, you already have a usable AI system.
* Week 2 helps you catch up on Week 1 materials and introduces a few more examples to strengthen your understanding of RAG.
* Week 3 adds agentic capabilities. We turn the RAG application into an agent capable of exploring the documentation database.
* Week 4 focuses on reliability. We add tests to verify that the agent works as intended. This includes both classical unit tests and LLM-based judges.
* Week 5 focuses on monitoring. You see how the agent behaves in production and collect the information you need to observe and debug it.
* Week 6 adds systematic evaluation. You learn how to evaluate agents with a human in the loop, create judges that mimic human evaluators, and use synthetic data.

By that point, the running example has gone through the same progression you want in a serious AI application: from a simple RAG system, to a tool-using agent, to a system that is tested, observable, and systematically evaluated.

You also get exposure to more advanced agent systems, which I cover in more detail in the next section on Optional Projects.

### 2. Optional Projects

While the main running example is the Documentation Agent, it is not the only system you see during the course.

Along the way, I introduce a range of optional projects that apply the same ideas to different use cases. The goal is to help you see how the underlying patterns change depending on the data, the task, and the product shape.

[![Image 2](https://substackcdn.com/image/fetch/$s_!2_uI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9982ea3f-ac65-4c8e-91af-1a94ebc78a6d_1280x853.jpeg)](https://substackcdn.com/image/fetch/$s_!2_uI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9982ea3f-ac65-4c8e-91af-1a94ebc78a6d_1280x853.jpeg)

You can study, reuse, and adapt them for your own work.

For RAG, the course includes these examples:

* FAQ Assistant: A chatbot for course FAQ data that uses RAG with boosting and filtering.
* YouTube Transcript Summarizer: A system that extracts summaries and chapter structure from YouTube videos using structured output.
* PDF Book Processor: A workflow for parsing a complex PDF, such as a book with mathematical formulas and non-trivial layout. This kind of document processing is especially relevant because similar tasks often appear in take-home assignments and interviews.

For agents, the optional projects become more action-oriented:

* Web Search Agent: An agent that uses web search tools to find, filter, and synthesize information from the internet.
* YouTube Researcher: An agent that searches YouTube, fetches transcripts, and produces structured research summaries.
* Coding Agent: A fully functional coding agent that scaffolds Django applications.
* Code Analysis Agent: An agent for analyzing and understanding codebases.
* Deep Research Agent: A multi-stage research system that starts with broad search, expands into follow-up queries, goes deeper into promising directions, fact-checks findings, and generates a final article.

So while the running example gives you one system that evolves throughout the course, the optional projects show how the same ideas can be applied more broadly.

### 3. Homework Projects

In addition to optional projects, most weeks of the course end with a separate homework mini-project, where you build another system yourself and practice the same ideas in a new setting.

[![Image 3](https://substackcdn.com/image/fetch/$s_!J9JI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1879969-ac70-4af0-97a9-b6ecc90298f9_853x1280.jpeg)](https://substackcdn.com/image/fetch/$s_!J9JI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1879969-ac70-4af0-97a9-b6ecc90298f9_853x1280.jpeg)

* Weeks 1-2: Document processing with AI. You download books, extract PDF text, chunk documents, and build a full RAG pipeline.
* Week 3: Wikipedia Agent. You implement search and page-fetching tools and build an agent using a framework of your choice.
* Week 4: Testing and evaluation through the DuckDB SQL Agent. You build an agent that queries NYC taxi data, write pytest tests, add LLM judges, and track costs.
* Week 5: Trivia Quizmaster Agent. You build an interactive trivia system and instrument it with Logfire.
* Week 6: Systematic evaluation through the Recipe Assistant Evaluation: You design 20+ evaluation scenarios, run batch tests, and detect hallucinations.

### 3. Capstone Project

On top of that, you’ll be working on your capstone project during the course.

[![Image 4](https://substackcdn.com/image/fetch/$s_!Nbna!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5e439ad-f0d1-4c8f-bad6-a7bc64d69f88_1280x853.jpeg)](https://substackcdn.com/image/fetch/$s_!Nbna!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5e439ad-f0d1-4c8f-bad6-a7bc64d69f88_1280x853.jpeg)

As you go through the course, you’ll keep building your project layer by layer, with each week adding something new:

* Weeks 1-2: Define the use case and build the first working version with RAG.
* Week 3: Make it agentic by adding tools. At this stage, your project goes beyond answering questions and becomes a system that can make decisions.
* Week 4: Make it reliable by adding testing.
* Week 5: Monitor it and start collecting logs from user interactions.
* Week 6: Evaluate the project based on the interactions you collected and the user scenarios you generated.
* Weeks 7 and 8: Polish, extend, and deploy the project.
* Week 9: Present the result, get peer feedback, and continue developing it.

I encourage you to work on your capstone from day 1. Based on the first two cohorts, I noticed a recurring problem: some participants took too long to decide what to build, and as a result, not all completed the course capstone.

For the third cohort, I want to address that directly.

I developed a new methodology based on a design thinking format. It provides more guidance during the project-definition stage, where many people tend to get stuck.

If you already have an idea, the framework helps you shape and scope it more clearly. If you do not, I provide prompts and templates so you can start immediately and keep making progress each week.

> If you follow this process closely, you should have a working capstone by the end of Week 6, leaving the final two weeks for refinement, testing, and presentation.

## Weekly Workload

The course lasts about nine weeks. It’s designed for working professionals, but it still requires a meaningful commitment.

Most of the work is asynchronous. Each week features pre-recorded lessons, practical exercises, and homework. Depending on your background and pace, this usually takes 3-10 hours per week.

There is one live session each week, mainly for office hours. This is when you can ask technical questions, discuss architecture decisions, and receive feedback on your projects from me. I record these sessions and share them with everyone, along with a written summary.

This is not a passive course. It is intended for people who want to spend real time building and debugging, rather than just watching explanations and taking notes.

## Ways to Join

The standard price of the course is $1,799.

1. You can use your company’s learning budget to cover the cost of this course. I wrote a [short guide](https://aishippinglabs.com/blog/how-to-join-ai-engineering-buildcamp) with an email template you can use to reach out to your manager, and Maven also has [their own guide](https://maven.com/expense).
2. You can get an additional 20% discount if you join as a team of 2-9 people and 25% if you book 10+ seats.
3. I also provide a number of full and partial scholarships for each new course cohort. For this cohort, the scholarship form is already closed. I selected the winners and emailed them. If you didn’t get an email from me, that means that you weren’t selected, but I still strongly encourage you to keep learning and building. There are many free resources I've shared online; you can [read about them here](https://alexeyondata.substack.com/i/184757855/thank-you-for-your-strong-submissions).
4. If none of the options above work for you, you can use the SUBSTACK promo code to get a 20% discount.

[Enroll now](https://maven.com/alexey-grigorev/from-rag-to-agents)

> If you need a student discount, PPP pricing, or have any questions about the joining options that I described, please contact me at [alexey@datatalks.club](mailto:alexey@datatalks.club), and I’ll help you.

## Join the Course

[![Image 5](https://substackcdn.com/image/fetch/$s_!GXIn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5383bbd3-fcb0-4b42-b1e5-f38ac729a5f1_2070x1022.png)](https://substackcdn.com/image/fetch/$s_!GXIn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5383bbd3-fcb0-4b42-b1e5-f38ac729a5f1_2070x1022.png)

The AI Engineering Buildcamp is designed for hands-on learning. Throughout the course, you’ll develop your own capstone project, complete mini-projects for homework, and engage in optional practical projects. You’ll gain experience working with RAG, agents, testing, observability, evaluation, and deployment.

If you’ve been thinking about joining, registration is open until April 13. After that, I’m pausing the course and shifting my focus to AI Shipping Labs, so I would not count on another cohort happening soon.

[Join the course now](https://maven.com/alexey-grigorev/from-rag-to-agents/)
