# Project 3 To-Do List

This to-do list outlines the step-by-step approach to implementing the source code for Project 3, as described in `projectDescription.txt`. It includes the extra credit (support for both Erdos-Renyi and Barabasi-Albert graph models), but excludes plots and report generation.

---

## 1. Graph Data Structure Implementation (`graph.py`)

- [x] Implement the `Graph` class:
  - [x] `__init__(self, num_nodes: int, edges: Iterable[tuple[int, int]])`: Initialize the graph with the given number of nodes and edges.
  - [x] `get_num_nodes(self) -> int`: Return the number of nodes.
  - [x] `get_num_edges(self) -> int`: Return the number of edges.
  - [x] `get_neighbors(self, node: int) -> Iterable[int]`: Return an iterable of neighbors for a given node.
  - [x] (Optional) Add any helper methods as needed (e.g., for internal representation).

- [x] **Extra Credit:** Implement graph generators as static/class methods:
  - [x] `@staticmethod def erdos_renyi_graph(n: int, p: float) -> 'Graph'`: Generate an Erdos-Renyi random graph G(n, p).
  - [x] `@staticmethod def barabasi_albert_graph(n: int, d: int) -> 'Graph'`: Generate a Barabasi-Albert random graph with parameter d.

---

## 2. Graph Algorithms Implementation (`graph_algorithms.py`)

- [x] Implement the following functions:
  - [x] `get_diameter(graph: Graph) -> int`: Compute the approximate graph diameter using a heuristic function.
  - [x] `get_clustering_coefficient(graph: Graph) -> float`: Compute the global clustering coefficient (3 × number of triangles / number of paths of length 2).
  - [x] `get_degree_distribution(graph: Graph) -> dict[int, int]`: Compute the degree distribution (mapping degree to count of nodes with that degree).

---

## 3. Testing and Validation (`project3_tests.py`)

- [ ] Use the provided test cases to validate the `Graph` class and algorithms.
- [ ] Add additional test cases for edge cases and larger graphs if needed.
- [ ] Test both Erdos-Renyi and Barabasi-Albert graph generation and algorithms for all required values of n: `{10, 100, 1000, 10000, 50000, 100000}` (as feasible for your environment).

---

## 4. Integration and Utility

- [ ] Ensure all imports and file structures match the requirements (no non-standard libraries).
- [ ] Ensure the code is compatible with Python 3.6+ and runs in a Linux environment.
- [ ] Make sure the code passes all provided and custom tests.

---

## 5. (Optional) Documentation

- [ ] Add docstrings and comments to all classes and functions for clarity.
- [ ] Briefly document the usage of graph generators and algorithms in code comments.

---

## 6. (For Future) Plots and Report Generation

- [ ] (Skip for now) Implement plotting and report generation for analysis and extra credit.

---

**Ready to begin implementation!** 