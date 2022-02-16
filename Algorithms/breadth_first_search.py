from collections import defaultdict
from collections import deque

# Complexity Analysis:
#       V is number of vertices
#       E is number of edges
#       Time Complexity: O(V+E)
#       Space Complexity: O(V)


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(set)

    def add_relation(self, from_node, to_node):
        self.graph[from_node].add(to_node)

    def remove_relation(self, from_node, to_node):
        self.graph[from_node].remove(to_node)

    def bread_first_search(self, start_node):
        queue = deque([start_node])
        visited = set()
        while queue:
            cur_node = queue.popleft()
            if cur_node in visited: continue
            visited.add(cur_node)
            print(cur_node)
            for neighbor in self.graph[cur_node]:
                queue.append(neighbor)
