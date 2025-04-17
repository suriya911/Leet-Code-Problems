class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        freq=[[] for i in range(101)]
        cnt=0
        for j, x in enumerate(nums):
            for i in freq[x]:
                cnt+=(i*j%k==0)
            freq[x].append(j)
        return cnt

        