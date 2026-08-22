---
title: "Building an AI Book Generator with a Plan-Then-Execute Pipeline"
date: 2026-05-08
url: https://aishippingblog.com/p/building-an-ai-book-generator-with
---

My child has very specific interests and information requests. He asks me to find books on narrow topics like metals or signal sirens, and most of the time, such books don’t exist. Or they exist, but not as kids’ books.

So I built a system to generate such books for him. It all started with an experiment with ChatGPT. When I validated the need for a more automated, complex approach, this project evolved into an [automated pipeline that uses AI to generate the entire book](https://github.com/alexeygrigorev/ai-book-generator).

In this post, I’ll share:

* How the first book about metals started the project
* Why direct ChatGPT generation was not enough
* How I used coding agents to create the first books
* Why I later built a dedicated book generator
* How the current pipeline plans, writes, formats, and packages books
* How audio, EPUB, and Amazon KDP outputs are generated
* What happened when I tried to publish one of the books on Amazon

## The First Request: a Book About Metals

[![Image 1](https://substackcdn.com/image/fetch/$s_!_Ywx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54414ccb-f6bd-4b12-813b-6ce6d6579c9b_2048x1288.png)](https://substackcdn.com/image/fetch/$s_!_Ywx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54414ccb-f6bd-4b12-813b-6ce6d6579c9b_2048x1288.png)

His first request was a book about metals. He wanted to know what metals are and how they are used. He only cared about a specific list: palladium, tin, magnesium, titanium, beryllium, lithium, and tungsten. He told me exactly which properties to describe. ChatGPT suggested adding a few other metals to complete the picture, and my son agreed. We planned one chapter per metal to cover its history, extraction, and uses.

We could not find a book like this, and he wanted to listen to it at bedtime. I first tried generating the book directly with ChatGPT. We iterated on a table of contents. I asked the model to write the first chapter, but the result was very poor. ChatGPT alone didn’t work.

I then considered coding agents. They are good at planning and executing. My normal approach to building applications is to iterate on a design with ChatGPT and delegate the implementation to a coding agent. I figured the same pattern should work here. I could use ChatGPT to generate the table of contents and let the coding agent write the actual book.

## Iterating with Coding Agents on the Metals Book

My son and I finalized the outline. I handed the plan to the coding agent. The first version was rough. The agent wrote bullet points instead of prose. Coding agents are likely tuned for documentation rather than narrative writing.

[![Image 2](https://substackcdn.com/image/fetch/$s_!Z4zj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F164a4d74-42c3-4df3-9c8e-6c0958fb02e0_1079x1447.png)](https://substackcdn.com/image/fetch/$s_!Z4zj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F164a4d74-42c3-4df3-9c8e-6c0958fb02e0_1079x1447.png)

Part of the table of contents of the metals book showing one chapter per metal, with descriptive subtitles like “gold: metal of pharaohs and pirates” or “tungsten: the highest melting point”.

I tightened the prompt and explicitly asked for normal prose. I managed the process just like my regular coding projects. I created a GitHub issue, let the agent work on it, reviewed the result, and created the next issue. This is the same approach I use when coding from my smartphone. I described it in one of my previous newsletters:

[Shipping Features from my Smartphone with GitHub Copilot](https://alexeyondata.substack.com/p/shipping-features-from-a-tram-stop)

Another problem was context limits. The agent didn’t finish the task. If I asked it to rewrite the whole book in proper prose, it would rewrite the first five chapters and stop because “it was tired.” I had to push the agent to finish the entire text repeatedly.

In parallel, I asked the agent to set up automation. I wanted to publish the book as a website first so I could read it in the browser. I added EPUB output later simply because I found it interesting. The automation worked well. The text for the metals book required a lot of manual guidance, but my child liked the final result.

The published book lives at <https://alexeygrigorev.com/little-book-of-metals-ru/>. Source code: [github.com/alexeygrigorev/little-book-of-metals-ru](https://github.com/alexeygrigorev/little-book-of-metals-ru).

## Second Book: Gallium and Potassium Alloys

Halfway through the metals project, my son decided he was only interested in two specific metals: gallium and potassium. He specifically wanted to read about their alloy because it has unusual properties. We made a separate book for that topic.

[![Image 3](https://substackcdn.com/image/fetch/$s_!1A7i!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F658e75dc-ae90-4e48-82a9-23dd574fb842_1265x704.png)](https://substackcdn.com/image/fetch/$s_!1A7i!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F658e75dc-ae90-4e48-82a9-23dd574fb842_1265x704.png)

By that point, I understood the workflow. I put exactly what I wanted directly into the first prompt. The experience from the metals book paid off immediately. The book came out well on the first attempt. The entire project required just two GitHub issues. One issue was to write the book. The second issue was to add EPUB and MOBI publishing.

The two closed issues in the gallium-kalium book repository: “Написать книгу” (write the book) and “epub and mobi generation”.

[![Image 4](https://substackcdn.com/image/fetch/$s_!pevx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F229f6b2f-f928-430b-840c-e5cc85c673b8_1080x636.png)](https://substackcdn.com/image/fetch/$s_!pevx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F229f6b2f-f928-430b-840c-e5cc85c673b8_1080x636.png)

Source code: [github.com/alexeygrigorev/gallium-kalium-book-ru](https://github.com/alexeygrigorev/gallium-kalium-book-ru).

## Third Book: Conifers

[![Image 5](https://substackcdn.com/image/fetch/$s_!0I7z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefe8105a-ea07-46b2-8b2e-4a2f5481ad77_1277x734.png)](https://substackcdn.com/image/fetch/$s_!0I7z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefe8105a-ea07-46b2-8b2e-4a2f5481ad77_1277x734.png)

Later, my son wanted to learn more about conifers after studying them in school. By then, the workflow was standard. We discussed the topic with ChatGPT, built a plan, created a GitHub issue, let Copilot work on it, and received the completed book.

Source code: [github.com/alexeygrigorev/conifers-book-ru](https://github.com/alexeygrigorev/conifers-book-ru).

## Building a Specialized Book Agent

After the third book, I realized a general coding agent like Copilot was not the best tool. I decided to build a dedicated program for two reasons. First, I needed a use case for my course participants to show how to build specialized agent systems. Second, I suspected a specialized agent would produce better narrative text than models tuned for code.

I built the program to compare GPT, Claude, and a newly released Gemini model. My evaluation was informal. I simply read the books with my child and picked the best text. Gemini produced the best results.

The hypothesis proved correct in practice. The specialized agent wrote better prose than the general coding agents.

The workflow settled into a standard plan-then-execute pattern, identical to what I teach for code:

1. Iterate in a chat interface to finalize the table of contents.
2. Convert the chat output into a structured YAML plan containing chapters, sections, and bullet points.
3. Run a loop over the plan using `for chapter in plan: generate_chapter(...)`. Each iteration receives a compressed summary of prior chapters to maintain context without passing the entire text.

## Many Books Since

I started by redoing the metals book just to test the new pipeline. Since then, the system has successfully handled several highly specific requests. These included a book on warning sirens, a guide to how fireworks work, and a book dedicated entirely to cable-driven mechanisms such as funiculars.

## How the Book Generator Works

The [repository](http://github.com/alexeygrigorev/ai-book-generator) provides an end-to-end pipeline for planning and generating books. It starts with an interactive planning step, converts the plan into a typed YAML file, generates chapters from that plan, and then produces audio, EPUB, and Amazon Kindle Direct Publishing print artifacts.

You can use the system through either a Streamlit interface or command-line scripts. The main design pattern is plan first, then execute. The book structure is decided upfront, and the later generation and publishing steps use that structure as their source of truth.

### 1. Plan Generation

The first stage is interactive because the system treats the book structure as something to review before text generation begins.

You launch the Streamlit interface with `make ui`.

In the UI, you enter a topic and select a book size, such as Small, Medium, or Large. Then you start a chat with Gemini 3 Pro Preview. The model streams a draft book plan into the interface.

[![Image 6](https://substackcdn.com/image/fetch/$s_!uYGj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c28ce7b-8900-4757-8bd7-64b5cda37c5b_1121x475.png)](https://substackcdn.com/image/fetch/$s_!uYGj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c28ce7b-8900-4757-8bd7-64b5cda37c5b_1121x475.png)

The Streamlit app interface that you can see after running `make ui`

You can refine the plan through chat. Each refinement call sends the current plan, along with your new feedback, back to Gemini, so the model updates the existing outline rather than starting from scratch.

When the outline looks good, you click: “`Ready - Create Structured Plan`”. This moves the workflow from freeform planning to structured execution. For headless runs, there is a command-line alternative. You run `uv run python -m chapter_based.plan -p books/mybook/input.txt` to build the plan from a text file instead of the Streamlit chat.

[![Image 7](https://substackcdn.com/image/fetch/$s_!S8JJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61fe3af2-726c-492d-96de-d479d284f737_1772x916.png)](https://substackcdn.com/image/fetch/$s_!S8JJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61fe3af2-726c-492d-96de-d479d284f737_1772x916.png)

### 2. Structured Plan Creation

The freeform chat plan is useful for humans, but the generator needs a predictable structure. The next step converts the outline into a typed plan that the execution scripts can read.

The system sends the finalized plan to Gemini one more time and requests JSON output using `response_mime_type=”application/json”` and a schema generated from the Pydantic `BookPlan` model. The structured output is saved to `books/<slug>/plan.yaml`.

[![Image 8](https://substackcdn.com/image/fetch/$s_!3AV-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52032518-a3c0-42b4-bf2d-7ef1613f0580_2006x982.png)](https://substackcdn.com/image/fetch/$s_!3AV-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52032518-a3c0-42b4-bf2d-7ef1613f0580_2006x982.png)

Here how a slice of the YAML structure looks like:

```
name: My Book
slug: my-book
book_language: ru
parts:
  - name: Part One
    introduction: ...
    chapters:
      - name: Chapter Name
        bullet_points:
          - point one
          - point two
```

This `plan.yaml` file is the contract between planning, writing, audio generation, and publishing. The writing scripts use it to generate chapters. The publishing scripts use it for metadata and structure. The cover pipeline uses it for back-cover text.

This separation is important because it allows the planning interface to change without rewriting the execution pipeline, provided it still produces the same structured plan.

Per-part introductions and back-cover text also come from fields already present in the plan and don’t require extra model calls during generation.

### 3. Chapter-by-Chapter Execution

Once `plan.yaml` exists, the writing scripts no longer need the chat history. They use the structured plan as the source of truth.

If you use the command line, you run `uv run python -m chapter_based.execute mybook`. There is also a Makefile command: `make generate-book`.

[![Image 9](https://substackcdn.com/image/fetch/$s_!pkO_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2d38e70-bf15-46cb-96ed-00756bcf35b9_1676x824.png)](https://substackcdn.com/image/fetch/$s_!pkO_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2d38e70-bf15-46cb-96ed-00756bcf35b9_1676x824.png)

The repository contains two generation implementations:

* `book_generator/`: section-based generation. It uses more LLM calls per chapter and gives finer-grained control, which is useful for longer books.
* `chapter_based/`: chapter-based generation. It makes one call per whole chapter and usually produces 3000 to 5000 words per chapter.

The chapter-based path is the cleaner illustration of the pipeline.

The script `chapter_based/execute.py` loads the YAML file, flattens the parts into a single list of chapter specifications, and iterates through them.

For each chapter, the script builds a book progress string with the full chapter list:

* Completed chapters are marked with `[x]`.
* The current chapter is marked with an arrow.
* Remaining chapters are marked with `[ ]`.

Gemini receives this outline together with the bullet points for the current chapter. It does not receive the full text of previous chapters. Cohesion comes from the upfront plan, not from passing actual prior chapter text into each generation call.

This makes the quality of the initial plan important. The plan needs enough structure to keep chapters aligned across the whole book.

### 4. Audio Generation

After the markdown chapters exist, the same book folder can be used to generate audio versions of the content. I added that part because my son sometimes wants to listen to the books rather than read them. The implementation uses Gemini text-to-speech because its voice quality was better than that of the previous setup used in a separate AI bedtime stories project.

You can start text-to-speech generation with `make tts BOOK=...` The script `book_generator/tts.py` calls `models/gemini-2.5-flash-preview-tts` and uses the default voice, `Charon`. The script wraps the returned PCM audio into a WAV file and uploads it directly to an S3 bucket.

Generation runs in parallel with `ThreadPoolExecutor`. It also uses a cost lock and a skip-if-already-generated check, so existing audio files aren’t regenerated unnecessarily.

A separate script, `scripts/convert_wav_to_mp3.py`, converts WAV files to MP3. It uses `ffmpeg` and produces MP3 derivatives for distribution.

## Publishing Process

The publishing scripts also use the generated markdown and the same `plan.yaml`, so EPUB and print output don’t depend on how the text was generated.

[![Image 10](https://substackcdn.com/image/fetch/$s_!pkO_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2d38e70-bf15-46cb-96ed-00756bcf35b9_1676x824.png)](https://substackcdn.com/image/fetch/$s_!pkO_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2d38e70-bf15-46cb-96ed-00756bcf35b9_1676x824.png)

There are three main publishing commands.

1. `make ebook BOOK=...` publishes the book to EPUB. `scripts/convert_to_ebook.py` aggregates the markdown files and adjusts heading levels so chapter headings fit the EPUB structure. It then calls Pandoc with title, author, language metadata, and an optional cover image. The output is an EPUB file.
2. `make kdp-interior BOOK=...` publishes the book to KDP interior PDF. `scripts/create_kdp_interior.py` aggregates the markdown files and renders it through XeLaTeX inside a Docker image for reproducibility. The output is a KDP-ready interior PDF with 6 by 9 inch trim size, mirror margins, gutter, DejaVu fonts for Cyrillic, and a generated table of contents. The resulting file is kdp\_interior.pdf.
3. `make kdp-cover BOOK=...` publishes the book to KDP cover PDF. `scripts/create_kdp_cover.py` builds a wraparound print cover with ReportLab. It lays out the back cover, spine, front cover image, and bleed area. The back-cover description comes from plan.yaml. The spine width is calculated from the page count using pages \* 0.0025 inches. The resulting file is kdp\_cover.pdf.

## Cost Tracking and Operational Conventions

The generator tracks cost during planning and writing because book-length generation can involve long contexts, multiple chapter calls, retries, and optional asset generation.

The function `calculate_gemini_3_cost` uses the November 2025 Gemini pricing tiers, including the standard tier and the over-200k-context tier. It also bills “thoughts” tokens as output tokens.

[![Image 11](https://substackcdn.com/image/fetch/$s_!E_ts!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9bda2357-fca8-441e-b483-df0db5105fca_1814x886.png)](https://substackcdn.com/image/fetch/$s_!E_ts!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9bda2357-fca8-441e-b483-df0db5105fca_1814x886.png)

A `CostTracker` accumulates cost during generation. In the Streamlit UI, the running total is shown live while the plan is drafted and refined. During text generation, the terminal output also reports incremental costs as chapters and sections are produced.

Because generation can take time and cost money, the system writes each artifact to a predictable location and checks whether it already exists before regenerating it.

Chapter output is written to paths like `books/<slug>/part_01/01_chapter.md`.

A typical book folder contains:

```
books/<slug>/
  plan.yaml
  back_cover.md
  cover.jpg
  part_01/
    01_chapter.md
    02_chapter.md
  part_02/
    01_chapter.md
  book.epub
  kdp_interior.pdf
  kdp_cover.pdf
```

The scripts infer where to read and write files based on naming conventions such as `books/<slug>/`, `part_XX/`, and predictable artifact names.

The generation script checks whether a chapter file already exists. If it does, the script skips that chapter on rerun. A `_ready` sentinel file in the book folder marks the book as complete and tells the system not to modify it anymore. Per-step `*_exists` checks prevent the system from regenerating artifacts that already exist.

All later steps use the same book folder and the same `plan.yaml`. Planning, writing, audio generation, and publishing are connected through files rather than through one large process. This design choice and operational convention make the pipeline idempotent and resumable: if a run is interrupted, it can continue from the missing pieces instead of starting from the beginning.

The Makefile wires the workflow together:

```
make ui

  -> chat and create structured plan
  -> make generate-book
  -> make tts BOOK=...
  -> make ebook BOOK=...
  -> make kdp-interior BOOK=...
  -> make kdp-cover BOOK=...
```

[Share](https://aishippingblog.com/p/building-an-ai-book-generator-with?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## Example Generation Run

During generation, the terminal output shows what the system is working on and how much each step costs. This makes the generator easier to monitor during long runs. It also makes cost visible while the book is still being produced, rather than only after completion.

[![Image 12](https://substackcdn.com/image/fetch/$s_!oSsg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51006a08-e0f4-4238-a0a4-8d19b1827c67_892x534.png)](https://substackcdn.com/image/fetch/$s_!oSsg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51006a08-e0f4-4238-a0a4-8d19b1827c67_892x534.png)

One example was a fireworks book generated with this system. It produced 21 chapters, took about 45 minutes of wall-clock time, and cost roughly $4 using Gemini 3 Pro.

This number is useful as a benchmark, but it should not be treated as a fixed estimate. The final cost depends on the model, book length, context size, retries, and which optional steps are included. Gemini Flash has not been tested yet for this workflow, so it isn’t clear how much quality or cost would change with a cheaper model.

### Cost and Quality

A fully generated book costs less than $5 in one run. The exact number depends on the book and the generation settings, but it gives a practical order of magnitude. The system currently uses Gemini 3 Pro for book generation. This is more expensive than using a smaller or faster model, but in these experiments, the output quality justified the cost. For a personal book to be read repeatedly, that cost may be acceptable.

The quality was good enough from the early experiments to make the project worth continuing. Books about metals and sirens were useful at home and readable enough. That observation led to the publishing experiment. If the books were useful privately, it was reasonable to test whether they could also be packaged for external readers.

## Publishing Experiment and Project Value

The project started as a way to generate books for private reading. Over time, the quality was good enough to raise another question: could these books be prepared for actual publication?

That changed the scope of the pipeline. It was no longer enough to generate markdown chapters; it needed to produce files that matched real publishing requirements: EPUB for ebooks, a formatted interior PDF for print, and a full-wrap cover PDF for Amazon KDP.

That is why I added the publishing scripts, `convert_to_ebook.py`, `create_kdp_interior.py`, and `create_kdp_cover.py`, I mentioned above to test the full publishing flow end to end. This test validated the production pipeline, but it didn’t validate demand.

The technical pipeline can produce a book package, but publishing files isn’t the same as selling a book. The book I tested has been on Amazon for about five months. So far, it has sold zero copies.

Uploading a generated book to Amazon isn’t enough on its own. Selling requires a separate layer of work: market research, niche selection, positioning, search optimization, metadata, reviews, and promotion.

The project is still useful, but its current value is mostly personal and technical. It works as a system for generating books for private reading and as a practical experiment in automated publishing. Turning it into a commercial workflow would require audience research and marketing work outside the generator itself.

[Share](https://aishippingblog.com/p/building-an-ai-book-generator-with?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## What I’ve Been Working On Recently

### 1. AI Shipping Labs First Sprint

[![Image 13](https://substackcdn.com/image/fetch/$s_!Thux!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d6a6edc-54da-4b51-8425-37046a8df079_2010x968.png)](https://substackcdn.com/image/fetch/$s_!Thux!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d6a6edc-54da-4b51-8425-37046a8df079_2010x968.png)

We launched Sprint 1 at AI Shipping Labs.

It’s a 6-week accountability sprint where members work on their projects, meet weekly, share progress, discuss blockers, and receive feedback.

For this sprint, Valeriia and I created 25+ personal plans. Each plan is based on the person’s background, goals, and current situation.

### 2. Freestyle Workshop at AI Shipping Labs

[![Image 14](https://substackcdn.com/image/fetch/$s_!86_G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1da7c11d-e35b-4336-b11a-5bc9317d93a4_2518x1386.png)](https://substackcdn.com/image/fetch/$s_!86_G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1da7c11d-e35b-4336-b11a-5bc9317d93a4_2518x1386.png)

I also ran another freestyle workshop at AI Shipping Labs.

In this format, people come with their own ideas or problems, and we try to implement something together. This time, we looked at how to deploy an app to AWS Lambda.

I wanted to figure this out for a while. Services like Render are convenient, but they are not really serverless. If you deploy something there, the server runs continuously, and you keep paying for it.

For small, low-traffic projects, it doesn’t always make sense. Lambda is a better fit because it runs only when needed.

I upload recordings and notes from my workshops to the [new AI Shipping Labs website](https://aishippinglabs.com/). To get full access to workshop materials, join the community.

[Join AI Shipping Labs](https://aishippinglabs.com/#tiers?utm_source=alexey_on_data&utm_medium=email&utm_campaign=ai_shipping_labs&utm_content=2026_05_08)

### 3. New Website for AI Shipping Labs

[![Image 15](https://substackcdn.com/image/fetch/$s_!TRk4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20bdd7bd-e183-4b45-a3a3-8ef8a21cfd0f_2514x1116.png)](https://substackcdn.com/image/fetch/$s_!TRk4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20bdd7bd-e183-4b45-a3a3-8ef8a21cfd0f_2514x1116.png)

I finally migrated the AI Shipping Labs website from Next.js to Django. There is still a lot to do, but the [new Django version is now live](https://aishippinglabs.com/).

You can already sign up for free, track your progress, and access some free resources, like the AI Hero course.

### 4. Data Makers Fest in Porto

[![Image 16](https://substackcdn.com/image/fetch/$s_!q90-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b37e699-1027-422f-9c3f-5de24cf5485c_1280x960.png)](https://substackcdn.com/image/fetch/$s_!q90-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b37e699-1027-422f-9c3f-5de24cf5485c_1280x960.png)

I was at Data Makers Fest in Porto this week.

On Monday, I ran a workshop called “Introduction to Agentic RAG.” For this workshop, I took the first two modules of LLM Zoomcamp on RAG and agents and simplified them as much as possible into a stripped-down introduction to agentic RAG.

The difficulty level was intentionally introductory because it works well for people new to the topic who want to understand the main pieces first.

The next day, I joined a panel in the morning and answered questions from the audience. Later, I moderated a session on production LLMs.

I also recorded several interviews with people at the conference. The podcast episode based on these interviews is still in preparation and should go out in a couple of weeks.

## Tools

[![Image 17](https://substackcdn.com/image/fetch/$s_!gHxX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc141a86-f802-4b37-ba44-f2042f57d030_1766x658.png)](https://substackcdn.com/image/fetch/$s_!gHxX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc141a86-f802-4b37-ba44-f2042f57d030_1766x658.png)

* [Code Review Graph](https://github.com/tirth8205/code-review-graph) is an MCP-based tool that builds a local knowledge graph of your codebase so AI coding assistants read only what matters during code reviews. It uses Tree-sitter to parse your code into a structural map of functions, classes, imports, and their relationships, then performs blast-radius analysis on changes to identify the minimal set of affected files. The tool supports 19 languages, updates incrementally in under 2 seconds, and benchmarks show an average 8.2x reduction in tokens compared to naive full-file reads.
* [Career-Ops](https://github.com/santifer/career-ops) is an open-source, AI-powered job search system built on Claude Code that turns your terminal into a full job search command center. It evaluates job offers using a structured scoring system, generates ATS-optimized, tailored CVs as PDFs, automatically scans 45+ company career portals, and tracks everything in a single pipeline. The author used it to evaluate 740+ job listings, generate 100+ personalized CVs, and land a Head of Applied AI role.

## Resource

[![Image 18](https://substackcdn.com/image/fetch/$s_!MAcr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feff23570-02b6-4959-9180-c0cb517b385d_2578x1362.png)](https://substackcdn.com/image/fetch/$s_!MAcr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feff23570-02b6-4959-9180-c0cb517b385d_2578x1362.png)

[Coding Challenges](https://codingchallenges.substack.com/) is a weekly newsletter by John Crickett that publishes hands-on project challenges designed to help software engineers level up by building real-world tools. Each issue walks through rebuilding well-known software from scratch - things like awk, gzip, Docker, an ebook reader, a Loom clone, or AI agents and coding assistants - giving you a concrete, scoped project to practice on. With over 92,000 subscribers and 100+ challenges in the archive, it is a great source of project ideas for anyone who learns best by doing.

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
