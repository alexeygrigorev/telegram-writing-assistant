---
title: "How I Moved Our Apps from AWS to Two Contabo Servers"
subtitle: "What the AWS bill looked like, what the move cost, and what still runs on AWS"
---

On October 21, I asked one of my agents to explain why our sandbox AWS account pays for encryption keys. By the next afternoon, all four of our production web apps ran on two Contabo servers instead of AWS.

We run four web apps on AWS:

- The [DataTalks.Club course management platform](https://courses.datatalks.club/)
- The [AI Shipping Labs](https://aishippinglabs.com/) website
- The DataTalks.Club website
- Relay, a service built on Amazon SES and SQS

All of them used managed databases and load balancers, with the apps in containers or on EC2 hosts.

The move took about two days. I gave the instructions in a chat with my coding agents, and the agents did the work.

In this post, I'll share:

- What the sandbox and main AWS accounts were paying for
- The first plan, which was to trim AWS
- Why I bought two Contabo servers and installed Coolify
- How the cutover went, one app at a time
- What it costs now, and what still runs on AWS

## The sandbox bill

I started with the sandbox account, where I deploy small internal tools. The bill had a line for KMS (Key Management Service), the AWS service for encryption keys, and another for Secrets Manager.

Together they cost about $14.91 for the first three weeks of October. KMS was about $10 of that, and Secrets Manager about $4.90.

The agent found 16 customer-managed keys, at about $1 per month each. Twelve of them didn't belong to any CloudFormation stack.

The keys came from a deployment bug. Every time I redeployed one of my internal tools, its CloudFormation template created a new key and kept the old one. Between July 30 and August 12, that left 12 orphan keys, which together cost about $12 per month.

Secrets Manager charges about $0.40 per secret per month, and the account had about 18 of them. The fee depends on the number of secrets, and API calls add almost nothing.

I asked if I could move the secrets to DynamoDB instead. The agent explained that DynamoDB doesn't replace KMS. You can store encrypted secrets in a DynamoDB table, but you still need a KMS key to encrypt them. So I switched the plan to one KMS key plus a table of encrypted values, without the per-secret fee.

These amounts are small, but I got curious about the main account, where the real money goes.

## The main account

The main account hosts the production apps. Cost Explorer (the AWS billing dashboard) showed about $455.50 for October 1 to 21. The agent projected roughly $650 to $700 for the full month.

Here's where the $455.50 went:

- RDS (managed Postgres): about $160
- Tax: about $73
- Elastic Load Balancing: about $64
- ECS Fargate containers: about $37
- AWS Business Support+: about $32
- EC2-Other: about $27
- Public IPv4 addresses: about $20
- WAF (web application firewall): about $11
- Secrets Manager: about $11
- KMS: about $3

The containers that run the apps cost about $37, and the EC2 hosts added about $7. The rest went to databases, networking, support and tax.

The Business Support+ line comes from the night [I dropped our production database](https://aishippingblog.com/p/how-i-dropped-our-production-database). I upgraded to get faster help from AWS, and the support plan has stayed on the bill since then.

The DataTalks.Club website surprised me the most. Its ECS services were scaled to zero. But its database, load balancer, firewall rules and seven secrets kept billing every day. Most of those secrets had never been read.

The website was scaled down, but nobody tore down the rest of its stack.

Another line was RDS SnapshotExportToS3, at about $19.80. A cron job on my Hetzner server snapshotted the four production databases every day and exported them to S3. That cost about $0.99 per day, or roughly $30 per month.

## The first plan: trim AWS

At first, I wanted to make AWS cheaper.

On the evening of October 21, I gave the agent a backlog in this order:

1. Move all secrets into one shared Secrets Manager setup on the main account
2. Find cheaper databases, possibly Neon, or merge the course platform and AI Shipping Labs into one RDS instance
3. Replace the three load balancers with one nginx server, because there's nothing to balance
4. Find out why the snapshot export costs so much

The load balancers annoyed me the most. Each app had its own Application Load Balancer, but none of them had real load to balance. We paid about $64 in three weeks for traffic that one reverse proxy could route.

In the same message, I asked the agent to look for hosting. I named a budget of about €70 to €80 per month for two machines with 64 GB of RAM each. I wanted to run [Coolify](https://coolify.io/) on them.

Coolify is an open-source, self-hosted platform for deploying apps. It does roughly what Heroku or Vercel do, on your own servers. It runs Docker containers and puts a Traefik reverse proxy in front of them, which handles routing and TLS certificates.

I asked for results by the next morning, China time.

## Buying the servers

I also told the agent not to purchase anything before a thorough analysis. Our Hetzner server costs about €30 per month, and I didn't want to pay much more for the same thing.

The agent first compared Hetzner options. One dedicated AX42 server for about €67 was more than we needed. Two smaller Hetzner cloud servers, a CAX31 and a CAX21, came to about €32.48.

Putting Coolify on the existing Hetzner server was another option. But my agents work on that server, so it isn't a quiet place for production.

I preferred two cheaper servers over one big one. I turned the €70 to €80 budget into a ceiling, and I hoped to spend closer to €30 to €50.

In the end, I picked two Cloud VPS 16 instances from [Contabo](https://contabo.com/), each with 16 cores and 64 GB of RAM. The promo price was about €29.60 each, and the total came to €70.44 per month including VAT.

That's above the range I hoped for, but each server has 64 GB of RAM. Before buying, I asked the agent to check with my other agents that this setup would work. Two of them reviewed the plan, and both said go.

I call this bare metal, but technically these are virtual servers. For me the difference that matters is the billing model. I pay a fixed monthly price for the whole machine, and there are no per-hour charges for databases, balancers or IP addresses.

The agent's plan also listed a few rules:

- Skip Contabo auto-backup and send backups to S3 instead
- Keep Postgres private and connect the two servers over WireGuard
- Keep email on Amazon SES
- Keep my agents on the Hetzner server, where they already run

After that, the agent bought both servers that night and installed Coolify 4.4.7. One server runs as the Coolify primary, and the other is managed from it.

By morning, staging versions of all four apps were running on Contabo, along with three Postgres containers. The agent pulled the images from GitHub Container Registry, while production on AWS still used ECR (Amazon's container registry).

## The cutover

The agent started with Relay and moved the other apps after it.

For Relay, the agent first restored the database into a Postgres container on Contabo. Then the agent pointed the CloudFront origin at the new server and checked that the health endpoint returned 200.

After that, the agent tore down Relay on AWS:

- The RDS instance, with a final snapshot kept
- The EC2 host and its EBS volume
- The listener rules and target group on the load balancer
- The security groups and CloudWatch alarms

The agent estimated the Relay savings at about $60 to $70 per month. That covers the database, the EC2 instance and the storage.

At the same time, the agent finished the shared Secrets Manager work. The agent added 40 secrets to the main account and moved 17 secrets over from the sandbox. On Contabo, though, the apps don't read Secrets Manager at all. Each app gets its secrets as Coolify environment variables.

Early on October 22, I asked for a status report.

It showed how little of the original backlog was done:

- Shared Secrets Manager: done
- Cheaper RDS: not done
- One nginx instead of three load balancers: not done
- Snapshot export: the cron was still running

By then, the agent was moving the apps instead of trimming AWS. There was no point in making the AWS databases cheaper if the apps were about to leave them.

In the same report, the agent noticed that the snapshot export cron still had a line for Relay. Its database no longer existed, so that export would fail every evening. I asked the agent to run one last export and then disable the cron.

Later that day, the agent switched DNS and CloudFront for the course platform, AI Shipping Labs and the website to the Traefik proxy on Contabo. All three came up healthy. The agent then deleted two of the three load balancers.

The third one stays for now, because the Relay dev environment still routes through it.

## The last step: the databases

Four RDS databases are still running on AWS. They belong to the course platform, AI Shipping Labs, the website, and a shared dev database. The production apps don't use them anymore, because they now read from Postgres on Contabo.

Before deleting anything, I asked the agent to take a snapshot of each one. All four snapshots are available now, three for regular instances and one for the Aurora cluster.

The agent has everything ready, but it won't run the command until I say so.

I set that rule after the database incident. Back then, an agent ran `terraform apply` with auto-approve and wiped our production infrastructure. Since then, I keep one hard rule: agents prepare destructive steps, and I approve them.

## The costs now

The new fixed cost is €70.44 per month for both Contabo servers, which is about $77.

I can't state the savings yet. AWS bills with a lag, the agent did most of the teardown in the last day, and the RDS databases are still running. I'll know the real number when the November bill arrives.

Some things will stay on AWS:

- SES for sending email, and the SQS queues that Relay uses for SES webhooks
- An S3 bucket for Coolify database backups
- Route 53 DNS and the CloudFront distribution in front of Relay
- The Relay dev environment, with its host and the last load balancer
- The bastion host for the course platform

I still have a few tasks left:

- I need to move the production deploy workflows from ECR to GitHub Container Registry
- I plan to add monitoring on Contabo, but nothing is installed yet
- I still need to clean up the orphan sandbox keys and stale secrets

## Lessons learned

I was paying AWS mostly for the parts around the apps.

The containers cost less than the databases, the load balancers or even the tax. For four small apps, I was paying for managed infrastructure built for much bigger systems.

I also learned to watch idle stacks. Scaling a service to zero stops the containers, but the database, balancer, IP addresses and secrets keep billing. When I stop using an app, I need to tear down the whole stack or accept the cost on purpose.

Finally, I liked working this way. The agents ran Cost Explorer, bought the servers, installed Coolify, migrated the data and switched DNS. I made the decisions in chat and approved the destructive steps.

I accepted some trade-offs, of course. On AWS, someone else patches the databases and replaces failed hardware. On Contabo, that's my job now, or my agents' job. But for apps of this size, I'm fine with that.

Once the RDS teardown is done and the November bill arrives, I'll write a follow-up with the real numbers. Subscribe if you want to see how it turns out.
