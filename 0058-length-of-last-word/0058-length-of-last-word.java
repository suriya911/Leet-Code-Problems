class Solution {
    public int lengthOfLastWord(String s) {
        int l = 0;
        boolean count = false;

        for (char c : s.toCharArray()) {
            if (c != ' ') {
                if (!count) {
                    count = true;
                    l = 1;
                } else {
                    l++;
                }
            } else {
                count = false;
            }
        }

        return l;        
    }
}