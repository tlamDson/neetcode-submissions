class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l,r = 0, len(matrix) - 1
        while l <= r :
            middle_matrix = (l + r) //2
            if matrix[middle_matrix][0] <= target <= matrix[middle_matrix][-1]:                
                left, right = 0,len(matrix[middle_matrix])-1
                while left <= right:
                    middle = (left + right) //2
                    if matrix[middle_matrix][middle] == target:
                        return True
                    elif matrix[middle_matrix][middle] > target:
                        right = middle -1
                    else : 
                        left = middle + 1
                return False     
            elif matrix[middle_matrix][0] > target:
                r = middle_matrix -1
            else : 
                l = middle_matrix + 1
        return False
