class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res = 1

        if n >= 0:
            for i in range(n):
                res = res*x
        else:
            n = -n
            for i in range(n):
                res = res*x
            res = 1/res

        return res
