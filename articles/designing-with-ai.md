---
title: "Approaching Design with AI as a Non-Designer"
created: 2026-05-19
updated: 2026-06-09
tags: [design, chatgpt, codex, tailwind, course-platform, datatalks-club, pocketshell, ui]
status: draft
---

# Approaching Design with AI as a Non-Designer

You can usually tell when a website was created by AI. It tends to happen with "one-shot designs": you tell the coding assistant to create a website. When you open it, you can see right away that it's AI-generated.[^9]

A lot of the time that is completely fine. For a simple website, one-shot is more than enough, and it's way better than I could ever design myself.

The problems start when you don't want something generic. There are thousands of websites now that all look the same. In writing we have markers like "delve" or excessive bold formatting that give away AI-generated text. In design there are similar elements you notice immediately.[^9]

One-shot designs also get hard to use. They tend to grow overly complex, with elements not always where I'd expect them. And it compounds. Each new page you build on brings elements that don't match the rest. Eventually the whole thing becomes messy.[^9]

I am not a designer. I do not claim to be one, and I never liked front-end or design work. But I build a lot of user-facing tools now, both web and mobile. I want them to look nice and clean, with elements placed logically.

This article is about how I approach designing with AI as a non-designer. I use AI tools to get something that looks pleasant and not generic, instead of AI slop.[^9]

## The design elements that give AI away

When I say AI design has characteristic elements, I mean specific habits. They are the ones I keep running into and correcting.

The most obvious one is the layout I think of as typical AI design: the feature grid. Every cell has an icon, a title, a short blurb, and a highlighted left border.[^25]

<figure>
  <img src="../assets/images/designing-with-ai/ai-feature-grid.jpg" alt="Marketing feature grid with four cells, each with an icon, a title, and a short description">
  <figcaption>Typical AI design - the icon-title-blurb feature grid</figcaption>
  <!-- The generic feature-grid pattern the user points at as the characteristic AI look -->
</figure>



Another is button placement. AI likes to cram the action buttons tightly on the right, as if the page had no room for them. I have to move them down and give them space instead.[^22]

<figure>
  <img src="../assets/images/designing-with-ai/ai-buttons-on-right.jpg" alt="Event series page with action buttons lined up on the right side">
  <figcaption>The buttons get crammed on the right by default - I give them room below</figcaption>
  <!-- Concrete example of the button-placement tic the user keeps correcting -->
</figure>

The same happens with layout. AI tends to reach for column layouts even where they are not necessary. That crowds everything together and makes the UI too dense.[^23][^24]

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

## My own designs are not much better

I am not a designer, and you can see it in the things I have built myself. When I need to design something, it comes out functional but not sleek. Take the main DataTalks.Club website. I put it together in 2020. It did the job, but it is plainly not the work of a designer.

<figure>
  <img src="../assets/images/designing-with-ai/dtc-main-website-2020.png" alt="The original DataTalks.Club website from 2020 - a plain, functional layout">
  <figcaption>The main DataTalks.Club website I built in 2020 - functional, but clearly not the work of a designer</figcaption>
  <!-- The user's own pre-AI design work, establishing the non-designer baseline before the redesign story -->
</figure>

The course management platform was the same story. Before it, I ran everything on Google Forms, spreadsheets, and a pile of custom Python scripts. That had become hard to manage, so I built the platform to replace it. It just replicated the process I already had, but made it easier to run.

I started it in 2023 and launched the first course on it in January 2024. I built it with Django and Bootstrap, the tools I already knew. AI helped along the way. It worked and had all the functionality, but it looked like this.[^14]

<figure>
  <img src="../assets/images/designing-with-ai/dtc-cmp-first-version.png" alt="The first version of the DataTalks.Club course management platform, a plain Bootstrap layout">
  <figcaption>The first version of the course management platform (<a href="https://web.archive.org/web/20240420184858/http://courses.datatalks.club/">Wayback Machine</a>) - functional, the same plain look</figcaption>
  <!-- The CMP before the redesign, the starting point for the story that follows -->
</figure>

For a long time that was fine. The platform did its job, and styling was never the priority.

