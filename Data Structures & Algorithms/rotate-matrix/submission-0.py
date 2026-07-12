class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Bước 1: Chuyển vị ma trận (Transpose)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Bước 2: Đảo ngược từng hàng (Reverse rows)
        for i in range(n):
            matrix[i].reverse()
        
        