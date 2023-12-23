from collections import defaultdict, deque
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

    # function to add an edge to graph
    def add_relation(self, from_node, to_node):
        ## CHILDREN TO PARENT MAPPING
        self.graph[to_node].add(from_node)  ### This is a reverse graph TO_NODE -> FROM_NODE

    def topological_sort_util(self, children_node, visited, topo_sort):

        # Mark the current node as visited.
        visited.add(children_node)

        # Recur for all the vertices adjacent to this vertex
        for parent_neighbors in self.graph[children_node]:
            if not visited[parent_neighbors]:
                self.topological_sort_util(parent_neighbors, visited, topo_sort)

        # Push current vertex to stack which stores result
        topo_sort.appendleft(children_node)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topological_sort(self):
        # Mark all the vertices as not visited
        visited = set([])
        topo_sort = deque([])

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for children_node in range(self.graph):
            if not visited[children_node]:
                self.topological_sort_util(children_node, visited, topo_sort)

        print(topo_sort)  # Print contents of the stack
