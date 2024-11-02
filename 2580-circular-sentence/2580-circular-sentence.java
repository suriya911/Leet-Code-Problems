class Solution {
    public boolean isCircularSentence(String sentence) {
        if(sentence.charAt(0) != sentence.charAt(sentence.length()-1)) 
            return false;
        int n = sentence.indexOf(" ");
        if(n == -1) return true;
        while(n != -1){
            if(sentence.charAt(n-1) != sentence.charAt(n+1)) return false;
            n = sentence.indexOf(" ",n+1);
        }
    return true;
    }
}