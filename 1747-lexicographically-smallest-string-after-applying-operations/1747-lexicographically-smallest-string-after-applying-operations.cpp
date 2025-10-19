class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        int stringLength = s.size();
        string smallestLexString = s; 
        for (int i = 0; i < stringLength; ++i) {
            s = s.substr(stringLength - b) + s.substr(0, stringLength - b);
            for (int j = 0; j < 10; ++j) {
                for (int k = 1; k < stringLength; k += 2) {
                    s[k] = ((s[k] - '0' + a) % 10) + '0';
                }
                if (b % 2 == 1) {
                    for (int p = 0; p < 10; ++p) {
                        for (int k = 0; k < stringLength; k += 2) {
                            s[k] = ((s[k] - '0' + a) % 10) + '0';
                        }
                        smallestLexString = min(smallestLexString, s);
                    }
                } else {
                    smallestLexString = min(smallestLexString, s);
                }
            }
        }
        return smallestLexString;
    }
};