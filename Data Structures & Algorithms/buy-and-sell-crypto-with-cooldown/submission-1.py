from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(index, can_buy):
            # nếu mà quá prices thì là trả về 0
            if index >= len(prices) : return 0
            if can_buy == True: 
                profit = dfs(index + 1, False) - prices[index]
                stay = dfs(index + 1, True)
                res = max(profit, stay)
            else :
                profit = prices[index] + dfs(index + 2, True)
                stay = dfs(index + 1, False)
                res = max(profit, stay)
            return res
        return dfs(0,True)
