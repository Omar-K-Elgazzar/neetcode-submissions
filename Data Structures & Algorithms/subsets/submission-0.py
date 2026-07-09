class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        subset = []

        def backtrack(index):
            # Base case: we've considered every number
            if index == len(nums):
                result.append(subset[:])   # Make a copy
                return

            # Choice 1: Include nums[index]
            subset.append(nums[index])
            backtrack(index + 1)

            # Undo the choice
            subset.pop()

            # Choice 2: Don't include nums[index]
            backtrack(index + 1)

        backtrack(0)
        return result

        