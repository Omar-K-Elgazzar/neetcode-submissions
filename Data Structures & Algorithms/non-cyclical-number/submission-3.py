class Solution:
    def isHappy(self, n: int, past_totals = None) -> bool:
        if past_totals is None:
            past_totals = []

        digits = list(str(n))
        total = 0
        for x in digits:
            total += pow(int(x),2)

        if total == 1:
            return True
        elif total in past_totals:
            return False
        else:
            past_totals.append(total)
            return self.isHappy(total, past_totals)

