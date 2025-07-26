/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    if(k==1) return 0;

    nums.sort((a,b) => a-b);
    let min = nums[nums.length-1];
    for(let i=0;i<=nums.length-k;i++){
        let diff =nums[i+k-1]-nums[i]
        min = Math.min(min,diff)
    }
    return min;
};