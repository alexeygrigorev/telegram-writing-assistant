# How I Moved Our Apps from AWS to Two Contabo Servers - publishing notes

Status: draft, 2026-10-22. Template: Build Log (shoot-the-article), outline and draft written in one pass (t1116u, Hub intake d8e419b9-dc11-40d9-9dac-6fefc624c535).

Sources: `inbox/raw/20261022_144628_alexey_msgt1116u_cloud-to-baremetal-chat-export.md` (cost report appendices) and `inbox/raw/20261022_125100_alexey_msg1792673460.md` (enriched dialogue: hosting analysis, Pack A, t995u cron disable). Both exports are a report-derived reconstruction of the Developer chat plus four cost reports, not a verbatim transcript. Every money figure in the draft comes from it. No account IDs, IPs, order numbers, distribution IDs or hostnames are in the draft.

## Thesis

I was paying AWS mostly for the parts around the apps (RDS, load balancers, public IPs, support, tax), while the containers themselves were about $37 + $7 EC2 of the $455.50.

## Section map

1. Opener + roadmap - sandbox KMS question on Oct 21, all four prod apps on Contabo by Oct 22 afternoon, done through agents
2. The sandbox bill - $14.91 KMS+SM, 12 orphan CMKs from a deploy leak (~$12/mo), DynamoDB still needs KMS
3. The main account - $455.50 Oct 1-21 breakdown, $650-700 projection, Business Support+ link to the dropped-DB post, idle website stack, SnapshotExport $19.80
4. The first plan: trim AWS - the 4-item backlog, ALB annoyance, hosting brief (EUR 70-80, 2x64 GB), Coolify defined
5. Buying the servers - no-buy-before-analysis rule, Hetzner ~EUR 30 baseline, AX42 ~EUR 67 vs CAX31+CAX21 ~EUR 32.48, agent box isn't prod, budget as ceiling, 2x Contabo Cloud VPS 16 at EUR 70.44/mo incl VAT, agents' go review, "bare metal" caveat, plan rules, Coolify 4.4.7, staging on GHCR
6. The cutover - Relay first, teardown list, ~$60-70/mo Relay savings, shared SM 40 + 17, t993u status vs backlog, cron bug, CMP/AISHL/website DNS cut, 2 of 3 ALBs deleted
7. The last step: the databases - 4 predelete snapshots available, delete waits for Alexey's go, rule from the dropped-DB incident
8. The costs now - EUR 70.44 (~$77), savings unknown until November bill, what stays on AWS, open tasks
9. Lessons learned - thesis, idle stacks, agent-driven workflow with human approval on destructive steps, trade-offs, follow-up + subscribe

## Things to verify before publishing

- Who scaled the website ECS services to zero and when (draft keeps it passive)
- Whether the t995u cron disable actually completed (export says "executed/tracked"; draft says I asked for it)
- Why Contabo Pack A over the ~EUR 32.48 Hetzner pair (sources don't say; draft only notes the 64 GB RAM)
- Whether prod deploys still go through ECR after the t998u cut
- Whether WireGuard between the two Contabo nodes was actually set up (draft lists it as part of the plan)
- Relay's one-line description ("a service built on Amazon SES and SQS") - Alexey may want a better one
- RDS delete status at publish time; update the "last step" section accordingly

## Platform deltas

Substack (Alexey On Data, aishippingblog.com):
- Subtitle: What the AWS bill looked like, what the move cost, and what still runs on AWS
- Paywall: if paywalled, place the break after "The main account"
- Publish-time apparatus added on Substack, not in the draft: editor credit, digest sections if it's a regular issue

Medium:
- Topic tags: AWS, Cloud Computing, DevOps, Self Hosting, AI Agents
- Member-only: no
- End CTA: Thanks for reading! If you found this useful, subscribe to Alexey On Data (https://aishippingblog.com) for more AI engineering deep dives, practical guides, and the occasional production war story.

## SEO keywords

- leaving AWS
- AWS cost reduction
- AWS to bare metal migration
- Coolify self-hosting
- Contabo VPS
- RDS cost
- Application Load Balancer cost
- AWS KMS orphan keys
- Secrets Manager pricing
- migrating with coding agents
- self-hosted PaaS

## Title and subtitle shortlist

Titles:
1. How I Moved Our Apps from AWS to Two Contabo Servers
2. Moving Our Production Apps from AWS to Contabo and Coolify
3. How I Left AWS for Two Servers in Two Days
4. What Leaving AWS Cost Me
5. From AWS to Coolify: Moving Four Apps in Two Days

Subtitles:
1. What the AWS bill looked like, what the move cost, and what still runs on AWS
2. Four apps, two servers, and an RDS teardown that's still waiting for my go
3. How a question about encryption keys ended with a migration

## Image placeholders

None in the draft. Candidates:
1. Cost Explorer screenshot of the main account by service (Oct 1-21)
2. Coolify dashboard with the four apps and three Postgres containers healthy
3. Simple before/after diagram: ALB + ECS + RDS per app on AWS vs Traefik + containers + Postgres on two Contabo servers
