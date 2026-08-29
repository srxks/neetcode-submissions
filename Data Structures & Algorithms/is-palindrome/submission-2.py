class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = [x.lower() for x in s if (x != " " and x.isalnum())]
        l, f = 0, len(k)-1
        while l < f:
            print(k[l], k[f])
            if k[l] != k[f]:
                return False
            
            l += 1
            f -= 1


        return True