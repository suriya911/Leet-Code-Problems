public class Solution {
    public long minEnd(int n, int x) {
        ArrayList<Integer> shifts = new ArrayList<>();
        long cur = x;
        long calc = n - 1;
        
        for(int i = 0; i < 32; i++) {
            if((x & (1 << i)) == 0) {
                shifts.add(i);
            }
        }
        
        for(int i = 32; i < 64; i++) {
            shifts.add(i);
        }
        
        for(int i = 0; calc > 0; i++, calc >>= 1) {
            cur += (calc & 1L) << shifts.get(i);
        }
        
        return cur;
    }
}