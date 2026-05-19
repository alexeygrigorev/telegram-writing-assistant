---
title: "Redesigning the DataTalks.Club Course Platform with ChatGPT Mockups"
created: 2026-05-19
updated: 2026-05-19
tags: [design, chatgpt, codex, tailwind, course-platform, datatalks-club, ui]
status: draft
---

# Redesigning the DataTalks.Club Course Platform with ChatGPT Mockups

The design on the DataTalks.Club courses site is much nicer now.[^1][^2][^3] I want to write a post about how I got there, because the approach was different from how I usually do front-end work.[^6]

<figure>
  <img src="../assets/images/dtc-course-platform-redesign/redesigned-homepage.jpg" alt="Redesigned DataTalks.Club course management platform homepage showing Active Courses with LLM Zoomcamp 2026">
  <figcaption>The course management site after the redesign, with LLM Zoomcamp 2026 highlighted under Active courses</figcaption>
  <!-- The end result the post is about - shown up front so the reader sees what the workflow produced -->
</figure>

## Mockup first, then code

I used an interesting approach. First, I asked ChatGPT to generate how the site should look. Then, based on those mockups - based on the image - I did the layout.[^4]

ChatGPT now generates great screenshots. I can say: I want a site in this format, with this content, please make me a mockup. It does that very well, and the result looks beautiful.[^5]

So the loop is:

1. Describe to ChatGPT what kind of site I want and what should be on it
2. ChatGPT generates a mockup image of how the site should look
3. Hand that image to a code agent and ask it to implement the layout based on the picture

The mockup acts as the spec. Instead of describing the layout in words, the agent has the picture to match.

## What I ran it on

I used this approach to refresh the DataTalks.Club course management platform. I had a team of Codex agents working on moving the site to Tailwind and updating the visuals. The mockup-first step is what got the design itself moving - once ChatGPT produced a mockup I liked, the code agents had a concrete target to reproduce.

## Sources

[^1]: [20260519_082455_AlexeyDTC_msg4172.md](../inbox/used/20260519_082455_AlexeyDTC_msg4172.md) - "by the way, the design on the courses site has become nicer"
[^2]: [20260519_082455_AlexeyDTC_msg4173.md](../inbox/used/20260519_082455_AlexeyDTC_msg4173.md) - "should make a post about this"
[^3]: [20260519_082455_AlexeyDTC_msg4174.md](../inbox/used/20260519_082455_AlexeyDTC_msg4174.md) - "I mean a Substack article"
[^4]: [20260519_082455_AlexeyDTC_msg4175_transcript.txt](../inbox/used/20260519_082455_AlexeyDTC_msg4175_transcript.txt) - voice note on the mockup-first approach
[^5]: [20260519_082455_AlexeyDTC_msg4176_transcript.txt](../inbox/used/20260519_082455_AlexeyDTC_msg4176_transcript.txt) - voice note on ChatGPT generating clean mockups from a description
[^6]: [20260519_082512_AlexeyDTC_msg4182_transcript.txt](../inbox/used/20260519_082512_AlexeyDTC_msg4182_transcript.txt) - voice note asking for a new article about the course management platform UI redesign
