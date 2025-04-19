def shell_sort2(a: list[int]) -> list[int]:
    
    n = len(a)
    
    gaps: list[int] = []
    k = 1
    while True:
        gap = 2 * (n // (2 ** (k + 1))) + 1
        if gap > 1:
            gaps.append(gap)
            k += 1
        else:
            break
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
#     print("After: ", shell_sort2(data))