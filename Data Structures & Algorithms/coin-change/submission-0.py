class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(1,amount + 1):
                if j - coins[i] < 0:
                    continue
                dp[j] = min(dp[j], 1 + dp[j - coins[i]]) 
        return dp[amount] if dp[amount] != float('inf') else -1
        