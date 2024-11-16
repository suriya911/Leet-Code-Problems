class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        vector<int> res;
        int l=0;
        int con = 1;

        for(int r = 0; r<nums.size(); r++){
            if(r > 0 && nums[r - 1]+1 == nums[r]){
                con++;
            }

            if(r - l + 1 > k){
                if(nums[l] + 1 == nums[l+1]){
                    con--;
                }
                l++;
            }

            if(r - l + 1 == k){
                res.push_back(con == k ? nums[r] : -1);
            }
        }
        return res;
    }
};