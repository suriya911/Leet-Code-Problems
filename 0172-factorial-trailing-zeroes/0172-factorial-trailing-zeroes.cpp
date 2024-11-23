class Solution {
public:
    int trailingZeroes(int n) {
        int r{0};

        for(int i=5;i<=n;i*=5){
            r = r + (n/i);
        }

        return r; 


    }
};