---
title: "How I Moved Our Apps from AWS to Two Contabo Servers"
subtitle: "What the AWS bill looked like, what broke after cutover, and how we fix production the same turn"
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
- Why I bought two Contabo servers and installed Coolify — after the analysis, not before
- How the cutover went, one app at a time
- The public IPv4 cleanup once the apps left AWS
- Observability on Contabo: metrics, logs, alerts, and the business metrics we're collecting first
- What broke in the first nights after cutover, and how we fixed each problem
- The ops loop we run now: alerts land in mail, and we fix the same turn
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

Public IPv4 alone was about $20 for those three weeks. Almost all of it was the EU public IPv4 in-use charge — about $19.58. That covered roughly seven or eight addresses: load balancers across availability zones, a NAT gateway, and a bastion. At about $3.60 per IP per month, the line adds up quietly.

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

The load balancers annoyed me the most. Each app had its own Application Load Balancer, but the ALBs were not required in that setup. None of them had real multi-target load to balance — just a few small apps. We still paid about $64 in three weeks for the balancers, plus public IPv4 addresses across availability zones, for traffic that one reverse proxy could route. The first idea was to replace the three ALBs with one nginx server.

In the same message, I asked the agent to look for hosting. I named a budget of about €70 to €80 per month for two machines with 64 GB of RAM each. I wanted to run [Coolify](https://coolify.io/) on them.

Coolify is an open-source, self-hosted platform for deploying apps. It does roughly what Heroku or Vercel do, on your own servers. It runs Docker containers and puts a Traefik reverse proxy in front of them, which handles routing and TLS certificates. That Traefik is what would later take over the routing role — not a standalone nginx.

I asked for results by the next morning, China time.

## Buying the servers

I also told the agent not to purchase anything before a thorough analysis. Our Hetzner server costs about €30 per month, and I didn't want to pay much more for the same thing.

So the agent analyzed first. No order went out until that comparison was done and reviewed.

The agent first compared Hetzner options. One dedicated AX42 server for about €67 was more than we needed. Two smaller Hetzner cloud servers, a CAX31 and a CAX21, came to about €32.48.

Putting Coolify on the existing Hetzner server was another option. But my agents work on that server, so it isn't a quiet place for production. The agent box and production don't share a machine.

I preferred two cheaper servers over one big one. I turned the €70 to €80 budget into a ceiling, and I hoped to spend closer to €30 to €50.

In the end, I picked two Cloud VPS 16 instances from [Contabo](https://contabo.com/), each with 16 cores and 64 GB of RAM. The promo price was about €29.60 each, and the total came to €70.44 per month including VAT.

That's above the range I hoped for, but each server has 64 GB of RAM. Before buying, I asked the agent to check with my other agents that this setup would work. Two of them reviewed the plan, and both said go.

Only after that review did the agent place the order.

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

By then, the agent was moving the apps instead of trimming AWS. There was no point in making the AWS databases cheaper if the apps were about to leave them. The standalone nginx never got built either — Coolify already ships Traefik, and that was enough for a few small apps.

In the same report, the agent noticed that the snapshot export cron still had a line for Relay. Its database no longer existed, so that export would fail every evening. I asked the agent to run one last export and then disable the cron.

Later that day, the agent switched DNS and CloudFront for the course platform, AI Shipping Labs and the website to Coolify's Traefik on Contabo. All three came up healthy. That was the real cutover of the routing idea: nginx was the first plan on AWS; Traefik is what actually routes traffic now. The agent then deleted the remaining Application Load Balancers. After cutover, the main account had none left.

## The last step: the databases

After the apps were on Contabo, four RDS databases were still running on AWS. They belonged to the course platform, AI Shipping Labs, the website, and a shared dev database. The production apps no longer used them.

Before deleting anything, I asked the agent to take a snapshot of each one. All four snapshots were kept — three for regular instances and one for the Aurora cluster.

I set that rule after the database incident. Back then, an agent ran `terraform apply` with auto-approve and wiped our production infrastructure. Since then, I keep one hard rule: agents prepare destructive steps, and I approve them.

Once the snapshots were in place and I approved, the agent deleted the RDS instances. The snapshots stay. The instances are gone.

## Public IPv4 after the move

Once the apps lived on Contabo, the main account's public IPv4 addresses had nothing left to serve.

For October 1 to 21, that line was about $20 — almost all of it the EU in-use charge of about $19.58. Roughly seven or eight public IPv4s were in play: load balancers across availability zones, a NAT gateway, and the course-management bastion. At about $3.60 per IP per month, idle addresses still billed.

The same day as the cutover, the agent tore those leftovers down:

- The course-management bastion EC2 host
- The website NAT gateway
- The Elastic IP attached to that NAT

AI Shipping Labs' ECS services were scaled to zero. They had been the only private consumers of that NAT.

After that cleanup, the main account had zero Elastic IPs, zero NAT gateways, zero public network interfaces, zero Application Load Balancers, and zero RDS instances.

The sandbox account still has a few associated Elastic IPs for live and dev tools. Those stay for now. The main account's public IPv4 story is over.

## Observability on Contabo

Moving off managed AWS also meant replacing CloudWatch. I asked for a small stack, not a Grafana / Prometheus / Loki zoo.

What landed is VictoriaMetrics and VictoriaLogs on Contabo. Vector ships logs and metrics into them. For day-to-day checks I use a thin vmui. The setup, including Docker fault-injection tests for the alerts, lives in the public repo [alexeygrigorev/coolify-observability](https://github.com/alexeygrigorev/coolify-observability).

An out-of-band coolify-healthcheck dead-man runs on both hosts. If the stack goes quiet, it emails via SES to alexey@datatalks.club and dev@dtcdev.click.

### Retention

I asked for about one day hot on disk. Each day, the day-before-yesterday ships compressed to S3. An S3 lifecycle rule keeps those objects for about two weeks, then deletes them.

In the compose file, VictoriaMetrics and VictoriaLogs use a hot retention of about two days. So hot retention is roughly one to two days; older data lives in S3 for about two weeks.

### What gets probed

The health checks cover the infra I care about:

- Postgres on the shared instance and on Relay
- The Coolify UI
- Relay and Relay-dev health endpoints
- The courses API health endpoint
- The website health and ready endpoints
- An AI Shipping Labs ping
- VictoriaMetrics and VictoriaLogs themselves, as dead-man targets

### Alert drills

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

### Disaster recovery raise metrics

Once a week, a timed restore takes Contabo Postgres dumps and raises them on Hetzner. On real data, the RTO was about 26 seconds.

VictoriaMetrics stores `dr_fast_pg_raise_rto_seconds`, `last_success_unixtime`, `ok`, and `db_bytes`. If there is no successful raise for about eight days, an alert goes to dev@.

### Business metrics

I also asked for business metrics — collect first, deviation alerts later. We catalogued about 50 of them. Phase 1 only collects and stores; no alert thresholds yet. I'll revisit that in about two weeks.

The durable store is Postgres: `biz_metrics.metric_daily` on the existing shared Postgres. VictoriaMetrics is the live view, but two days of hot retention is too short for week-over-week, so the daily table is the source of truth.

Priority examples I named:

- Relay: transactional messages, campaign recipients, bounce and complaint rates
- Course management: homework submissions, course registrations
- AI Shipping Labs: lesson opens and active learners, paid conversions and new MRR

Broader families in the same catalog include website event registrations, DataOps newsletter issue stats, and dapier workflow usage. Collection is on; alerting on deviations comes later.


## What broke after cutover

Moving the apps was the easy half. The first nights on Contabo showed the real work: small misconfigurations that only show up in production, and a habit of fixing them the same turn instead of waiting for a weekly review.

Here is what actually showed up, and what we did about each one.

### Healthcheck false alarms on the Coolify primary

The healthcheck started failing on the Coolify control-plane host for dump and WAL freshness. Those backups live on the data host, not on the control plane. The control plane was looking for files that were never supposed to be there.

We set `SKIP_BACKUP_CHECKS` on the control-plane host so it only watches apps, disk, and HTTP. The data host still checks dump and WAL age. After that, both hosts reported green, and the false FAIL storm stopped.

### Relay workers kept an old Postgres address

Coolify recreated the Relay Postgres container. Docker gave it a new address on the internal network. The long-lived Relay workers still had the old address cached. They could not open the database. SES webhook messages piled up, the oldest-message alarm fired, and messages landed in the dead-letter queue.

Public health endpoints still looked fine, because they do not exercise that worker-to-database path.

We restarted the Contabo Relay workers so they resolved the name again, then redrove the dead-letter queue back to the main queue. After that, ingress drained with failures at zero.

To stop the silent repeat, we installed a small watchdog on the data host. Every minute it checks, from inside the dependent containers, that the Postgres hostname still resolves and accepts a connection. If Postgres itself is healthy but a worker cannot reach it, the watchdog restarts that worker and emails us. We kept hostname plus the watchdog. We did not pin a fixed Docker IP — that path was cancelled on purpose.

### Alert mail went only to the shared inbox

For a while, Contabo production alerts went only to `dev@dtcdev.click`. I want them in my own inbox too.

We restored the alert recipients to both `alexey@datatalks.club` and `dev@dtcdev.click`, on both Contabo hosts, and smoke-tested the mail path.

### SES webhooks stuck after the worker outage

The same Postgres DNS churn left the production SES webhooks queue aging past the threshold, with messages in the dead-letter queue. That was not an SES outage. The consumers on Contabo were the ones stuck.

Restarting the workers and redriving the dead-letter queue cleared both CloudWatch alarms. The queues went back to empty.

### Deploy from GitHub Actions could not reach Coolify

After we tightened the edge firewall, GitHub Actions could no longer reach Coolify's API on port 8000. Deploys from CI timed out.

We kept port 8000 closed to the world. Instead, Actions calls Coolify through Traefik over HTTPS, with the token as before. The next website deploy through that path succeeded.

### Dead CloudWatch alarms after we deleted RDS

Once the RDS instances were gone, a few leftover CloudWatch alarms for deleted databases and load balancers stayed in ALARM because they had no datapoints left to evaluate. They were noise.

We deleted the orphaned RDS and load-balancer alarms. We kept the SES and SQS alarms that still point at real queues.

### Backups: keep little on disk, ship the rest off-host

On Contabo we keep only about two days of Postgres dumps on the data host. Older dumps and WAL live in S3 for about two weeks. The healthcheck alerts if a dump is missing or too old, or if WAL shipping goes stale. The old Hetzner SnapshotExport cron stays disabled — those RDS instances no longer exist.

### Website database empty on Contabo

The public DataTalks.Club apex still served from the static CloudFront path, so visitors did not see an empty site. The Contabo Postgres for the website, though, had schema and almost no content — zero users, documents, and events in the live checks.

Separately, the website importer still expected the old SQLite export from the RDS SnapshotExport pipeline. Contabo dumps are `pg_dump` archives. That bridge needs a Contabo-native import path, not the old parquet-to-SQLite route. We filed that as its own fix and started the content load against Contabo.

### AI Shipping Labs had no background worker

The AISHL web container was up, but there was no `qcluster` worker on Contabo. Scheduled jobs in the database had gone stale for about a day. HTTP looked fine; background work did not run.

We treated that as a same-turn production gap: add the worker service on Contabo and clear the stalled schedules once the process is healthy.

### Postgres metrics pointed at the wrong target

The Relay Postgres exporter was scraping the wrong address on the private network, so `pg_up` stayed at zero even while Relay Postgres itself was fine. Shared Postgres metrics were already green.

We repointed the exporter at the Coolify Postgres hostname on the Docker network — again hostname, not a pinned IP — and confirmed `pg_up=1`.

### The watchdog only proved a fresh TCP connect

The DNS watchdog's first version opened a new connection from a short-lived probe. That can pass while a long-lived worker still holds a dead pool. SES recovery after the restart was real, but the probe alone is not full proof.

We filed a follow-up to add progress checks (task or queue freshness) on top of the TCP probe, so `ALL_OK` cannot mask a stuck worker.

### The agent scheduler got in the way of the fixes

While we were fixing the above, our agent Hub often could not place a coding session — no free capacity, or the requested engine was unavailable. Work sat waiting even when the fix was clear.

The standing rule is: check Hub placement first, fix the host or capacity when that is the blocker, and only then start a backup coding runner. One host release unblocked part of the queue. Capacity is still a live concern — it delays how fast a fix can land, so it stays on the same alert loop.

## How we run production after the move

After the migration, I do not want a weekly postmortem culture for Contabo. I want the opposite.

Every production error should fly to me and to the shared developer inbox — healthcheck mail, CloudWatch SES alarms, backup age alerts. When something fires, I (or the Developer agent working as me) triage immediately. We open a Hub task with clear acceptance criteria, start a coding session when we need one, check placement before spinning extra agents, and fix the failure in the same turn.

The standing rule is fix-on-failure: maximally fast reaction to production problems, not batching until someone asks «почини». The cutover nights were the first real test of that loop. Some fixes were a one-line env change. Some needed a watchdog. Some are still open. All of them started from an alert or a live probe, not from a scheduled review.

## The costs now

The new fixed cost is €70.44 per month for both Contabo servers, which is about $77.

I can't state the savings yet. AWS bills with a lag, and the agent did most of the teardown in the last day. I'll know the real number when the November bill arrives.

Some things will stay on AWS:

- SES for sending email, and the SQS queues that Relay uses for SES webhooks
- An S3 bucket for Coolify database backups, plus the short-lived observability archives
- Route 53 DNS and the CloudFront distribution in front of Relay
- The Relay sandbox / dev tooling that still needs a few Elastic IPs on the sandbox account

I still have a few tasks left:

- I need to move the production deploy workflows from ECR to GitHub Container Registry
- I still need to clean up the orphan sandbox keys and stale secrets
- Business-metric deviation alerts — revisit in about two weeks, once we have enough daily rows
- Finish the website Contabo content load and the importer bridge off the old SQLite export path
- Keep Hub placeability healthy so same-turn fixes are not stuck waiting for a free engine

## Lessons learned

I was paying AWS mostly for the parts around the apps.

The containers cost less than the databases, the load balancers or even the tax. For four small apps, I was paying for managed infrastructure built for much bigger systems.

I also learned to watch idle stacks. Scaling a service to zero stops the containers, but the database, balancer, IP addresses and secrets keep billing. When I stop using an app, I need to tear down the whole stack or accept the cost on purpose. The public IPv4 line was a clear example: about $20 for three weeks of addresses that became useless the moment Traefik took over.

Finally, I liked working this way. The agents ran Cost Explorer, analyzed hosting before any purchase, bought the servers, installed Coolify, migrated the data, switched DNS, cleaned up IPs, and stood up observability. I made the decisions in chat and approved the destructive steps.

The first nights after cutover also changed how I want to operate. Alerts go to my mail. We dig, open a Hub task, and fix the same turn. That is slower to write about than a clean migration story, and more useful.

I accepted some trade-offs, of course. On AWS, someone else patches the databases and replaces failed hardware. On Contabo, that's my job now, or my agents' job. But for apps of this size, I'm fine with that.

Once the November bill arrives, I'll write a follow-up with the real numbers. Subscribe if you want to see how it turns out.
