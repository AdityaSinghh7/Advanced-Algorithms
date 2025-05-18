from __future__ import annotations


from typing import TypeVar, Optional

from dataclasses import dataclass

import math

import random

import numbers


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


class ZipZipTree:

	def __init__(self, capacity: int):

		self.capacity = capacity

		self.root: Optional[Node] = None

		self.size = 0


	def get_random_rank(self) -> Rank:

		geometric_rank = 0

		while random.getrandbits(1) == 0:

			geometric_rank += 1

		uniform_rank = random.randint(0, int(math.log(self.capacity) ** 3) - 1) if self.capacity > 1 else 0

		return Rank(geometric_rank, uniform_rank)


	def insert(self, key: KeyType, val: ValType, rank: Rank = None):

		if rank is None:

			rank = self.get_random_rank()

		self.root, inserted = self._insert(self.root, key, val, rank)

		if inserted:

			self.size += 1


	def _insert(self, node: Optional[Node], key: KeyType, val: ValType, rank: Rank) -> tuple[Optional[Node], bool]:

		if node is None:

			return Node(key, val, rank), True

		if rank < node.rank or (rank == node.rank and key > node.key):

			if key < node.key:

				node.left, inserted = self._insert(node.left, key, val, rank)

			elif key > node.key:

				node.right, inserted = self._insert(node.right, key, val, rank)

			else:

				node.value = val

				return node, False

			return node, inserted

		else:

			left, right = self._split(node, key)

			new_node = Node(key, val, rank, left, right)

			return new_node, True


	def _split(self, node: Optional[Node], key: KeyType) -> tuple[Optional[Node], Optional[Node]]:

		if node is None:

			return None, None

		if key < node.key:

			left, right = self._split(node.left, key)

			node.left = right

			return left, node

		else:

			left, right = self._split(node.right, key)

			node.right = left

			return node, right


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

		self.root, removed = self._remove(self.root, key)

		if removed:

			self.size -= 1


	def _remove(self, node: Optional[Node], key: KeyType) -> tuple[Optional[Node], bool]:

		if node is None:

			return None, False

		if key < node.key:

			node.left, removed = self._remove(node.left, key)

			return node, removed

		elif key > node.key:

			node.right, removed = self._remove(node.right, key)

			return node, removed

		else:

			return self._merge(node.left, node.right), True


	def _merge(self, left: Optional[Node], right: Optional[Node]) -> Optional[Node]:

		if not left or not right:

			return left or right

		if left.rank > right.rank:

			left.right = self._merge(left.right, right)

			return left

		else:

			right.left = self._merge(left, right.left)

			return right


	def print_tree(self, node=None, depth=0):

		if node is None:

			node = self.root

		if node is not None:

			print('  ' * depth + f'key={node.key}, rank=({node.rank.geometric_rank},{node.rank.uniform_rank}), depth={depth}')

			self.print_tree(node.left, depth + 1)

			self.print_tree(node.right, depth + 1)



	def lower_bound(self, threshold: float):

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