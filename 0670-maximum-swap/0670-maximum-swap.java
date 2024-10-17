class Solution {
    public int maximumSwap(int num) {
        char[] numArr = Integer.toString(num).toCharArray();
        int n = numArr.length;

        int[] list = new int[10];

        for(int i=0;i<n;i++){
            list[numArr[i]-'0']=i;
        }

        for(int i=0;i<n;i++){
            for(int d=9; d>numArr[i]-'0';d--){
                if(list[d] > i){
                    char temp = numArr[i];
                    numArr[i]=numArr[list[d]];
                    numArr[list[d]]=temp;
                    return Integer.parseInt(new String(numArr));
                }
            }
        }
        return num;
    }
}