class Solution:
    def search(self, n: List[int], target: int) -> int:
        l = 0
        u = len(n)-1
        while l <= u:
            mid = (l+u)//2
            if target == n[mid]:
                return mid
            elif target > n[mid]:
                l = mid+1
            elif target < n[mid]:
                u = mid-1

        return -1