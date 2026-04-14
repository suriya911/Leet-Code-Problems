class Solution {
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        Collections.sort(robot);
        Arrays.sort(factory, (a, b) -> a[0] - b[0]);

        int r = robot.size();
        int f = factory.length;
        long[][] dp = new long[r + 1][f + 1];

        for (int i = 0; i <= r; i++) {
            Arrays.fill(dp[i], Long.MAX_VALUE / 2);
        }

        for (int j = 0; j <= f; j++) {
            dp[0][j] = 0;
        }

        for (int j = 1; j <= f; j++) {
            int pos = factory[j-1][0], limit = factory[j-1][1];

            for (int i = 0; i <= r; i++) {
                dp[i][j] = dp[i][j-1];

                long dist = 0;
                for (int k = 1; k <= limit && i - k >= 0; k++) {
                    dist += Math.abs(robot.get(i - k) - pos);
                    dp[i][j] = Math.min(dp[i][j], dp[i - k][j - 1] + dist);
                }
            }
        }

        return dp[r][f];
    }
}