---
title: "AI Course Generation with Claude Skills"
created: 2026-04-12
updated: 2026-04-12
tags: [research, claude-code, course-design, ai-generation]
status: draft
---

# AI Course Generation with Claude Skills

## Overview

This article analyzes a Claude skill (custom instruction set) designed to generate full interactive courses from a single topic prompt[^1]. The skill produces a complete Vite + React application with D3.js visualizations, quizzes, and a dark-themed UI. The file is named `ic.md` (likely "interactive course")[^2]. The focus is on how the course is created - the prompt engineering and content generation approach - not the course content itself[^3].

## The Prompt / Project Structure

Source: https://drive.google.com/file/d/1zvu42kRJPsnRhekDHSDfbExr1zFVHpqH/view?usp=sharing

### How It Works

The prompt takes a single argument - a topic name - and generates an entire interactive course as a web application. The user types something like "Build Interactive Course on Statistics" and the skill handles everything else.

The prompt is roughly 1,270 lines long. It follows a 9-step sequential process that guides Claude through scaffolding, component creation, curriculum design, and page generation.

### The 9-Step Pipeline

Step 1 - Decisions and Optional Questions. The prompt explicitly tells Claude to decide things on its own (number of sections, visualization tools) rather than asking the user. It sets smart defaults: "zero to hero" audience level, English language. Only three optional questions are allowed, and only briefly.

Step 2 - Project Scaffolding. A fixed Vite + React project structure with exact file paths. Uses Tailwind CSS v4, D3.js, React Flow, and React Router. Every file name and directory is specified upfront.

Step 3 - Shared Components. Four reusable UI components are provided verbatim - Claude must copy them exactly. These are `Explain.jsx` (explanation blocks, formula boxes, symbol legends, key takeaways), `Quiz.jsx` (mixed multiple-choice and text-input with per-answer feedback), `ArchitectureDiagram.jsx` (React Flow wrapper for system diagrams), and `SequenceDiagram.jsx` (pure SVG step-through message flows).

Step 4 - Curriculum Data Structure. A centralized `curriculum.js` file defines all sections and pages. Each section gets a color from a fixed palette. This drives both the sidebar navigation and the home page grid.

Step 5 - Home Page. Must include a `sectionColors` mapping for every section ID. The prompt warns about a specific crash bug: missing color mappings cause blank screens.

Step 6 - Router Setup. Standard React Router config importing all pages.

Step 7 - Content Pages. Three page templates (A, B, C) for different content types. Each template is a complete working example.

Step 8 - Quiz Authoring. Detailed rules for creating 20 questions per page.

Step 9 - Build Process. Specific order of operations and a parallelism strategy for large courses.

### Prompt Engineering Techniques

The prompt uses several notable patterns.

Technique: "Copy Exactly" for shared components. Rather than describing what the components should do, the prompt includes complete working code that Claude must reproduce verbatim. This eliminates variation and ensures consistency across generated courses. The Quiz component alone is about 150 lines of working React code embedded in the prompt.

Technique: Decision delegation with guardrails. The prompt says "Decide yourself (do NOT ask the user)" for things like section count and visualization tools. But it constrains the range: "typically 5-8 sections." This prevents Claude from over-asking while keeping outputs reasonable.

Technique: Template selection via lookup table. Step 7 includes a table mapping content types to visualization approaches. Data/charts get D3.js. System architecture gets React Flow. Message flows get the custom SVG sequence diagram. Claude picks the right template per page based on what the page teaches.

Technique: Bug prevention through explicit warnings. The prompt calls out a specific failure mode: "If Home.jsx's sectionColors object is missing ANY section.id from curriculum.js, the whole page crashes to blank." It then provides the fix: "Always include a fallbackColor." This is learned-from-experience error handling baked into the prompt.

Technique: Quality constraints on quiz content. The quiz rules are unusually specific. Every wrong answer needs personalized feedback explaining the misconception. Text input answers must use only standard keyboard characters. The difficulty mix is specified: 30% easy, 50% medium, 20% hard. Questions must be interleaved (not grouped by type).

