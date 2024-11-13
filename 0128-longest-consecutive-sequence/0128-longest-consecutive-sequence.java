class Solution {
    int max = 0;
    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Boolean> hashMap = new HashMap<>();
        for (int i : nums)
            hashMap.put(i, true);
        for (int i : nums) {
            int count = 1, j = i;
            while (hashMap.containsKey(--j)) {
                hashMap.remove(j);
                count++;
            }
            j = i;
            while (hashMap.containsKey(++j)) {
                hashMap.remove(j);
                count++;
            }
            max = Math.max(max, count);
        }
        return max;
    }
}