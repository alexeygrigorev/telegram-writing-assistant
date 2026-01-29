---
title: "Course Material Preparation"
created: 2026-01-22
updated: 2026-01-29
tags: [course-preparation, jupyter, markdown, workflow, automation, claude]
status: draft
---

# Course Material Preparation

The challenge of preparing course materials: keeping code and documentation in sync. When code exists in multiple places (Jupyter notebooks, Python scripts, markdown descriptions), updates in one location don't automatically propagate to others. This synchronization problem makes maintaining consistent course content difficult[^1].

## The Synchronization Problem

Common pain points when preparing course materials:
- Code in Jupyter notebooks becomes outdated when markdown descriptions are updated
- Changes in Python scripts don't reflect in the course documentation
- Jupyter notebooks are cumbersome for diffs and version control (stored as JSON)
- Describing code directly in Jupyter cells doesn't work well for git workflows
- During video recording, the actual implementation often differs from prepared documentation, creating inconsistencies[^3]

## The Solution

A template-based approach where:
- Code lives in a single location (Jupyter notebooks)
- Markdown descriptions reference the notebooks and pull code automatically
- A command renders the final markdown with embedded code
- Tests can be added alongside code for continuous validation

This ensures:
- One source of truth for code
- Code and descriptions stay synchronized
- Easier to review changes in git
- Ability to add tests to code for ongoing verification[^1]

## Command-Line Workflow

A command-line utility was created to interact with Jupyter notebooks:
- Write content in Jupyter notebooks as usual
- The utility converts notebook content to article format
- The rendered markdown becomes the base that can be further edited
- Focus on faster material preparation for courses[^2]

## CLI Utility for Notebook Management

The CLI tool allows viewing and manipulating Jupyter notebooks without dealing with raw JSON:
- View notebook cells in a readable format
- Tag cells for reference in markdown templates
- Reference specific code blocks by tags in documentation
- Add code to notebooks through the CLI
- Automate the workflow between notebooks and markdown[^4]

This approach enables programmatic notebook manipulation, which is not possible through Jupyter's standard interface. The utility can quickly turn notebooks into templates and back again, saving time on manual editing[^4].

## Video-Driven Synchronization

When recording course videos, the implementation often differs from the prepared documentation. Variables might have different names, or the order of topics might change. A synchronization workflow handles this:

1. After recording, the transcript is analyzed for topics not in the documentation
2. The notebook used during recording is identified (not yet committed to git)
3. Changes are compared against template notebooks
4. Templates are updated based on the actual recording
5. Variable names and order are synchronized
6. Documentation is regenerated with updated content[^3]

This entire workflow is implemented as Claude skills that automate the process:
- Commit uncommitted notebooks to git
- Analyze what changed in the notebooks
- Compare against template notebooks
- Update templates based on transcript and notebook changes
- Compile final documentation[^3]

## HTML Generation for Course Platform

Converting markdown to HTML for the course platform (Maven) presented formatting challenges. Line breaks and spacing would be lost when copying HTML directly into Maven's editor.

A solution was implemented:
- A watcher monitors markdown files for changes
- When a file changes, it immediately generates HTML
- The HTML includes invisible spacing elements that prevent Maven from removing formatting
- One click copies the properly formatted HTML
- Paste directly into Maven without manual reformatting[^5]

This reduced manual formatting work significantly. Previously, extensive manual editing was required after pasting HTML into Maven. Now the workflow is streamlined to a single copy-paste operation[^5].

## Long-Term Vision: Own Documentation Platform

Maven lacks an API for creating and updating course content programmatically. All content must be manually managed through their interface. This creates several problems:
- Cannot automatically upload generated content
- Content is locked on Maven's platform
- Manual work required for every update
- No way to retrieve existing content for backup or migration[^6]

The long-term vision is to build a custom documentation site where:
- Content is stored in a personal repository
- Maven units simply link to the documentation site
- All content management happens through automation
- Students access documentation directly on the custom platform[^6]

This would eliminate the manual copy-paste workflow and keep all content under direct control. The only remaining manual task would be creating the Maven unit itself and adding the link[^6].

## Automation Trade-offs

While automation significantly speeds up course material preparation, it requires upfront time investment to set up. During course launch, balancing video recording with automation development can be challenging. Time spent on automation is time not spent on course content[^7].

However, once automation is in place, material preparation becomes much faster. The upfront investment pays off over time, especially when running multiple iterations of a course[^7].

## AI-Assisted Course Preparation Workflow

The current workflow for preparing course materials leverages Claude Skills to automate repetitive tasks. Over multiple iterations of feedback and refinement, the skills have improved significantly.

### The Template System

Code is stored in Jupyter notebooks while content is in markdown documents. When editing the template, the markdown result updates in real-time. This allows immediate preview of changes without manual synchronization[^8].

### Notebook Interaction with Claude

Claude can interact with Jupyter notebooks through the console:
- Inserting needed commands
- Running notebooks
- Editing cell contents

