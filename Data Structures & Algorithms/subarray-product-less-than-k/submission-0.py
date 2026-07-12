class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1 : 
            return 0
        l = 0
        current_product = 1
        res = 0
        for r in range(len(nums)):
            current_product *= nums[r]
            while current_product >= k :
                current_product //= nums[l]
                l +=1 

            res += (r - l +1)

        return res
            
        
