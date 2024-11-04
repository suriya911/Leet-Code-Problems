class Solution {
    public String compressedString(String word) {
        StringBuilder res = new StringBuilder();
        int cnt = 1, n = word.length();
        char ch = word.charAt(0);
        for (int i = 1; i < n; i++) {
            if (word.charAt(i) == ch && cnt < 9) {
                cnt++;
            } else {
                res.append(cnt).append(ch);
                ch = word.charAt(i);
                cnt = 1;
            }
        }
        res.append(cnt).append(ch);
        return res.toString();
    }
}