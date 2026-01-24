class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = nums.sort()
        i = 0
        j = len(nums) - 1
        result = 0

        while i<j :
            sum = nums[i] + nums[j]
            result = max(result, sum)
            i += 1
            j -= 1
        return result