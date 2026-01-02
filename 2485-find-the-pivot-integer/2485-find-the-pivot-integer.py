class Solution:
    def pivotInteger(self, n: int) -> int:
        m=sqrt((n*(n+1))//2)
        if m.is_integer(): return int(m)
        else: return -1
        