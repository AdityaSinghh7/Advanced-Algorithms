from zipzip_tree import ZipZipTree


def first_fit(items: list[float], assignment: list[int], free_space: list[float]):

    free_space.clear()

    if not items:

        return

    n = len(items)

    tree = ZipZipTree(n)

    bin_count = 0

    tree.insert(0, 1.0)

    bin_count = 1

    for i, item_size in enumerate(items):

        found_bin = -1

        for bin_id in range(bin_count):

            space = tree.find(bin_id)

            if item_size <= space + 1e-8:

                found_bin = bin_id

                break

        if found_bin != -1:

            assignment[i] = found_bin

            space = tree.find(found_bin)

            tree.insert(found_bin, space - item_size)

        else:

            assignment[i] = bin_count

            tree.insert(bin_count, 1.0 - item_size)

            bin_count += 1

    free_space.extend([tree.find(bin_id) for bin_id in range(bin_count)])


def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):

    free_space.clear()

    if not items:

        return

    n = len(items)

    indexed_items = [(items[i], i) for i in range(n)]

    indexed_items.sort(reverse=True, key=lambda x: x[0])

    tree = ZipZipTree(n)

    bin_count = 0

    tree.insert(0, 1.0)

    bin_count = 1

    for sorted_index, (item_size, original_index) in enumerate(indexed_items):

        found_bin = -1

        for bin_id in range(bin_count):

            space = tree.find(bin_id)

            if item_size <= space + 1e-8:

                found_bin = bin_id

                break

        if found_bin != -1:

            assignment[sorted_index] = found_bin

            space = tree.find(found_bin)

            tree.insert(found_bin, space - item_size)

        else:

            assignment[sorted_index] = bin_count

            tree.insert(bin_count, 1.0 - item_size)

            bin_count += 1

    free_space.extend([tree.find(bin_id) for bin_id in range(bin_count)])
