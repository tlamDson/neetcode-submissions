class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Bước 1: Chuyển vị ma trận (Transpose)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for r in range(len(matrix)):
            l = 0
            rr = len(matrix[0]) - 1
            while l < rr:
                matrix[r][l], matrix[r][rr] = matrix[r][rr], matrix[r][l]
                l +=1
                rr -=1
        
        