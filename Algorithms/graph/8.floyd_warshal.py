# The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem.
# The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph

from collections import defaultdict


class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)
        self.all_nodes = set([])

    def add_edge(self, from_node, to_node, weight):
        self.graph[from_node].append([to_node, weight])
        self.all_nodes.add(from_node)
        self.all_nodes.add(to_node)

    def floyd_warshall(self):
        distances = self.initialize_distances()

        for middle in self.graph:
            for start in self.graph:
                for end in self.graph:
                    distances[start, end] = min(distances[start, end],
                                                distances[start, middle] + distances[middle, end])

        for from_node, to_node in distances:
            print(from_node, to_node, distances[from_node, to_node])

    def initialize_distances(self):
        distances = defaultdict(int)
        for first_node in self.all_nodes:
            for second_node in self.all_nodes:
                if first_node == second_node:
                    distances[first_node, second_node] = 0
                    continue
                distances[first_node, second_node] = float("inf")
                for to_node, weight in self.graph[first_node]:
                    if to_node == second_node:
                        distances[first_node, second_node] = weight
                        break
        return distances


graph_obj = Graph()
graph_obj.add_edge(0, 1, 5)
graph_obj.add_edge(0, 3, 10)
graph_obj.add_edge(1, 2, 3)
graph_obj.add_edge(2, 3, 1)
graph_obj.floyd_warshall()
