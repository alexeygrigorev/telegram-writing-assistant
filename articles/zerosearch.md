---
title: "ZeroSearch: A Zero-Dependency Search Library for a Lightweight FAQ Assistant"
created: 2026-06-19
updated: 2026-06-19
tags: [search, serverless, cloudflare, lambda, project]
status: draft
---

# ZeroSearch: A Zero-Dependency Search Library for a Lightweight FAQ Assistant

ZeroSearch is a new search library: [github.com/alexeygrigorev/zerosearch](https://github.com/alexeygrigorev/zerosearch) [^1]. It came out of an attempt to move the DataTalks.Club FAQ assistant onto Cloudflare Workers, and now there is one more entry in the portfolio of search libraries.

## Why a new FAQ assistant

The existing FAQ assistant was created by Alex Litvinov, who I have [written about before](https://alexeyondata.substack.com/p/from-google-docs-to-an-automated) [^2]. Recently it ran out of money, and Alex had to top it up. On top of that, Alex hosts it on Fly, and it is used by services like Milvus. All of this costs money, and Alex pays for it [^2].

Every time something breaks, I have to ping Alex and ask him to fix it. First, it is inconvenient to keep doing that. Second, he is the one paying for it, and I am not sure that is OK in the long term [^2].

So I started building a small replacement that runs on Lambda and could also run on Cloudflare, so it could be done for free. There are some limits, and I quickly ran into them [^2].

For the vector database part, I decided I would probably just use a free option. We do not strictly need a vector database here - plain text search is enough for this case [^2].

The lightweight FAQ assistant lives at [github.com/DataTalksClub/faq-assistant](https://github.com/DataTalksClub/faq-assistant) [^3].

## The Cloudflare Workers constraint

This started from the Cloudflare Workers workshop I ran in AI Shipping Labs: [Cloudflare Workers Vectorize Agent](https://aishippinglabs.com/workshops/2026-06-17-cloudflare-workers-vectorize-agent) [^4]. After that workshop I decided to try porting the FAQ assistant to Cloudflare, and that is how ZeroSearch appeared [^5].

Cloudflare Workers has a particular limitation. Everything there is actually written in JavaScript, and the Python layer is still in beta - it practically does not support any additional libraries. So if you want to write something, you have to write it in pure Python. That was one of the main constraints I noticed [^5].

## What ZeroSearch does

ZeroSearch does roughly the same thing as MinSearch, the small in-process search library behind my [RAG workshops and courses](https://alexeyondata.substack.com/p/minsearch-the-small-search-library) [^5].

The difference is in the dependencies. MinSearch depends on scikit-learn, which in turn pulls in NumPy and SciPy, and there is also a dependency on Pandas. These are all heavy libraries [^5].

Using them in a serverless environment is a problem. First, it is not very easy to deploy all of that to serverless. Second, because of the Cloudflare Workers constraint above, those libraries are not available there at all [^5].

So I rewrote MinSearch as pure Python, with zero dependencies - zero dependency leading to zero search, hence ZeroSearch [^6]. I decided to try the rewrite, and it basically worked out fine. Now my portfolio of search libraries has one more entry [^5].

## Sources

[^1]: [20260619_085722_AlexeyDTC_msg4610.md](../inbox/used/20260619_085722_AlexeyDTC_msg4610.md)
[^2]: [20260619_085045_AlexeyDTC_msg4605_transcript.txt](../inbox/used/20260619_085045_AlexeyDTC_msg4605_transcript.txt)
[^3]: [20260619_085722_AlexeyDTC_msg4609.md](../inbox/used/20260619_085722_AlexeyDTC_msg4609.md)
[^4]: [20260619_090525_AlexeyDTC_msg4621.md](../inbox/used/20260619_090525_AlexeyDTC_msg4621.md)
[^5]: [20260619_090642_AlexeyDTC_msg4623_transcript.txt](../inbox/used/20260619_090642_AlexeyDTC_msg4623_transcript.txt)
[^6]: [20260619_085722_AlexeyDTC_msg4610.md](../inbox/used/20260619_085722_AlexeyDTC_msg4610.md)
