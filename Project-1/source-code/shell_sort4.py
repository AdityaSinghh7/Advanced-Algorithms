import math
def shell_sort_4(a: list[int]) -> list[int]:
    
    arr = a[:]
    n = len(arr)
    if n <= 1:
        return arr

    
    smooth = set()
    max_i = int(math.log(n, 2))
    for i in range(max_i + 1):
        pow2 = 2**i
        if pow2 >= n:
            break
        max_j = int(math.log(n / pow2, 3))
        for j in range(max_j + 1):
            gap = pow2 * (3**j)
            if gap < n:
                smooth.add(gap)

    
    gaps = sorted(smooth, reverse=True)
    if gaps[-1] != 1:
        gaps.append(1)

    
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

    return arr

# if __name__ == "__main__":
#     data = [23, 12, 1, 8, 34, 54, 2, 3]
#     print("Before:", data)
#     print("After: ", shell_sort_4(data))