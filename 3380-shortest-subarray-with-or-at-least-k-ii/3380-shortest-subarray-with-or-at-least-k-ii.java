class Solution {
    public int minimumSubarrayLength(int[] nums, int k) {
        if (k == 0) return 1;

        int[] bit = new int[32];
        int n = nums.length;
        int orr = 0, ans = Integer.MAX_VALUE, j = 0;

        for (int i = 0; i < n; i++) {
            if (i > 0) {
                for (int m = 31; m >= 0; m--) {
                    if (((1 << m) & nums[i - 1]) != 0) {
                        if (bit[m] == 1) orr -= (1 << m);
                        bit[m]--;
                    }
                }
            }
            while (j < n && orr < k) {
                orr |= nums[j];
                for (int m = 31; m >= 0; m--) {
                    if (((1 << m) & nums[j]) != 0)
                        bit[m]++;
                }
                j++;
            }
            if (orr >= k)
                ans = Math.min(ans, j - i);
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}