class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c_num = set()
        for num in nums:
            if num in c_num:
                return True
            c_num.add(num)
        return False
        
        