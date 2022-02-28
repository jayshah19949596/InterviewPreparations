from collections import defaultdict
from collections import deque

# Used to figure out ordering when dependencies are involved
# Application:
#       1. yum package installer searches for package dependencies using topological sort
#       2. Used to decide in which order to load tables with foreign keys in databases.
#       3. Ordering of formula cell evaluation when recomputing formula values in spreadsheets, logic synthesis.
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

    def topological_ordering(self):
        in_degree = defaultdict(int)
        for u, v in self.graph.items():
            in_degree[v] += 1

        queue = deque([node for node in in_degree if in_degree[node] == 0])
        visited = set([])
        while queue:
            cur_node = queue.popleft()
            print(cur_node)

            if cur_node in visited: continue
            visited.add(cur_node)

            for connection in self.graph[cur_node]:
                if in_degree[connection] > 0:
                    in_degree[connection] -= 1
                if in_degree[connection] == 0:
                    queue.append(connection)
