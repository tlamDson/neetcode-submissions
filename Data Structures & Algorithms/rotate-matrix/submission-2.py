class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(i+1,cols):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for r in range(rows):
            l=0
            rr=cols-1
            while l<rr:
                matrix[r][l],matrix[r][rr]=matrix[r][rr],matrix[r][l]
                rr-=1
                l+=1

