class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n <= 0) return false;
        int cnt = Integer.bitCount(n);
        return cnt==1;
    }
}