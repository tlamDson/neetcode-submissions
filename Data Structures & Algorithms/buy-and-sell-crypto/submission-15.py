class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxP = 0
        while r < len(prices):
            current = prices[r] - prices[l]
            if current < 0:
                l = r
            else:
                maxP = max(maxP,current)
            r += 1
        return maxP
        
            
            
 


            
                
       
            
            
            
 
                
            
            
            
       
       