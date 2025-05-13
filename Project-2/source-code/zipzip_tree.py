from __future__ import annotations

from typing import TypeVar, Optional, Any
from dataclasses import dataclass
import math
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

@dataclass(order=True)
class Rank:
	geometric_rank: int
	uniform_rank: int

@dataclass
class Node:
	key: KeyType
	value: ValType
	rank: Rank
	left: Optional['Node'] = None
	right: Optional['Node'] = None
	max_subtree_free_space: float = float('-inf')

	def __post_init__(self):
		if isinstance(self.value, float):
			self.max_subtree_free_space = self.value

class ZipZipTree:
	def __init__(self, capacity: int):
		# self.random = random.Random(42) # Example if you wanted instance-specific RNG
		self.capacity = capacity
		self.root: Optional[Node] = None
		self.size = 0

	def _recompute_max_fs(self, node: Optional[Node]):
		if not node:
			return
		
		left_max_fs = node.left.max_subtree_free_space if node.left else float('-inf')
		right_max_fs = node.right.max_subtree_free_space if node.right else float('-inf')
		
		current_node_value_as_float = float('-inf')
		if isinstance(node.value, float):
			current_node_value_as_float = node.value

		node.max_subtree_free_space = max(current_node_value_as_float, left_max_fs, right_max_fs)

	def get_random_rank(self) -> Rank:
		geometric_rank = 0
		while random.getrandbits(1) == 0:
			geometric_rank += 1
		uniform_rank = random.randint(0, int(math.log(self.capacity) ** 3) - 1) if self.capacity > 1 else 0
		return Rank(geometric_rank, uniform_rank)

	def insert(self, key: KeyType, val: ValType, rank: Rank = None):
		if rank is None:
			rank = self.get_random_rank()
		
		self.root, new_node_created = self._insert(self.root, key, val, rank)
		
		if new_node_created:
			self.size += 1

	def _insert(self, node: Optional[Node], key: KeyType, val: ValType, rank: Rank) -> tuple[Optional[Node], bool]:
		if node is None:
			return Node(key, val, rank), True

		if key == node.key:
			# print(f"Updating node {key}: old_val={node.value}, new_val={val}") # DEBUG PRINT - ensure commented out
			node.value = val
			self._recompute_max_fs(node)
			return node, False

		newly_created_flag = False
		if rank < node.rank:
			if key < node.key:
				node.left, newly_created_flag = self._insert(node.left, key, val, rank)
			else: # key > node.key (since key == node.key handled above)
				node.right, newly_created_flag = self._insert(node.right, key, val, rank)
			self._recompute_max_fs(node)
			return node, newly_created_flag
		else: # Promote (rank_new >= rank_old)
			new_node = Node(key, val, rank)
			left_child_for_new, right_child_for_new = self._split(node, key)
			new_node.left = left_child_for_new
			new_node.right = right_child_for_new
			self._recompute_max_fs(new_node)
			return new_node, True

	def _split(self, node: Optional[Node], key: KeyType) -> tuple[Optional[Node], Optional[Node]]:
		if node is None:
			return None, None
		
		if key < node.key:
			new_left_for_node, new_right_for_node_left = self._split(node.left, key)
			node.left = new_right_for_node_left
			self._recompute_max_fs(node)
			return new_left_for_node, node
		else:
			new_left_for_node_right, new_right_for_node = self._split(node.right, key)
			node.right = new_left_for_node_right
			self._recompute_max_fs(node)
			return node, new_right_for_node

	def find(self, key: KeyType) -> Optional[ValType]:
		node = self.root
		while node:
			if key < node.key:
				node = node.left
			elif key > node.key:
				node = node.right
			else:
				return node.value
		raise KeyError(f"Key {key} not found in ZipZipTree.")

	def get_size(self) -> int:
		return self.size

	def get_height(self) -> int:
		return self._get_height(self.root)

	def _get_height(self, node: Optional[Node]) -> int:
		if not node:
			return -1
		return 1 + max(self._get_height(node.left), self._get_height(node.right))

	def get_depth(self, key: KeyType) -> int:
		node = self.root
		depth = 0
		while node:
			if key < node.key:
				node = node.left
			elif key > node.key:
				node = node.right
			else:
				return depth
			depth += 1
		raise KeyError(f"Key {key} not found in ZipZipTree.")

	def remove(self, key: KeyType):
		self.root, node_was_removed = self._remove(self.root, key)
		if node_was_removed:
			self.size -= 1

	def _remove(self, node: Optional[Node], key: KeyType) -> tuple[Optional[Node], bool]:
		if node is None:
			return None, False

		node_removed_flag = False
		if key < node.key:
			node.left, node_removed_flag = self._remove(node.left, key)
		elif key > node.key:
			node.right, node_removed_flag = self._remove(node.right, key)
		else:
			merged_children = self._merge(node.left, node.right)
			return merged_children, True

		if node_removed_flag:
			self._recompute_max_fs(node)
		return node, node_removed_flag

	def _merge(self, left: Optional[Node], right: Optional[Node]) -> Optional[Node]:
		if not left:
			return right
		if not right:
			return left

		if left.rank > right.rank or (left.rank == right.rank and random.getrandbits(1) == 0):
			left.right = self._merge(left.right, right)
			self._recompute_max_fs(left)
			return left
		else:
			right.left = self._merge(left, right.left)
			self._recompute_max_fs(right)
			return right

	def print_tree(self, node=None, depth=0):
		if node is None and depth == 0:
			node = self.root
		if node is not None:
			val_str = f'{node.value}' if not isinstance(node.value, float) else f'{node.value:.2f}'
			print('  ' * depth + f'key={node.key}, val={val_str}, rank=({node.rank.geometric_rank},{node.rank.uniform_rank}), max_fs={node.max_subtree_free_space:.2f}, depth={depth}')
			self.print_tree(node.left, depth + 1)
			self.print_tree(node.right, depth + 1)

	def lower_bound(self, threshold: KeyType):
		node = self.root
		result = None
		while node:
			if node.key < threshold:
				node = node.right
			else:
				result = node
				node = node.left
		if result:
			return result.key, result.value
		return None, None

	def find_first_fit_bin(self, item_size: float, epsilon: float = 1e-9) -> Optional[KeyType]:
		return self._find_first_fit_recursive(self.root, item_size, epsilon)

	def _find_first_fit_recursive(self, node: Optional[Node], item_size: float, epsilon: float) -> Optional[KeyType]:
		# print(f"START _find_ff_rec: node={node.key if node else 'None'}, item_size={item_size:.4f}") # MODIFIED: Top level entry log
		
		if not node:
			# print(f"  _find_ff_rec: node is None, returning None")
			# print(f"END _find_ff_rec: node was None, returning None for item_size={item_size:.4f}") # MODIFIED
			return None

		res_left = None 
		if node.left:
			# Potential to go left
			if node.left.max_subtree_free_space >= item_size - epsilon: # Condition A
				res_left = self._find_first_fit_recursive(node.left, item_size, epsilon)
				if res_left is not None: 
					return res_left # Found in left, definitely smaller ID or same subtree
		
		# If not found in left (or no left, or left not promising)
		current_node_fs_value = float('-inf')
		if isinstance(node.value, float): 
			current_node_fs_value = node.value
		
		if current_node_fs_value >= item_size - epsilon: # Condition B
			return node.key # Current node fits
		
		# If not found in left or current
		res_right = None
		if node.right:
			# Potential to go right
			if node.right.max_subtree_free_space >= item_size - epsilon: # Condition C
				res_right = self._find_first_fit_recursive(node.right, item_size, epsilon)
				if res_right is not None: 
					return res_right # Found in right
		
		return None # No fit anywhere in this path

