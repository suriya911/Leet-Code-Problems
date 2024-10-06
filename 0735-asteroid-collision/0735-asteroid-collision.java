class Solution {
    public int[] asteroidCollision(int[] a) {
        int n = a.length;
        int s = 0;
        int[] ans = new int[n];

        for(int j=0;j<n;j++){
            int cur=a[j];
            if(cur>0) ans[s++]=cur;
            
            else{
                while(s>0 && ans[s-1]>0){
                    if(ans[s-1] < -cur) s--;
                    else if(ans[s-1]==-cur){
                        s--;
                        cur=0;
                        break;
                    }
                    else{
                        cur=0;
                        break;
                    }
                }
                if(cur!=0){
                    ans[s++]=cur;
                }
            }
        }
        return Arrays.copyOf(ans,s);
    }
}