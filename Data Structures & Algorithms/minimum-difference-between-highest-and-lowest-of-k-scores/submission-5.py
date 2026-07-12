class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1: return 0
        
        nums.sort()
        res = float('inf')
        
        # We only need to check windows of size k
        # The window starts at i and ends at i + k - 1
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            res = min(res, diff)
            
        return res