---
title: "Telegram Bot Server Migration"
created: 2026-02-13
updated: 2026-02-20
tags: [telegram-bot, infrastructure, deployment, hetzner, claude-code]
status: draft
---

# Telegram Bot Server Migration

Moving the Telegram writing assistant bot and other workloads from a local computer to a dedicated Hetzner server.

## The Problem

The Telegram bot currently requires the computer to be always on. This is not very convenient. I want to be able to turn off the computer without worrying about the bot stopping[^2].

On top of the bot, the agent that builds the community site was running all day. It runs tests - integration tests, Playwright tests. This was severely loading the laptop. The laptop was going crazy at times. There were many agents running - Claude Code with 5-6 sessions in parallel, plus the session working on the site that keeps 2-3 subagents running at all times. Everything was incredibly slow. I had to restart the computer 2 or 3 times in one day. The computer is old, lots of things running on it, need to clean the system somehow - there are many problems. This is a problem - I need to focus on video, but I can't because of technical issues, which is very frustrating. I decided to finally move everything to the cloud[^4].

## The Original Plan

We set up an n8n server some time ago but never really used it. Now instead of n8n, I want to repurpose that server to run the Telegram bot. I also want to run other things on it, including OpenCode[^1].

## Choosing Hetzner Dedicated Servers

I already had experience running Claude in the cloud - I wrote about it before. I have many Telegram bots. I had an Amazon machine - ARM architecture with 2 cores. I was paying something like 5-10 EUR per month for it. I wanted something more powerful but not too expensive. All more powerful machines cost decent money - 50-60 or even 200-300 EUR per month. I was not ready to pay that much, but I wanted more memory, and more memory means paying more[^4].

I found Hetzner dedicated servers - not a virtual instance, but an actual physical server in a rack that you rent. You get full access to the actual hardware. This is cheaper than cloud VMs - more hassle with configuration (AWS is very easy to set up, here you need to configure things), but the price is much better. For a server with 64GB RAM, 6 cores / 12 threads - a good configuration - only 40 EUR per month. A similar configuration on AWS would cost 300-350 EUR per month[^4].

## Configuring with Claude Code

I did not do the configuration myself - it was evening, no time to figure things out. I told Claude Code "here is the password, go configure everything, then change the password so you do not know it"[^5].

It did not work from the first try. The server came with a rescue OS that needs to be replaced. Hetzner has a special interactive script for installing the OS that Claude could not handle. Claude messed up the machine, and I had to restart and do part of it manually. This took about 20 minutes[^5].

After the OS was installed, I asked Claude to generate an SSH key and set up SSH access. I naturally do not log in as root - I asked Claude to create a user for me and I changed the password on my user. I dictated the list of what to install: Ruby, Node, Python, Docker. I told Claude to take my GitHub SSH key and put it on the server, clone the projects I am currently working on, and copy the credential files I need (like OpenAI keys). I also told Claude to install itself on that server. I had to intervene a couple of times, but the process was successful overall[^5].

## Migrating Bots from AWS

I asked Claude to take the bots that were running on AWS - on that instance I mentioned - and move them too. The bots and crontab were there. Claude moved everything over. I checked what it was doing - everything looked fine. After that, I deleted the old AWS instance. I was paying 10 EUR per month for that. Now I pay 40 EUR per month but for a much more powerful machine that runs all the bots that were already on AWS[^5].

## Security Setup

### Firewall

I asked Claude Code to configure the firewall and verify it. If any application starts on the server, there is no access from outside. Only port 22 (SSH) is open, everything else is closed. I connect via SSH, do port forwarding, and can work. I also set up VS Code to connect there[^6].

All of this took less than an hour to configure[^6].

### Credentials

I am not moving my AWS admin key to the server. If someone compromises it, all infrastructure is at risk. The OpenAI key is project-specific - if it gets compromised, I can just delete it, and I have spending limits configured to get notifications if someone starts spending money[^5].

I am currently researching HashiCorp Vault for forwarding credentials. The idea is to create a temporary session on my laptop, then when I connect via SSH, the temporary keys are used. While the session runs, keys exist. When it stops, keys are gone[^5].

