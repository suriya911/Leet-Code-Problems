class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        @lru_cache(None)
        def countWithout1s(n:int,maxVal:int): # num of distinct numbers 
            if n == 1:
                return maxVal - 1
            ans=0
            for i in range(2, maxVal // 2**(n-1) + 1):
                ans += countWithout1s(n-1, maxVal//i)
            return ans

        MOD, comb, ans = 10**9+7, 1, 1
        for i in range(1,floor(log2(maxValue))+1):
            comb = comb * (n - i + 1) // i
            ans += comb * countWithout1s(i, maxValue)
        return ans%MOD