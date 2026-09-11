class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for i in s:
            s1[i] = s1.get(i, 0) + 1
        for _ in t:
            s2[_] = s2.get(_, 0) + 1
        return s1 == s2