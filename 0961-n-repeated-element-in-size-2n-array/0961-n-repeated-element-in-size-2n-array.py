class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s=len(nums)//2
        d=set(nums)
        for i in d:
            if nums.count(i)==s:
                return i
        return 0