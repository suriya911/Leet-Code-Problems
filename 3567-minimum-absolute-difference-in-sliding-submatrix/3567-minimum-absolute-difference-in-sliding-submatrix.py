class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        n, m = len(grid), len(grid[0])
        res = [[0] * (m - k + 1) for _ in range(n - k + 1)]

        for i in range(n - k + 1):
            for j in range(m - k + 1):

                # Collect, sort and deduplicate all elements in this window
                elements = sorted(set(
                    grid[r][c]
                    for r in range(i, i + k)
                    for c in range(j, j + k)
                ))

                # Only 1 unique value → diff is 0
                if len(elements) <= 1:
                    res[i][j] = 0
                else:
                    res[i][j] = min(elements[x+1] - elements[x] for x in range(len(elements)-1))

        return res