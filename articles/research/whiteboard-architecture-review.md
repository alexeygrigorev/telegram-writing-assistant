---
title: "Whiteboard Architecture Review - Forwarded Notes"
created: 2026-10-01
updated: 2026-10-01
tags: [research, architecture, code-review, whiteboard]
status: draft
---

# Whiteboard Architecture Review - Forwarded Notes

I saved a forwarded review of Whiteboard as a resource. The reviewer works at CodeSpeak and came across a Hacker News discussion about Whiteboard as an IDE for architecture review. They tried it to see what it did and shared their impressions.[^1][^2]

## Review structure

The reviewer describes Whiteboard as an agent plugin plus a VS Code review viewer. It uses VS Code for display rather than editing. It can produce a review for an individual pull request or an overview of a whole codebase.[^2]

Each review has three sections:[^2]

- What changed and why.
- Design: new and changed components, flows, diagrams, and decisions.
- Implementation: a step-by-step explanation with text, call trees, and code diffs.

## Diagrams and diffs

You can click a diagram element, such as a flow-diagram step or a function in a call tree, and see the corresponding code diff.[^2]

The semantic diff viewer automatically hides irrelevant sections, folds comments and tests, and collapses large functions into pseudocode.[^2]

## The reviewer's positive findings

The reviewer tried several pull requests containing substantial business logic in their club bot. They liked the step-by-step algorithm diagrams and the ability to click through to descriptions of individual blocks.[^2]

They also liked explaining feature implementation through call trees. A single tree could connect functions and execution paths from different files and modules. These included the frontend, backend business logic, a private API, and functions called by cron. Whiteboard grouped them because they were semantically related.[^2]

## Limitations reported in the review

The reviewer found that Whiteboard explained logic inside a pull request without helping them understand how the change fit the existing architecture. They could check whether the agent understood them correctly, but couldn't judge how well it changed the system as a whole.[^2]

They reported other problems:[^2]

- The developers claimed to extract decisions and requirements, but this worked poorly in the reviewer's tests.
- Some diagrams were irrelevant or unhelpful. Whiteboard inserted sequence diagrams too aggressively in places that didn't need them.
- The tool felt immature, with many bugs and freezes.
- It couldn't describe a large project's full codebase, despite advertising that capability.

## The reviewer's conclusion

The reviewer didn't see much that differed from skills that generate HTML and diagrams from a diff. They liked several UX choices and thought the diff viewer worked well. They didn't understand why the developers used VS Code and considered it overkill.[^2]

The developers had many plans, so the reviewer intended to follow future releases. They also planned to keep testing Whiteboard on large pull requests for a few more weeks.[^2]

## Sources

[^1]: [20261001_041856_AlexeyDTC_msg4986.md](../../inbox/used/20261001_041856_AlexeyDTC_msg4986.md)
[^2]: [20261001_041857_AlexeyDTC_msg4987.md](../../inbox/used/20261001_041857_AlexeyDTC_msg4987.md)
