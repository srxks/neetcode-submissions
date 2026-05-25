class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        s = list(set(nums))
        for i in s:
            if (nums.count(i) > 1):
                return True
                break
        else:
            return False