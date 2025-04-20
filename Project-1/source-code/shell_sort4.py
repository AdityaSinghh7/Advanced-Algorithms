import math
def a003586_sequence(n):
    gaps = set()
    p = 0
    while 2**p < n:
        q = 0
        while 2**p * 3**q < n:
            gaps.add(2**p * 3**q)
            q += 1
        p += 1
    
    return sorted(gaps, reverse=True)

def shell_sort4(arr: list[int]) -> list[int]:
    
    n = len(arr)
    gaps = a003586_sequence(n)
    
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