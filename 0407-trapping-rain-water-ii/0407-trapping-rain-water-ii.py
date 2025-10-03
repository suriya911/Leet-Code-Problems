import heapq

class Solution(object):
    def trapRainWater(self, h):
        """
        :type h: List[List[int]]
        :rtype: int
        """
        # Edge cases: empty or too small
        if not h or not h[0]: return 0
        m, n = len(h), len(h[0])
        if m < 3 or n < 3: return 0
        
        # Initialize priority queue with boundary cells
        q = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heapq.heappush(q, (h[i][j], i, j))
                    h[i][j] = -1  # Mark as visited
        
        l, r = 0, 0  # l = water level, r = total trapped water
        
        # Process cells from lowest to highest
        while q:
            v, x, y = heapq.heappop(q)
            l = max(l, v)  # Update water level
            
            # Check all 4 neighbors
            for a, b in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if 0 <= a < m and 0 <= b < n and h[a][b] != -1:
                    heapq.heappush(q, (h[a][b], a, b))
                    if h[a][b] < l:
                        r += l - h[a][b]  # Trap water!
                    h[a][b] = -1  # Mark as visited
        
        return r