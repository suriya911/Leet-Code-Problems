class Solution {
    public int minAddToMakeValid(String s) {
        int open=0, close=0;
        for(char i : s.toCharArray()){
            if(i=='(') open++;
            else{ 
                if(open>0) open--;
                else close++;
            }
        }
        return open + close;
    }
}