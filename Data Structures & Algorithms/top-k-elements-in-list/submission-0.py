class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        nums.sort()

        frequency = {}

        curr = nums[0]
        count = 0

        for num in nums:
            if num == curr:
                count += 1
            else:
                curr = num
                count = 1

            frequency[curr] = count

        sorted_items = sorted(
            frequency.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [num for num, freq in sorted_items[:k]]