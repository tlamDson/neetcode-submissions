class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        r_set = set()
        c_set = set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    r_set.add(r)
                    c_set.add(c)
        for r in range(row):
            for c in range(col):
                if r in r_set:
                    matrix[r][c] = 0
                if c in c_set:
                    matrix[r][c] = 0
        
        