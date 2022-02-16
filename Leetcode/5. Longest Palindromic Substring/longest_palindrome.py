# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000, and
# there exists one unique longest palindromic substring.

# For each centre point of a character or between 2 characters,
# expand the palindrome if the end characters are the same.
# Return early by starting with the middle centre and
# ruling out later centres that could not have longer
# substring than the palindrome already found.
# Time - O(n^2), 2n centres, each expanded upto n times
# Space - O(n) to store the result

# Note that Manacher's algorithm provides a O(n) time solution.

class Solution:
    def longestPalindrome(self, s):
        longest = ""
        for center in range(2*len(s)-1):
            i, j = center//2, (center//2)+(center%2)
            while i>=0 and j<len(s) and s[i] == s[j]:
                i, j = i-1, j+1
            else:
                i, j = i+1, j-1
            if j-i+1>len(longest): longest = s[i:j+1]
        return longest