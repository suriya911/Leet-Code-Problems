class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        
        for(int i = 0; i < nums.length; i++) {
            if(!set.add(nums[i])) {
                return true;
            }
            if(i >= k) {
                set.remove(nums[i - k]); 
            }
        }
        
        return false;
    }
}