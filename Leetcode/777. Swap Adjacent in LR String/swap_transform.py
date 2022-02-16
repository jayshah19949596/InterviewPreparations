# In a string composed of 'L', 'R', and 'X' characters,
# like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX",
# or replacing one occurrence of "RX" with "XR".
# Given the starting string start and the ending string end, return True if and only if there exists a sequence of
# moves to transform one string to the other.
# https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/217070/Python-using-corresponding-position-
# https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/1536718/Python-Check-their-positions-with-Picture-Clean-and-Concise


# Operations:
# 1. The letter "L" can only move to left until it encounters "R" or another "L".
# 2. Similarly, letter "R" can only move to right until it encounters "R" or "L".
# Hence:
# 1. The numbers of "R"s and "L"s in "start "must be same as the numbers of "L"s and "R"s in "end".
# 2. The index "i" of "R" in "start" must be smaller than/in the left of the index "j" of the corresponding "R" in "end"
# 3. The index "i" of "L" in "start" must be greater than/in the ryt of the index "j" of the corresponding "L" in "end"

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end): return False

        start_processed = [(s, idx) for idx, s in enumerate(start) if s == 'L' or s == 'R']
        end_processed = [(e, idx) for idx, e in enumerate(end) if e == 'L' or e == 'R']
        if len(start_processed) != len(end_processed): return False

        for (s, i), (e, j) in zip(start_processed, end_processed):
            if s != e: return False
            if s == 'L':
                if i < j: return False
            if s == 'R':
                if i > j: return False

        return True