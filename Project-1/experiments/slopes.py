"""
Read results/raw.json → results/slopes.csv (empirical exponent α).
"""
import json, math, csv, pathlib
from collections import defaultdict

data = json.load(open("results/raw.json"))
groups = defaultdict(list)
for row in data:
    key = (row["algorithm"], row["dist"])
    groups[key].append((math.log(row["size"]), math.log(row["time"])))

out = []
for (alg, dist), pts in groups.items():
    xs, ys = zip(*pts)
    
    n = len(xs)
    xbar = sum(xs)/n
    ybar = sum(ys)/n
    slope = sum((x-xbar)*(y-ybar) for x,y in pts) / sum((x-xbar)**2 for x in xs)
    out.append((alg, dist, round(slope, 3)))

pathlib.Path("results").mkdir(exist_ok=True)
with open("results/slopes.csv","w", newline="") as f:
    csv.writer(f).writerows([("algorithm","dist","slope")] + out)
print("✔ slopes.csv written")