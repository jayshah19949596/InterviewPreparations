class Node(object):
    def __init__(self, value: str) -> None:
        self.left = None
        self.right = None
        self.value = value


class Tree(object):
    def __init__(self, value: str) -> None:
        self.root = Node(value)

    def pre_order_traversal(self):
        output = []

        def pre_order_traversal_helper(node: Node):
            if not node:
                return
            output.append(node.value)
            pre_order_traversal_helper(node.left)
            pre_order_traversal_helper(node.right)

        pre_order_traversal_helper(self.root)
        return output

    def post_order_traversal(self):
        output = []

        def post_order_traversal_helper(node: Node):
            if not node:
                return
            post_order_traversal_helper(node.left)
            post_order_traversal_helper(node.right)
            output.append(node.value)

        post_order_traversal_helper(self.root)
        return output

    def in_order_traversal(self):
        output = []

        def in_order_traversal_helper(node: Node):
            if not node:
                return
            in_order_traversal_helper(node.left)
            output.append(node.value)
            in_order_traversal_helper(node.right)

        in_order_traversal_helper(self.root)
        return output

