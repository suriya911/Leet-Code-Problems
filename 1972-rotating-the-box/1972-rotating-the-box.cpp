class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m = box.size();
        int n = box.front().size();        
        vector<vector<char>> out(n, vector<char>(m, '.'));

        for (int j = 0; j < m; j++) {
            int fall_to = n-1;
            for (int i = n-1; i >= 0; i--) {
                char cell = box[m-1-j][i];
                if (cell == '*') {
                    out[i][j] = '*';
                    fall_to = i-1;
                }
                else if (cell == '#') {
                    out[fall_to][j] = '#';
                    fall_to--;
                }
            }
        }

        return out;
    }
};