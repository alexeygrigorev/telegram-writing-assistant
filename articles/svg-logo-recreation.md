---
title: "Recreating a PNG Logo as SVG with Claude Code"
created: 2026-02-25
updated: 2026-02-25
tags: [claude-code, opencv, svg, design]
status: draft
---

# Recreating a PNG Logo as SVG with Claude Code

This week I spent time trying to convert a PNG logo (made for a website) into an SVG. It started as a kind of procrastination but turned into an interesting experiment with different approaches[^1].

## The Problem

I had a logo generated with ChatGPT as a PNG image and wanted to recreate it as a clean SVG.

<figure>
  <img src="../assets/images/svg-logo-recreation/original-logo-chatgpt.jpg" alt="Original rocket logo generated with ChatGPT">
  <figcaption>The original PNG logo generated with ChatGPT - the target to recreate</figcaption>
  <!-- This is the reference image that all SVG conversion attempts try to match -->
</figure>

## First Attempts

I tried asking ChatGPT directly to convert it - that did not work well. Then I tried giving Claude the image, thinking maybe after a few iterations it would produce something decent. The results were much worse[^1].

<figure>
  <img src="../assets/images/svg-logo-recreation/claude-code-svg-attempt.jpg" alt="SVG created directly by Claude Code">
  <figcaption>SVG created directly by Claude Code - not close enough</figcaption>
  <!-- First attempt at having Claude Code generate SVG directly from the image -->
</figure>

Then I found some website that can convert images and told Claude to remove all the extra stuff. That also did not produce anything good[^1].

## The OpenCV + Potrace Approach

I realized I needed something more serious. I told Claude to download OpenCV and use it for proper contour approximation. Then I looked online at what Claude was doing and found another tool - potrace - that produces better bezier curves. The combination of potrace and OpenCV gives decent results[^1].

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

I started a second approach with a fresh reproduction pipeline. After 16 iterations, it reached MSE ~97 (1.4% mean pixel error)[^2].

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

## Sources

[^1]: [20260225_202646_AlexeyDTC_msg2455_transcript.txt](../inbox/used/20260225_202646_AlexeyDTC_msg2455_transcript.txt)
[^2]: [20260225_225401_AlexeyDTC_msg2469.md](../inbox/used/20260225_225401_AlexeyDTC_msg2469.md)
