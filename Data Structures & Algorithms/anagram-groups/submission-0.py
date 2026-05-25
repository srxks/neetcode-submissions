class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        for i in strs:
            k = []
            for j in strs:
                if (sorted(i) == sorted(j)):
                    k += [j]
            if (k not in l):
                l.append(k)
        return l