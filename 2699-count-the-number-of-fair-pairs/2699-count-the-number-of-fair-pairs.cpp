class Solution {
public:
    int n;
    long long cnt(vector<int>& nums, int x){
        int l=0, r=n-1;
        long long ans=0;
        while(l<r){
            int s=nums[l]+nums[r];
            if (s<x) {
                ans+=(r-l);
                l++;
            }
            else r--;
        }
        return ans;

    }
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        n=nums.size();
        return cnt(nums, upper+1)-cnt(nums, lower);
    }
};