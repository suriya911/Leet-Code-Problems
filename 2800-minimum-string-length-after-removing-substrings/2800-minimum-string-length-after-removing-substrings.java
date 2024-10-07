class Solution {
    public int minLength(String s) {
        Stack<Character> list = new Stack<>();

        for(int i=0;i<s.length();i++){
            char curr = s.charAt(i);
            if(list.isEmpty()){
                list.push(curr);
                continue;
            }
            if((curr == 'B' && list.peek() == 'A')||(curr == 'D' && list.peek() == 'C')){
                list.pop();
            }
            else{
                list.push(curr);
            }
        }
        return list.size();
        
    }
}