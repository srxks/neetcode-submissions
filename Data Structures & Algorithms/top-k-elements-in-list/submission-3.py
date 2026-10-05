from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], p: int) -> List[int]:
        k = Counter(nums)

        return [item[0] for item in k.most_common(p)]