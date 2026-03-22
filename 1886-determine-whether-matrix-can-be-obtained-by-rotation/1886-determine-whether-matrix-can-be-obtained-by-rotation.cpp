class Solution {
public:
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        int a=mat.size();
        for(int n=0;n<4;n++){
            for(int i=0;i<a;i++){
                for(int j=i;j<a;j++){
                    swap(mat[i][j],mat[j][i]);
                }
            }
            for(int c=0;c<a;c++){
                for(int d=0;d<a/2;d++){
                    swap(mat[c][d],mat[c][a-d-1]);
                }
            }
            if(mat==target)return true;
        }
        return false;
    }
};