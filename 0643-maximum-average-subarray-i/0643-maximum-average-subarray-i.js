/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let sum =0
    for(let i=0;i<k;i++){
        sum += nums[i];
    }
    let max = sum
    for(let i=k;i<nums.length;i++){
        sum += nums[i] - nums[i-k]
        max = Math.max(max,sum)
    }
    return max/k;
};