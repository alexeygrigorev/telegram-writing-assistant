---
title: "Autoresearch Project"
created: 2026-03-10
updated: 2026-03-12
tags: [ai-agents, automation, newsletter-idea]
status: draft
---

# Autoresearch Project

Newsletter idea[^1]. Karpathy's new project went viral: [autoresearch](https://github.com/karpathy/autoresearch). He uses agents to train LLMs, with agents automating everything[^1].

Right now many people on Twitter are actively discussing this approach and trying to use it for many other things. It is worth writing a few words about what autoresearch actually does, since there is so much interest[^4].

## The short version

You can really just explain this in a couple of paragraphs. The approach is cool because it automates a routine task that normally takes a lot of time. You launch it, go for a walk, come back in 24 hours, and you have an optimized model[^8].

There are also built-in limitations that make it work. The agent analyzed the repository and figured out heuristics like "no run should take more than 10 minutes." These kinds of constraints are what make the whole process efficient in practice[^8].

## My understanding

Say we have a task: optimize model quality. We have a way to measure this quality - we run our model on some data and track a metric, for example accuracy[^4].

Previously data scientists optimized this manually. They tuned parameters, changed the model, ran experiments, tracked these experiments somewhere in MLflow, and so on. Then a thing called AutoML appeared. Instead of doing it manually, the model does it for you - there is some smart parameter search that works better than full grid search[^4].

As I understand it, the autoresearch approach delegates this parameter search and architecture selection to an LLM. The LLM uses some criterion and tries to optimize it. It looks at the metric, looks at the code, and tries to change something in the code to optimize that metric. There is nothing fundamentally new here. But the point is: you optimize a metric, you delegate it to an LLM, and the LLM has a loop - something like a REPL loop - that optimizes the metric. It keeps doing this until you stop it[^4].

Since there is so much interest, it might be useful to write a short note about this. Maybe someone will find it interesting[^4].

## Repository analysis

The repo has three files that matter[^2][^7]:

- `prepare.py` - fixed data prep and evaluation utilities (~300 lines). Defines the ground truth metric, downloads data shards from HuggingFace, trains a BPE tokenizer, provides the `evaluate_bpb()` function. The agent cannot touch this file[^7].
- `train.py` - the single file the agent edits (~450 lines). Contains a full GPT model implementation with modern techniques (RoPE, RMS norm, Flash Attention 3, sliding window attention, logit soft-capping), a custom MuonAdamW optimizer, and the training loop[^7].
- `program.md` - markdown instructions for the AI agent (~120 lines). The human iterates on this file to improve agent behavior. This is "research org code" written in English[^2][^7].

### The agent loop

The loop described in `program.md`[^7]:

Setup phase:
1. Agree on a run tag (e.g., `mar5`)
2. Create branch `autoresearch/<tag>` from master
3. Read all in-scope files for context
4. Verify data exists in `~/.cache/autoresearch/`
5. Initialize `results.tsv` with header row
6. Run baseline (unmodified `train.py`) to establish the starting val_bpb

Experiment loop (runs forever):
1. Look at current git state
2. Edit `train.py` with an experimental idea
3. `git commit`
4. Run: `uv run train.py > run.log 2>&1`
5. Extract results: `grep "^val_bpb:\|^peak_vram_mb:" run.log`
6. If grep is empty, the run crashed. Read the last 50 lines of the log for the stack trace, attempt fix
7. Log to `results.tsv`
8. If val_bpb improved (lower) - keep the commit, advance the branch
9. If val_bpb is same or worse - `git reset` back to where it was

Critical rules from `program.md`: the agent must never stop. It runs until manually interrupted. "If you run out of ideas, think harder." Any run exceeding 10 minutes gets killed. A tiny improvement that adds ugly complexity is not worth keeping, but deleting code for equal results is worth keeping[^7].

### The metric

The single metric is val_bpb (validation bits per byte) - lower is better[^2][^7].

Why BPB instead of cross-entropy loss: BPB is vocab-size-independent. If the agent changes the tokenizer vocab size or architecture, results remain comparable. It is calculated as the sum of per-token cross-entropy (in nats) divided by the sum of target byte lengths (UTF-8), converted to bits-per-byte[^7].

The time-budget design is key: every experiment trains for exactly 300 seconds of wall-clock training time (excluding startup and torch.compile compilation). This means experiments are always comparable regardless of what the agent changes. The agent can trade off model size vs. number of training steps - a bigger model does fewer steps in 5 minutes, a smaller one does more[^7].

