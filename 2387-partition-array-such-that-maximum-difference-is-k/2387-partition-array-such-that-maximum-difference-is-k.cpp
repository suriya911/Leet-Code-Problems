class Solution {
public:
    int partitionArray(vector<int>& power, int k) {
        sort(begin(power), end(power));

        int range = -1;
        int section = 0;

        for(int i=0;i<power.size();i++){
            // if we exceed power range of current section
            if(power[i] > range){
                // create new section
                section++;
                range = power[i]+k;
            }
        }

        return section;
    }
};