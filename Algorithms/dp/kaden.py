# Kadane’s Algorithm can be viewed both as a greedy and DP.
# Kadane's keeps a running sum of integers and when it becomes less than 0, it reset  to 0 (Greedy Part).
# This is because continuing with a negative sum is way more worse than restarting with a new range.
# Now it can also be viewed as a DP, at each stage we have 2 choices:
# Either take the current element and continue with previous sum OR restart a new range.
# These both choices are being taken care of in the implementation/
# Limitation:
#        1. Algorithm does not work with test case where array has all negative integers
# Complexity Analysis:
#       Time Complexity: O(1)
#       Space Complexity: O(1)

def kadenze_max_sum_subarray(array):
    max_so_far = array[0]
    curr_max = array[0]
    for i in range(1, len(array)):
        curr_max = max(array[i], curr_max + array[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far