Technique: Parallelism instructions for the agent. Step 9 tells Claude to use background agents for large courses, splitting page generation across 3+ agents. Each agent gets the full component code and templates. This is a meta-instruction - telling the AI how to organize its own work.

### Page Structure Pattern

Every content page follows the same 6-part structure:

1. Header - title with emoji, one-line description
2. Explanation - 2-3 paragraphs using the ExplainBlock component
3. Interactive visualization - the main teaching element with sliders/controls
4. Formula/concept box - with symbol legend
5. Key takeaways - exactly 4 items
6. Quiz - 20 questions, 10 multiple-choice + 10 text input, interleaved

This structure is rigid by design. It creates predictable learning experiences regardless of topic.

### Design System

The prompt includes a complete design system reference: specific hex colors for backgrounds, text hierarchy rules, card styles, button variants, grid layouts, and font sizes. All courses share the same dark theme (slate-900 background, indigo accents).

The color palette is consistent across all visualization types. D3 charts use indigo for primary data, emerald for secondary, amber for highlights, red for errors. Architecture diagrams use the same colors for node types (indigo for services, emerald for databases, amber for external systems).

### What Makes This Effective

The prompt works because it is extremely specific about the output format while leaving content decisions to Claude. It does not try to teach Claude how to explain statistics or networking. Instead, it gives Claude a rigid container (the page template, the quiz format, the component library) and lets Claude fill it with domain knowledge.

The "copy exactly" approach for shared components means Claude spends zero tokens figuring out UI code. All creative energy goes into curriculum design and content writing.

The quiz requirements force depth. Writing 20 questions per page with personalized wrong-answer feedback requires genuine understanding of common misconceptions in the topic area.

### Limitations and Observations

The prompt is tightly coupled to a specific tech stack (Vite, React 18, Tailwind v4, D3 v7). Updating any dependency would require rewriting the prompt.

All courses look the same. The dark theme and layout are hardcoded. There is no mechanism for visual customization.

The 20-question quiz requirement per page is ambitious. For a course with 30+ pages, that is 600+ quiz questions. Quality likely degrades for less common topics.

The prompt does not address content accuracy verification. It trusts Claude's training data for domain knowledge.

## Notes

- This skill represents a "template-first" approach to AI generation. The prompt author built one great course manually, then reverse-engineered the process into a reusable prompt.
- The shared component code is the most valuable part. It solves the hardest UI problems once, then every generated course inherits those solutions.
- Related to the course-design-methodology research - this is a practical implementation of structured course generation.
- The parallelism strategy (Step 9) shows awareness of Claude's agent capabilities and context window limits.

## Resources

### Interactive Course Builder Skill (ic.md)

Source: https://drive.google.com/file/d/1zvu42kRJPsnRhekDHSDfbExr1zFVHpqH/view?usp=sharing

A 1,270-line Claude skill that generates complete interactive web courses from a single topic prompt.

Key Ideas:
- The skill produces a full Vite + React application with routing, sidebar navigation, and a dark-themed UI
- Four shared components (Explain, Quiz, ArchitectureDiagram, SequenceDiagram) are provided as exact copy-paste code
- Three page templates cover different content types: D3 data visualization, React Flow architecture diagrams, and SVG sequence diagrams
- Every page follows a fixed 6-part structure: header, explanation, visualization, formula box, takeaways, quiz
- Each page must include exactly 20 quiz questions (10 MC + 10 text input) with personalized feedback on every answer
- The prompt delegates design decisions to Claude (section count, visualization choice) while constraining the output format
- A parallelism strategy splits page generation across multiple background agents for large courses

Actionable Patterns:
- Embed working component code directly in prompts rather than describing desired behavior
- Use "decide yourself, do NOT ask the user" to prevent unnecessary back-and-forth
- Include explicit bug warnings for known failure modes (like the missing sectionColors crash)
- Provide a lookup table for template selection rather than letting the model choose freely
- Specify difficulty distribution for generated content (30/50/20 easy/medium/hard)
- Give each parallel agent the full context (component code + templates + rules) for consistent output

