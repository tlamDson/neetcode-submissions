from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
     
        @lru_cache(None)
        def dfs(remaining : int):
            if remaining == 0: 
                return 1
            combination = 0
            for i in range(n):
                if remaining - nums[i] < 0: break
                combination += dfs(remaining - nums[i])
            return combination
        
        return dfs(target)
                    
            
    