from zipzip_tree import ZipZipTree


def next_fit(items: list[float], assignment: list[int], free_space: list[float]):

	free_space.clear()

	if not items:

		return

	n = len(items)

	tree = ZipZipTree(n)

	current_bin_index = 0

	tree.insert(current_bin_index, 1.0)


	for i, item_size in enumerate(items):

		space = tree.find(current_bin_index)

		if item_size <= space + 1e-8:

			assignment[i] = current_bin_index

			tree.insert(current_bin_index, space - item_size)

		else:

			current_bin_index += 1

			tree.insert(current_bin_index, 1.0 - item_size)

			assignment[i] = current_bin_index


	free_space.extend([tree.find(bin_id) for bin_id in range(current_bin_index + 1)])


