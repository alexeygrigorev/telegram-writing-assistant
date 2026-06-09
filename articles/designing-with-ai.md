---
title: "Approaching Design with AI as a Non-Designer"
created: 2026-05-19
updated: 2026-06-09
tags: [design, chatgpt, codex, tailwind, course-platform, datatalks-club, pocketshell, ui]
status: draft
---

# Approaching Design with AI as a Non-Designer

We all understand by now what AI slop looks like when it comes to projects. You can often tell right away that a project was made with AI, because it has certain design elements that are characteristic of AI.[^9]

I am not a designer, I do not claim to be one, and I never liked front-end or design work. But now I do end up making some of these things. This article is about how I approach design, so that the result does not look like slop, even though I am not a designer.[^9]

## The design elements that give AI away

When I say a project has design elements characteristic of AI, I mean specific habits I keep running into and correcting.

One is button placement. AI likes to put action buttons on the right, the way they show up here. I have to correct it and move them underneath instead.[^22]

<figure>
  <img src="../assets/images/designing-with-ai/ai-buttons-on-right.jpg" alt="Event series page with action buttons lined up on the right side">
  <figcaption>The buttons end up on the right by default - I move them underneath</figcaption>
  <!-- Concrete example of the button-placement tic the user keeps correcting -->
</figure>

Another is column density. AI produces these columns that sometimes make the UI too dense.[^23][^24]

<figure>
  <img src="../assets/images/designing-with-ai/ai-dense-columns-event.jpg" alt="Edit event page with a right-hand column of state and meeting details">
  <figcaption>Columns that make the layout too dense</figcaption>
  <!-- First example of the dense-column tic -->
</figure>

<figure>
  <img src="../assets/images/designing-with-ai/ai-dense-columns-student.jpg" alt="Student progress page with a row of metric cards and a two-column layout">
  <figcaption>Another page where the columns crowd the layout</figcaption>
  <!-- Second example of the same dense-column tic -->
</figure>

And then there is the layout I think of as typical AI design: the feature grid where every cell has an icon, a title, and a short blurb.[^25]

<figure>
  <img src="../assets/images/designing-with-ai/ai-feature-grid.jpg" alt="Marketing feature grid with four cells, each with an icon, a title, and a short description">
  <figcaption>Typical AI design - the icon-title-blurb feature grid</figcaption>
  <!-- The generic feature-grid pattern the user points at as the tell-tale AI look -->
</figure>

## ChatGPT generates great designs

Not long ago GPT Image 2 came out, and for me it was a turning point. On Twitter people started posting images of screenshots with the caption "this is not a screenshot". The point is that this part of GPT became really good at generating designs. It can essentially reproduce any design. You can tell it to generate a WhatsApp window or a Telegram window, and it does it easily.[^10]

As an illustration of how well ChatGPT generates screenshots: I just sent it a screenshot of my own Telegram and said I wanted the same conversation, but with Elon Musk. It reproduced it. I do not think the screenshot itself will surprise anyone now, but the point is that GPT Image 2 is genuinely very good. It can generate great images, including screenshots and designs, and it can come up with a design that looks beautiful.[^11]

<figure>
  <img src="../assets/images/designing-with-ai/generated-screenshot-elon-musk.jpg" alt="ChatGPT-generated screenshot of a WhatsApp conversation with Elon Musk">
  <figcaption>A generated screenshot - I sent ChatGPT a screenshot of my Telegram and asked for the same conversation with Elon Musk. <a href="https://chatgpt.com/s/m_6a270ab6ce6c81918ea2240c74178a56">The generation</a>.</figcaption>
  <!-- Concrete proof of how well the image model reproduces a real app's look, which is the foundation of the whole mockup-first approach -->
</figure>

## How it started: the Tailwind migration issue

I will step back to where it all started. On the course management platform for DataTalks.Club there was an issue that had been open for a couple of years: migrate the site to Tailwind. One of the students had filed it. I never had time to deal with it, so I never did.[^12]

