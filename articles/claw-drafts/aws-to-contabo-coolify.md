---
title: "How I Moved Our Apps from AWS to Two Contabo Servers"
subtitle: "What the AWS bill looked like, what broke after cutover, and how we fix production the same turn"
---

On October 21, I asked one of my agents to explain why our sandbox AWS account pays for encryption keys. By the next afternoon, all four of our production web apps ran on two Contabo servers instead of AWS.

We ran four web apps on AWS:

- The [DataTalks.Club course management platform](https://courses.datatalks.club/)
- The [AI Shipping Labs](https://aishippinglabs.com/) website
- The DataTalks.Club website
- Relay, our service for which we use Amazon SES and SQS

We used managed databases and load balancers for all four apps. We ran the apps in containers or on EC2 hosts.

The move took about two days. I gave the instructions in a chat with my coding agents, and the agents did the work.

In this post, I'll share:

- What the sandbox and main AWS accounts were paying for
- The first plan, which was to trim AWS
- How I compared hosting options before buying two Contabo servers and installing Coolify
- How the cutover went, one app at a time
- The public IPv4 cleanup once the apps left AWS
- Observability on Contabo: metrics, logs, alerts, and the business metrics we're collecting first
- What broke in the first nights after cutover, and how we fixed each problem
- A dated timeline of the incidents in the first week
- The production workflow we run now, from emailed alerts to immediate fixes
- What it costs now, and what still runs on AWS

## The sandbox bill

I started with the sandbox account, where I deploy small internal tools. The bill had a line for KMS (Key Management Service), the AWS service for encryption keys, and another for Secrets Manager.

Together they cost about $14.91 for the first three weeks of October. KMS was about $10 of that, and Secrets Manager about $4.90.

I had the agent investigate the charges. It found 16 customer-managed keys, at about $1 per month each. Twelve of them didn't belong to any CloudFormation stack.

The keys came from a deployment bug. Whenever I redeployed one of my internal tools, I created a new key through its CloudFormation template without removing the old one. Between July 30 and August 12, that left 12 orphan keys, which together cost about $12 per month.

Secrets Manager charges about $0.40 per secret per month, and the account had about 18 of them. The fee depends on the number of secrets, and API calls add almost nothing.

I asked if I could move the secrets to DynamoDB instead. The agent explained that DynamoDB doesn't replace KMS. You can store encrypted secrets in a DynamoDB table, but you still need a KMS key to encrypt them. So I switched the plan to one KMS key plus a table of encrypted values, without the per-secret fee.

These amounts are small, but I got curious about the main account, where the real money goes.

## The main account

We ran the production apps in the main account. Cost Explorer (the AWS billing dashboard) showed about $455.50 for October 1 to 21. I had the agent project the full-month bill at roughly $650 to $700.

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

Public IPv4 alone was about $20 for those three weeks. Almost all of it was the EU public IPv4 in-use charge, about $19.58.

That covered roughly seven or eight addresses across load balancers, a NAT gateway and a bastion. At about $3.60 per IP per month, those addresses added to the bill.

The Business Support+ line comes from the night [I dropped our production database](https://aishippingblog.com/p/how-i-dropped-our-production-database). I upgraded to get faster help from AWS, and the support plan has stayed on the bill since then.

The DataTalks.Club website surprised me the most. Its ECS services were scaled to zero. But its database, load balancer, firewall rules and seven secrets kept billing every day. Most of those secrets had never been read.

Another line was RDS SnapshotExportToS3, at about $19.80. A cron job on my Hetzner server snapshotted the four production databases every day and exported them to S3. That cost about $0.99 per day, or roughly $30 per month.

## The first plan: trim AWS

At first, I wanted to make AWS cheaper.

On the evening of October 21, I gave the agent a backlog in this order:

1. Move all secrets into one shared Secrets Manager setup on the main account
2. Find cheaper databases, possibly Neon, or merge the course platform and AI Shipping Labs into one RDS instance
3. Replace the three load balancers with one nginx server, because there's nothing to balance
4. Find out why the snapshot export costs so much

The load balancers annoyed me the most. We had configured ECS so that each app needed its own Application Load Balancer. Our few small apps had little traffic to distribute across multiple targets.

We also used the ALBs for zero-downtime deploys. Each ALB waited for a new target to become healthy before sending traffic to it and draining the old one.

We paid about $64 in three weeks for the balancers, plus public IPv4 addresses across availability zones. My first idea was to replace the three ALBs with one nginx server.

In the same message, I asked the agent to look for hosting. I named a budget of about €70 to €80 per month for two machines with 64 GB of RAM each. I wanted to run [Coolify](https://coolify.io/) on them.

Coolify is an open-source, self-hosted platform for deploying apps. It does roughly what Heroku or Vercel do, on your own servers. It runs Docker containers and puts a Traefik reverse proxy in front of them, which handles routing and TLS certificates.

I asked for results by the next morning, China time.

## Buying the servers

I also told the agent not to purchase anything before a thorough analysis. Our Hetzner server costs about €30 per month, and I didn't want to pay much more for the same thing.

The agent first compared Hetzner options. One dedicated AX42 server for about €67 was more than we needed. Two smaller Hetzner cloud servers, a CAX31 and a CAX21, came to about €32.48.

Putting Coolify on the existing Hetzner server was another option. But I run my agents on that server, so I wanted production on separate machines.

I preferred two cheaper servers over one big one. I treated €70 to €80 as the maximum and hoped to spend closer to €30 to €50.

In the end, I picked two Cloud VPS 16 instances from [Contabo](https://contabo.com/), each with 16 cores and 64 GB of RAM. The promo price was about €29.60 each, and the total came to €70.44 per month including VAT.

That's above the range I hoped for, but each server has 64 GB of RAM. Before buying, I asked the agent to check with my other agents that this setup would work. Two of them reviewed the plan, and both approved.

I call this bare metal, but technically these are virtual servers. For me the difference that matters is the billing model. I pay a fixed monthly price for the whole machine, and there are no per-hour charges for databases, balancers or IP addresses.

The agent's plan also listed a few rules:

- Skip Contabo auto-backup and send backups to S3 instead
- Keep Postgres private and connect the two servers over WireGuard
- Keep email on Amazon SES
- Keep my agents on the Hetzner server, where they already run

After that review, I had the agent buy both servers that night and install Coolify 4.4.7. We use one server as the Coolify primary and manage the other from it.

By morning, staging versions of all four apps were running on Contabo, along with three Postgres containers. For staging, we pulled the images from GitHub Container Registry. For production on AWS, we still used ECR (Amazon's container registry).

## The cutover

I had the agent migrate Relay first, then move the other apps.

For Relay, the agent first restored the database into a Postgres container on Contabo. Then the agent pointed the CloudFront origin at the new server and checked that the health endpoint returned 200.

After that, the agent tore down Relay on AWS:

- The RDS instance, with a final snapshot kept
- The EC2 host and its EBS volume
- The listener rules and target group on the load balancer
- The security groups and CloudWatch alarms

I had the agent estimate the Relay savings at about $60 to $70 per month. That covers the database, the EC2 instance and the storage.

At the same time, we finished the shared Secrets Manager work. We added 40 secrets to the main account and moved 17 secrets over from the sandbox. On Contabo, though, the apps don't read Secrets Manager at all. We give each app its secrets through Coolify environment variables.

Early on October 22, I asked for a status report.

It showed how little of the original backlog was done:

- Shared Secrets Manager: done
- Cheaper RDS: not done
- One nginx instead of three load balancers: not done
- Snapshot export: the cron was still running

By then, we were moving the apps instead of trimming AWS. There was no point in making the AWS databases cheaper if the apps were about to leave them. We routed traffic to our few small apps through Coolify's Traefik, so we dropped the standalone nginx plan. We still needed to reproduce the ALB's rolling deploy behavior.

In the same report, the agent noticed that the snapshot export cron still had a line for Relay. Its database no longer existed, so that export would fail every evening. I asked the agent to run one last export and then disable the cron.

Later that day, we switched DNS and CloudFront for the course platform, AI Shipping Labs and the website to Coolify's Traefik on Contabo. All three came up healthy. We then deleted the remaining Application Load Balancers from the main account.

## The last step: the databases

After the apps were on Contabo, four RDS databases were still running on AWS. They belonged to the course platform, AI Shipping Labs, the website, and a shared dev database. The production apps no longer used them.

Before deleting anything, I asked the agent to take a snapshot of each one. All four snapshots were kept, three for regular instances and one for the Aurora cluster.

I set that rule after the database incident. Back then, an agent ran `terraform apply` with auto-approve and wiped our production infrastructure. Since then, I keep one hard rule: agents prepare destructive steps, and I approve them.

Once the snapshots were in place and I approved, the agent deleted the RDS instances.

## Public IPv4 after the move

Once the apps lived on Contabo, the main account's public IPv4 addresses had nothing left to serve.

For October 1 to 21, that line was about $20, mostly the EU in-use charge of about $19.58. Roughly seven or eight public IPv4 addresses served the load balancers, a NAT gateway and the course-management bastion. At about $3.60 per IP per month, idle addresses still billed.

The same day as the cutover, I had the agent remove those leftovers:

- The course-management bastion EC2 host
- The website NAT gateway
- The Elastic IP attached to that NAT

AI Shipping Labs' ECS services were scaled to zero. They had been the only services using that NAT from the private network.

After that cleanup, the main account had no Elastic IPs or NAT gateways. There were also no public network interfaces, Application Load Balancers or RDS instances.

The sandbox account still has a few associated Elastic IPs for live and dev tools. Those stay for now.

## Observability on Contabo

Moving off managed AWS also meant replacing CloudWatch. I asked for a small monitoring stack that we could run ourselves.

We installed VictoriaMetrics and VictoriaLogs on Contabo. We configured Vector to ship logs and metrics into them. I use vmui for day-to-day checks. The setup, including Docker fault-injection tests for the alerts, lives in the public repo [alexeygrigorev/coolify-observability](https://github.com/alexeygrigorev/coolify-observability).

A coolify-healthcheck dead-man check runs independently of the monitoring stack on both hosts. If the stack stops reporting, it emails via SES to alexey@datatalks.club and dev@dtcdev.click.

## Retention

I asked to keep about one day of data on disk. Each day, we compress the data from two days earlier and send it to S3. An S3 lifecycle rule keeps those objects for about two weeks, then deletes them.

In the compose file, we set retention to about two days for VictoriaMetrics and VictoriaLogs. We keep roughly one to two days on disk and older data in S3 for about two weeks.

## Health check targets

The health checks cover the infrastructure I care about:

- Postgres on the shared instance and on Relay
- The Coolify UI
- Relay and Relay-dev health endpoints
- The courses API health endpoint
- The website health and ready endpoints
- An AI Shipping Labs ping
- VictoriaMetrics and VictoriaLogs themselves, as dead-man targets

## Alert drills

The public repo includes Docker fault-injection tests for the alert scenarios I required:

- HTTPS target down and recover
- Postgres stop
- Disk fill
- Memory pressure / OOM
- Container restart loop
- Log ERROR spike
- SMTP down
- Scrape target missing
- Vector / VictoriaLogs backpressure
- VictoriaMetrics stop (caught only by the out-of-band dead-man)

## Disaster recovery metrics

Once a week, we time a restore of Contabo Postgres dumps on Hetzner. On real data, the recovery time (RTO) was about 26 seconds.

We record `dr_fast_pg_raise_rto_seconds`, `last_success_unixtime`, `ok`, and `db_bytes` in VictoriaMetrics. If a successful restore is missing for about eight days, the shared developer inbox gets an alert.

## Business metrics

I also asked the agent to collect business metrics before setting deviation alerts. We catalogued about 50 metrics, which we're collecting and storing in Phase 1. I'll revisit alert thresholds in about two weeks.

The durable store is `biz_metrics.metric_daily` on the existing shared Postgres. We use VictoriaMetrics for the live view, but two days of hot retention is too short for weekly comparisons. We use the daily table for historical comparisons.

I named these priority examples:

- Relay: transactional messages, campaign recipients, bounce and complaint rates
- Course management: homework submissions, course registrations
- AI Shipping Labs: lesson opens and active learners, paid conversions and new MRR

Broader families in the same catalog include website event registrations, DataOps newsletter issue stats, and dapier workflow usage.

## Problems after cutover

During the first nights on Contabo, we found misconfigurations in the new setup. We investigated each alert as it arrived and changed how we run production based on what we found.

## Healthcheck false alarms on the Coolify primary

The healthcheck started failing on the Coolify control-plane host. It couldn't find recent database dumps and write-ahead log (WAL) backups. Those backups live on the data host, not on the control plane.

We set `SKIP_BACKUP_CHECKS` on the control-plane host so it only watches apps, disk, and HTTP. The data host still checks dump and WAL age. After that, both hosts passed their checks, and the repeated false FAIL alerts stopped.

## Relay workers kept an old Postgres address

Coolify recreated the Relay Postgres container, and Docker gave it a new address on the internal network. The long-lived Relay workers still had the old address cached and couldn't open the database.

SES webhook messages piled up until the oldest-message alarm fired. Some messages ended up in the dead-letter queue.

Public health endpoints still looked fine because they don't exercise that worker-to-database path.

We restarted the Contabo Relay workers so they resolved the name again, then redrove the dead-letter queue back to the main queue. After that, the incoming message backlog cleared with zero failures.

To detect this if it happened again, we installed a small watchdog on the data host. Every minute it checks, from inside the dependent containers, that the Postgres hostname still resolves and accepts a connection. If Postgres is healthy but a worker can't reach it, the watchdog restarts that worker and emails us. We kept hostname lookup and the watchdog instead of assigning a fixed Docker IP.

## Alert mail went only to the shared inbox

For a while, Contabo production alerts went only to `dev@dtcdev.click`. I want them in my own inbox too.

We restored the alert recipients to both `alexey@datatalks.club` and `dev@dtcdev.click`, on both Contabo hosts, and smoke-tested the mail path.

## SES webhooks stuck after the worker outage

After the same Postgres address change, messages in the production SES webhooks queue exceeded the age threshold. Some were in the dead-letter queue. The consumers on Contabo were stuck while SES remained available.

Restarting the workers and redriving the dead-letter queue cleared both CloudWatch alarms. The queues went back to empty.

## Deploy from GitHub Actions couldn't reach Coolify

After we tightened the edge firewall, GitHub Actions could no longer reach Coolify's API on port 8000. Deploys from CI timed out.

We kept port 8000 closed to public access. Instead, we configured Actions to call Coolify through Traefik over HTTPS, with the token as before. The next website deploy through that path succeeded.

## Coolify deploys return 502/503 errors

On AWS, the ALB waited for the new target to pass health checks before it drained the old one. On Contabo today, we deploy through Coolify by force-recreating the single web container. Between stop and start, Traefik has nothing healthy to send to, so deploys leave a short 502/503 window.

We replaced the ALBs with Traefik for routing, but still need to check the new container's health before switching traffic. We need to configure Coolify to start the new version beside the old one and wait for it to become healthy. Only then should we switch traffic and drain the old container.

## Dead CloudWatch alarms after we deleted RDS

After we deleted RDS, some CloudWatch alarms still referred to the removed databases and load balancers. They stayed in ALARM because they had no datapoints left to evaluate.

We deleted the orphaned RDS and load-balancer alarms. We kept the SES and SQS alarms that still point at real queues.

## Backups: keep little on disk, ship the rest off-host

On Contabo we keep only about two days of Postgres dumps on the data host. Older dumps and WAL live in S3 for about two weeks. The healthcheck alerts if a dump is missing or too old, or if WAL shipping goes stale. The old Hetzner SnapshotExport cron stays disabled because those RDS instances no longer exist.

## Website database empty on Contabo

The main DataTalks.Club domain still served the static site through CloudFront, so visitors didn't see an empty site. The website's Contabo Postgres had its schema but almost no content. Live checks found zero users, documents and events.

Separately, the website importer still expected the old SQLite export from the RDS SnapshotExport pipeline. Contabo dumps are `pg_dump` archives. We need to import the Contabo dumps directly instead of using the old parquet-to-SQLite route. We filed that as its own fix and started the content load against Contabo.

## AI Shipping Labs had no background worker

The AISHL web container was up, but there was no `qcluster` worker on Contabo. The database's scheduled jobs had gone stale for about a day. HTTP looked fine while background work wasn't running.

We opened an immediate fix to add the worker service on Contabo. Once the process is healthy, we can clear the stalled schedules.

## Postgres metrics pointed at the wrong target

We had pointed the Relay Postgres exporter at the wrong address on the private network. Its `pg_up` stayed at zero even while Relay Postgres was fine. The shared Postgres metrics were already green.

We configured the exporter to use the Coolify Postgres hostname on the Docker network and confirmed `pg_up=1`.

## The watchdog only proved a fresh TCP connect

The DNS watchdog's first version opened a new connection from a short-lived probe. That can pass while a long-lived worker still has unusable connections in its pool. SES recovery after the restart was real, but the probe alone isn't full proof.

We filed a follow-up to add progress checks (task or queue freshness) on top of the TCP probe, so `ALL_OK` can't mask a stuck worker.

## Agent scheduling delayed fixes

While we were fixing these problems, our agent Hub often lacked free capacity or access to the requested engine. Work sat waiting even when the fix was clear.

I check Hub placement first and resolve host or capacity problems before starting a backup coding runner. Releasing one host unblocked part of the queue.

We track those delays through the same alert workflow.

## Incident timeline, October 22 to 27

Here's our first week on Contabo, including the monitoring we added along the way. All times are Berlin time.

October 22:

- 00:20 - We run Coolify 4.4.7 on both Contabo servers. We use one as the Coolify primary and the other for the data.
- 02:20 to 02:35 - We cut over Relay first. CloudFront's health check returns 200 through Contabo. We haven't moved everything the ALB did to Traefik yet. On AWS, we had the ALB check a secret origin header from CloudFront, and on Contabo we haven't set up Traefik to check it.
- 07:13 - The first alert emails say both Postgres databases are down. The databases are up. The healthcheck ran with its default environment, and the data host had no `pg_isready`. Also, the default `postgres` user doesn't exist, because Coolify creates a different admin user. We install the Postgres client and change the default user.
- 12:50 to 14:05 - After we deploy the Relay workers, the scheduler and the SES ingress worker restart in a loop. The scheduler is missing a database column, and the ingress worker has no AWS credentials. By 14:05, both run and the SQS queues are empty.
- 15:04 - The main AWS account has no RDS databases and no load balancers left. Continuous WAL archiving is live, and a restore drill on real data takes 26 seconds.
- 16:04 - Relay sends email through SES from Contabo.
- 17:13 - Coolify recreates the Relay Postgres container after a WAL config change, and the container gets a new internal address. The Relay workers keep the old one and stop processing messages, while the healthcheck stays green.
- 18:45 to 19:10 - The AI Shipping Labs staging container gets recreated every five minutes. An auto-deploy script compared image names with and without the `ghcr.io/` prefix, never found a match, and redeployed on every run. We disable the cron and replace the script with one that normalizes the prefix.

October 23:

- 03:02 - We install the DNS watchdog on the data host, and the Relay workers reach Postgres at its new address.
- 03:41 - We have an agent combine three independent audits of the live state. It finds no active outage and files two follow-ups. For about 26 hours, callbacks from Relay to the course platform had returned 503 errors, with 103 failed final attempts. The course platform's webhook token was empty. The disaster-recovery staleness check also sent a false alert.
- 08:40 to 12:15 - The old AI Shipping Labs dev service on ECS keeps coming back. We scale it to zero at 08:40. At 11:52, a GitHub Actions deploy script sets it back to one, and a scheduled Playwright job could do the same. We set the Terraform count to zero and add an IAM rule that denies scaling that service.
- 14:02 to 14:13 - The AI Shipping Labs web and worker containers lose their connection to the shared Postgres network, and the web container crashes because it can't resolve the database name. Coolify runs `docker compose up` first and then connects each container to its networks with `|| true`, so a failed connect stays silent. We declare the networks in the compose file instead.

October 25:

- 01:55 - We fix the Relay deploy check. Each deploy had waited about eight minutes for Coolify to report the aggregate status `running:healthy`, which never happens when some apps have no healthcheck. The new check looks at each app separately. On October 27, we found that the first version read the desired config and not the running containers, and fixed it to check the actual replacement containers.
- 02:08 to 02:23 - Relay dev times out, while production stays at 200. We had recreated the Traefik proxy to add a metrics endpoint, and the recreate dropped its network attachments. We reconnect the networks by hand. Later that day, we add a script that runs every two minutes and keeps Traefik attached to its networks, plus a check every five minutes that only alerts.

October 25 and 26:

- The website staging workers get stuck in the `Created` state. An old workflow step wrote production database settings into the staging secret, so the web container failed its database preflight check. The worker waits for a healthy web container, so it never starts. We fix the workflow and restore the staging database name, and a watchdog that runs every two minutes starts stuck workers. Three staging deploys in a row pass on October 26 between 07:35 and 07:38.

October 27:

- 18:31 - We redeploy the dead-man check with two fixes. It used to split URLs at the first `::`, which broke IPv6 addresses. And an earlier version of its test harness had sent real alert mail through SES, because the test stubs didn't cover the mail binaries.

For a few items from that week, I don't have a recorded outcome yet:

- TODO: Confirm that the Relay callbacks to the course platform work again after the webhook token fix.
- TODO: Confirm that Traefik on Contabo checks the CloudFront origin header.
- TODO: Run a real proxy recreate to prove that the network keeper works, in a maintenance window.
- TODO: Add the Grok Bot conversation history. It lives on the Windows desktop, which was offline from Hub as of November 10. This timeline comes only from the dated agent reports.

## Running production after the move

After the migration, I wanted production errors investigated as soon as they appeared. Healthcheck mail, CloudWatch SES alarms and backup age alerts should reach me and the shared developer inbox.

When an alert fires, I investigate it immediately or have the Developer agent investigate it. We open a Hub task with clear acceptance criteria and start a coding session when needed. We check placement before starting extra agents and work on the failure in the same turn.

We first handled alerts this way during the cutover nights. Some fixes needed a single environment variable change, while others needed a watchdog. Several tasks remain open, each starting from an alert or a live probe.

## The costs now

Three weeks after the cutover, I have final October numbers from Cost Explorer and the first Contabo invoice.

When I first checked on October 21, Cost Explorer showed about $455.50 for October 1 to 21. Cost Explorer hadn't counted all of those costs yet. After October closed, it showed $483.14 for the same 21 days. The full October bill for the main account came to $518.02, not the $650 to $700 the agent had projected. We had stopped most of the infrastructure on October 22.

## Before and after, per day

This is the daily cost of the main AWS account around the cutover:

- October 2 to 21, everything on AWS: $17.25 per day on average, between $16.14 and $21.02
- October 22, the cutover day: $8.18
- October 23: $3.52
- October 24 to 31: between $2.36 and $3.74 per day
- November 2 to 11: between $2.04 and $3.73 per day, except November 9 at $15.96

I left out the first day of each month. AWS charges the monthly support fee and tax on that day, so October 1 was $138.20 and November 1 was $47.05.

On the Contabo side, there's one invoice so far, the proforma invoice from October 21. It covers two Cloud VPS 16 NVMe servers for one month: €59.19 net plus €11.25 VAT, €70.44 in total. At the ECB reference rate on the invoice date, 1.1234 dollars per euro, that's $79.13 per month. Spread over a year, it's about €2.32, or $2.60, per day.

On a regular November day, the main AWS account costs about $2.76 (the average for November 2 to 11 without November 9). Together with Contabo, that's about $5.36 per day, compared with $17.25 per day before the move.

For a month-level comparison, I took the same eleven days in both months, because both include the support fee and tax on the first day:

- October 1 to 11, all on AWS: $312.69
- November 1 to 11: $87.82 on AWS plus about $28.62 for Contabo, $116.44 in total

## The remaining AWS bill

Here's where the $87.82 for November 1 to 11 went:

- AWS Business Support+: $29.00
- SES (Simple Email Service): $15.43
- Tax: $14.02
- RDS backups: $12.74
- WAF: $7.87
- Route 53: $5.88
- KMS: $1.45
- S3: $0.74
- CloudWatch, Cost Explorer, Secrets Manager, SQS and the rest: about $0.70 together

Business Support+ takes the biggest share. It costs $29 per month whether we use AWS a lot or a little, and it's now a third of the main account's bill.

I didn't expect to still pay for RDS. We deleted the databases on October 22, but AWS Backup still holds 222 recovery points for them, with the 90-day retention from our backup plan. We deleted the backup plan on October 23, but that didn't remove the recovery points it had already created. They cost about $1.27 per day. The latest ones are from October 22, so they keep billing until about January 20 unless I delete them earlier.

SES was $15.43, and $13.22 of that came from one day. On November 9, we sent 132,227 emails, and CloudWatch shows the same number of outbound sends. The billing data doesn't show which app sent them.

WAF went up in November. We added a third web ACL on November 10, and the daily WAF cost rose from about $0.64 to $1.12.

On November 12, AWS Budgets emailed me that the organization forecast had crossed my $350 budget. The forecast was $471.68 for November, while the actual spend so far was $100.90. AWS Budgets still bases the forecast on October, when everything ran on AWS. Since then, we added budgets for the main account alone, in $50 steps, plus a daily check that alerts on sudden jumps.

The sandbox account wasn't part of the move. It cost $74.71 in October and $13.07 for November 1 to 11.

I'll keep using AWS for:

- SES for sending email, and the SQS queues that Relay uses for SES webhooks
- An S3 bucket for Coolify database backups, plus the short-lived observability archives
- Route 53 DNS and the CloudFront distribution in front of Relay
- The Relay sandbox / dev tooling that still needs a few Elastic IPs on the sandbox account

I still have a few tasks left:

- I need to move the production deploy workflows from ECR to GitHub Container Registry
- I still need to clean up the orphan sandbox keys and stale secrets
- Business-metric deviation alerts - revisit in about two weeks, once we have enough daily rows
- Finish the website Contabo content load and the importer bridge off the old SQLite export path
- Keep Hub placement available so production fixes can start promptly
- Add rolling web deployments with health checks to Coolify/Traefik to prevent 502/503 errors

## Sources for the cost figures

The cost numbers above come from these sources:

- AWS figures: Cost Explorer, `get-cost-and-usage` with UnblendedCost, filtered to the main account, daily and monthly, grouped by service and usage type. Queried on November 12, 2026. AWS marks the November daily figures as estimated until the month closes.
- October 1 to 21 totals before the move: the same Cost Explorer data, final for October. The earlier $455.50 and its breakdown in this post are the snapshot I saw on October 21.
- RDS backup counts and retention: the AWS Backup recovery point inventory on November 12.
- November 9 sends: the CloudWatch SES Send metric for eu-west-1.
- Contabo: the Contabo proforma invoice dated October 21, 2026, for 2x Cloud VPS 16 NVMe.
- EUR to USD: the ECB euro reference rate for October 21, 2026.

Open TODOs for these numbers:

- TODO: Check for a second Contabo invoice for the second month. On November 12, our invoice records only had the October 21 proforma, and the invoice tool's login had expired, so I couldn't search for newer ones.
- TODO: Replace the November estimates with final figures once AWS closes November.
- TODO: Find out which app sent the 132,227 emails on November 9.

## Lessons learned

I was paying AWS mostly for the parts around the apps.

The containers cost less than the databases, the load balancers or even the tax. For four small apps, I was paying for managed infrastructure built for much bigger systems.

I also learned to watch idle stacks. Scaling a service to zero stops the containers, but the database, balancer, IP addresses and secrets keep billing. When I stop using an app, I need to tear down the whole stack or accept the cost on purpose.

I also had to correct myself on the load balancers. We had little traffic to distribute, but we also used the ALBs to keep deployments available. Removing them without rolling deployments and health checks left us with 502/503 errors during container recreation.

Finally, I liked working this way. I directed the agents in chat through cost analysis, purchasing, migration and monitoring. I made the decisions and approved the destructive steps.

After the first nights on Contabo, I also changed how I want to operate. Alerts arrive by email, and we investigate them through Hub tasks.

I accepted some trade-offs, of course. On AWS, someone else patches the databases and replaces failed hardware. On Contabo, that's my job now, or my agents' job. But for apps of this size, I'm fine with that.

I also learned that deleting a database doesn't delete its backups. Three weeks after the move, retained RDS recovery points are still one of the largest lines on the AWS bill.

So far, the main account went from about $17.25 per day to about $2.76, plus $2.60 per day for Contabo. Subscribe if you want to see the final November numbers.
