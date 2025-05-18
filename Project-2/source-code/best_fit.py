from zipzip_tree import ZipZipTree, Rank


def merge_sort(nums: list[float]):
    n = len(nums)
    if n > 1:
        mid = n // 2
        S1 = nums[:mid]
        S2 = nums[mid:]
        merge_sort(S1)
        merge_sort(S2)
        merge(nums, S1, S2)


def merge(nums: list[float], S1: list[float], S2: list[float]):
    i = j = k = 0
    while i < len(S1) and j < len(S2):
        if S1[i] < S2[j]:
            nums[k] = S1[i]
            i += 1
        else:
            nums[k] = S2[j]
            j += 1
        k += 1
    while i < len(S1):
        nums[k] = S1[i]
        i += 1
        k += 1
    while j < len(S2):
        nums[k] = S2[j]
        j += 1
        k += 1


def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    bins = ZipZipTree(len(items))
    free_space.clear()
    for i, item in enumerate(items):
        current_bin_idx = None
        node = bins.root
        best_fit_node = None
        while node:
            if node.key[0] >= item:
                best_fit_node = node
                node = node.left
            else:
                node = node.right
        if best_fit_node:
            current_bin_idx = best_fit_node.key[1]
            updated_free_space = round(free_space[current_bin_idx] - item, 10)
            bins.remove((free_space[current_bin_idx], current_bin_idx))
            bins.insert((updated_free_space, current_bin_idx), current_bin_idx)
            free_space[current_bin_idx] = updated_free_space
        else:
            current_bin_idx = len(free_space)
            new_free_space = round(1.0 - item, 10)
            free_space.append(new_free_space)
            bins.insert((new_free_space, current_bin_idx), current_bin_idx)
        assignment[i] = current_bin_idx
    return assignment


def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    merge_sort(items)
    best_fit(items[::-1], assignment, free_space)