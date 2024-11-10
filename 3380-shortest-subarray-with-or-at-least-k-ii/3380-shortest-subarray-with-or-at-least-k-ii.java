class Solution {
     public int minimumSubarrayLength(int[] nums, int k) {
        int w = 0, min = Integer.MAX_VALUE;
        int[] bits = new int[32]; // bits' counts
        for (int l = 0, r = 0; r < nums.length; r++) {
            if (nums[r] >= k) return 1;
            w |= nums[r];
            for (int i = 0; i < bits.length; i++) {
                bits[i] += (nums[r] >> i) & 1;
            }
            while (w >= k) {
                min = Math.min(min, r - l + 1);
                for (int i = 0; i < bits.length; i++) {
                    bits[i] -= (nums[l] >> i) & 1;
                    if (bits[i] == 0) w &= ~(1 << i);
                }
                l++;
            } 
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    }
    // public int minimumSubarrayLength(int[] nums, int k) {
    //     if (k == 0) return 1;

    //     int[] bit = new int[32];
    //     int n = nums.length;
    //     int orr = 0, ans = Integer.MAX_VALUE, j = 0;

    //     for (int i = 0; i < n; i++) {
    //         if (i > 0) {
    //             for (int m = 31; m >= 0; m--) {
    //                 if (((1 << m) & nums[i - 1]) != 0) {
    //                     if (bit[m] == 1) orr -= (1 << m);
    //                     bit[m]--;
    //                 }
    //             }
    //         }
    //         while (j < n && orr < k) {
    //             orr |= nums[j];
    //             for (int m = 31; m >= 0; m--) {
    //                 if (((1 << m) & nums[j]) != 0)
    //                     bit[m]++;
    //             }
    //             j++;
    //         }
    //         if (orr >= k)
    //             ans = Math.min(ans, j - i);
    //     }
    //     return ans == Integer.MAX_VALUE ? -1 : ans;
    // }
}