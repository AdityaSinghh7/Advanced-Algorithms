def shell_sort_5(a: list[int]) -> list[int]:
    
    arr = a[:]  
    n = len(arr)
    if n <= 1:
        return arr
    gaps: list[int] = []
    k = 1
    while True:
        gap = (3**k - 1) // 2
        if gap >= n:
            break
        gaps.append(gap)
        k += 1

    
    for gap in reversed(gaps):
    
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

    return arr


# if __name__ == "__main__":
#     data = [23, 12, 1, 8, 34, 54, 2, 3, 99, 7]
#     print("Before:", data)
#     print("After: ", shell_sort_5(data))