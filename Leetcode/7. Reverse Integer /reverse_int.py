# https://leetcode.com/problems/reverse-integer/
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Repeatedly multiply previous result by 10 and add last digit.
# Time - O(n) where n is the number of digits.
# Space - O(n), same number of digits in output as input.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            x = abs(x)
            negative = True

        rev = 0
        while x != 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10

        if rev > 2 ** 31 - 1: return 0
        if negative: return -rev
        return rev
