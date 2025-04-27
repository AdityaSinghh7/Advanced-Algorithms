"""
Create one log-log plot *per distribution* with all algorithms overlaid.
"""
import json, math, pathlib, csv
import matplotlib.pyplot as plt
from collections import defaultdict
from itertools import cycle

COLORS = cycle("bgrcmyk")   # simple colour cycle

data = json.load(open("results/raw.json"))
by_dist = defaultdict(list)
for row in data:
    by_dist[row["dist"]].append(row)

# Load slopes for nicer legend labels
slopes = {(r[0], r[1]): r[2] for r in csv.reader(open("results/slopes.csv")) if r[0]!="algorithm"}

pathlib.Path("results").mkdir(exist_ok=True)
for dist, rows in by_dist.items():
    plt.figure()
    # regroup by algorithm
    per_alg = defaultdict(list)
    for r in rows:
        per_alg[r["algorithm"]].append((r["size"], r["time"]))
    for alg, pts in per_alg.items():
        pts.sort()
        n, t = zip(*pts)
        s = slopes.get((alg, dist), "?")
        plt.loglog(n, t, marker='o', linestyle='-', label=f"{alg} (α≈{s})",
                   color=next(COLORS))
    plt.title(f"{dist} permutations")
    plt.xlabel("n (log scale)")
    plt.ylabel("time / s (log scale)")
    plt.legend()
    plt.grid(True, which="both", ls="--", lw=0.5)
    fname = f"results/{dist.lower()}_plot.png"
    plt.savefig(fname, dpi=300, bbox_inches='tight')
    print("✔", fname)