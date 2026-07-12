class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix: return []
        row, col = len(matrix), len(matrix[0])
        visited = set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0 and (r,c) not in visited:
                    visited.add((r,c))
                    for allr in range(r, r + 1):
                        for allc in range(col):
                            if matrix[allr][allc] == 0 or (allr,allc) in visited:
                                continue
                            matrix[allr][allc] = 0
                            visited.add((allr,allc))
                    for allc in range(c, c + 1):
                        for allr in range(row):
                            if matrix[allr][allc] == 0 or (allr,allc) in visited:
                                continue
                            matrix[allr][allc] = 0
                            visited.add(((allr,allc)))

 
        