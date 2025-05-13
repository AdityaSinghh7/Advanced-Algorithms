from zipzip_tree import ZipZipTree
from typing import Optional, Any

# Epsilon for float comparisons
EPSILON = 1e-9

def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    free_space.clear()
    if not items:
        return

    n = len(items)
    # Tree stores: key=bin_id, value=current_free_space_in_that_bin
    # Augmented with max_subtree_free_space for efficient first-fit search.
    bin_tree = ZipZipTree(n) # Max n bins possible
    
    # actual_bin_free_spaces[bin_id] stores the current free space of that bin.
    # This is the source of truth for free space values, tree values are copies.
    actual_bin_free_spaces: list[float] = []
    bin_count = 0

    for i, item_size in enumerate(items):
        chosen_bin_id: Optional[int] = None

        chosen_bin_id = bin_tree.find_first_fit_bin(item_size)

        if chosen_bin_id is not None:
            # Assign to this existing bin
            assignment[i] = chosen_bin_id
            
            current_fs_for_chosen_bin = actual_bin_free_spaces[chosen_bin_id]
            updated_fs_for_chosen_bin = round(current_fs_for_chosen_bin - item_size, 10)
            
            actual_bin_free_spaces[chosen_bin_id] = updated_fs_for_chosen_bin
            bin_tree.insert(chosen_bin_id, updated_fs_for_chosen_bin) # Update tree value and its augmented data

        else:
            # Create a new bin
            new_bin_id = bin_count
            assignment[i] = new_bin_id
            
            initial_fs_for_new_bin = round(1.0 - item_size, 10)
            
            if new_bin_id == len(actual_bin_free_spaces):
                actual_bin_free_spaces.append(initial_fs_for_new_bin)
            else: # Should not happen if bin_count is managed correctly
                actual_bin_free_spaces[new_bin_id] = initial_fs_for_new_bin

            bin_tree.insert(new_bin_id, initial_fs_for_new_bin)
            bin_count += 1

    # Populate the output free_space list from actual_bin_free_spaces
    # Ensure it has the correct size up to bin_count.
    # actual_bin_free_spaces should have size equal to bin_count.
    free_space.extend(actual_bin_free_spaces)
    # If some bins were created but never used or fully emptied, they still count.
    # The actual_bin_free_spaces list should correctly reflect this.
    # If bin_count is larger than len(actual_bin_free_spaces), pad with 0.0, but this shouldn't occur.
    if bin_count > len(actual_bin_free_spaces):
        free_space.extend([0.0] * (bin_count - len(actual_bin_free_spaces)))


def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    free_space.clear()
    if not items:
        return

    n = len(items)
    # Sort items in decreasing order.
    # Assignment list refers to item indices *after* sorting.
    sorted_items = sorted(items, reverse=True)
    
    # Call the optimized first_fit on the sorted items
    first_fit(sorted_items, assignment, free_space)
