class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        for i in range(32):
            if (1 << i) & n:
                output += 1
        return output