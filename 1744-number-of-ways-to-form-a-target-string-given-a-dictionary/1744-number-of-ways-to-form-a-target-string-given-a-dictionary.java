class Solution {
    public int numWays(String[] words, String target) {
        final int MOD = 1000000007;
        int m = words[0].length(), n = target.length();

        Map<Character, Integer>[] freq = new Map[m];
        for (int i = 0; i < m; i++) {
            freq[i] = new HashMap<>();
        }
        for (String word : words) {
            for (int i = 0; i < m; i++) {
                freq[i].put(word.charAt(i), freq[i].getOrDefault(word.charAt(i), 0) + 1);
            }
        }

        int[] dp = new int[n + 1];
        dp[0] = 1;
        
        for (int i = 0; i < m; i++) {
            for (int j = n - 1; j >= 0; j--) { 
                if (freq[i].containsKey(target.charAt(j))) {
                    dp[j + 1] = (int)((dp[j + 1] + (long)dp[j] * freq[i].get(target.charAt(j))) % MOD); }
            }
        }

        return dp[n]; }
}