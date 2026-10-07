# Source: Kyle Daigle (GitHub COO), X, Apr 3 2026
# https://x.com/kdaigle/status/2040164759836778878
# "There were 1 billion commits in 2025. Now, it's 275 million per week,
#  on pace for 14 billion this year if growth remains linear (spoiler: it won't.)"
from pathlib import Path

import matplotlib.pyplot as plt

ACCENT = "#2a78d6"
TEXT = "#0b0b0b"
TEXT2 = "#52514e"
MUTED = "#8a8985"

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["hatch.color"] = "white"
plt.rcParams["hatch.linewidth"] = 3
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor("white")
ax = fig.add_axes([0.08, 0.15, 0.84, 0.62])

xs = [0, 1]
vals = [1, 14]
ax.bar(0, 1, width=0.55, color=ACCENT, zorder=2)
ax.bar(1, 14, width=0.55, color=ACCENT, alpha=0.55, hatch="//", zorder=2)

ax.text(0, 1 + 0.35, "1B", ha="center", va="bottom", fontsize=40,
        fontweight="bold", color=TEXT)
ax.text(0, 1 + 2.5, "actual", ha="center", va="bottom", fontsize=24, color=MUTED)
ax.text(1, 14 + 0.35, "~14B", ha="center", va="bottom", fontsize=40,
        fontweight="bold", color=TEXT)
ax.text(1.32, 7, "275M commits a week\nin April 2026,\nprojected for the year",
        ha="left", va="center", fontsize=22, color=MUTED)

ax.set_xticks(xs)
ax.set_xticklabels(["2025", "2026"], fontsize=30, color=TEXT)
ax.tick_params(axis="x", length=0, pad=12)
ax.set_yticks([])
ax.set_xlim(-0.6, 2.0)
ax.set_ylim(0, 17)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(TEXT2)

fig.text(0.035, 0.925, "Commits on GitHub per year", fontsize=38,
         fontweight="bold", color=TEXT, ha="left", va="baseline")
fig.text(0.035, 0.862, "2026 is on pace for 14 times the commits of 2025",
         fontsize=24, color=TEXT2, ha="left", va="baseline")
fig.text(0.035, 0.045, "Source: Kyle Daigle, GitHub COO, Apr 3 2026", fontsize=18,
         color=MUTED, ha="left", va="baseline")

out = Path(__file__).with_suffix(".png")
fig.savefig(out, dpi=100, facecolor="white")
print(out)
