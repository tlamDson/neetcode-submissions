class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        row, col = len(grid), len(grid[0])
        def dfs(r,c):
            if 0 <= r < row and 0 <= c < col:
                if grid[r][c] == "0": return 0
                if grid[r][c] == "1":
                    grid[r][c] = 0
                    dfs(r+ 1, c)
                    dfs(r, c + 1)
                    dfs(r-1,c)
                    dfs(r,c-1)
            
        res = 0
        for r in range(0,row):
            for c in range(0,col):
                if grid[r][c] == "1": 
                    res += 1
                    dfs(r,c)
        return res


       
            
                



        