"""
Run every (algorithm × distribution × size) combination `RUNS` times,
store each timing sample as one JSON row.  Usage:

    python -m experiments.benchmark
"""
import sys, pathlib, json, time, random, gc
from statistics import mean

# ---------- set up paths ----------
ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC  = ROOT / "source-code"
sys.path.append(str(SRC))          # sorting routines live here
# -----------------------------------

from .generators import uniform_perm, almost_sorted, two_runs

from insertion_sort import insertion_sort
from tim_sort      import tim_sort
from shell_sort1   import shell_sort1
from shell_sort2   import shell_sort2
from shell_sort3   import shell_sort3
from shell_sort4   import shell_sort4
from shell_sort5   import shell_sort5

ALGORITHMS = {
    "Insertion"         : insertion_sort,
    "TimSort"           : tim_sort,
    "Shell-Sort-Orginal"     : shell_sort1,
    "Shell-Sedgewick"   : shell_sort2,
    "Shell-Sort-A083318"   : shell_sort3,
    "Shell-Sort-A003586"     : shell_sort4,
    "Shell-Sort-A003462"       : shell_sort5,
}

DISTRIBUTIONS = {
    "Uniform"  : uniform_perm,
    "Almost"   : almost_sorted,
    "TwoRuns"  : two_runs,
}

SIZES = [10, 100, 500, 1_000, 2_500, 5_000, 7_500, 10_000, 20_000]
RUNS  = 7 

random.seed(42)

rows = []
for dist_name, gen_fn in DISTRIBUTIONS.items():
    for n in SIZES:
        # generate the *same* input list for every algorithm this (dist,n) round
        base_inputs = [gen_fn(n) for _ in range(RUNS)]
        for alg_name, sort_fn in ALGORITHMS.items():
            print(f"{alg_name:<15} | {dist_name:<7} | n={n:>6} …", end="", flush=True)
            times = []
            for r in range(RUNS):
                data = base_inputs[r].copy()
                gc.disable()
                t0 = time.perf_counter()
                sort_fn(data)
                dt = time.perf_counter() - t0
                gc.enable()
                times.append(dt)
                rows.append(dict(algorithm=alg_name,
                                 dist=dist_name,
                                 size=n,
                                 run=r,
                                 time=dt))
            print(f"avg {mean(times):.5f}s")

pathlib.Path("results").mkdir(exist_ok=True)
with open("results/raw.json", "w") as f:
    json.dump(rows, f, indent=2)
print("\n✔ Timings saved to results/raw.json")