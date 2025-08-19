function zeroFilledSubarray(nums: number[]): number {
    let cnt = 0, streak = 0;
    for (let num of nums) {
        if (num === 0) {
            streak++;
            cnt += streak;
        } else {
            streak = 0;
        }
    }
    return cnt;
}