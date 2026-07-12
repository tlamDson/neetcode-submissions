class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first = 0
        second = 0
        for i in range(2, n + 1):
            current = min(first + cost[i-2],second + cost[i-1])

            first = second
            second = current
        return second
        