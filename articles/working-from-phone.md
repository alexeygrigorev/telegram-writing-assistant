---
title: "Working from a Phone"
created: 2026-05-16
updated: 2026-05-16
tags: [mobile, workflow, agents, tmux, claude-code, codex, opencode]
status: draft
---

# Working from a Phone

Lately I've been at three conferences in a row: first Darmstadt, then Amsterdam, then Porto. The work doesn't slow down for any of that, so I have to keep things moving.[^1][^2][^3][^29]

On top of the conferences, I've been travelling with my child a lot. We went away during the Easter holidays. May 1st was a long weekend in Germany. I'm dictating this just after we got back from another long weekend around 14-15 May. We went to Stuttgart and into the Schwarzwald (Black Forest).[^29]

My day-to-day schedule is uneven on its own:

- I take my child to school in the morning
- I go to the gym
- I have lunch meetings
- I pick the child up at 4 PM

Between all those slots I have lots of commute time. The rest periods between sets in the gym add another minute or two of free time per set.[^17][^29]

I want to use all of that in-between time. I have too many projects on the go - the AI Shipping Labs site alone takes a lot of work. I want them to progress.[^17]

This article is about how I work from the phone during all of that spare time. The slots include trams, school runs, gym rest periods, and planes.[^1][^17]

<figure>
  <img src="../assets/images/working-from-phone/claude-code-session-on-phone.jpg" alt="Claude Code session on phone showing task list and prompt input">
  <figcaption>A Claude Code session on the phone, mid-task</figcaption>
  <!-- Sets the visual baseline for the rest of the article: this is what "working from the phone" looks like -->
</figure>

## A dedicated remote server

