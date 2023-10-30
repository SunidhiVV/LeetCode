class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        while(haystack):
            if haystack.startswith(needle):
                return index
            index +=1
            haystack = haystack[1:]
        return -1

#Random Note
