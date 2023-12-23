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
import concurrent.futures
from collections import deque, defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(set)
        self.lock = threading.Lock()
        self.max_no_of_thread = 4

    def add_relation(self, from_node, to_node):
        self.graph[from_node].add(to_node)

    def remove_relation(self, from_node, to_node):
        self.graph[from_node].remove(to_node)

    def visit_neighbors(self, current_node, next_level, visited):
        for neighbor in self.graph[current_node]:
            if neighbor not in visited:
                # Applying MUTEX lock to protect critical section of updating shared resources from race condition
                self.lock.acquire()
                visited.add(neighbor)
                self.lock.release()
                next_level.append(neighbor)

    def parallel_bread_first_search(self, seed_node):
        """
            Different threads handle different level of the graph search space concurrently.
        """
        cur_level, visited = deque([seed_node]), set([seed_node])
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

        while cur_level:
            threads, next_level = deque([]), deque([])
            print(cur_level)

            for current_node in cur_level:
                # This for loop block is paralellized
                thread = threading.Thread(target=self.visit_neighbors, args=(current_node, next_level, visited))
                threads.append(thread)
                if len(threads)>self.max_no_of_thread: # Restrict the maximum number of threads
                    threads[0].join()
                    threads.popleft()
                thread.start()
            else:
                for thread in threads: thread.join()  # Barrier synchronization to stope execution of current program

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
