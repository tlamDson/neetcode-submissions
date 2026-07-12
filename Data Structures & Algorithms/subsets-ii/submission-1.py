class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.n = n
        self.nums = nums
        nums.sort()
        self.res = []
        self.backtrack(0,[],nums)
        return self.res
    def backtrack(self,i,path,nums):
        if i == self.n:
            self.res.append(path[:])
            return
     
        path.append(nums[i])
        self.backtrack(i+1,path,nums)
        path.pop()
        while i + 1 < self.n and nums[i] == nums[i+1]:
            i+=1
        self.backtrack(i+1,path,nums)

    
    





        