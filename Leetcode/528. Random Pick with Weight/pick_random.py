# https://leetcode.com/problems/random-pick-with-weight/
# Given an array w of positive integers, where w[i] describes
# the weight of index i, write a function pickIndex which
# randomly picks an index in proportion to its weight.

# Create a list of cumulative weights. Choose a random integer
# between 1 and the sum of all weights. Binary search the
# cumulative list for the index where the random integer
# would be inserted and return that index. Probability of
# choosing an index is proprtional to its weight.
# Time - O(n log n) for number of weights n
# Space - O(n)

import random, bisect


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.cumulative = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.cumulative.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        """
        :rtype: int
        """
        # target = self.total_sum * random.random()\
        target = random.randint(1, self.cumulative[-1])
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.cumulative):
            if target <= prefix_sum:
                return i

    def pickIndexBinary(self):
        # target = self.total_sum * random.random()
        target = random.randint(1, self.cumulative[-1])
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()