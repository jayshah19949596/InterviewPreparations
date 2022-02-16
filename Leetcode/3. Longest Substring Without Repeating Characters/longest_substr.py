# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest
# substring without repeating characters.

# Maintain a sliding window, updating the start
# whenever we see a character repeated.
# Time - O(n)
# Space - O(1), dictionary is limited by fixed size alphabet

class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}                                       # mapping from character to its last seen index in s
        start, longest = 0, 0                                # start index of current substring

        for end, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1                  # start a new substring after the previous sighting of char
            else:
                longest = max(longest, end - start + 1)
            last_seen[char] = end                            # update the last sighting index
        return longest
