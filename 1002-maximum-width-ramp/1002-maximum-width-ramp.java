class Solution {
    public int maxWidthRamp(int[] nums) {
        int n = nums.length;
        List<Integer> dec = new ArrayList<>();
        dec.add(0);

        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[dec.get(dec.size() - 1)]) {
                dec.add(i);
            }
        }

        int max = 0;

        for (int i = n - 1; i >= 0; i--) {
            while (!dec.isEmpty() && nums[i] >= nums[dec.get(dec.size() - 1)]) {
                max = Math.max(max, i - dec.get(dec.size() - 1));
                dec.remove(dec.size() - 1);  // pop the stack
            }
        }

        return max;
    }
}