class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [(i >> 1) ^ i for i in range(1 << n)]
        