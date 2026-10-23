# How I Moved Our Apps from AWS to Two Contabo Servers - publishing notes

Status: draft, 2026-10-23 (post-cutover expansion t1221u Europe/Berlin; prior IP + observability t1138u). Template: Build Log (shoot-the-article), outline and draft written in one pass (t1116u, Hub intake d8e419b9-dc11-40d9-9dac-6fefc624c535); IP + observability expansion from t1138u; post-cutover problems/fixes + ops loop from t1221u.

Sources: `inbox/raw/20261022_144628_alexey_msgt1116u_cloud-to-baremetal-chat-export.md` (cost report appendices) and `inbox/raw/20261022_125100_alexey_msg1792673460.md` (enriched dialogue: hosting analysis, Pack A, t995u cron disable); t1138u ask to deepen analysis-before-buy, public IPv4 story, and Contabo observability; t1221u post-cutover incidents from `~/tmp/agent-reports` (alerts-t1205u/t1209u, relay-contabo-stability-t1207u, relay-pg-no-pin-t1210u, coolify-gha-api-8000-t1040u, main-dead-cw-alarms-t1127u, contabo-dump-wal-retention-t1146u, website-importer-contabo-dump-t1154u, postgres-exporter-relay-fix-t1218u, contabo-current-state-*-t1212u / t1218u follow-ups). Every money figure in the draft comes from the cost sources. No account IDs, IPs, order numbers, distribution IDs or hostnames are in the draft.

## Thesis

I was paying AWS mostly for the parts around the apps (RDS, load balancers, public IPs, support, tax), while the containers themselves were about $37 + $7 EC2 of the $455.50.

## Section map

1. Opener + roadmap - sandbox KMS question on Oct 21, all four prod apps on Contabo by Oct 22 afternoon, done through agents; roadmap includes IP cleanup + observability + post-cutover problems/fixes + ops loop
2. The sandbox bill - $14.91 KMS+SM, 12 orphan CMKs from a deploy leak (~$12/mo), DynamoDB still needs KMS
3. The main account - $455.50 Oct 1-21 breakdown, $650-700 projection, Public IPv4 ~$20 (~$19.58 EU in-use, ~7-8 IPs, ~$3.6/IP/mo), Business Support+ link to the dropped-DB post, idle website stack, SnapshotExport $19.80
4. The first plan: trim AWS - the 4-item backlog, ALB annoyance, hosting brief (EUR 70-80, 2x64 GB), Coolify defined
5. Buying the servers - no-buy-before-analysis rule (analysis completed before order), Hetzner ~EUR 30 baseline, AX42 ~EUR 67 vs CAX31+CAX21 ~EUR 32.48, agent box isn't prod, budget as ceiling, 2x Contabo Cloud VPS 16 at EUR 70.44/mo incl VAT, peer-agent go review then buy, "bare metal" caveat, plan rules, Coolify 4.4.7, staging on GHCR
6. The cutover - Relay first, teardown list, ~$60-70/mo Relay savings, shared SM 40 + 17, t993u status vs backlog, cron bug, CMP/AISHL/website DNS cut, all ALBs deleted (none left on MAIN)
7. The last step: the databases - 4 predelete snapshots kept, instances deleted after Alexey's go (current as of late Oct 22 afternoon Europe/Berlin); rule from the dropped-DB incident
8. Public IPv4 after the move - ~$20 MAIN public IPv4 story; same-day teardown of bastion, website NAT + its EIP; AISHL ECS scaled to 0; MAIN left with zero EIP / NAT / public ENI / ALB / RDS; sandbox still has a few EIPs for live/dev tools
9. Observability on Contabo - VictoriaMetrics + VictoriaLogs + Vector + thin vmui; public repo alexeygrigorev/coolify-observability with Docker alert drills; coolify-healthcheck dead-man → SES to alexey@datatalks.club + dev@dtcdev.click; retention ~1-2d hot, day-before-yesterday to S3 ~2 weeks; probed targets (Postgres, Coolify UI, Relay/Relay-dev, courses, website, AISHL, VM/VL); alert drill list; DR weekly raise RTO ~26s + VM metrics + stale ~8d alert; business metrics ~50 catalogued, Phase 1 collect-only into biz_metrics.metric_daily, P0 families named, deviation alerts later (~2 weeks)
10. What broke after cutover - real first-night incidents + fixes: SKIP_BACKUP_CHECKS on CP; Relay PG Docker DNS stale → worker restart + DLQ redrive + relay-pg-dns-watchdog (DNS+watchdog, no IP pin); ALERT_TO dual; SES oldest/DLQ; GHA→Coolify via Traefik HTTPS (port 8000 stays closed); dead MAIN RDS/ALB CloudWatch alarms deleted; dump/WAL local≤2d S3~14d + age alerts; empty website Contabo DB + importer still SQLite; AISHL missing qcluster; postgres-exporter-relay wrong target fixed; watchdog TCP-only gap follow-up; Hub no_eligible_route / dig-before-aplexer
11. How we run production after the move - alerts to alexey@ + dev@ → immediate triage → Hub intake+AC+sessions → same-turn fix-on-failure (not weekly postmortem / not wait for «почини»)
12. The costs now - EUR 70.44 (~$77), savings unknown until November bill, what stays on AWS, open tasks (ECR→GHCR, orphan keys, biz-metric alerts later, website Contabo content/importer, Hub placeability)
13. Lessons learned - thesis, idle stacks (incl. public IPv4), agent-driven workflow with human approval on destructive steps, fix-on-failure loop, trade-offs, follow-up + subscribe

