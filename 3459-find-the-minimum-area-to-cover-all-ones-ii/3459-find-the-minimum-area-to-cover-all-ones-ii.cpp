#define pii pair <int,int>
#define F first
#define S second

#define pii pair <int,int>
class Solution {

    pair<pii, pii> MinRectangle(pii x, pii y, vector <vector <int>>& grid) {
        int lft = x.S, rgt = y.S;
        int top = x.F, dwn = y.F;
        for (; lft <= rgt; lft ++) {
            int one = 0;
            for (int i = top; i <= dwn; i ++) 
            {
                if(grid[i][lft] == 1)
                {
                    one++;
                    break;    
                }
            }
            if (one > 0) break;
        }
        for (; rgt >= lft; rgt --) {
            int one = 0;
            for (int i = top; i <= dwn; i ++) 
            {
                if(grid[i][rgt] == 1)   
                {
                    one++;
                    break;
                }
            }
            if (one > 0) break;
        }
        
        for (; top <= dwn; top ++) {
            int one = 0;
            for (int i = lft; i <= rgt; i ++) 
            {
                if(grid[top][i] == 1)
                {
                    one++;
                    break;
                }
            }
            if (one > 0) break;
        }
        for (; dwn >= top; dwn --) {
            int one = 0;
            for (int i = lft; i <= rgt; i ++) 
            {
                if(grid[dwn][i] == 1)
                {
                    one++;
                    break;
                }
            }
            if (one > 0) break;
        }
        
        if (lft > rgt) return {{x.F, x.S}, {x.F, x.S}}; // rectangle with area 1
        return {{top, lft}, {dwn, rgt}};
    }

    int Area(pair <pii, pii> r)
    {
        return (r.S.F - r.F.F+1)*(r.S.S - r.F.S + 1);
    }

    int Min2Rectangle(pii x, pii y, vector <vector <int>>& grid)
    {
        int ans = Area({x, y});

        for(int col=x.S;col<y.S;col++)
        {
            auto lft = MinRectangle({x.F, x.S},{y.F, col}, grid);
            auto rgt = MinRectangle({x.F, col+1},{y.F, y.S}, grid);
            ans = min(ans, Area(lft)+Area(rgt));
        }
        
        for(int row=x.F;row<y.F;row++)
        {
            auto lft = MinRectangle({x.F, x.S}, {row, y.S}, grid);
            auto rgt = MinRectangle({row+1, x.S}, {y.F, y.S}, grid);
            ans = min(ans, Area(lft)+Area(rgt));
        }

        return ans;
    }

    int findMinRectangle3(pii x, pii y, vector <vector <int>>& grid)
    {
        int ans = Area({x,y});

        for(int col=x.S;col<y.S;col++)
        {
            auto lft1 = MinRectangle({x.F, x.S}, {y.F, col}, grid);
            auto rgt1 = Min2Rectangle({x.F , col+1}, {y.F , y.S}, grid);

            auto lft2 = Min2Rectangle({x.F, x.S}, {y.F, col}, grid);
            auto rgt2 = MinRectangle({x.F , col+1}, {y.F , y.S}, grid);

            ans = min(ans, Area(lft1)+rgt1);
            ans = min(ans, lft2+Area(rgt2));
        }

        for(int row=x.F;row<y.F;row++)
        {
            auto lft1 = MinRectangle({x.F, x.S},{row, y.S}, grid);
            auto rgt1 = Min2Rectangle({row+1, x.S},{y.F, y.S}, grid);

            auto lft2 = Min2Rectangle({x.F, x.S},{row, y.S}, grid);
            auto rgt2 = MinRectangle({row+1, x.S},{y.F, y.S}, grid);

            ans = min(ans, Area(lft1)+rgt1);
            ans = min(ans, lft2+Area(rgt2));
        }

        return ans;
    }

public:
    int minimumSum(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        return findMinRectangle3({0,0}, {n-1,m-1}, grid);
    }
};