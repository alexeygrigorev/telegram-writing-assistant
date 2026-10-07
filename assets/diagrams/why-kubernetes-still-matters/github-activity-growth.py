# Source: GitHub Blog, "Building Git infrastructure for agent-scale development",
# Brian Celenza, Oct 6 2026
# https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ACCENT = "#2a78d6"
TEXT = "#0b0b0b"
TEXT2 = "#52514e"
MUTED = "#8a8985"
GRID = "#d9d8d4"

# (label, value plotted, value label, absolute note)
data = [
    ("Commits", 5.0, "5x+", "7.38B in Sep 2026"),
    ("Pushes", 4.9, "4.9x", "0.69B → 3.35B / month"),
    ("Actions runs", 4.0, "4x+", "3.26B in Sep 2026"),
    ("PR merges", 4.0, "~4x", ""),
    ("All Git events", 2.2, "2.2x", "218.2B → 473.3B / month"),
]

plt.rcParams["font.family"] = "DejaVu Sans"
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor("white")
ax = fig.add_axes([0.205, 0.13, 0.765, 0.63])

bar_h = 0.56
ys = list(range(len(data)))[::-1]
for y, (name, v, lab, note) in zip(ys, data):
    # bar: square at baseline, slightly rounded at the data end
    ax.add_patch(FancyBboxPatch((0, y - bar_h / 2), v, bar_h,
                                boxstyle="round,pad=0,rounding_size=0.06",
                                mutation_aspect=1 / 1.6,
                                facecolor=ACCENT, edgecolor="none", zorder=2))
    ax.add_patch(plt.Rectangle((0, y - bar_h / 2), 0.2, bar_h,
                               facecolor=ACCENT, edgecolor="none", zorder=2))
    t = ax.text(v + 0.1, y, lab, va="center", ha="left", fontsize=26,
                fontweight="bold", color=TEXT, zorder=3)
    if note:
        ax.annotate(note, xycoords=t, xy=(1, 0.5), xytext=(14, 0),
                    textcoords="offset points", va="center", ha="left",
                    fontsize=19, color=MUTED)

ax.set_yticks(ys)
ax.set_yticklabels([d[0] for d in data], fontsize=24, color=TEXT)
ax.tick_params(axis="y", length=0, pad=14)
ax.set_xlim(0, 7.6)
ax.set_ylim(-0.6, len(data) - 0.4)
ax.set_xticks([])
for s in ax.spines.values():
    s.set_visible(False)
ax.axvline(0, color=TEXT2, lw=1.5, zorder=1)

# 1x reference line
ax.axvline(1, color=TEXT2, lw=2, ls=(0, (5, 4)), zorder=4)
ax.text(1, len(data) - 0.42, "1x = a year ago", ha="center", va="bottom",
        fontsize=19, color=TEXT2)

fig.text(0.035, 0.925, "GitHub activity, one year later", fontsize=38,
         fontweight="bold", color=TEXT, ha="left", va="baseline")
fig.text(0.035, 0.862,
         "Growth in the year to September 2026, as developers and agents commit more",
         fontsize=22, color=TEXT2, ha="left", va="baseline")
fig.text(0.035, 0.045, "Source: GitHub Blog, Oct 6 2026", fontsize=18,
         color=MUTED, ha="left", va="baseline")

out = Path(__file__).with_suffix(".png")
fig.savefig(out, dpi=100, facecolor="white")
print(out)
