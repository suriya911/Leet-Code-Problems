class Solution {
public:
    bool hasSameDigits(string s) {
        int currentlength = s.length();
        while (currentlength > 2) {
            for (int i = 0; i < currentlength - 1; ++i) {
                int d1 = s[i] - '0';
                int d2 = s[i + 1] - '0';
                s[i] = ((d1 + d2) % 10) + '0';
            }
            currentlength--;
        }
        return s[0] == s[1];
    }
};