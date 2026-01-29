---
title: "Claude Code Experiments"
created: 2026-01-17
updated: 2026-01-29
tags: [claude-code, experiments, automation, copilot, github]
status: draft
---

# Claude Code Experiments

Experiments and practical applications of Claude Code in various scenarios beyond traditional coding tasks.

## Running Code on Cloud vs Phone

I experimented with running Claude Code on different platforms. Initially, I wanted to run it on my phone to be able to work from anywhere without carrying a laptop. The idea was to install Linux on the phone and run Code Code there, connecting via SSH[^1].

### Phone as Server Experiment

The rationale: Android phones have many Google services consuming resources. My old Samsung has 2GB of RAM, with 1.8GB occupied by Google services and Android itself. Installing Linux or a minimal Android could free up resources for running a personal server.

The experiment did not succeed due to Samsung's Knox protection, which prevents reflashing. The phone turned into a brick during the process. However, Claude helped me restore it to factory settings. With a different phone brand (friends say non-Samsung phones work), this approach might succeed[^1].

### Why Not Cloud?

GitHub Copilot Cloud can run code remotely, but it's tied to a specific project and requires a properly configured environment with tests. Claude Code can handle any task possible through a terminal - a much broader range of operations[^1].

Currently, the solution is running a Telegram bot on the laptop that processes requests through Claude. This is the experiment behind the "Telegram Writing Assistant" project[^1].

### Long-Term Vision

The goal is to have an agent running somewhere (ideally on a personal laptop or server) that can handle any request through Telegram. Send a voice or text message, Claude processes it and executes the task. This could eliminate the need to carry a laptop for many tasks[^1].

## Learning New Products Independently

I was asked to prepare an in-person workshop for Exo, a company with a new product for AI agents. The product has minimal documentation. They gave me access to internal courses and asked me to figure out how to use it.

Instead of spending hours going through the materials myself, I gave the task to Claude Code. Here is what I provided:
- The task description
- Instructions on how to install the product
- How to create an account
- Links to internal courses

Claude spent about two hours analyzing the materials. It found a Python library and solved all the required tasks using it. Then it produced a markdown file with complete documentation.

This saved me significant time. I did not have to figure out what works and what does not. Claude did the exploration and delivered organized documentation.

## Course Management Platform Development

Currently working on a new feature for the course management platform to reduce manual administrative work. Previously, administrative tasks required clicking through the Django admin interface manually.

With AI assistants available, I decided to create a more convenient custom admin interface tailored to our platform.

<figure>
  <img src="../assets/images/claude-code-experiments/closed-pull-requests.jpg" alt="List of closed pull requests by Copilot">
  <figcaption>Recent closed pull requests showing Copilot's contributions to the course management platform</figcaption>
  <!-- This illustrates the output of delegating features to AI assistants -->
</figure>

### GitHub-Copilot Workflow

Copilot handles this project well. I have already written about my workflow - I create a GitHub issue, assign it to Copilot, and review the pull request when ready.

The recent pull requests demonstrate this workflow in action[^1]. PR #135 shows a comprehensive implementation:
- Individual review criteria scores editing (instead of aggregate score)
- Auto-calculation of total scores using JavaScript
- Message display fixes across templates
- Template refactoring to eliminate code duplication
- Full test coverage

What is notable about this approach is how features that were previously delayed due to implementation time can now be attempted. If the implementation is good, I accept it. If not, I can iterate with feedback.

### Copilot vs Claude Code

Both tools have their place:

- Cursor and other coding-focused IDEs are optimized for writing code within projects
- Claude Code is better for general-purpose tasks that are not strictly about coding

For example, tasks like "figure out this binary file" or "deal with this USB-connected phone" are better suited to Claude Code's terminal access and general problem-solving capabilities. Cursor can handle them too, but its strength is in coding workflows rather than general automation.

### Terminal-Based vs IDE-Based AI Assistants

I see Claude Code as an assistant that can execute bash commands in the terminal. This is not necessarily about coding - Claude Code handles this well, but for more thoughtful coding work, I prefer Cursor or other IDE-based assistants.

