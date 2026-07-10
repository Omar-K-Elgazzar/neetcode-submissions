class Solution:
    def combinationSum(self, nums: List[int], target: int):

        result = []

        def dfs(start, remaining, path):

            if remaining == 0:
                result.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])

                dfs(i, remaining - nums[i], path)

                path.pop()

        dfs(0, target, [])

        return result