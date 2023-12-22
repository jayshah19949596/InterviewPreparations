"""
This Python code uses the multiprocessing module to parallelize the BFS traversal.
The Pool class is used to create a pool of worker processes, and the BFS traversal is divided among these processes.
The Manager class is used to create shared data structures (visited and result) among processes.
The Lock is used to synchronize access to the shared result list.
Note that the parallelization of BFS can be challenging due to the inherent dependencies in the traversal order. Depending on the specific requirements and characteristics of the graph, the parallelization strategy might need adjustments.
    0
    |
    1
 /  |  \
2   3   4
    |
    5
"""
from multiprocessing import Pool, Manager, Lock, Process
from collections import deque, defaultdict


class Graph(Process):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_relation(self, from_node, to_node):
        self.graph[from_node].append(to_node)

    def remove_relation(self, from_node, to_node):
        self.graph[from_node].remove(to_node)

    def bread_first_search(self, start, visited, result, lock):
        queue = deque([start])
        visited.append(start)
        i = 10
        while queue:
            current_node = queue.popleft()
            with lock: result.append(current_node)

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    with lock:
                        queue.append(neighbor)
                        visited.append(neighbor)

    def parallel_bfs_executor(self):
        self.add_relation(0, 1)
        self.add_relation(1, 2)
        self.add_relation(1, 3)
        self.add_relation(1, 4)
        self.add_relation(2, 5)
        self.add_relation(3, 5)
        self.add_relation(4, 5)

        source = 0

        manager = Manager()
        lock = manager.Lock()
        visited = manager.list()
        result = manager.list()

        with Pool() as pool:
            pool.apply(self.bread_first_search, (0, visited, result, lock))

        print(f"BFS traversal starting from node {source}:")
        print(result)


def main():

    graph_obj = Graph()
    graph_obj.parallel_bfs_executor()


main()
