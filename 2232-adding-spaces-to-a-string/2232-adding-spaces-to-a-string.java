class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder res = new StringBuilder();
        int start = 0;
        for(int i : spaces){
            res.append(s,start,i).append(" ");
            start = i;
        }
        res.append(s.substring(start));
        return res.toString();
    }
}