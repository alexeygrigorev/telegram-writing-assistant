---
title: "Course Design Methodology"
created: 2026-03-05
updated: 2026-03-05
tags: [research, course-design, teaching, python]
status: draft
---

# Course Design Methodology

Research on pedagogical frameworks and stage-gate processes for designing programming courses. The context is a Python course that prepares students for subsequent courses (ML, data engineering, etc.), using an RSS podcast aggregator as a running project.

## Recommended Framework Combination

Three frameworks work well together for a programming course with a running project:

1. Backward Design - for overall course structure
2. Constructive Alignment - for verifying module consistency
3. Cognitive Load Theory - for breaking material into digestible pieces

Bloom's Taxonomy serves as a checklist for levels, not as a primary framework.

## Frameworks

## Backward Design

The most popular approach in modern education. Start from the learning outcome, then design content.

Steps:

1. Learning Outcomes - what the student should be able to do (not "know")
2. Assessment - how to verify (project, exam, case study, practical assignment)
3. Content - only then decide on lectures, practices, materials

Without backward design, a course becomes "I will tell everything I know." With it, the course becomes "the student must be able to do X."

For a Python course preparing students for other courses, the capability list should be formulated through real tasks:

- Load data from an API
- Process JSON
- Save data
- Write a processing script
- Organize code into modules

## Bloom's Taxonomy

A hierarchy of understanding levels:

1. Remember - memorize
2. Understand - comprehend
3. Apply - use in practice
4. Analyze - break down
5. Evaluate - judge and choose
6. Create - build something new

Example for a programming course:

| Module | Level |
| --- | --- |
| syntax | Remember |
| how a loop works | Understand |
| write an algorithm | Apply |
| optimize code | Analyze |
| choose architecture | Evaluate |
| build a project | Create |

Each module should move the student one level higher.

## Constructive Alignment

All course elements must be aligned:

Learning Outcomes -> Teaching Activities -> Assessment

Bad course: outcome is "able to program," lectures are theory, exam is a test. This is a mismatch.

Good course: outcome is "write programs," activity is coding, assessment is a project.

Verification example for an API module:

- Outcome: student can load data from an API
- Teaching: requests, HTTP, JSON
- Practice: download RSS feed
- Assessment: RSS aggregator fetch step

If all four match, the course is aligned.

## Competency-Based Learning

Focus on skills, not knowledge.

Not "student knows SQL" but "student can write a query for analytics."

Structure: Skill -> Subskill -> Practice -> Project

Used in bootcamps, online schools, and corporate training.

## Spiral Curriculum

Return to the same concepts at a deeper level each time.

Example for Machine Learning:

1. What is a model
2. Linear regression
3. Regularization
4. Neural networks
5. Architecture design

Benefits: better retention, systemic understanding.

## Problem-Based Learning (PBL)

Build the course around problems, not topics.

Instead of separate modules for SQL, Python, Visualization - use one problem: "build a dashboard for business." SQL, Python, and visualization are taught inside that problem context.

Makes learning contextual.

## Cognitive Load Theory

The brain can absorb a limited amount of information at once.

Practical rules:

- One concept per lesson
- Short lectures (10-20 minutes)
- Many examples
- Gradual complexity increase

Bad lesson: functions + loops + lists. Good lesson: loops only.

Key principle - Worked Example -> Practice -> Variation:

1. Show code (download RSS)
2. Explain
3. Student repeats
4. Student modifies (download multiple feeds)

## Stage-Gate Process for Course Design

A step-by-step process with questions, deliverables, quality checks, and transition criteria at each stage.

## Stage 0: Context and Course Boundaries

Goal: understand why the course exists and who it is for.

Questions to ask:

- Who are the students? What do they already know (minimum prerequisites)?
- In which "other courses" do they need Python? What typical tasks appear there?
- What are the constraints: duration, format (online/offline), hours per week, will there be a mentor?
- What does "success" look like 2-4 weeks after the course (not at the end)?
- What is explicitly not included (course boundaries)?

