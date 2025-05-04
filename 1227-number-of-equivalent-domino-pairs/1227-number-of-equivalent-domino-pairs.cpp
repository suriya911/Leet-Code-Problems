class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        int freq[100]={0},count=0;
        for(auto& d: dominoes){
            int d0=d[0],d1=d[1], x=(d0<d1)? 10*d0+d1 : 10*d1+d0;
            count+=freq[x];
            freq[x]++;
        }
        return count;
    }
};