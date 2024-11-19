class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long global, local;
        global = local = 0;
        
        bool pre[(int)(1e5 + 1)] = {false};
        
        int l, r, n = nums.size();

        for(l = r = 0; l < n; l++) {
            local += nums[l];
            while(pre[nums[l]] || l - r == k) {
                local -= nums[r];
                pre[nums[r++]] = false;
            }
            pre[nums[l]] = true;

            if(l - r + 1 == k)
                global = max(global, local);
        }
        
        return global;
    }
};