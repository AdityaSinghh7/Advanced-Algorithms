# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.

from collections.abc import Iterable
import random

class Graph:
	def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
		"""
		Initialize the graph with a given number of nodes and edges.
		Edges are tuples (u, v) for an undirected graph.
		"""
		self._num_nodes = num_nodes
		self._edges = set()
		self._adj = {i: set() for i in range(num_nodes)}
		for u, v in edges:
			if u == v:
				continue  # Skip self-loops (optional, can be included if needed)
			if (u, v) not in self._edges and (v, u) not in self._edges:
				self._edges.add((u, v))
				self._adj[u].add(v)
				self._adj[v].add(u)

	def get_num_nodes(self) -> int:
		"""Return the number of nodes in the graph."""
		return self._num_nodes

	def get_num_edges(self) -> int:
		"""Return the number of edges in the graph."""
		return len(self._edges)

	def get_neighbors(self, node: int) -> Iterable[int]:
		"""Return an iterable of neighbors for the given node."""
		return self._adj[node]

	def nodes(self) -> Iterable[int]:
		"""Return an iterable of all node indices."""
		return range(self._num_nodes)

	def edges(self) -> Iterable[tuple[int, int]]:
		"""Return an iterable of all edges as (u, v) with u < v."""
		for u, v in self._edges:
			yield (u, v) if u < v else (v, u)

	def has_edge(self, u: int, v: int) -> bool:
		"""Return True if there is an edge between u and v."""
		return v in self._adj[u]

	@staticmethod
	def erdos_renyi_graph(n: int, p: float) -> 'Graph':
		"""
		Generate an Erdos-Renyi random graph G(n, p).
		Each possible edge is included with probability p.
		"""
		edges = []
		for u in range(n):
			for v in range(u + 1, n):
				if random.random() < p:
					edges.append((u, v))
		return Graph(n, edges)

	@staticmethod
	def barabasi_albert_graph(n: int, d: int) -> 'Graph':
		"""
		Generate a Barabasi-Albert random graph with parameter d.
		Each new node attaches to d existing nodes with probability proportional to degree.
		"""
		if d < 1 or d >= n:
			raise ValueError("Barabasi-Albert model requires 1 <= d < n")
		edges = []
		# Start with a complete graph of d+1 nodes
		targets = list(range(d + 1))
		for u in range(d + 1):
			for v in range(u + 1, d + 1):
				edges.append((u, v))
		# List of nodes with degree, used for preferential attachment
		node_list = []
		for u, v in edges:
			node_list.extend([u, v])
		for new_node in range(d + 1, n):
			# Preferential attachment: choose d unique targets
			targets = set()
			while len(targets) < d:
				chosen = random.choice(node_list)
				targets.add(chosen)
			for target in targets:
				edges.append((new_node, target))
				node_list.extend([new_node, target])
		return Graph(n, edges)

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
