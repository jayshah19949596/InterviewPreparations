
from collections import defaultdict

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

    def depth_first_search(self, start_node):
        visited = set([])
        self.dfs_recurse(start_node, visited)

    def dfs_recurse(self, cur_node, visited):
        if cur_node in visited: return
        print(cur_node)
        visited.add(cur_node)
        for neighbor in self.graph[cur_node]:
            self.dfs_recurse(neighbor, visited)
