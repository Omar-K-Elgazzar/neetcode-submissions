class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num   #. "^" is an XOR function, where a ^ a = 0 (same numbers cancel out) and a ^ 0 = a
        return result