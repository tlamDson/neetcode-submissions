class Solution:
    def rob(self, nums: List[int]) -> int:
        # can rob cach 1 nha
        # dp formula : dp[i] = max(dp[i-1],dp[i-2])
        # case 1 : 1,1,3,3
        # dp = [1,1,4,4]
        # case 2 : [2,9,8,3,6]
        # dp = [2,9,10,12,16]
        # dp[i] = dp[i-2] + cost[i-2], dp[i-1]
        n = len(nums)
        if n == 1: return nums[0]
        def rob1(nums):
            n = len(nums)
            dp = [-1]*(n+2)
            dp[0] = 0
            dp[1] = 0
            for i in range(2,n+2):
                dp[i] = max(dp[i-2] + nums[i-2],dp[i-1])
            return dp[-1]
        return max(rob1(nums[0:n-1]),rob1(nums[1:n]))
        