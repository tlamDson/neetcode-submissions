class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums) # this is o(n)
        left_sum = 0
        for i, val in enumerate(nums):
            right_sum = total_sum - left_sum - val

            if right_sum == left_sum:
                return i 
            left_sum += val
        return -1
            
