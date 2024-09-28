class Solution {
    public boolean containsDuplicate(int[] nums) {
       Set<Integer> s = new HashSet<>();
        for (int num : nums) {
            if (!s.add(num)) {  // if add returns false, there's a duplicate
                return true;
            }
        }
        return false;
    }
}