class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter = 0;
        while counter in nums:
            counter += 1
        return counter