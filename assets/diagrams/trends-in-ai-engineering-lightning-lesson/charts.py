import json, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
D = json.load(open("/data/tmp/claude-1000/-home-alexey-git-telegram-writing-assistant/ef286e4e-10bc-4266-ace2-4700dc6c4c53/scratchpad/trend_data.json"))
dates = list(D); labels = ["Feb 4","Feb 27","Mar 27","Apr 22","May 29","Jun 25","Jul 22","Aug 25","Sep 23"]
OUT = "assets/images/trends-in-ai-engineering-lightning-lesson/"
SURF, TXT, TXT2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e6e5e0"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": GRID,
    "axes.labelcolor": TXT2, "xtick.color": TXT2, "ytick.color": TXT2, "text.color": TXT})
def base(title, sub):
    fig, ax = plt.subplots(figsize=(10, 5.4), dpi=160)
    fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.grid(axis="y", color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(length=0)
    fig.text(0.06, 0.94, title, fontsize=16, fontweight="bold", color=TXT)
    fig.text(0.06, 0.885, sub, fontsize=11.5, color=TXT2)
    fig.subplots_adjust(left=0.08, right=0.86, top=0.82, bottom=0.1)
    return fig, ax
def bars(key, title, sub, fname, color):
    fig, ax = base(title, sub)
    vals = [D[d][key] for d in dates]
    b = ax.bar(labels, vals, color=color, width=0.62)
    for r, v in zip(b, vals):
        ax.text(r.get_x()+r.get_width()/2, v + max(vals)*0.015, f"{v:g}", ha="center", va="bottom", fontsize=10.5, color=TXT2)
    fig.subplots_adjust(right=0.97)
    fig.savefig(OUT + fname); plt.close(fig)
def lines(series, title, sub, fname, ylim):
    fig, ax = base(title, sub)
    for key, name, c in series:
        v = [D[d][key] for d in dates]
        ax.plot(labels, v, "-o", color=c, lw=2, ms=6, mec=SURF, mew=2)
        ax.text(len(labels)-1+0.2, v[-1], f"{name}\n{v[-1]:.0f}%", va="center", fontsize=11, color=TXT)
        ax.text(-0.2, v[0], f"{v[0]:.0f}%", va="center", ha="right", fontsize=10.5, color=TXT2)
    ax.set_ylim(*ylim); ax.yaxis.set_major_formatter(lambda x, _: f"{x:.0f}%")
    ax.set_xlim(-0.6, len(labels)-0.5)
    fig.savefig(OUT + fname); plt.close(fig)
bars("n", "AI engineering job postings per monthly scrape", "Berlin, Amsterdam, London, New York, Los Angeles, and India", "postings-per-month.png", BLUE)
bars("fde", "Forward-deployed engineer postings per scrape", "Titles containing \"forward deployed\" or \"FDE\"", "fde-postings.png", AQUA)
lines([("integ", "Integrator stack\n(RAG, agents, APIs)", BLUE), ("trainer", "Trainer stack\n(PyTorch, fine-tuning)", ORANGE)],
      "Integrators up, trainers down", "Share of AI-first postings that mention each stack", "integrator-vs-trainer.png", (0, 100))
lines([("agents", "Agents", BLUE), ("rag", "RAG", ORANGE)],
      "Agents and RAG keep growing", "Share of all postings that mention each skill", "agents-and-rag.png", (0, 70))
# seniority, latest scrape
s = D[dates[-1]]["sen"]
order = [("Junior/Entry","Junior / entry"),("Mid (unspecified)","No level in title"),("Senior","Senior"),("Lead","Lead"),("Staff+","Staff, principal"),("Mgmt/Director","Manager, director")]
fig, ax = base("Almost no junior AI engineering roles", "Seniority from the job title, September 2026 scrape (1,086 postings)")
names = [n for _, n in order][::-1]; vals = [s.get(k, 0) for k, _ in order][::-1]
cols = [ORANGE if n == "Junior / entry" else "#9fc3ee" for n in names]
b = ax.barh(names, vals, color=cols, height=0.6)
for r, v in zip(b, vals): ax.text(v + 0.8, r.get_y()+r.get_height()/2, f"{v:.1f}%", va="center", fontsize=11, color=TXT)
ax.grid(axis="y", visible=False); ax.grid(axis="x", color=GRID, lw=0.8); ax.spines["left"].set_visible(False)
ax.xaxis.set_major_formatter(lambda x, _: f"{x:.0f}%"); ax.set_xlim(0, 58)
fig.subplots_adjust(left=0.2, right=0.97)
fig.savefig(OUT + "seniority.png"); plt.close(fig)
