class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        int i=0,j=0;
        int n1=str1.length(), n2=str2.length();
        while(i<n1 && j<n2) {
            if((str2[j]-str1[i]+26)%26 <= 1) {
                j++;
            }
            i++;
        }
        return j == n2;
    }
};