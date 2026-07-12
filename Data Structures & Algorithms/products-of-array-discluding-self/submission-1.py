class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_array = []
        for i in range(len(nums)):
            copy_array = nums.copy()
            copy_array.pop(i)
            product = 1
            for num in copy_array:
                product = product*num
            new_array.append(product)
        return new_array     