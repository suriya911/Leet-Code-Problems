class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> h = new HashMap<Character,Integer>();
        h.put('I',1);
        h.put('V',5);
        h.put('X',10);
        h.put('L',50);
        h.put('C',100);
        h.put('D',500);
        h.put('M',1000);
        int t=0;
        for(int i=0;i<s.length();i++){
            int c = h.get(s.charAt(i));
            if(i+1<s.length() && h.get(s.charAt(i+1))>c){
                t-=c;
            }else{
                t+=c;
            }
        }
        return t;
        
    }
}