class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        i = [0, 0, 0]
        for a in stones:
            i[a % 3] += 1

        if i[1] == 0 and i[2] == 0:
            return False  

        if i[0] % 2 == 0:
            return i[1] > 0 and i[2] > 0
        else:
            return abs(i[1] - i[2]) > 2

        