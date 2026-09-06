class Solution:
    def maxArea(self, arr: List[int]) -> int:
        i, j = 0, len(arr)-1
        area = 0
        while i < j:
            area = max(area, (j-i)*min(arr[i], arr[j]))
            if arr[i] < arr[j]:
                i+=1
            else:
                j-=1


        return area