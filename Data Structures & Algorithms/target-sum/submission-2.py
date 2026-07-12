from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if (total_sum + target) % 2 != 0 or abs(target) > total_sum:
            return 0
        P = (total_sum + target) // 2
        n = len(nums)

        dp = [[0]*(P+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            current_num = nums[i-1]
            for j in range(P+1):
                dp[i][j] = dp[i-1][j]
                if j >= current_num:
                    dp[i][j] += dp[i-1][j-current_num]
        return dp[n][P]

            
            

                

        