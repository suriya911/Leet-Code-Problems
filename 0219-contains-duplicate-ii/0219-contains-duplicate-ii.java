class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int c = 0;
        for (int i = 0; i < nums.length; i++)
            for (int j = Math.min(i + k, nums.length - 1); j > i; j--, c++) {
                if (nums[i] == nums[j])
                    return true;
                if (c > 9999)
                    return false;
            }
        return false;
    }
}