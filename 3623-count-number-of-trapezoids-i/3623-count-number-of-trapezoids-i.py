class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        groups = defaultdict(int)
        for _, y in points:
            groups[y] += 1
        res = total = 0
        for y, count in groups.items():
            lines = count * (count - 1) // 2
            res = (res + total * lines) % MOD
            total = (total + lines) % MOD
        return res