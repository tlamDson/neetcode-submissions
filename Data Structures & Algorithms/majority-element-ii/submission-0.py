class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major = {}
        res= []
        n = len(nums) /3

        for num in nums:
            major[num] = major.get(num,0) + 1
        for k,v in major.items():
            if v > n:
                res.append(k)
        return res
        
        