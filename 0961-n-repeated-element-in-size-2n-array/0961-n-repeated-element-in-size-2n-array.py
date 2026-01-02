class Solution:
    def repeatedNTimes(self, a: List[int]) -> int:
        d={}
        for i in a:
            if i in d:
                return i
            d[i]=1