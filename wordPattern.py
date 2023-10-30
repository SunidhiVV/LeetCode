class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strwords = s.split(" ")
        dict_p = {}
        dict_s = {}

        if len(pattern) != len(strwords):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in dict_p:
                dict_p[pattern[i]] = strwords[i]
            if strwords[i] not in dict_s:
                dict_s[strwords[i]] = pattern[i]
            
            if dict_s[strwords[i]] != pattern[i] or dict_p[pattern[i]] != strwords[i]:
                return False
        return True


