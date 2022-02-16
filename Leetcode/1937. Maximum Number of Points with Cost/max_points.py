# You are given an m x n integer matrix points (0-indexed). Starting with 0 points,
# you want to maximize the number of points you can get from the matrix.
#
# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c)
# will add points[r][c] to your score.
#
# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row.
# For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2)
# will subtract abs(c1 - c2) from your score.
#
# Return the maximum number of points you can achieve

# Explaination:
# https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/C%2B%2BJavaPython-3-DP-Explanation-with-pictures.
# Time - O(rows*cols)

class Solution:
    def maxPoints(self, array: List[List[int]]) -> int:
        rows, cols = len(array), len(array[0])
        if rows == 1: return max(array[0])
        if cols == 1: return sum(sum(x) for x in array)

        def left(prv_row):
            lft = [prv_row[0]] + [0] * (cols - 1)
            for col in range(1, cols):
                lft[col] = max(lft[col - 1] - 1, prv_row[col])  # max(lft[col-1] - ABS((col-1)-col), prv_row[col])
            return lft

        def right(prv_row):
            rgt = [0] * (cols - 1) + [prv_row[-1]]
            for col in range(cols - 2, -1, -1):
                rgt[col] = max(rgt[col + 1] - 1, prv_row[col])  # max(rgt[col-1] - ABS((col-(col+1)), prv_row[col])
            return rgt

        prev_row = array[0]
        for row in range(rows - 1):
            lft, rgt, cur_row = left(prev_row), right(prev_row), [0] * cols
            for col in range(cols):
                cur_row[col] = array[row + 1][col] + max(lft[col], rgt[col])
            prev_row = cur_row[:]
        return max(cur_row)

