class Solution {
public:
    vector<vector<int>> ids;
    int n;

    int dfs(int r, int c, int id, vector<vector<int>>& grid) {

        if(r < 0 || r >= n || c < 0 || c >= n || !grid[r][c] || ids[r][c])   
            return 0;

        ids[r][c] = id;

        return 1 + dfs(r + 1, c, id, grid) + dfs(r - 1, c, id, grid) + 
                   dfs(r, c + 1, id, grid) +  dfs(r, c - 1, id, grid);
    }

    int largestIsland(vector<vector<int>>& grid) {
        n = grid.size();
        ids.assign(n, vector<int>(n));

        unordered_map<int, int> sizes;
        int largest = 0, id = 2;

        for(int r = 0; r < n; ++r) {
            for(int c = 0; c < n; ++c) {

                if(grid[r][c] && !ids[r][c]) {
                    int size = dfs(r, c, id, grid);

                    sizes[id++] = size;
                    largest = max(largest, size);
                }
            }
        }
        
        for(int r = 0; r < n; ++r) {
            for(int c = 0;c < n; ++c) {

                if(!ids[r][c]) {
                    unordered_set<int> neighbors;

                    if(r > 0)
                        neighbors.insert(ids[r - 1][c]);

                    if(r < n - 1)  
                        neighbors.insert(ids[r + 1][c]);

                    if(c > 0)
                        neighbors.insert(ids[r][c - 1]);

                    if(c < n - 1)
                        neighbors.insert(ids[r][c + 1]);

                    int new_size = 1;

                    for(const auto& nei : neighbors)   
                        if(nei != 0)
                            new_size += sizes[nei];

                    largest = max(largest, new_size);
                }   
            }
        }

        return largest;
    }
};