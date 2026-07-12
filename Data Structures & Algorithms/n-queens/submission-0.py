class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 1. Khai báo các bộ chứa (Sets) để kiểm tra va chạm trong O(1)
        cols = set()      # Lưu các cột đã có quân hậu
        posDiag = set()   # Lưu (r + c) cho đường chéo phụ
        negDiag = set()   # Lưu (r - c) cho đường chéo chính
        
        res = []          # Kết quả cuối cùng
        board = [["."] * n for _ in range(n)] # Bàn cờ ban đầu

        def backtrack(r):
            # 2. Điều kiện dừng: Nếu r == n, nghĩa là đã đặt xong N quân hậu
            if r == n:
                copy_board = []
                for row in board:
                    row_string = "".join(row)
                    copy_board.append(row_string)
                res.append(copy_board)
                # Chuyển đổi board thành định dạng đề bài yêu cầu và lưu vào res
                return

            # 3. Vòng lặp: Thử đặt quân hậu vào từng cột c của hàng r
            for c in range(n):
                # 4. Kiểm tra va chạm: Nếu c, (r+c), hoặc (r-c) đã có trong sets -> Bỏ qua
                if (c in cols) or ((r + c) in posDiag) or ((r - c) in negDiag):
                    continue
                # 5. ĐẶT QUÂN HẬU (Bước tiến)
                # Thêm c, (r+c), (r-c) vào các sets tương ứng
                # Cập nhật board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r +c)
                negDiag.add(r-c)
                board[r][c] = 'Q'
                # 6. ĐỆ QUY (Đi sâu vào hàng tiếp theo)
                backtrack(r + 1)
                
                # 7. QUAY LUI (Bước lùi - BẮT BUỘC)
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r -c)
                board[r][c] = '.'
                # Gỡ bỏ c, (r+c), (r-c) khỏi các sets
                # Đặt lại board[r][c] = "."
        
        backtrack(0) # Bắt đầu từ hàng 0
        return res