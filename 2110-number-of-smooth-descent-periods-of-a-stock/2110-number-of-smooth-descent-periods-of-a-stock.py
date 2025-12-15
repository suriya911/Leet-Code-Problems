class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        tally, ans = 1, 0

        for p1, p2 in pairwise(prices):
            if p2 == p1 - 1:
                tally+= 1
            else:
                ans+= tally * (tally + 1)
                tally = 1
        ans+= tally * (tally + 1)

        return  ans//2
        