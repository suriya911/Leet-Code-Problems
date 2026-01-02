class Solution:
    def pivotInteger(self, n: int) -> int:
        l=[i+1 for i in range(n)]

        for x in range(n):
            if sum(l[:x+1])==sum(l[x:]):
                return l[x]
        return -1