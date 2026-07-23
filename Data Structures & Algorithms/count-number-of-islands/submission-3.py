class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # runtime : r*c with r is row and c is col because every cell in the gird is visited
        # a constant number of time ( not infinite)

        # space : r* c because call stack base on the grid
        row, col = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r,c):
            grid[r][c] = '0'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':
                    dfs(nr,nc)
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r,c)
        return res
        

            
        