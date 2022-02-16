# O(n) to build segment tree
# O(n) space to maintain segment tree
# O(logn) to query segment tree
# Representation of Segment trees
# 1. Leaf Nodes are the elements of the input array.
# 2. Each internal node represents some merging of the leaf nodes. The merging may be different for different problems.
# For this problem, merging is sum of leaves under a node.
# An array representation of tree is used to represent Segment Trees.
# For each node at index i, the left child is at index 2*i+1, right child at 2*i+2 and the parent is at  ⌊(i – 1) / 2⌋.

from math import ceil, log2


class SegmentTree(object):
    def __init__(self):
        self.seg_tree = []
        self.og_arr = []

    def build_tree(self, arr):
        n = len(arr)
        self.og_arr = arr

        # Height of segment tree
        x = ceil(log2(n))

        # Maximum size of segment tree
        max_size = 2 * (2**x) - 1

        # Allocate memory
        self.seg_tree = [[-float('inf'), float('inf'), 0]] * max_size

        # Fill the allocated memory
        self.build_tree_util(arr, 0, n-1, 0)

    def build_tree_util(self, arr, low, high, pos):
        if low == high:
            print(pos, low, high)
            self.seg_tree[pos] = [arr[low], arr[low], arr[low]]
            return

        mid = (high + low) // 2
        self.build_tree_util(arr, low, mid, pos * 2 + 1)
        self.build_tree_util(arr, mid + 1, high, pos * 2 + 2)

        mini = min(self.seg_tree[2 * pos + 1][0], self.seg_tree[2 * pos + 2][0])
        maxi = max(self.seg_tree[2 * pos + 1][1], self.seg_tree[2 * pos + 2][1])
        summ = self.seg_tree[2 * pos + 1][2]+self.seg_tree[2 * pos + 2][2]
        self.seg_tree[pos] = [mini, maxi, summ]

    def query_range(self, low, high, operation):
        if low < 0 or high >= len(self.seg_tree) or low > high:
            return -1

        self.query_range_util(0, len(self.og_arr)-1, low, high, 0, operation)

    def query_range_util(self, ss, se, qs, qe, si, op):

        # If segment of this node is a part of given range,
        # then return the sum of the segment
        if qs <= ss and qe >= se:
            if op == 'MIN': return self.seg_tree[si][0]
            elif op == 'MAX': return self.seg_tree[si][1]
            elif op == 'SUM': return self.seg_tree[si][-1]

        # If segment of this node is
        # outside the given range
        if se < qs or ss > qe: return 0

        # If a part of this segment overlaps
        # with the given range
        mid = ss + (se - ss) // 2

        a = self.query_range_util(ss, mid, qs, qe, 2*si+1, op)
        b = self.query_range_util(mid + 1, se, qs, qe, 2*si+2, op)

        if op == 'MIN':
            return min(a, b)
        elif op == 'MAX':
            return max(a, b)
        elif op == 'SUM':
            return a + b


seg_tree = SegmentTree()
seg_tree.build_tree([1, 3, 5, 7, 9, 11])
print(seg_tree.seg_tree)
print("Sum of values in given range = ", seg_tree.range_sum(1, 3, 'SUM'))
