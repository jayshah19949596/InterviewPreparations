# Explanation: https://leetcode.com/problems/number-of-matching-subsequences/discuss/329381/Python-Solution-With-Detailed-Explanation

from collections import defaultdict


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        word_dict = defaultdict(list)
        count = 0

        for word in words:
            word_dict[word[0]].append(word)

        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []

            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence!
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])

        return count