"""
  2   0     1
  \  |  /  | | \
     3    8  9  10
 /  |  \      /  \
5   4   6    11  12
    |
    7
Reference: https://en.wikipedia.org/wiki/Parallel_breadth-first_search
"""
import threading
from collections import deque, defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        self.lock = threading.Lock()
        self.max_no_of_thread = 4

    def add_relation(self, from_node, to_node):
        self.graph[from_node].add(to_node)

    def remove_relation(self, from_node, to_node):
        self.graph[from_node].remove(to_node)

    def visit_neighbors_in_dfs(self, current_node, results, visited):
        results.append(current_node)
        for neighbor in self.graph[current_node]:
            if neighbor not in visited:
                self.lock.acquire()
                visited.add(neighbor)
                self.lock.release()
                self.visit_neighbors_in_dfs(neighbor, results, visited)
        threading.current_thread().return_value = results

    def parallel_depth_first_search(self, stack):
        """
            Different threads handle different path of the graph search space concurrently.
        """
        visited = set([])
        merged_results, results, threads = [], [], deque([])

        # Performing parallel DFS for each seed node.
        for current_node in stack:
            # Parallel traversal for each seed node
            visited.add(current_node)
            thread = threading.Thread(target=self.visit_neighbors_in_dfs, args=(current_node, [], visited))
            threads.append(thread)
            if len(threads) > self.max_no_of_thread:  # Restrict the maximum number of threads
                threads[0].join()
                merged_results = merged_results+threads.popleft().return_value

            thread.start()
        else:
            for thread in threads:
                thread.join() # Barrier synchronization
                merged_results = merged_results+thread.return_value
        print(merged_results)  # Nodes printed in DFS order


    def parallel_bfs_executor(self):
        self.graph[0] = [3]
        self.graph[1] = [3, 8, 9, 10]
        self.graph[10] = [11, 12]
        self.graph[2] = [3]
        self.graph[3] = [4, 5, 6]
        self.graph[4] = [7]
        self.parallel_depth_first_search([0, 2, 1])


graph_obj = Graph()
graph_obj.parallel_bfs_executor()