With Cursor, I see all changes the agent makes. I can accept or reject each change. I have more control over what happens. When working from the terminal, I see what the agent is doing and can stop it, but it's more of a "wipe-coding" experience than AI-assisted coding[^2].

For tasks like "send a POST request" or "make this pull request" where I can review the plan first, the terminal workflow works great. I can ask to see the plan first, approve it, and then the agent creates everything[^3].

## Course Material Automation

Beyond the platform development, I've also automated the creation of course materials. Previously, creating homework assignments and course plans required 20-30 minutes of clicking in the admin interface for each course.

I created a Claude agent with skills describing how to interact with the course management platform API. Now I can describe what I want in text format - which homework assignments to create, what deadlines they should have - and the agent makes the POST requests and sends me a URL to review[^4].

This same approach works for creating individual homework assignments. My previous workflow:
1. Write homework in a Markdown document
2. Push to repository
3. Open the platform admin interface
4. Manually enter questions and answers (5-10 minutes)

Now I can tell the agent: "Here's a markdown document with homework, please create the homework form." Done[^5].

## Sources
- [20260117_193932_AlexeyDTC_msg249_transcript.txt](../inbox/raw/20260117_193932_AlexeyDTC_msg249_transcript.txt)
- [20260117_193932_AlexeyDTC_msg250_transcript.txt](../inbox/raw/20260117_193932_AlexeyDTC_msg250_transcript.txt)
- [20260117_193932_AlexeyDTC_msg251_transcript.txt](../inbox/raw/20260117_193932_AlexeyDTC_msg251_transcript.txt)
- [20260117_193932_AlexeyDTC_msg252.md](../inbox/raw/20260117_193932_AlexeyDTC_msg252.md)
- [20260117_193932_AlexeyDTC_msg253_transcript.txt](../inbox/raw/20260117_193932_AlexeyDTC_msg253_transcript.txt)
- [20260117_193932_AlexeyDTC_msg254.md](../inbox/raw/20260117_193932_AlexeyDTC_msg254.md)
- [20260117_193932_AlexeyDTC_msg255_transcript.txt](../inbox/raw/20260117_193932_AlexeyDTC_msg255_transcript.txt)
- [20260117_193932_AlexeyDTC_msg257_transcript.txt](../inbox/raw/20260117_193932_AlexeyDTC_msg257_transcript.txt)
- [20260117_193932_AlexeyDTC_msg256.jpg](../assets/images/claude-code-experiments/closed-pull-requests.jpg)
- [20260123_120918_valeriia_kuka_msg424_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg424_transcript.txt)
- [20260123_120918_valeriia_kuka_msg425_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg425_transcript.txt)
- [20260123_120918_valeriia_kuka_msg426_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg426_transcript.txt)
- [20260123_120918_valeriia_kuka_msg427_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg427_transcript.txt)
- [20260123_120918_valeriia_kuka_msg428_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg428_transcript.txt)
- [20260123_120918_valeriia_kuka_msg429_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg429_transcript.txt)
- [20260123_120956_valeriia_kuka_msg436.md](../inbox/raw/20260123_120956_valeriia_kuka_msg436.md)
- [20260123_121239_valeriia_kuka_msg438.md](../inbox/raw/20260123_121239_valeriia_kuka_msg438.md)
- [20260129_171140_AlexeyDTC_msg641_transcript.txt](../inbox/raw/20260129_171140_AlexeyDTC_msg641_transcript.txt)

[^1]: [20260129_171140_AlexeyDTC_msg641_transcript.txt](../inbox/raw/20260129_171140_AlexeyDTC_msg641_transcript.txt)
[^2]: [PR #135 - Edit individual review criteria scores in project submission and fix message display in cadmin](https://github.com/DataTalksClub/course-management-platform/pull/135)
[^3]: [20260123_120918_valeriia_kuka_msg426_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg426_transcript.txt)
[^4]: [20260123_120918_valeriia_kuka_msg428_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg428_transcript.txt)
[^5]: [20260123_120918_valeriia_kuka_msg424_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg424_transcript.txt)
[^6]: [20260123_120918_valeriia_kuka_msg425_transcript.txt](../inbox/raw/20260123_120918_valeriia_kuka_msg425_transcript.txt)
