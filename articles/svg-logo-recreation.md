---
title: "Recreating a PNG Logo as SVG with Claude Code"
created: 2026-02-25
updated: 2026-02-26
tags: [claude-code, opencv, svg, design]
status: draft
---

# Recreating a PNG Logo as SVG with Claude Code

This week I spent time trying to convert a PNG logo (made for a website) into an SVG. It started as a kind of procrastination but turned into an interesting experiment with different approaches[^1].

## The Problem

We have new websites and I wanted to add an icon - a nice-looking logo. Besides the website, there is also Slack and other places where this logo could be useful. So I decided to make something proper[^3].

I took two screenshots of what was on the website and gave them to ChatGPT to generate a logo based on those screenshots. It generated one. I showed it to Valera, she said let's tweak it a bit. On the second iteration it was more or less OK[^3].

But ChatGPT generates PNG. I wanted a vector image - SVG - so the logo could scale to any size, be used anywhere, and take up less space. This problem is similar to what I tried to solve before when converting certificates from images to HTML/CSS[^3].

<figure>
  <img src="../assets/images/svg-logo-recreation/original-logo-chatgpt.jpg" alt="Original rocket logo generated with ChatGPT">
  <figcaption>The original PNG logo generated with ChatGPT - the target to recreate</figcaption>
  <!-- This is the reference image that all SVG conversion attempts try to match -->
</figure>

## First Attempts

The first attempt was to ask ChatGPT directly to make the SVG. It thought for 3 minutes and produced something completely incoherent. Then it thought for 5 minutes and produced something even worse[^3].

I thought the problem was lack of feedback - no way to iterate. I told Claude: convert the PNG to SVG, render the SVG back to PNG, look at it, and try to match the original. Keep iterating until it works. But the result was terrible - even worse than ChatGPT[^1][^3].

<figure>
  <img src="../assets/images/svg-logo-recreation/claude-code-svg-attempt.jpg" alt="SVG created directly by Claude Code">
  <figcaption>SVG created directly by Claude Code - not close enough</figcaption>
  <!-- First attempt at having Claude Code generate SVG directly from the image -->
</figure>

Then I started googling "PNG to SVG transformation" and found an Adobe service where you can upload an image and it converts to SVG. The result was fairly large and looked a bit strange, but at least it was SVG. I thought the Adobe SVG probably has approximation artifacts, and if I clean it up with Claude, I should get what I need. That also did not produce anything good[^1][^3].

## The OpenCV + Potrace Approach

Before googling more, I had the idea that Claude needs help finding the anchor points in the image - based on those, create the SVG and then compare. I imagined how I would do it manually: open Inkscape, remove some anchor points from the curves, try to make them smoother. I told Claude: use OpenCV, do it that way. Claude installed OpenCV (I did not have it) and started working on it. I told it to simplify anchor points and smooth curves like I would in Inkscape, but that did not produce good results either[^3].

At this point I was ready to give up and just use PNG. But then I decided to ask ChatGPT how people actually convert PNG to SVG. It gave many options, and one of them was OpenCV - the same conclusion I had already reached on my own. It also mentioned Inkscape - a tool I had also found independently. ChatGPT even wrote actual conversion code, step by step[^3].

I also found potrace, which produces better bezier curves. The combination of potrace and OpenCV gives decent results[^1].

<figure>
  <img src="../assets/images/svg-logo-recreation/opencv-potrace-approach.jpg" alt="Result using Claude + OpenCV + potrace">
  <figcaption>Result using the Claude + OpenCV + potrace approach</figcaption>
  <!-- Intermediate result from the automated contour tracing pipeline -->
</figure>

## Iterative Refinement Strategy

I also needed to control the process. I told Claude: look, the result is decent but there is still a lot of pixelation. I asked it to make a plan and focus on one detail at a time - first fix the background, then fix the circles, then fix the exhaust trails from the rocket, then fix something else. One by one, so the end result would be good[^1].

It had been working for about 30 minutes and the result still was not great, but it was getting close[^1].

<figure>
  <img src="../assets/images/svg-logo-recreation/attempt-035.jpg" alt="Iteration 35 of the SVG recreation">
  <figcaption>attempt_035.svg - getting closer after 35 iterations</figcaption>
  <!-- After many iterations of the one-detail-at-a-time approach -->
</figure>

## Second Approach - Full Reproduction

