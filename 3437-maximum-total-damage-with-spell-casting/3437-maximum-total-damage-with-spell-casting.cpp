class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        int n = power.size();
        sort(power.begin(), power.end());

        vector<long long> dp(n, 0);
        dp[0] = power[0];
        long long ans = power[0];
        long long maxPow = 0;

        for(int i = 1, j = 0; i < n; i++){
            if(power[i]==power[i-1]){
                dp[i] = power[i] + dp[i-1];
            }
            else{
                while(power[j]+2 < power[i]){
                    maxPow = max(maxPow, dp[j]);
                    j++;
                }
                dp[i] = maxPow + power[i];
            }
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};