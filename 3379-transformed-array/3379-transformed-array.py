class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        for index, value in enumerate(nums):
            if value > 0:
                res.append(nums[(index+value) % len(nums)])
            elif value < 0:
                res.append(nums[(index + len(nums) - (abs(value) % len(nums))) % len(nums)])
            else:
                res.append(0)
        return res