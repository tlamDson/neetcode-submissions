class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # lưu vào dict
        # nếu mà cái 7 - 4 = 3 thì return thôi lưu thêm index để trả về
        if not nums: return []
        my_dict = {}
        for index, num in enumerate(nums):
            if target - num in my_dict:
                return [my_dict[target-num], index]
            my_dict[num] = index
        return []
            
        