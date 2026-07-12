class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robHouse(nums,1,len(nums)),self.robHouse(nums,0,len(nums)-1))
    
    def robHouse(self,nums : List[int],start : int, end :int) -> int:

        
        rob1,rob2 = 0,0
        for i in range(start,end):
            temp = max(nums[i] + rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

           
            
           
        