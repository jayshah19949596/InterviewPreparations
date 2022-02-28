from collections import defaultdict
import heapq

# Dijkstra algorithm for finding the shortest paths between nodes in a graph
# It does not work for graphs with negative weight cycle.
# It may give correct results for a graph with negative edges but you must allow a vertex can be visited multiple times
# and that version will lose its fast time complexity.
# For graphs with negative weight edges and cycles, Bellman–Ford algorithm can be used
# It can handle graphs consisting of cycles.
# Application:
#      1. Used in routing protocols.
# Limitation:
#      1. It does not work for graphs with negative weights.
# Complexity Analysis:
#       V is number of vertices
#       E is number of edges
#       Time Complexity: O((E+V)*log|V|)
#       Space Complexity: O(V)


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(set)

    def add_relation(self, from_node, to_node, weight):
        self.graph[from_node].add((to_node, weight))

    def remove_relation(self, from_node, to_node):
        for neighbor_node, weight in self.graph[from_node]:
            if neighbor_node == to_node:
                to_weigh = weight
                break
        self.graph.remove(to_node, to_weigh)

    def dijkstra_shortest_path(self, start_node, end_node):
        queue, visited = [[start_node, 0, []]], set()
        while queue:
            cur_node, cur_weight, path = heapq.heappop(queue)
            if cur_node == end_node: return path
            if cur_node in visited: continue
            visited.add(cur_node)
            for neighbor, neighbor_weight in self.graph[cur_node]:
                queue.append((neighbor, cur_weight+neighbor_weight, path+[neighbor]))
        return []
