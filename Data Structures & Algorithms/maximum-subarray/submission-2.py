class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        glob_max = nums[0]
        curr_max = nums[0]
        
        n = len(nums)
        for i in range(1, len(nums)):
            num = nums[i]
            curr_max = max(num, curr_max + num)
            glob_max = max(glob_max, curr_max)
        return glob_max

        
        