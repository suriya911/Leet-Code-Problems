class Solution {
public:
    string convert(string s, int numRows) {
        int n = s.length();
        int m = 2 * numRows - 2;
        string output = "";

        if (numRows == 1)
            return s;
        
        // First row
        for (int i = 0; i < n; i += m) 
            output.push_back(s[i]);

        // Mid rows
        int j, k;
        for (int i = 1; i < numRows - 1; i++) {
            for (j = i, k = m - i; j < n && k < n; j += m, k += m) {
                output.push_back(s[j]);
                output.push_back(s[k]);
            }
            if (j < n)
                output.push_back(s[j]);
            if (k < n)
                output.push_back(s[k]);
        }

        // Last row
        for (int i = numRows - 1; i < n; i += m) 
            output.push_back(s[i]);

        return output;
    }
};