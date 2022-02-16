class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        index2char = {}
        result = []
        for i in range(len(indices)):
            strt_idx = indices[i]
            end_idx = strt_idx + len(sources[i])
            if sources[i] == s[strt_idx:end_idx]:
                index2char[strt_idx] = [i, end_idx]

        i = 0
        while i < len(s):
            char = s[i]

            if i in index2char:
                result.append(targets[index2char[i][0]])
                i = index2char[i][1]
            else:
                result.append(char)
                i += 1

        return "".join(result)
