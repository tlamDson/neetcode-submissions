class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        q = deque()

        for r in range(row):
            for c in range(col):
                if r == 0 or (r == row-1) or c == 0 or (c == col -1):
                    if board[r][c] == 'O':  
                        q.append((r,c))
                        board[r][c] = 'T'
        while q: 
            r, c = q.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == 'O':
                    q.append((nr,nc))
                    board[nr][nc] = 'T'
        print(board)
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'


        
