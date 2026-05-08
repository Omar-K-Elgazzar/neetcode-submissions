class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = 0
        output = []
        while counter <= n:
            output.append(bin(counter).count("1"))
            counter += 1
        return output