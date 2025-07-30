class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size();
        int len = 0;
        int maxn = *max_element(nums.begin(),nums.end()); 
        int count =0;
        for(int i=0;i<n;i++){ 
            if(nums[i]==maxn){
                count++; 
            }
            else{
                len = max(len, count);
                count=0;
            }
        }

        len = max(len, count);

        return len;
    }
};