"""
  2   0   1
  \  |  /
     3
 /  |  \
5   4   6
    |
    7
Reference: https://en.wikipedia.org/wiki/Parallel_breadth-first_search
"""
import threading
from collections import deque, defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_relation(self, from_node, to_node):
        self.graph[from_node].add(to_node)

    def remove_relation(self, from_node, to_node):
        self.graph[from_node].remove(to_node)

    def visit_neighbors_in_dfs(self, current_node, results, visited):
        results.append(current_node)
        for neighbor in self.graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.visit_neighbors_in_dfs(neighbor, results, visited)

    def parallel_depth_first_search(self, stack):
        visited = set([])
        results, threads = [], []

        # Performing parallel DFS for each seed node.
        for current_node in stack:
            # Parallel traversal for each seed node
            visited.add(current_node)
            thread = threading.Thread(target=self.visit_neighbors_in_dfs, args=(current_node, results, visited))
            threads.append(thread)
            thread.start()
        else:
            for thread in threads:
                thread.join() # Barrier synchronization
        print(results)  # printing node in DFS order

    def parallel_bfs_executor(self):
        self.graph[0] = [3]
        self.graph[1] = [3]
        self.graph[2] = [3]
        self.graph[3] = [4, 5, 6]
        self.graph[4] = [7]
        self.parallel_depth_first_search([0, 1, 2])


graph_obj = Graph()
graph_obj.parallel_bfs_executor()
