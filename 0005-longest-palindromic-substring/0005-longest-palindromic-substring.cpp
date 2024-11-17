class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        if (s.length() == 1) return s;

        string transformed = "#";
        for (char c : s) {
            transformed += c;
            transformed += "#";
        }

        int n = transformed.size();
        vector<int> P(n, 0); 
        int center = 0, right = 0;  
        int maxLen = 0, maxCenter = 0;  

        for (int i = 0; i < n; ++i) {
           
            int mirror = 2 * center - i;

            if (i < right) {
                P[i] = min(right - i, P[mirror]); 
            }

            while (i + P[i] + 1 < n && i - P[i] - 1 >= 0 && transformed[i + P[i] + 1] == transformed[i - P[i] - 1]) {
                P[i]++;
            }

            if (i + P[i] > right) {
                center = i;
                right = i + P[i];
            }

            if (P[i] > maxLen) {
                maxLen = P[i];
                maxCenter = i;
            }
        }
        int start = (maxCenter - maxLen) / 2;  
        return s.substr(start, maxLen);
    }
};