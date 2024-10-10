class Solution {
    public int maxWidthRamp(int[] nums) {
        int low = 1, high = nums.length-1, res = 0;

        while(low <= high) {
            int mid = low + (high - low)/2;
            if(pos(nums, mid)) {
                res = mid;
                low = mid + 1;
            } else high = mid - 1;
        }
        return res;
    }

    private boolean pos(int[] nums, int width) {
        int i=0,j=width;
        int min = nums[i];
        while(j < nums.length) {
            if(nums[j] >= min) return true;
            j++;
            min = Math.min(min, nums[++i]);
        }   
        return false;
    }
}