def shell_sort1(a: list[int]) -> list[int]:
    n = len(a)
    gap = n // 2
    
    while gap > 0:
        
        for i in range(gap, n):
            temp = a[i]
            j = i
        
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        
        gap //= 2
    return a

# if __name__ == "__main__":
#     data = [23, 12, 1, 8, 34, 54, 2, 3]
#     print("Before:", data)
#     print("After: ", shell_sort1(data))