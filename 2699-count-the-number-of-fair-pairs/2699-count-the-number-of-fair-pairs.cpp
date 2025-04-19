class Solution {
public:
    long long solve(vector<int>& nums, int value) {
        int l = 0, r = nums.size() - 1;
        long long ans = 0;
        while (l < r) {
            if (nums[l] + nums[r] >= value)
                r--;
            else {
                ans += (r - l);
                l++;
            }
        }
        return ans;
    }

    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        return solve(nums, upper + 1) - solve(nums, lower);
    }
};