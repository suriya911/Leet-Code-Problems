function zeroFilledSubarray(nums: number[]): number {
    let cnt = 0, streak = 0;
    for (let i=0;i<nums.length;i++) {
        if (nums[i] === 0) {
            streak++;
            cnt += streak;
        } else {
            streak = 0;
        }
    }
    return cnt;
}