### The meta-level insight

The most interesting aspect is the layering of "programming"[^7]:

- Layer 1: `prepare.py` is traditional Python code that defines the fixed rules (data, eval metric, time budget)
- Layer 2: `train.py` is Python code that the AI agent modifies - it is the "genome" being optimized
- Layer 3: `program.md` is natural language that the human writes to program the AI agent's research behavior

The human does not write Python to improve the model. The human writes English in `program.md` to instruct the agent, which writes Python in `train.py`. As Karpathy puts it: "you are programming the `program.md` Markdown files that provide context to the AI agents and set up your autonomous research org."[^2]

## Where my understanding was right and wrong

The core understanding is correct: autoresearch delegates optimization to an LLM that runs in a loop, looks at a metric, modifies code, and keeps iterating until stopped. The comparison to AutoML is apt - it is a similar concept but using an LLM as the search engine instead of traditional optimization algorithms[^4][^7].

A few things to refine:

- The specific metric is val_bpb (validation bits per byte), not accuracy. BPB was chosen because it is vocab-size-independent, so results stay comparable even if the agent changes the tokenizer[^7].
- The loop is more structured than a simple REPL. Each experiment is a git commit. If it improves the metric, the commit stays. If not, `git reset` reverts it. This gives a clean git history of only successful experiments[^7].
- The time-budget approach (exactly 5 minutes per experiment) is a key design choice that makes all experiments comparable regardless of what the agent changes[^7].
- There is a meta-level that goes beyond just "LLM optimizes a metric." The human programs in natural language (`program.md`), which instructs the LLM, which programs in Python (`train.py`). Three layers of programming[^7].

## Karpathy's results

In [his tweet](https://x.com/karpathy/status/2029701092347630069), Karpathy reports 110 changes made over ~12 hours, bringing validation loss from 0.862415 down to 0.858039. The agent works on a feature branch, tries ideas, merges them when they work, and iterates. He says over the last ~2 weeks he iterated more on the "meta-setup" (optimizing agent flows) than on the nanochat repo directly[^3].

## Twitter buzz

This approach is getting a lot of discussion on Twitter. It is interesting that people are discovering this for themselves[^4].

Based on what Karpathy proposed, someone is already using this approach in their own project[^5]. Varun Mathur is applying the same pattern to build a distributed search engine called Autosearcher. Their network had 67 autonomous agents run 704 ML training experiments in 20 hours, rediscovering Kaiming initialization, RMSNorm, and compute-optimal training schedules from scratch through pure experimentation and gossip-based cross-pollination. Agents shared discoveries over GossipSub, and new agents bootstrapped from the swarm's collective knowledge. They are now applying the same evolutionary loop to search ranking[^5][^6].

## Connection to our work

This is reminiscent of the idea with automating certificate template creation. In a general sense - how agents can iterate and automate tasks on their own. If they can train LLMs, maybe they can do other tasks without human intervention too[^1].

He writes about having several setups, and one of them produced the best results. The interesting question is what he did from an engineering perspective. Can this be generalized and shared with people so they can use it in their own projects? Or is it all obvious?[^1]

## Sources

[^1]: [20260309_133627_valeriia_kuka_msg2788.md](../inbox/used/20260309_133627_valeriia_kuka_msg2788.md)
[^2]: [autoresearch README](https://github.com/karpathy/autoresearch)
[^3]: [Karpathy tweet](https://x.com/karpathy/status/2029701092347630069)
[^4]: [20260312_080548_AlexeyDTC_msg2860_transcript.txt](../inbox/used/20260312_080548_AlexeyDTC_msg2860_transcript.txt)
[^5]: [20260312_080548_AlexeyDTC_msg2858.md](../inbox/used/20260312_080548_AlexeyDTC_msg2858.md) and [20260312_080548_AlexeyDTC_msg2859.md](../inbox/used/20260312_080548_AlexeyDTC_msg2859.md)
[^6]: [Varun Mathur tweet](https://x.com/varun_mathur/status/2031550020101480507)
[^7]: [autoresearch repository analysis](https://github.com/karpathy/autoresearch) via [20260312_080712_AlexeyDTC_msg2864.md](../inbox/used/20260312_080712_AlexeyDTC_msg2864.md)
[^8]: [20260312_082424_AlexeyDTC_msg2870_transcript.txt](../inbox/used/20260312_082424_AlexeyDTC_msg2870_transcript.txt)
