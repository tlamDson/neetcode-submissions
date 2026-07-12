class Solution:
    def countBits(self, n: int) -> List[int]:
        def to_binary_list(n):
            if n == 0: return "0"
            bits = []
            while n > 0:
                bits.append(str(n & 1))
                n >>= 1
            return "".join(bits[::-1])
        res = []
        for i in range(0,n+1):
            numBits = int(to_binary_list(i),2)
            count = 0
            while numBits:
                count += numBits & 1
                numBits >>= 1
            res.append(count)
        return res
                
            
        
        
        