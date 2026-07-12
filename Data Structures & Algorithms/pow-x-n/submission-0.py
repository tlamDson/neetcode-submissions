from functools import lru_cache
class Solution:
    @lru_cache(None)
    def myPow(self, x: float, n: int) -> float:
        return x ** n 
        


        