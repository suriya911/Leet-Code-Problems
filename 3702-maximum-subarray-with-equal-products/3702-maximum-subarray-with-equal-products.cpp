class Solution {
public:
    int gcd(int a,int b){
        while(b){
            a%=b;
            swap(a,b);
        }    
        return a;
    }
    int lcm(int a,int b){
        return a/gcd(a,b) * b;
    }
    int maxLength(vector<int>& nums) {
        int n=nums.size(), maxi=0;
        for(int i=0;i<n;i++){
            int pro=nums[i],l=nums[i],g=nums[i];
            for(int j=i+1;j<n;j++){
                pro *=nums[j];
                g=gcd(g,nums[j]);
                l=lcm(l,nums[j]);
                if(pro == g*l){
                    maxi = max(maxi,j-i+1);
                }
                else break;
            }
        }
        return maxi;

    }
};