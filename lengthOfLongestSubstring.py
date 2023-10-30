class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()

        start, end = 0, 0
        maxlen = 0

        while end < len(s):
            if s[end] not in substring:
                substring.add(s[end])
                maxlen = max(maxlen, end - start + 1)
                end += 1
            elif s[end] in substring:
                substring.remove(s[start])
                start +=1
        
        return maxlen
                

