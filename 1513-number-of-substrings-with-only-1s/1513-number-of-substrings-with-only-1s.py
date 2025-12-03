class Solution:
    def numSub(self, s: str) -> int:
        count = 0 
        total= 0 
        mod = 10**9 + 7 
        for a in s:
            if a=='1':
                count+=1
            else:
                count=0
            total = (total+count)%mod
        return total