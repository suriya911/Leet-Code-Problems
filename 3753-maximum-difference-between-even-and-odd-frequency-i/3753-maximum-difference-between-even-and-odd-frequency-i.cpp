class Solution {
public:
    int maxDifference(string s) {
        unordered_map<char, int> m;
        int mina = INT_MAX;
        int maxa = INT_MIN;

        for (char ch : s) {
            m[ch]++;
        }

        for (auto i : m) {
            if (i.second % 2) {
                maxa = max(maxa, i.second);
            } else {
                mina = min(mina, i.second);
            }
        }

        return maxa - mina;
    }
};