class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def dp(nums,start,end):
            nums = nums[start:end]
            n = len(nums)
            if len(nums) == 1: return nums[0]
            dp = [0]*(n+2)
            for i in range(2,n+2):
                dp[i] = max(dp[i-1],dp[i-2] + nums[i-2])
            return dp[-1]
        return max(dp(nums,0,len(nums)-1),dp(nums,1,len(nums)))
