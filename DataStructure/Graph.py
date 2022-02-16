from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(set)

    def add_relation(self, from_node, to_node):
        self.graph[from_node].add(to_node)

    def remove_relation(self, from_node, to_node):
        self.graph[from_node].remove(to_node)
