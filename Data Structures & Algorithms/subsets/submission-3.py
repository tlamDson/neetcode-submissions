class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i,path):
            res.append(path.copy())
            for j in range(i,n):
                path.append(nums[j])
                backtrack(j + 1,path)
                path.pop()
        backtrack(0,[])
        return res
# path  = 1, 1,2 1,2,3

            
                    