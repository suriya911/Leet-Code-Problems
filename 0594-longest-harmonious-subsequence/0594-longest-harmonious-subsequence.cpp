class Solution {
public:
    int findLHS(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l=0, r=0, ans=0, n= nums.size();
        while(r<n){
            int d= nums[r]- nums[l];
            if(d==1)    ans=max(ans, r-l+1);
            if(d<=1)    r++;
            else        l++;
        }
        return ans;
    }
};