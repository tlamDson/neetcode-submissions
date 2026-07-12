class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Initialization  
        res = []
        nums.sort()
        for i in range(len(nums) - 2 ):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i+1, len(nums) - 1
            while l < r :
                current_sum = nums[l] + nums[r]
                if current_sum == target : 
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1 
                    while r > l and nums[r] == nums[r+1]:
                        r -=1
                elif current_sum < target : 
                    l +=1 
                else: 
                    r -= 1
        return res 
       
        