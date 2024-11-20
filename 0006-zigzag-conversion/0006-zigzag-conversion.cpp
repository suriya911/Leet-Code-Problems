class Solution {
public:
    string convert(string s, int numRows) {
        int n = s.length();

        if (n <= numRows || numRows==1) return s;

        string res = "";
        int magic = numRows + numRows-2;
        pair<int,int> currMagic = {magic,magic};

        for(int i = 0;i<numRows;i++) {
            int id = i;
            bool tog = 1;

            while(id<n) {
                res += s[id];
                id += tog ? currMagic.first : currMagic.second; 
                tog=!tog;
            }

            currMagic.first = currMagic.first == 2 ? magic : currMagic.first-2;
            currMagic.second = currMagic.first == magic ? magic : magic - currMagic.first;

        }

        return res;
    }
};