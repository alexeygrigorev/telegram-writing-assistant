---
title: "Karpathy's Autoresearch: Agents Training LLMs"
created: 2026-03-10
updated: 2026-03-10
tags: [ai-agents, automation, newsletter-idea]
status: draft
---

# Karpathy's Autoresearch: Agents Training LLMs

Newsletter idea[^1].

Karpathy's new project went viral: [autoresearch](https://github.com/karpathy/autoresearch). He uses agents to train LLMs, with agents automating everything[^1].

## How it works

The idea: give an AI agent a small but real LLM training setup and let it experiment autonomously overnight. It modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats. You wake up in the morning to a log of experiments and a better model[^2].

The repo has three files that matter[^2]:

- `prepare.py` - fixed data prep and evaluation utilities (not modified by the agent)
- `train.py` - the single file the agent edits, containing the GPT model, optimizer, and training loop
- `program.md` - markdown instructions for the AI agent (edited by the human)

Training runs for a fixed 5-minute time budget. The metric is val_bpb (validation bits per byte) - lower is better. This makes experiments comparable regardless of what the agent changes. You get roughly 12 experiments per hour, about 100 overnight[^2].

The human's job is to iterate on `program.md` (the "research org code"), not on Python files. This is the meta-setup Karpathy mentions[^3].

## Karpathy's results

In [his tweet](https://x.com/karpathy/status/2029701092347630069), Karpathy reports 110 changes made over ~12 hours, bringing validation loss from 0.862415 down to 0.858039. The agent works on a feature branch, tries ideas, merges them when they work, and iterates. He says over the last ~2 weeks he iterated more on the "meta-setup" (optimizing agent flows) than on the nanochat repo directly[^3].

## Connection to our work

This is reminiscent of the idea with automating certificate template creation. In a general sense - how agents can iterate and automate tasks on their own. If they can train LLMs, maybe they can do other tasks without human intervention too[^1].

He writes about having several setups, and one of them produced the best results. The interesting question is what he did from an engineering perspective. Can this be generalized and shared with people so they can use it in their own projects? Or is it all obvious?[^1]

## Sources

[^1]: [20260309_133627_valeriia_kuka_msg2788.md](../inbox/used/20260309_133627_valeriia_kuka_msg2788.md)
[^2]: [autoresearch README](https://github.com/karpathy/autoresearch)
[^3]: [Karpathy tweet](https://x.com/karpathy/status/2029701092347630069)
