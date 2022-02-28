# Bellman-Ford algorithm finds the shortest paths with negative weight cycle.
# It is not better than Dijsktras.
# Dijsktras time complexity is O((V+E)log(V)) and Bellman ford time complexity is O(VE).
# It may give correct results for a graph with negative edges but you must allow a vertex can be visited multiple times.
# For graphs with negative weight edges and cycles, Bellman–Ford algorithm can be used.
# Bellman-Ford works better (better than Dijkstra’s) for distributed systems.
# Unlike Dijkstra’s where we need to find the minimum value of all vertices, in Bellman-Ford edges are considered 1 by 1
# Application:
#      1. A distributed variant of the Bellman–Ford algorithm is used in distance-vector routing protocols.
#      2. Cycle-cancelling techniques
# Limitation:
#      1. It does not scale well.
#      2. Changes in network topology are not reflected quickly since updates are spread node-by-node.
#      3. Does not handle negative cycle reachable from the source vertex to destination vertex.
# Complexity Analysis:
#       V is number of vertices
#       E is number of edges
#       Time Complexity: O(VE)
#       Space Complexity: O(V)

from collections import defaultdict


class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, from_node, to_node, weight):
        self.graph[from_node].append([to_node, weight])

    def print_array(self, dist):
        print("Vertex Distance from Source")
        for node in self.graph:
            print("{0}\t\t{1}".format(node, dist[node]))

    # The main function that finds shortest distances from src to all other vertices using Bellman-Ford algorithm.
    # The function also detects negative weight cycle
    def bellman_ford(self, start_node):

        # Step 1: Initialize distances from src to all other vertices as INFINITE
        distances = defaultdict(int)
        for from_node in self.graph:
            distances[from_node] = float("inf")
            for to_node, weight in self.graph[from_node]:
                distances[to_node] = float("inf")
        distances[start_node] = 0

        # Step 2: Relax all edges |V| - 1 times.
        # A simple shortest path from src to any other vertex can have at-most |V| - 1 edges
        for _ in range(len(self.graph)):
            # Update dist value and parent index of the adjacent vertices of the picked vertex.
            # Consider only those vertices which are still in queue
            for from_node in self.graph:
                for to_node, weight in self.graph[from_node]:
                    cur_dist = distances[from_node] + weight
                    if distances[from_node] != float("inf") and cur_dist < distances[to_node]:
                        distances[to_node] = cur_dist

        # Step 3: Check for negative-weight cycles. Above step guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there is a cycle.
        if self.is_neg_wegh_cycle(distances): return
        # print all distance
        self.print_array(distances)

    def is_neg_weight_cycle(self, distances):
        for from_node in self.graph:
            for to_node, weight in self.graph[from_node]:
                cur_dist = distances[from_node] + weight
                if distances[from_node] != float("inf") and cur_dist < distances[to_node]:
                    print("Graph contains negative weight cycle")
                    return True


g = Graph()
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

# Print the solution
g.bellman_ford(0)

