class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits) - 1
        while digits[size] == 9 and size >= 0:
            digits[size] = 0
            size -= 1
        
        if size < 0:
            digits.insert(0, 1)
        else:
            digits[size] += 1

        return digits

        