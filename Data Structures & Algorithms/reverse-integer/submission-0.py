class Solution:
    def reverse(self, x: int) -> int:
        
        negative = x < 0
        x = abs(x)

        res = int(str(x)[::-1])

        if negative:
            res = -res

        if res < -(2**31) or res > (2**31) - 1:
            return 0

        return res