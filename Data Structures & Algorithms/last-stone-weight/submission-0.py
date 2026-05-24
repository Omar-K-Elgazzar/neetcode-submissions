class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            crashedStone = stones[-1] - stones[-2]
            stones.pop(-1)
            stones.pop(-1)
            if crashedStone != 0:
                stones.append(crashedStone)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0