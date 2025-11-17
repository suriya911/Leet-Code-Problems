class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for l in range(n - length + 1):

                r = length + l - 1

                takeLeft = nums[l] - dp[l + 1][r] 

                takeRight = nums[r] - dp[l][r - 1]

                dp[l][r] = max(takeLeft, takeRight)
        
        return dp[0][n - 1] >= 0




