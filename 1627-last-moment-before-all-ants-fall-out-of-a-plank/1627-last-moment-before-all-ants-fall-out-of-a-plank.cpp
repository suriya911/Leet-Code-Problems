class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int time = 0;
        for( int pos: left){
            time = max(time,pos);
        }
        for(int pos : right){
            time = max(time,n-pos);
        }

        return time;
    }
};
