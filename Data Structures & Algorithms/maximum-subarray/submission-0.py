class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):

            # Greedy choice:
            # either start new subarray
            # or continue existing one
            current_sum = max(nums[i], current_sum + nums[i])

            # update global maximum
            max_sum = max(max_sum, current_sum)

        return max_sum