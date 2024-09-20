class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> h = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(h.containsKey(target-nums[i]))
                return new int[]{h.get(target-nums[i]),i};
            h.put(nums[i],i);
        }
        return new int[]{};
    }
}