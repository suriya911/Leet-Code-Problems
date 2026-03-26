class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])

        sumGrid = [[0] * n for _ in range(m)]

        # first row
        pref_sum = 0
        for j in range(n):
            pref_sum += grid[0][j]
            sumGrid[0][j] = pref_sum

        for i in range(1, m):
            pref_sum = 0
            for j in range(n):
                pref_sum += grid[i][j]
                sumGrid[i][j] = pref_sum + sumGrid[i - 1][j]

        total_sum = sumGrid[m - 1][n - 1]

        # column cuts
        for j in range(n - 1):
            if sumGrid[m - 1][j] == total_sum - sumGrid[m - 1][j]:
                return True

        # row cuts
        for i in range(m - 1):
            if sumGrid[i][n - 1] == total_sum - sumGrid[i][n - 1]:
                return True

        return False