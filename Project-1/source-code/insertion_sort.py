# Each sorting function should accept a list of integers as the single required
# parameter, as shown below. The input list should be sorted upon completion.
def insertion_sort(nums: list[int]):
    list_len = len(nums)
    for i in range(1, list_len):
        curr = nums[i]
        j = i
        while j > 0 and curr < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = curr
    return nums

