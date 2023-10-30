class Solution:
    def isValid(self, s: str) -> bool:
        openings = '({['
        closings = ')}]'
        stack = []
        for i in s:
            if i in openings:
                stack.append(i)
            elif i in closings:
                if not stack:
                    return False
                last = stack.pop()
                if (i ==')' and last != '(') or (i =='}' and last != '{') or (i ==']' and last != '['):
                    return False
        if stack:
            return False
        return True


