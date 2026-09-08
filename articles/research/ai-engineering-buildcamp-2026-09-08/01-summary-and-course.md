# AI Engineering Buildcamp

## Public-source research dossier

Prepared for Alexey Grigorev · Research cut-off: September 7, 2026

This dossier separates what the course advertises, what other people actually say, and what public project artifacts establish. It accompanies a separate first-person article draft. The source register contains 94 records: course and style references, third-party posts and comments, student project repositories, additional repository discoveries, duplicate posts, and excluded or unresolved leads. That is a source count, not a count of independent reviews.

### The central finding

The strongest story is the progression from retrieval to a scoped application that can be tested, observed, and improved. Participant-authored learning notes and public project repositories support that story more concretely than generic praise. Eduardo discusses retrieval difficulties; Vancesca endorses evaluation alongside development; public capstones document tests, failure cases and trade-offs. [[S11](https://www.linkedin.com/posts/edugonzaloalmorox_lessons-from-the-first-week-of-the-ai-bootcamp-activity-7385917817474322432-q2G-), [S12](https://www.linkedin.com/posts/agrigorev_just-got-a-new-review-for-my-ai-bootcamp-activity-7409140793849851904-wXX7), [P01](https://github.com/Amar-Ag/ats-gap-analyser), [P02](https://github.com/leo-cabibihan/chess-coach-agent), [P08](https://github.com/larsvasseldonk/datawarehouse_agent)]

The public evidence is encouraging, but not a representative satisfaction survey. Maven displays 4.7 (40), yet the 40 individual review texts were not available in the accessible page. Instructor-shared reviews, prospective endorsements and project showcases must not be relabeled as 40 independently examined graduate reviews. [[S01](https://maven.com/alexey-grigorev/from-rag-to-agents), [S13](https://www.linkedin.com/posts/agrigorev_just-received-a-new-testimonial-for-the-ai-activity-7404535444891414528-hfe1), [S14](https://www.linkedin.com/posts/agrigorev_got-a-new-review-from-cohort-2-of-the-ai-activity-7451162686756806657-dxeo), [S15](https://www.linkedin.com/posts/vancesca-dinh_ai-engineering-buildcamp-from-rag-to-agents-activity-7375803828488642560-hVNi), [S16](https://www.linkedin.com/posts/tim-becker-aachen_ai-bootcamp-from-rag-to-agents-by-alexey-activity-7373802527433195520-kFim)]

### Findings that change the article

The course has evolved. The January redesign followed feedback about overly fast pacing. The current cohort is September 21–November 22, 2026, while a six-week promise remains in one part of the sales page. The article uses the current dates and explains the redesign rather than recycling the old duration. [[S01](https://maven.com/alexey-grigorev/from-rag-to-agents), [S02](https://aishippingblog.com/p/ai-bootcamp-becomes-ai-engineering)]

Some social proof belongs to another course. Luis C. S.’s TacticMate and Elina Nagarnowicz’s completion posts explicitly concern LLM Zoomcamp. Ayuna Barlukova’s LLM Zoomcamp participation is confirmed, but the exact original diet-project testimonial was not recovered. None should be presented as verified paid-Buildcamp graduation evidence. [[S01](https://maven.com/alexey-grigorev/from-rag-to-agents), [S24](https://www.linkedin.com/posts/luiscs_llmzoomcamp-ai-datascience-activity-7257788358892900353-9nz9), [S25](https://www.linkedin.com/posts/elina-nagarnowicz_llmzoomcamp-machinelearningzoomcamp-ai-activity-7253028751620358145-tsSx), [S26](https://www.linkedin.com/posts/ayuna-barlukova_github-datatalksclubllm-zoomcamp-llm-activity-7232764477182558208-H612)]

Project metrics need their original meaning. Amar’s 88% recall describes an LLM judge’s failure detection, not recruitment success or overall application accuracy. Lars’s project seeds a local warehouse; it is not evidence of deployment at Dutch Railways. The repositories also disclose unfinished operational work. [[P01](https://github.com/Amar-Ag/ats-gap-analyser), [P08](https://github.com/larsvasseldonk/datawarehouse_agent)]

There is criticism worth retaining. Public concerns include pace, affordability, learner accountability and instructor credibility after a separate production-database incident. These have different evidentiary status; they should neither be hidden nor combined into an invented negative graduate-review consensus. [[S02](https://aishippingblog.com/p/ai-bootcamp-becomes-ai-engineering), [S17](https://www.linkedin.com/posts/agrigorev_can-you-build-ai-agents-without-prior-ai-activity-7366726267938738176-NGWV), [S18](https://aishippingblog.com/p/how-i-dropped-our-production-database/comments), [S19](https://www.reddit.com/r/learnmachinelearning/comments/1t65wrx/looking_for_accountability_partners_for_ai/), [S20](https://www.reddit.com/r/learnmachinelearning/comments/1t9cka1/study_partners_for_ai_engineering_bootcamps/)]

## 1. Course facts, history and unresolved inconsistencies

### Current offer: verified snapshot

The course is titled AI Engineering Buildcamp: From RAG to Agents. Maven lists Alexey Grigorev as instructor, a $1,799 USD price, the September 21–November 22, 2026 cohort, and a 4.7 (40) aggregate. The syllabus summary shows eight live sessions and 203 lessons. These are a September 7 snapshot, not permanent specifications. [[S01](https://maven.com/alexey-grigorev/from-rag-to-agents)]

The page lists one-hour office hours and Monday sessions at 15:00 UTC. It separately lists 3–10 hours/week for asynchronous material and homework and 10–20 hours/week for project work, distributed across the course. The FAQ’s “at least five hours” is not a credible total upper bound. The article avoids advertising this as a one-hour-a-week course. [[S01](https://maven.com/alexey-grigorev/from-rag-to-agents)]

Prerequisites are coding ability, Python, Git, Docker, the command line and an OpenAI or alternative provider key. Included items are recordings/materials with lifetime access, community, live sessions and a completion certificate. The page links the Maven Guarantee rather than supplying a distinct unconditional refund promise. Do not invent refund conditions. [[S01](https://maven.com/alexey-grigorev/from-rag-to-agents)]

The latest blog announcement advertises SUBSTACK for 20% off. The enrollment guide covers employer reimbursement, teams and scholarships; actual availability, tax treatment, scholarship dates and discount stacking were not tested at checkout. The historical scholarship application volume is not enrollment. [[S04](https://aishippingblog.com/p/13-ai-projects-from-ai-engineering), [S07](https://aishippinglabs.com/blog/how-to-join-ai-engineering-buildcamp)]

### Evolution of the course

The first version was called AI Bootcamp. The December 2025 showcase contains four participant projects plus Alexey’s own To-Do reference agent. In January 2026, Alexey announced the Buildcamp rename and approximately 90% re-recording, responding to valuable-but-too-fast feedback. [[S06](https://aishippingblog.com/p/5-ideas-for-ai-agents-and-openais), [S02](https://aishippingblog.com/p/ai-bootcamp-becomes-ai-engineering)]

The redesign separates the core learning path from optional tools and use cases. Students first implement the agent/tool-calling loop and then use PydanticAI as the principal framework. Alternative frameworks and providers are optional exploration, not a requirement to master every named package. [[S02](https://aishippingblog.com/p/ai-bootcamp-becomes-ai-engineering)]

The April walkthrough describes a nine-week path: RAG foundations; a buffer and optional RAG applications; tool-using agents; testing; monitoring; systematic evaluation; capstone refinement; and a final demo/feedback stage. It distinguishes a running Documentation Agent over Evidently documentation, homework, optional examples and the learner’s own capstone. This is a published teaching design, not an independently observed attendance record. [[S03](https://aishippingblog.com/p/last-call-for-ai-engineering-buildcamp)]

The May showcase describes nine projects from cohort two. The September showcase describes 13 submissions from cohort three, including five live presentations, and makes finishing the capstone a continuing priority. These counts establish showcased work, not completion percentages, total cohort sizes or guaranteed outcomes. [[S05](https://aishippingblog.com/p/9-real-life-ai-projects-from-ai-engineering), [S04](https://aishippingblog.com/p/13-ai-projects-from-ai-engineering)]

### Copy that needs reconciliation

The sales page still includes a six-week outcome line alongside the approximately nine-week current calendar. Historical seven/eight-week references should remain historical. “8+ projects,” optional examples and homework should not be combined into a promise that every participant must complete all examples. Eight office hours and nine calendar weeks are not necessarily contradictory. [[S01](https://maven.com/alexey-grigorev/from-rag-to-agents), [S02](https://aishippingblog.com/p/ai-bootcamp-becomes-ai-engineering), [S03](https://aishippingblog.com/p/last-call-for-ai-engineering-buildcamp)]

The earlier April message that another cohort was not planned soon is superseded by the September launch. Likewise, the instructor’s claimed reach across 100,000-plus learners concerns his broader teaching, not paid Buildcamp enrollment. A legacy 45-enrollee social post is an early owner-reported count, not a current total. [[S01](https://maven.com/alexey-grigorev/from-rag-to-agents), [S03](https://aishippingblog.com/p/last-call-for-ai-engineering-buildcamp), [S39](https://www.linkedin.com/posts/agrigorev_im-launching-a-new-iteration-of-my-ai-engineering-activity-7498635450195009536-Kd8G), [S40](https://www.linkedin.com/posts/agrigorev_45-students-have-enrolled-in-the-ai-bootcamp-activity-7380998869507129344-C6XH)]
