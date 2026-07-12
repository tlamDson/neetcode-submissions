from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        
        @lru_cache(None)
        def dfs(i):
            # Nếu từ i có thể nhảy tới hoặc quá đích
            if i + nums[i] >= n - 1:
                return 1
            
            # Nếu bị kẹt tại 0 và chưa tới đích
            if nums[i] == 0: 
                return float("inf")
            
            min_jumps = float("inf")
            # Thử mọi khả năng nhảy
            for j in range(i + 1, i + nums[i] + 1):
                res = dfs(j)
                if res != float("inf"):
                    min_jumps = min(min_jumps, 1 + res)
            return min_jumps
        
        return dfs(0)