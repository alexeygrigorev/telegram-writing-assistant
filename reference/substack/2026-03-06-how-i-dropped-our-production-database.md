---
title: "How I Dropped Our Production Database and Now Pay 10% More for AWS"
date: 2026-03-06
url: https://aishippingblog.com/p/how-i-dropped-our-production-database
---

I’m working on expanding the [AI Shipping Labs website](https://aishippinglabs.com/) and wanted to migrate its current version from static GitHub Pages to AWS. And later, replace the original Next.js setup with a Django version.

My gradual plan was:

1. Move the current static site from GitHub Pages to AWS S3
2. Move DNS to AWS so the domain is fully managed there
3. Deploy the new Django version on a subdomain
4. When everything works, switch the main domain to Django

This way, everything would already be inside AWS, and the final switch would be seamless.

The migration strategy itself was reasonable, but the problems came from how I executed it.

I was overly reliant on my Claude Code agent, which accidentally wiped all production infrastructure for the [DataTalks.Club course management platform](https://courses.datatalks.club/) that stored data for 2.5 years of all submissions: homework, projects, leaderboard entries, for every course run through the platform.

To make matters worse, all automated snapshots were deleted too. I had to upgrade to AWS Business Support, which costs me an extra 10% for quicker assistance. Thankfully, they helped me restore the database, and the full recovery took about 24 hours.

In this post, I’ll share how I let this happen and the steps I’ve taken to prevent it from happening again.

[![Image 1](https://substackcdn.com/image/fetch/$s_!5utR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F334309b4-8eed-4116-ac1f-96bba42f9fa5_1532x841.png)](https://substackcdn.com/image/fetch/$s_!5utR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F334309b4-8eed-4116-ac1f-96bba42f9fa5_1532x841.png)

Course management platform with no data: no courses, no questions, no answers, no login providers

## Incident Timeline

Thu, Feb 26

* ~10:00 PM: Started deploying website changes using Terraform, but I forgot to use the state file, as it was on my old computer.
* ~11:00 PM: A Terraform auto-approve command inadvertently wiped out all production infrastructure, including the Amazon Relational Database Service (RDS). I later discovered that all snapshots were also deleted, prompting me to create an AWS support ticket.

Fri, Feb 27

* ~12:00 AM: Upgraded to AWS Business support for faster response times.
* ~12:30 AM: AWS support confirmed that a snapshot exists on their side.
* ~1:00-2:00 AM: Had a phone call with AWS support, which was escalated to their internal team for restoration.
* During the day: Implemented preventive measures, including setting up a backup Lambda function, enabling deletion protection, creating S3 backups, and moving the Terraform state to S3.
* ~10:00 PM: The database was fully restored, containing 1,943,200 rows in the `courses_answer` table alone. The platform was brought back online.

[Share](https://aishippingblog.com/p/how-i-dropped-our-production-database?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## How the Disaster Happened

### Reusing an Existing Terraform Setup

I already had Terraform managing production infrastructure for another project – a [course management platform for DataTalks.Club Zoomcamps](https://courses.datatalks.club/). Instead of creating a separate setup for AI Shipping Labs, I added it to the existing one to save a small amount of money.

Claude was trying to talk me out of it, saying I should keep it separate, but I wanted to save a bit because I have this setup where everything is inside a Virtual Private Cloud (VPC) with all resources in a private network, a bastion for hosting machines.

The savings are not that big, maybe $5-10 per month, but I thought, why do I need another VPC, and told it to do everything there. That increased complexity and risk because changes to this site were now mixed with those to other infrastructure.

### First Warning Sign

Instead of going through the plan manually, I let Claude Code run `terraform plan` and then `terraform apply`. My first clue that something was off was when I saw a long list of resources being created. That made no sense: the infrastructure already existed. We weren’t building a new environment.

I stopped Claude and asked, “Why are we creating so many resources?” The agent’s answer was simple and terrifying at the same time: Terraform believed nothing existed.

But why? I had recently moved to a new computer and hadn’t migrated Terraform. When I ran `terraform plan`, it assumed no existing infrastructure was present, and we were starting from scratch.

I quickly cancelled the `terraform apply`, but some resources had already been created.

### Analyzing and Deleting Duplicate Resources through AWS CLI

The next step was to assess what had been created. I instructed Claude to analyze the environment using AWS CLI and identify which resources were newly created and which were part of production. I wanted to delete only the newly created duplicates, leaving the existing infrastructure untouched.

The assistant reported that it had identified the duplicate resources using the AWS CLI and was deleting them. That sounded correct.

While this cleanup was happening, I went to my old computer, archived the Terraform folder, including the state file, and transferred it to the new machine. I thought the cleanup was also done, and I pointed out the Terraform archive to the agent so it could use it to compare newly created resources with archived ones.

### Deleting with terraform destroy

The agent kept deleting files, and at some point, it output: “I cannot do it. I will do a `terraform destroy`. Since the resources were created through Terraform, destroying them through Terraform would be cleaner and simpler than through AWS CLI.”

That looked logical: if Terraform created the resources, Terraform should remove them. So I didn’t stop the agent from running `terraform destroy`. The destroy command completed. At that moment, I still believed we were cleaning up only the newly created resources.

Then I checked the course management platform for DataTalks.Club Zoomcamps, and it was down. I thought, “What is this?” and opened the AWS console to investigate.

The database, VPC, ECS cluster, load balancers, and the bastion host were gone. The entire production infrastructure had been destroyed.

[![Terminal showing the full list of destroyed infrastructure including VPC, RDS, ECS, load balancers, and bastion host](https://substackcdn.com/image/fetch/$s_!ropw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc7921dd-b81d-453a-b832-7c8670a9fbeb_1600x880.jpeg)](https://substackcdn.com/image/fetch/$s_!ropw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc7921dd-b81d-453a-b832-7c8670a9fbeb_1600x880.jpeg)

The full list of destroyed production infrastructure - VPC, RDS, ECS cluster, load balancers, bastion host

When I asked Claude where the database was, the answer was straightforward: it had been deleted.

### What Actually Happened

What happened was that I didn’t notice Claude unpacking my Terraform archive. It replaced my current state file with an older one that had all the info about the DataTalks.Club course management platform.

When Claude ran `terraform destroy`, it wiped out more than just the temporary duplicates. It actually destroyed the real infrastructure behind the course platform instead of the state file it created.

## Finding a Solution

### 1. Searching for Backups

After realizing that production infrastructure was gone, I turned to looking for backups. There should have been daily backups.

It was around 11 PM, and I knew that a snapshot was created every night at 2 AM. I went to the RDS console and checked for available snapshots, but none were visible. I checked the console again, but still saw nothing.

[![Image 3](https://substackcdn.com/image/fetch/$s_!6KGh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4a8d1c5-03a6-456a-9005-9ca51814fefa_1589x1200.png)](https://substackcdn.com/image/fetch/$s_!6KGh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4a8d1c5-03a6-456a-9005-9ca51814fefa_1589x1200.png)

RDS events on Thursday. The backup was created at 00:24 and was visible in the AWS console in the events section, but the backup itself was gone.

Next, I opened the RDS Events section and saw that a backup had indeed been created at 2 AM, as expected. The event was listed, but when I clicked on it, nothing opened, and the snapshot was inaccessible.

At that point, I was uncertain whether the backup had been deleted or was simply not visible.

### 2. Contacting AWS Support

Around midnight, I opened a support ticket about a deleted database and missing backups. I reached out to my AWS contact, but didn’t expect a response so late.

After not hearing back, I noticed that Business support offers a one-hour response time for production incidents, so I upgraded, which added about 10% to my cloud costs.

I then created another ticket with all the necessary details. Support got back to me in about 40 minutes.

### 3. What AWS Support Found

AWS support confirmed that my database and all snapshots were deleted, which I didn’t see coming. The API request clearly told AWS to delete everything.

[![AWS support response confirming the cluster deletion and finding an available snapshot](https://substackcdn.com/image/fetch/$s_!8kBy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a9d3dfe-d2fb-44c6-9198-0b3a4c3866e6_1254x575.jpeg)](https://substackcdn.com/image/fetch/$s_!8kBy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a9d3dfe-d2fb-44c6-9198-0b3a4c3866e6_1254x575.jpeg)

First response from AWS support, they confirmed the deletion and found a snapshot that was not visible in my console

They found a snapshot on their end that I couldn’t see in my console. After I pointed that out, they suggested hopping on a call.

### 3. Call with AWS

We joined a call and reviewed the situation together.

They tried recovery steps on their side. After some time, the support engineer said he needed to escalate internally. We stayed on the phone while they investigated.

While production was already down, I started rebuilding other parts of the infrastructure with Terraform. That went relatively quickly. I also used the opportunity to simplify some things, such as consolidating multiple load balancers into one.

I created a new empty database instance to prepare for a possible restore.

The call lasted around 40 to 60 minutes. Eventually, they said they needed more time and would follow up once they had clarity.

### 4. 24 Hours Later

Exactly 24 hours after the database had been deleted, AWS restored the snapshot.

I received an email confirming that the snapshot restoration was complete and ready for use:

[![AWS support email confirming snapshot restoration is complete](https://substackcdn.com/image/fetch/$s_!L6Zx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc876176d-91a9-4005-a2e7-41bf2033901f_1202x596.jpeg)](https://substackcdn.com/image/fetch/$s_!L6Zx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc876176d-91a9-4005-a2e7-41bf2033901f_1202x596.jpeg)

The email from AWS support confirming the snapshot was restored and available

The snapshot that had been invisible before now appeared in the console.

[![Image 6](https://substackcdn.com/image/fetch/$s_!icYs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F968294be-196c-405d-88bd-d4430db95585_1600x1013.png)](https://substackcdn.com/image/fetch/$s_!icYs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F968294be-196c-405d-88bd-d4430db95585_1600x1013.png)

Restored snapshot

### 5. Restoring the Database

I recreated the database from the restored snapshot via Terraform.

At this point, I changed how I work with Terraform through Claude Code. All permissions are disabled. No automatic execution. No file writes.

The process now is simple:

1. Generate a plan
2. Review it manually
3. Run commands myself

After restoring the database, I checked the data. The `courses_answer` table contained 1,943,200 rows:

[![Terminal showing PostgreSQL query with 1,943,200 rows restored in courses_answer table](https://substackcdn.com/image/fetch/$s_!RiGc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F526712b2-a8d5-489b-b5a8-953e9baa4812_1527x744.jpeg)](https://substackcdn.com/image/fetch/$s_!RiGc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F526712b2-a8d5-489b-b5a8-953e9baa4812_1527x744.jpeg)

Data is back: 1,943,200 rows in the `courses_answer table`

The course management platform came back online. All homework assignments were visible.

[![Data Engineering Zoomcamp 2026 course dashboard showing all homework assignments](https://substackcdn.com/image/fetch/$s_!mYGm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1d38474-b4fa-4fb7-9429-2e93e2a662f5_1420x1144.jpeg)](https://substackcdn.com/image/fetch/$s_!mYGm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1d38474-b4fa-4fb7-9429-2e93e2a662f5_1420x1144.jpeg)

The final step was to configure backups on the new database instance and carefully delete the temporary empty database created during the incident, making sure not to confuse the two.

## What I Did to Prevent This in the Future

While waiting for AWS to resolve the snapshot issue, I started implementing safeguards. I did not want a single `destroy` command to ever wipe everything again.

Here is what I changed.

### 1. Backups Outside of Terraform State

I created backups that are not managed by Terraform.

I did not expect snapshots to disappear together with the database. To avoid that risk, I made sure there are backups independent of the Terraform lifecycle.

I also added S3-based backups. These are stored separately from the database and not tied to infrastructure state.

### 2. Daily Restore Test with Lambda and Step Functions

I built an automated backup workflow.

Every night at 2 AM, AWS creates the regular automated backup. At around 3 AM, a Lambda function wakes up and creates a new database instance from that automated backup. This gives me a fresh copy of production every day. It takes about 20 to 30 minutes.

Once the database is created, another Lambda function runs, orchestrated through Step Functions. It verifies that the database is actually usable by running a simple read query like `SELECT COUNT(*) FROM email`. After the check passes, the database is stopped, not deleted. That way I only pay for storage, not compute.

After that, yesterday’s restored database is deleted. At any time, one recently restored replica is available.

I did this for two reasons:

1. I want to continuously test that backups can actually be restored
2. If production goes down, I can redirect traffic to a ready-to-start replica

I may not always use it that way, but I want that option.

### 3. Terraform and AWS Deletion Protection

I enabled deletion protection at two levels:

1. In Terraform configuration
2. In AWS itself

Both provide safeguards against accidental deletion.

[![Claude Code explaining deletion_protection vs prevent_destroy and running terraform plan with permission prompt](https://substackcdn.com/image/fetch/$s_!vnUR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff339c6cf-8bf3-4348-93a2-322c4f8493fd_1600x761.jpeg)](https://substackcdn.com/image/fetch/$s_!vnUR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff339c6cf-8bf3-4348-93a2-322c4f8493fd_1600x761.jpeg)

Setting up deletion protection. Now every Terraform action requires explicit approval

Technically, these protections can still be removed via CLI if someone explicitly disables them. But they add friction and prevent accidental, destructive actions.

### 4. S3 Backup Protection

For S3 backups, I enabled versioning. If something is deleted, previous versions remain available. Deleting a bucket also requires first deleting its contents, which adds another barrier.

[![Image 10](https://substackcdn.com/image/fetch/$s_!0_Ec!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aac34e1-b44b-4086-858a-3b6d7fe13deb_1575x691.png)](https://substackcdn.com/image/fetch/$s_!0_Ec!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aac34e1-b44b-4086-858a-3b6d7fe13deb_1575x691.png)

### 5. Moving Terraform State to S3

Most importantly, I moved Terraform state to S3.

State is no longer stored locally on a single machine. Terraform now has a consistent and shared view of infrastructure. That removes the original condition when I assumed the state was already remote when it was actually local on my old machine, which allowed duplicate resources to be created.

With state stored in S3:

* It is not tied to one laptop
* It cannot silently disappear when switching machines
* Terraform always has a consistent view of infrastructure

## Lessons Learned

This incident was my fault:

* I over-relied on the AI agent to run Terraform commands. I treated `plan`, `apply`, and `destroy` as something that could be delegated. That removed the last safety layer.
* I also over-relied on backups that I assumed existed. Automated backups were deleted together with the database. I had not fully tested the restore path end-to-end.
* The database was too easy to delete. There were not enough protections to slow down destructive actions.

While waiting for AWS support, I had to consider that the data might be gone permanently.

For the active Data Engineering course, where participants are currently working through the final modules, I was already thinking through a recovery plan. For older courses, it would have been a permanent loss.

Fortunately, AWS support found a snapshot and restored everything.

### What Changes Now

The safeguards I implemented are staying.

For Terraform:

* Agents no longer execute commands
* Every plan is reviewed manually
* Every destructive action is run by me

For AI Shipping Labs, I am considering using a separate AWS account for development and production for proper isolation before anything launches.

## What I’ve Been Working On Recently

### 1) AI Engineering Buildcamp

I finished recording the DIY Monitoring Platform section for the monitoring module at the [AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents).

In the previous cohort, the module focused mainly on building our own monitoring platform, with Pydantic LogFire as more of an afterthought. For this cohort, I shifted the focus to Pydantic LogFire because it’s easy to integrate, with the only real challenge being data extraction. I made sure to explain how to work around that. The DIY Monitoring Platform is still included as an optional deep-dive section.

I also incorporated feedback from the previous cohort and adjusted the material accordingly. The recordings for this section are now finished.

I still need to complete a couple of remaining sections of the AI Engineering Buildcamp later this week.

### 2) AI Engineering Newsletter Series

This week, we published a new post as part of our [Wednesday AI Engineering Newsletter series](https://alexeyondata.substack.com/t/ai-engineering), where we analyzed 1,000+ AI Engineer job descriptions from major tech hubs around the world to understand how companies actually define the role today.

We shared what consistently appears across these postings: the different subtypes of the AI Engineer role, the responsibilities companies expect, the skills and tools that appear most often, and the practical use cases teams are hiring for.

[What 1,000+ Job Descriptions Reveal About the AI Engineer Role in 2026](https://alexeyondata.substack.com/p/what-1000-job-descriptions-reveal)

### 3) AI Engineer Live Research Series

On Tuesday, I hosted the third live session of my [event series](https://alexeyondata.substack.com/p/what-is-an-ai-engineer-in-2026-join) called “[AI Engineering: The Interview Process](https://maven.com/p/69550a/ai-engineering-the-interview-process).”

I shared insights based on a large dataset of real interview materials. We discussed what companies actually expect from AI Engineering candidates, the types of technical and conceptual questions that appear in interviews, and examples of live coding challenges.

To prepare for this session, I reviewed 700+ sources: reports, Twitter and Reddit discussions, and YouTube interviews. From these, I extracted a large collection of interview questions and then curated the most relevant ones. A significant part of the work involved filtering, validating, and categorizing this material.

The research is also published and continuously updated in the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main/role) on GitHub. Star it and share it on social media if you find it helpful. You can use this template:

> Found this AI Engineering Field Guide repo from Alexey Grigorev based on real data (1,765 job descriptions + interview experiences).
>
> Great if you’re prepping for AI Eng roles:
>
> - role + skills breakdown
>
> - interview questions + take-home assignments
>
> - learning paths + project ideas
>
> https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main

The final event in the series, “[AI Engineering Take-Home Assignments](https://maven.com/p/250595/ai-engineering-take-home-assignments),” will be live on Zoom next Monday. In this session, we will analyze what companies actually ask candidates to build at home and identify the patterns behind these assignments. [Register in advance](https://maven.com/p/250595/ai-engineering-take-home-assignments) to receive the Zoom link.

### 4) In-Person Workshop

[![Image 11](https://substackcdn.com/image/fetch/$s_!Z7_G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F31785cfa-b9a5-4f35-b8c8-120d14b07599_1600x900.png)](https://substackcdn.com/image/fetch/$s_!Z7_G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F31785cfa-b9a5-4f35-b8c8-120d14b07599_1600x900.png)

Next Tuesday, March 10, I’ll host a [hands-on data engineering workshop](https://www.meetup.com/en-au/berlin-datatalks-club/events/313061198/?eventOrigin=group_upcoming_events) at Exasol Xperience 2026 in Berlin.

In this session, we’ll build a complete data pipeline using UK NHS prescription data with more than 1 billion records, moving from raw ingestion to an analytics-ready system. We’ll ingest the dataset, set up a staging environment, build a warehouse using Exasol Personal on AWS, orchestrate the pipeline with Kestra, and explore the results through a Grafana dashboard.

If you’re in Berlin, feel free to join. Members of the DataTalks.Club community can [attend the conference for free](https://www.exasol.com/events/exasol-xperience/registration/) using the code EXA-VIP-RDTC, but the [workshop requires separate registration](https://www.meetup.com/en-au/berlin-datatalks-club/events/313061198/?eventOrigin=group_upcoming_events) because we’ll check the attendee list at the entrance.

The materials were prepared about a month ago, and I’m currently polishing the content and rehearsing the workshop with the Exasol team. We’re also figuring out how to provide database access for attendees who don’t have their own AWS account.

### 5) Apache Flink workshop

On Wednesday, I ran a workshop on Apache Flink for the Data Engineering Zoomcamp to update the streaming module.

The original material was created by [Zach Wilson](https://open.substack.com/users/10367987-zach-wilson?utm_source=mentions), who ran a Flink stream for the course last year. Around 80-90% of the workshop content is based on his material, updated to run with Flink 2.x and modern Python versions (3.12, 3.9, 3.8).

Since Flink is not my primary area of expertise, I relied on Zach’s work, which is very solid. Thanks again, Zach, for the great workshop material!

During the workshop, we first walked through Zach’s original example and then explored another case involving aggregation with watermarks and bolt windows. Updating the material required a fair amount of testing to ensure everything worked correctly. Claude Code helped with the updates, though it required quite a bit of guidance.

## Tools

[![Image 12](https://substackcdn.com/image/fetch/$s_!MGLc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3d5f068-6b6b-4550-8d93-d90baf4e5d7c_1600x900.png)](https://github.com/getnao/nao)

[nao](https://github.com/getnao/nao) is an open-source framework for building and deploying analytics agents

* **[nao](https://github.com/getnao/nao)**: an open-source framework for building and deploying analytics agents that let users query data in natural language while maintaining engineering-grade control and reliability. Data teams define a structured, versioned context using the CLI, integrate with any data stack, unit test performance, and self-host securely with their own LLM keys. Business users get a chat interface with native visualizations, transparent reasoning, and built-in feedback loops, bridging the gap between analytics engineering and decision-making.
* **[Pilot Shell](https://github.com/maxritter/claude-pilot)**: a professional development environment for Claude Code that embeds engineering guardrails directly into the workflow. Instead of adding complex multi-agent scaffolding, it enforces testing, linting, formatting, and type checking on every edit while preserving context across sessions. The result is agentic coding with production standards built in, allowing developers to delegate tasks, step away, and return to verified, convention-compliant code ready to ship.
* **[rtk (Rust Token Killer)](https://github.com/rtk-ai/rtk)**: a high-performance CLI proxy that reduces LLM token consumption by filtering and compressing command outputs before they enter the model context. In typical Claude Code sessions, it cuts token usage by 60 to 90 percent across common operations such as git, tests, file reads, and search commands, significantly lowering cost and improving context efficiency. It is purpose-built for AI-assisted development workflows where large terminal outputs would otherwise overwhelm the token budget.

## Resources

[![Image 13](https://substackcdn.com/image/fetch/$s_!9eoC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0bf898e-171f-4120-8fbe-ab168b6c2e30_1782x854.png)](https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main)

[AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main): a data-driven resource on AI engineering role – skills, tools, interview questions, and learning paths

* **[AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main)**: a data-driven resource on AI engineering role – skills, tools, interview questions, and learning paths, based on real job descriptions and practitioner insights. It analyzes what companies actually expect from AI engineers, covering topics such as role responsibilities, hiring processes, common interview questions, and learning paths for different backgrounds. The project is evolving into a comprehensive reference for anyone preparing for an AI engineering career.

* **[Marketing for Founders](https://github.com/EdoStra/Marketing-for-Founders)**: a curated, practical resource hub designed to help technical founders acquire their first 10, 100, or 1,000 users without a large budget. Instead of high-level growth stories, it offers actionable guides across launch platforms, SEO, including LLM SEO and AEO, cold outreach, content, pricing, conversion optimization, and idea validation. It serves as a structured starting point for building an early-stage go-to-market strategy grounded in execution rather than theory.

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
