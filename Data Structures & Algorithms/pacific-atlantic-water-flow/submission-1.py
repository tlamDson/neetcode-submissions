from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        row, col = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        q_pacific = deque()
        q_atlantic = deque()

        res = []

        for r in range(row):
            for c in range(col):
                if r == 0 or c == 0:
                    q_pacific.append((r,c))
                    pacific.add((r,c))
                if ( r == row - 1) or (c == col -1):
                    q_atlantic.append((r,c))
                    atlantic.add((r,c))
        while q_pacific: 
            r,c = q_pacific.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and heights[nr][nc] >= heights[r][c] and (nr,nc) not in pacific:
                    q_pacific.append((nr,nc))
                    pacific.add((nr,nc))
        while q_atlantic: 
            r,c = q_atlantic.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and heights[nr][nc] >= heights[r][c] and (nr,nc) not in atlantic:
                    q_atlantic.append((nr,nc))
                    atlantic.add((nr,nc))
        for r, c in pacific:
            if (r,c) in atlantic:
                    res.append([r,c])
        return res


        