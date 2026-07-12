class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
            
        ROWS, COLS = len(matrix), len(matrix[0])
        # Padded matrix with extra row and col of 0s
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Shift indices by +1 to account for the padding
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1 - 1][c2]
        left = self.sumMat[r2][c1 - 1]
        topLeft = self.sumMat[r1 - 1][c1 - 1]

        return bottomRight - above - left + topLeft