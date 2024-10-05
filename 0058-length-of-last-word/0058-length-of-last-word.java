class Solution {
    public int lengthOfLastWord(String s) {
        String j[] = s.split(" ");
        return j[j.length-1].length();
    }
}