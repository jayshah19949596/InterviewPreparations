# https://leetcode.com/problems/palindrome-number/
# Determine whether an integer is a palindrome. Do this without extra space.

# Check equivalence of first and last characters, moving inwards.
# Time - O(n)
# Space - O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        num, rev = x, 0

        while num > 0:
            rem = num % 10
            rev = 10 * rev + rem
            num = num // 10

        if rev == x: return True
        return False