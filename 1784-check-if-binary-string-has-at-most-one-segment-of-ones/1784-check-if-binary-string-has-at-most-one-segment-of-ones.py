class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i, comp = 0, 0
        while i < len(s):
            if comp and s[i] == "1":
                return False
            if s[i] == "1":
                while (i+1 < len(s) and s[i+1] == "1"):
                    i+= 1
                comp = 1
            i+= 1
        return True
