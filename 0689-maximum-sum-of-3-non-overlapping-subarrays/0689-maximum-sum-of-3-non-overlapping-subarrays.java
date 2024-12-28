class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        if(nums == null || nums.length < k * 3) return new int[]{};

        int numSub = nums.length - k + 1;
        //1. find sum of k len sub array start at index i
        int[] subSum = new int[numSub];
        int sum = 0;
        //initialize window
        for(int i=0; i<k; i++) sum += nums[i];
        subSum[0] = sum;
        //moving subarray window and calculate sum
        for(int i=k; i<nums.length; i++){
            sum -= nums[i-k];
            sum += nums[i];
            subSum[i-k+1] = sum;
        }

        //2. find the max sub at left 
        int[] maxAtLeft = new int[numSub];
        for(int i=1; i<numSub; i++){
            maxAtLeft[i] = (subSum[i] > subSum[maxAtLeft[i-1]])? i : maxAtLeft[i-1];
        }
        //3. find the max sub at right 
        int[] maxAtRight = new int[numSub];
        maxAtRight[numSub-1] = numSub-1;
        for(int i=numSub-2; i>=0; i--){
            maxAtRight[i] = (subSum[i] >= subSum[maxAtRight[i+1]])? i : maxAtRight[i+1];//equal to keep smallest index
        }
        //4.find the max 3 array such that i is the middle array
        int[] maxThree = new int[3];
        int maxSum = 0;
        for(int i=k; i<numSub-k; i++){
            int curSum = subSum[maxAtLeft[i-k]] + subSum[i] + subSum[maxAtRight[i+k]];
            if(curSum > maxSum){
                maxSum = curSum;
                maxThree = new int[]{maxAtLeft[i-k], i, maxAtRight[i+k]};
            }
        }
        return maxThree;
    }
}