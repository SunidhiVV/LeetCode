class Solution:
    def reverse(self, x: int) -> int:
        i = 0
        print(f"x = {x}")
        print(f"i = {i}")
        negative = 0
        if x<0:
            negative = 1
            x = x*(-1)
        while x>=1:
            i = i*10 + x%10
            x = int(x/10)
            print(f"x = {x}")
            print(f"i = {i}")
        if negative:
            i = i*(-1)
        if i > 2**31-1 or i < - (2**31):
            return 0
        return i
        


