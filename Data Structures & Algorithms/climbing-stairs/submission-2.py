class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1
        for i in range(n - 1):
            current = first + second
            first = second
            second = current
        return second
       
       
           
        