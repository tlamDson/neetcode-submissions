class Solution:
    def climbStairs(self, n: int) -> int:
        def step(num, cache):
            if num <= 2:
                return num
            if num in cache:
                return cache[num]
            cache[num] = step(num-1,cache) + step(num-2,cache)
            return cache[num]
        return step(n,{})