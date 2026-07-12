class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            triplets = self.threeSum(nums[i + 1:],target - nums[i])
            for t in triplets:
                res.append([nums[i]] + t)
        return res
            
    def threeSum(self, nums: List[int],target : int) -> List[List[int]]:
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i +1, len(nums) - 1
            while l < r:
                current = nums[i] + nums[l] + nums[r]
                if current == target:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -=1
                    l +=1
                    r -=1
                elif current < target:
                    l += 1
                else:
                    r -=1
                    
        return res