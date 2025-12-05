class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime=[2,3,5,7,11,13,17,19]
        res=0
        for i in range(left,right+1):
            x = i.bit_count()
            if x in prime:
                res+=1
        return res