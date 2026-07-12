class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dict = {}
        for index,key in enumerate(nums):
            if nums[index] in dict:
                return True
            dict[key] = index
        return False
            
        
        
        
       

        
