class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        @cache
        def dp(i,j,x,d,k):
            if not (0<=i<n and 0<=j<m):
                return 0 # when i or j> no of rows or coloumns
            if grid[i][j]!=x:
                return 0
            r=dp(i+ds[d][0],j+ds[d][1],nx[x],d,k)+1
            if k>0:
                d2=(d+1)%4
                r2=dp(i+ds[d2][0],j+ds[d2][1],nx[x],d2,0)+1
                r=max(r,r2)
            return r
        ds=[[1,1],[1,-1],[-1,-1],[-1,1]]
        nx=[2,2,0]
        r=0
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    c=max(dp(i,j,1,d,1) for d in range(4))
                    r=max(r,c)
        return r

    