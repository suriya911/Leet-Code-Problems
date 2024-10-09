class Solution {
    public boolean isHappy(int n) {
        while(n > 6){
            n=square(n);
        }
        if(n==1) return true;
        else return false;
    }
    public int square(int n){
        int s=0;
        while(n>0){
            s += (n%10) * (n%10);
            n/=10;
        }
        return s;
    }
}