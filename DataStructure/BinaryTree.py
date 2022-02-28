class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
