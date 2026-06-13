class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        seen = []

        for number in nums:
            if number in seen:
                return number
            else:
                seen.append(number)

        