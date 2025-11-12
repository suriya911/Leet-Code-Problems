class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int dp[105][105];
        int ans = 0;
        memset(dp, 0, sizeof(dp));
        for (auto str : strs) {
            int ones = 0, zeroes = 0;
            for (auto c : str) {
                if (c == '1') ones++;
                if (c == '0') zeroes++;
            }
            for (int i = m; i >= 0; i--) {
                for (int j = n; j >= 0; j--) {
                    if (i - zeroes >= 0 && j - ones >= 0 && dp[i - zeroes][j - ones]) {
                        dp[i][j] = max(dp[i][j], 1 + dp[i - zeroes][j - ones]);
                        ans = max(ans, dp[i][j]);
                    }
                }
            }
            if (zeroes <= m && ones <= n) {
                dp[zeroes][ones] = max(dp[zeroes][ones], 1);
                ans = max(ans, dp[zeroes][ones]);
            }
        }
        return ans;
    }
};