class DisjointSets(object):
    def __init__(self):
        self.rank = {}
        self.parent = {}

    # Time Complexity: O(1)
    def add_node(self, node):
        self.parent[node] = node
        self.rank[node] = 0

    # Time Complexity: O(d), where d is number of depth of the parent tree
    def find_parent(self, child):
        while child != self.parent[child]:
            child = self.parent[child]
            self.parent[child] = self.parent[self.parent[child]]  # Compression
        return self.parent[child]

    # Time Complexity: O(d), where d is number of depth of the parent tree
    def union(self, node_a, node_b):
        parent_a = self.find_parent(node_a)
        parent_b = self.find_parent(node_b)

        if parent_a == parent_b: return

        if self.rank[parent_a] > self.rank[parent_b]:
            self.parent[node_b] = parent_a
        elif self.rank[parent_a] < self.rank[parent_b]:
            self.parent[node_a] = parent_b
        else:
            self.parent[node_b] = parent_a
            self.rank[parent_a] += 1

