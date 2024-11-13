class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());

        return countless(nums, upper) - countless(nums,lower -1);
    }

private:

    long long countless(vector<int>& nums, int sum) {
        long long res = 0;
        int j = nums.size() - 1;

        for(int i = 0; i < j ; i++){
            while(i < j && nums[i] + nums[j] > sum){
                --j;
            }
            res += j-i;
        }
        return res;
    }
};