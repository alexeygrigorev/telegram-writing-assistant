---
title: "Microphone Booster App"
created: 2026-02-13
updated: 2026-02-13
tags: [vibe-coding, rust, tauri, glm-5, opencode]
status: draft
---

# Microphone Booster App

A Windows microphone booster built with OpenCode and GLM-5 using Tauri + Rust. Solves the problem of quiet USB-C microphones that the built-in Windows booster does not support.

Code: https://github.com/alexeygrigorev/microboost/[^6]

## The problem

At home I use regular headphones for recording and the sound is okay, though some people have complained about it in YouTube videos. The built-in Windows microphone booster works with headphones plugged into the audio jack port, but it does not boost as much as I would like. And it does not work at all with USB-C devices. I wanted a more universal solution[^1].

When recording away from home, I use Apple earbuds with a USB-C connector. They have a good microphone - much better than my laptop's built-in microphone - but the audio comes out too quiet[^1].

Today was exactly this situation - I needed to record a video, was not at home, and only had my Apple earbuds. I decided to try writing a booster app to see what happens[^1].

## Building with GLM-5

I asked OpenCode with GLM-5 to implement it. I said I do not care about the technology, so it chose Rust with Tauri 2.0 and Svelte for the UI[^2].

<figure>
  <img src="../assets/images/microphone-booster-app/microboost-plan.jpg" alt="OpenCode plan for Microboost app using Tauri 2.0, Rust, and Svelte">
  <figcaption>GLM-5 chose Rust with Tauri 2.0 and Svelte for the microphone booster</figcaption>
  <!-- Shows the architecture plan with src-tauri for Rust backend and Svelte frontend -->
</figure>

## Three attempts to get it right

The microphone booster works well, but it took three attempts to get there[^3].

First attempt: GLM-5 built a complex application with some kind of browser engine inside. It used Svelte for the interface - which I did not notice at first, it is right there in the plan screenshot. The UI looked mediocre and the app was heavy. Worse, it completely forgot about the booster requirement and just made a sound recording app. And even that did not work - when I pressed record, it would record something, but the resulting file played back 100 times slower than the actual recording. It did not account for any of my requirements - just made something with a record button[^3].

I told it to rewrite everything. It said that making a microphone booster is too complex and it cannot figure out how to do it[^3].

On the third attempt, it rewrote everything from scratch and it worked well. The booster worked, the recording worked. There were a couple of small issues I asked it to fix, but overall I was satisfied[^3].

I had to intervene - I was hoping it would work on the first try. Despite GLM-5 being the new model that is supposed to be impressive, things were not as rosy as expected[^3].

## The good outcome

The app ended up working well. It uses native Windows APIs. The best part is that I now know this technology stack - Tauri + Rust - and can use it to build GUI applications for Windows. These apps are self-contained - no libraries, no .NET, nothing else needed. They just work out of the box[^3].

## FFmpeg wrapper use case

This is relevant because I had a case where I needed to make a tool for a DataTalks Club team member who is a community manager, not a developer. She needs to run FFmpeg commands, which is not easy even for me - FFmpeg is complex and it is easy to make mistakes with parameters. A GUI is much better for this[^4].

I previously tried building an FFmpeg wrapper in Python GUI and with .NET, but neither was straightforward - guessing the right .NET version and other issues. Now with Rust, I have hope that I can build self-contained GUI apps quickly. I plan to make an FFmpeg wrapper for her so she can just paste a video link and cut/trim videos more easily[^4][^5].

Right now she has to write FFmpeg commands herself and run them. Even I would not want to do that - I would write some wrapper in Python, because FFmpeg is complex and it is easy to make a mistake with a parameter or copy the wrong thing. A GUI is much better for this kind of work[^5].

## Sources

[^1]: [20260213_143859_AlexeyDTC_msg1604_transcript.txt](../inbox/used/20260213_143859_AlexeyDTC_msg1604_transcript.txt)
[^2]: [20260213_100439_AlexeyDTC_msg1599_photo.md](../inbox/used/20260213_100439_AlexeyDTC_msg1599_photo.md)
[^3]: [20260213_143306_AlexeyDTC_msg1601_transcript.txt](../inbox/used/20260213_143306_AlexeyDTC_msg1601_transcript.txt)
[^4]: [20260213_143624_AlexeyDTC_msg1602_transcript.txt](../inbox/used/20260213_143624_AlexeyDTC_msg1602_transcript.txt)
[^5]: [20260213_143701_AlexeyDTC_msg1603_transcript.txt](../inbox/used/20260213_143701_AlexeyDTC_msg1603_transcript.txt)
[^6]: [20260213_182141_AlexeyDTC_msg1645.md](../inbox/used/20260213_182141_AlexeyDTC_msg1645.md) - GitHub repository link
