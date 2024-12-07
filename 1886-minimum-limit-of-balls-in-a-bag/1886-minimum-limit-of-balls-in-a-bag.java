class Solution {
    public int minimumSize(int[] nums, int maxOperations) {
     Arrays.sort(nums);

        int low = 1, high = nums[nums.length-1],ans=0;

        while (low <= high) {

            int mid = (low + high) / 2;

            int counter = 0;

            for (int i = 0; i < nums.length; i++) {

                counter = counter + (int)Math.ceil((double)nums[i] / (double)mid) - 1;

            }

            if (counter <= maxOperations) {
                ans = mid;
                high = mid - 1;
            } else
                low = mid + 1;

        }
        return ans;
    }
}