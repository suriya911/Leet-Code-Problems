class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        bitset<100001> exists;
        int minV = nums[0];
        int maxV = nums[0];

        for (auto v: nums) {
            minV = min(minV, v);
            maxV = max(maxV, v);
            exists[v] = true;
        }

        int seq = 1;
        int start = minV;
        for (int v = minV; v <= maxV; ++v) {
            if (exists[v]) {
                if (v - start > k) {
                    start = v;
                    ++seq;
                }
            }
        }

        return seq;
    }
};