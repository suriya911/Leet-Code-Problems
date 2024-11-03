class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        int right = 0;
        int [] vocab = new int[128];
        for (int left = 0 ; left < s.length() ; left++) {
            char ch = s.charAt(left);
            right = Math.max(vocab[ch], right);
            res = Math.max(res, left - right + 1);
            vocab[ch] = left + 1;
        }
        return res;
    }
}