class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            curr = 0
            curr_days = 1
            for w in weights:
                if curr + w > mid:
                    curr_days += 1
                    curr = 0
                curr += w

            if curr_days <= days:
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1
        return ans

                
            
        