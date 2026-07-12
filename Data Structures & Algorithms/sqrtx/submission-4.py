from bisect import bisect_left
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        if x < 2: return x
        def check(mid):
            return mid*mid > x
        search_range = range(low,high + 1)
        ans_index = bisect_left(search_range,True, key = check)
        return search_range[ans_index] - 1
      