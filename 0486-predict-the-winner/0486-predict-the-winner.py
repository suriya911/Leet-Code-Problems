class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left,right):
            if left == right:
                return nums[left]
            return max(nums[left] - helper(left+1,right),nums[right]-helper(left,right-1))
        return helper(0,len(nums)-1) >=0