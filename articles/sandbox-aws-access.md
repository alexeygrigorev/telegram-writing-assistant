---
title: "Sandbox AWS Access Without Distributing Keys"
created: 2026-06-10
updated: 2026-06-10
tags: [aws, security, workshop, agents, lambda, codespaces]
status: draft
---

# Sandbox AWS Access Without Distributing Keys

This is for anyone who needs to hand out AWS access to people or to coding agents without handing out long-lived keys. It started as a workshop problem and turned into something I now use every day for running agents safely.

I teach and run workshops. That's my main focus right now. At some point this year people from Exasol approached me. Exasol is a database company, and they asked me to run a workshop for them. I said yes, and then I went home and had to figure out how to actually do it[^1].

Exasol released a new version of their database called Exasol Personal. It's normally a paid service, but with this new thing you can roll it out in your own AWS account. You just need an AWS account and a few permissions to provision the resources, then you create a cluster and use it from your laptop. I played with it and it worked[^1].

The problem was the workshop. Imagine 50 or 60 people in a room. Every single one of them needs access to this system: one EC2 machine and a bunch of other resources. Each one needs it to provision their own Exasol Personal instance. How do I make that possible for people who don't have their own AWS account?[^1]

## Distributing keys doesn't work

The obvious idea is to give people my key. I didn't want to do that. How would I even distribute it - type it from the screen, send it by email? And once a key is out there, anyone who has it can provision whatever they want and start mining bitcoin on my account. Too many open questions, and none of the answers were good[^1].

The experience I wanted for attendees was simple. You sit down with your laptop, you connect, and you can provision the resources. No keys to copy around[^1].

I started thinking about EC2 instance profiles. If you attach an instance profile to an EC2 instance, that instance always has access to certain resources, and you never deal with keys. So I could give an EC2 instance all the permissions it needs and let it provision resources from there[^1].

But that runs into the same wall. With 50 or 60 people, each one needs their own EC2 instance to create their own Exasol Personal instance. And to provision that EC2 instance in the first place, they again need a key. The key problem comes right back[^1].

There was one more thing I wanted. I like using GitHub Codespaces for workshops. You click a button and you get a remote machine with everything already installed. You connect to it from VS Code, and every participant has the exact same environment.

It's convenient, so I wanted to use Codespaces here too. Whatever solution I picked had to work from a Codespace, not just from an EC2 instance[^1].

## Instance profiles under the hood

Before solving this, I had to understand how instance profiles work. They feel magical. You attach a profile to an EC2 instance and it can call all the services you need, with no keys anywhere. So how does that happen?[^1]

You launch an instance, you access a service, and it works. There are no keys you can see, but there are keys you just don't see them.

Here's the sequence:

1. You launch an instance with a role attached to it.
2. EC2 sees the attached role and, under the hood, calls STS to assume that role.
3. STS returns temporary credentials, good for something like 20 to 30 minutes.
4. Those credentials get saved on the instance metadata, where every AWS SDK looks for them - boto3 sees them, the AWS CLI sees them.
5. When they expire, they're automatically refreshed.

From your point of view it just works. The credentials are temporary and they rotate automatically, and you never know any of this is happening[^1].

I wanted exactly the same thing, but working outside of AWS - the same instance-profile experience from a Codespace, on any machine[^1].

## Instance profiles outside AWS with a credential URL

The answer turned out to be one environment variable: `AWS_CONTAINER_CREDENTIALS_FULL_URI`. You set it just like you'd set a key, and it specifies the full HTTP URL endpoint the SDK calls when it needs credentials. Normally containers use it, but it works anywhere[^1].

So you configure that environment variable, then you stand up any web service to answer on that URL. In my case it was Lambda, but it could be anything. The Lambda assumes a role, gets temporary credentials, and returns them. The SDK takes those credentials and uses them. This works on any machine - it doesn't have to be EC2[^1].

In practice the flow looks like this:

1. The first time you use an AWS service - boto3 or the AWS CLI - the SDK sends a request to the Lambda configured in the environment variable.
2. The Lambda assumes a role and gets temporary credentials.
3. Those credentials are propagated back to the SDK, which caches them, just like with instance profiles.
4. After some time, depending on how long you set the temporary credentials to live, they refresh automatically without you knowing.

It's the same as instance profiles. The only difference is the Lambda in the middle[^1].

<!-- illustration: sequence diagram - SDK calls the Lambda URL from AWS_CONTAINER_CREDENTIALS_FULL_URI, Lambda assumes a role via STS, returns 15-minute credentials, SDK caches and auto-refreshes -->

## The workshop setup

With the mechanism settled, here's what I built before the workshop[^1]:

1. Created a sandbox account. I didn't want to use my personal account, so I made a separate sandbox account that I could delete easily. These were 50 people I didn't know, and I didn't know their intentions.
2. Created the Lambda in that sandbox account.
3. Created a repository template that everyone would fork. The template has a dev container - it's like a Docker image, but for Codespaces - so all the settings are already there.

During the workshop, people forked the repo, and I shared a secret with them. The code was open, so anyone with GitHub access could see it and provision resources to mine bitcoin or whatever. To make it more secure I added a secret that I only shared offline. I wrote it on the screen during the session - something funny, I think it was "bananas". People created their Codespaces, and the workshop happened[^1].

