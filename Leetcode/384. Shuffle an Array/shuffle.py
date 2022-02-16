# Given an integer array nums, design an algorithm to randomly shuffle the array.
# All permutations of the array should be equally likely as a result of the shuffling.
#
# Implement the Solution class:
#
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.

# Fisher Yates algorithm
# The idea is to start from the last element
# Swap it with a randomly selected element from the whole array (including last).
# Now consider the array from 0 to n-2 (size reduced by 1), and repeat the process till we hit the first element.
#
# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
