class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n<2 or k==0:
            return 0
        dp_prev = [0] * n
        dp_cur = [0] * n
        for t in range(1,k+1):
            best_buy = -prices[0]
            best_short = prices[0]
            dp_cur[0] = 0

            for i in range(1,n):
                a = dp_cur[i-1]
                b = best_buy + prices[i]
                c = best_short - prices[i]

                dp_cur[i] = max(a,b,c)

                best_buy = max(best_buy, dp_prev[i-1] - prices[i])
                best_short = max(best_short, dp_prev[i-1] + prices[i])

            dp_prev, dp_cur = dp_cur, dp_prev
        return dp_prev[-1]