On the other hand, some things are better not done on this server at all. I am somewhat worried that an LLM might go to the AWS credentials folder, read the file, and send it somewhere. If a library is infected, that is dangerous. I have not added AWS credentials yet. I am doing research on how to do this properly. I am thinking of just not putting AWS credentials there at all. In the end, I will probably just do all infrastructure work locally[^5].

There is risk of infected packages on the local laptop too, but it seems smaller than on a remote Hetzner server. While speaking this message, I realize the laptop also needs to be more careful[^5].

### SSH Access

Even if someone sees the IP and tries to get in through port 22, they will not succeed. I set a very complex root password, and my user access is through SSH key. From outside, breaking in should be extremely difficult or impossible. But I am still trying to be more careful with credentials[^6].

## Documentation

The most important thing - I ask Claude to document everything. This seems like a key practice. Claude did some things, not always on the first try - it needed to figure things out. It is important to understand what specifically worked and what did not, and document all of it. If I ever need to reset this server or stop using it and create a new one, I can repeat everything quickly because all the steps are documented. The documentation is useful for both humans and any agent that can read and repeat the instructions[^6].

## Package Security

I have not heard stories about people running Claude Code, it installing an infected library, and credentials leaking as a result. But I think it is a good idea to rewrite certain things yourself rather than using small unknown libraries, because it is not that hard. The ones worth writing yourself are generally small. I have not heard about infected Python packages, but I have heard about JavaScript ones. Big libraries like React are reliable enough that nothing will happen with them. I do not use small unknown libraries[^8].

## Testing the New Setup

I wanted to check that the bot works after the migration. "1, 2, 3" - a connection check. I moved the bot to the new server. Now it lives not locally but on Hetzner. Interesting to see how well it works[^3].

It works. The voice messages I am recording are now being processed by the bot running on Hetzner. I no longer need to keep my laptop always on and running. It can finally breathe freely. I am moving all heavy tasks to the remote server[^7].

I tried running the process to check how everything works. There were unprocessed messages from the day before. I recorded voice messages and was interested to see how the processing would go. I also added code to handle custom audio files (mp4, m4a) - not just voice notes. I tried sending a voice message recorded from another app to see how it would be processed[^9].

It seems nothing happened - need to check the logs to see what went wrong. I will create an issue so I do not forget to check later[^10].

## Sources

[^1]: [20260213_171420_AlexeyDTC_msg1637_transcript.txt](../inbox/used/20260213_171420_AlexeyDTC_msg1637_transcript.txt)
[^2]: [20260213_171440_AlexeyDTC_msg1639_transcript.txt](../inbox/used/20260213_171440_AlexeyDTC_msg1639_transcript.txt)
[^3]: [20260220_064658_AlexeyDTC_msg2091_transcript.txt](../inbox/used/20260220_064658_AlexeyDTC_msg2091_transcript.txt)
[^4]: [20260220_065150_AlexeyDTC_msg2093_transcript.txt](../inbox/used/20260220_065150_AlexeyDTC_msg2093_transcript.txt)
[^5]: [20260220_065848_AlexeyDTC_msg2095_transcript.txt](../inbox/used/20260220_065848_AlexeyDTC_msg2095_transcript.txt)
[^6]: [20260220_070135_AlexeyDTC_msg2097_transcript.txt](../inbox/used/20260220_070135_AlexeyDTC_msg2097_transcript.txt)
[^7]: [20260220_070213_AlexeyDTC_msg2099_transcript.txt](../inbox/used/20260220_070213_AlexeyDTC_msg2099_transcript.txt)
[^8]: [20260220_070341_AlexeyDTC_msg2101_transcript.txt](../inbox/used/20260220_070341_AlexeyDTC_msg2101_transcript.txt)
[^9]: [20260220_070425_AlexeyDTC_msg2103_transcript.txt](../inbox/used/20260220_070425_AlexeyDTC_msg2103_transcript.txt)
[^10]: [20260220_070616_AlexeyDTC_msg2106_transcript.txt](../inbox/used/20260220_070616_AlexeyDTC_msg2106_transcript.txt)
