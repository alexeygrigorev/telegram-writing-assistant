---
title: "Exasol Workshop Infrastructure Setup"
created: 2026-03-06
updated: 2026-03-11
tags: [workshop, aws, security, exasol, devcontainers, codespaces]
status: draft
---

# Exasol Workshop Infrastructure Setup

Preparing for a Tuesday workshop with Exasol. The main challenge: everyone needs the same infrastructure, and some participants will come without their own AWS account. They need the ability to create their own Exasol Personal instance, which requires AWS access.

## The Problem

Giving AWS keys directly to workshop participants is risky. They could use the keys to create EC2 instances, mine bitcoin, or do anything else. The key could also leak.

## Solution: Instance Profile-like Mechanism Outside AWS

The idea is to replicate the AWS instance profile mechanism but outside of AWS, for use with GitHub Codespaces.

With instance profiles, if something happens, the key cannot leak. Even if someone gets onto the machine, they can only do what's available from that machine. The keys are temporary and have a short lifespan - something like 5-10 minutes.

The solution uses a Lambda function that issues temporary credentials by creating temporary sessions. The AWS CLI requests a key first, then uses it, and stores everything locally. This is essentially the same mechanism as instance profiles, just not tied to EC2 instances.

## DevContainers and Codespaces

Everything is set up in DevContainers so that when participants create a Codespace, all the necessary settings are already there. Participants just need to press a button and everything works.

To get AWS access from the Codespace, two things are needed: a URL and a token.

## Token Security

The token should not be published openly on the internet - someone could find the repository, use the token, and get access to start mining bitcoin.

The solution: encrypt the token and store it in the repository in encrypted form. The decryption key (passphrase) is given to participants during the workshop session itself. At the start of the workshop, participants are told to clone the repository, go to settings, and create a secret with the passphrase.

This minimizes the damage window. During the workshop itself, people could potentially misuse the access, but the window is only 1.5 hours. The probability of malicious hackers attending a workshop to mine bitcoin instead of learning is quite low.

Additionally, the Exasol team will monitor the account status and shut down any suspicious activity.

## Credential Flow

The Codespace uses the AWS SDK to request temporary credentials from the Lambda function. The Lambda calls AWS STS to assume a workshop participant role and returns short-lived credentials (15 minutes). The SDK caches these credentials and auto-refreshes them before expiry[^2][^3].

<figure>
  <img src="../assets/images/exasol-workshop-infrastructure/credential-flow-diagram.png" alt="Sequence diagram showing credential flow between Codespace, Lambda, and AWS STS">
  <figcaption>Credential flow: Codespace requests temporary AWS credentials via Lambda, which calls STS to assume a workshop participant role</figcaption>
  <!-- Rendered from the mermaid diagram provided by Alexey, showing the full request-response cycle for temporary credential issuance and auto-refresh -->
</figure>

## Workshop Results

The workshop ran successfully. The temporary credential system worked as planned - participants got AWS access from Codespaces without receiving direct AWS keys. After the workshop, the Lambda function is simply disabled, cutting off all access[^2][^3].

A separate video recording is being prepared since the live workshop recording did not come out well. This can be shared in the newsletter[^4].

## Sources

[^1]: [20260306_162155_AlexeyDTC_msg2776_transcript.txt](../inbox/used/20260306_162155_AlexeyDTC_msg2776_transcript.txt)
[^2]: [20260311_192843_AlexeyDTC_msg2818_transcript.txt](../inbox/used/20260311_192843_AlexeyDTC_msg2818_transcript.txt)
[^3]: [20260311_192913_AlexeyDTC_msg2822_transcript.txt](../inbox/used/20260311_192913_AlexeyDTC_msg2822_transcript.txt)
[^4]: [20260311_192843_AlexeyDTC_msg2819_transcript.txt](../inbox/used/20260311_192843_AlexeyDTC_msg2819_transcript.txt)
