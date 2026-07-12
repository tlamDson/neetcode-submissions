class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict={}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                return True
            my_dict[nums[i]] = i
        return False
    
                