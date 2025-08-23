class Solution {
public:
    int hold;
    
    int longestAlternatingSubarray(vector<int>& nums, int threshold) {
        this->hold = threshold;
        int maxi = 0;
        int l=0;
        int n=nums.size();

        while(l < n){
            if(!iseven(nums[l]) || !isless(nums[l])){
                l++;
                continue;
            }

            int r=l+1;

            while(r<n && isless(nums[r]) && isdifferent(nums[r],nums[r-1])){
                r++;
            }

            maxi =  std::max(maxi,r-l);
            l = r;
        }
        return maxi;
    }

    bool isdifferent(int n,int m){
        return n%2 != m%2;
    }

    bool iseven(int n){
        return n%2==0;
    }

    bool isless(int n){
        return n<=hold;
    }

};