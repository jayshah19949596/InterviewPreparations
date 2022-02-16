# Given an integer array nums, design an algorithm to randomly shuffle the array.
# All permutations of the array should be equally likely as a result of the shuffling.
#
# Implement the Solution class:
#
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.

# Let the given array be arr[].
# A simple solution is to create an auxiliary array temp[] which is initially a copy of arr[].
# Randomly select an element from temp[], copy the randomly selected element to arr[0] and remove the selected element from temp[].
# Repeat the same process n times and keep copying elements to arr[1], arr[2], … .

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        aux = list(self.array)

        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)

        return self.array
