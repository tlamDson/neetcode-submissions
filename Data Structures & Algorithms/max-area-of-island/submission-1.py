class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # di thi dien het vao
        row , col = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(r,c):
            if ( r < 0 or r == row or c < 0 or c == col or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                area += dfs(nr,nc)
            return area
        maxIsland = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    ans = dfs(r,c)
                    maxIsland = max(maxIsland,ans)
        return maxIsland
        