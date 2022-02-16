# https://leetcode.com/problems/find-original-array-from-doubled-array/
# An integer array original is transformed into a doubled array changed by appending twice the value of every
# element in original, and then randomly shuffling the resulting array.
#
# Given an array changed, return original if changed is a doubled array.
# If changed is not a doubled array, return an empty array.
# The elements in original may be returned in any order.

# Time Complexity: O(n*log(n)) + O(n)
# Space Complexity: O(n) for freq_map hash_map

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0: return []

        changed.sort()
        n, freq_map, res = len(changed) - 1, defaultdict(int), []
        for num in changed: freq_map[num] += 1

        for i in range(n):

            if changed[i] in freq_map:

                freq_map[changed[i]] -= 1

                if freq_map[changed[i]] == 0:
                    del freq_map[changed[i]]

                if 2 * changed[i] not in freq_map:
                    return []
                else:
                    freq_map[2 * changed[i]] -= 1
                    if freq_map[2 * changed[i]] == 0: del freq_map[2 * changed[i]]

                res.append(changed[i])
                if 2 * len(res) == len(changed): return res

        return res