The workflow:
1. Sketch code in the notebook
2. Ask Claude to review the prototype and leave comments
3. Write the lesson material together
4. Have Claude run everything to verify it works before recording
5. Record the video using the prepared template[^8]

### Post-Recording Synchronization

After recording, Claude helps update the documentation:
1. Takes the final notebook used during recording
2. Takes the video transcript
3. Updates the documentation to match what was actually done in the video
4. Ensures lesson notes align with the video content[^8]

This eliminates hours of manual work that was previously required to sync documentation with recorded videos.

### Iterative Skill Improvement

Initially, Claude made mistakes that required correction. Each time an error occurred, Claude was asked to:
1. Analyze what went wrong
2. Update its skills instructions to prevent future occurrences
3. Apply the fix

After 20-30 iterations of this feedback loop, the skills now work correctly about 80% of the time. Some manual fixes are still needed, but the automation saves significant time overall[^8].

### Shift in Focus

With this workflow, more time is spent on:
- Writing and testing code
- Experimenting with different approaches
- Thinking about how to present material clearly
- Deciding what to include or exclude

Less time is spent on:
- Manual synchronization between notebooks and documentation
- Checking variable names and consistency
- Technical cleanup tasks

Claude handles the technical verification - ensuring variables are declared, names match, and the document is clean and ready for publication[^9].

## Sources

- [20260122_170054_AlexeyDTC_msg403_transcript.txt](../inbox/raw/20260122_170054_AlexeyDTC_msg403_transcript.txt)
- [20260122_170137_AlexeyDTC_msg405_transcript.txt](../inbox/raw/20260122_170137_AlexeyDTC_msg405_transcript.txt)
- [20260126_171649_AlexeyDTC_msg589_transcript.txt](../inbox/raw/20260126_171649_AlexeyDTC_msg589_transcript.txt)
- [20260126_171652_AlexeyDTC_msg590_transcript.txt](../inbox/raw/20260126_171652_AlexeyDTC_msg590_transcript.txt)
- [20260126_172612_AlexeyDTC_msg591_transcript.txt](../inbox/raw/20260126_172612_AlexeyDTC_msg591_transcript.txt)
- [20260126_172806_AlexeyDTC_msg592_transcript.txt](../inbox/raw/20260126_172806_AlexeyDTC_msg592_transcript.txt)
- [20260126_173112_AlexeyDTC_msg593_transcript.txt](../inbox/raw/20260126_173112_AlexeyDTC_msg593_transcript.txt)
- [20260126_173253_AlexeyDTC_msg594_transcript.txt](../inbox/raw/20260126_173253_AlexeyDTC_msg594_transcript.txt)
- [20260126_173605_AlexeyDTC_msg595_transcript.txt](../inbox/raw/20260126_173605_AlexeyDTC_msg595_transcript.txt)
- [20260126_180937_AlexeyDTC_msg597_transcript.txt](../inbox/raw/20260126_180937_AlexeyDTC_msg597_transcript.txt)
- [20260129_173421_AlexeyDTC_msg651_transcript.txt](../inbox/raw/20260129_173421_AlexeyDTC_msg651_transcript.txt)
- [20260129_173609_AlexeyDTC_msg652_transcript.txt](../inbox/raw/20260129_173609_AlexeyDTC_msg652_transcript.txt)

[^1]: [20260122_170054_AlexeyDTC_msg403_transcript.txt](../inbox/raw/20260122_170054_AlexeyDTC_msg403_transcript.txt)
[^2]: [20260122_170137_AlexeyDTC_msg405_transcript.txt](../inbox/raw/20260122_170137_AlexeyDTC_msg405_transcript.txt)
[^3]: [20260126_173112_AlexeyDTC_msg593_transcript.txt](../inbox/raw/20260126_173112_AlexeyDTC_msg593_transcript.txt)
[^4]: [20260126_172806_AlexeyDTC_msg592_transcript.txt](../inbox/raw/20260126_172806_AlexeyDTC_msg592_transcript.txt)
[^5]: [20260126_173253_AlexeyDTC_msg594_transcript.txt](../inbox/raw/20260126_173253_AlexeyDTC_msg594_transcript.txt)
[^6]: [20260126_173605_AlexeyDTC_msg595_transcript.txt](../inbox/raw/20260126_173605_AlexeyDTC_msg595_transcript.txt)
[^7]: [20260126_180937_AlexeyDTC_msg597_transcript.txt](../inbox/raw/20260126_180937_AlexeyDTC_msg597_transcript.txt)
[^8]: [20260129_173421_AlexeyDTC_msg651_transcript.txt](../inbox/raw/20260129_173421_AlexeyDTC_msg651_transcript.txt)
[^9]: [20260129_173609_AlexeyDTC_msg652_transcript.txt](../inbox/raw/20260129_173609_AlexeyDTC_msg652_transcript.txt)
