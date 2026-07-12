from bisect import bisect_left
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        def check(mid):
            return nums[mid] >= target
        search_range = range(left,right + 1)
        ans_index = bisect_left(search_range, True, key = check)
        return ans_index
        
                
        