## Throwing it at Codex

In November 2024, one of the students filed an issue: migrate the site to Tailwind. I had no time for it, so it just sat there untouched, like plenty of other issues.[^12]

That issue is [github.com/DataTalksClub/course-management-platform/issues/76](https://github.com/DataTalksClub/course-management-platform/issues/76).[^13]

I only got to it in 2026. By then I had coding agents like Codex on plans where the tokens reset on a schedule. I wanted to use mine up before the reset day. I had been clearing the platform's issues for a long time, and this one was still sitting there. So I picked it up.

I had heard Tailwind was a more modern system than Bootstrap, but I did not know it myself. There had been redesign attempts from other people before, and I did not like them. They were overloaded. Still, it was probably time to try.

As an experiment, I threw it at Codex and told it to migrate everything to Tailwind. It did the migration, but I did not like the result. So I started thinking about how I could approach this better.[^14][^15]

## ChatGPT can generate designs

Around that time, GPT Image 2 came out, and it changed how I thought about all this. On Twitter people started posting screenshots with the caption "this is not a screenshot". This part of GPT had become good at generating designs. It can reproduce almost any design. You can ask it for a WhatsApp window or a Telegram window, and it does it easily.[^10]

Here is how well it does it. I sent ChatGPT a screenshot of my own Telegram and asked for the same conversation, but with Elon Musk. It reproduced it. The screenshot will not surprise anyone now, but GPT Image 2 is genuinely good. It generates great images, including screenshots and designs. The results can look genuinely beautiful.[^11]

<figure>
  <img src="../assets/images/designing-with-ai/generated-screenshot-elon-musk.jpg" alt="ChatGPT-generated screenshot of a WhatsApp conversation with Elon Musk">
  <figcaption>A generated screenshot - I sent ChatGPT a screenshot of my Telegram and asked for the same conversation with Elon Musk.</figcaption>
  <!-- Concrete proof of how well the image model reproduces a real app's look, which the whole mockup-first approach relies on -->
</figure>

So the next thought was simple. Instead of describing the redesign to a coding agent in words, I could show it a picture.

## Mockup first, then code

The approach I landed on was different from how I usually do front-end work. First, I asked ChatGPT to generate how the site should look. Then I built the layout from those mockups.[^4]

After several iterations I got something fairly cute, something I liked. Then I gave the agent the design idea, both the desktop and mobile versions. I asked it to build everything in that same style. It produced something similar, and I liked it.[^15]

So the loop is:

1. Describe to ChatGPT what kind of site I want and what should be on it
2. ChatGPT generates a mockup image of how the site should look
3. Hand that image to a code agent and ask it to implement the layout based on the picture

The mockup acts as the spec. Instead of describing the layout in words, the agent has the picture to match.

I noticed one thing while iterating with GPT-5. After a while, it forgets the screenshots you gave it. The first screenshot will not necessarily produce something similar, and that is fine. When you ask ChatGPT for a screenshot or a design, you are just setting the direction. It shows roughly how you want it to look, not the final product. You are using it to point the way, not to ship the exact pixels.[^15]

## Generating mockups per page

I asked ChatGPT to generate every photo. First I gave it a description of what was on the site. Then, for each page, I asked it to generate a web version and a mobile version.[^7]

I iterated on the pictures until I got something I liked. The course dashboard and the homework page each went through their own loop. I kept saying "make it look like this, change that" until the mockup matched what I had in mind.

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

After playing with the mockups, I noticed a different problem: there was no consistent system. I had heard from designers I used to work with that they have design systems. A design system is reusable components plus rules for how things should be laid out on a page.[^16]

So I told Codex we should pick a design system now. We had the mockups and a rough sense of direction. But the pages were all different, with no single style. Codex suggested we choose one that already exists instead of inventing our own. I thought that was a great idea and asked it to propose the best fit. It suggested several, and in the end we chose GitHub.[^16]

I cannot say it turned out to be a copy of GitHub - if you look, it is not. But some things are traceable. We took GitHub as a basis. We borrowed some of its design decisions, like how buttons and components should look. From that we wrote a design-guidelines document. That document is how the agents make decisions when they design a page.[^16]

<figure>
  <img src="../assets/images/designing-with-ai/mockup-homework-dark.jpg" alt="ChatGPT-generated dark-theme desktop mockup of the redesigned Homework 1 page">
  <figcaption>A dark-theme variant from the iteration loop - one of the style directions explored before the code agent picked up the final look</figcaption>
  <!-- Shows that iteration also covered different style directions, not just layout -->
</figure>

## Polishing the details in code

That was not the end of it - there was still a lot of work. But things were already better. From there I could open each page and say what I wanted changed. Move this here, drop some padding there, that kind of thing. Overall I liked the direction we were moving in, and what was left was only the details.[^20]

You can't make those pointwise changes through the mockup generator. If you ask the screenshot tool to move a single element, it redoes the whole screenshot. Making targeted edits is hard that way.

The mockup sets the direction, the agent implements it, and you polish in code.[^8]

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

I have not finished the redesign. There is still a lot to change and many places I do not like. But the direction is there, the general look is one I like, and the design guidelines exist. What remains is to sit down and finish all the pages.

The public pages already look more or less fine. What I still have to work on are the non-public pages. Overall I like how it looks now. It is clean and neat.[^17]

## Applying the approach to other projects

I liked this approach so much that I started using it for other things. That way the code does not come out looking awful, and the design is not an eyesore.[^17]

For the web I will not go into detail. You do not even need screenshots. You can just tell the agent to set up a design system. Ask which one would fit the project best.

It proposes some options, you pick one, and then you have it document the choice. That alone helps a lot. The interfaces it creates are better and need fewer changes.[^17]

With a screenshot it is even better, because you already know where the elements should go. The agent does not have to decide that. You also do not spend a long time moving everything around afterward.

But screenshots generate slowly, and moving individual elements through them is hard. So they are mostly there to set the direction. The agent implements it. Then you finish it off in code, telling it what to change and where.[^17]

## Applying it to an Android app: Pocket Shell

I started trying this approach on other apps too. Right now I am working on an app that lets me manage agents from my phone. I call it Pocket Shell. As soon as I reached the first level of functionality that more or less worked, the interface was so-so.

I did the same thing as before. I told the agent I did not like the interface and wanted to change it. We picked a style together.

The same loop helped. I went to ChatGPT, described how I saw it, and had it implement that. The result came closer to what I wanted.[^18]

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

This took many iterations. The problem with Android is feedback speed. On the web you change something, reload the page, and see the result immediately. With Vite you do not even need to reload. The elements move on screen as you tell the agent what to change. With Android you get none of that.[^18]

What helped was a screenshot tool that takes a picture of any screen. That way I did not have to fiddle with building an APK each time. It just produces a picture, and from there I can iterate much faster than before.[^18]

I had never written Android before, but now I needed to. What works for web design also works for Android. My approach is the same.

I generate an initial image myself to figure out roughly how it should look. Talking with ChatGPT helps me work out how I want the interface to look. It generates an image, I hand it to the agents, and they implement it. Then I move the layout and buttons around until it looks the way I want.[^18]

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

From there the code agent implemented the changes, and I polished from the picture. For example, I refactored the tree structure in the projects list to reduce vertical space and improve readability. I focused on visual hierarchy, indentation, and a compact layout.[^18]

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

## Better than one-shotting it

Both problems from the start of this article come from the same move. You hand the whole design to AI in one shot and accept what comes back. This approach splits that move apart.

Generating a mockup first deals with the visual half. I decide what the page should look like and hand the agent a picture to match. That way it does not fall back on the feature grid, the right-side buttons, or the dense columns. I set the direction, not the model. That is also what keeps it from looking like every other one-shot site.

The design system deals with the other half: the part where everything rots as you keep building on it. Once there is a guidelines document, every new page follows the same rules. The site stays consistent instead of drifting into a mess one screen at a time.

And none of this is specific to the DTC platform, or even to the web. The same loop took an Android app I had no idea how to design. It turned that into something I would actually want to use. I am still not a designer. But this is how I get a result that looks pleasant and not generic, instead of slop.

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
