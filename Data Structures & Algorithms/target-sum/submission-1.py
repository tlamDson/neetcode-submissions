from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def dfs(path, total):
            if path == len(nums):
                if total == target: 
                    return 1
                else: 
                    return 0
            return dfs(path + 1, total + nums[path]) + dfs(path + 1, total - nums[path])

        return dfs(0,0)


            
            

                

        