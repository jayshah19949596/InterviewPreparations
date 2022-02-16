
# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag
# pattern on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and
# make this conversion given a number of rows.

# Build a list of chars for each row by tracking
# the direction of movement up or down and
# reversing direction at end rows.
# Time - O(n), use a list of chars and join
# instead of adding to immutable strings.
# Space - O(n)

class Solution(object):
    def convert(self, s: str, num_rows: int) -> str:
        """
        :type s: str
        :type num_rows:

        int :rtype: str
        """
        if num_rows == 1: return s
        row, direction = 0, -1
        table = [[] for i in range(num_rows)]

        for i in range(len(s)):

            if row == 0 or row == num_rows - 1: direction = -1 * direction
            table[row].append(s[i])
            row = row + direction

        return "".join([char for row in table for char in row])
