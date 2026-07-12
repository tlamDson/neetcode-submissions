class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        greedy = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                greedy += prices[i] - prices[i-1]
        return greedy