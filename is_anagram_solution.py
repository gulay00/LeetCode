class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            t = list(t)
            for x in s:
                if x not in t:
                    return False
                t.remove(x)
            return True
        return False
