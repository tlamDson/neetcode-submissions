class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        def backtrack(i, path, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return 
            for j in range(i, n):
                if curr_sum + nums[j] > target:
                    return 
                path.append(nums[j])
                backtrack(j , path, curr_sum + nums[j])
                path.pop()
        backtrack(0,[],0)
        return res
        
        