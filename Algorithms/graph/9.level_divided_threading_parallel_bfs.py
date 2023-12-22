"""
    0
    |
    1
 /  |  \
2   3   4
 \  |  /
    5
Reference: https://en.wikipedia.org/wiki/Parallel_breadth-first_search
"""
import threading
from collections import deque, defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(set)
        self.lock = threading.Lock()

    def add_relation(self, from_node, to_node):
        self.graph[from_node].add(to_node)

    def remove_relation(self, from_node, to_node):
        self.graph[from_node].remove(to_node)

    def visit_neighbors(self, current_node, next_level, visited):
        for neighbor in self.graph[current_node]:
            if neighbor not in visited:
                self.lock.acquire()
                visited.add(neighbor)
                self.lock.release()
                next_level.append(neighbor)

    def parallel_bread_first_search(self, seed_node):
        cur_level, visited = deque([seed_node]), set([seed_node])

        while cur_level:
            threads, next_level = [], deque([])
            print(cur_level)

            for current_node in cur_level:
                # This for block is paralellized
                thread = threading.Thread(target=self.visit_neighbors, args=(current_node, next_level, visited))
                threads.append(thread)
                thread.start()
            else:
                for thread in threads: thread.join() # Barrier synchronization

            cur_level = next_level

    def parallel_bfs_executor(self):
        self.graph[0] = set([1])
        self.graph[1] = set([2, 3, 4])
        self.graph[2] = set([5])
        self.graph[3] = set([5])
        self.graph[4] = set([5])
        self.parallel_bread_first_search(0)


graph_obj = Graph()
graph_obj.parallel_bfs_executor()
