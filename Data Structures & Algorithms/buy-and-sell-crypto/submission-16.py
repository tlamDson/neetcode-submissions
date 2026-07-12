class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 
        curr_max = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r 
            else:
                curr_max = max(curr_max, prices[r] - prices[l])
            r += 1
        return curr_max

        