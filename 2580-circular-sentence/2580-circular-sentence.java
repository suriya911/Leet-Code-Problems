class Solution {
    public boolean isCircularSentence(String sentence) {
        String list[] = sentence.split(" ");
        for(int i=0;i<list.length;i++){
            int l = list[i].length();
            if(i==list.length-1){
                if(list[i].charAt(l-1)==list[0].charAt(0)) continue;
                else return false;
            }else{
                if(list[i].charAt(l-1)==list[i+1].charAt(0)) continue;
                else return false;
            }
        }
        return true;
    }
}