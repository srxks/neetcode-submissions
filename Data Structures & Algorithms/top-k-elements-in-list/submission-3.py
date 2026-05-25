from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in set(nums):
            d[i] = nums.count(i)

        l = sorted(d.items(), key=lambda x: x[1], reverse=True)

        return [num for num, freq in l[:k]]