class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = False
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                l, r = 0, len(matrix[i])
                while l <= r:
                    mid = (l + r) //2
                    if matrix[i][mid] == target:
                        result = True
                        break
                    elif matrix[i][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
        return result
            
                
        