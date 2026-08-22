---
title: "What AI Forward-Deployed Engineers Do"
date: 2026-07-25
url: https://aishippingblog.com/p/what-ai-forward-deployed-engineers
---

Forward-deployed engineering became a growing part of the AI engineering market in 2026.

Since January 2026 [I scrape AI Engineering jobs](https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main/job-market/data_structured) monthly for [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide/). So far we have 4,894 descriptions, and among them, the number of FDE-related postings increased from 28 in January to 108 in July.

According to this dataset, the AI Engineering job market doubled in these 6 months. But the number of FDE listings grew 4 times! That is, it’s growing at twice the overall AI Engineering market rate.

[![Image 1](https://substackcdn.com/image/fetch/$s_!tGZG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7f03a95-3615-4a28-97d0-80c9e6bfcac5_824x371.png)](https://substackcdn.com/image/fetch/$s_!tGZG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7f03a95-3615-4a28-97d0-80c9e6bfcac5_824x371.png)

Live FDE job postings nearly quadrupled between January and June 2026

In this article, I analyze 113 FDE postings to understand what this work involves. Since our dataset focuses on AI Engineering roles, it’s limited to FDEs working in AI.

We discuss

* how companies define the role
* which skills they expect
* how FDE differs from applied AI engineering, solutions engineering, and consulting

At the end of the article, we also include a quick self-assessment checklist to help you determine whether the FDE role is for you.

## Forward-Deployed Engineer

Palantir created the forward-deployed engineering model in 2006. They had a general platform, but making it useful required adapting it to each customer’s data, workflows, and infrastructure.

To solve it, they placed their engineers in their customer’s teams. FDEs identified their problem, configured Palantir’s platforms, built integrations and custom components. They also supported product development: when the same problem appeared across deployments, Palantir would integrate this as a feature to the main platform.

Palantir’s FDE model applies directly to AI in enterprises today. General-purpose models must be adapted to each customer’s data, systems, and workflows before they can deliver value in production.

There’s a “deployment gap” - the gap between a prototype and a working customer system. It exists because many enterprises don’t have the engineering capacity or product knowledge to close it themselves. FDEs fill that gap.

A forward-deployed engineer is a customer-facing software engineer who turns an ambiguous business problem into a working production system. They work alongside the customer to define the problem, design the solution, adapt and integrate the company’s product, build any missing software, deploy and debug the system, and feed recurring customer needs back into the core product.

## FDE’s responsibilities: our analysis

We collected a dataset of 113 FDE jobs descriptions from January to July, and [then analyzed the expected responsibilities](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/06-fde.md).

They include:

* Direct client engagement (90% of postings)
* Building and deploying production system (87% of postings)
* System, API, and data integration (62% of postings)
* Project scoping, discovery, and requirements gathering (51% of postings)
* System testing, evaluation, and monitoring (41% of postings)
* Channeling customer feedback back into the core product roadmap (39% of postings)
* Developing prototypes, demos, and proofs of concept (25% of postings)
* Travel or client on-site presence (10% of postings)

[![Image 2](https://substackcdn.com/image/fetch/$s_!LxRa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3cf8e481-92d2-4521-8a5f-7aada5234de5_2375x1341.png)](https://substackcdn.com/image/fetch/$s_!LxRa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3cf8e481-92d2-4521-8a5f-7aada5234de5_2375x1341.png)

If we compare it with the rest of the dataset, only 21% of the other AI roles are expected to interact with the clients.

Here’s how we can describe the FDE’s main responsibilities

[![Image 3](https://substackcdn.com/image/fetch/$s_!iXBX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4847ffa8-8bdf-463b-a15b-e458272d6c02_1456x443.png)](https://substackcdn.com/image/fetch/$s_!iXBX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4847ffa8-8bdf-463b-a15b-e458272d6c02_1456x443.png)

### 1) Understand the customer’s problem

FDEs usually begin with a desired business outcome. They work with users, domain experts, and engineering teams to understand the existing workflow, examine the available data, and identify technical constraints. They then translate what they learn into deployment requirements and success criteria.

### 2) Build the production AI application

Once the problem is clear, the FDE writes the software to solve it, handling conventional production engineering tasks like authentication, permissions, testing, error handling, deployment, logging, and observability.

### 3) Connect the application to the customer’s systems

FDEs also work on integration, and this need is present in 62% of job postings. They build connectors, data pipelines, transform data, configure access controls, integrate APIs, and deploy applications in the customer’s cloud.

### 4) Deploy, evaluate, and debug the system

Production deployment expands the FDE’s role beyond implementation. The engineer must define evaluation criteria for realistic conditions and use logs, traces, metrics, and user feedback to identify failures post-release. FDE continue to be involved in the project after deployment.

### 5) Bring field findings back to the product

Some deployment issues are unique to individual customers, while others highlight common needs. FDEs identify these recurring problems and relay customer feedback to the product team, with 39% of postings referencing this contribution. This process connects customer delivery and product development, allowing the FDE to adapt the product for one customer and identify reusable capabilities for others.

## Skills companies ask for

It’s natural that with these responsibilities FDEs are expected to have a broad mix of skills.

[![Image 4](https://substackcdn.com/image/fetch/$s_!b_gT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ca161db-1839-4768-8963-e2b61c9d96ae_1375x796.png)](https://substackcdn.com/image/fetch/$s_!b_gT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ca161db-1839-4768-8963-e2b61c9d96ae_1375x796.png)

### Software engineering

The technology stack varies from job to job, but all of the FDEs are expected to deploy production software.

Python is the most frequently mentioned programming language, appearing in 89% of job postings. Other commonly referenced languages and frameworks include:

* TypeScript: 29%
* SQL: 23%
* React: 14%

### Applied AI

FDEs are expected to build applications with existing models, not train them. The most frequently mentioned gen AI technologies are:

* Prompt engineering: 56%
* RAG: 50%
* LangChain: 32%
* AI agents: 30%
* Vector databases: 23%
* Agentic workflows: 19%

### Cloud and deployment

In the job descriptions, the three major cloud providers appear at similar rates:

* AWS: 40%
* GCP: 36%
* Azure: 32%

Companies also seek candidates with experience in the following areas:

* Docker: 35%
* Kubernetes: 31%
* CI/CD: 27%

### Customer-facing work

The technical requirements represent only part of the role. With 92% of FDE postings identified as customer-facing, engineers must also navigate technical discovery and tackle evolving requirements.

FDEs need to be able to:

* Understand existing business workflows
* Translate user needs into technical requirements
* Communicate constraints and tradeoffs to stakeholders
* Collaborate with domain specialists and customer engineering teams
* Adapt implementations based on new information
* Differentiate customer-specific integration from reusable product gaps

## How the role differs from related titles

FDEs have a broad set of responsibilities, so it’s natural that the role overlaps with many others.

The main difference is the type of code FDEs write, how long they work with one customer, and the involvement in production deployment.

An FDE builds and deploys systems for specific customers, writes production code, and stays involved until the deployment works.

* Consultant: Works within a defined engagement and usually leaves after delivering recommendations or an implementation. FDE: Stays through production deployment, owns more of the outcome, and feeds customer needs back into the product.
* Solutions or sales engineer: Focuses on demos, technical validation, and supporting multiple deals before handing off implementation. FDE: Writes production code, owns deployment, and works more deeply with fewer customers.
* AI engineer: Builds production AI systems, often with more focus on the underlying product or platform. FDE: Places greater emphasis on customer integration, deployment, and close collaboration.

## Who is a good fit

FDEs come from different technical backgrounds:

* AI engineer: Strong in LLM applications, RAG, agents, evaluation, and production AI. Gap: Customer discovery, enterprise integration, and ownership of customer-specific deployments.
* Software or product engineer: Strong in APIs, backend or full-stack development, testing, and shipping software. Gap: Applied AI, evaluation, data pipelines, and customer discovery.
* Data engineer: Strong in pipelines, integrations, distributed systems, cloud platforms, and production operations. Gap: Full-stack development, LLM systems, evaluation, and product discovery.
* ML engineer: Strong in model deployment, monitoring, evaluation, and production ML. Gap: Broader product engineering, customer-specific integrations, and direct customer work.
* Platform, DevOps, or SRE engineer: Strong in infrastructure, CI/CD, security, reliability, observability, and debugging. Gap: Application development, applied AI, customer discovery, and workflow analysis.
* Solutions engineer or technical consultant: Strong in customer discovery, solution design, technical communication, and varied customer environments. Gap: Production software development, long-term ownership, and applied AI evaluation.
* Data scientist: Strong in experimentation, model evaluation, analysis, domain knowledge, and stakeholder communication. Gap: Maintainable application development, systems integration, infrastructure, and deployment.

For our dataset and set of responsibilities, AI engineering is the closest technical background because the tools and systems often overlap. (But our data is probably biased because in our scrapes we focus on AI Engineering roles.)

[![Image 5](https://substackcdn.com/image/fetch/$s_!iveB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b12bfbe-d823-4989-a500-36010b340d8c_1148x938.png)](https://substackcdn.com/image/fetch/$s_!iveB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b12bfbe-d823-4989-a500-36010b340d8c_1148x938.png)

The strongest fit is someone who can combine three capabilities:

* Build and operate production software across application code, data, integrations, and infrastructure.
* Work directly with customers to turn unclear problems into technical requirements and measurable outcomes.
* Remain responsible through deployment, evaluation, and production debugging.

## Is this role for you?

Forward-deployed engineering may suit you if you want to be a hands-on engineer while working closely with customers and owning projects through production.

The role may be less suitable if you prefer narrow technical ownership, stable specifications, limited customer interaction, or handing projects off before production.

Before applying, ask yourself:

* Do I want regular customer interaction to be part of my engineering work?
* Can I make progress when requirements are incomplete or changing?
* Am I comfortable working across several parts of the stack?
* Do I want to own deployment and production results, not only implementation?
* Can I explain technical constraints to non-specialists?
* Am I willing to work within the customer’s existing systems and infrastructure?
* Do I enjoy turning recurring customer problems into reusable product improvements?

## Conclusion

FDE is still an inconsistent job title, but we can see a clear focus on customers and production.

Compared to traditional AI engineering, FDEs place a stronger, more consistent emphasis on customer discovery, systems integration, and deployment responsibilities. For engineers who want that combination, forward-deployed engineering provides a path to remain technical while owning a broader part of the production outcome.

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/).