I decided to try a second attempt from scratch. I took the code ChatGPT wrote and gave it to Claude: forget everything we did before and try reproducing the image using this code. I also upscaled the original PNG to 1024x1024 first - working from a larger image instead of a small one also helped[^3].

Claude could not get ChatGPT's code running, so it rewrote everything in pure OpenCV. And it worked - Claude segmented the image into pieces, converted each piece to SVG, then assembled everything into one image. It simplified shapes, found circles that could just be replaced with a `<circle>` element. Initially the result was angular, but then at some iteration I noticed Claude started creating Python files - it shifted from writing SVG by hand to writing Python scripts that generate the SVG files[^3]. After 16 iterations, it reached MSE ~97 (1.4% mean pixel error)[^2].

<figure>
  <img src="../assets/images/svg-logo-recreation/final-result-iter016.jpg" alt="Final SVG result after 16 iterations">
  <figcaption>reproduce/iter_016.svg - the final result with 1.4% pixel error</figcaption>
  <!-- The final result from the second, more systematic approach -->
</figure>

<figure>
  <p>Video: Screen recording of building the SVG logo - <a href="https://t.me/c/3688590333/2471">View on Telegram</a></p>
  <figcaption>Building the SVG logo</figcaption>
  <!-- Time-lapse of the iterative SVG recreation process -->
</figure>

<figure>
  <video src="../assets/images/svg-logo-recreation/second-attempt-progress.mp4" controls>
    Video of PNG to SVG translation - second attempt
  </video>
  <figcaption>Progress recording of the second PNG to SVG conversion attempt</figcaption>
  <!-- Shows the iterative improvement during the second approach using OpenCV -->
</figure>

## Technical Details

The process Claude followed[^2]:

1. Started with a potrace-based PNG-to-SVG script. pypotrace failed to install (missing libagg), so Claude swapped in OpenCV contour tracing (cv2.findContours + cv2.approxPolyDP) - same preprocessing, different tracing backend

2. Traced the image into 9 contours and identified each one by rendering them individually: rounded rectangle, rocket body, window cutout, 3 exhaust trails, 2 particle dots, 1 window dot

3. Assembled the SVG layer by layer (iter_001-006), assigning colors to each contour based on its role in the hierarchy (yellow background, black shapes, yellow cutouts)

4. Smoothed the polygon paths using Catmull-Rom splines (iter_007-009). Found that smoothing all shapes distorted the rectangle, so applied it selectively to organic shapes only

5. Precision-tuned colors by sampling exact pixel values from the original (iter_012), added a subtle background glow via SVG filter (iter_013-016), and used pixel-level MSE + diff heatmaps to guide each refinement

## What Worked

- OpenCV contours as a drop-in replacement for potrace
- Ultra-fine polygon approximation (epsilon_frac=0.0003) for shape accuracy
- SVG circle elements (via cv2.minEnclosingCircle) for perfectly round dots
- Median of multiple pixel samples for robust color extraction

## What Did Not Work

- pypotrace - would not build without libagg
- Smoothing all shapes uniformly - distorted the rectangle's straight edges
- Catmull-Rom bezier smoothing in general - looks nicer visually but increased MSE from 97 to 130
- SVG glow filter - barely moved MSE (98.0 to 97.8); the original's glow is too subtle to replicate well

## Bottom Line

The remaining 1.4% error is almost entirely edge anti-aliasing - an inherent difference between how cairosvg rasterizes SVG paths versus how the original image was rendered. The shapes, colors, and layout match[^2].

I spent a disproportionate amount of time on this, but I enjoyed the process. I am not sure how reproducible this approach is with other images, but this particular logo was fairly simple[^3].

## Sources

[^1]: [20260225_202646_AlexeyDTC_msg2455_transcript.txt](../inbox/used/20260225_202646_AlexeyDTC_msg2455_transcript.txt)
[^2]: [20260225_225401_AlexeyDTC_msg2469.md](../inbox/used/20260225_225401_AlexeyDTC_msg2469.md)
[^3]: [20260226_065034_AlexeyDTC_msg2477_transcript.txt](../inbox/used/20260226_065034_AlexeyDTC_msg2477_transcript.txt)
[^4]: [20260226_065539_AlexeyDTC_msg2479.md](../inbox/used/20260226_065539_AlexeyDTC_msg2479.md)
