import random
import math

def uniform_perm(n: int) -> list[int]:
    """Uniformly random permutation of 1‥n."""
    return random.sample(range(1, n + 1), n)

def almost_sorted(n: int) -> list[int]:
    """Start sorted, then perform ⌊log₂n⌋ random swaps."""
    a = list(range(1, n + 1))
    swaps = int(math.log2(n))
    for _ in range(swaps):
        i, j = random.randrange(n), random.randrange(n)
        a[i], a[j] = a[j], a[i]
    return a

def two_runs(n: int) -> list[int]:
    """1,3,5,… then 2,4,6,… (odd indices first)."""
    odds  = list(range(1, n + 1, 2))
    evens = list(range(2, n + 1, 2))
    return odds + evens