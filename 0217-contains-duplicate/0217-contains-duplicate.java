class Solution {
    public boolean containsDuplicate(int[] nums) {
       Set<Integer> s = IntStream.of(nums).boxed().collect(Collectors.toSet());
        return s.size() != nums.length;
    }
}