class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low, high = prices[0], 0
        for x in prices:
            if high < x:
                high = x
                if profit < high - low:
                    profit = high - low
            if low > x:
                low = x
                high = 0
        return profit if profit > 0 else 0