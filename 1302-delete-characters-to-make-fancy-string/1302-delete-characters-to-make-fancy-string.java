class Solution {
    public String makeFancyString(String s) {
        StringBuilder sb = new StringBuilder();
        char pre = s.charAt(0);
        int cnt = 0;
        for(char cur : s.toCharArray()){
            if(cur == pre) cnt ++;
            else cnt = 1;

            if(cnt<3) sb.append(cur);
            pre = cur;

        }
        return sb.toString();
    }
}