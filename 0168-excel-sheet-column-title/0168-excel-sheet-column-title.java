class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder s= new StringBuilder();
        while(columnNumber > 0){
            columnNumber--;
            int r=columnNumber%26;
            char a = (char) (r+'A');
            s.append(a);
            columnNumber/=26;
        }
        return s.reverse().toString();
    }
}