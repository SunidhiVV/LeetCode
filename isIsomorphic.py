class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_st = {}
        dict_ts = {}

        for i in range(len(s)):
            if s[i] not in dict_st:
                dict_st[s[i]] = t[i]
            if t[i] not in dict_ts:
                dict_ts[t[i]] = s[i]
            
            if dict_st[s[i]] != t[i] or dict_ts[t[i]] != s[i]:
                return False
        return True
            

