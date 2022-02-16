# Whenever the current element "cur_num" is bigger than the previous element "prev_num",
# we need at lease "cur_num - prev_num" operations to make this difference.

# We accumulate the total number of the operations,
# this result is a lower bound and it's feasible.

# Time O(N)
# Space O(1)
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/discuss/754682/Wall-of-bricks
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/discuss/754674/JavaC%2B%2BPython-Comparison-of-Consecutive-Elements
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        min_ops = prev_num = 0
        for cur_num in target:
            min_ops += max(cur_num - prev_num, 0)
            prev_num = cur_num
        return min_ops
