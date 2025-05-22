class Solution {
    public int maxRemoval(int[] nums, int[][] queries) {
        Arrays.sort(queries, (a, b) -> a[0] - b[0]);
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        int[] delta = new int[nums.length + 1];
        for (int i = 0, j = 0; i < nums.length; i++) {
            delta[i] += (i == 0) ? 0 : delta[i - 1];
            int v = nums[i] - delta[i];
            for (; j < queries.length && queries[j][0] == i; j++) {
                pq.offer(queries[j][1]);
            }
            while (v > 0) {
                if (pq.isEmpty()) {
                    return -1;
                }
                int x = pq.remove();
                if (x >= i) {
                    v--;
                    delta[i]++;
                    delta[x + 1]--;
                }
            }
        }
        return pq.size();
    }
}