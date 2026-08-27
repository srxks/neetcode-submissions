class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in hashmap:
                return [hashmap[find], i]
            hashmap[nums[i]] = i
        
        return [0,0]