from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        
        # dung bfs
        # neu ma khac inf thi continue
        # neu ma qua boundarie thi continue
        # gap 0 thi bfs 
        # how to track the distance, dung depth
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        q = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))     
        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 2147483647:
                    q.append((nr,nc))
                    grid[nr][nc] = 1 + grid[r][c]


        