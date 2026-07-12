from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return False
        if sum(nums) % 2 == 1: return False

        nums.sort(reverse = True)
        n = len(nums)
        target = sum(nums) // 2

        @lru_cache(None)
        def dfs(i, current_sum):
            if current_sum == target: return True
            if current_sum > target or i >=n : return False
            if dfs(i+1, current_sum + nums[i]) : return True
            if dfs(i+1, current_sum) : return True
            return False
        return dfs(0,0)

        


        




