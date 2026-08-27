class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = dict(), dict()
        for i in set(s):
            d1[i] = s.count(i)
        
        for j in set(t):
            d2[j] = t.count(j)

        return d1 == d2