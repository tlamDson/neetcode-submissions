class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i,path):
            res.append(path.copy())
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1,path)
                path.pop()
        dfs(0,[])
        return res
            
            