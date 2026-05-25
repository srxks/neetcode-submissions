class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        for i in range(32):
            mask = 1 << i
            if n & mask:
                c += 1
        return c