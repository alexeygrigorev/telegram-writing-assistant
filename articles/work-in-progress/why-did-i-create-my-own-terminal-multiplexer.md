---
title: "Aplexer - Why I Stopped Using Tmux and Created My Own Terminal Multiplexer"
created: 2026-08-27
updated: 2026-09-17
tags: [aplexer, tmux, rust, coding-agents, terminal-multiplexer]
status: draft
---

## Advantages and disadvantages of tmux and my new agent multiplexer 

tmux is a terminal multiplexer that I use to run agents on a remote machine. I wrote about using it in my article [The System I Built to Ship Code From a Phone](https://aishippingblog.com/p/the-system-i-built-to-ship-code-from).

When you connect to a remote machine with ssh, the processes you launch are bound to your ssh session. That means when you disconnect, or the connection drops, the processes die together with the session. 

A terminal multiplexer is a tool that detaches the processes you start from the ssh session, so they can keep running after the disconnect. Screen and tmux are the most well-known terminal multiplexers, but tmux is more modern and generally preferred among developers. 

I've used tmux for ages but with agents running 24/7 on my remote dev box, it no longer works for me. To replace it, I created [aplexer](https://github.com/alexeygrigorev/aplexer). In this article I'll tell you why. 

In particular, we'll cover:

- What tmux is and how it works
- Advantages and disadvantages of tmux 
- My tool tmuxctl to make tmux easier to manage
- Aplexer as the solution to my current problems with tmux

Let's start!

## Terminal Multiplexer

The [tmux README](https://github.com/tmux/tmux) says:

> tmux is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattached.

It's a layer between you (your ssh session) and the processes you run. 

After I ssh into my devbox, I can start a tmux session:

```bash
tmux new-session -s ai-shipping-labs
```

Under the hood, multiple things happen:

- My terminal becomes a tmux client 
- The client connects to a tmux server
- If the server is not running, the command starts it 

The client connects to the server through a Unix-domain socket. The server creates a session and a PTY for that session. 

TODO: diagram 
user -> ssh -> tmux server -- socket -- tmux client -- PTY

A PTY is a pseudo-terminal created by the kernel. It has two sides:

- the master (user side) - sends the input from the user to whatever is runing in the terminal. 
- the slave (shell side) - receives the input from the master and sends it to shell or whatever programm running in the terminal.  

TODO diagram
user --> PTY master <--> PTY slave <-- shell

When we start the standard terminal emulator app on any Linux, it creates a PTY. The master side is the terminal app, and the slave side is a shell (usually bash).

TODO: image of terminal on Ubuntu 
user --> ubuntu terminal --> PTY master <--> PTY slave <-- shell


When we start a proccess from a PTY, it gets attached to the shell runing on the slave side - unless we explicitly detach it with `nohup`. 

TODO terminal
terminal <-> PTY <-> bash -> claude -> make run

When the PTY stops, the slave exists too, switching off the shell. All the connected processes follow.

```
kill ----------------> kill -> kill -> kill 
terminal <-> PTY <-> bash -> claude -> make run
```

That's why when you're close  a terminal tab in Ubuntu, all the processed that run there exit too.


When we use ssh, the ssh client on our computer connects to the ssh server (sshd) on the remote machine. sshd also server creates a PTY: the master is on the sshd side, and the slave is on the shell side.


TODO diagram
```
    local                                                         remote
---------------------------------------------------------     ------------------------------------
terminal emulator --> PTY <-- bash (local) --> ssh client <-> ssh server --> PTY <-- bash (remote)
---------------------------------------------------------     ------------------------------------
```

When ssh disconnects, sshd stops the PTY that was created for this session, and all the processed die with it.

TOOD diagram with kill propagation

Terminal multiplexers add one more hup: tmux server creates another PTY, and the shell that's running inside that PTY is the parent for all these processes. 

```
 ssh connection                              tmux session
-------------------------------------     -------------------------------------------------------
sshd --> PTY <-- bash --> tmux client <-> tmux server --> PTY <-- bash --> claude -> ...
-------------------------------------     ------------------------------------------------------- 
```

That's why when we stop the ssh connection, all the processes that we started in tmux continue running - they are attached to tmux server's PTY. Only the tmux client dies. 

```
 ssh connection                              tmux session
-------------------------------------     -------------------------------------------------------
kill -----------> kill ----> kill -x-x-x- not propagated

sshd <-> PTY <-> bash <-> tmux client <-> tmux server <-> PTY <-> bash -> claude -> uv run python ...
-------------------------------------     ------------------------------------------------------- 
```


One tmux server holds multiple PTYs. The basic unit of tmux is a pane and each pane has its own PTY. Then there's a window that can have multiple panes inside it, and a session that can have multiple windows. 

<figure>
  <img src="../../assets/images/why-did-i-create-my-own-terminal-multiplexer/tmux-multiple-panes.png" alt="A tmux window with three panes: htop monitors the devbox, an agent session runs in the top-right pane, and a shell lists other sessions in the bottom pane">
  <figcaption>One tmux window with 3 panes: htop, claude and shell.</figcaption>
</figure>


When I create a new session with a command like this:

```bash
tmux new-session -s ai-shipping-labs
```

It creates a session with one window with one pane inside it, and this pane has a PTY. Then I can add a new window or split the current one horizontally or vertically into multiple panes. But I usually don't do that. For me it's always one session - one PTY setup.

One tmux server can have multiple sessions

TODO diagram 

```
            <-> PTY <-> session 1
tmux server <-> PTY <-> session 2
. ...       <-> PTY <-> session 3 
```

This allows me to run many agentic sessions on my remote machine. 


Also we can do a lot of things programmatically with tmux. We can create all these windows and panes using tmix CLI, or we can send input to any of the panes as if it was typed by a human. In fact, the scheenshot above came from [this script](https://gist.github.com/alexeygrigorev/8df0400d8814914291487ada31b4a119).


## Problems with tmux and solving them with tmuxctl

As I started running more and more agents, session management with tmux became more difficult. 

I really struggle with the CLI. The commands are:

```bash
tmux new-session -s ai-shipping-labs
tmux list-sessions
tmux attach-session -t ai-shipping-labs
```

I always forget these commands. Typing all that, even with autocomplete, is always complicated. I never seem to remember what to type and need to look it up.

Also, you have to remember that it's `-s` for new session and `-t` for attach. To make it even more consufing, `new-session` also has the `-t` parameter, but it's not the same as `-s`: (it groups the new session with an existing one. TODO rewrite it to make it clear what's that)

Eventually I solved this problem with [tmuxctl](https://github.com/alexeygrigorev/tmuxctl). I created an executable `tmuxctl` and an alias `t` for it to save typing time.

With it, I can simply run 

```bash
t -
```

It will:

- create a tmux session in the current directory
- name the session after the directory
- if a session already exists, attach to it


If I run just `t` without any arguments, I'll see the list of sessions ordered by creation time.

(TODO attach screenshot)

And if I want to connect to any particular session from that list, I simply run 

```
t 8
```

That made the process more convenient and also saved a lot of time when jumping between sessions.



## OOM and cgroups 

But then there's another problem with tmux - its server is its single point of failure.

On my devbox, I run many things in parallel. 

At the same time, it could be running 

- compiling something in Rust
- running Android emulator tests
- running e2e tests with Playwright 

If I'm unlucky, all these things can run exactly at the same time, and my machine runs out of memory. 

It's usually not a problem for Android emulators or Playwright - they are simply killed when it happens.

But with something like `cargo clippy` (a linter in Rust) it can not only bring `cargo`, but also the agent that's running it, the shell that's running the agent, the session that's running the shell, and the tmux server too. And when tmux server dies, all the other sessions go with it. So an OOM in Rust can wipe out all the tmux sessions on the machine. 

TODO illustation

This problem is not specific to Rust. When there's OOM, the kernel (OOM killer) decides which process should receive SIGKILL. Usually it's just the process that caused the OOM error. But [sometimes](link tmux#4151) it may decide to kill the entire memory cgroup where it's working, which includes the tmux server and all the sessions that it started. 

A cgroup (control group) is a container around a group of processes that Linux manages like a single unit. It helps limiting the resources each group can use - memory, CPU, the number of processes, and so on. If a process in the group exceeds its memory limit, the kernel kills only that group, and everything outside keeps running.

For clippy, I eventually started running it in an isolated cgroup with [cargo-safe](https://github.com/alexeygrigorev/rustkyll/blob/main/scripts/cargo-safe), so OOM killer only kills it.

However, you don't really know in advance which thing can cause the OOM collapse. I wrapped clippy, but at some point I was testing 

However, you can't know in advance which thing may cause the OOM collapse, so you want to have a session-level isolation. That is, the process you start in your session should also be wrapped in such a scope.

This is what I eventually did in tmuxctl. Under the hood, when I create a new session with `t -`, it wraps the command in a systemd scope with a memory limit and runs the session isolated.

It still didn't completely solve the problem - the tmux server was still the single point of failure. With many things running on the devbox, OOMs were still happening, and occasionally they would still kill the server. 

After consulting Fable, we did it this way: every session now has its own server, with its own socket file and its own systemd unit.

So when I implemented it with tmuxctl, it no longer was just a wrapper around tmux. Now listing sessions in tmuxctl would give a completely different result from `tmux list-sessions`.

And the whole thing became a Frankenstein monster. At this point, I looked at this, opened ChatGPT and asked "how difficult is it to write own terminal multiplexer?" It said it would be a few weeks of work. Then I asked it to implement it (turning the pro mode on), it thought for 10 minutes and gave me a version written in Rust. 

I decided to call it "aplexer" (it's very difficult to find a name that's available on PyPI these days!), which stands for "Agent Multiplexer". "Amux" was already taken - I counted 3 products with this name, and none of them were doing what I needed.

## Aplexer's initial requirements

What I needed from it:

- Simple commands to create sessions, list sessions, attach and detach
- No server - so no single point of failure.
- Dealing with OOM errors without having to worry about cgroups - but with optional cgroups support

Plus I wanted to have the same features that tmux had:

- Working after ssh disconnects
- Attaching and detaching sessions
- Sending input to each session
- Seeing the history 

The main focus was on running agents, so I also wanted

- Which folder ("workspace") this session is running in
- What's running inside each session - which agent
- Letting agents send messages to each other natively

I always follow [spec-driven development approach](https://aishippingblog.com/p/ai-native-development-specifications), so I discussed the requirements with ChatGPT, got the [specification](https://github.com/PocketShell-io/aplexer/blob/main/spec.md) out, and started developing it.

## Eat your own dog food 

I don't know why this approach is called this way (to me the dog food doesn't smell nice at all) but the idea behind it is that you use the tool you develop in your development process as soon as you can.

This approach works extremely well and forces you to find and fix all the inconvenient points. 

My v0 was that - the version of aplexer that I could use for running the agents that were building aplexer.

The main acceptance criteria for v0 were:

- I can use it for running agents
- Agents are in detachable sessions that don't stop after ssh disconnect
- OOM in one session doesn't affect any other session  

It took one week to have a stable version that works well, and then another couple of weeks to polish and add the features that I needed. Now it has fully replaced tmux in my workflow. 

I like short aliases, so I use `a` for aplexer in my terminal. 

## aplexer's architecture

A session starts with the client, not with a shared daemon.

When I create a session, the client first figures out what this session is: which workspace (folder) it belongs to, which agent to run, and with which settings. It writes all of this to disk as a session record - together with runtime details like the process IDs, the socket path, and the current status. Since the record is on disk, aplexer can always pick the session back up, even after a restart.

Then the client starts one worker for that session and waits for the worker to become ready.

The worker does the session-specific work:

1. It binds a private Unix control socket.
2. It creates an optional workload cgroup with the requested memory, task-count, CPU, and swap limits.
3. It opens a PTY master and slave.
4. It starts the workload with the PTY slave as its controlling terminal.
5. It keeps the PTY master and reads the workload's output.
6. It serves attach, input, resize, capture, status, rename, and kill operations.
7. It records exit or out-of-memory diagnostics and cleans up when the session ends.

The workload child performs the normal Unix terminal setup:

1. It creates a session with `setsid`.
2. It acquires the PTY slave as its controlling terminal.
3. It connects the slave to standard input, output, and error.
4. It applies the working directory and environment.
5. It executes the configured program.

The worker stays outside the workload cgroup, which limits the agent or shell. This lets it observe the workload, report its exit state, and clean up after a kill.

aplexer keeps two views of the output. The first is a bounded log of everything the workload has printed - useful for scrolling back through the history. The second is the current screen: the same bytes are also fed through a screen tracker that reconstructs what an interactive application, like vim, is showing right now. When you attach, you can get either view.

The resulting architecture looks like this:

<figure>
  <img src="../../assets/images/why-did-i-create-my-own-terminal-multiplexer/aplexer-architecture.png" alt="The aplexer client routes to three independent session boundaries, each containing a worker and workload, with session B shown in red to illustrate an independent failure">
  <figcaption>aplexer gives each session its own worker, PTY, lifecycle, and optional workload cgroup.</figcaption>
</figure>

Both runtimes have a client and a persistent process.

They differ in who owns the session and where the failure boundary sits:

- tmux's primary abstraction is persistent terminal layout.
- aplexer's primary abstraction is an identified agent or workspace session.
- tmux has one shared server, while aplexer has one worker per session.
- tmux exposes pane-backed PTYs, while aplexer gives each worker its own PTY.
- aplexer can add an optional workload cgroup to each session.
- aplexer exposes structured state, a mailbox, and worker operations.

With three independent sessions, no single worker owns all three PTYs. If the memory limit kills B's workload, sessions A and C keep their own workers and workload boundaries. If worker B dies, session B loses its supervisor, but workers A and C can continue.

That's the invariant I was building toward.


## Conclusion

I didn't create a terminal multiplexer because tmux is bad. It's excellent for what it does, but it stopped working for my particular use case - running agents on a devbox.

aplexer is my smaller, more specialized, Linux-specific attempt to make that model explicit.
