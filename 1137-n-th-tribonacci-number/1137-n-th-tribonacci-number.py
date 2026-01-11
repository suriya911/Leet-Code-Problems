class Solution:
    def tribonacci(self, n: int) -> int:
        l=[0,1,1]
        if n<3:
            return l[n]
        for i in range(3,n+1):
            l.append(sum(l[i-3:i]))
        return l[-1]