# You are given an m x n binary matrix grid.
# In one operation, you can choose any row or column and flip each value in that row or column
# (i.e., changing all 0's to 1's, and all 1's to 0's).
# Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.
# Explanation:
# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/discuss/1671908/Python-3-or-Math-or-Explanation

'''
001100 and 001100 are the same pattern
001100 and 110011 (the invert of original) are the same pattern
'''


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1, r1_invert = grid[0], [1-val for val in grid[0]]
        for i in range(1, len(grid)):
            if grid[i] != r1 and grid[i] != r1_invert:
                return False
        return True
