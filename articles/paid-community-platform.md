---
title: "Paid Community Platform Requirements"
created: 2026-02-18
updated: 2026-02-18
tags: [community, platform, ghost, courses, infrastructure]
status: draft
---

# Paid Community Platform Requirements

Technical requirements and platform evaluation for hosting the AI Shipping Labs paid community at aishippinglabs.com. This covers what features are needed, what platforms were considered, and the current state of the discussion.

## Current Setup

The community site is live at [aishippinglabs.com](https://aishippinglabs.com). It is currently invite-only and positions itself as a "technical community for action-oriented builders interested in AI engineering and AI tools." The tagline is "Turn AI ideas into real projects"[^9].

Current tier structure on the site[^9]:

- Basic (200 EUR/year) - content only. Substack content access, tutorials, tool breakdowns, research, curated social posts. No community access.
- Main (500 EUR/year) - live learning + community. Everything in Basic plus closed community access, group coding sessions, hackathons, guided project-based learning, career discussions, personal brand guidance, topic voting.
- Premium (1000 EUR/year) - courses + personalized feedback. Everything in Main plus access to all mini-courses, upcoming Python for Data and AI Engineering course, resume/LinkedIn/GitHub teardowns, mini-course topic voting.

## Platform Requirements

### Access Control by Tier

The platform needs to differentiate access between the three tiers[^4]:

- Basic members: receive content by email only. No community access. Tutorials, examples, and materials are sent by email. All members (Basic, Main, and Premium) can receive these mailings.
- Main members: community access plus everything in Basic. They can view materials on the site, but materials should be gated between tiers.
- Premium members: access to everything including mini-courses and voting on course topics.

Materials on the site should be access-controlled between plans. Basic has access to certain materials, Main to others, and Premium to all[^4].

### Events and Calendar

Events should be tier-differentiated[^4]:

- Some events accessible to everyone (to attract new people)
- Some events only for Premium
- Some events for Premium + Main
- Some events for Premium + Main + Basic
- Basic probably will not have many events, but the differentiation should be possible

A calendar is needed, ideally with integration with Luma. Luma already has calendar features and it could avoid reimplementing this. There may be a paid Luma plan with API features that would be useful[^4].

Ideally: a button to create an event, everything gets set up automatically, and after the event it records and gets posted to the platform. This is how Maven works now - press a button, everything is created, then it auto-records and publishes[^4].

### Course Hosting

Courses are a core Premium feature. The platform needs[^4]:

- A course catalog visible to all users
- People not subscribed can see the courses but get a "Join" button that leads to Premium signup
- Inside a course: modules and units
- Each unit can have video, text content, and homework
- Cohort support should be considered (whether to run cohorts or not). Can add cohort functionality in advance to make future implementation easier

One idea: host all courses on a private GitHub repository. The course catalog shows what is available, and the actual content lives on GitHub[^4].

### Video Hosting

Ghost does not allow hosting large videos in the current subscription tier. The recommendation is to use specialized services like YouTube with unlisted/private links[^3][^5].

This is actually similar to how the Maven course works - videos are recorded on YouTube and then shared via private links with students[^5].

The platform needs to support both video and text content[^3b].

### Email and Newsletters

Need the ability to send emails to all members. Announcements in Slack, in newsletters, and potentially a Telegram channel[^4].

If building a custom platform, emails can be sent through Amazon Simple Email Service (SES). This requires some setup but is doable[^6].

### Ghost as Platform

Ghost has login functionality and closed content sections accessible only to members on specific plans. The question is whether Ghost is sufficient out of the box or if custom development is needed[^3].

<figure>
  <img src="../assets/images/paid-community-platform/ghost-forum-course-hosting.jpg" alt="Ghost forum post discussing whether Ghost is suitable for hosting online courses">
  <figcaption>Ghost community discussion on using Ghost for course hosting - recommends Podia as alternative</figcaption>
  <!-- Screenshot from Ghost forum showing user feedback on Ghost's suitability for course hosting -->
</figure>

<figure>
  <img src="../assets/images/paid-community-platform/ghost-forum-ghost-vs-podia.jpg" alt="Ghost forum post comparing Ghost and Podia for online courses">
  <figcaption>Another Ghost community member describing their hybrid model using Ghost for subscriptions and Podia for standalone courses</figcaption>
  <!-- Screenshot from Ghost forum showing a user who uses both Ghost and Podia for different purposes -->
</figure>

According to Ghost community feedback (from 2021, but the platform has not changed drastically)[^5]:

- For standalone courses with different prices per course - Ghost is not ideal
- For putting content behind a paywall with subscription pricing (monthly or paid) - Ghost works, but its focus is on "creators" (publishers, podcasters, journalists, bloggers) with membership/subscription-driven sites
- Podia was recommended as a better fit for standalone course hosting
- For a hybrid model (half-way between online course and newsletter) with paid subscribers and free content for free subscribers - Ghost can work

In our case, since the goal is to use a subscription model with mini-courses for community members (not standalone course purchases), Ghost could work. The main limitation is video hosting in our tier[^5].

### Ghost LMS Theme

There is a Ghost theme specifically designed for learning management: [Ghost Learning Management System theme](https://explore.ghost.org/p/ghost-learning-management-system). This could potentially be integrated as part of the site alongside other content[^7].

The theme is made by Themeix and turns a standard Ghost site into a course platform. It provides course catalog pages, course detail pages with structured lesson sidebars, and individual lesson pages with breadcrumb navigation. Courses are organized using Ghost's tag system, and access is gated through Ghost's native membership tiers.

What it does well:
- Course catalog with category browsing
- Structured lesson navigation within courses
- Membership gating using Ghost's built-in tiers
- Blog section alongside courses
- Responsive design, three homepage variants

What it lacks:
- No quizzes, assessments, or grading
- No progress tracking or completion status
- No certificates
- No video hosting (text-based lessons only, though videos can be embedded manually)
- No per-course pricing - access is all-or-nothing based on Ghost tier
- Course structure is manually maintained through Ghost tags
- Third-party theme, so long-term maintenance depends on developer

### Maven Evaluation

Maven is convenient as a course platform with a lot of built-in functionality. The issue is student registration automation. There does not seem to be an API for adding students programmatically. Payment would go through our platform, then a webhook should fire, and we would add the student to the Maven course. There appears to be only a manual way to add students, not an API for it[^8].

Can check in the Maven community or search further, but it seems Maven is not the right fit. On the other hand, all the needed functionality could be coded with Claude Code in about 2 hours[^8].

### Valeria's Platform Research

Valeria explored platform requirements in a [ChatGPT conversation](https://chatgpt.com/share/6995e377-ca94-8013-afab-c44b21967400)[^5b]. The key findings:

Ghost was selected as the recommended platform. The architecture: Ghost acts as CMS, membership system, payment integration (via Stripe), email capture engine, newsletter sender, and content gating layer. Ghost themes (Handlebars templates) provide layout and SEO control, developed in an IDE like normal code. Slack remains the community platform. Local development is possible (ghost install local), similar to standard web development workflow[^5b].

Specific feature requirements discussed:
- Workshop pages with video embeds, clickable timestamps, tools used, learning outcomes, and resource lists
- Resource directory displayed as a grid of tools/courses/models with external links
- Recording library with gated archives based on tier
- Tag-based content organization using internal tags (#resource, #workshop, #recording, #article)
- Custom structured data (JSON-LD, schema markup, OpenGraph) for SEO
- Tag-based conditional components (e.g., "if article is tagged ai-engineer, show roadmap signup form")
- Content gating by tier
- Lead magnet flow: user enters email, becomes free member, download is unlocked
- Downloadable resources (PDFs, templates, slides, code bundles) gated behind email signup or paid membership
- Reusable signup/download CTAs that can be embedded across multiple related articles

Acknowledged limitations of Ghost:
- No true custom content types or database fields (simulated through tags and structured content blocks)
- Not a React app runtime (server-rendered Handlebars templates with optional JS)
- Not suitable for app-like dashboards, learning progress tracking, or heavy automation pipelines
- Roughly 80% flexibility compared to a fully custom system, but with much faster launch

### Building Custom

After listing all the requirements, the conclusion is that finding everything in one platform is unrealistic. Would need Luma, Maven, Ghost, and everything to work together. It might be simpler to build and host everything ourselves[^6].

Estimated hosting cost: about 50 EUR. The issue is with emails, but Amazon SES can handle that. An admin interface would be needed for managing these things. Building an admin interface, connecting email sending, setting up course hosting - with Claude Code and with Valeria's help, this is doable in about a week[^6].

This is not rocket science to implement. If dedicated time is allocated (one week), everything can be built. With Claude Code help, it is realistic[^6].

## Next Steps

1. Document all the features needed (this article)
2. Evaluate what Ghost can and cannot do out of the box
3. Decide whether to use Ghost + custom code, or build everything from scratch
4. If custom: estimate the development effort for an MVP

## Sources

[^3]: [20260218_155901_AlexeyDTC_msg1951_transcript.txt](../inbox/used/20260218_155901_AlexeyDTC_msg1951_transcript.txt)
[^3b]: [20260218_155901_AlexeyDTC_msg1952_transcript.txt](../inbox/used/20260218_155901_AlexeyDTC_msg1952_transcript.txt)
[^3c]: [20260218_155901_AlexeyDTC_msg1953_transcript.txt](../inbox/used/20260218_155901_AlexeyDTC_msg1953_transcript.txt)
[^4]: [20260218_160548_AlexeyDTC_msg1963_transcript.txt](../inbox/used/20260218_160548_AlexeyDTC_msg1963_transcript.txt)
[^5]: [20260218_160224_valeriia_kuka_msg1961_transcript.txt](../inbox/used/20260218_160224_valeriia_kuka_msg1961_transcript.txt)
[^5b]: [20260218_160718_valeriia_kuka_msg1965.md](../inbox/used/20260218_160718_valeriia_kuka_msg1965.md)
[^6]: [20260218_161001_AlexeyDTC_msg1970_transcript.txt](../inbox/used/20260218_161001_AlexeyDTC_msg1970_transcript.txt)
[^7]: [20260218_161001_AlexeyDTC_msg1969.md](../inbox/used/20260218_161001_AlexeyDTC_msg1969.md)
[^8]: [20260218_160725_AlexeyDTC_msg1967_transcript.txt](../inbox/used/20260218_160725_AlexeyDTC_msg1967_transcript.txt)
[^9]: [20260218_161244_AlexeyDTC_msg1975.md](../inbox/used/20260218_161244_AlexeyDTC_msg1975.md), [aishippinglabs.com](https://aishippinglabs.com)
[^10]: [20260218_161109_AlexeyDTC_msg1973_transcript.txt](../inbox/used/20260218_161109_AlexeyDTC_msg1973_transcript.txt)
[^11]: [20260218_160017_valeriia_kuka_msg1957_photo.md](../inbox/used/20260218_160017_valeriia_kuka_msg1957_photo.md)
[^12]: [20260218_160017_valeriia_kuka_msg1958_photo.md](../inbox/used/20260218_160017_valeriia_kuka_msg1958_photo.md)
