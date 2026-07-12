class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # why we use prefix sum here that is the question
        # [1,1,2,8]
        # [48,24,6,1]
        n = len(nums)
        res = [1]*n
        prefix =1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res