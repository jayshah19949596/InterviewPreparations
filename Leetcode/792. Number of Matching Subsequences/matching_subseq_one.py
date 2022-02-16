class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        results = 0
        for word in words:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                    if j == len(word):
                        results += 1
                        break
                else:
                    i += 1
        return results
