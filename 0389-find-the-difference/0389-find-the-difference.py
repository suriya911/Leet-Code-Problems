class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=s.encode('ascii')
        t=t.encode('ascii')

        sa = sum(bytearray(s))
        ta = sum(bytearray(t))

        r=ta-sa

        return (chr(r))