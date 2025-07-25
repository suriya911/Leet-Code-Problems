/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function(nums) {
    if(nums.every((x) => x < 0))return Math.max(...nums)

    const mySet = new Set(nums)
    const arr = Array.from(mySet.values()).filter((x) => x > 0)
    return arr.reduce((total, item)=> total + item, 0)
};