### Generated Output: Learn Quantum Computing

Source: https://qc.vassilyv.me

Overview: A live example of a course generated by the ic.md skill. The topic is quantum computing. The site is a Vite + React single-page application with client-side routing. Examining its bundled JavaScript reveals the exact structures the skill produces.

Key Ideas:
- The course has 6 sections with 3 lessons each, totaling 18 lessons. This fits the prompt's "typically 5-8 sections" guideline.
- The site claims 360 quiz questions. That is exactly 20 questions per page across 18 pages.
- Each section follows a clear progression from foundations to applications: Quantum Foundations, Quantum Gates, Entanglement, Quantum Circuits, Quantum Algorithms, Real-World Quantum.
- Individual lesson pages are React components rendered client-side. The inner page routes return 404 when accessed directly without proper SPA server config (hash routing or catch-all redirect was not set up).
- The curriculum data structure (`qo` in the minified bundle) is a flat array of section objects. Each section has: id, title, icon (emoji), color (hex), and a pages array with id/title/path/emoji per lesson.

Content Structure Per Lesson (confirmed from bundle analysis):
- Title with subtitle showing section name and lesson number (e.g. "Foundations . Lesson 1")
- ExplainBlock (`st` component) with 2-3 paragraphs of expository content. Color-coded emphasis using the section's palette.
- Interactive D3.js visualization. The first lesson includes a measurement simulator with a slider for the theta parameter and a histogram chart that accumulates measurement results. Users can run 100 measurement shots and watch the histogram converge to Born-rule probabilities.
- FormulaBox (`lt` component) with a rendered formula and a symbol legend table. Example: the qubit state vector formula with definitions for each symbol.
- Key Takeaways (`ct` component) as a bulleted list of exactly 4 items.
- Quiz (`ut` component) with mixed question types. Multiple-choice questions have 4 options each with per-option feedback. Text-input questions accept multiple valid answer formats (e.g. "Born rule", "born rule", "Born's rule", "the Born rule" all accepted for the same question).

Technical Details:
- The shared components match the skill specification exactly. `st` = ExplainBlock (color-coded left-border panel). `lt` = FormulaBox (displays formula + symbol legend). `ct` = KeyTakeaways (bulleted summary). `ut` = Quiz (stateful component tracking answers and showing score).
- D3.js visualizations use a fixed canvas size (680x320) with consistent margins. Color constants are defined once and reused: indigo (#6366f1) for primary, emerald (#10b981) for secondary, amber (#f59e0b) for highlights.
- Quiz questions include computational problems (e.g. "If a qubit has amplitude alpha = 0.6 for |0>, what is P(|0>)?") with text-input answers accepting multiple formats ("0.36", "36%", ".36").
- The interactive simulation uses React refs for D3 rendering and React state for the theta parameter. It runs 100 random samples per click and accumulates results, showing observed vs expected frequencies.

Observations:
- The generated content is dense and technically accurate. The quantum computing explanations use correct notation and formulas.
- The 6-part page structure is followed without deviation across all 18 lessons. The rigid template creates a predictable learning rhythm.
- Each visualization is custom-built for its lesson topic, not a generic chart. The measurement simulator for the first lesson directly demonstrates the concept being taught (superposition and probability).
- The SPA routing issue (404 on direct page access) suggests the build step does not include server configuration. This is a gap in the skill's Step 9 build process.
- Wrong-answer feedback on quiz questions addresses specific misconceptions. Example: selecting "Two qubits are always correlated" for a superposition question gets the feedback "That describes entanglement, not superposition." This shows the quiz authoring rules produce genuinely useful feedback.

## Sources

[^1]: [20260412_152155_AlexeyDTC_msg3371.md](../../inbox/used/20260412_152155_AlexeyDTC_msg3371.md)
[^2]: [20260412_152155_AlexeyDTC_msg3372.md](../../inbox/used/20260412_152155_AlexeyDTC_msg3372.md)
[^3]: [20260412_152249_AlexeyDTC_msg3375.md](../../inbox/used/20260412_152249_AlexeyDTC_msg3375.md)