Deliverables:

- Course brief (1 page): audience, goal, constraints, out-of-scope
- Prerequisite checklist (what the student must know before starting)
- Success criteria (2-5 measurable signs of success)

Quality checks:

- Goals are about "doing/solving," not "learning"
- There is an honest out-of-scope section

Gate: you can answer "this course exists so students can do X, Y, Z in other courses" in one paragraph.

## Stage 1: Python Needs Analysis

Goal: turn "Python is needed" into a list of specific skills and patterns.

Questions to ask:

- What 20-50 code fragments/patterns appear in subsequent courses?
- Which libraries/tools are mandatory: requests? pandas? pathlib? typing?
- What is must-have vs. nice-to-have?
- What typical mistakes do students make in other courses (from your experience)?
- What are the "conceptual holes": functions, mutability, exceptions, project structure?

Deliverables:

- Skill inventory: list of skills/patterns + where each is used (in which next course)
- Must/Nice matrix (prioritization)
- Top-10 student pitfalls (errors you want to "cure" in advance)

Quality checks:

- Each skill is tied to real usage ("in course A this is needed for...")
- Must-have fits within time constraints

Gate: you can show a table "Skill -> where needed -> importance."

## Stage 2: Outcome Map

Goal: create outcomes that are verifiable.

Questions to ask:

- What 5-8 key outcomes cover your must-have?
- What artifact proves each outcome?
- Which "qualities" matter: readability, testability, error resilience?
- What minimum code quality level do you want (baseline style)?

Deliverables:

- Outcome map (5-8 outcomes) in the format: "Student is able to [action] in the context of [scenario] by the criterion of [how we verify]"
- Rubric for the final project (or 2-3 rubrics: code quality, functionality, design)
- Definition of Done (what "project accepted" means)

Quality checks:

- Outcomes do not duplicate topics ("knows loops") but describe actions ("filters episodes by criteria")
- Each outcome has a verification method

Gate: there is a rubric that another instructor could use to evaluate work without you.

## Stage 3: Project Decomposition

Goal: turn the RSS aggregator into a "learning staircase."

Questions to ask:

- What is "version 0.1" of the project that can be done in 30-60 minutes and already works?
- What 5-7 increments give a feeling of progress?
- In what order do project steps minimize cognitive load?
- Where will there intentionally be "pain points" (and how will you support them with templates/hints)?

Deliverables:

- Project roadmap: versions v0.1 -> v1.0 (by modules)
- Skill-to-step mapping: which skill is introduced at which step
- Starter repo / project skeleton (if format allows)

Quality checks:

- Early win: the project comes "alive" quickly
- No jumps where "6 new ideas are needed at once"

Gate: each project step "pulls" exactly a limited set of new skills.

## Stage 4: Course Skeleton

Goal: assemble the course into a sequence.

Questions to ask:

- What modules (4-8) logically correspond to project steps?
- What is in each module: 1-2 key ideas (no more)?
- Where is practice: exercises, mini-labs, project increment?
- What is the rhythm: "lesson -> practice -> integration into project"?

Deliverables:

- Course outline: modules -> lessons -> assignments -> project step
- Assessment plan: what is evaluated and when (checkpoints)
- Time budget: approximate time estimate per lesson/assignment

Quality checks:

- Each lesson has a specific "exit capability" and a small result
- Assessment is not only at the end: there are 2-4 checkpoints

Gate: the course can be run "by plan" without improvisation - it is clear what to do each week.

## Stage 5: Lesson Design (Cognitive Load)

Goal: make lessons "digestible."

Questions to ask:

- What is the "one new idea" of the lesson?
- What worked example do you show?
- What does guided practice (with hints) look like?
- What does independent variation (without hints) look like?
- What are typical errors and what hints/tips to provide?

Deliverables:

- Lesson template (one for all): Problem -> Concept -> Worked Example -> Guided Practice -> Independent Practice -> Project Integration
- Cheat sheets (brief syntax/pattern references)
- Error catalog: common errors + how to diagnose

