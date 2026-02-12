---
title: "ML System Design Case Studies"
created: 2026-02-12
updated: 2026-02-12
tags: [research, ml-engineering, system-design]
status: draft
---

# ML System Design Case Studies

A curated selection from [A Curated List of ML System Design Case Studies](https://github.com/Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies) - a collection of 300+ case studies from over 80 companies[^1].

## Top 10 Picks

### 1. How we built it: Stripe Radar (Stripe, 2023)

Fraud detection in payments - one of the most classic and high-stakes ML system design problems. Stripe processes billions of transactions and their Radar system needs to balance precision (blocking fraud) with recall (not blocking legitimate payments).

Link: https://stripe.com/blog/how-we-built-it-stripe-radar

### 2. Twitter's Recommendation Algorithm (Twitter, 2023)

Twitter open-sourced their recommendation algorithm, making this one of the rare cases where you can see exactly how a major social platform ranks content. Covers candidate generation, ranking, and filtering.

Link: https://blog.twitter.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm

### 3. How to build an enterprise LLM application: Lessons from GitHub Copilot (GitHub, 2023)

Practical lessons from building one of the most successful LLM products. Covers the full lifecycle from prototype to production, including evaluation, latency optimization, and user experience design.

Link: https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/

### 4. Building the Neural Zestimate (Zillow, 2023)

House price estimation at scale. Zillow's Zestimate is one of the most well-known ML products in real estate. The neural approach shows how deep learning replaced traditional models for property valuation.

Link: https://www.zillow.com/tech/building-the-neural-zestimate/

### 5. DeepETA: How Uber Predicts Arrival Times Using Deep Learning (Uber, 2022)

ETA prediction is a core ML problem in delivery and mobility. Uber's approach uses deep learning to handle the complexity of real-world routing, traffic, and conditions across millions of daily trips.

Link: https://www.uber.com/en-GB/blog/deepeta-how-uber-predicts-arrival-times/

### 6. Scaling the Instagram Explore recommendations system (Meta, 2023)

Recommendation at massive scale - Instagram Explore serves personalized content to billions of users. Covers the multi-stage ranking pipeline, embedding models, and how they handle the cold-start problem.

Link: https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/

### 7. Lifecycle of a Successful ML Product: Reducing Dasher Wait Times (DoorDash, 2023)

Goes beyond just the model to cover the full lifecycle of an ML product. Shows how DoorDash iterated from a simple heuristic to an ML solution, including how they measured business impact.

Link: https://doordash.engineering/2023/02/15/lifecycle-of-a-successful-ml-product-reducing-dasher-wait-times/

### 8. 150 Successful Machine Learning Models: 6 Lessons Learned at Booking.com (Booking.com, 2019)

A meta-study of what makes ML projects succeed or fail in production. Covers 150 models across different use cases and distills lessons about deployment, monitoring, and organizational challenges.

Link: https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/

### 9. Machine Learning for Fraud Detection in Streaming Services (Netflix, 2022)

Fraud detection in a non-financial context. Netflix tackles account sharing, credential stuffing, and payment fraud using ML. Interesting because it shows how fraud detection applies beyond traditional fintech.

Link: https://netflixtechblog.medium.com/machine-learning-for-fraud-detection-in-streaming-services-b0b4ef3be3f6

### 10. All the Hard Stuff Nobody Talks About when Building Products with LLMs (Honeycomb, 2023)

Honest account of the challenges in building LLM-powered products. Covers evaluation, prompt engineering, handling failures, and the gap between demo and production. Relevant for anyone building with LLMs.

Link: https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm

## Full Repository

The complete repository contains 309 case studies organized by company and industry, covering:

- E-commerce and retail (Walmart, Etsy, Instacart, Wayfair, Zillow, Shopify)
- Delivery and mobility (Uber, DoorDash, Lyft, Swiggy, Grab, Gojek)
- Social platforms (LinkedIn, Pinterest, Twitter/X, Meta, Yelp, Nextdoor)
- Media and streaming (Netflix, Spotify, Dailymotion, Scribd)
- Fintech and banking (Stripe, PayPal, Nubank, Monzo, Adyen)
- Travel (Airbnb, Expedia, Booking.com, Trivago)
- Tech (GitHub, Google, Microsoft, Apple, Grammarly, Salesforce)

ML use cases span recommendation systems, search ranking, fraud detection, demand forecasting, delivery time prediction, content moderation, NLP, computer vision, and LLM applications.

## Sources

[^1]: [20260212_171745_AlexeyDTC_msg1565.md](../inbox/used/20260212_171745_AlexeyDTC_msg1565.md)