## Things to verify before publishing

- Who scaled the website ECS services to zero and when (draft keeps it passive)
- Whether the t995u cron disable actually completed (export says "executed/tracked"; draft says I asked for it)
- Why Contabo Pack A over the ~EUR 32.48 Hetzner pair (sources don't say; draft only notes the 64 GB RAM)
- Whether prod deploys still go through ECR after the t998u cut
- Whether WireGuard between the two Contabo nodes was actually set up (draft lists it as part of the plan)
- Relay's one-line description ("a service built on Amazon SES and SQS") - Alexey may want a better one
- RDS / ALB / bastion status: draft marks snapshots kept, instances removed, ALBs gone, bastion gone — current as of late Oct 22 afternoon Europe/Berlin; re-check at publish time
- Exact MAIN public IPv4 count (draft says ~7-8 from ALBs × AZs + NAT + bastion); ~$3.6/IP/mo and ~$19.58 EU in-use are from the cost reports
- Observability compose hot retentionPeriod=2d vs the ~1 day hot ask — draft says ~1-2 days hot without inventing past the report
- DR RTO ~26s and stale-alert ~8 days — from the observability work; reconfirm numbers if a later run differs
- Business metrics catalog size (~50) and that no deviation alert thresholds are live yet
- Post-cutover incident list vs live Contabo state at publish time (website content load, AISHL qcluster, Hub placeability, watchdog progress checks may still be in flight)
- ALERT_TO still dual alexey@ + dev@ on both Contabo hosts
- Confirm GHA COOLIFY_URL still Traefik HTTPS (not raw :8000)

## Platform deltas

Substack (Alexey On Data, aishippingblog.com):
- Subtitle: What the AWS bill looked like, what the move cost, and what still runs on AWS
- Paywall: if paywalled, place the break after "The main account"
- Publish-time apparatus added on Substack, not in the draft: editor credit, digest sections if it's a regular issue

Medium:
- Topic tags: AWS, Cloud Computing, DevOps, Self Hosting, AI Agents, Observability
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
- AWS public IPv4 cost
- AWS KMS orphan keys
- Secrets Manager pricing
- migrating with coding agents
- self-hosted PaaS
- VictoriaMetrics
- VictoriaLogs
- Coolify observability
- production incident response
- self-hosted Postgres Docker DNS

## Title and subtitle shortlist

Titles:
1. How I Moved Our Apps from AWS to Two Contabo Servers
2. Moving Our Production Apps from AWS to Contabo and Coolify
3. How I Left AWS for Two Servers in Two Days
4. What Leaving AWS Cost Me
5. From AWS to Coolify: Moving Four Apps in Two Days

Subtitles:
1. What the AWS bill looked like, what broke after cutover, and how we fix production the same turn
2. Four apps, two servers, public IPv4 cleanup, and observability that isn't a Grafana zoo
3. How a question about encryption keys ended with a migration

## Image placeholders

None in the draft. Candidates:
1. Cost Explorer screenshot of the main account by service (Oct 1-21)
2. Coolify dashboard with the four apps and three Postgres containers healthy
3. Simple before/after diagram: ALB + ECS + RDS per app on AWS vs Traefik + containers + Postgres on two Contabo servers
4. vmui or coolify-healthcheck alert email example (no account IDs / IPs)
