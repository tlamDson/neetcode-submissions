from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])

        o_set = set()
        q = deque()

        for r in range(row):
            for c in range(col):
                if r == 0 or (r == row-1) or c == 0 or (c == col -1):
                    if board[r][c] == 'O':  
                        q.append((r,c))
                        o_set.add((r,c))
        while q: 
            r, c = q.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == 'O' and (nr,nc) not in o_set:
                    q.append((nr,nc))
                    o_set.add((nr,nc))
        print(o_set)
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O' and (r,c) not in o_set:
                    board[r][c] = 'X'


        