For the participants it was seamless. The first time their Codespace needed an AWS resource, the SDK sent a request to the Lambda, the Lambda handed back permissions, and they could provision what they needed. They didn't even know the Lambda existed. All they did was click a button in GitHub to get a Codespace, and from there the whole thing worked[^1].

After the workshop I just rotated the secret, or removed the sandbox account completely. The whole setup is on GitHub if you want to check how it works: [aws-workshop-credentials](https://github.com/alexeygrigorev/aws-workshop-credentials) for the credential-vending Lambda and [exasol-workshop-starter](https://github.com/alexeygrigorev/exasol-workshop-starter) for the dev-container template[^1].

## Giving coding agents AWS access

The same trick solves a problem I have with coding agents. Maybe you also use coding systems like Claude Code or Codex, and sometimes they need to use AWS[^1].

I was running them on my computer, and I'm guilty of running them in skip-permissions mode. Skip-permissions mode means the agent doesn't ask every time it wants to read or change something - it's annoying to approve each step, so I just told it to do whatever it wants. What could go wrong?[^1]

Some things went wrong. One of the agents dropped my production database. I have a postmortem about it: [How I Dropped Our Production Database and Now Pay 10% More for AWS](https://alexeyondata.substack.com/p/how-i-dropped-our-production-database).

When you delete an RDS instance, the backups are deleted with it. I thought I had daily backups to fall back on, but I didn't. I opened support requests to recover the database but couldn't, and recovery only became possible after I upgraded to business support.

This talk isn't about that incident. It's the reason I now think hard about how agents get AWS access[^1].

So the question became how to give AWS access to agents safely. My setup is a laptop running agents, with admin credentials to AWS sitting on it.

Here's what I changed[^1]:

1. Got a sandbox server I can SSH into, and moved the agents there. The agents run on that remote server, not on my laptop. If one of them decides to drop the database, it simply can't - it has no access. They can do whatever they want on the sandbox, because if something goes wrong I can recreate the whole thing from scratch. Every configuration is easily recreatable. I don't want agents to nuke it, but if it happens, it's fine.
2. For real deployments, I use CI/CD and all the usual best practices. If I need to apply a Terraform change, I let the agents create the files, they push to GitHub, and I apply it from my laptop. On my laptop I never use skip-permissions mode, so I stay in control of what happens.

That covers safe deployment. But sometimes I want to let agents actually experiment with AWS, to figure out how to deploy a new service or what resources it needs, without sitting there monitoring every step. I want to give them freedom to explore in a safe environment, so that at the end they've built something that works and I can port it[^1].

For that I created a sandbox account. When I want to give agents access to it, I run a script. The script creates a credential file in the folder where the agents work for that project. They read that file and get temporary access to the sandbox account, say for one hour.

It also runs in interactive mode. I say I want to give credentials to a server, then I pick which folder to drop the file into. The tool is [aws-sandbox-cli](https://github.com/alexeygrigorev/aws-sandbox-cli)[^1].

## A toggle on my phone

There's one more case. Sometimes I'm not at my laptop - I'm on my phone. I can SSH into the remote sandbox from my phone using Terminus, an SSH client you install on the phone. I travel and I'm on the go often, and I might want to let agents figure out some inference work while I'm away from my desk[^1].

The problem is credentials. I don't have admin AWS credentials on my phone, and I don't want them there - why would I keep my AWS credentials on my phone? When I'm traveling my laptop is in my backpack, but when I'm just out and about it's at home, and SSHing to it isn't trivial since it sits behind a router. I also didn't want to just let agents hit AWS whenever they please. They might provision 10 GPU instances and then I'd have to sell a kidney to pay the bill[^1].

So I reused the credential-URL trick again. I built an app I can turn on and off. The remote sandbox has the credential URI pointing at a Lambda. When the toggle is on, the Lambda hands out credentials. When it's off, the sandbox tries to get credentials and can't.

The access is temporary, and I can limit it to one hour. When I need agents to run an experiment, I open my phone, flip the toggle, and turn it off when I'm done. The tool is [phone-aws-gate](https://github.com/alexeygrigorev/phone-aws-gate)[^1].

Here's the live demo. I connect to the remote server and run `aws sts get-caller-identity`, and it fails because there's no access. I flip the toggle on my phone, it asks for my fingerprint, and it grants 15 minutes with a timer running. Now `get-caller-identity` works. I flip the toggle off, and access is gone again[^1].

<!-- illustration: phone screen showing the AWS access toggle with the 15-minute countdown timer -->

I vibe-coded the whole thing, and it's turned out to be quite useful[^1].

## Sources

[^1]: [Sandbox AWS Access Without Distributing Keys (talk recording)](https://www.youtube.com/watch?v=bScTPc0RnXU), [20260610_123249_AlexeyDTC_msg4527.md](../inbox/used/20260610_123249_AlexeyDTC_msg4527.md), [20260610_123620_AlexeyDTC_msg4529.md](../inbox/used/20260610_123620_AlexeyDTC_msg4529.md)
