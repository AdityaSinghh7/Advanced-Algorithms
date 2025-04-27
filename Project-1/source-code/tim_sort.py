from typing import List, Tuple

def minrun(n: int) -> int:
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r

def binary_insertion_sort(a: List[int], left: int, right: int) -> None:
    for i in range(left + 1, right):
        key = a[i]
        lo, hi = left, i
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] <= key:
                lo = mid + 1
            else:
                hi = mid
        a[lo+1:i+1] = a[lo:i]
        a[lo] = key

def run_decomposition(a: List[int]) -> List[Tuple[int,int]]:
    n = len(a)
    m = minrun(n)
    runs: List[Tuple[int,int]] = []
    i = 0
    while i < n:
        start = i
        i += 1
        
        if i < n and a[i] < a[i-1]:
        
            while i < n and a[i] < a[i-1]:
                i += 1
            a[start:i] = reversed(a[start:i])
        else:
        
            while i < n and a[i] >= a[i-1]:
                i += 1
        
        run_len = i - start
        if run_len < m:
            end = min(start + m, n)
            binary_insertion_sort(a, start, end)
            i = end
        runs.append((start, i))
    return runs

def merge_runs(a: List[int], s1: int, e1: int, s2: int, e2: int) -> None:
    
    L, R = a[s1:e1], a[s2:e2]
    i = j = 0
    merged: List[int] = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            merged.append(L[i]); i += 1
        else:
            merged.append(R[j]); j += 1
    merged.extend(L[i:])
    merged.extend(R[j:])
    a[s1:e2] = merged

def tim_sort(a: List[int]) -> None:
    
    runs = run_decomposition(a)
    stack: List[Tuple[int,int]] = []
    for run in runs:
        stack.append(run)
    
        while True:
            h = len(stack)
            merged = False

    
            lengths = [e - s for (s, e) in stack]

    
            if not merged and h > 3 and lengths[-1] > lengths[-3]:
                s3, e3 = stack[-3]
                s2, e2 = stack[-2]
                merge_runs(a, s3, e3, s2, e2)
                stack[-3:-1] = [(s3, e2)]
                merged = True

    
            if not merged and h > 2 and lengths[-1] > lengths[-2]:
                s2, e2 = stack[-2]
                s1, e1 = stack[-1]
                merge_runs(a, s2, e2, s1, e1)
                stack[-2:] = [(s2, e1)]
                merged = True

    
            if not merged and h > 3 and lengths[-1] + lengths[-2] > lengths[-3]:
                s2, e2 = stack[-2]
                s1, e1 = stack[-1]
                merge_runs(a, s2, e2, s1, e1)
                stack[-2:] = [(s2, e1)]
                merged = True

    
            if not merged and h > 4 and lengths[-2] + lengths[-3] > lengths[-4]:
                s2, e2 = stack[-2]
                s1, e1 = stack[-1]
                merge_runs(a, s2, e2, s1, e1)
                stack[-2:] = [(s2, e1)]
                merged = True

            if not merged:
                break

    
    while len(stack) > 1:
        s2, e2 = stack[-2]
        s1, e1 = stack[-1]
        merge_runs(a, s2, e2, s1, e1)
        stack[-2:] = [(s2, e1)]


