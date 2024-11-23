class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        if(points.size() == 1) return 1;
        int ans = 0;

        for(int i=0; i<points.size();++i){
            unordered_map <double, int> mapping;
            for(int j=0; j<points.size();++j){
                if(j==i) continue;

                auto dy = points[j][1] - points[i][1];
                auto dx = points[j][0] - points[i][0];

                auto theta = atan2(dy,dx);

                mapping[theta]++;
            }
            for(auto &it : mapping){
                ans = max(ans, it.second + 1);
            }
        }
        return ans;
    }
};