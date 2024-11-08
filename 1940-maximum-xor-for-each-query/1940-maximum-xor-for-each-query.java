class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        int n = nums.length;
        int xor = nums[0];
        int maxi = (1 << maximumBit) - 1;

        for(int i=1; i<n; i++){
            xor ^= nums[i];
        }

        int ans[] = new int[n];
        for(int i=0; i<n; i++){
            ans[i] = xor ^ maxi;
            xor ^= nums[n-1-i];
        }

        return ans;
    }
}