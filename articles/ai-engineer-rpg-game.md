---
title: "AI Engineer RPG Game"
created: 2026-02-13
updated: 2026-02-13
tags: [vibe-coding, rust, game-dev, glm-5, opencode, agents]
status: draft
---

# AI Engineer RPG Game

An RPG game for practicing AI engineering interview skills, built with OpenCode and GLM-5 in Rust. The long-term vision is to add LLM-powered NPC agents.

Code: https://github.com/alexeygrigorev/game-ai-engineer/[^4]

## How the idea came about

One of my friends and fellow speakers, who I know personally, is very into vibe coding - he has been doing it for a long time and is a real pro at it. I constantly discuss ideas with him. He is going to give a talk at our DataTalks Club soon[^1].

When the new Sonnet came out, he tried making an RPG game with it. He sent screenshots and videos saying "look how well this works." I got interested. He said he wrote it in Rust. I have never done game development - I made text games in the terminal and simple HTML browser games when I was about 12 years old, and that was it[^1].

I was interested to try because I have this understanding that to code something new, you need to understand at least a little bit about it, so you can look at the code and steer it in the right direction[^1].

My long-standing idea is to make an interactive interview preparation trainer as an RPG. When I first started experimenting with agents, I wanted to make an RPG where the NPCs are actual LLM-powered agents. I could walk up to them, talk to them, and learn things from them - with an LLM controlling everything inside. That project stalled, but I want to come back to it[^1].

Today I just pointed OpenCode at my old project and said "look at what is here and let's implement this idea as an RPG in Rust"[^1].

## The implementation plan

GLM-5 built a plan and said it would take about 4 hours to implement[^2].

<figure>
  <img src="../assets/images/ai-engineer-rpg-game/rpg-implementation-plan.jpg" alt="Implementation plan showing 7 phases totaling 4 hours for the RPG game">
  <figcaption>The implementation plan - 7 phases, estimated 4 hours total</figcaption>
  <!-- Shows the phased plan: Macroquad setup, tile map, NPCs, study system, job board, interview quiz, and polish -->
</figure>

I was excited seeing the detailed plan. But 20 minutes later it said "done, check it out." I said "you planned 4 hours but finished in 20 minutes?" It admitted it cut corners. I asked it to show what shortcuts it took, and it listed everything it skipped - about 80% of what was planned was not implemented[^2].

## Testing the game

I tried running it and nothing worked. The graphics were off - the image was flipped, mirrored, and running off screen. One limitation is that I cannot tell the agent to launch the game, look at it, and fix things by itself. I do not know how to set up this feedback loop. With browser-based apps I can imagine launching through a browser and somehow controlling it, but with desktop applications I have no idea how to do this[^2].

I sent a screenshot showing what was wrong. After two more iterations, it got significantly better. By the third iteration, it actually looked like what I wanted. The graphics are very simple - basic shapes - but for a start it is fine[^2].

<figure>
  <p>Video: First version of the AI engineering game (0m 31s, 1080p) - <a href="https://t.me/c/3688590333/1627">View on Telegram</a></p>
  <figcaption>First version of the AI engineering game</figcaption>
  <!-- Screen recording showing the RPG game running with basic graphics and character movement -->
</figure>

I was doing this in the background while my main focus was course recording and video production. OpenCode sends push notifications when work is ready. I would get a notification, switch over to check, and if something did not work, I would send a screenshot and let it keep fixing while I went back to my main work[^2].

## Future plans

I want to attach LLMs to all the NPC characters. I will use some LLM - maybe OpenAI, maybe Anthropic, I have not decided yet. They do not need to be full agents - just conversational, like a conversational chatbot with some prompts. The NPCs should be characters I can walk up to and have actual conversations with[^3].

For agents, the maximum would be a database with interview questions. Both the player and the agents could have some memory. I have not figured out all the details yet[^3].

The NPCs could have different roles - for example, recruiter agents. The gameplay mechanic would be leveling up your character by passing interviews[^1].

I plan to work on this after I finish the current course. I think this would be a great thing for the new community - something for people to play with[^3].

## Sources

[^1]: [20260213_144259_AlexeyDTC_msg1605_transcript.txt](../inbox/used/20260213_144259_AlexeyDTC_msg1605_transcript.txt)
[^2]: [20260213_145555_AlexeyDTC_msg1608_transcript.txt](../inbox/used/20260213_145555_AlexeyDTC_msg1608_transcript.txt)
[^3]: [20260213_145721_AlexeyDTC_msg1609_transcript.txt](../inbox/used/20260213_145721_AlexeyDTC_msg1609_transcript.txt)
[^4]: [20260213_182206_AlexeyDTC_msg1647.md](../inbox/used/20260213_182206_AlexeyDTC_msg1647.md) - GitHub repository link
