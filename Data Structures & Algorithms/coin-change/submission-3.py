from functools import lru_cache
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # base case :
        # if i == len(coins): return 0
        # special case if coins = 0 return 0
        # dfs(i, coin) 
        # dfs tai so dau tien neu ma het so dau tien thi quay lai va dfs i + 1
        # sau do quay lai va dfs i + 2
        # khong no se dfs tu 10 truoc
        # 10 xong 10 quay ve 5 xong 5 quay ve 1 xong 1 xong 1 thi la oke
        @lru_cache(None)
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            res = float("inf")
            for c in coins:
                res = min(res, 1 + dfs(rem - c))
            return res
        ans = dfs(amount)
        return ans if ans != float('inf') else -1

    
        