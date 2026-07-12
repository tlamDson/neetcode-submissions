from bisect import bisect_left
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def check(k):
            if k == 0: return False
            total_hours = 0
            for p in piles:
                total_hours += (p + k -1) // k
            return total_hours <= h
        search_range = range(l,r + 1)
        ans = bisect_left(search_range,True, key = check)
        return search_range[ans]
                
         