Working from a phone is not new for me. I already wrote about this flow in [Shipping Features from my Smartphone with GitHub Copilot](https://alexeyondata.substack.com/p/shipping-features-from-a-tram-stop). I leaned on GitHub Copilot to write code from a tram. Under the hood that was GitHub Actions doing the work for me. It was a kind of "remote environment", but not one I owned - I borrowed GitHub's runtime for each task.

I've been practicing phone work for a long time. My whole DataTalks.Club routine was built around it so I could keep things moving from anywhere.

That's changed in the last few months. I now have a full dedicated Linux server on rent, running 24/7. I use it for everything described here. I connect over SSH and install whatever I need: Claude Code, Codex, OpenCode. They all live there.[^4][^29][^31]

On Android I use a client called Termius. I just SSH into the server through it and run whatever I want.[^5]

## tmuxctl: simplifying tmux

Because I'm connecting remotely and might be on the move, I always need tmux so my sessions don't drop. I create a tmux session and the agents live inside it.[^5]

Once I started using tmux heavily, I realised typing tmux commands from a phone is painful. The usual flow is `tmux new-session -s some-long-session-name` or `tmux attach -t some-long-session-name`. With long session names that is impossible from a phone.

So I built [tmuxctl](https://github.com/alexeygrigorev/tmuxctl) to make this fast:[^5][^6][^7][^29]

- `t` lists all sessions
- `t 1` attaches to the session with index 1
- `t -` creates (or attaches to) a session named after the current folder
- `t -web` creates a separate session with that suffix. In the same folder I can run a code session and a `-web` session running `make dev`

I also lean on Makefiles heavily. From a phone I can't type long commands. I keep everything behind a `make dev` style target. I used Makefiles before, but the phone makes them non-negotiable.[^8]

<figure>
  <img src="../assets/images/working-from-phone/tmuxctl-session-list.jpg" alt="Terminal output of the t command listing tmux sessions by index and name">
  <figcaption>`t` listing all current sessions on the server, ready to attach by index</figcaption>
  <!-- Shows the actual session picker - the part of the workflow that replaces typing long tmux commands -->
</figure>

I know things can be more touchscreen-friendly than this. I have ideas for improving the terminal experience further, but for now this is what I have.[^8]

## Three agents, three aliases

Inside the session I run agents. I use three of them, in order:

1. Claude Code more and more
2. Codex when Claude limits run out
3. OpenCode after that

None of them are new to me - I've been using all three for a while.[^9]

I have aliases for all three:[^10][^11]

- `csp` - Claude with skip permissions
- `cy` - Codex YOLO
- `oc` - OpenCode

When I want to start a session, I just type two or three letters. Usually the sessions are already running. I tend to start them from my computer ahead of time. From the phone I just attach and do something inside.[^11]

I know "skip permissions" and "YOLO" sound reckless, and I'm aware of the risks. They're acceptable for me because of how this server is isolated.

I'm careful with AWS now because one Gemini agent dropped my production database not long ago. I wrote about that in [How I Dropped Our Production Database and Now Pay 10% More for AWS](https://alexeyondata.substack.com/p/how-i-dropped-our-production-database). After that I made sure to never leave AWS access open to an agent.

The agents on this remote dev box don't have access to my main AWS account. They can reach a sandbox AWS account, but only through a temporary 2-hour session. A runaway agent can't touch anything that matters.

If an agent does something destructive, the radius is limited to this one machine. I can rebuild it easily from my bootstrap instructions. That isolation makes the bypass modes safe for me to use here.[^29][^30][^31]

## Portable setup via dotfiles

The aliases and configs don't live on a single machine. They come from my dotfiles project at [github.com/alexeygrigorev/.claude](https://github.com/alexeygrigorev/.claude). I install that project on a machine and it sets up all my aliases automatically. The same dotfiles run on my laptop, my tablet, and my remote server. The configuration is identical everywhere and all managed through Git.

If I ever move to a different machine, one command brings back all my settings for Claude Code, Codex, and OpenCode. That same setup is also what I rely on when restoring the remote server from scratch.[^11][^29]

The dotfiles repo also has skills.[^12]

## Typing by talking: Typeless and Google Recorder

Even with short aliases and tmuxctl, typing on a phone is painful. It gets worse when I want to give an agent a real task. I solve this in two ways.[^12][^13]

First, I use a special Android keyboard called Typeless. I enter the Claude Code session, switch the keyboard into dictation mode, and talk into the phone. Typeless turns my stream of thought into properly structured text - not just a transcript, but something that reads like a written message. The result lands directly in the agent.[^12][^13]

<figure>
  <img src="../assets/images/working-from-phone/typeless-dictated-input.jpg" alt="Claude Code session on phone with a long, well-formed English sentence in the input area">
  <figcaption>A long prompt dictated into Claude Code via Typeless, ready to send</figcaption>
  <!-- Illustrates how Typeless restructures a brain dump into a coherent prompt before it reaches the agent -->
</figure>

There are two problems with Typeless. I'm still on the free version. I already pay for too many things and haven't been ready to add another subscription. That means I hit usage limits.

When that happens I fall back to Android's built-in voice recognition, which is, to put it mildly, not great. With a terminal it gets confused. Agents still mostly understand what I mean, but it's not ideal.[^13]

When the built-in recogniser isn't good enough, I switch to Google Recorder. On the phone I open Google Recorder and record what I want to say. Then I tap Share and create a public link. I send that link to the agent.[^13][^14]

<figure>
  <img src="../assets/images/working-from-phone/google-recorder-share-menu.jpg" alt="Google Recorder share menu with options for audio, transcript, Google Docs, NotebookLM, video clip and link">
  <figcaption>Google Recorder's share menu - I use "Create a link to view on recorder.google.com" to hand the recording to the agent</figcaption>
  <!-- Shows the exact entry point for the recorder-to-agent flow described in the text -->
</figure>

I have a skill that knows what to do with a recorder link. It downloads the audio file from there and transcribes it. The skill recognises when a link is from Google Recorder and runs the transcription path.[^14]

Recorder keeps recording when it's in the background. Right now I'm recording this article while the app is minimised - I'm brain-dumping my ideas for it. Later I'll hand the recording to my Telegram writing assistant. It turns the notes into a readable text I can edit.[^15][^30]

## From a recording to GitHub issues

Once a recording is transcribed, I can hand it to my orchestrator agent. The orchestrator takes the recording, decomposes it into GitHub issues, and starts working on them.[^16]

This is especially useful when I want to give feedback in the background. I open the AI Shipping Labs site on my phone and start using it. As I find issues I record them as I go. I end up with a 20-30 minute file. I send that file to the agent on the phone. The agent transcribes it, decomposes it into issues, and starts work.[^16]

The same approach works on a plane. On a plane I obviously can't SSH anywhere. I run a local version on my own laptop, then record feedback into Google Recorder from the phone. Recorder works offline. When I leave the plane and turn off airplane mode, I push the recordings to the agent and it does the work from there.[^18]

## ssh-auto-forward-android: port forwarding from the phone

The last awkward thing about phone work is port forwarding. The Android apps for SSH port forwarding aren't great. I already had a tool I love on the computer side: [ssh-auto-forward](https://github.com/alexeygrigorev/ssh-auto-forward) [^19]. I described it in [5 Useful Utilities I Built with AI Coding Assistants](https://alexeyondata.substack.com/p/5-useful-utilities-i-built-with-ai). It watches the ports that open on the remote machine and forwards them to localhost. It runs on the computer in Python.[^19][^29]

I needed the same thing on the phone, so I gave the task to one of the agents (probably OpenCode). I asked it to port the thing to Android. The result is [ssh-auto-forward-android](https://github.com/alexeygrigorev/ssh-auto-forward-android), written in Kotlin. I haven't looked inside it, just like I never looked inside the Python version. I don't even know what's in there. But it works the way I need it to.[^19][^20]

The flow is simple. I open the app, hit Connect, it connects, and I see the list of remote ports being auto-forwarded.[^21]

<figure>
  <img src="../assets/images/working-from-phone/ssh-auto-forward-android-ports.jpg" alt="ssh-auto-forward-android showing a list of auto-forwarded ports with traffic counters">
  <figcaption>The Android app listing the ports it is forwarding from the remote server to localhost</figcaption>
  <!-- Shows what "Connected" looks like in practice - the list of live forwarded ports the user can tap on -->
</figure>

When I tap a port row, the browser opens and goes straight to that port on localhost.[^22] In the screenshot above, port 8030 is `llama.cpp` running on the server. Tapping that row drops me into the chat UI.[^23]

<figure>
  <img src="../assets/images/working-from-phone/qwen-coder-via-forwarded-port.jpg" alt="A browser chat UI showing a Qwen2.5-Coder 14B exchange via the forwarded port">
  <figcaption>Talking to a Qwen2.5-Coder 14B server (llama.cpp on port 8030) after tapping the forwarded-port row</figcaption>
  <!-- This is the payoff of the previous screenshot - one tap on the port row and the browser is on localhost talking to the model -->
</figure>

## Looking at things the phone can't show

The phone also can't browse the file system. SFTP works but is awkward. Sometimes I need to see something visually - a picture, a screenshot the agent produced.[^24]

For screenshots I ask the agent to upload them to GitHub, into an issue. I can view the issue on my phone and decide if it's right. Here is an example of [an issue where I have the agent post screenshots](https://github.com/AI-Shipping-Labs/website/issues/655#issuecomment-4460971855).[^24][^25]

I used this approach a bit at first and use it less now. With CI/CD set up, every push runs the tests and auto-deploys to the dev site. I just open the dev site on the phone and see how it looks there. The screenshots-in-issues option still exists when I want it.[^25]

That CI/CD setup is specific to the AI Shipping Labs site, which I'm working on actively. For smaller side projects I don't have a dev environment. The GitHub-screenshots trick is more relevant there.[^26]

For other visual problems I sometimes ask an agent for a small throw-away tool. Recently I needed to pick banners for the website. I couldn't look at them comfortably from the phone. I told Codex to make me a small HTML page that serves on a specific port and lets me like, reject, and comment on banner variants. It's nothing general-purpose, just a one-shot throwaway app. I open it from the phone, mark what I want, done.[^24][^27]

I had been waiting for days for a chance to do this banner review from a computer, and it never came. Eventually I asked Codex for the picker tool so I could like banners and leave comments from the phone. That's how I ended up choosing the banners for the site.[^27]

<figure>
  <img src="../assets/images/working-from-phone/banner-picker-community-launch.jpg" alt="Banner review tool showing the AI Shipping Labs Community Launch banner variants with like/neutral/reject controls">
  <figcaption>The throwaway banner picker: 30 variants of the Community Launch banner, with like / neutral / reject and per-variant comments</figcaption>
  <!-- Concrete example of a one-shot HTML app the agent built so I could review banners from the phone -->
</figure>

<figure>
  <img src="../assets/images/working-from-phone/banner-picker-workshop-liked.jpg" alt="Banner review tool with a liked workshop banner and a comment about removing project-based and adding date and time">
  <figcaption>Same picker on a workshop banner - I can mark a banner liked and leave a note ("not sure why we need 'project-based' there, add date with weekday and time")</figcaption>
  <!-- Shows the comment flow on a specific variant, which is the whole point of using the picker instead of a static gallery -->
</figure>

<figure>
  <img src="../assets/images/working-from-phone/banner-picker-filter-view.jpg" alt="Banner review tool filter view with All/Liked/Rejected/Unreviewed tabs and a Save Feedback button">
  <figcaption>The filter view - "Save Feedback" and "Export Picks" turn the review into something the agent can act on afterwards</figcaption>
  <!-- Illustrates how the throwaway tool closes the loop - my picks get exported back to the agent that built it -->
</figure>

## The Telegram writing assistant

So far I've talked about how I communicate with agents from the phone, but a large part of my work is also writing - I write a lot. As I mentioned in an [earlier post about the Telegram writing assistant](https://alexeyondata.substack.com/p/telegram-assistant), it's an inseparable part of how I work from the phone too.[^17][^29]

All of the above plus my Telegram writing assistant means I can be in the metro, like right now, and still get my thoughts out of my head. I dump them into the Telegram assistant. I can also check on my agents, correct them, or hand them a new task if I need to. I don't have a lot of free time, and this is how I make more of it.[^17][^29]

## Behind the scenes: how this article was made

I use Telegram a lot. Right now, as I'm dictating this, I'm in the metro. Here's a small behind-the-scenes look at how this article came together:[^31]

1. I dictated my thoughts into the Telegram writing assistant, along with screenshots from the phone.[^31]
2. The agent took the brain dump and restructured it into a draft article.[^31]
3. I read the result, didn't like parts of it, and recorded another voice note with corrections. The agent did another polishing pass on top - I ran agents several times this way.[^31]
4. Once the structure was close enough, a human came in for final editing.[^31]

The same flow works for plans and stories: I open the phone, get a stream of thoughts out, then look at it and do the restructuring. Most of the restructuring is done by the agent. What I don't like, I rearrange. And then a human polishes the result.[^31]

## Time accounting for this article

The 40 minutes I usually quote for an article like this is the first draft (the brain dump) not the total. That part happens in the in-between time.

Right now I'm at the gym. I've done my warm-up, I've got a few working sets ahead of me, and between sets I have about two minutes of rest each time. I press pause on Google Recorder, do a working set, come back, and pick up where I left off. I got on the tram earlier, talked into Telegram while riding, took screenshots along the way, then switched to the metro. The brain dump was around 40 minutes.[^28][^29]

After that comes the polishing pass, because the agent doesn't get everything right on the first try. The polishing flow goes like this. I open Google Recorder, open the article in parallel, and read through it while recording voice feedback on what needs to change. When I'm done I send that recording to the Telegram writing assistant, and it folds all that feedback into the article. After that there's another style-polish pass by the agent, and finally the human editing pass.[^29]

In total, several more hours go into editing, maybe 3-4 hours, to bring the article into a proper format. Then Valeria and I go through it together. And out comes the article.[^28]

Earlier, an article like this would have taken me much longer - several days, probably, to sit down, write it, and plan the story. It now takes much less time than before. That's what lets me share interesting material here and keep trying new things constantly.[^28]

## Sources

[^1]: [20260516_175010_AlexeyDTC_msg4040_transcript.txt](../inbox/used/20260516_175010_AlexeyDTC_msg4040_transcript.txt)
[^2]: [20260516_175104_AlexeyDTC_msg4042_transcript.txt](../inbox/used/20260516_175104_AlexeyDTC_msg4042_transcript.txt)
[^3]: [20260516_175208_AlexeyDTC_msg4044_transcript.txt](../inbox/used/20260516_175208_AlexeyDTC_msg4044_transcript.txt)
[^4]: [20260516_175208_AlexeyDTC_msg4044_transcript.txt](../inbox/used/20260516_175208_AlexeyDTC_msg4044_transcript.txt)
[^5]: [20260516_175446_AlexeyDTC_msg4048_transcript.txt](../inbox/used/20260516_175446_AlexeyDTC_msg4048_transcript.txt)
[^6]: [20260516_175456_AlexeyDTC_msg4050.md](../inbox/used/20260516_175456_AlexeyDTC_msg4050.md)
[^7]: [20260516_175535_AlexeyDTC_msg4052_transcript.txt](../inbox/used/20260516_175535_AlexeyDTC_msg4052_transcript.txt)
[^8]: [20260516_175757_AlexeyDTC_msg4056_transcript.txt](../inbox/used/20260516_175757_AlexeyDTC_msg4056_transcript.txt)
[^9]: [20260516_175853_AlexeyDTC_msg4058_transcript.txt](../inbox/used/20260516_175853_AlexeyDTC_msg4058_transcript.txt)
[^10]: [20260516_175903_AlexeyDTC_msg4060.md](../inbox/used/20260516_175903_AlexeyDTC_msg4060.md)
[^11]: [20260516_180033_AlexeyDTC_msg4062_transcript.txt](../inbox/used/20260516_180033_AlexeyDTC_msg4062_transcript.txt)
[^12]: [20260516_180053_AlexeyDTC_msg4064.md](../inbox/used/20260516_180053_AlexeyDTC_msg4064.md)
[^13]: [20260516_180240_AlexeyDTC_msg4068_transcript.txt](../inbox/used/20260516_180240_AlexeyDTC_msg4068_transcript.txt)
[^14]: [20260516_180511_AlexeyDTC_msg4074_transcript.txt](../inbox/used/20260516_180511_AlexeyDTC_msg4074_transcript.txt)
[^15]: [20260516_180728_AlexeyDTC_msg4076_transcript.txt](../inbox/used/20260516_180728_AlexeyDTC_msg4076_transcript.txt)
[^16]: [20260516_180907_AlexeyDTC_msg4080_transcript.txt](../inbox/used/20260516_180907_AlexeyDTC_msg4080_transcript.txt)
[^17]: [20260516_182051_AlexeyDTC_msg4106_transcript.txt](../inbox/used/20260516_182051_AlexeyDTC_msg4106_transcript.txt)
[^18]: [20260516_181332_AlexeyDTC_msg4088_transcript.txt](../inbox/used/20260516_181332_AlexeyDTC_msg4088_transcript.txt)
[^19]: [20260516_181020_AlexeyDTC_msg4082_transcript.txt](../inbox/used/20260516_181020_AlexeyDTC_msg4082_transcript.txt)
[^20]: [20260516_181044_AlexeyDTC_msg4084.md](../inbox/used/20260516_181044_AlexeyDTC_msg4084.md)
[^21]: [20260516_181137_AlexeyDTC_msg4086_transcript.txt](../inbox/used/20260516_181137_AlexeyDTC_msg4086_transcript.txt)
[^22]: [20260516_181410_AlexeyDTC_msg4092_transcript.txt](../inbox/used/20260516_181410_AlexeyDTC_msg4092_transcript.txt)
[^23]: [20260516_181449_AlexeyDTC_msg4096_transcript.txt](../inbox/used/20260516_181449_AlexeyDTC_msg4096_transcript.txt)
[^24]: [20260516_181636_AlexeyDTC_msg4098_transcript.txt](../inbox/used/20260516_181636_AlexeyDTC_msg4098_transcript.txt)
[^25]: [20260516_181737_AlexeyDTC_msg4100.md](../inbox/used/20260516_181737_AlexeyDTC_msg4100.md) / [20260516_181827_AlexeyDTC_msg4102_transcript.txt](../inbox/used/20260516_181827_AlexeyDTC_msg4102_transcript.txt)
[^26]: [20260516_181848_AlexeyDTC_msg4104_transcript.txt](../inbox/used/20260516_181848_AlexeyDTC_msg4104_transcript.txt)
[^27]: [20260515_155640_AlexeyDTC_msg4038_transcript.txt](../inbox/used/20260515_155640_AlexeyDTC_msg4038_transcript.txt)
[^28]: [20260516_182349_AlexeyDTC_msg4111_transcript.txt](../inbox/used/20260516_182349_AlexeyDTC_msg4111_transcript.txt)
[^29]: [20260516_191031_AlexeyDTC_msg4130_transcript.txt](../inbox/used/feedback/20260516_191031_AlexeyDTC_msg4130_transcript.txt)
[^30]: [20260516_193345_AlexeyDTC_msg4138.md](../inbox/used/feedback/20260516_193345_AlexeyDTC_msg4138.md)
[^31]: [20260516_202338_AlexeyDTC_msg4144_transcript.txt](../inbox/used/feedback/20260516_202338_AlexeyDTC_msg4144_transcript.txt)
