import math

def shell_sort_3(a: list[int]) -> list[int]:
    
    n = len(a)
    if n <= 1:
        return

    
    max_k = int(math.floor(math.log2(n)))
    gaps = [2**k + 1 for k in range(max_k, 0, -1) if 2**k + 1 < n]
    gaps.append(1)  

    
    for gap in gaps:
        for i in range(gap, n):
            temp = a[i]
            j = i
    
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
    return a
# if __name__ == "__main__":
#     data = [23, 12, 1, 8, 34, 54, 2, 3]
#     print("Before:", data)
#     print("After: ", shell_sort_3(data))