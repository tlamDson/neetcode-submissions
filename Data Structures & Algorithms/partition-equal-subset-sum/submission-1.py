class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return False
        if sum(nums) % 2 == 1: return False

        nums.sort()
        n = len(nums)
        target = sum(nums) // 2
        dp = [0] * (target + 1)
        
        for i in range(n):
            w = nums[i]
            v = nums[i]
            
            for j in range(target, w - 1, -1):
                dp[j] = max(dp[j], dp[j - w] + v)
                
        return True if dp[target] == target else False
                    

        




