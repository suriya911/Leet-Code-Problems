class Solution:
    def maxWalls(self, robots: list[int], distance: list[int], walls: list[int]) -> int:
        n = len(robots)
        r = sorted(zip(robots, distance))
        rs = set(robots)
        
        bw = 0
        vw = []
        for w in walls:
            if w in rs:
                bw += 1
            else:
                vw.append(w)
        vw.sort()
        
        def get_w(x, y):
            if x > y:
                return 0
            i1 = bisect.bisect_left(vw, x)
            i2 = bisect.bisect_right(vw, y)
            return i2 - i1
        
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = get_w(r[0][0] - r[0][1], r[0][0] - 1)
        dp[0][1] = 0
        
        for i in range(1, n):
            L, d1 = r[i-1]
            R, d2 = r[i]
            
            eR = min(R - 1, L + d1)
            sL = max(L + 1, R - d2)
            
            wR = get_w(L + 1, eR)
            wL = get_w(sL, R - 1)
            wBoth = get_w(L + 1, R - 1) if eR >= sL else wR + wL
            
            dp[i][0] = max(dp[i-1][0] + wL, dp[i-1][1] + wBoth)
            dp[i][1] = max(dp[i-1][0], dp[i-1][1] + wR)
            
        wEnd = get_w(r[-1][0] + 1, r[-1][0] + r[-1][1])
        ans = max(dp[-1][0], dp[-1][1] + wEnd)
        
        return ans + bw