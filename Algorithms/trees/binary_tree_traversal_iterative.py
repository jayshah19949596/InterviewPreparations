from collections import deque


class Node(object):
    def __init__(self, value: str) -> None:
        self.left = None
        self.right = None
        self.value = value


class Tree(object):
    def __init__(self, value: str) -> None:
        self.root = Node(value)

    def pre_order_traversal(self):
        stack, output = [self.root], []
        while stack:
            node = stack.pop()
            if node is None: continue
            output.append(node.value)
            stack.append(node.right)
            stack.append(node.left)
        return output

    def post_order_traversal(self):
        if not self.root: return []
        stack, output = [self.root], deque()  # deque instead of list so we can append at front
        while stack:
            node = stack.pop()
            if not node: continue
            output.appendleft(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return list(output)

    def in_order_traversal(self):
        node, stack, output = self.root, [], []
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return output

    def level_order(self):
        current_level_nodes, result = [self.root], []
        while current_level_nodes:
            next_level_nodes = []
            result.append([])
            for node in current_level_nodes:
                result[-1].append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            current_level_nodes = next_level_nodes
        return result
