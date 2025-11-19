class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(left,right):
            if left > right:
                return (0,0)
            pickLeft = dp(left+1,right)
            pickRight = dp(left,right-1)

            if piles[left]+pickLeft[1] > piles[right] + pickRight[1]:
                return piles[left] + pickLeft[1],pickLeft[0]
            return piles[right] + pickRight[1],pickRight[0]
        alex,lee = dp(0,len(piles)-1)
        return alex > lee
