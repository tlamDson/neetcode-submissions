class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first = 0
        second = 0
        for i in range(2,n + 1):
            current = min(first + cost[i-1],second + cost[i-2])
            print(current)
            second = first
            first = current
            print(first)
            print(second)
        return first
       
        
     