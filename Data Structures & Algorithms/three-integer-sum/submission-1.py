class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 1. Sorting is mandatory for the two-pointer strategy to work
        nums.sort() 
        
        for i in range(len(nums) - 2):
            # 2. Skip the same element to avoid duplicate triplets in the output
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 3. Initialize the two pointers
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                
                if total_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    # 4. Move pointers and skip duplicates for j and k
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                        
                    j += 1
                    k -= 1
                elif total_sum < 0:
                    # Sum is too small; move the left pointer to get a larger value
                    j += 1
                else:
                    # Sum is too large; move the right pointer to get a smaller value
                    k -= 1
                    
        return res
