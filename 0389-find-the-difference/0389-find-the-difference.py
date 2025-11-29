class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r=list(t)
        for i in s:
            r.remove(i)
        return r[0]