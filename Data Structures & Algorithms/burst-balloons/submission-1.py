from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.append(1)
        nums.insert(0,1)
        if not nums: return 0
        @lru_cache(None)
        def dfs(l,r):
            if l > r: return 0
            max_coins = 0
            for k in range(l, r + 1):
                coins = nums[l-1] * nums[k] * nums[r + 1]
                coins += dfs(l, k -1) + dfs( k + 1, r)
                max_coins = max(max_coins, coins)
            return max_coins
        return dfs(1, len(nums) - 2)
            

        