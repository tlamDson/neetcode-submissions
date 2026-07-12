class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l = 0 
        current = 0
        minP = float('inf')

        for r in range(len(nums)):
            current += nums[r]
            while current >= target:
                minP = min(minP, r - l + 1)
                current -= nums[l]
                l += 1

        return minP if minP != float('inf') else 0
        