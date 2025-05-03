class Solution {
public:
    static int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        const int n=tops.size(), m=bottoms.size();
        if (n!=m) return -1;// edge case
        int T[7]={0}, B[7]={0}, S[7]={0};
        for(int i=0; i<n; i++){
            T[tops[i]]++;
            B[bottoms[i]]++;
            S[tops[i]]+=(tops[i]==bottoms[i]);
        }
        int ans=INT_MAX;
        for(int x=1; x<=6; x++){
            if (T[x]+B[x]-S[x]==n)
                ans=min(ans, min(n-T[x], n-B[x]));
        }
        return ans==INT_MAX?-1:ans;
    }
};