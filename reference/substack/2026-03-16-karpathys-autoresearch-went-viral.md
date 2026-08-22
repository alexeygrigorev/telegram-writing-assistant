---
title: "Karpathy's Autoresearch Went Viral. Here's How It Works (and One Idea to Try)"
date: 2026-03-16
url: https://aishippingblog.com/p/karpathys-autoresearch-went-viral
---

Over the last few days, [Andrej Karpathy](https://open.substack.com/users/23972309-andrej-karpathy?utm_source=mentions)’s [autoresearch project](https://github.com/karpathy/autoresearch) has been widely shared and discussed. Many people on X (Twitter) are exploring the idea and trying to apply the same pattern to their own projects.

[![Image 1](https://substackcdn.com/image/fetch/$s_!D7lm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa793ff14-9e3a-4278-a5e7-24711063d9db_2590x1212.png)](https://substackcdn.com/image/fetch/$s_!D7lm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa793ff14-9e3a-4278-a5e7-24711063d9db_2590x1212.png)

I looked through the repository and decided to write a short note explaining what the project actually does and why it is attracting so much interest.

## Core Idea

At a high level, autoresearch automates something that normally takes a large amount of human time: running experiments and iterating on models. In a typical workflow, a researcher modifies the training code or parameters, runs an experiment, evaluates the result, logs the metrics, and then repeats the process.

[![Image 2](https://substackcdn.com/image/fetch/$s_!1mPz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52d31ca7-d253-4d00-b79d-7b6e58273f6f_2816x1414.png)](https://substackcdn.com/image/fetch/$s_!1mPz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52d31ca7-d253-4d00-b79d-7b6e58273f6f_2816x1414.png)

Autoresearch delegates this entire loop to an agent. You start the system, let it run for hours, and it performs many small experiments on its own, gradually improving the model.

Conceptually, this resembles AutoML, where algorithms search through hyperparameters and architectures. The difference is that autoresearch uses an LLM to perform the search directly in code. Instead of selecting parameters from predefined spaces, the model edits the training script itself and proposes new ideas for the architecture or training procedure.

[![teaser](https://substackcdn.com/image/fetch/$s_!MuQR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45f2323e-bac5-493b-9298-ab45a399835f_2382x1180.png)](https://substackcdn.com/image/fetch/$s_!MuQR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45f2323e-bac5-493b-9298-ab45a399835f_2382x1180.png)

## Repository Structure

The repository implementing this system is surprisingly small.

[![Image 4](https://substackcdn.com/image/fetch/$s_!Uxvx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9e81ecc-b628-4d4c-b97f-ce4b17f0e8cb_1800x860.png)](https://substackcdn.com/image/fetch/$s_!Uxvx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9e81ecc-b628-4d4c-b97f-ce4b17f0e8cb_1800x860.png)

It revolves around three files:

1. `prepare.py`: Contains the fixed components of the experiment: data preparation, dataset downloads, and the evaluation logic. The agent cannot modify this file.
2. `train.py`: Contains the model implementation and training loop. This is the file the agent edits when proposing new experiments.
3. `program.md`: Contains instructions for the agent written in natural language. Karpathy describes it as “research org code written in English.”

When the system starts, the agent establishes a baseline by creating a new Git branch, running the unmodified training script, and recording the initial metric.

After that, it enters the experiment loop:

* Edits `train.py`, commits the change
* Runs the experiment
* Extracts the resulting metrics from the logs

If the metric improves, the commit is kept. If the result is worse or unchanged, the repository is reset to the previous state. Each experiment runs under the same fixed time budget, which ensures that results remain comparable even if the agent modifies the model size or training procedure.

[![Image 5](https://substackcdn.com/image/fetch/$s_!xD_d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb0c5d04-3b62-486f-ae83-360b3201961b_1475x1400.png)](https://substackcdn.com/image/fetch/$s_!xD_d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb0c5d04-3b62-486f-ae83-360b3201961b_1475x1400.png)

The most interesting aspect of the project is the system's structure. There are effectively three layers of programming:

* First layer: Traditional code in `prepare.py`, which defines the rules of the environment and the evaluation metric.
* Second layer: Python code in `train.py`, which represents the model and can be modified during experiments.
* Third layer: `program.md`, where the human writes natural-language instructions describing how the agent should behave as a researcher.

In practice, this creates an unusual chain where a human writes instructions in English, the LLM translates them into modifications to Python code, and the Python code trains a neural network. Instead of directly improving the model, the human is programming the experimental process using natural language.

[Share](https://aishippingblog.com/p/karpathys-autoresearch-went-viral?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## Optimization Process

[![Image 6](https://substackcdn.com/image/fetch/$s_!7WdW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d80e043-c70b-4bae-9e3a-9c9fbe9e6952_1802x676.png)](https://substackcdn.com/image/fetch/$s_!7WdW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d80e043-c70b-4bae-9e3a-9c9fbe9e6952_1802x676.png)

The system works because the experimentation process is tightly constrained. Each experiment has a strict time budget, so runs cannot expand indefinitely. Every change is evaluated using a single metric, and only modifications that improve the metric are kept. If a change fails or produces worse results, it is automatically reverted. These rules keep the exploration focused and prevent the system from drifting into unproductive directions.

[![Image 7](https://substackcdn.com/image/fetch/$s_!b7nr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd2e9a33-4291-4e51-ae6b-07912997b8b1_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!b7nr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd2e9a33-4291-4e51-ae6b-07912997b8b1_2816x1536.png)

The objective of the loop is to optimize a metric that measures model quality. In Karpathy’s example, the metric is validation bits per byte (val\_bpb). Lower values indicate better performance. This metric is useful because it remains comparable even if the tokenizer or vocabulary size changes during experimentation.

Each iteration follows a simple structure: the agent modifies the training code, runs the experiment, evaluates the metric, and keeps the change only if the result improves. Otherwise, it rolls back the change and tries something else. This process continues indefinitely.

## Results

Karpathy [reported](https://x.com/karpathy/status/2029701092347630069) that the system produced 110 successful changes in about twelve hours, improving the validation metric from 0.862415 to 0.858039. He also noted that much of his recent effort has gone into refining the experimental setup rather than directly modifying the model. In other words, the work has shifted toward improving the system that runs the research.

[![X avatar for @karpathy](https://substackcdn.com/image/fetch/$s_!oMwR!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1296667294148382721%2F9Pr6XrPB.jpg)

Andrej Karpathy@karpathy

nanochat now trains GPT-2 capability model in just 2 hours on a single 8XH100 node (down from ~3 hours 1 month ago). Getting a lot closer to ~interactive! A bunch of tuning and features (fp8) went in but the biggest difference was a switch of the dataset from FineWeb-edu to

![Image 9](https://pbs.substack.com/media/HCrwu6YaUAAoAlh.jpg)

11:30 PM · Mar 5, 2026 · 584K Views

332 Replies · 555 Reposts · 6.43K Likes](https://x.com/karpathy/status/2029701092347630069)

## Others Experimenting with the Pattern

Since the project was published, others have started experimenting with the same pattern.

* One example is [Autosearcher](https://x.com/varun_mathur/status/2031550020101480507), a distributed system in which multiple agents run experiments in parallel and share their discoveries. In early runs, the system rediscovered techniques such as Kaiming initialization and RMSNorm purely through experimentation.

* Another example is [AutoVoiceEvals](https://x.com/archiexzzz/status/2033258540312510702), in which the same iterative loop is applied to optimize prompts for voice agents via adversarial evaluation. In one reported experiment, twenty automated iterations improved a scheduling agent’s success rate from 25 percent to 100 percent, while the final prompt became shorter rather than longer.

## Project Idea

One possible experiment with the autoresearch approach is applying it to writing style optimization.

When working with LLMs, the generated text often differs noticeably from my own writing style. To reduce this gap, I currently maintain a style guide that describes how I phrase things, structure sentences, and revise outputs that do not match my voice. Over time, this guide grows as I manually correct generated text and add new rules.

The idea is to automate this process using an autoresearch-style loop.

Instead of refining the style guide manually, the system would treat the prompt or style guide itself as the artifact being optimized. The loop would use a dataset consisting of texts I wrote or texts where I corrected LLM output after generation.

Each iteration would follow a pattern similar to the autoresearch workflow:

1. Modify the style prompt or guide
2. Generate sample outputs from the model
3. Compare the outputs to reference texts
4. Evaluate stylistic similarity using a metric
5. Keep the change if the score improves

Possible evaluation signals could include embedding similarity, a classifier trained to distinguish my writing from generated text, or LLM-based evaluation.

This approach turns prompt tuning into an automated search process. Instead of manually adjusting instructions, the agent iteratively improves the prompt based on measurable feedback.

## Why People Find It Interesting

autoresearch’s underlying optimization loop is not fundamentally new. What has changed is that LLMs can now participate directly in the research workflow. They can read code, propose modifications, run experiments, analyze results, and generate the next hypothesis. Instead of manually exploring ideas, the human defines the rules and constraints of the research environment and lets the system explore it automatically.

That shift in how experimentation is organized is what makes autoresearch interesting to so many people right now.

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
