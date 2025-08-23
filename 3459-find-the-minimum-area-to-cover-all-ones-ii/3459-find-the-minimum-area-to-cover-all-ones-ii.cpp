class Solution {
public:
     int minimumArea(vector<vector<int>>& grid,int startR, int endR, int startC , int endC) {
        int minR = 1e9;
        int maxR = -1e9;
        int minC = 1e9;
        int maxC = -1e9;
        bool lock = true;
        for(int i=startR;i<=endR;++i)
        {
            for(int k=startC;k<=endC;++k)
            {
                if( grid[i][k] == 1 )
                {
                    lock = false;
                    minR = min(minR, i);
                    maxR = max(maxR, i);
                    minC = min(minC, k);
                    maxC = max(maxC, k);
                }
            }
        }
        if(lock)
        {
            return 1e9;
        }
        return (maxR-minR+1)*(maxC-minC+1);
    }
    
    
    int splitRec(vector<vector<int>> &grid,int startR, int endR, int startC , int endC, int splitNum)
    {
        
        if( splitNum == 0 ) // split done(no chance), using Leet 3195 to find the optimal solution
        {
            int val = minimumArea(grid,startR, endR, startC, endC);
            return val;
        }
        
        int now = 1e9;
        // rowCut
        for(int i=startR;i<endR;++i)
        {
            now = min( {now,
                        splitRec(grid,startR, i, startC, endC, 0) + splitRec(grid,i+1, endR, startC, endC, splitNum-1),
                       splitRec(grid,startR, i, startC, endC, splitNum-1) + splitRec(grid,i+1, endR, startC, endC, 0)});
        }
        //colCut
        for(int k=startC;k<endC;++k)
        {
            now = min( {now,
                        splitRec(grid,startR, endR, startC, k, 0) + splitRec(grid,startR, endR, k+1, endC, splitNum-1),
                       splitRec(grid,startR, endR, startC, k, splitNum-1) + splitRec(grid,startR, endR, k+1, endC, 0)});
        }
        return now;
    }
    
    int minimumSum(vector<vector<int>>& grid) {
        
        int n = grid.size();
        int m = grid[0].size();

        //first we have [0,0] ~ [n-1,m-1] rectangle  (inclusive)
        // and we have 2 chances to split
        int ans = splitRec(grid, 0, n-1, 0, m-1, 2);
        return ans;
    }
};