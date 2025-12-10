class Solution {
public:

    int MOD = 1e9+7;
    int countPermutations(vector<int>& complexity) {
        int n=complexity.size();

        long long ans = 1;
        for(int i=1;i<n;i++){
            if(complexity[i] <= complexity[0]) return 0;
            ans *= i;
            ans%= MOD;
        }

        return ans;
    }
};