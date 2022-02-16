# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution.


# For each element, we try to find its complement by looping through the rest of the array
# The space required does not depend on the size of the input array, so only constant space is used.
#
# Time complexity: O(n^2)
# Space complexity: O(1)
#

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

# Maintain a mapping from each number to its index.
# Check if target - num has already been found.
# Time - O(n)
# Space - O(n) for the dictionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num2idx = {}
        for i in range(len(nums)):
            num = nums[i]
            to_find = target-num
            if to_find in num2idx:
                return [num2idx[to_find], i]
            num2idx[num] = i
        return [-1, -1]
