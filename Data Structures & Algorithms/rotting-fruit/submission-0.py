from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1
        row, col = len(grid), len(grid[0])

        q = deque()
        fresh_oranges = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1: 
                    fresh_oranges += 1
        if fresh_oranges == 0:
            return 0

        depth = 0
        while q and fresh_oranges > 0: 
            level_size = len(q)
            for _ in range((level_size)):
                r, c = q.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        q.append((nr,nc))
            depth += 1
        return depth if fresh_oranges == 0 else -1
        

        
            
        