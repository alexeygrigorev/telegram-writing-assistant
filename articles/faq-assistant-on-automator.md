---
title: "Taking Over the FAQ Assistant: How the Whole Process Works Now"
created: 2026-07-15
updated: 2026-07-30
tags: [faq, automator, agents, datatalks-club, search, serverless, article-idea]
status: draft
---

# Taking Over the FAQ Assistant: How the Whole Process Works Now

This is a continuation of [From Google Docs to an Automated FAQ System for DataTalks.Club Courses](https://alexeyondata.substack.com/p/from-google-docs-to-an-automated). Things have changed since that article, and I want to write a full article about how the whole process works now. In this post I want to tell you what I did and how everything works for me at the moment[^2].

The previous FAQ assistant was maintained by Alex Litvinov, who I wrote about in that article. Periodically things happened and I had to pull Alex in and ask him to fix them. That was inconvenient. In the end Alex and I agreed that I can take this project on myself and start moving it onto different infrastructure - DataTalks.Club infrastructure - so that it is easier for me to solve whatever problems come up without involving Alex[^2].

The post has two parts, matching the two parts of the system[^3]:

1. The part that automates filling the FAQ with new questions
2. The RAG itself - the retrieval side

There is a bit of RAG in the first part too[^3].

The split is also a split across two repositories. [DataTalksClub/faq](https://github.com/DataTalksClub/faq) holds the FAQ content in `_questions/`, the GitHub-issue-to-pull-request agent, and the website. [DataTalksClub/faq-assistant](https://github.com/DataTalksClub/faq-assistant) holds the Slack answering bot that runs on Lambda, the search index build, and the retrieval evaluations.

## Part 1: How questions get into the FAQ

### Source one: people creating issues

The first source for adding to the FAQ is people. Anyone can create an issue. I already wrote about this in the previous issue, but the general process is that the issue goes through something RAG-like, and then automation takes over[^3].

Concretely, there is an issue template called FAQ Proposal which auto-labels the issue and asks for the course through a dropdown. A workflow fires on issue creation, gated on that label. It parses the course, question and answer out of the issue body, and the agent builds a search index over that one course's existing entries. It searches twice - once with the question alone, once with the full question and answer proposal - fuses the two result lists with reciprocal rank fusion, and then makes a single structured call that returns one of four actions: new, update, duplicate, or wrong course, along with a rationale, the section, a filename slug and an order.

The workflow branches on the action. New and update create a branch, commit as the FAQ Bot account, and open a pull request that closes the issue. Duplicate closes the issue as completed. Wrong course closes it as not planned.

I process the results with Claude Code or Codex - with assistants. A skill shows me the pull request, and I decide what to do with it: merge it or not[^3].

### Source two: issues that ignore the contribution guide

Some course participants, instead of studying the contribution guide and creating an issue with the right tag and the right format, just create an issue in the FAQ with a plain description. I process those as well[^4].

### Source three: Slack

The third source I take from Slack.

TODO: separate short section about how the Slack part happens[^4].

### The batch flow

The flow now looks like this[^4]:

1. A course participant creates an issue
2. The automation creates a pull request from that issue
3. Once a week or once every two weeks I do a batch and process them
4. For each pull request, Codex or Claude Code tells me whether everything is fine, whether the category or the section needs to be changed, whether anything in the pull request needs fixing, and also whether this case can be added to the evaluation set and why

Correcting an answer is no longer a manual edit followed by a manual test run. The agent takes the correction, fixes the content, commits it to the right repositories, and reports back what it changed and what it verified[^1].

<figure>
  <img src="../assets/images/faq-assistant-on-automator/automator-faq-fix-report.jpg" alt="Screenshot of an agent report about correcting a certificate requirement in the FAQ, listing two new commits and the validation test results">
  <figcaption>An Automator run correcting the certificate requirement in the FAQ</figcaption>
  <!-- Concrete example of the correction workflow described above: a correction goes in, the agent commits it across the faq and faq-assistant repos and reports the test results -->
</figure>

The run in the screenshot corrected a clarification about certificate requirements: the certificate requires completing the capstone project and the required peer reviews, homework is not required, and the evaluation case was reclassified as incomplete with the corrected expectation. It produced two commits - `09c95d5` in the faq repo clarifying the LLM peer review requirement, and `353810d` in the faq-assistant repo correcting the certificate evaluation expectation. Validation ran 45 assistant tests, 39 FAQ unit tests, and 26 FAQ integration tests, all passing, with nothing pushed[^1].

Automator is the Slack bot behind the DataTalks.Club Slack workspace, described in [Building and Maintaining a Slack Community](https://alexeyondata.substack.com/p/building-and-maintaining-a-slack).

## The evaluation set

I want this agent to work well, and for that you obviously need a reliable evaluation set[^3].

How I composed it: we took all the issues and pull requests. If I changed something in a pull request, that means the agent did something wrong. So we identified several special cases - not the frequent, general ones - and for each of these cases found several representative examples. That is how the evaluation set was made[^3].

The evaluation set is built in an interesting way. The issues have already been merged, so if a question is already in our dataset then, with the agent working correctly, it will always come out as a duplicate. So what we do instead: we take the record, take our data, take the issue that was created, remove that record, and check that the agent then makes the right decision[^3].

In the runner this is a leave-one-out setup. It copies the course directory to a temporary directory, deletes the markdown files matching the case's target document plus any explicitly hidden documents, and builds the agent over the reduced corpus - while keeping the course catalog complete, so wrong-course detection still works. Duplicate cases run against the full index instead, which is the mirror image of the same test.

The cases are hand-written Python dataclasses rather than data files, and the case id carries meaning: a positive id is the real GitHub issue number, a negative id is a synthetic case. They come from listing all issues with the `faq-proposal` label, plus correction commits - commits where a human had to fix the bot's output after a merge. There are currently 61 cases in the agent evaluation: 38 expecting a new entry, 10 duplicates, 7 wrong-course, 4 not-wrong-course and 2 updates. A separate retrieval-only evaluation has 73 cases, 55 real and 18 synthetic, and runs in about four seconds because it involves no LLM call.

For every case whose expected action is not wrong-course, the runner prepends an implicit not-wrong-course check. So the whole suite doubles as the false-positive budget, not just the cases written for it.

The evaluations do not run in CI in either repository. That is deliberate - they cost money and they are noisy. Recorded results: recall@5 of 0.849 and MRR@5 of 0.836 on the search evaluation, and zero false positives out of 44 non-wrong-course cases.

I want to keep the evaluation set maximally lean - I want representative cases in there, so I try not to add everything that comes along. But in some cases genuinely new and interesting cases come up that really do need to be added[^4].

### What the evaluation optimises for

Some mistakes are not fatal. If the category is chosen wrong, that is easy to fix, and I do it through Claude Code[^3].

The bad decisions are the other ones: when the agent decides the course is wrong, or in some cases when the pull request does not even fire and never gets created. Those are the worst outcomes. The evaluation is aimed at reducing those cases - false positives where no pull request gets created - to zero. That is the main target[^3].

In the end I chose `gpt-5.4-nano`, because that is the one that helped achieve this result[^3]. The workflow deliberately passes no model argument - the default in `rag_agent.py` is the single source of truth, so production and the evaluations cannot drift apart.

The model comparison behind that choice: across 84 observations, wrongly-closed valid proposals were 15 for `gpt-5-nano`, 12 for `gpt-5.4-nano` and 9 for `gpt-5.6-luna`. On wrong-course recall the numbers were 13 of 35, 7 of 35 and 27 of 35, with zero false positives out of 20 in all three. `gpt-5.4-nano` costs $0.20 per million input tokens and $1.25 per million output tokens.

The Slack answering bot on the retrieval side is a different system and uses a different model - `gpt-5.4-mini` for answering, with `gpt-4o-mini` for query rewriting.

### Choosing the section

Sections are defined per course in a metadata file as a list of id, name and an optional comment. The comment gets injected into the prompt along with the section list, and the prompt tells the agent to give the comment more weight than the search results when choosing a section. There are 74 sections across 6 courses, 42 of them with a comment. Because the course comes from a dropdown on the issue form and only that one course is loaded, the agent's real choice set on any given run is 9 to 18 sections.

The most useful thing the evaluation surfaced here was about the catch-all section. The intuitive worry is that an agent will dump everything into `misc`. The opposite happened. With `misc` carrying no comment, the agent placed entries correctly 5 times out of 5 everywhere else, but could not use `misc` when `misc` was the right answer - it sent a cross-cutting "Python 3.13 breaks sklearn" question to `module-5` five times out of five. Adding a scoping comment to `misc` took those cases from 10 out of 15 to 15 out of 15. An undescribed section does not attract entries, it repels them.

The comments earn their keep in other ways too. The Data Engineering `workshop-1-dlthub` comment says that questions about dlt go there and not to confuse dlt with dbt, because they are different tools. The `module-7` comment says not to name specific tools like Kafka, PyFlink, Spark Streaming or Redpanda in the section name, because the course's streaming stack changes between cohorts.

### Implicit feedback from Slack

There is another way I build the evaluation set: I go into Slack and look at the answers I corrected. The automation fired, and after that I or someone else added something to the answer. Those are exactly the ones that go into the evaluation set - answers that are not very good and need improving. It is implicit feedback[^6].

On the retrieval side this feeds a hand-curated end-to-end regression set of real questions the bot got wrong. It is deliberately small - six records so far, all from LLM Zoomcamp - and it is fed by a Slack review script and a feedback-loop skill.

The retrieval ground-truth set is built the same way, from real Slack threads. Around 6,800 answered, question-shaped, non-staff messages get sampled down to 130, then judged with pooled relevance: the pool is the union of what ZeroSearch returns on the raw question, what minsearch returns on the raw question, and what ZeroSearch returns on a neutral rewrite, and an LLM judge marks which candidates actually answer the question. The average query has 2.82 relevant documents.

## Part 2: Retrieval

The second part is the retrieval itself, the RAG. I did a lot here, because the process Alex had was not so much complex as something I wanted to simplify as much as possible[^5].

Alex handed over all the info and the whole project, and I started thinking about how to deploy it. There was vector search, ingestion from Slack, ingestion from YouTube - a lot of things. The project turned out to be quite complex. There were grounds for that: some historical reasons, and some things just ended up that way over time[^5].

I wanted to simplify it as much as possible. I wanted a serverless architecture, with everything deployed on Lambda[^5].

### Dropping the extra sources

Everything that appears in Slack I curate, and everything that appears on YouTube we curate too. When we have a course launch I add some things to Slack, and many things we add to our documentation. We now have a documentation site where all of this is written down[^5].

So there is no need to index the videos - we already have all of it available in prepared form. I spent quite a lot of effort on curating the YouTube course data, so the need for the other sources falls away[^5].

### Dropping the vector database

Second, I removed the vector database. The retrieval could be improved with it, but it is a lot of hassle. On the course I teach that you need to process this data, and there is a lot to process: you have to store embeddings somewhere, you need a service to store them, and if you compute those embeddings you need somewhere to compute them. In short, serverless does not fit[^5].

### Why MinSearch did not fit either

Third, MinSearch does not quite fit on Lambda. MinSearch was originally a library written for educational purposes, and only later turned out to be useful more broadly - it is the small search library behind my [RAG workshops and courses](https://alexeyondata.substack.com/p/minsearch-the-small-search-library). Because it was written for educational purposes it uses scikit-learn internally, plus NumPy, plus Pandas. Those libraries are in every data scientist's standard set, but if we are talking about deploying to Lambda, a lot of problems appear with how to do that at all. It is not a trivial process, you need to use Docker, and in short it becomes very difficult[^5].

### ZeroSearch

So I decided to replace MinSearch. I asked Claude Code or Codex - I do not remember which - to rewrite it completely into zero-dependency Python. I already had an implementation of this inverted-index search in MinSearch, something similar, and we implemented it[^6].

The result is [ZeroSearch](https://github.com/alexeygrigorev/zerosearch): a library with absolutely no dependencies. There is one shared dependency, because I now have three libraries for search - ZeroSearch, MinSearch and [SQLiteSearch](https://alexeyondata.substack.com/p/how-i-built-sqlitesearch-a-lightweight) - and a common part with stemming appeared across them. I extracted that common stemming part into a separate library, and it is optional for ZeroSearch, for when stemming is needed[^6].

ZeroSearch is made exactly for environments like Lambda, which I love, where you need a minimum of dependencies[^6].

The dependency claim is literal. The `pyproject.toml` of ZeroSearch declares an empty dependency list with the comment "Intentionally empty: standard library only". The only optional extra is `stemming = ["stemlite>=0.1.0"]`, and stemlite itself is also standard library only. Stemlite exists precisely because minsearch, ZeroSearch and SQLiteSearch all needed to normalise words the same way without each carrying its own copy or pulling in a heavyweight NLP stack. It is imported lazily, and only when a stemmer is requested by name.

### Benchmarks

I benchmarked all of this[^6]. There are two separate benchmark efforts, and they answer two different questions.

The first is a speed benchmark inside the ZeroSearch repo, which measures ZeroSearch against its own previous version - the working tree against a git ref - across a search-path optimisation. The dataset is Simple English Wikipedia, sampled to 1,000 and 10,000 articles, with queries sampled from article titles. It records build time, peak memory, serialized artifact size, and search latency at average, median and p95, plus queries per second.

| Sample | Version | Build | Peak memory | Avg search | p95 | QPS |
|--------|---------|-------|-------------|------------|-----|-----|
| 1,000 docs | before | 1.095 s | 51.1 MB | 0.087 ms | 0.337 ms | 11,478 |
| 1,000 docs | after | 1.106 s | 59.3 MB | 0.063 ms | 0.224 ms | 15,791 |
| 10,000 docs | before | 8.277 s | 338.3 MB | 0.875 ms | 2.693 ms | 1,142 |
| 10,000 docs | after | 8.531 s | 371.2 MB | 0.345 ms | 1.467 ms | 2,897 |

Average search latency improved 2.5x on the 100-query run and 1.9x on a longer 100,000-query run, with p95 improving 1.8x to 1.9x. Build time is unchanged, because this was a search-path change and not a build change. The cost is about 1.5 MB more on disk and 33 MB more peak memory during the build. The 10,000-document index has 392,806 vocabulary terms and 3,462,657 postings.

The rankings themselves are identical before and after - matched to a 1e-12 tolerance with zero mismatches, checked across 100 Simple Wikipedia queries, 9,845 unique queries from the long run, and the entire FAQ assistant evaluation corpus.

One methodology detail is worth keeping. Earlier versions of that table timed the index build under `tracemalloc`, which traces every allocation and slowed the build by roughly 4x - an 8.5 second build was being reported as 34 seconds. Build memory is now measured in a separate, untimed run. The same trap showed up in the Node port benchmark, where it made Node look 8x faster than Python when the real gap is 1.8x.

The second benchmark is a relevance benchmark, and it lives in the FAQ assistant repo rather than in ZeroSearch. It sweeps eight query-rewrite variants against two engines - ZeroSearch and minsearch - at k of 1, 3 and 5, over a ground-truth set built from real Slack threads. The best result is hit@5 of 0.62 and MRR@5 of 0.43 on ZeroSearch, against 0.586 and 0.419 for the best minsearch configuration. So ZeroSearch is not worse than minsearch on real queries, and it is noticeably more robust to aggressive rewriting: minsearch drops to around 0.33 to 0.41 on the most compressed rewrite variants, while ZeroSearch holds around 0.42 to 0.55.

The finding underneath that is the interesting one. Rewriting the question helps, but how you rewrite matters more than whether you rewrite. The winning variant distills a chatty Slack message down to keywords while preserving exact error messages, tool names, commands and filenames. Over-compressing, or adding synonyms, makes things worse - because it drops the exact tokens keyword search depends on.

### Keeping the index fresh

Then I started thinking about what to do with updating the index. If a record in the FAQ changes, the search needs to reflect it in real time, right away[^6].

The main idea is that I want it to update as fast as possible. So every time an update happens, I completely rebuild the index and push it to Lambda - I deploy a new Lambda[^6].

There is one deploy workflow with three triggers: a push to `main` touching the source, config or build scripts; a daily schedule at 08:00 to pick up new FAQ, docs and repository content; and a manual dispatch. Every run rebuilds the corpus from the live sources, builds the index, and deploys. Push deploys and scheduled deploys are therefore identical, and neither the corpus nor the index is ever committed to git.

The run installs uv, sets up Python 3.14 - which has to match the Lambda runtime, because the index is tagged with the Python version - runs the tests, rebuilds the corpus, compiles the config, builds the index, runs a handler smoke test, then takes AWS credentials via OIDC and runs `sam build` and `sam deploy`.

There is no incremental update path at all. A full rebuild every time is what makes the freshness guarantee simple.

The deployment is a zip-based Lambda through AWS SAM: Python 3.14 on arm64, 256 MB, a 30 second timeout, in eu-west-1. No Docker anywhere - which was the whole point of dropping the scikit-learn stack. The index ships inside the zip rather than from S3. The build step installs ZeroSearch into the artifacts directory, copies the application package in, and copies the `search-index.zsx` file in next to it:

```make
build-FaqWorkerFunction:
	uv pip install --target "$(ARTIFACTS_DIR)" zerosearch==0.4.0
	cp -r src/faq_assistant "$(ARTIFACTS_DIR)/faq_assistant"
	cp artifacts/search/search-index.zsx "$(ARTIFACTS_DIR)/search-index.zsx"
```

S3 is only involved as SAM's ordinary upload bucket. Nothing is fetched from S3 at runtime. The handler loads the index once per container as a module-level lazy singleton.

The corpus comes from four sources: the Slack-curated FAQ pulled from the published site JSON, the general documentation site, per-course documentation pages, and six course GitHub repositories read through the `gitsource` library. That is 3,337 chunk records, about 5.3 MB of JSON, producing an index file of roughly 8 MB. Chunks are 1,800 characters with 150 characters of overlap, and retrieval returns 6 results by default with a minimum score of 0.2.

The runtime dependency list really is just ZeroSearch. The OpenAI call uses `urllib` from the standard library, the structured models are hand-rolled, and there is no pydantic and no requests.

### Fast index loading

I also optimised ZeroSearch so that loading the index happens as fast as possible[^6].

This is a separate piece of work from the search-path optimisation above. When `fit()` runs, it compacts the `Counter` scaffolding into flat `array` buffers in a CSR-style postings layout, and `save` and `load` serialize that packed form through `marshal`, with magic bytes, a format version, a Python version guard and array item-size guards. A prebuilt index then loads in milliseconds instead of re-tokenizing the corpus on startup, and the ranking is bit-identical to the previous format.

The reported figures are about 15 ms to load the packed index at cold start versus about 520 ms for a fresh `fit()`. These are observed numbers rather than benchmark output - unlike the search-path numbers above, there is no checked-in benchmark that measures index load time yet.

## To fill in

- The Slack section: how questions get from Slack into the FAQ
- How the assistant was wired into Automator and what triggers a run
- What the agent is allowed to change on its own and what still needs review before pushing
- What maintenance used to require before the migration, for the before-and-after comparison

## Sources

[^1]: [20260715_101244_AlexeyDTC_msg4773_photo.md](../inbox/used/20260715_101244_AlexeyDTC_msg4773_photo.md)
[^2]: [20260730_220026_AlexeyDTC_msg4805_transcript.txt](../inbox/used/20260730_220026_AlexeyDTC_msg4805_transcript.txt)
[^3]: [20260730_220553_AlexeyDTC_msg4807_transcript.txt](../inbox/used/20260730_220553_AlexeyDTC_msg4807_transcript.txt)
[^4]: [20260730_220745_AlexeyDTC_msg4809_transcript.txt](../inbox/used/20260730_220745_AlexeyDTC_msg4809_transcript.txt)
[^5]: [20260730_221538_AlexeyDTC_msg4811_transcript.txt](../inbox/used/20260730_221538_AlexeyDTC_msg4811_transcript.txt)
[^6]: [20260730_222124_AlexeyDTC_msg4813_transcript.txt](../inbox/used/20260730_222124_AlexeyDTC_msg4813_transcript.txt)
