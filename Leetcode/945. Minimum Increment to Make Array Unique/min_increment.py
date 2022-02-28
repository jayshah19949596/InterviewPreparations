# Approach 1: Counting
# -------------------
# Intuition:
# -------------------
# Let's count the quantity of each element. Since our goal is to make every value unique, we will need to increment duplicate values.
# For each duplicate value, we could take the "brute force" approach and increment it repeatedly until it is unique.
# However, this might require a lot of work - consider the work done for an array of all ones.
# We should think of how to amend our solution to solve this case as well.
# What we can do instead is lazily evaluate our increments.
# If for example, we have [1, 1, 1, 1, 3, 5], we don't need to process all the increments of duplicate 1s.
# We could take the three duplicate ones (taken = [1, 1, 1]) and continue processing.
# When we find an empty place like 2, 4, or 6, we can then determine that our increment will be 2-1, 4-1, and 6-1.
# -------------------
# Algorithm:
# -------------------
# 1. First count how many times each value occurs in nums.
# 2. Iterate over all possible values of x. Note that the x will never be larger than the largest value in nums plus the length of nums. For each possible value of x:
#       - If there are 2 or more values x in nums, save the duplicate values to increment later.
#       - If there are 0 values x in nums, then the last saved value in taken gets incremented to x.

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        count, max_val = collections.Counter(nums), max(nums)
        taken_num, change_moves = [], 0

        for cur_num in range(len(nums) + max_val):

            if count[cur_num] >= 2:
                taken_num.extend([cur_num] * (count[cur_num] - 1))
            elif taken_num and count[cur_num] == 0:
                duplicate_num = taken_num.pop()
                change_moves += cur_num - duplicate_num  # Change duplicate number to current number whose count is 0

        return change_moves
