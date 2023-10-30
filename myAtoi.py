class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        p = 1
        num=0
        nums="0123456789"
        for i in range(len(s)):
            if i == 0 and s[i] == '-':
                p = -1
                continue
            elif i == 0 and s[i] == '+':
                continue
            elif s[i] not in nums:
                break
            else:
                num = num*10+int(s[i])
        res = p*num
        if res < -(2**31):
            res = -(2**31)
        elif res > 2**31 - 1:
            res = 2**31-1
        return res


