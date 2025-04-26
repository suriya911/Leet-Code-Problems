/**
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function(nums, minK, maxK) {
    let total = 0, lastInvalid = -1, lastMin = -1, lastMax = -1;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < minK || nums[i] > maxK) lastInvalid = i;
        if (nums[i] === minK) lastMin = i;
        if (nums[i] === maxK) lastMax = i;

        let validStart = Math.min(lastMin, lastMax);
        total += Math.max(0, validStart - lastInvalid);
    }

    return total;
};