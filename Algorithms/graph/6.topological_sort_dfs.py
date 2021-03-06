from collections import defaultdict

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
        self.graph[from_node].add(to_node)

    def topological_sort_util(self, cur_node, visited, stack):

        # Mark the current node as visited.
        visited.add(cur_node)

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[cur_node]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(cur_node)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topological_sort(self):
        # Mark all the vertices as not visited
        visited = set([])
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for node in range(self.V):
            if not visited[node]:
                self.topological_sort_util(node, visited, stack)

        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order
