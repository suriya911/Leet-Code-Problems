class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n=nums.size();
        if(n==1){
            return 0;
        }

        sort(nums.begin(),nums.end());

        int min = nums[nums.size()-1];
        for(int i=0;i+k-1<nums.size();i++){
            int j=i+k-1;
            int diff = nums[j]-nums[i];
            min = min<diff ? min:diff;
        }
        return min;
    }
};