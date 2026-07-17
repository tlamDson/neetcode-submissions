class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        for i in range(n):
            curr = first + second
            first = second
            second = curr
        return second

        