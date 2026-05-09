---
title: "Declarative Diagram Generator"
created: 2026-05-08
updated: 2026-05-08
tags: [ideas, diagrams, svg, tooling]
status: draft
---

# Declarative Diagram Generator

Idea for a diagram generator that takes a declarative description of the desired diagram and produces a clean SVG file that can later be opened in Inkscape, Figma, or another vector editor for manual touch-ups.

## Why

ChatGPT generates pretty pictures, but they often come out stretched, inconsistent, or not in the style you want. It is hard to get the exact look you are after.

Mermaid covers structural diagrams, but the styling is limited. Want something with nicer styles and the ability to drop in icons (Font Awesome and others) so the result looks polished out of the box.

## What it would do

- Accept a declarative description of the diagram.
- Generate an SVG with consistent, attractive styling.
- Allow icons to be added (Font Awesome and others).
- Output a file that opens cleanly in Inkscape or Figma so it can be edited by hand without fighting the tool.

The key property is the editable SVG output - the generator does the heavy lifting, but the user can always tweak the result in a familiar vector editor.

## Status

Just an idea for now. Already have prior projects that generate Mermaid-style diagrams, so something similar could be built on top of that. Worth picking up when there is time[^1][^2].

## Sources

[^1]: [20260508_144110_AlexeyDTC_msg3978_transcript.txt](../../inbox/used/20260508_144110_AlexeyDTC_msg3978_transcript.txt)
[^2]: [20260508_144214_AlexeyDTC_msg3980_transcript.txt](../../inbox/used/20260508_144214_AlexeyDTC_msg3980_transcript.txt)
