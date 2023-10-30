class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        if strs == [""]:
            return ""

        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            for j in range(len(strs)):
                if strs[0][i] != strs[j][i]:
                    return common
            common += strs[0][i]
        
        return common


