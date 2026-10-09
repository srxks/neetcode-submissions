class Solution:
    def maxProfit(self, p: List[int]) -> int:
        res = 0
        minBuy = p[0]

        for i in p:
            res = max(res, i - minBuy)
            minBuy = min(minBuy, i)
        return res