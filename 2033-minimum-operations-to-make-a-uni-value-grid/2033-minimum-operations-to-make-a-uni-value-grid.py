class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        y = x
        x = []
        for i in grid:
            x += i
        rem = x[0] % y
        for num in x:
            if num % y != rem:
                return -1  
        x.sort()
        ans = 0
        mid = x[len(x) // 2]  
        
        for i in x:
            ans += abs(i - mid) // y
        
        return ans