That issue is [github.com/DataTalksClub/course-management-platform/issues/76](https://github.com/DataTalksClub/course-management-platform/issues/76) [^13].

The issue appeared in November 2024. I had created the platform earlier that year. I knew nothing besides Bootstrap, so I used Bootstrap. The interface was what it was - it had functionality and it did its job. Even back then I used AI to help me build the site, and I picked the tools I already knew, so I went with Django and Bootstrap. I made something, and it worked.[^14]

One of the community members suggested migrating everything to Tailwind. I had heard Tailwind was a more modern system than Bootstrap, but I did not know it myself. There had been attempts to submit a redesign from other people, and I did not like them - they were overloaded. I latched onto this issue because it was probably time to try. I already had Codex Pro, or whatever it is called, and I probably still had tokens left. The course management platform has a lot of issues that I have been clearing for a long time, and I noticed this one and remembered that we still had it. So, as an experiment, I just threw it at Codex and said: get to work, migrate all of this to Tailwind, show me what comes out. It did the migration, but I did not really like the result. So I started thinking about how I could approach this better.[^14][^15]

## Mockup first, then code

The approach I landed on was different from how I usually do front-end work. First, I asked ChatGPT to generate how the site should look. Then, based on those mockups - based on the image - I did the layout.[^4]

I remembered that people had started actively sharing the screenshots ChatGPT generated, and that GPT-5 really does this well. So I thought: what if I ask it to generate a design? After several iterations I got something fairly cute, something I liked. Then I told the agent: okay, here is our design idea, here is the desktop version, here is the mobile version, I want everything in this same style. It produced something similar, and I liked it.[^15]

So the loop is:

1. Describe to ChatGPT what kind of site I want and what should be on it
2. ChatGPT generates a mockup image of how the site should look
3. Hand that image to a code agent and ask it to implement the layout based on the picture

The mockup acts as the spec. Instead of describing the layout in words, the agent has the picture to match.

One thing I noticed while iterating with GPT-5: when you generate images, after a while it forgets about the screenshots you gave it. The first screenshot will not necessarily produce something similar, and that is fine. The idea is that when you ask ChatGPT to generate a screenshot or a design, you are just setting the direction - roughly how you want it to look. It will not look like the final product. You are using it to point the way, not to ship the exact pixels.[^15]

## Generating mockups per page

I asked ChatGPT to generate every photo. First I gave it a description of what was on the site, and then for each page I asked it to generate a web version and a mobile version.[^7]

I iterated on the pictures until I got something I liked. The course dashboard and the homework page each went through their own loop of "make it look like this, change that" until the mockup matched what I had in mind.

<figure>
  <img src="../assets/images/designing-with-ai/mockup-course-dashboard.jpg" alt="ChatGPT-generated mockup of the redesigned Data Engineering Zoomcamp 2026 dashboard with homework list and project submissions">
  <figcaption>One of the ChatGPT mockups for the course dashboard page - homework list with status pills and a projects section</figcaption>
  <!-- Shows what a generated mockup looks like before it goes to the code agent -->
</figure>

<figure>
  <img src="../assets/images/designing-with-ai/mockup-homework-mobile.jpg" alt="ChatGPT-generated mobile mockup of the redesigned Homework 1 page with multiple-choice questions">
  <figcaption>Mobile version of the homework page mockup - I asked ChatGPT for both desktop and mobile per page</figcaption>
  <!-- Shows that the per-page mockup loop produced both web and mobile variants -->
</figure>

## Choosing a design system

After playing with the mockups, I noticed a different problem: there was no consistent system. I had heard from designers I used to work with that they have design systems - reusable components and rules about how things should be laid out on a page.[^16]

So I told Codex: what if we pick a design system now? We have these mockups and a rough sense of where we are going, but the pages are all different and there is no single style. Let's make a design style. Codex said yes, we can make a design style, but what if we choose one that already exists? I said that was a great idea and asked it to think about which design system would suit us best. It proposed several, and in the end we chose GitHub.[^16]

I cannot say it turned out to be a copy of GitHub - if you look, it is not. But some things are traceable. The idea was that we took GitHub as a basis, took some of its design decisions (how buttons should look, how components should look), and prepared a design guidelines document. That document is how the agents should make decisions when they design a page.[^16]

<figure>
  <img src="../assets/images/designing-with-ai/mockup-homework-dark.jpg" alt="ChatGPT-generated dark-theme desktop mockup of the redesigned Homework 1 page">
  <figcaption>A dark-theme variant from the iteration loop - one of the style directions explored before the code agent picked up the final look</figcaption>
  <!-- Shows that iteration also covered different style directions, not just layout -->
</figure>

## Polishing the details in code

That was not the end of it - there was still a lot of work. But things were already better. From there I could open each page and say: I do not like this here, move this over there, too much padding here, too little there. Overall I liked the direction we were moving in, and what was left was only the details.[^20]

So how did I reach that direction? By generating the mockups first, then asking the agent to pick a design reference (GitHub in this case), then having it compose a design system specifically for our platform based on the best practices of existing companies, and only then opening each page to move elements around so it looked nice.[^20]

You can't make those pointwise changes through the mockup generator, because if you ask the screenshot tool to move a single element it redoes the whole screenshot. Targeted edits are very hard through a generator like that. The mockup sets the direction; the agent implements it; then you polish in code.[^8]

So the workflow that emerged is:

1. Generate mockups to fix the rough style direction.
2. Have the code agent build a site that more or less matches the mockup.
3. Have the agent pick a design reference and write a design-guidelines doc from it.
4. Polish the small details directly in the code.

<figure>
  <img src="../assets/images/designing-with-ai/redesigned-homepage.jpg" alt="Redesigned DataTalks.Club course management platform homepage showing Active Courses with LLM Zoomcamp 2026">
  <figcaption>The course management site after the redesign, with LLM Zoomcamp 2026 highlighted under Active courses</figcaption>
  <!-- The end result of the workflow on the original project - clean and consistent -->
</figure>

I have not finished the redesign - there is actually still a lot to change and many places I do not like. But the point is that the direction is there, the general look is one I like, and the design guidelines exist. What remains is to sit down and finish all the pages. The public pages already look more or less fine. What I still have to work on are the non-public pages of the course management platform. Overall I really like how it looks now - clean and neat.[^17]

## Applying the approach to other projects

Because I liked this approach so much, I started using it for other things, so that the code does not come out looking awful and the design is not an eyesore.[^17]

For the web I will not go into detail. The key point is that you do not even need screenshots. You can just tell the agent in the project: let's make a design system, which design system would suit our project best? The agent will propose some options, you pick one, and then you say: now let's document this. That alone already helps a lot - the interfaces it creates will be better and will need fewer changes.[^17]

With a screenshot it is even better, because you yourself will have an understanding of where the elements should go. The agent does not have to decide that, and you do not have to spend a long time moving everything around afterward. But screenshots generate slowly and moving individual elements through them is hard, so they are mostly there to set the direction. The agent implements it, and then you finish it off, saying what to change, where to put things, and what to fix.[^17]

## Applying it to an Android app: Pocket Shell

I started trying this approach on other apps too. Right now I am working on an app that lets me manage agents from my phone. I call it Pocket Shell. As soon as I reached the first level of functionality that more or less worked, the interface was so-so. I did the same thing: I said, look, here is our interface, I do not like it, I want to change it, let's pick a style. What helped was the same loop - I went to ChatGPT, said this is how I see it, let's implement this, and the implementation brought the interface closer to what I wanted.[^18]

<figure>
  <img src="../assets/images/designing-with-ai/pocketshell-before-conversation.jpg" alt="Pocket Shell agent conversation screen before the redesign">
  <figcaption>How Pocket Shell looked before - the agent conversation screen[^21]</figcaption>
  <!-- The starting point on the Android app, before applying the mockup-first approach -->
</figure>

<figure>
  <img src="../assets/images/designing-with-ai/pocketshell-before-projects.jpg" alt="Pocket Shell projects list before the redesign, with cramped boxed rows">
  <figcaption>How Pocket Shell looked before - the projects list</figcaption>
  <!-- The other "before" screen the user explicitly paired with the conversation view -->
</figure>

This took many iterations. The problem specifically with Android is feedback speed. For the web you can change something, reload the page, and immediately see the result - or, with Vite, even without a reload you see the elements move on screen in real time as you tell the agent what to change. With Android there is none of that.[^18]

What helped was a screenshot tool that lets you take a picture of any screen, so you do not have to go through the long fiddling with building an APK. It just produces a picture, and from that picture you can iterate much faster than before.[^18]

I had never written Android before, but now there was a need. The best part is that the things that work for web design also work for Android. My approach is the same: I generate some initial image myself to roughly figure out how it should look. Talking with ChatGPT helps me understand how I want the interface to look. It generates an image, I throw that image to the agents and say "implement this here", they implement it, and then I start moving the picture, the buttons, and so on, to get what I want.[^18]

<figure>
  <img src="../assets/images/designing-with-ai/pocketshell-mockup-conversation.jpg" alt="ChatGPT-generated mockup of the Pocket Shell conversation screen with a compose prompt">
  <figcaption>What I arrived at with ChatGPT after many iterations - the conversation screen mockup. <a href="https://chatgpt.com/s/m_6a270e24c37c8191ae0bd71fd2170434">The generation</a>.</figcaption>
  <!-- The generated target for the conversation screen - not the final product, just the direction -->
</figure>

<figure>
  <img src="../assets/images/designing-with-ai/pocketshell-mockup-projects.jpg" alt="ChatGPT-generated mockup of the Pocket Shell projects list with chevron expanders and a list/grid toggle">
  <figcaption>What I arrived at with ChatGPT for the projects list - cleaner hierarchy, more compact rows</figcaption>
  <!-- The generated target for the projects list, paired with the conversation mockup -->
</figure>

These mockups are not the final result - they are what I arrived at with ChatGPT to set the direction.[^19]

From there the code agent implemented the changes, and I polished from the picture - for example, refactoring the tree structure in the projects list to reduce vertical space and improve readability, focusing on visual hierarchy, indentation, and a compact layout.[^18]

<figure>
  <img src="../assets/images/designing-with-ai/pocketshell-implementation.jpg" alt="Coding agent debugging the Pocket Shell projects list implementation">
  <figcaption>The coding agent working through the implementation details after the mockup set the direction</figcaption>
  <!-- Illustrates the "agent implements, then you polish in code" step on the Android app -->
</figure>

<figure>
  <img src="../assets/images/designing-with-ai/pocketshell-result.jpg" alt="Pocket Shell projects list after the redesign, with a compact tree layout">
  <figcaption>The result now - still room for improvement (like removing the dots from everywhere), but this is the current state</figcaption>
  <!-- The implemented result on Android, closing the before/mockup/after arc -->
</figure>

## Sources

[^4]: [20260519_082455_AlexeyDTC_msg4175_transcript.txt](../inbox/used/20260519_082455_AlexeyDTC_msg4175_transcript.txt) - voice note on the mockup-first approach
[^7]: [20260519_085055_AlexeyDTC_msg4202_transcript.txt](../inbox/used/20260519_085055_AlexeyDTC_msg4202_transcript.txt) - voice note on asking ChatGPT for web and mobile versions of each page and iterating on the pictures
[^8]: [20260519_085551_AlexeyDTC_msg4204_transcript.txt](../inbox/used/20260519_085551_AlexeyDTC_msg4204_transcript.txt) - voice note on Codex turning the mockups into the site, then polishing small things in code with a style-guidelines doc
[^9]: [20260608_181334_AlexeyDTC_msg4469_transcript.txt](../inbox/used/20260608_181334_AlexeyDTC_msg4469_transcript.txt) - voice note framing the article: AI slop, being a non-designer, and his approach to design
[^10]: [20260608_181425_AlexeyDTC_msg4471_transcript.txt](../inbox/used/20260608_181425_AlexeyDTC_msg4471_transcript.txt) - voice note on GPT Image 2 generating designs and screenshots ("this is not a screenshot")
[^11]: [20260608_183324_AlexeyDTC_msg4485_transcript.txt](../inbox/used/20260608_183324_AlexeyDTC_msg4485_transcript.txt) - voice note on the generated Elon Musk screenshot example
[^12]: [20260608_181650_AlexeyDTC_msg4473_transcript.txt](../inbox/used/20260608_181650_AlexeyDTC_msg4473_transcript.txt) - voice note on the long-standing Tailwind migration issue
[^13]: [20260608_181745_AlexeyDTC_msg4475.md](../inbox/used/20260608_181745_AlexeyDTC_msg4475.md) - link to the Tailwind migration issue
[^14]: [20260608_182129_AlexeyDTC_msg4477_transcript.txt](../inbox/used/20260608_182129_AlexeyDTC_msg4477_transcript.txt) - voice note on the platform's Bootstrap history and throwing the issue at Codex as an experiment
[^15]: [20260608_183015_AlexeyDTC_msg4479_transcript.txt](../inbox/used/20260608_183015_AlexeyDTC_msg4479_transcript.txt) - voice note on generating designs with GPT-5, mockups setting direction, and it forgetting screenshots over time
[^16]: [20260608_183015_AlexeyDTC_msg4479_transcript.txt](../inbox/used/20260608_183015_AlexeyDTC_msg4479_transcript.txt) - voice note on choosing a design system, picking GitHub as a reference, and writing design guidelines
[^17]: [20260608_183601_AlexeyDTC_msg4487_transcript.txt](../inbox/used/20260608_183601_AlexeyDTC_msg4487_transcript.txt) - voice note on the unfinished state, applying the approach to other projects, and the design-system-without-screenshots variant
[^18]: [20260608_183921_AlexeyDTC_msg4489_transcript.txt](../inbox/used/20260608_183921_AlexeyDTC_msg4489_transcript.txt) - voice note on applying the approach to the Pocket Shell Android app and the screenshot-tool feedback loop
[^19]: [20260608_184726_AlexeyDTC_msg4503_transcript.txt](../inbox/used/20260608_184726_AlexeyDTC_msg4503_transcript.txt) - voice note that the Pocket Shell mockups are what he arrived at with ChatGPT, not the final result
[^20]: [20260608_183151_AlexeyDTC_msg4481_transcript.txt](../inbox/used/20260608_183151_AlexeyDTC_msg4481_transcript.txt) - voice note on opening each page to move elements and how the direction was achieved (mockups, design reference, design system, then polishing)
[^21]: [20260608_184455_AlexeyDTC_msg4497_transcript.txt](../inbox/used/20260608_184455_AlexeyDTC_msg4497_transcript.txt) - voice note: "these two pictures are how the app looked" (the Pocket Shell before screens), then he sent the ChatGPT-generated versions
[^22]: [20260609_072934_AlexeyDTC_msg4513_photo.md](../inbox/used/20260609_072934_AlexeyDTC_msg4513_photo.md) - screenshot with caption: AI likes to put these buttons on the right, so he corrects it to move them under
[^23]: [20260609_073226_AlexeyDTC_msg4515_photo.md](../inbox/used/20260609_073226_AlexeyDTC_msg4515_photo.md) - screenshot with caption: columns that sometimes make the UI too dense
[^24]: [20260609_073226_AlexeyDTC_msg4516_photo.md](../inbox/used/20260609_073226_AlexeyDTC_msg4516_photo.md) - screenshot: another page with the dense-column layout
[^25]: [20260609_074637_AlexeyDTC_msg4519_photo.md](../inbox/used/20260609_074637_AlexeyDTC_msg4519_photo.md) - screenshot with caption: typical AI design (the feature grid)
