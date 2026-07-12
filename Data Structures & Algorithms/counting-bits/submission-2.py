class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            temp = i
            while temp >0:
                count += temp & 1
                temp >>= 1 
            res.append(count)
        return res
                
            
        
        
        