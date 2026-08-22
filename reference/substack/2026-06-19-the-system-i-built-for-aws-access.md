---
title: "The System I Built for AWS Access Without Keys"
date: 2026-06-19
url: https://aishippingblog.com/p/the-system-i-built-for-aws-access
---

I sometimes run offline workshops. These workshops require participants to have access to cloud resources such as AWS. This is okay when people come prepared, but often it’s not the case.

This happened when Exasol, a database company, asked me to run a workshop for them. They released a new version of their database, Exasol Personal. It’s normally a paid service, but this edition runs in your own AWS account. You need an account and a few permissions, then you can create a cluster and use it from your laptop.

[![Image 1](https://substackcdn.com/image/fetch/$s_!FnCR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf8b3925-5ffa-4a56-a2fa-421b8f27d1b8_1798x676.png)](https://substackcdn.com/image/fetch/$s_!FnCR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf8b3925-5ffa-4a56-a2fa-421b8f27d1b8_1798x676.png)

For me, it was very easy to set it up. But then I started thinking about how to make it scale to 50-60 workshop participants, who will most likely be unprepared.

So I needed to find a way for the participants to provision resources in my AWS account without giving them my AWS keys.

The solution I found turned out to be useful not only for workshops, but also for coding agents. I don’t want to give my agents permanent access to my main AWS account. Instead, I want to restrict them to a sandbox environment and decide when and for how long they can have access.

This article is based on the workshop that I ran at the Berlin AWS Group meetup. Watch the [recording](https://youtu.be/bScTPc0RnXU?si=R5KDk1Ld6p-QiE_R) below and check out the [slides](https://docs.google.com/presentation/d/1wrH2we0J4atE3Dt2afbhygyoyATCLybGIBdfj84IMYM/edit) from this talk.

## The workshop problem

[![Image 2](https://substackcdn.com/image/fetch/$s_!1OrG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9407f6de-cf55-4cb1-b55a-b879745a6722_1788x544.png)](https://substackcdn.com/image/fetch/$s_!1OrG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9407f6de-cf55-4cb1-b55a-b879745a6722_1788x544.png)

I needed to find a way to give 50 or 60 people in a room access to provision AWS resources from their own machines, with nothing to install and no keys to copy. You sit down, open the workshop environment, and it works.

I didn’t want to give the participants my AWS key. First, it’s a very bad idea for security reasons. Second, how do I even do it?

[![Image 3](https://substackcdn.com/image/fetch/$s_!TbEt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1bc3e6cc-da88-43f2-9210-7807b0fa2f6c_1802x676.png)](https://substackcdn.com/image/fetch/$s_!TbEt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1bc3e6cc-da88-43f2-9210-7807b0fa2f6c_1802x676.png)

Type it on the screen, send it by email, drop it in a repo for a few minutes? Once a key is out, anyone who has it can provision whatever they want until I disable it. If somebody starts mining Bitcoin on my account, that’s my problem.

I also didn’t want to use my main AWS account. I’m not a security expert, and with 50+ people I don’t know (and don’t necessarily trust), things may go wrong.

And finally, I wanted to run in GitHub Codespaces. It’s very convenient, and I use it for all my workshops. You click a button and get a remote machine with everything installed and the same environment as everyone else. I didn’t know if it’d be possible for this workshop, but I wanted to find an equally convenient option.

## EC2 instance profiles

The first thing I thought about was EC2 instance profiles.

[![Image 4](https://substackcdn.com/image/fetch/$s_!rUJD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d6f0ad3-e63d-4ddd-93e2-8de605f76d99_1802x786.png)](https://substackcdn.com/image/fetch/$s_!rUJD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d6f0ad3-e63d-4ddd-93e2-8de605f76d99_1802x786.png)

You attach a role to an instance, and when you start it, it gets access to all the resources you configured. You don’t need to worry about managing keys: EC2 does it for you.

But to create instances with the profiles, I’d need to distribute my key to the participants again, who would then use it to provision the instances.

So I wanted something that’s like EC2 instance profiles, but it would work without having to share my keys, and ideally outside of AWS – on GitHub Codespaces.

I needed to reproduce the way instance profiles work. The flow in EC2 looks like this:

1. You launch an EC2 instance with a role attached
2. EC2 calls STS and assumes that role
3. STS returns temporary credentials
4. Those credentials become available through the instance metadata service
5. The AWS CLI, boto3, and other SDKs know where to find them
6. When the credentials expire, AWS refreshes them automatically

If I could do something similar, but for Codespaces, it’d solve my problem: when the workshop is over, I just deactivate the profile, and my key is never used.

[![Image 5](https://substackcdn.com/image/fetch/$s_!cVpp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba0a7e00-3044-4c4c-9c3b-c2d7dec37d77_1802x1004.png)](https://substackcdn.com/image/fetch/$s_!cVpp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba0a7e00-3044-4c4c-9c3b-c2d7dec37d77_1802x1004.png)

## What I built: a credential endpoint I host

I started looking for alternatives and found this environment variable:

```
AWS_CONTAINER_CREDENTIALS_FULL_URI
```

It tells the AWS SDK where to fetch credentials. It is typically used in container environments, but it also works outside them. So I can point it to an HTTP URL and run a small service behind it. The service needs to create temporary credentials, and when they expire, the AWS SDK automatically asks for a refresh.

In my case, I created a Lambda that assumes an AWS role and returns temporary credentials in the format the SDK expects.

[![Image 6](https://substackcdn.com/image/fetch/$s_!uWUS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8cca88c7-44a4-4749-abd9-191c34e31ca5_1796x1000.png)](https://substackcdn.com/image/fetch/$s_!uWUS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8cca88c7-44a4-4749-abd9-191c34e31ca5_1796x1000.png)

It’s the same flow as instance profiles, but I provide the endpoint instead of AWS doing it via the metadata service.

It moves the mechanism off EC2 and lets it run anywhere the SDK runs, including a Codespace.

## Wiring it into Codespaces

I didn’t want this anywhere near my personal account. So I created a separate AWS sandbox account, put the Lambda there, and built a repository template for the workshop. The template carried a dev container, so when participants forked the repo and opened it in Codespaces, they got the right tools and the credential URL already configured. They opened a Codespace, ran the workshop commands, and the SDK pulled credentials from the Lambda. They never had to know the Lambda existed.

Second, the repo was public, so anyone with the URL could find the credential endpoint, and I didn’t want the Lambda handing out credentials to the whole internet. So I added a secret check and shared the secret offline during the workshop. I wrote it on the screen. I think it was something funny, like bananas.

You can check the code for this on GitHub:

1. [aws-workshop-credentials](https://github.com/alexeygrigorev/aws-workshop-credentials) for the credential-vending Lambda.
2. [exasol-workshop-starter](https://github.com/alexeygrigorev/exasol-workshop-starter) for the dev-container template.

## The same problem with coding agents

The same pattern helps with coding agents.

Maybe you use Claude Code or Codex too, and sometimes they need AWS. I was running them on my laptop, where I also kept admin AWS credentials. And I am guilty of running them in skip-permissions mode, where the agent doesn’t ask before reading a file, running a command, or changing something. Approving every small step is annoying, so I told it to do whatever it wanted.

What could go wrong?

Plenty. One of the agents dropped my production database. I wrote about that here: [How I Dropped Our Production Database and Now Pay 10% More for AWS](https://alexeyondata.substack.com/p/how-i-dropped-our-production-database). When you delete an RDS instance, the backups go with it. I thought I had daily backups to fall back on. I didn’t. I opened support requests, couldn’t recover anything, and recovery only became possible after I upgraded to business support.

[How I Dropped Our Production Database and Now Pay 10% More for AWS](https://alexeyondata.substack.com/p/how-i-dropped-our-production-database)

This post isn’t about that incident. But that incident is the reason I now think about how agents get AWS access at all. The rule I took from it: an agent should never have a path to production.

My first step was to move agents to a remote sandbox server. If an agent decides to delete something, it can’t do that because it lacks access. The server itself is disposable. I can easily recreate it, so if an agent breaks it, that’s fine.

Second, real deployments go through CI/CD. When I need to apply a Terraform change, I let the agents write the files and push them to GitHub, then I apply the change from my laptop. On my laptop for infra work, I don’t use skip-permissions mode, so I stay in control of anything that touches real infrastructure.

But sometimes I want my agents to experiment with infra on AWS. It happens when I need to work out how to deploy a new service, which resources it needs, and which permissions it requires. For this, I created a separate sandbox AWS account. When agents need access to it, I run a script that writes a credential file into the project folder the agent is working in, and the agent gets access for about an hour. The tool is [aws-sandbox-cli](https://github.com/alexeygrigorev/aws-sandbox-cli).

The result is that agents have enough room to explore and break things, but only within the sandbox, and never on a path that reaches production.

## Turning access on from my phone

But sometimes I’m not at my laptop, I’m on my phone, and I still want agents to work. I travel often, and now and then I want to let an agent figure out some inference work [while I’m away from my desk](https://alexeyondata.substack.com/p/the-system-i-built-to-ship-code-from).

[The System I Built to Ship Code From a Phone](https://alexeyondata.substack.com/p/the-system-i-built-to-ship-code-from)

I don’t have admin AWS credentials on my phone, and I don’t want them there. Reaching my laptop instead isn’t an option either. When I travel, it’s in my backpack, and when I’m out for the day, it’s at home behind a router, so SSHing into it isn’t trivial. And even when I can access the sandbox, I don’t want agents hitting AWS at will. They might provision ten GPU instances, and then I have a very expensive problem.

[![Image 7](https://substackcdn.com/image/fetch/$s_!n25z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F694f3f6f-0bc7-44ae-8799-dc8df46d023f_1808x1004.png)](https://substackcdn.com/image/fetch/$s_!n25z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F694f3f6f-0bc7-44ae-8799-dc8df46d023f_1808x1004.png)

So I reused the credential URL. The remote sandbox already points its credential URI at a Lambda, so I built a phone app that toggles that Lambda on and off. When the toggle is on, the Lambda hands out credentials. When it’s off, the sandbox asks and fails. The access is temporary, and I can hold it for an hour. When I need an agent to run an experiment, I open the app, flip the toggle on, and flip it off when I’m done. The tool is [phone-aws-gate](https://github.com/alexeygrigorev/phone-aws-gate). I connect to the sandbox from the phone with Termius, an SSH client for phones.

[![Image 8](https://substackcdn.com/image/fetch/$s_!YBEl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a957c24-beac-4606-9885-aca1a4ba03a6_1802x1004.png)](https://substackcdn.com/image/fetch/$s_!YBEl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a957c24-beac-4606-9885-aca1a4ba03a6_1802x1004.png)

caption...

For example, when I connect to the remote server and run:

```
aws sts get-caller-identity
```

It fails because there is no AWS access. I flip the toggle on my phone; it asks for my fingerprint and grants access for 15 minutes, with a timer running. Now `get-caller-identity` works. I flip the toggle off, and the access is gone.

[![Image 9](https://substackcdn.com/image/fetch/$s_!4MZP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fae0a96c0-ddbc-48f3-b948-6c5678cd14aa_1790x998.png)](https://substackcdn.com/image/fetch/$s_!4MZP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fae0a96c0-ddbc-48f3-b948-6c5678cd14aa_1790x998.png)

## Where I use it now

It started as a workshop problem: how do I let 50 or 60 people use AWS without handing out long-lived keys? The answer was a credential endpoint I control. The same endpoint now does two more jobs. It gives coding agents temporary access to a sandbox account and sits behind a toggle on my phone, so I can turn that access on and off from anywhere.

One mechanism covered all three because the underlying need was the same each time: temporary, revocable AWS access with no long-lived keys sitting on a machine.

I run the credential endpoint now, so its security is mine to get right, and the access is only as locked down as I make it. The workshop ran behind a word I wrote on a screen. That was a deliberate trade for a setup I could throw away the same day, not a pattern I’d reuse for anything that had to last.

The rule I follow now is the one the dropped database taught me. Before anything gets AWS access, whether it’s a room full of strangers, an agent, or a script, I ask the same questions. Is the access scoped to a sandbox? Is it temporary? Can I revoke it? And can it reach production? If the answer to that last one is yes, I stop and fix it first.

## What I’ve been working on this week

### Sprint prep with Codex

I spent a lot of the week getting [AI Shipping Labs](https://aishippinglabs.com/) ready for the [next sprint](https://aishippinglabs.com/events/groups/july-2026-community-sprint). Codex ran for over two days on platform features, and I gave it a lot of feedback along the way. Most of it was fixes and polish of existing features, making what already exists look and work better. It kept going until everything on my list was done.

[![Image 10](https://substackcdn.com/image/fetch/$s_!xIQl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e3b4c14-35fe-4857-81e8-2c5ccd65d2f9_1080x1049.png)](https://substackcdn.com/image/fetch/$s_!xIQl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e3b4c14-35fe-4857-81e8-2c5ccd65d2f9_1080x1049.png)

Codex (gpt-5.5) reporting the backlog goal complete: the shipped fixes, around 9.5M tokens, and 2d 11h 39m elapsed

### Cloudflare Workers workshop

[![Image 11](https://substackcdn.com/image/fetch/$s_!iyhj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffbe053fd-bdf5-4691-8da6-67da816b8762_1290x980.png)](https://substackcdn.com/image/fetch/$s_!iyhj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffbe053fd-bdf5-4691-8da6-67da816b8762_1290x980.png)

On Wednesday, we ran an AI Shipping Labs [workshop on Cloudflare Workers](https://aishippinglabs.com/workshops/2026-06-17-cloudflare-workers-vectorize-agent), and it was more interesting than I expected. The idea was to take the FAQ agent from our earlier deployment workshops and move its whole online path onto Cloudflare.

The question we wanted to answer was whether Cloudflare could replace the usual stack for a small FAQ agent: a FastAPI server, a separate vector database, and a paid always-on host.

It mostly can. Cloudflare runs the full online path, with one caveat: ingestion still runs locally as an operator command rather than as a public endpoint, so you load the FAQ into Vectorize yourself when you need to.

We built that path end-to-end, creating credentials and a Vectorize index, ingesting the FAQ, running the Worker locally against the real Cloudflare services, then deploying it and cleaning it up. We also tried a Python Worker rewrite. Workers are still cheap, and for small pet projects, they're close to ideal.

If you want the notes from this workshop, [join AI Shipping Labs](https://aishippinglabs.com/#tiers?utm_source=alexey_on_data&utm_medium=email&utm_content=2026_05_22). The Basic plan includes notes, and the Main plan includes recordings.

### A lighter FAQ assistant, and zerosearch

[![Image 12](https://substackcdn.com/image/fetch/$s_!-WEf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78967d0f-0376-4c34-9fac-54ddc4c6ba47_1772x818.png)](https://substackcdn.com/image/fetch/$s_!-WEf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78967d0f-0376-4c34-9fac-54ddc4c6ba47_1772x818.png)

After that workshop, I tried to port the [DataTalks.Club FAQ assistant](https://github.com/DataTalksClub/faq-assistant) to Cloudflare Workers and make it as small as possible. The Python layer on Workers doesn’t support extra libraries, so I rewrote MinSearch as a zero-dependency, pure-Python library called [zerosearch](https://github.com/alexeygrigorev/zerosearch).

### A shared email service for the course management platform

[![Image 13](https://substackcdn.com/image/fetch/$s_!lut6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75dcc301-0b4e-483a-8fd4-41fd19640e0b_1782x960.png)](https://substackcdn.com/image/fetch/$s_!lut6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75dcc301-0b4e-483a-8fd4-41fd19640e0b_1782x960.png)

I started wiring email into the [course management platform](https://courses.datatalks.club/), which wasn’t possible before. It uses Amazon SES to send mail tailored to our setup, starting with the course management platform.

Emails already work in AI Shipping Labs, which I finished a few weeks ago, but I want to pull the logic into a separate service, [DataMailer](https://github.com/DataTalksClub/datamailer), so all our platforms can share it. My current goal is to get the course management platform emails working first, then move the AI Shipping Labs emails over, and maybe the weekly emails after that. If it ends up replacing MailChimp, great. If not, that’s fine, and we keep MailChimp. But that’s the direction.

I plan to write more about DataMailer in one of my future newsletters. Subscribe to stay updated!

## Interesting Tools

[![Image 14](https://substackcdn.com/image/fetch/$s_!jj1N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7413762a-2f58-4c5a-81ba-ff3f9f59fff4_1706x1336.png)](https://substackcdn.com/image/fetch/$s_!jj1N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7413762a-2f58-4c5a-81ba-ff3f9f59fff4_1706x1336.png)

* [Omnigent](https://github.com/omnigent-ai/omnigent) is an open-source meta-harness from Databricks. It sits above the coding agents you already use (Claude Code, Codex, Pi, the OpenAI Agents SDK, or your own YAML-defined agents) and makes them work together as one system. You can run several agents in a single session, for example, one vendor’s agent reviewing another’s code. Policies like spend caps and approval gates are enforced at the harness layer instead of through prompts, and tools run inside an OS sandbox with an egress proxy that injects secrets the agent never sees. Sessions follow you across the terminal, web, mobile, and a macOS app, and you can share a live one by URL so teammates can watch or co-drive. It’s released under Apache 2.0.
* [Ponytail](https://github.com/DietrichGebert/ponytail) is an AI agent skill that pushes coding agents to write the least code that does the job, what its author calls “the laziest senior dev in the room,” replacing fifty lines with one. Before writing anything, the agent works down a ladder: does this need to exist, does the standard library or a native platform feature already cover it, can it be done in one line? It builds only the minimum that works, but never cuts validation, error handling, security, or accessibility. It installs as a plugin for Claude Code, Codex, and a dozen other agents. On agentic benchmarks, it cut code by around 54% while staying cheaper and faster than the unassisted baseline.

## Resources

Ivan Brigida ran a [workshop on building a Stock Research Agent](https://www.youtube.com/live/MdZLf6C5rW8?si=76oYuKJC5u0DkqKn). He had clearly prepared a lot, and I liked how he presented it.

Edited by [Valeriia Kuka](https://www.linkedin.com/in/valeriia-kuka/)
