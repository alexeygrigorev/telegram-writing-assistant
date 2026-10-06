---
title: "AI Agents Do Everything Now. You Still Need Kubernetes."
created: 2026-10-06
updated: 2026-10-06
tags: [kubernetes, ai-agents, infrastructure]
status: draft
---

# AI Agents Do Everything Now. You Still Need Kubernetes.

AI agents write code, deploy services, monitor systems, and fix problems automatically. So why would you still care about Kubernetes?

The answer is simple: agents need somewhere to run.

## Agents Are Tenants, Not Landlords

An AI agent can generate a Dockerfile, write a Helm chart, and push it to a cluster. But it can't be the cluster. It needs compute, GPUs, networking, access to data, the ability to scale, and a way to recover when something fails.

That's infrastructure. Kubernetes is that infrastructure layer.

Think of it this way: AI agents are software that runs on infrastructure. Kubernetes is the infrastructure. One doesn't replace the other. They work at different levels of the stack.

## The AI Boom Made Kubernetes More Relevant

Here's the thing most people miss: AI workloads didn't make Kubernetes less important. They made it more important.

Running AI in production comes with a specific set of problems:

- GPU scheduling. A single A100 costs $2-3 per hour. Without proper scheduling, GPUs sit idle while teams wait for their turn
- Model serving at scale. You need autoscaling for inference endpoints, or you're either over-provisioning (wasting money) or dropping requests
- Multi-model deployments. Canary rollouts, A/B testing between model versions, traffic splitting. Kubernetes networking handles all of that
- Training pipelines. Distributed training across multiple nodes needs orchestration that manual scripts can't reliably provide
- Multi-tenancy. Multiple teams sharing GPU resources need fair scheduling and resource quotas

The ecosystem is already built for this. Kubeflow runs end-to-end ML pipelines on Kubernetes. KServe handles serverless model inference with autoscaling. KubeRay runs distributed Ray workloads. The NVIDIA GPU Operator automates GPU driver management. Kueue provides job queueing for batch and AI workloads.

The 2025 CNCF survey found that 82% of container users run Kubernetes in production, up from 66% in 2023. Two-thirds of organizations running generative AI models use Kubernetes for some or all of their inference workloads, and 90% expect their AI workloads on Kubernetes to increase in the next 12 months. The CNCF now calls Kubernetes "the de facto operating system for AI."

## AI Agents Make Kubernetes Easier

There's an irony here. While people ask "does AI replace Kubernetes?", AI is actually making Kubernetes more accessible.

Tools like K8sGPT diagnose cluster issues in plain language. Kubectl AI lets you manage clusters through natural conversation. Robusta automates incident response. Kagent, an open-source framework by Solo.io, runs AI agents inside Kubernetes that troubleshoot and manage the cluster itself. AI coding agents generate correct Kubernetes manifests from a description of what you want.

The barrier to using Kubernetes was always the learning curve. AI agents are lowering that barrier, which means more teams can use Kubernetes, not fewer.

## The Complexity Didn't Go Away

"But serverless replaces Kubernetes." Most serverless platforms run on Kubernetes under the hood. AWS Fargate, Google Cloud Run - they abstract it away, but it's still there.

"AI agents can deploy themselves." They can write deployment scripts, but they need a platform to deploy to. You don't remove the platform just because the tenant got smarter.

"You can just use managed services for everything." Until you hit vendor lock-in, cost problems at scale, GPU availability issues, or compliance requirements that force you on-prem.

The complexity of running production systems hasn't decreased. It shifted. AI helps manage that complexity, but the underlying infrastructure challenges remain. Someone needs to schedule containers, manage secrets, handle network policies, perform rolling updates, and run health checks.

That someone is Kubernetes.

## KubeAuto Day Berlin

If you're in Berlin and want to see how Kubernetes and AI work together in practice, check out Kubernetes Automation Day on October 15.

There are talks about taking autonomous AI agents from your laptop to Kubernetes, building autonomous SRE agents, optimizing hundreds of Kubernetes clusters, and what platform engineering looks like in an AI-driven world.

It's a free, community-run evening event at Alte Turnhalle with 200+ attendees and speakers from Delivery Hero, DKB, Weaviate, Giant Swarm, Pulumi, Google Cloud, and AWS.

Register at [kubeauto.day/berlin](https://kubeauto.day/berlin).

If you're not in Berlin, there are KubeAuto Days in other cities too - check [kubeauto.day](https://kubeauto.day/) for the full list.

## Sources

[^1]: [20261006_172142_AlexeyDTC_msg5006.md](../../inbox/used/20261006_172142_AlexeyDTC_msg5006.md)
