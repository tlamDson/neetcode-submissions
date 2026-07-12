
from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(i):
            max_len = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_len = max(max_len, 1 + dfs(j))
            return max_len
        return max(dfs(i) for i in range(len(nums)))


