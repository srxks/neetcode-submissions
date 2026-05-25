from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:          # Note: < instead of <=
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]   # 1-based indices
                
            elif current_sum < target:
                left += 1                    # Need bigger numbers
            else:
                right -= 1                   # Need smaller numbers
                
        # Problem guarantees exactly one solution, so this line shouldn't be reached
        return []