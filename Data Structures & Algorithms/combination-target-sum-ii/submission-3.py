class Solution:
    def combinationSum2(self,candidates : List[int], target :int) -> List[List[int]]:
        self.res = []
        self.nums = sorted(candidates)
        self.target = target
        self.backtrack(0,[],0)
        return self.res
    def backtrack(self,start_index,path,current_sum):
        if current_sum == self.target:
            self.res.append(list(path))
            return
        for i in range(start_index,len(self.nums)):
            if current_sum + self.nums[i] > self.target: break
            if i > start_index and self.nums[i] == self.nums[i-1]  : continue

            path.append(self.nums[i])

            self.backtrack(i+1,path,current_sum + self.nums[i])
            path.pop()