
class QuadTreeNode:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class QuadTree(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def helper(r, c, side):     # construct quad tree for grid from cell (r, c) with side length of side

            if side == 1:           # base case of single cell
                return QuadTreeNode(bool(grid[r][c]), True, None, None, None, None)

            top_left = helper(r, c, side // 2)
            top_right = helper(r, c + side // 2, side // 2)
            bottom_left = helper(r + side // 2, c, side // 2)
            bottom_right = helper(r + side // 2, c + side // 2, side // 2)

            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf:
                if top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                    return QuadTreeNode(top_left.val, True, None, None, None, None)

            node_val = any((top_left.val, top_right.val, bottom_left.val, bottom_right.val))
            print(node_val, top_left.val)
            return QuadTreeNode(node_val, False, top_left, top_right, bottom_left, bottom_right)

        if not grid:
            return None
        return helper(0, 0, len(grid))
