/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const window = new Set();

    for(var i=0;i<nums.length;i++){
        if (window.has(nums[i])){
            return true;
        }
        window.add(nums[i]);
        if(i>=k){
            window.delete(nums[i-k]);
        }
    }
    return false;
};