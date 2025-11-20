class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        r=0
        n=len(nums)
        d=n//3
        for i in range(d,n,2):
            r+=nums[i]
        return r