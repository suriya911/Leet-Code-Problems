class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend == Integer.MIN_VALUE && divisor == -1){
            return Integer.MAX_VALUE;
        }
        int sign = (dividend > 0) == (divisor > 0)? 1:-1;

        long a = Math.abs((long) dividend);
        long b = Math.abs((long) divisor);

        long q = 0;

        while(a >= b){
            long temp = b;
            long multiply = 1;
            while(a >= (temp << 1)){
                temp <<= 1;
                multiply <<= 1; 
            }
            a -= temp;
            q += multiply;
        }

        return (int) (sign * q);
    }
}