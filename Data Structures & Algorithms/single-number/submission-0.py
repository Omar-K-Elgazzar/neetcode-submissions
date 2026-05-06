class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        search_point = 0
        found = False
        while not found:
            integer = nums[search_point]
            sub_nums = nums[:search_point] + nums[search_point+1:]
            if integer not in sub_nums:
                found = True
            else:
                search_point += 1
        return integer