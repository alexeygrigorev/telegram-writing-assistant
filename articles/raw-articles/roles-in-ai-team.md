---
title: "Roles in an AI Team"
created: 2026-09-03
updated: 2026-09-03
tags: [roles, ai-engineer, ml-engineer, data-team, career]
status: draft
---

# Roles in an AI Team

This article is an updated version of [Roles in a Data Team](https://datatalks.club/blog/data-roles.html) [^1]. The original covered the classic data team roles. Since then, the AI engineer role has become common enough to deserve its own section. The rest of the roles are still relevant - most AI teams include all of them.

During the ML Zoomcamp pre-course event, there were many questions about AI, even on a course about ML. People asked about the differences between ML engineer, AI engineer, data engineer, and other roles. This article covers all of them[^2].

This is not a comprehensive list, and most of it comes from the perspective of a data scientist and ML practitioner. The descriptions may simplify some roles because not all complexities are visible from the outside.

## Roles in a Team

A typical AI or data team consists of the following roles:

- Product managers
- Data analysts
- Data scientists
- Data engineers
- Machine learning engineers
- AI engineers
- Site reliability engineers / MLOps engineers

All these people work together to create data and AI products.

To explain the core responsibilities of each role, we use a case scenario: an online classifieds platform where users sell things they do not need. Sellers sometimes struggle to pick the correct category for their items. The team wants to build a service that suggests the best category automatically.

## Product Manager

A product manager is responsible for making sure the team builds the right thing. They are typically less technical than the rest of the team. They focus on the problem itself, not on the implementation.

Product managers speak to the team on behalf of the users. They need to make sure that the product is actually used by the end-users. In many companies, engineers create something that does not solve real problems. The PM prevents that.

The primary skill a PM needs is communication. For data scientists, communication is a soft skill. For a product manager, it is a hard skill - they cannot do their job without it.

PMs also do a lot of planning: understanding the problem, coming up with a solution, and making sure it is implemented on time. When somebody has a problem, they approach the PM. The PM figures out if users actually need this feature, how important it is, and if the team has the capacity to build it.

In our example, someone comes to the PM and says: "We want to build a feature to automatically suggest the category for a listing." The PM needs to answer: "Is this feature important enough to the users? Is it worth solving?"

To answer these questions, PMs ask data analysts for help.

## Data Analyst

Data analysts know how to analyze the data available in the company. They discover insights in the data and explain their findings to others.

Analysts need to know:

- What kind of data the company has
- How to get the data
- How to interpret the results
- How to explain findings to colleagues and management

Data analysts are often responsible for defining metrics and building dashboards - things like company profits, number of listings, or how many contacts buyers made with sellers.

Skills for data analysts:

- SQL - the main tool
- Python or R
- Tableau or similar dashboard tools
- Basics of statistics
- How to run experiments (A/B tests)
- Some machine learning: regression analysis, time series modeling

In our example, the PM turns to the data analyst to quantify the problem. Together they answer: "How many users are affected? How many users do not finish creating their listing because of this? How many listings end up in the wrong category?"

After the analyst runs the analysis and confirms it is a real problem, the team agrees it is worth solving.

Later, after the model is deployed, the data analyst runs an A/B test to see if the service actually helps users.

## Data Scientist

The roles of data scientist and data analyst are similar. In some companies, the same person does both jobs. Data scientists focus more on predicting rather than explaining.

A data analyst fetches the data, looks at it, explains what is going on, and gives recommendations. A data scientist focuses on creating machine learning services. Their question is: "How can we use this data to build a model that predicts something?"

Data scientists incorporate data into the product. Their focus is more on engineering than analysis. They work closely with engineers on integrating data solutions.

Skills for data scientists:

- Machine learning - the main tool for building predictive services
- Python - the primary programming language
- SQL - to fetch training data
- Flask, Docker, and similar - to create simple web services for serving models

In our example, the data scientists develop the model for predicting the category and build a simple web service to host it.

## Data Engineer

Data engineers do the heavy lifting when it comes to data. A lot of work needs to happen before data analysts can go to a database, fetch data, and run their analysis. Data engineers make sure this is possible. Their responsibility is to prepare all the data in a form that is consumable for their colleagues.

Data engineers create "a data lake" - all the data that users generate needs to be captured and saved in a separate database. This way, analysts can run their analysis, and data scientists can use this data for training models.

At larger companies, data engineers also manage data access controls. Some user data is sensitive - people should not have access to personal information unless they have a good reason.

Skills for data engineers:

- AWS or Google Cloud
- Kubernetes and Terraform
- Kafka or similar tools for capturing and processing data
- Databases
- Airflow or similar orchestration tools for building data pipelines

In our example, a data engineer prepares all the required data. They make sure the analyst has data for analysis and the data scientist has data for training - listing titles, descriptions, categories, and so on.

## Machine Learning Engineer

Machine learning engineers take what data scientists build and help them scale it up. They also make sure the service is maintainable and that the team follows engineering best practices. Their focus is more on engineering than on modeling.

Skills for ML engineers:

- AWS or Google Cloud
- Kubernetes and Terraform
- Python and other programming languages
- Flask, Docker, and other tools for creating web services

ML engineers work closely with backend, frontend, and mobile engineers to make sure the data team's services are integrated into the final product.

In our example, ML engineers work with data scientists on productionizing the category suggestion service. They make sure it is stable once rolled out to all users and that it is possible to make changes in the future.

## AI Engineer

AI engineers build applications powered by foundation models - large language models (LLMs), vision models, and other pre-trained models. Instead of training custom models from scratch, they use existing models through APIs and integrate them into products.

The difference from ML engineers: ML engineers focus on training, deploying, and maintaining custom models. AI engineers work with pre-trained models and focus on getting the best results through prompt engineering, context engineering, retrieval-augmented generation (RAG), and agent-based systems.

The difference from data scientists: data scientists build models for specific prediction tasks using the company's data. AI engineers use general-purpose models that already know how to reason about text, images, and code, and apply them to solve business problems.

Skills for AI engineers:

- Python - the primary programming language
- LLM APIs - OpenAI, Anthropic, Google, open-source models
- Prompt and context engineering - structuring inputs to get reliable outputs
- RAG - combining retrieval systems with LLMs for knowledge-grounded answers
- Vector databases and search - for similarity search and retrieval
- Agent frameworks - building systems where LLMs take actions and use tools
- Evaluation - measuring output quality, building test suites for non-deterministic systems

In our example, an AI engineer might take a different approach to the category suggestion problem. Instead of training a custom classification model, they could use an LLM that reads the listing description and suggests the category directly. They might build a RAG system that retrieves similar listings from the database and uses an LLM to match the best category. This approach can be faster to prototype and can handle edge cases that a fixed classifier might miss.

AI engineers and ML engineers often work on the same team. For some problems, a custom model is the right solution - it is faster, cheaper, and more predictable at scale. For other problems, an LLM-based approach works better - especially for tasks involving natural language understanding, content generation, or complex reasoning. The team decides which approach fits each use case.

## DevOps / Site Reliability Engineer

The role of SREs is similar to ML engineers, but the focus is on availability and reliability of services. SREs are not limited to data - their role is more general. They focus on infrastructure: networking, provisioning, and monitoring.

SREs look after the servers where services run and collect operational metrics like CPU usage, requests per second, and process health. They set up alerts and are on call to make sure services run without interruptions.

Skills for SREs:

- Cloud infrastructure tools
- Python
- Unix/Linux
- Networking
- DevOps practices: automation, CI/CD

## MLOps Engineer

An MLOps engineer is a DevOps engineer who also knows the basics of machine learning. Their responsibility is to make sure that the services developed by data scientists, ML engineers, and data engineers are up and running.

MLOps engineers know the lifecycle of a machine learning model: training, serving, monitoring, and retraining. They set up continuous retraining pipelines, CI/CD, model registries, and monitoring for model drift.

Despite knowing ML, MLOps engineers focus on operational support. They follow DevOps practices and make sure the rest of the team follows them too.

## Summary

The roles in an AI team and their responsibilities:

- Product managers - make sure the team builds the right thing, act as a gateway for requests, speak on behalf of users
- Data analysts - analyze data, define metrics, create dashboards, run experiments
- Data scientists - build custom models and incorporate them into the product
- Data engineers - prepare data for analysts and data scientists
- Machine learning engineers - productionize ML services, establish engineering best practices
- AI engineers - build applications powered by foundation models, work with LLM APIs, RAG, and agents
- Site reliability engineers / MLOps engineers - focus on availability, reliability, and operational support

This list is not comprehensive, but it should be a good starting point for understanding how the roles are defined in the industry.

This article is based on the original [Roles in a Data Team](https://datatalks.club/blog/data-roles.html) [^1] published on DataTalks.Club.

## Sources

[^1]: [Roles in a Data Team - DataTalks.Club](https://datatalks.club/blog/data-roles.html)
[^2]: [20260903_062310_AlexeyDTC_msg4904_transcript.txt](../../inbox/used/20260903_062310_AlexeyDTC_msg4904_transcript.txt)
[^3]: [20260903_062330_AlexeyDTC_msg4906_transcript.txt](../../inbox/used/20260903_062330_AlexeyDTC_msg4906_transcript.txt)
[^4]: [20260903_062436_AlexeyDTC_msg4908.md](../../inbox/used/20260903_062436_AlexeyDTC_msg4908.md)
