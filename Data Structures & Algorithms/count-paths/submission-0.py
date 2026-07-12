from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Bước 1: Khởi tạo mảng memo 2 chiều kích thước m x n toàn giá trị -1
        memo = [[-1] * n for _ in range(m)]
        
        @lru_cache(None)
        # Bước 2: Định nghĩa hàm DFS
        def dfs(r, c):
            # 2.1: Kiểm tra xem có bị out khỏi lưới không? (r >= m hoặc c >= n)
            # Nếu có, return 0
            if r >=m or c >=n: return 0
            
            # 2.2: Kiểm tra xem đã đến đích chưa? (r == m-1 và c == n-1)
            # Nếu có, return 1
            if r == m-1 and c == n-1: return 1
            
            # 2.3: Kiểm tra xem ô (r, c) này đã được tính toán và lưu vào memo chưa?
            # Nếu memo[r][c] != -1, return memo[r][c]

            # 2.4: Nếu chưa có trong memo, tính toán bằng cách đi tiếp sang phải và đi xuống
            # memo[r][c] = dfs(...) + dfs(...)
            ways_left = dfs(r,c+1)
            ways_right = dfs(r+1,c)
            memo[r][c] = ways_left + ways_right
            
            # 2.5: Trả về kết quả của ô hiện tại
            return memo[r][c]
            
        # Bước 3: Bắt đầu chạy DFS từ ô (0, 0)
        return dfs(0, 0)