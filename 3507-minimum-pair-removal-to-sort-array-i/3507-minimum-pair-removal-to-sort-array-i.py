class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        c=0
        i=0
        n=len(nums)
        while i<n-1:
            if(nums[i]>nums[i+1]):
                mini=math.inf
                index=0
                for j in range(n-1):
                    if(mini>(nums[j]+nums[j+1])):
                        mini=nums[j]+nums[j+1]
                        index=j
                nums[index]=mini
                nums.pop(index+1)
                c=c+1
                n=n-1
                i=0
            else:
                i=i+1
        return c


        