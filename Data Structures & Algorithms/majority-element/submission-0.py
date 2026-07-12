class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        for key,index in count.items():
            if index > len(nums) / 2:
                return key
        
        