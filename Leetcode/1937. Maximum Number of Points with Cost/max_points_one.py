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

# Time - O(rows*cols^2)

class Solution:
    def maxPoints(self, arr: List[List[int]]) -> int:
        rows, cols = len(arr), len(arr[0])
        if rows == 1: return max(arr[0])
        if cols == 1: return sum(sum(x) for x in arr)

        score_arr = []
        for i in range(rows):
            score_arr.append([])
            for j in range(cols):
                score_arr[i].append(0)

        for col in range(cols):
            score_arr[0][col] = arr[0][col]

        for row in range(1, rows):
            for col in range(cols):
                max_val = 0
                for prev_rows_col in range(cols):
                    max_val = max(max_val, score_arr[row - 1][prev_rows_col] - abs(col - prev_rows_col))
                score_arr[row][col] = max_val + arr[row][col]

        return max(score_arr[-1])
