class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        isVisited = [False]*len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return 
            for j in range(len(nums)):
                if isVisited[j]: continue
                if j > 0 and nums[j] == nums[j-1] and not isVisited[j-1] : continue
                path.append(nums[j])
                isVisited[j] = True
                backtrack(path)
                path.pop()
                isVisited[j] = False
        backtrack([])
        return res
#path = [1,1,2]
#isVisited = [T,T,F]

        