Quality checks:

- Each lesson ends with project integration (or a mini-artifact)
- Material is portioned: no "everything about functions at once"

Gate: you can take any lesson and deliver it in 30-60 minutes with a predictable result.

## Stage 6: Pilot and Iterations

Goal: test the reality of the course, not the theory.

Questions to ask:

- Where do students "get stuck" and why (concept/tool/instructions)?
- What takes twice as long as you thought?
- Which assignments are too easy/hard?
- Do they understand "why" this matters in the context of subsequent courses?

Deliverables:

- Pilot report: 10-15 observations + changes
- Updated rubric/assignments
- List of edits: what to remove, what to move, what to rewrite

Quality checks:

- There is data: completion time, error frequency, project quality
- Fixes address root causes (not "add another lecture")

Gate: after the pilot, the course became shorter/clearer, not "bloated."

## Universal Quality Checklist

Use this at every stage:

- Connection to future courses: every must-have skill has a "where it goes next"
- Alignment: outcome, practice, and assessment match
- Progressive project: the project evolves by versions, not "everything at the end"
- Cognitive load: 1-2 new ideas per lesson, the rest is reinforcement
- Early wins: the first 1-2 sessions produce a working result
- Anti-errors: you proactively teach what breaks most often

## Example Course Structure (RSS Podcast Aggregator)

## Module 1 - Python Basics

Goal: write simple programs. Topics: variables, types, lists, dicts, loops. Practice: process a list of episodes.

## Module 2 - Functions

Goal: structure code. Topics: functions, parameters, return. Practice: parse episode.

## Module 3 - Files

Goal: save data. Topics: files, json. Practice: save episodes.

## Module 4 - HTTP

Goal: work with APIs. Topics: requests, HTTP, JSON. Practice: download RSS.

## Module 5 - Parsing

Goal: process XML. Topics: xml parsing. Practice: parse RSS feed.

## Module 6 - CLI

Goal: write CLI programs. Topics: argparse. Practice: rss fetch, rss list, rss download.

## Progressive Project Pattern

Each module produces a new version of the program:

- Stage 1: fetch feed
- Stage 2: parse feed
- Stage 3: store episodes
- Stage 4: filter
- Stage 5: download

## Skill Tree

Map skills to where they are used in the project:

```
Python
 |- Variables
 |- Lists
 |- Dicts
 |- Loops
 |- Functions
 |- Files
 |- HTTP
 |- Parsing
 |- CLI
```

Each skill should have a note: "used in project for [specific purpose]."

## Best Programming Course Structure

The pattern used by top courses:

Concept -> Mini Exercise -> Project Step

Example: Lesson on Lists -> Exercise: filter episodes -> Project step: implement episode filter.

## Templates

## Course Brief (1 page)

- Who it is for:
- After the course, the student will be able to:
- Where this will be used next:
- Format / duration:
- What is not included:
- Final project:
- Success criteria:

## Outcome Template

"Student is able to [action] in the context of [scenario] by the criterion of [how we verify]."

## Lesson Template

- Problem:
- Concept:
- Worked example:
- Guided practice:
- Independent practice:
- Project step:

## Three Main Course Design Mistakes

1. Course equals a list of lectures. A proper course is a list of skills.
2. No project. Without a project, knowledge does not integrate.
3. Too much theory. Better ratio: 20% theory, 80% practice.

## Notes

- This article is closely related to [Instructional Design for Online Courses](instructional-design.md) which covers completion rates and student engagement.
- The backward design approach here aligns with how the Python course RSS aggregator project was conceived - starting from what students need in subsequent courses.
- The stage-gate process provides a concrete checklist for the Python course development workflow.

## Sources

[^1]: [ChatGPT conversation on course design](https://chatgpt.com/share/69a99cff-2b54-800a-8048-3291dffa6103) via [20260305_151138_AlexeyDTC_msg2766.md](../../inbox/used/20260305_151138_AlexeyDTC_msg2766.md)
