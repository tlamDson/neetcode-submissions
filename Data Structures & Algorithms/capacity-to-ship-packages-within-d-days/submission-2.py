from bisect import bisect_left
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def check(capacity):
            curr_days= 1
            curr_load = 0
            for w in weights:
                if curr_load + w > capacity:
                    curr_days += 1
                    curr_load = 0
                curr_load += w
            return curr_days <= days
        range_index = range(l,r+ 1)
        ans = bisect_left(range_index,True, key = check)
        return range_index[ans]

                
            
        