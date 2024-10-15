class Solution {
    public long minimumSteps(String s) {
        long ans = 0, c = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='1') c++;
            else ans+=c;
        }
        return ans;
    }
}