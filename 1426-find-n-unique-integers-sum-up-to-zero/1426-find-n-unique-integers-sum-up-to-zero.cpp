class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> a;
        if (n % 2 != 0) {
            a.push_back(0);
        }

        for (int i = 1; i <= n/2; i++) {
            a.push_back(i);
            a.push_back(-i);
        }
        return a;
    }
};