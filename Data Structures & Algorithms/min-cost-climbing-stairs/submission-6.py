class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # công thức dp là cái top = min(cost1, cost2)
        # cost1 = dp[i-1] + cost[i-1]
        # cost2 = dp[i-2] + cost[i-2]
        # cost ch
        n = len(cost)
        dp = [-1]*(n+2)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+2):
            cost_1 = dp[i-1]
            cost_2 = dp[i-2]
            dp[i] = min(cost_1, cost_2) + cost[i-2]
        return min(dp[-1],dp[-2])
