def a003462_sequence(n):
    gaps = []
    k = 1
    while True:
        value = (3**k - 1) // 2
        if value < n:
            gaps.append(value)
        else:
            break
        k += 1
    
    return gaps[::-1] 

def shell_sort5(arr: list[int]) -> list[int]:
    
    n = len(arr)
    gaps = a003462_sequence(n)
    
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
#     data = [23, 12, 1, 8, 34, 54, 2, 3, 99, 7]
#     print("Before:", data)
#     print("After: ", shell_sort_5(data))