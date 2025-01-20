class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = sum(nums[:3])
        if len(nums) <= 3:
            return ans
        for l in range(n-2):
            # prune search
            low,high = nums[l]+nums[l+1]+nums[l+2],nums[l]+nums[-2]+nums[-1]
            ans = min(ans,low,high,key=lambda v:abs(v-target))
            if target < low or target > high:
                continue
            # 2pointer
            m,r = l+1,n-1
            while m<r:
                summ = nums[l]+nums[m]+nums[r]
                if abs(target-summ) < abs(target-ans):
                    ans = summ
                if summ < target:
                    m+=1
                elif summ > target:
                    r-=1
                else: # exact solution
                    return ans
        return ans
            
        