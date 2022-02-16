# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612105/3-Steps
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1613071/Idea-Explained-oror-LCA-Tree-Traversal-and-Backtracking-oror-C%2B%2B-Clean-Code

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def LCA(root, p, q):
            # From : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/
            if not root or p == root.val or q == root.val:  # base cases
                return root

            left_lca = LCA(root.left, p, q)
            right_lca = LCA(root.right, p, q)

            if left_lca and right_lca:
                return root

            if left_lca:
                return left_lca
            else:
                return right_lca

        root = LCA(root, startValue, destValue)  # only this sub-tree matters

        ps = pd = ""
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if node.val == startValue: ps = path
            if node.val == destValue: pd = path
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
        return "U" * len(ps) + pd
