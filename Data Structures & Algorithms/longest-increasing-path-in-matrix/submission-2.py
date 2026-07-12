import sys
from functools import lru_cache
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Nâng giới hạn đệ quy lên 100,000 (đủ cho ma trận tối đa của LeetCode)
        sys.setrecursionlimit(100000)
        
        if not matrix or not matrix[0]: return 0
        row, col = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(i, j):
            max_len = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < row and 0 <= nj < col:
                    if matrix[ni][nj] > matrix[i][j]:
                        max_len = max(max_len, 1 + dfs(ni, nj))
            return max_len
            
        res = 0
        for r in range(row):
            for c in range(col):
                res = max(res, dfs(r, c))
                
        return res