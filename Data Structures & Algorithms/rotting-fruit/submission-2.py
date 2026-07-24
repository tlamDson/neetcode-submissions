from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # the time complexity can be o(m*n) because each cell is visited in a limited number of time
        # space complexity is o(m*n) at the worst case
        row, col = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        q = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c,0))
        ans = 0
        while q:
            r, c, time = q.popleft()
            ans = time
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr,nc,time + 1))  
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1
        return ans


        
        