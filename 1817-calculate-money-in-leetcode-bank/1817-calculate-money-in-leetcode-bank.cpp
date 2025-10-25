class Solution {
public:
    int totalMoney(int n) {
        int w = n/7;
        int d=n%7;
        return (w*(49+7*w) +d*(2*w+d+1))/2;
    }
};