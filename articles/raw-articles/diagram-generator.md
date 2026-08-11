---
title: "Diagram Creator: Declarative SVG and PNG Workflows"
created: 2026-05-08
updated: 2026-08-09
tags: [ideas, diagrams, svg, tooling]
status: complete
---

# Diagram Creator: Declarative SVG and PNG Workflows

[Diagram Creator](https://github.com/alexeygrigorev/diagram-creator) implements the original idea: it takes a compact JSON specification and deterministically renders SVG or PNG. The SVG remains editable in Inkscape, Figma, or another vector editor.

## Problem

Image generators can make attractive diagrams, but they often stretch text, vary styles between renders, or miss the requested structure. It's hard to get the exact layout you want or make a precise correction later.

Mermaid covers structural diagrams, but its styling is limited. The missing layer was a small declarative format with polished reusable cards, icons, connectors, and layouts.

## Capabilities

Diagram Creator provides the following capabilities:

- Accepts a JSON description of nodes, edges, canvas dimensions, and layout.
- Generates deterministic SVG and PNG output with the same layout, fonts, and icons.
- Supports horizontal workflows, explicit rows and columns, staircases, and circular loops.
- Supports reusable icons, colored cards, labels, curved routes, and bidirectional edges.
- Produces SVG files that remain easy to edit by hand.

Diagram Creator handles the initial layout and styling. You can then edit the SVG in a familiar vector editor.

## Implementation

The tool is now a tested Python CLI.

Render a diagram with either output extension:

```bash
uv run diagram-creator input.json output.svg
uv run diagram-creator input.json output.png
```

The repository includes generated examples and their JSON sources, so each layout doubles as documentation. Diagram Creator now fulfills the original idea, and future work belongs in its repository rather than in this note[^1][^2].

## Sources

[^1]: [20260508_144110_AlexeyDTC_msg3978_transcript.txt](../../inbox/used/20260508_144110_AlexeyDTC_msg3978_transcript.txt)
[^2]: [20260508_144214_AlexeyDTC_msg3980_transcript.txt](../../inbox/used/20260508_144214_AlexeyDTC_msg3980_transcript.txt)
