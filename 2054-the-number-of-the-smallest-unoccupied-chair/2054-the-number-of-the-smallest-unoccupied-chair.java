class Solution {
    public int smallestChair(int[][] times, int target) {
        int n = times.length, max = -1, end = -1, start = times[target][0];
        Arrays.sort(times, (a, b) -> a[0] - b[0]);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        PriorityQueue<Integer> seats = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            while (!pq.isEmpty() && pq.peek()[0] <= times[i][0]) {
                seats.offer(pq.poll()[1]);
            }
            end = seats.isEmpty() ? ++max : seats.poll();            
            pq.offer(new int[]{times[i][1], end});
            if (times[i][0] == start) {
                break;
            }
        }
        return end;
    }
}