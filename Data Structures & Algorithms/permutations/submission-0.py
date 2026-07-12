class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        self.used = [False] * len(nums)   
        self.backtrack([])
     
        return self.res
    def backtrack(self,path,):
        if len(path) == len(self.nums) :
            self.res.append(list(path))
            return
        for i in range(len(self.nums)):
            if self.used[i] == True:
                continue
            path.append(self.nums[i])
            self.used[i] = True
            
            self.backtrack(path)
            self.used[i] = False

            path.pop()

        