class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        for i in s:
            mapping_s[i] = mapping_s.get(i, 0) + 1
        for j in t:
            mapping_t[j] = mapping_t.get(j, 0) + 1
        return mapping_s == mapping_t