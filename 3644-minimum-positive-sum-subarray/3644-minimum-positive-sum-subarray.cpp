class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size();
        int sm = INT_MAX;

        for (int win = l; win <= r; win++) { 
            int s = 0;

            for (int i = 0; i < win; i++) s += nums[i];
            if (s > 0) sm = min(sm, s);

            for (int i = win; i < n; i++) {
                s += nums[i];
                s -= nums[i - win];
                if (s > 0) sm = min(sm, s);
            }
        }

        return (sm == INT_MAX ? -1 : sm);
    }
};