from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Bước 1: Khởi tạo mảng memo 2 chiều kích thước m x n toàn giá trị -1
        dp = [[1] * n for _ in range(m)]
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]
               